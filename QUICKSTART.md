# Quick Start Guide

Get started with the Data Analytics Project in just a few steps!

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/boddapaa/data-analytics-project.git
   cd data-analytics-project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Running the Project

### Option 1: Generate All Visualizations

Generate all plots and save them to `/plots`:

```bash
cd scripts
python generate_plots.py
```

**Output:** 6 PNG files in the `/plots` directory

---

### Option 2: Launch Interactive Dashboard

Start the Streamlit dashboard for interactive exploration:

```bash
cd scripts
streamlit run dashboard.py
```

**Access:** Open `http://localhost:8501` in your browser

**Features:**
- Interactive filters (date, category, region)
- Real-time visualization updates
- Multiple analysis tabs
- Download filtered data

---

### Option 3: Export Data for BI Tools

Create export files for Power BI and Tableau:

```bash
cd scripts
python export_for_bi.py
```

**Output:** 
- Excel files with multiple sheets
- CSV files for quick import
- Data dictionary
- Pre-aggregated tables

**Location:** `/data/exports/`

---

### Option 4: Run SQL Queries

Execute SQL queries on the data:

```bash
cd scripts
python sql_queries.py
```

**Features:**
- Creates SQLite database
- Runs sample analytics queries
- Returns aggregated results

---

### Option 5: Jupyter Notebook Analysis

Open and run the exploratory analysis notebook:

```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

**Includes:**
- Step-by-step data analysis
- Statistical summaries
- Visualizations (saved to `/plots`)
- Key insights

---

## 📁 Project Structure Summary

```
├── data/                    # Data files and exports
├── notebooks/               # Jupyter notebooks
├── scripts/                 # Python scripts
├── plots/                   # Generated visualizations
├── requirements.txt         # Dependencies
└── README.md               # Full documentation
```

## 🎯 Quick Tasks

### Task 1: View All Generated Plots
```bash
ls -lh plots/
```

### Task 2: Check Export Files
```bash
ls -lh data/exports/
```

### Task 3: View Sample Data
```bash
head -10 data/sample_sales_data.csv
```

### Task 4: Run All Scripts
```bash
cd scripts
python generate_plots.py
python sql_queries.py
python export_for_bi.py
```

---

## 💡 Tips

1. **First time?** Start with `generate_plots.py` to see what the project can do
2. **Want interactivity?** Use `streamlit run dashboard.py`
3. **Need BI exports?** Run `export_for_bi.py`
4. **Prefer notebooks?** Open `exploratory_analysis.ipynb`

---

## 🆘 Troubleshooting

### Issue: ModuleNotFoundError
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Streamlit won't start
**Solution:** Install streamlit separately
```bash
pip install streamlit
```

### Issue: Plots not generating
**Solution:** Ensure matplotlib is installed
```bash
pip install matplotlib seaborn
```

---

## 📖 Next Steps

1. ✅ Run one of the scripts
2. ✅ View the generated outputs
3. ✅ Modify the sample data
4. ✅ Create your own visualizations
5. ✅ Read the full README.md

---

**Ready to start?** Pick any option above and run it! 🚀
