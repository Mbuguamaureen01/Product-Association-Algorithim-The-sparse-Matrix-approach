from fastapi import FastAPI, Query
from src.analysis import run_analysis, get_top_related_items

app = FastAPI(title="Retail Sparse Co-Purchase API")

# Run once and keep in memory
item_similarity, item_encoder = run_analysis()

@app.get("/")
def root():
    return {"message": "Retail Sparse Matrix API is running!"}

@app.get("/recommendations/{item_id}")
def recommend_items(item_id: str, top_n: int = Query(10)):
    recs = get_top_related_items(item_id, item_encoder, item_similarity, top_n)
    return {"item_id": item_id, "recommended_items": recs}
