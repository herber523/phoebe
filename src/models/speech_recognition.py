
class STT:
    def __init__(self, audio):
        self.audio = audio

    def get_text(self):
        return self.audio.decode('utf-8')

