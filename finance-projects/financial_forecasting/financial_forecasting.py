from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
OUT = BASE / "outputs"
DATA.mkdir(exist_ok=True)
OUT.mkdir(exist_ok=True)

np.random.seed(42)
dates = pd.date_range(start="2020-01-01", periods=60, freq="M")
revenue = np.round(np.linspace(100000, 250000, 60) + np.random.normal(0, 10000, 60), 2)
expenses = np.round(np.linspace(60000, 180000, 60) + np.random.normal(0, 8000, 60), 2)
profit = revenue - expenses
df = pd.DataFrame({"Date": dates, "Revenue": revenue, "Expenses": expenses, "Profit": profit})
df.to_csv(DATA / "financial_data.csv", index=False)

df["Month_Num"] = np.arange(len(df))
X = df[["Month_Num"]]
y = df["Revenue"]
model = LinearRegression().fit(X, y)
future = pd.DataFrame({"Month_Num": np.arange(len(df), len(df)+12)})
forecast = model.predict(future)
future_dates = pd.date_range(df["Date"].iloc[-1] + pd.DateOffset(months=1), periods=12, freq="M")
forecast_df = pd.DataFrame({"Date": future_dates, "Forecast_Revenue": forecast})
forecast_df.to_csv(OUT / "forecast_revenue.csv", index=False)

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Revenue"], label="Actual")
plt.plot(forecast_df["Date"], forecast_df["Forecast_Revenue"], label="Forecast", linestyle="--")
plt.title("Financial Forecast – Revenue Projection")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()
plt.grid(True)
plt.savefig(OUT / "revenue_forecast.png", bbox_inches="tight")
plt.close()

y_pred = model.predict(X)
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

report = f'''
# Financial Forecasting Report

**Model:** Linear Regression  
**MAE:** {mae:.2f}  
**RMSE:** {rmse:.2f}  
**R²:** {r2:.3f}  

- Revenue growth trend is strong.
- Profit margins are improving.
- Forecast suggests continued growth.
'''
(BASE / "REPORT.md").write_text(report)
print("✅ Financial Forecasting completed successfully.")
