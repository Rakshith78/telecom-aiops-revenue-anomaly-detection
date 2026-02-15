from src.alert_engine import generate_alert

def test_critical_alert():
  row = {
        "drop_flag": True,
        "anomaly_flag": -1,
        "revenue_deviation_pct": -20
        }
assert generate_alert(row) == "CRITICAL"
