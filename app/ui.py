import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("Retail Co-Purchase (Sparse Matrix Model)")
st.write("Discover which items are frequently bought together using item similarity.")

item_id = st.text_input("Enter Item No. (SKU):", "")
top_n = st.slider("Number of similar items", 5, 30, 10)

if st.button("Get Recommendations"):
    if not item_id:
        st.warning("Please enter an item number.")
    else:
        response = requests.get(f"{API_URL}/recommendations/{item_id}?top_n={top_n}")
        if response.status_code == 200:
            recs = response.json()["recommended_items"]
            if recs:
                df = pd.DataFrame(recs, columns=["Item No.", "Similarity Score"])
                st.dataframe(df)
            else:
                st.info("No similar items found.")
        else:
            st.error("Error connecting to API.")
