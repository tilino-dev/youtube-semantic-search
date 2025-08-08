# youtube-semantic-search

Minimal semantic search prototype for YouTube video transcripts. Copy audio transcripts into the data folder or use the provided example_transcripts.json

## What is this project about?

This project is called **YouTube Semantic Search**, and it’s basically a smarter way to search through YouTube video transcripts. Instead of just looking for exact words, it tries to understand what you really mean and finds the parts of the video that best match your question.

### How does it work?

- First, it uses OpenAI’s Whisper model to turn the audio from YouTube videos into text transcripts.  
- Then, it converts those transcripts into “meaningful” number vectors using advanced language models — this helps the computer get the context, not just keywords.  
- It stores these vectors in a fast search index (called FAISS) so it can quickly find the most relevant parts when you search.  
- Finally, it shows you the results in a simple web app built with Gradio, where you just type your question and get back the best matching transcript snippets.  
- It’s built so you can add transcripts from multiple videos and search all of them at once.

### Why did I build this?

Normal text search looks for exact matches, so it misses a lot if you don’t use the right keywords. This tool understands meaning and context, making it way easier to find what you want in long videos. It’s super useful if you watch a lot of educational videos, lectures, or interviews and want to jump straight to the part that matters.

## Run locally

1. python -m venv venv && source venv/bin/activate
2. pip install -r requirements.txt
3. python app.py

Open the Gradio link and test queries.
