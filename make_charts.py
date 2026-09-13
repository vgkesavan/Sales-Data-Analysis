"""
make_charts.py
Generates chart visuals summarizing the sales KPIs — a preview of what
the Power BI dashboard should show. Tools: Python, Pandas, Matplotlib
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

df = pd.read_csv("outputs/sales_clean.csv")
plt.rcParams["figure.dpi"] = 110
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
palette = ["#2E5EAA", "#E8743B", "#3FA796", "#C94277", "#F2C14E"]


def money(ax, axis="y"):
    fmt = mticker.FuncFormatter(lambda x, _: f"₹{x/100000:,.1f}L")
    (ax.yaxis if axis == "y" else ax.xaxis).set_major_formatter(fmt)


# 1. Sales by category
cat = df.groupby("Category")["Sales"].sum().sort_values()
fig, ax = plt.subplots(figsize=(7, 5))
cat.plot(kind="barh", ax=ax, color=palette)
ax.set_title("Total Sales by Category", fontweight="bold")
ax.set_xlabel("Sales (₹)")
money(ax, "x")
plt.tight_layout()
plt.savefig("charts/01_sales_by_category.png")
plt.close()

# 2. Monthly sales trend
monthly = df.groupby("Order_Month")["Sales"].sum()
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(monthly.index, monthly.values, marker="o", color="#2E5EAA")
ax.set_title("Monthly Sales Trend", fontweight="bold")
ax.set_ylabel("Sales (₹)")
money(ax)
plt.xticks(rotation=60, ha="right")
plt.tight_layout()
plt.savefig("charts/02_monthly_trend.png")
plt.close()

# 3. Top 5 states
states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(5)
fig, ax = plt.subplots(figsize=(7, 5))
states.sort_values().plot(kind="barh", ax=ax, color=palette)
ax.set_title("Top 5 States by Sales", fontweight="bold")
ax.set_xlabel("Sales (₹)")
money(ax, "x")
plt.tight_layout()
plt.savefig("charts/03_top_states.png")
plt.close()

# 4. Payment mode share
pay = df.groupby("Payment_Mode")["Sales"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(6.5, 6.5))
ax.pie(pay.values, labels=pay.index, autopct="%1.0f%%", colors=palette,
       wedgeprops={"edgecolor": "white"})
ax.set_title("Sales Share by Payment Mode", fontweight="bold")
plt.tight_layout()
plt.savefig("charts/04_payment_mode.png")
plt.close()

# 5. Discount band vs margin
band_order = ["No Discount", "Low (<=10%)", "Medium (<=20%)", "High (>20%)"]
df["discount_band"] = pd.cut(df["Discount"], bins=[-0.01, 0, 0.1, 0.2, 1],
                              labels=band_order)
margin = df.groupby("discount_band", observed=True)["Profit_Margin_Pct"].mean()
fig, ax = plt.subplots(figsize=(7, 5))
margin.plot(kind="bar", ax=ax, color=palette)
ax.set_title("Average Profit Margin by Discount Band", fontweight="bold")
ax.set_ylabel("Avg Margin (%)")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig("charts/05_discount_vs_margin.png")
plt.close()

print("Saved 5 charts to charts/")
