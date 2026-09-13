# Building the Power BI Dashboard

You have `outputs/sales_clean.csv` — ready to import. This guide gets you
to a working, resume-worthy dashboard in about 15 minutes.

## 1. Import the data
1. Open Power BI Desktop → **Get Data → Text/CSV** → select `sales_clean.csv`
2. Click **Transform Data** to open Power Query, confirm:
   - `Order_Date` is typed as **Date**
   - `Sales`, `Cost`, `Profit`, `Unit_Price` are **Decimal Number**
   - `Discount`, `Profit_Margin_Pct` are **Decimal Number**
3. Click **Close & Apply**

## 2. Add KPI cards (top row)
Use the **Card** visual for each:
- Total Sales → `Sum(Sales)`
- Total Profit → `Sum(Profit)`
- Total Orders → `Count(Order_ID)`
- Avg Profit Margin % → `Average(Profit_Margin_Pct)`

## 3. Core visuals
| Visual | Type | Fields |
|---|---|---|
| Sales by Category | Bar chart | Axis: `Category`, Value: `Sum(Sales)` |
| Monthly Sales Trend | Line chart | Axis: `Order_Month`, Value: `Sum(Sales)` |
| Top 5 States | Bar chart | Axis: `State`, Value: `Sum(Sales)`, filter Top N = 5 |
| Payment Mode Share | Pie/Donut chart | Legend: `Payment_Mode`, Value: `Sum(Sales)` |
| Profit Margin by Discount Band | Column chart | Axis: `Discount` (grouped/binned), Value: `Average(Profit_Margin_Pct)` |
| Product Table | Table | `Product_Name`, `Category`, `Sum(Quantity)`, `Sum(Sales)` — sort descending |

## 4. Add slicers (interactivity — this is what makes it "interactive")
Add slicer visuals for:
- `Category`
- `State`
- `Order_Month` (or a date range slicer on `Order_Date`)
- `Payment_Mode`

These let you click a category/state/month and watch every visual filter
live — this single feature is what turns a set of static charts into an
"interactive dashboard" you can talk about in an interview.

## 5. Polish
- Rename the page tab to "Sales Overview"
- Add a title text box at the top: "Sales Performance Dashboard"
- Pick 1 consistent color theme (View → Themes)
- Format cards with `₹` currency formatting

## 6. Save & export
- Save as `.pbix`
- File → Export → **Export to PDF** (gives you a static image to attach
  to your resume/portfolio if the reviewer can't open `.pbix`)
- Optionally publish to Power BI Service and share the live link

## What to say about the slicers/interactivity in an interview
*"I added slicers for category, state, month, and payment mode so a
stakeholder could filter the whole dashboard live — for example, isolate
just Electronics sales in Maharashtra for Q2 — without needing a new
report built for them."*
