import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

FILE_PATH = "data/raw_data.xlsx"

def load_data():
    print("Loading data...")
    df = pd.read_excel(FILE_PATH)
    df = df.dropna(subset=["TransactionId", "Item No."])
    print(f"Loaded {len(df):,} rows.")
    return df

def prepare_sparse_matrix(df):
    print("Preparing sparse matrix...")

    # Map Item and Transaction IDs to integer indices
    item_encoder = {item: idx for idx, item in enumerate(df["Item No."].unique())}
    trans_encoder = {t: idx for idx, t in enumerate(df["TransactionId"].unique())}

    df["item_idx"] = df["Item No."].map(item_encoder)
    df["trans_idx"] = df["TransactionId"].map(trans_encoder)

    # Create sparse matrix (transactions x items)
    rows = df["trans_idx"]
    cols = df["item_idx"]
    data = np.ones(len(df), dtype=np.int8)
    sparse_matrix = csr_matrix((data, (rows, cols)), 
                               shape=(len(trans_encoder), len(item_encoder)))

    print(f"Sparse matrix: {sparse_matrix.shape[0]:,} transactions × {sparse_matrix.shape[1]:,} items")
    return sparse_matrix, item_encoder, trans_encoder

def compute_item_similarity(sparse_matrix):
    print("Computing cosine similarity between items...")
    item_similarity = cosine_similarity(sparse_matrix.T, dense_output=False)
    print("Similarity matrix computed.")
    return item_similarity

def get_top_related_items(item_id, item_encoder, item_similarity, top_n=10):
    idx = item_encoder.get(item_id)
    if idx is None:
        return []
    
    # Get similarity scores for this item
    sim_scores = item_similarity[idx].toarray().flatten()
    similar_indices = np.argsort(sim_scores)[::-1][1:top_n+1]

    reverse_encoder = {v: k for k, v in item_encoder.items()}
    similar_items = [(reverse_encoder[i], sim_scores[i]) for i in similar_indices]
    
    return similar_items

def run_analysis():
    df = load_data()
    sparse_matrix, item_encoder, trans_encoder = prepare_sparse_matrix(df)
    item_similarity = compute_item_similarity(sparse_matrix)
    return item_similarity, item_encoder

