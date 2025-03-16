import json
import os
from module.text_to_speech import tts
from module.gemini_create_text import create_text
from pydub import AudioSegment
import glob


from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/podcast",methods=["POST"])
def podcast():
    print("Podcast route called")
    file = request.files['pdf']
    file.save("./static/input.pdf")
    json_text_data=create_text("./static/input.pdf")
    with open('./static/data.json', 'w') as f:
        f.write(json_text_data)

    print("Data.json created successfully")

    json_data = json.loads(open('./static/data.json').read())

    speaker_1_pitch="-20Hz"
    speaker_2_pitch="+0Hz"

    if not os.path.exists("./static/audio"):
        os.makedirs("./static/audio")
    else:
        for file in os.listdir("./static/audio"):
            os.remove(f"./static/audio/{file}")

    for count,data in enumerate(json_data["script"]):
        if data["speaker"] ==json_data['speakers'][0]:
            pitch = speaker_1_pitch
            tts(data['text'],pitch,f"audio/{count}")
        else:
            pitch = speaker_2_pitch
            tts(data['text'],pitch,f"audio/{count}")
    print("All audio files created successfully")

    # 連結
    audio_files = glob.glob("./static/audio/*.mp3")
    count_files = len(audio_files)

    for count in range(count_files):
        sound = AudioSegment.from_file(f"./static/audio/{count}.mp3", "mp3")
        if count == 0:
            sounds=sound
        else:
            sounds = sounds + sound
        
    sounds.export("./static/output.mp3", format="mp3")
    print("All audio files concatenated successfully")
    return render_template("podcast.html",podcast="output.mp3")

if __name__ == '__main__':
    app.run(debug=True)