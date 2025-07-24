import os
import aiml
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Global size
Window.size = (360, 640)

# AIML Bot setup
BRAIN_FILE = "bot_brain.brn"
bot = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    bot.bootstrap(brainFile=BRAIN_FILE)
else:
    bot.bootstrap(learnFiles="startup.xml", commands="LOAD AIML B")
    bot.saveBrain(BRAIN_FILE)

class ChatBotLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatBotLayout, self).__init__(orientation='vertical', **kwargs)
        
        # Chat history
        self.chat_history = Label(size_hint_y=None, markup=True, halign="left", valign="top")
        self.chat_history.bind(texture_size=self.chat_history.setter("size"))
        
        self.scroll = ScrollView(size_hint=(1, 0.85))
        self.scroll.add_widget(self.chat_history)

        # User input
        self.input_box = TextInput(size_hint=(1, 0.075), multiline=False, hint_text="Apna message likhein...")
        self.send_button = Button(text="Send", size_hint=(1, 0.075), on_press=self.send_message)

        # Add widgets
        self.add_widget(self.scroll)
        self.add_widget(self.input_box)
        self.add_widget(self.send_button)

        self.chat_history.text = "[b][color=4caf50]Jarvis:[/color][/b] Assalamu Alaikum! Main aapki madad ke liye yahan hoon.\n"

    def send_message(self, instance):
        user_input = self.input_box.text.strip()
        if user_input:
            # Show user message
            self.chat_history.text += f"\n[b][color=2196f3]You:[/color][/b] {user_input}"
            response = bot.respond(user_input)
            # Show bot reply
            self.chat_history.text += f"\n[b][color=4caf50]Jarvis:[/color][/b] {response if response else 'Mujhe samajh nahi aaya.'}"
            self.input_box.text = ""
            self.scroll.scroll_y = 0

class ChatBotApp(App):
    def build(self):
        self.title = "Offline ChatBot"
        return ChatBotLayout()

if __name__ == "__main__":
    ChatBotApp().run()
