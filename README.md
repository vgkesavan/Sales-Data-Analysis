# Sales Data Analysis & Interactive Dashboard

**Tools:** Excel, SQL, Power BI (Python used for the data-prep/QA layer)

## Project Structure
```
sales_analysis/
├── clean_data.py              # Cleans raw data, validates fields, engineers columns
├── make_charts.py             # Generates dashboard-preview charts
├── data/
│   └── raw.xlsx                # Original raw sales export (900 orders)
├── sql/
│   └── sales_queries.sql      # 8 business queries (KPIs, trends, segmentation)
├── outputs/
│   ├── sales_clean.csv        # Cleaned data — import this into Power BI
│   ├── sales.db               # SQLite database used to run the SQL queries
│   ├── query_results.md       # All query results
│   └── insights_summary.md    # Written findings
├── charts/                     # 5 preview charts (category, trend, states, etc.)
└── POWERBI_GUIDE.md            # Step-by-step: build the live dashboard (~15 min)
```

## Pipeline
1. **Clean** — dedupe, standardize text, fix dtypes, validate that
   `Sales = Unit_Price × Quantity × (1 − Discount)` holds for every row,
   engineer `Order_Month`, `Order_Year`, `Profit_Margin_Pct`
2. **SQL** — 8 queries answering real business questions: overall KPIs,
   category/state performance, top products, monthly trend, payment mode
   mix, demographic breakdown, discount-vs-margin impact
3. **Power BI** — see `POWERBI_GUIDE.md` to turn `sales_clean.csv` into an
   interactive dashboard with KPI cards, charts, and cross-filtering slicers

## Completed deliverables
- `outputs/dashboard.html` — interactive Plotly dashboard preview with KPI cards,
  monthly trend, category mix, discount-margin analysis, payment mix, and a
  top-products table
- `run_pipeline.py` — one-command rebuild of the cleaned CSV, SQLite database,
  and five PNG charts
- `requirements.txt` — Python dependencies for reproducing the analysis

Run the reproducible pipeline from this folder:

```bash
python run_pipeline.py
```

The pipeline was validated against the included data: 900 rows, no duplicate
rows, no missing values, zero sales-calculation mismatches, and all 8 SQL
business queries execute successfully.

## Key Insight (see full report in outputs/insights_summary.md)
Electronics drives 77% of revenue from 30% of orders, and every 10% jump
in discount tier costs roughly 4-5 points of profit margin — a clear,
quantifiable signal for pricing strategy.
