# Minimal Gradio app to demonstrate semantic search
import gradio as gr
from src.embed import load_model, embed_texts
from src.search import SimpleIndex
import json

DATA_FILE = 'data/example_transcripts.json'

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

texts = [item['text'] for item in data]

model = load_model()
embs = embed_texts(model, texts)
index = SimpleIndex(embs.shape[1])
index.add(embs, texts)


def query(q, k=5):
    q_emb = model.encode([q])[0]
    hits = index.search(q_emb, topk=int(k))
    return "\n\n".join([f"{i+1}. {t} (dist={d:.3f})" for i,(t,d) in enumerate(hits)])

iface = gr.Interface(fn=query, inputs=[gr.Textbox(lines=1, placeholder='Search...'), gr.Slider(minimum=1, maximum=10, value=5)], outputs='text')

if __name__ == '__main__':
    iface.launch()
