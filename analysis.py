# analysis.py
# Author: 22f3001405@ds.study.iitm.ac.in
# Q2 2025 Business Analysis – Data-Driven Insights

import marimo

__generated_with__ = "0.9.13"
app = marimo.App(width="medium")

@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import marimo as mo
    return mo, pd, plt

@app.cell
def _(pd):
    # Key Metrics Data
    data = {
        "Metric": ["Revenue", "Users", "Retention", "Cost/User"],
        "Q1 2025": [2.1, 12000, 85, 45],
        "Q2 2025": [2.4, 15000, 89, 38],
        "Change": ["+15%", "+25%", "+4%", "-15%"]
    }
    df = pd.DataFrame(data)
    df
    return data, df

@app.cell
def _(df, plt):
    # Revenue Growth Visualization
    plt.figure(figsize=(6,4))
    plt.bar(["Q1 2025", "Q2 2025"], df.loc[0, ["Q1 2025", "Q2 2025"]], color=["skyblue","lightgreen"])
    plt.title("Revenue Growth ($M)")
    plt.show()

@app.cell
def _(df, plt):
    # User Growth Visualization
    plt.figure(figsize=(6,4))
    plt.plot(["Q1 2025","Q2 2025"], df.loc[1,["Q1 2025","Q2 2025"]], marker="o")
    plt.title("User Growth")
    plt.show()

@app.cell
def _():
    import math
    # Algorithm Complexity Comparison
    n = 10**6
    old_time = (n**2) * math.log(n)
    new_time = n * math.log(n)
    efficiency_gain = (old_time - new_time) / old_time * 100
    efficiency_gain
    return efficiency_gain, math, n, new_time, old_time

@app.cell
def _(efficiency_gain):
    print(f"Efficiency Gain: {efficiency_gain:.2f}%")

@app.cell
def _():
    summary = {
        "Revenue Growth": "15% increase compared to Q1 2025",
        "Market Expansion": "Entered 3 new regions",
        "Customer Base": "25% growth in active users",
        "Profitability": "Margins improved by 8%"
    }
    summary
    return summary,

@app.cell
def _(summary):
    for k, v in summary.items():
        print(f"{k}: {v}")

# ----------------------------
# Interactive Slider Example
# ----------------------------
@app.cell
def _(mo, plt):
    # Slider to project next quarter revenue
    revenue_slider = mo.ui.slider(2.0, 3.5, step=0.1, value=2.4, label="Projected Q3 Revenue ($M)")

    def plot_projection(value):
        plt.figure(figsize=(6,4))
        plt.bar(["Q1 2025","Q2 2025","Q3 2025 (Projected)"], [2.1, 2.4, value], color=["skyblue","lightgreen","orange"])
        plt.title("Revenue Projection")
        plt.show()

    mo.vstack([revenue_slider, mo.lazy(plot_projection)(revenue_slider.value)])
    return plot_projection, revenue_slider

if __name__ == "__main__":
    app.run()
