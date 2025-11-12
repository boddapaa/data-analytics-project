# Data Analytics Project

Python-based data analytics project for cleaning, analyzing, and visualizing business data.

## Overview

This project demonstrates comprehensive data analysis techniques including:
- **Data Loading**: Load datasets from seaborn's built-in datasets
- **Data Cleaning**: Handle missing values, outliers, and duplicates
- **Exploratory Data Analysis**: Summary statistics and correlation analysis
- **Data Visualization**: Create insightful visualizations using matplotlib and seaborn

## Features

- 🔍 **Data Exploration**: Automatic dataset profiling with shape, types, and missing value analysis
- 🧹 **Data Cleaning**: 
  - Remove duplicate rows
  - Handle missing values (median for numerical, mode for categorical)
  - Detect and cap outliers using IQR method
- 📊 **Statistical Analysis**: 
  - Summary statistics for all numerical columns
  - Correlation matrix with strong correlation detection
  - Categorical variable distribution analysis
- 📈 **Visualizations**:
  - Distribution plots with KDE for numerical variables
  - Correlation heatmap
  - Box plots for outlier visualization
  - Categorical variable distributions
  - Pairplot for numerical variable relationships

## Requirements

- Python 3.8+
- pandas >= 2.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- scikit-learn >= 1.3.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/boddapaa/data-analytics-project.git
cd data-analytics-project
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main analysis script:
```bash
python data_analysis.py
```

The script will:
1. Load the 'tips' dataset from seaborn
2. Display dataset information
3. Clean the data
4. Perform exploratory data analysis
5. Generate visualizations

### Using Different Datasets

You can modify the script to use different seaborn datasets by changing the dataset name:

```python
# Available datasets: 'tips', 'iris', 'titanic', 'diamonds', 'fmri', 'penguins', etc.
analyzer = DataAnalyzer(dataset_name='iris')
```

### Programmatic Usage

You can also use the `DataAnalyzer` class in your own scripts:

```python
from data_analysis import DataAnalyzer

# Initialize with a dataset
analyzer = DataAnalyzer(dataset_name='tips')

# Run complete analysis pipeline
analyzer.run_complete_analysis()

# Or run individual steps
analyzer.load_data()
analyzer.display_data_info()
analyzer.clean_data()
analyzer.exploratory_analysis()
analyzer.visualize_data()
```

## Output Files

The script generates the following visualization files:
- `distributions.png` - Distribution plots for all numerical variables
- `correlation_heatmap.png` - Heatmap showing correlations between numerical variables
- `boxplots.png` - Box plots for outlier detection
- `categorical_distributions.png` - Bar charts for categorical variables
- `pairplot.png` - Pairwise relationships between numerical variables

## Project Structure

```
data-analytics-project/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── data_analysis.py             # Main analysis script
├── .gitignore                   # Git ignore file
├── distributions.png            # Generated visualization (not committed)
├── correlation_heatmap.png      # Generated visualization (not committed)
├── boxplots.png                 # Generated visualization (not committed)
├── categorical_distributions.png # Generated visualization (not committed)
└── pairplot.png                 # Generated visualization (not committed)
```

## Key Components

### DataAnalyzer Class

The main class that orchestrates the entire analysis pipeline:

- **`load_data()`**: Loads data from seaborn datasets
- **`display_data_info()`**: Shows dataset information, types, and missing values
- **`clean_data()`**: Performs data cleaning operations
- **`exploratory_analysis()`**: Conducts statistical analysis
- **`visualize_data()`**: Creates comprehensive visualizations
- **`run_complete_analysis()`**: Executes the complete analysis pipeline

## Data Cleaning Strategy

1. **Duplicate Removal**: Identifies and removes duplicate rows
2. **Missing Value Handling**:
   - Numerical columns: Filled with median
   - Categorical columns: Filled with mode
3. **Outlier Detection**: Uses IQR (Interquartile Range) method
   - Outliers are capped rather than removed to preserve data
   - Bounds: Q1 - 1.5×IQR to Q3 + 1.5×IQR

## Example Output

```
============================================================
DATA ANALYTICS PROJECT
============================================================

Loading 'tips' dataset from seaborn...
✓ Data loaded successfully! Shape: (244, 7)

============================================================
DATASET INFORMATION
============================================================
Dataset Shape: (244, 7)
Number of rows: 244
Number of columns: 7

============================================================
DATA CLEANING
============================================================
✓ Removed 1 duplicate rows
✓ Handled 0 missing values
✓ Capped 26 outlier values

============================================================
EXPLORATORY DATA ANALYSIS
============================================================
--- Strong Correlations (|correlation| > 0.5) ---
  total_bill <-> tip: 0.654
  total_bill <-> size: 0.613
```

## Technologies Used

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Basic plotting and visualization
- **seaborn**: Statistical data visualization
- **scikit-learn**: Machine learning utilities (StandardScaler)

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available for educational purposes.
