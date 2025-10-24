from gtts import gTTS
import os

# ✅ Step 1: Create abc.txt automatically if it doesn't exist
if not os.path.exists("abc.txt"):
    with open("abc.txt", "w") as f:
        f.write("Hello! This is a text to speech example using Python.")

# ✅ Step 2: Read the text file
with open("abc.txt", "r") as file:
    text = file.read()

# ✅ Step 3: Convert text to speech
speech = gTTS(text=text, lang='en', slow=False)

# ✅ Step 4: Save the output as an mp3 file
speech.save("voice.mp3")

print("✅ Speech file saved as 'voice.mp3'")

# ✅ Step 5: Play the audio file (platform-dependent)
# For Codespaces or Linux:
os.system("mpg123 voice.mp3")

# For Windows (uncomment this instead):
# os.system("start voice.mp3")

# For macOS (uncomment this instead):
# os.system("afplay voice.mp3")
