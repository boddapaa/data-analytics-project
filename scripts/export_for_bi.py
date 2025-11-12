"""
Export Data for Power BI and Tableau
This script prepares and exports data in formats suitable for Power BI and Tableau.
"""

import pandas as pd
import os
from datetime import datetime


def ensure_export_directory():
    """Create export directory if it doesn't exist"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    export_dir = os.path.join(project_root, 'data', 'exports')
    os.makedirs(export_dir, exist_ok=True)
    return export_dir


def load_and_prepare_data():
    """Load and prepare data for BI tools"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(project_root, 'data', 'sample_sales_data.csv')
    
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])
    
    # Add derived columns for better analysis
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.strftime('%B')
    df['quarter'] = df['date'].dt.quarter
    df['day_of_week'] = df['date'].dt.day_name()
    df['revenue'] = df['sales']  # Alias for clarity
    
    return df


def create_aggregated_tables(df):
    """Create pre-aggregated tables for faster BI tool performance"""
    
    # Sales by Product
    sales_by_product = df.groupby(['product', 'category']).agg({
        'sales': 'sum',
        'quantity': 'sum',
        'date': 'count'
    }).reset_index()
    sales_by_product.columns = ['product', 'category', 'total_sales', 'total_quantity', 'transaction_count']
    
    # Sales by Region
    sales_by_region = df.groupby(['region']).agg({
        'sales': 'sum',
        'quantity': 'sum',
        'date': 'count'
    }).reset_index()
    sales_by_region.columns = ['region', 'total_sales', 'total_quantity', 'transaction_count']
    
    # Monthly Sales
    monthly_sales = df.groupby(['year', 'month', 'month_name']).agg({
        'sales': 'sum',
        'quantity': 'sum'
    }).reset_index()
    monthly_sales.columns = ['year', 'month', 'month_name', 'total_sales', 'total_quantity']
    
    # Category-Region Matrix
    category_region = df.groupby(['category', 'region']).agg({
        'sales': 'sum',
        'quantity': 'sum'
    }).reset_index()
    category_region.columns = ['category', 'region', 'total_sales', 'total_quantity']
    
    return {
        'sales_by_product': sales_by_product,
        'sales_by_region': sales_by_region,
        'monthly_sales': monthly_sales,
        'category_region': category_region
    }


def export_for_power_bi(df, aggregated_tables, export_dir):
    """
    Export data for Power BI
    Power BI works well with Excel files and CSV files
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Export main dataset as Excel with multiple sheets
    excel_path = os.path.join(export_dir, f'powerbi_data_{timestamp}.xlsx')
    
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Raw_Data', index=False)
        aggregated_tables['sales_by_product'].to_excel(writer, sheet_name='Sales_by_Product', index=False)
        aggregated_tables['sales_by_region'].to_excel(writer, sheet_name='Sales_by_Region', index=False)
        aggregated_tables['monthly_sales'].to_excel(writer, sheet_name='Monthly_Sales', index=False)
        aggregated_tables['category_region'].to_excel(writer, sheet_name='Category_Region', index=False)
    
    print(f"✓ Power BI Export (Excel): {excel_path}")
    
    # Also export as CSV for alternative import method
    csv_path = os.path.join(export_dir, f'powerbi_data_{timestamp}.csv')
    df.to_csv(csv_path, index=False)
    print(f"✓ Power BI Export (CSV): {csv_path}")
    
    return excel_path, csv_path


def export_for_tableau(df, aggregated_tables, export_dir):
    """
    Export data for Tableau
    Tableau works well with CSV, Excel, and Hyper files
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Export main dataset as CSV (Tableau's preferred format for quick imports)
    csv_path = os.path.join(export_dir, f'tableau_data_{timestamp}.csv')
    df.to_csv(csv_path, index=False)
    print(f"✓ Tableau Export (CSV): {csv_path}")
    
    # Export as Excel with multiple sheets
    excel_path = os.path.join(export_dir, f'tableau_data_{timestamp}.xlsx')
    
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Raw_Data', index=False)
        aggregated_tables['sales_by_product'].to_excel(writer, sheet_name='Sales_by_Product', index=False)
        aggregated_tables['sales_by_region'].to_excel(writer, sheet_name='Sales_by_Region', index=False)
        aggregated_tables['monthly_sales'].to_excel(writer, sheet_name='Monthly_Sales', index=False)
        aggregated_tables['category_region'].to_excel(writer, sheet_name='Category_Region', index=False)
    
    print(f"✓ Tableau Export (Excel): {excel_path}")
    
    # Export individual aggregated tables as separate CSV files for Tableau relationships
    for table_name, table_df in aggregated_tables.items():
        table_csv_path = os.path.join(export_dir, f'tableau_{table_name}_{timestamp}.csv')
        table_df.to_csv(table_csv_path, index=False)
        print(f"✓ Tableau Export ({table_name}): {table_csv_path}")
    
    return csv_path, excel_path


def create_data_dictionary(df, export_dir):
    """Create a data dictionary for BI tools"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    data_dict = []
    for col in df.columns:
        data_dict.append({
            'Column Name': col,
            'Data Type': str(df[col].dtype),
            'Sample Values': ', '.join(df[col].astype(str).unique()[:3]),
            'Null Count': df[col].isnull().sum(),
            'Unique Values': df[col].nunique()
        })
    
    dict_df = pd.DataFrame(data_dict)
    dict_path = os.path.join(export_dir, f'data_dictionary_{timestamp}.xlsx')
    dict_df.to_excel(dict_path, index=False)
    print(f"✓ Data Dictionary: {dict_path}")
    
    return dict_path


def export_all():
    """Main function to export data for all BI tools"""
    print("=" * 60)
    print("Data Export for Power BI and Tableau")
    print("=" * 60)
    
    print("\n1. Loading and preparing data...")
    df = load_and_prepare_data()
    print(f"   ✓ Loaded {len(df)} records")
    
    print("\n2. Creating aggregated tables...")
    aggregated_tables = create_aggregated_tables(df)
    print(f"   ✓ Created {len(aggregated_tables)} aggregated tables")
    
    print("\n3. Creating export directory...")
    export_dir = ensure_export_directory()
    print(f"   ✓ Export directory: {export_dir}")
    
    print("\n4. Exporting for Power BI...")
    export_for_power_bi(df, aggregated_tables, export_dir)
    
    print("\n5. Exporting for Tableau...")
    export_for_tableau(df, aggregated_tables, export_dir)
    
    print("\n6. Creating data dictionary...")
    create_data_dictionary(df, export_dir)
    
    print("\n" + "=" * 60)
    print("✓ Export completed successfully!")
    print("=" * 60)
    print("\nHow to use the exports:")
    print("- Power BI: Import the Excel file or CSV file")
    print("- Tableau: Connect to CSV or Excel file")
    print("- Data Dictionary: Reference for column descriptions")
    print("=" * 60)


if __name__ == "__main__":
    export_all()
