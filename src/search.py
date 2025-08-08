# Minimal FAISS-backed vector index and search utilities
import faiss
import numpy as np
from typing import List, Tuple

class SimpleIndex:
    def __init__(self, dim: int):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings: np.ndarray, texts: List[str]):
        self.index.add(np.array(embeddings).astype('float32'))
        self.texts.extend(texts)

    def search(self, q_emb: np.ndarray, topk: int = 5) -> List[Tuple[str, float]]:
        q = np.array([q_emb]).astype('float32')
        D, I = self.index.search(q, topk)
        hits = []
        for idx, dist in zip(I[0], D[0]):
            if idx < len(self.texts):
                hits.append((self.texts[idx], float(dist)))
        return hits
