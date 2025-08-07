from fastapi import FastAPI, HTTPException
from app.database import fetch_orders
from app.recommender import get_recommendations  # You will create this module later

app = FastAPI(title="nopCommerce Recommendation API")

@app.get("/")
async def root():
    return {"message": "Welcome to the Recommender System API"}

@app.get("/recommend")
def recommend(user_id: int):
    df_orders = fetch_orders()
    if user_id not in df_orders['CustomerId'].values:
        raise HTTPException(status_code=404, detail="User not found")
    recs = get_recommendations(user_id, df_orders)
    return {"user_id": user_id, "recommendations": recs}
