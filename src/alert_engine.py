def generate_alert(row)

 if row["drop_flag"] or row ["anamoloy_flag"] == -1
  return "CRITICAL"
 
 if abs(row["revenue_deviation_pct"]) > 10:
   return "WARNING"

return "CLEAR"

def apply_alert_logic(df):
  df["alert_status"] = df.apply(generate_alert, axis=1)
  return df
