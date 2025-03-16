import edge_tts
from IPython.display import Audio
def tts(text, pitch,audio_path):
    communicate = edge_tts.Communicate(
        text,
        "ja-JP-NanamiNeural",
        rate="+10%",
        volume="+10%",
        pitch=pitch,
    )
    communicate.save_sync(f"./static/{audio_path}.mp3")

if __name__ == "__main__":
    tts("こんにちは", "-30Hz", "audio")
    tts("こんにちは", "+10Hz", "audio")