from prepocessing import load_data, feature_engineering
from anomaly_model import train_isolation_forest
from alert_engine import appl_alert_logic

def run_pipeline():

  df = load_data("data/sample_revenue.csv")
  
  df = feature_enginering(df)

  df, model = train_isolation_forest(df)

  df = apply_alert_logic(df)

  print(df[["date", "revenue", "revenue_deviation_pct", "alert_status"]])

if __name__ == "__main__":
    run_pipeline()
