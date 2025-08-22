
---

# 🎬 AiMovier
A movie recommendation system that recommends movies similar to your favorites :p

A simple and interactive **content-based movie recommender system** built with **Python, Streamlit, and scikit-learn**.
It suggests movies based on your favorite movie, or lets you explore by **genre, actor, or director**.

🚀 **Live Demo**: [click me](https://aimovier.streamlit.app/)

---

## ✨ Features
* 🔍 **Search by Movie** – Get top 5 most similar movies.
  <img width="1061" height="755" alt="Screenshot 2025-08-22 100622" src="https://github.com/user-attachments/assets/ec394cb9-1560-4473-b786-02aad6c06ce6" />

* 🎭 **Search by Genre** – Discover random picks from any genre.
  <img width="1041" height="764" alt="Screenshot 2025-08-22 135256" src="https://github.com/user-attachments/assets/543e19d5-bafc-47b4-9244-06cd21c3663d" />

* 🎥 **Search by Actor** – Find movies featuring your favorite stars.
  <img width="1040" height="764" alt="Screenshot 2025-08-22 135243" src="https://github.com/user-attachments/assets/a9c0b43f-cde9-4f71-9dff-a372ed641761" />

* 🎬 **Search by Director** – Explore films directed by specific filmmakers.
  <img width="1066" height="784" alt="Screenshot 2025-08-22 135118" src="https://github.com/user-attachments/assets/59edb55a-0694-4307-8f2f-005fd62778c6" />

---

## ⚙️ How it Works

* Dataset: [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* Preprocessing: Extracts **genres, keywords, cast, and crew** from JSON-like fields.
* Vectorization: Uses **CountVectorizer** to turn text into feature vectors.
* Similarity: Computes **cosine similarity** between movie vectors to recommend top matches.

---

## 🛠 Installation & Local Setup

Clone the repo:

```bash
git clone https://github.com/Praduamn/Ai_Movie_Recommender.git
cd Ai_Movie_Recommender
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 📦 Requirements

* Python 3.9+
* Streamlit
* Pandas
* Scikit-learn

(Already listed in `requirements.txt`)

---

## 📂 Project Structure

```
├── app.py                  # Main Streamlit app  
├── tmdb_5000_movies.csv    # Movies dataset  
├── tmdb_5000_credits.csv   # Credits dataset  
├── requirements.txt        # Python dependencies  
└── README.md               # Project documentation  
```

---

## Contributing

* [Praduamn](https://github.com/Praduamn)

Pull requests and suggestions are welcome!

---

## 📜 License

This project is for educational purposes. Dataset © TMDB.

---

