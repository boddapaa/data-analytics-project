"""
Generate Plots Script
This script generates various visualizations from the sales data and saves them to the plots folder.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


def ensure_plots_directory():
    """Create plots directory if it doesn't exist"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    plots_dir = os.path.join(project_root, 'plots')
    os.makedirs(plots_dir, exist_ok=True)
    return plots_dir


def load_data():
    """Load the sales data from CSV"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(project_root, 'data', 'sample_sales_data.csv')
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])
    return df


def plot_sales_by_category(df, plots_dir):
    """Generate bar plot of total sales by category"""
    plt.figure(figsize=(10, 6))
    category_sales = df.groupby('category')['sales'].sum().sort_values(ascending=False)
    
    ax = category_sales.plot(kind='bar', color='steelblue')
    plt.title('Total Sales by Category', fontsize=16, fontweight='bold')
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Total Sales ($)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save plot
    output_path = os.path.join(plots_dir, 'sales_by_category.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    plt.close()


def plot_sales_by_region(df, plots_dir):
    """Generate pie chart of sales distribution by region"""
    plt.figure(figsize=(10, 8))
    region_sales = df.groupby('region')['sales'].sum()
    
    colors = plt.cm.Set3(range(len(region_sales)))
    plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', 
            colors=colors, startangle=90)
    plt.title('Sales Distribution by Region', fontsize=16, fontweight='bold')
    plt.axis('equal')
    
    # Save plot
    output_path = os.path.join(plots_dir, 'sales_by_region.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    plt.close()


def plot_sales_trend(df, plots_dir):
    """Generate line plot of sales over time"""
    plt.figure(figsize=(12, 6))
    daily_sales = df.groupby('date')['sales'].sum().sort_index()
    
    plt.plot(daily_sales.index, daily_sales.values, marker='o', 
             linewidth=2, markersize=4, color='darkblue')
    plt.title('Daily Sales Trend', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Total Sales ($)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save plot
    output_path = os.path.join(plots_dir, 'sales_trend.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    plt.close()


def plot_top_products(df, plots_dir):
    """Generate horizontal bar plot of top products by sales"""
    plt.figure(figsize=(10, 8))
    product_sales = df.groupby('product')['sales'].sum().sort_values(ascending=True)
    
    ax = product_sales.plot(kind='barh', color='coral')
    plt.title('Top Products by Total Sales', fontsize=16, fontweight='bold')
    plt.xlabel('Total Sales ($)', fontsize=12)
    plt.ylabel('Product', fontsize=12)
    plt.tight_layout()
    
    # Save plot
    output_path = os.path.join(plots_dir, 'top_products.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    plt.close()


def plot_category_region_heatmap(df, plots_dir):
    """Generate heatmap of sales by category and region"""
    plt.figure(figsize=(10, 6))
    
    # Create pivot table
    pivot_data = df.pivot_table(values='sales', index='category', 
                                 columns='region', aggfunc='sum', fill_value=0)
    
    sns.heatmap(pivot_data, annot=True, fmt='.0f', cmap='YlOrRd', 
                linewidths=0.5, cbar_kws={'label': 'Total Sales ($)'})
    plt.title('Sales Heatmap: Category vs Region', fontsize=16, fontweight='bold')
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Category', fontsize=12)
    plt.tight_layout()
    
    # Save plot
    output_path = os.path.join(plots_dir, 'category_region_heatmap.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    plt.close()


def plot_quantity_vs_sales(df, plots_dir):
    """Generate scatter plot of quantity vs sales"""
    plt.figure(figsize=(10, 6))
    
    colors = {'Electronics': 'blue', 'Furniture': 'green'}
    for category in df['category'].unique():
        category_data = df[df['category'] == category]
        plt.scatter(category_data['quantity'], category_data['sales'], 
                   label=category, alpha=0.6, s=100, color=colors.get(category, 'gray'))
    
    plt.title('Quantity vs Sales by Category', fontsize=16, fontweight='bold')
    plt.xlabel('Quantity', fontsize=12)
    plt.ylabel('Sales ($)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save plot
    output_path = os.path.join(plots_dir, 'quantity_vs_sales.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_path}")
    plt.close()


def generate_all_plots():
    """Generate all plots and save to plots directory"""
    print("Loading data...")
    df = load_data()
    
    print("Creating plots directory...")
    plots_dir = ensure_plots_directory()
    
    print("\nGenerating visualizations...")
    plot_sales_by_category(df, plots_dir)
    plot_sales_by_region(df, plots_dir)
    plot_sales_trend(df, plots_dir)
    plot_top_products(df, plots_dir)
    plot_category_region_heatmap(df, plots_dir)
    plot_quantity_vs_sales(df, plots_dir)
    
    print(f"\n✓ All plots saved to: {plots_dir}")
    print(f"✓ Total plots generated: 6")


if __name__ == "__main__":
    generate_all_plots()
