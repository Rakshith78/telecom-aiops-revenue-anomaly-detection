from sklearn.ensemble import IsolationForest

def train_isolation_forest(df):
  model = IsolationForest(contaminator=0.1, random_state=42)
  features = df[["revenue", "paid_count", "free_count"]]
  model.fit(features)
   
  df["anomaly_score"] = model.decision_function(features)
  df["anomaly_flag"] = model.predict(features)
    
  return df, model
