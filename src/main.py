import logging
import os

from prepocessing import load_data, feature_engineering
from anomaly_model import train_isolation_forest
from alert_engine import appl_alert_logic

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)


# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
  logging.info("Pipeline started")
  
  df = load_data("data/sample_revenue.csv")
  logging.info("Data loaded succesfully")
  
  df = feature_enginering(df)
  logging.info("Feature engineering completed")

  df, model = train_isolation_forest(df)
  logging.info("Anomaly model trained")

  df = apply_alert_logic(df)
  logging.info("Alert logic applied")

  print(df[["date", "revenue", "revenue_deviation_pct", "alert_status"]])
  logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
