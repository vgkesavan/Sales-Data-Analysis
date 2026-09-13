### sales_queries.sql

| total_orders | total_sales | total_profit | avg_margin_pct |
|---|---|---|---|
| 900 | 20546342.5 | 4693202.5 | 31.46 |

### 2. Sales & profit by category

| Category | orders | total_sales | total_profit |
|---|---|---|---|
| Electronics | 272 | 15803600.0 | 3209900.0 |
| Home & Kitchen | 185 | 2816635.0 | 786035.0 |
| Clothing | 199 | 1023370.0 | 376770.0 |
| Sports | 122 | 603225.0 | 209175.0 |
| Beauty | 122 | 299512.5 | 111322.5 |

### 3. Top 5 products by revenue

| Product_Name | Category | units_sold | total_sales |
|---|---|---|---|
| Laptop | Electronics | 208 | 10760750.0 |
| Smartphone | Electronics | 172 | 3572800.0 |
| Office Chair | Home & Kitchen | 163 | 1272025.0 |
| Smart Watch | Electronics | 233 | 969300.0 |
| Air Fryer | Home & Kitchen | 114 | 694200.0 |

### 4. Top 5 states by sales

| State | total_sales | total_profit |
|---|---|---|
| Maharashtra | 3940857.5 | 899807.5 |
| Kerala | 2787707.5 | 608497.5 |
| Tamil Nadu | 2670755.0 | 610025.0 |
| Karnataka | 2632772.5 | 611162.5 |
| West Bengal | 2519485.0 | 573935.0 |

### 5. Monthly sales trend

| Order_Month | total_sales | total_profit |
|---|---|---|
| 2025-01 | 1174962.5 | 246322.5 |
| 2025-02 | 1346150.0 | 291710.0 |
| 2025-03 | 789925.0 | 210335.0 |
| 2025-04 | 1328320.0 | 315020.0 |
| 2025-05 | 1049247.5 | 242147.5 |
| 2025-06 | 1465397.5 | 320397.5 |
| 2025-07 | 766720.0 | 205890.0 |
| 2025-08 | 631655.0 | 160475.0 |
| 2025-09 | 1790840.0 | 393550.0 |
| 2025-10 | 1442365.0 | 322215.0 |
| 2025-11 | 748202.5 | 180452.5 |
| 2025-12 | 1086045.0 | 277735.0 |
| 2026-01 | 1066642.5 | 245212.5 |
| 2026-02 | 1181795.0 | 258505.0 |
| 2026-03 | 595417.5 | 149677.5 |
| 2026-04 | 1759375.0 | 383505.0 |
| 2026-05 | 765257.5 | 170977.5 |
| 2026-06 | 1558025.0 | 319075.0 |

### 6. Sales by payment mode

| Payment_Mode | orders | total_sales |
|---|---|---|
| Upi | 353 | 8136592.5 |
| Credit Card | 185 | 4417967.5 |
| Debit Card | 166 | 3914010.0 |
| Net Banking | 120 | 2539892.5 |
| Cash | 76 | 1537880.0 |

### 7. Customer demographics: average order value by gender & age group

| Gender | age_group | orders | avg_order_value |
|---|---|---|---|
| Female | 18-24 | 69 | 26245.33 |
| Female | 25-34 | 128 | 21872.56 |
| Female | 35-44 | 100 | 22226.3 |
| Female | 45-54 | 87 | 20794.22 |
| Female | 55+ | 50 | 21819.55 |
| Male | 18-24 | 68 | 22725.29 |
| Male | 25-34 | 102 | 27869.02 |
| Male | 35-44 | 100 | 27013.4 |
| Male | 45-54 | 102 | 18540.25 |
| Male | 55+ | 68 | 16620.7 |
| Other | 18-24 | 7 | 18308.57 |
| Other | 25-34 | 3 | 35716.67 |
| Other | 35-44 | 7 | 5911.43 |
| Other | 45-54 | 7 | 36635.0 |
| Other | 55+ | 2 | 84637.5 |

### 8. Discount impact: does higher discount correlate with lower margin?

| discount_band | orders | avg_margin_pct |
|---|---|---|
| No Discount | 226 | 35.85 |
| Low (<=10%) | 496 | 31.7 |
| Medium (<=20%) | 178 | 25.22 |
