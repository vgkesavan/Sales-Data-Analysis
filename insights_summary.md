# Sales Data Analysis — Key Insights

**Dataset:** 900 cleaned sales orders, Jan 2025 – Jun 2026
**Total Sales:** ₹2,05,46,342.5 | **Total Profit:** ₹46,93,202.5 | **Avg Margin:** 31.46%

## Key Findings

1. **Electronics dominates revenue** — ₹1,58,03,600 (77% of total sales)
   from just 272 of 900 orders. Laptops alone generated ₹1,07,60,750.
2. **Maharashtra is the top state** by sales (₹39.4L), followed by Kerala,
   Tamil Nadu, and Karnataka — all within a tight ₹1.5L band of each other.
3. **UPI is the leading payment mode**, used in 353 of 900 orders (39%)
   and accounting for ₹81.4L in sales — nearly double the next channel.
4. **Discounting erodes margin steadily**: no-discount orders average
   35.85% margin, dropping to 31.7% at low discount and 25.22% at
   medium discount — a clear, quantifiable trade-off for any pricing
   conversation.
5. **September and April were peak months** (₹17.9L and ₹17.6L),
   suggesting a seasonal pattern worth investigating further (e.g.
   festival season, back-to-school).
6. **Male customers aged 25-44 have the highest average order value**
   (₹27,000+), while male customers 55+ have the lowest (₹16,620) —
   useful for age-targeted marketing.

## Recommendations
- Double down on Electronics marketing in Maharashtra/Kerala/Tamil Nadu
- Investigate why discounts above 10% aren't driving proportionally
  higher volume to offset the margin loss
- Promote UPI further given its already-dominant adoption and zero
  processing friction reported by customers

## Files
- `outputs/sales_clean.csv` — cleaned dataset, ready for Power BI
- `outputs/sales.db` — SQLite database used for the SQL analysis
- `outputs/query_results.md` — all 8 SQL queries with results
- `sql/sales_queries.sql` — the SQL script itself
- `charts/` — 5 dashboard-preview charts
- `POWERBI_GUIDE.md` — step-by-step guide to build the live dashboard
