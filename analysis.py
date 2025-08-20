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
    return pd, plt

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
def _(df):
    import matplotlib.pyplot as plt
    # Revenue Growth Visualization
    plt.figure(figsize=(6,4))
    plt.bar(["Q1 2025", "Q2 2025"], df.loc[0, ["Q1 2025", "Q2 2025"]], color=["skyblue","lightgreen"])
    plt.title("Revenue Growth ($M)")
    plt.show()

@app.cell
def _(df):
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

if __name__ == "__main__":
    app.run()
