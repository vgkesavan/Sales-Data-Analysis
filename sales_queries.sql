-- sales_queries.sql
-- SQL analysis of cleaned sales data.
-- Run against sales.db (table: sales) with any SQLite/MySQL client.

-- 1. Overall KPIs
SELECT
    COUNT(*)              AS total_orders,
    ROUND(SUM(Sales), 2)  AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(AVG(Profit_Margin_Pct), 2) AS avg_margin_pct
FROM sales;

-- 2. Sales & profit by category
SELECT
    Category,
    COUNT(*) AS orders,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;

-- 3. Top 5 products by revenue
SELECT
    Product_Name,
    Category,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY Product_Name, Category
ORDER BY total_sales DESC
LIMIT 5;

-- 4. Top 5 states by sales
SELECT
    State,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY State
ORDER BY total_sales DESC
LIMIT 5;

-- 5. Monthly sales trend
SELECT
    Order_Month,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY Order_Month
ORDER BY Order_Month;

-- 6. Sales by payment mode
SELECT
    Payment_Mode,
    COUNT(*) AS orders,
    ROUND(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY Payment_Mode
ORDER BY total_sales DESC;

-- 7. Customer demographics: average order value by gender & age group
SELECT
    Gender,
    CASE
        WHEN Age < 25 THEN '18-24'
        WHEN Age < 35 THEN '25-34'
        WHEN Age < 45 THEN '35-44'
        WHEN Age < 55 THEN '45-54'
        ELSE '55+'
    END AS age_group,
    COUNT(*) AS orders,
    ROUND(AVG(Sales), 2) AS avg_order_value
FROM sales
GROUP BY Gender, age_group
ORDER BY Gender, age_group;

-- 8. Discount impact: does higher discount correlate with lower margin?
SELECT
    CASE
        WHEN Discount = 0 THEN 'No Discount'
        WHEN Discount <= 0.1 THEN 'Low (<=10%)'
        WHEN Discount <= 0.2 THEN 'Medium (<=20%)'
        ELSE 'High (>20%)'
    END AS discount_band,
    COUNT(*) AS orders,
    ROUND(AVG(Profit_Margin_Pct), 2) AS avg_margin_pct
FROM sales
GROUP BY discount_band
ORDER BY avg_margin_pct DESC;
