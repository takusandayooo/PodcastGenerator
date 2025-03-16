import json
import os
from module.text_to_speech import tts
from module.gemini_create_text import create_text
from pydub import AudioSegment
import glob

json_text_data=create_text("input.pdf")
with open('data.json', 'w') as f:
    f.write(json_text_data)

print("Data.json created successfully")

json_data = json.loads(open('data.json').read())

speaker_1_pitch="-20Hz"
speaker_2_pitch="+0Hz"
import os

if not os.path.exists("audio"):
    os.makedirs("audio")
else:
    for file in os.listdir("audio"):
        os.remove(f"audio/{file}")

for count,data in enumerate(json_data["script"]):
    if data["speaker"] ==json_data['speakers'][0]:
        pitch = speaker_1_pitch
        tts(data['text'],pitch,f"audio/{count}")
    else:
        pitch = speaker_2_pitch
        tts(data['text'],pitch,f"audio/{count}")
print("All audio files created successfully")

# 連結
audio_files = glob.glob("audio/*.mp3")
count_files = len(audio_files)

for count in range(count_files):
    sound = AudioSegment.from_file(f"./audio/{count}.mp3", "mp3")
    if count == 0:
        sounds=sound
    else:
        sounds = sounds + sound
    
sounds.export("output.mp3", format="mp3")



print("All audio files concatenated successfully")
