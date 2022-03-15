import pandas as pd
import numpy as np
from plotly_calplot import calplot

def cal():
    dummy_start_date = "2019-01-01"
    dummy_end_date = "2021-10-03"

    dummy_df = pd.DataFrame({
        "ds": pd.date_range(dummy_start_date, dummy_end_date),
        "value": np.random.randint(low=0, high=30,
        size=(pd.to_datetime(dummy_end_date) - pd.to_datetime(dummy_start_date)).days + 1,),
        })
    fig = calplot(
        dummy_df,
        x="ds",
        y="value"
    )
    return fig
