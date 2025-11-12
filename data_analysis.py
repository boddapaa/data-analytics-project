"""
Data Analytics Project - Main Analysis Script

This script performs comprehensive data analysis including:
- Data loading from seaborn datasets
- Data cleaning (missing values, outliers, duplicates)
- Exploratory data analysis with statistics and correlations
- Data visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)


class DataAnalyzer:
    """A class to perform comprehensive data analysis."""
    
    def __init__(self, dataset_name='tips'):
        """
        Initialize the DataAnalyzer with a dataset.
        
        Args:
            dataset_name (str): Name of the seaborn dataset to load.
                              Options: 'tips', 'iris', 'titanic', 'diamonds', etc.
        """
        self.dataset_name = dataset_name
        self.df = None
        self.df_cleaned = None
        
    def load_data(self):
        """Load data from seaborn datasets."""
        print(f"Loading '{self.dataset_name}' dataset from seaborn...")
        try:
            self.df = sns.load_dataset(self.dataset_name)
            print(f"✓ Data loaded successfully! Shape: {self.df.shape}")
            print(f"\nFirst few rows:")
            print(self.df.head())
            return self.df
        except Exception as e:
            print(f"✗ Error loading dataset: {e}")
            return None
    
    def display_data_info(self):
        """Display basic information about the dataset."""
        if self.df is None:
            print("No data loaded. Please load data first.")
            return
        
        print("\n" + "="*60)
        print("DATASET INFORMATION")
        print("="*60)
        print(f"\nDataset Shape: {self.df.shape}")
        print(f"Number of rows: {self.df.shape[0]}")
        print(f"Number of columns: {self.df.shape[1]}")
        
        print("\n--- Data Types ---")
        print(self.df.dtypes)
        
        print("\n--- Missing Values ---")
        missing = self.df.isnull().sum()
        missing_pct = (missing / len(self.df)) * 100
        missing_df = pd.DataFrame({
            'Missing Count': missing,
            'Percentage': missing_pct
        })
        print(missing_df[missing_df['Missing Count'] > 0])
        
        print("\n--- Duplicate Rows ---")
        duplicates = self.df.duplicated().sum()
        print(f"Number of duplicate rows: {duplicates}")
    
    def clean_data(self):
        """
        Perform data cleaning operations:
        - Handle missing values
        - Remove duplicates
        - Handle outliers
        """
        if self.df is None:
            print("No data loaded. Please load data first.")
            return
        
        print("\n" + "="*60)
        print("DATA CLEANING")
        print("="*60)
        
        # Create a copy for cleaning
        self.df_cleaned = self.df.copy()
        
        # 1. Handle duplicates
        duplicates_before = self.df_cleaned.duplicated().sum()
        self.df_cleaned = self.df_cleaned.drop_duplicates()
        duplicates_after = self.df_cleaned.duplicated().sum()
        print(f"\n✓ Removed {duplicates_before - duplicates_after} duplicate rows")
        
        # 2. Handle missing values
        missing_before = self.df_cleaned.isnull().sum().sum()
        
        # For numerical columns: fill with median
        numerical_cols = self.df_cleaned.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            if self.df_cleaned[col].isnull().sum() > 0:
                median_val = self.df_cleaned[col].median()
                self.df_cleaned[col].fillna(median_val, inplace=True)
                print(f"  - Filled missing values in '{col}' with median: {median_val:.2f}")
        
        # For categorical columns: fill with mode
        categorical_cols = self.df_cleaned.select_dtypes(include=['object', 'category']).columns
        for col in categorical_cols:
            if self.df_cleaned[col].isnull().sum() > 0:
                mode_val = self.df_cleaned[col].mode()[0] if not self.df_cleaned[col].mode().empty else 'Unknown'
                self.df_cleaned[col].fillna(mode_val, inplace=True)
                print(f"  - Filled missing values in '{col}' with mode: {mode_val}")
        
        missing_after = self.df_cleaned.isnull().sum().sum()
        print(f"\n✓ Handled {missing_before - missing_after} missing values")
        
        # 3. Handle outliers using IQR method for numerical columns
        print("\n--- Outlier Detection (IQR Method) ---")
        outliers_removed = 0
        
        for col in numerical_cols:
            Q1 = self.df_cleaned[col].quantile(0.25)
            Q3 = self.df_cleaned[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = ((self.df_cleaned[col] < lower_bound) | (self.df_cleaned[col] > upper_bound)).sum()
            if outliers > 0:
                print(f"  - '{col}': {outliers} outliers detected (bounds: [{lower_bound:.2f}, {upper_bound:.2f}])")
                # Cap outliers instead of removing them to preserve data
                self.df_cleaned[col] = self.df_cleaned[col].clip(lower_bound, upper_bound)
                outliers_removed += outliers
        
        print(f"\n✓ Capped {outliers_removed} outlier values")
        print(f"\nCleaned data shape: {self.df_cleaned.shape}")
        
        return self.df_cleaned
    
    def exploratory_analysis(self):
        """Perform exploratory data analysis with summary statistics."""
        if self.df_cleaned is None:
            print("No cleaned data available. Please clean data first.")
            return
        
        print("\n" + "="*60)
        print("EXPLORATORY DATA ANALYSIS")
        print("="*60)
        
        # Summary statistics
        print("\n--- Summary Statistics ---")
        print(self.df_cleaned.describe())
        
        # Numerical columns analysis
        numerical_cols = self.df_cleaned.select_dtypes(include=[np.number]).columns
        
        if len(numerical_cols) > 0:
            print("\n--- Correlation Matrix ---")
            correlation_matrix = self.df_cleaned[numerical_cols].corr()
            print(correlation_matrix)
            
            # Find strong correlations
            print("\n--- Strong Correlations (|correlation| > 0.5) ---")
            for i in range(len(correlation_matrix.columns)):
                for j in range(i+1, len(correlation_matrix.columns)):
                    corr_val = correlation_matrix.iloc[i, j]
                    if abs(corr_val) > 0.5:
                        col1 = correlation_matrix.columns[i]
                        col2 = correlation_matrix.columns[j]
                        print(f"  {col1} <-> {col2}: {corr_val:.3f}")
        
        # Categorical columns analysis
        categorical_cols = self.df_cleaned.select_dtypes(include=['object', 'category']).columns
        
        if len(categorical_cols) > 0:
            print("\n--- Categorical Variables ---")
            for col in categorical_cols:
                print(f"\n{col}:")
                print(self.df_cleaned[col].value_counts())
    
    def visualize_data(self):
        """Create comprehensive visualizations of the data."""
        if self.df_cleaned is None:
            print("No cleaned data available. Please clean data first.")
            return
        
        print("\n" + "="*60)
        print("DATA VISUALIZATION")
        print("="*60)
        
        numerical_cols = self.df_cleaned.select_dtypes(include=[np.number]).columns
        categorical_cols = self.df_cleaned.select_dtypes(include=['object', 'category']).columns
        
        # 1. Distribution plots for numerical variables
        if len(numerical_cols) > 0:
            n_cols = min(3, len(numerical_cols))
            n_rows = (len(numerical_cols) + n_cols - 1) // n_cols
            
            fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
            if n_rows == 1 and n_cols == 1:
                axes = [axes]
            else:
                axes = axes.flatten() if n_rows > 1 else axes
            
            for idx, col in enumerate(numerical_cols):
                ax = axes[idx] if len(numerical_cols) > 1 else axes[0]
                sns.histplot(data=self.df_cleaned, x=col, kde=True, ax=ax)
                ax.set_title(f'Distribution of {col}')
                ax.set_xlabel(col)
                ax.set_ylabel('Frequency')
            
            # Hide extra subplots
            for idx in range(len(numerical_cols), len(axes)):
                fig.delaxes(axes[idx])
            
            plt.tight_layout()
            plt.savefig('distributions.png', dpi=300, bbox_inches='tight')
            print("✓ Saved distribution plots to 'distributions.png'")
            plt.close()
        
        # 2. Correlation heatmap
        if len(numerical_cols) > 1:
            plt.figure(figsize=(10, 8))
            correlation_matrix = self.df_cleaned[numerical_cols].corr()
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                       square=True, linewidths=1, cbar_kws={"shrink": 0.8})
            plt.title('Correlation Heatmap')
            plt.tight_layout()
            plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
            print("✓ Saved correlation heatmap to 'correlation_heatmap.png'")
            plt.close()
        
        # 3. Box plots for outlier visualization
        if len(numerical_cols) > 0:
            n_cols = min(3, len(numerical_cols))
            n_rows = (len(numerical_cols) + n_cols - 1) // n_cols
            
            fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
            if n_rows == 1 and n_cols == 1:
                axes = [axes]
            else:
                axes = axes.flatten() if n_rows > 1 else axes
            
            for idx, col in enumerate(numerical_cols):
                ax = axes[idx] if len(numerical_cols) > 1 else axes[0]
                sns.boxplot(data=self.df_cleaned, y=col, ax=ax)
                ax.set_title(f'Box Plot of {col}')
                ax.set_ylabel(col)
            
            # Hide extra subplots
            for idx in range(len(numerical_cols), len(axes)):
                fig.delaxes(axes[idx])
            
            plt.tight_layout()
            plt.savefig('boxplots.png', dpi=300, bbox_inches='tight')
            print("✓ Saved box plots to 'boxplots.png'")
            plt.close()
        
        # 4. Categorical variable plots
        if len(categorical_cols) > 0:
            n_plots = min(4, len(categorical_cols))
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))
            axes = axes.flatten()
            
            for idx, col in enumerate(categorical_cols[:n_plots]):
                value_counts = self.df_cleaned[col].value_counts()
                axes[idx].bar(range(len(value_counts)), value_counts.values)
                axes[idx].set_xticks(range(len(value_counts)))
                axes[idx].set_xticklabels(value_counts.index, rotation=45, ha='right')
                axes[idx].set_title(f'Distribution of {col}')
                axes[idx].set_xlabel(col)
                axes[idx].set_ylabel('Count')
            
            # Hide extra subplots
            for idx in range(len(categorical_cols[:n_plots]), 4):
                fig.delaxes(axes[idx])
            
            plt.tight_layout()
            plt.savefig('categorical_distributions.png', dpi=300, bbox_inches='tight')
            print("✓ Saved categorical distributions to 'categorical_distributions.png'")
            plt.close()
        
        # 5. Pairplot for numerical variables (if not too many)
        if len(numerical_cols) >= 2 and len(numerical_cols) <= 5:
            print("\nCreating pairplot (this may take a moment)...")
            pairplot = sns.pairplot(self.df_cleaned[numerical_cols], diag_kind='kde')
            pairplot.fig.suptitle('Pairplot of Numerical Variables', y=1.02)
            plt.savefig('pairplot.png', dpi=300, bbox_inches='tight')
            print("✓ Saved pairplot to 'pairplot.png'")
            plt.close()
        
        print("\n✓ All visualizations completed!")
    
    def run_complete_analysis(self):
        """Run the complete data analysis pipeline."""
        print("\n" + "="*60)
        print("STARTING COMPLETE DATA ANALYSIS PIPELINE")
        print("="*60)
        
        # Step 1: Load data
        self.load_data()
        if self.df is None:
            return
        
        # Step 2: Display data information
        self.display_data_info()
        
        # Step 3: Clean data
        self.clean_data()
        
        # Step 4: Exploratory analysis
        self.exploratory_analysis()
        
        # Step 5: Visualize data
        self.visualize_data()
        
        print("\n" + "="*60)
        print("ANALYSIS COMPLETE!")
        print("="*60)
        print("\nGenerated files:")
        print("  - distributions.png")
        print("  - correlation_heatmap.png")
        print("  - boxplots.png")
        print("  - categorical_distributions.png")
        print("  - pairplot.png (if applicable)")


def main():
    """Main function to run the data analysis."""
    print("="*60)
    print("DATA ANALYTICS PROJECT")
    print("="*60)
    print("\nThis project demonstrates comprehensive data analysis including:")
    print("  • Data loading from seaborn datasets")
    print("  • Data cleaning (missing values, outliers, duplicates)")
    print("  • Exploratory data analysis")
    print("  • Data visualization")
    print()
    
    # Initialize analyzer with the 'tips' dataset (can be changed to 'iris', 'titanic', etc.)
    analyzer = DataAnalyzer(dataset_name='tips')
    
    # Run complete analysis
    analyzer.run_complete_analysis()


if __name__ == "__main__":
    main()
