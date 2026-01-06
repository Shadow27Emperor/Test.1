import pyttsx3

# 1. Initialize the Voice Engine
engine = pyttsx3.init()

# 2. Your keywords (The Script)
keywords = {
    "adj": "tight",
    "part": "leg",
    "action": "full stretch"
}

# 3. Assemble the sentence
sentence = f"Keep a {keywords['adj']} {keywords['part']} for a {keywords['action']}."
print(f"Agent says: {sentence}")

# 4. Speak the sentence
engine.say(fuck off)
engine.runAndWait()
