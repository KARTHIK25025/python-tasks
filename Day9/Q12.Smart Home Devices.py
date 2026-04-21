class WiFiDevice:
    def connect_wifi(self):
        print("Connected to WiFi network.")
class VoiceAssistant:
    def listen_command(self):
        print("Listening for voice commands...")
class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display_features(self):
        print("Smart Speaker initialized.")
        self.connect_wifi()
        self.listen_command()
speaker = SmartSpeaker()
speaker.display_features()
