import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from statsmodels.tsa.seasonal import seasonal_decompose


class TimeAnalysis:
    def __init__(self, data):
        self.data = data

    def date_prep(self):
        daily_headlines = self.data.groupby([self.data.index.date]).size()
        monthly_headlines = self.data.resample("ME").size()
        yearly_headlines = self.data.resample("YE").size()

        time_series_daily = pd.DataFrame(
            {"Date": daily_headlines.index, "Headlines_Count": daily_headlines.values}
        )
        time_series_daily["Date"] = pd.to_datetime(time_series_daily["Date"])
        time_series_daily.set_index("Date", inplace=True)

        time_series_monthly = pd.DataFrame(
            {
                "Date": monthly_headlines.index,
                "Headlines_Count": monthly_headlines.values,
            }
        )
        time_series_monthly["Date"] = time_series_monthly["Date"].dt.strftime(
            "%Y-%m-%d"
        )
        time_series_monthly["Date"] = pd.to_datetime(time_series_monthly["Date"])
        time_series_monthly.set_index("Date", inplace=True)

        time_series_yearly = pd.DataFrame(
            {"Date": yearly_headlines.index, "Headlines_Count": yearly_headlines.values}
        )
        time_series_yearly.set_index("Date", inplace=True)

        return time_series_daily, time_series_monthly, time_series_yearly

    def time_decompose(self, ts_data, period, day=False):

        fig, axes = plt.subplots(ncols=1, nrows=4, figsize=(14, 10))

        if day:
            decomposition = seasonal_decompose(
                ts_data["Headlines_Count"].loc[ts_data.index.year == 2018],
                model="additive",
                period=period,
            )
            axes[0].plot(
                ts_data["Headlines_Count"].loc[ts_data.index.year == 2018],
                label="Original",
                color="blue",
            )
        else:
            decomposition = seasonal_decompose(
                ts_data["Headlines_Count"], model="additive", period=period
            )
            axes[0].plot(ts_data["Headlines_Count"], label="Original", color="blue")

        axes[0].tick_params(axis="x", rotation=90)
        axes[0].legend(loc="upper left")

        axes[1].plot(decomposition.trend, label="Trend", color="orange")
        axes[1].tick_params(axis="x", rotation=90)
        axes[1].legend(loc="upper left")

        axes[2].plot(decomposition.seasonal, label="Seasonal", color="green")
        axes[2].tick_params(axis="x", rotation=90)
        axes[2].legend(loc="upper left")

        axes[3].plot(decomposition.resid, label="Residual/Irregular", color="red")
        axes[3].tick_params(axis="x", rotation=90)
        axes[3].legend(loc="upper left")

        plt.tight_layout()
        plt.show()

    def decompose_season(self, ts_data, period, day=False):
        if day:
            decomposition = seasonal_decompose(
                ts_data["Headlines_Count"].loc[ts_data.index.year == 2018],
                model="additive",
                period=period,
            )
        else:
            decomposition = seasonal_decompose(
                ts_data["Headlines_Count"], model="additive", period=period
            )

        fig = px.line(decomposition.seasonal, title="Seasonal Component")
        fig.show()
