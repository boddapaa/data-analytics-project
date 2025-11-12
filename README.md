# Data Analytics Project

Exploratory data analysis and dashboard reporting using Python (Pandas, Matplotlib, Plotly, Streamlit) and SQL to uncover business insights from real-world datasets.

## 📁 Project Structure

```
data-analytics-project/
├── data/                           # Data files
│   ├── sample_sales_data.csv      # Sample sales dataset
│   └── exports/                    # BI tool exports (Power BI/Tableau)
├── notebooks/                      # Jupyter notebooks
│   └── exploratory_analysis.ipynb # EDA notebook with visualizations
├── scripts/                        # Python scripts
│   ├── sql_queries.py             # SQL queries for data extraction
│   ├── generate_plots.py          # Generate and save visualizations
│   ├── export_for_bi.py           # Export data for Power BI/Tableau
│   └── dashboard.py               # Interactive Streamlit dashboard
├── plots/                          # Visual outputs (charts, graphs)
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 🚀 Features

### 1. **SQL Data Extraction**
- Pre-defined SQL queries for common analytics tasks
- Support for SQLite, PostgreSQL, MySQL, and other databases
- Automated database creation from CSV data
- Query templates for:
  - Sales by product, region, category
  - Time-series trends
  - Top performers analysis
  - Regional and categorical breakdowns

### 2. **Data Visualization**
All visualizations are automatically saved to the `/plots` folder:
- Sales by category (bar charts)
- Regional distribution (pie charts)
- Sales trends over time (line charts)
- Product performance (horizontal bar charts)
- Category-region heatmaps
- Quantity vs sales scatter plots

### 3. **Interactive Dashboard**
Built with Streamlit and Plotly for real-time data exploration:
- Interactive filters (date range, category, region)
- Key metrics dashboard
- Multiple visualization tabs:
  - Trends: Time series analysis
  - Performance: Product and category insights
  - Regional: Geographic analysis
  - Analysis: Advanced statistical views
- Download filtered data as CSV

### 4. **Power BI & Tableau Export**
Automated data export for business intelligence tools:
- Excel format with multiple sheets
- CSV format for quick imports
- Pre-aggregated tables for faster BI performance
- Data dictionary for column descriptions
- Export formats:
  - Raw transaction data
  - Sales by product
  - Sales by region
  - Monthly sales trends
  - Category-region matrix

## 📋 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Required packages:
- pandas >= 2.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- plotly >= 5.14.0
- streamlit >= 1.28.0
- openpyxl >= 3.1.0
- sqlalchemy >= 2.0.0

## 🎯 Usage

### 1. Generate Visualizations

Run the plot generation script to create all visualizations:

```bash
cd scripts
python generate_plots.py
```

This will create 6 visualization files in the `/plots` folder.

### 2. Run SQL Queries

Execute SQL queries to extract and analyze data:

```bash
cd scripts
python sql_queries.py
```

This creates a SQLite database and runs sample queries.

### 3. Launch Interactive Dashboard

Start the Streamlit dashboard:

```bash
cd scripts
streamlit run dashboard.py
```

Then open your browser to `http://localhost:8501`

### 4. Export for Power BI/Tableau

Generate export files for BI tools:

```bash
cd scripts
python export_for_bi.py
```

Files will be saved in `/data/exports/` directory.

### 5. Run Jupyter Notebook

Launch Jupyter and open the analysis notebook:

```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

## 📊 Data Description

The sample dataset (`sample_sales_data.csv`) contains sales transactions with:

- **date**: Transaction date
- **product**: Product name (Laptop, Mouse, Keyboard, Monitor, Desk, Chair)
- **category**: Product category (Electronics, Furniture)
- **sales**: Sales amount in dollars
- **quantity**: Quantity sold
- **region**: Geographic region (North, South, East, West)

## 🔍 Key Insights

The analysis provides insights on:
- Top performing products and categories
- Regional sales distribution
- Sales trends over time
- Product performance metrics
- Category-region relationships
- Statistical summaries

## 🛠️ Advanced Features

### SQL Query Templates

The `sql_queries.py` script includes:
- Total sales by product
- Sales by region
- Sales by category
- Monthly sales trends
- Top performing products
- Regional category performance

### Dashboard Capabilities

The interactive dashboard offers:
- Real-time filtering
- Multiple visualization types
- Drill-down capabilities
- Export functionality
- Responsive design

### BI Tool Integration

Export script creates:
- Multi-sheet Excel workbooks
- Optimized CSV files
- Pre-aggregated views
- Data dictionaries
- Timestamped exports

## 📈 Next Steps

To extend this project:
1. Add more data sources
2. Implement predictive analytics
3. Create additional SQL queries
4. Enhance dashboard with more KPIs
5. Integrate with cloud databases
6. Add automated reporting
7. Implement data quality checks

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional visualization types
- More SQL query templates
- Enhanced dashboard features
- New data sources
- Documentation improvements

## 📄 License

This project is open source and available for educational and commercial use.

---

**Built with:** Python, Pandas, Matplotlib, Seaborn, Plotly, Streamlit, SQL
