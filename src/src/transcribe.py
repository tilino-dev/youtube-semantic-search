# Simple wrapper that transcribes audio files using OpenAI Whisper local package
from pathlib import Path
import whisper

def transcribe_file(audio_path: str, model_name: str = "base") -> dict:
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python transcribe.py path/to/audio.mp3')
        raise SystemExit(1)
    out = transcribe_file(sys.argv[1])
    print(out['text'][:500])
