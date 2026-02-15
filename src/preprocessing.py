import pandas as pd

def load_data(path)
  df = pd.read_csv(path)
  df['date'] = pd.to_datetime(df['date'])
  return df

def feature_engineering(df):
  df = df.sort_values("date")

    df["revenue_deviation_pct"] = (
        (df["revenue"] - df["revenue"].shift(1)) 
        / df["revenue"].shift(1)
    ) * 100

    df["drop_flag"] = df["revenue_deviation_pct"] < -15
    
    return df
