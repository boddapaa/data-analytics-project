"""
SQL Queries for Data Extraction
This module contains SQL queries for extracting data from databases.
"""

# Sample SQL queries for common data extraction tasks

# Query 1: Get total sales by product
TOTAL_SALES_BY_PRODUCT = """
SELECT 
    product,
    SUM(sales) as total_sales,
    SUM(quantity) as total_quantity,
    COUNT(*) as transaction_count
FROM sales_data
GROUP BY product
ORDER BY total_sales DESC;
"""

# Query 2: Get sales by region
SALES_BY_REGION = """
SELECT 
    region,
    SUM(sales) as total_sales,
    SUM(quantity) as total_quantity,
    AVG(sales) as avg_sales
FROM sales_data
GROUP BY region
ORDER BY total_sales DESC;
"""

# Query 3: Get sales by category
SALES_BY_CATEGORY = """
SELECT 
    category,
    SUM(sales) as total_sales,
    COUNT(DISTINCT product) as product_count,
    AVG(sales) as avg_sales_per_transaction
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;
"""

# Query 4: Get monthly sales trends
MONTHLY_SALES_TREND = """
SELECT 
    DATE_TRUNC('month', date) as month,
    SUM(sales) as total_sales,
    SUM(quantity) as total_quantity,
    COUNT(*) as transaction_count
FROM sales_data
GROUP BY DATE_TRUNC('month', date)
ORDER BY month;
"""

# Query 5: Get top performing products
TOP_PRODUCTS = """
SELECT 
    product,
    category,
    SUM(sales) as total_sales,
    SUM(quantity) as total_quantity
FROM sales_data
GROUP BY product, category
ORDER BY total_sales DESC
LIMIT 10;
"""

# Query 6: Get regional performance with category breakdown
REGIONAL_CATEGORY_PERFORMANCE = """
SELECT 
    region,
    category,
    SUM(sales) as total_sales,
    SUM(quantity) as total_quantity,
    AVG(sales) as avg_sales
FROM sales_data
GROUP BY region, category
ORDER BY region, total_sales DESC;
"""

# Function to execute queries (example with SQLAlchemy)
def execute_query(engine, query):
    """
    Execute a SQL query using SQLAlchemy engine
    
    Args:
        engine: SQLAlchemy engine object
        query: SQL query string
    
    Returns:
        pandas DataFrame with query results
    """
    import pandas as pd
    return pd.read_sql_query(query, engine)


# Example usage with SQLite
def create_sample_database():
    """
    Create a sample SQLite database from CSV data
    """
    import pandas as pd
    from sqlalchemy import create_engine
    import os
    
    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(project_root, 'data', 'sample_sales_data.csv')
    db_path = os.path.join(project_root, 'data', 'sales_database.db')
    
    # Read CSV
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])
    
    # Create SQLite database
    engine = create_engine(f'sqlite:///{db_path}')
    df.to_sql('sales_data', engine, if_exists='replace', index=False)
    
    print(f"Database created at: {db_path}")
    return engine


if __name__ == "__main__":
    # Create sample database
    engine = create_sample_database()
    
    # Execute sample queries
    print("\n=== Total Sales by Product ===")
    result = execute_query(engine, TOTAL_SALES_BY_PRODUCT)
    print(result)
    
    print("\n=== Sales by Region ===")
    result = execute_query(engine, SALES_BY_REGION)
    print(result)
    
    print("\n=== Sales by Category ===")
    result = execute_query(engine, SALES_BY_CATEGORY)
    print(result)
