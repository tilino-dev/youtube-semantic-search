from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = 'all-MiniLM-L6-v2'

def load_model(name=MODEL_NAME):
    return SentenceTransformer(name)

def embed_texts(model, texts: list):
    return model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

if __name__ == '__main__':
    m = load_model()
    print(m.encode(['hello world']).shape)
