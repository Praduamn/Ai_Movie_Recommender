
---

# 🎬 AiMovier
A simple and interactive **content-based movie recommender system** built with **Python, Streamlit, and scikit-learn**.
It suggests movies based on your favorite movie, or lets you explore by **genre, actor, or director**.

🚀 **Live Demo**: [click me](https://aimovier.streamlit.app/)

---

## ✨ Features
* 🔍 **Search by Movie** – Get top 5 most similar movies.
  <img width="1061" height="755" alt="Screenshot 2025-08-22 100622" src="https://github.com/user-attachments/assets/ec394cb9-1560-4473-b786-02aad6c06ce6" />

* 🎭 **Search by Genre** – Discover random picks from any genre.
  <img width="960" height="536" alt="Screenshot 2025-08-22 135256" src="https://github.com/user-attachments/assets/0d93f2c9-2c39-4760-951f-d97367f12e38" />

* 🎥 **Search by Actor** – Find movies featuring your favorite stars.
  <img width="950" height="526" alt="480808890-a9c0b43f-cde9-4f71-9dff-a372ed641761" src="https://github.com/user-attachments/assets/77ad497d-240d-40c8-adca-b738e9eaef0c" />

* 🎬 **Search by Director** – Explore films directed by specific filmmakers.
  <img width="961" height="536" alt="Screenshot 2025-08-22 135118" src="https://github.com/user-attachments/assets/a33994e3-4da7-496f-810d-028efd13bc75" />

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

