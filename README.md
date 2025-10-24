🧩 Product Association Algorithm — Sparse Matrix Approach
🔍 Overview

This project implements a Product Association Algorithm designed to identify products frequently bought together — a critical capability for retail recommendation systems and basket analysis.

Unlike traditional association rule mining methods (e.g., Apriori or FP-Growth), this approach leverages Sparse Matrices to efficiently handle large, high-dimensional retail datasets where most product combinations do not co-occur.

⚙️ Tech Stack

Python

FastAPI → Backend API for running model inference and serving association results

Streamlit → Frontend UI for visualizing insights interactively

Pandas / Scikit-learn / Scipy → For data preprocessing, model building, and sparse computations

Render → For cloud deployment (CI/CD setup and live hosting)

🚀 Project Structure
Sparse-Matrix-Model/
│
├── api/                   # FastAPI backend service
│   ├── main.py            # API entry point
│   ├── requirements.txt   # Backend dependencies
│   └── ...                
│
├── streamlit_app/         # Streamlit frontend UI
│   ├── app.py             # Main Streamlit app file
│   ├── requirements.txt   # Frontend dependencies
│   └── ...
│
├── data/                  # (local use only, ignored in git)
├── requirements.txt        # Root dependencies file
├── .gitignore              # Ensures data folder and venv aren’t tracked
└── README.md               # This file

🧮 Why the Sparse Matrix Approach?
Method	Description	Pros	Cons
Apriori	Generates association rules by iteratively expanding frequent itemsets.	Easy to interpret, well-known	Computationally expensive for large datasets.
FP-Growth	Compresses transactions into a prefix tree (FP-tree) and mines it recursively.	Faster than Apriori, no candidate generation	Still memory-heavy for huge item catalogs.
Sparse Matrix	Represents user–product relationships as a high-dimensional, memory-efficient sparse matrix and uses similarity metrics (e.g., cosine similarity).	Scalable, memory efficient, integrates well with ML models	Requires linear algebra knowledge; less intuitive than rule-based methods.
🧠 How It Works

Transactional data is preprocessed into a user–product matrix.

The matrix is converted into a sparse representation (e.g., CSR format).

Using cosine similarity, the algorithm computes product affinities efficiently.

Top-N product associations are returned via a FastAPI endpoint.

The Streamlit UI consumes the API and displays association results interactively.

🌐 Deployment (CI/CD on Render)

This project was deployed on Render using two connected services:

FastAPI backend – serves model results via REST API

Streamlit frontend – consumes the API and provides the UI

A basic CI/CD pipeline was configured through Render, automatically redeploying both services whenever changes are pushed to GitHub.

This setup was implemented to test and practice deployment and CI/CD integration skills on a real-world data application.

🧰 Local Setup
# 1️⃣ Clone repo
git clone git@github.com:Mbuguamaureen01/Product-Association-Algorithim-The-sparse-Matrix-approach.git
cd Product-Association-Algorithim-The-sparse-Matrix-approach

# 2️⃣ Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run backend
cd api
uvicorn main:app --reload

# 5️⃣ Run frontend
cd ../streamlit_app
streamlit run app.py

🧩 Future Improvements

Integrate product metadata (price, category, seasonality) for contextual recommendations

Extend to hybrid recommendation systems (Matrix Factorization + Sparse Associations)

Add caching and batch processing for real-time deployment