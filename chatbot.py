import aiml
import os

# Bot setup
BRAIN_FILE = "bot_brain.brn"

kernel = aiml.Kernel()

# Agar trained brain file maujood hai tou load karo
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file...")
    kernel.loadBrain(BRAIN_FILE)
else:
    print("Parsing AIML files...")
    kernel.bootstrap(learnFiles="startup.xml", commands="LOAD AIML B")
    print("Saving brain file...")
    kernel.saveBrain(BRAIN_FILE)

# Chat loop
while True:
    message = input("You: ")
    if message.lower() == "exit":
        break
    response = kernel.respond(message)
    print("Bot:", response)
