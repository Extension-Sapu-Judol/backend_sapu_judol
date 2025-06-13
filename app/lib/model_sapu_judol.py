import joblib
import os
import re
import emoji

# Path relatif ke file ini
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "model_rf", "model_rf_sapu_judol.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "..", "model", "model_rf", "vectorizer_tfidf.pkl")

# Load model dan vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def preprocess(text: str):
  text = text.lower()
  text = re.sub(r"http\S+|www\S+", "", text)  # Hilangkan link
  text = emoji.demojize(text)  # Ubah emoji jadi teks (misal: 😎 → :smiling_face_with_sunglasses:)
  text = re.sub(r":[a-z_]+:", r" \g<0> ", text)  # Tambah spasi di sekitar emoji teks
  text = re.sub(r"[^a-zA-Z0-9 :_]", " ", text)  # Hilangkan simbol aneh tapi pertahankan emoji teks
  text = re.sub(r"\s+", " ", text).strip()  # Hilangkan spasi berlebih
  return text

def predict_comment(text: str) -> bool:
  processed = preprocess(text)
  vectorized = vectorizer.transform([processed])
  pred = model.predict(vectorized)[0]
  return True if pred == 1 else False
