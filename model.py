import whisper


class Whisper:
    def __init__(self, language='en'):
        self.model = whisper.load_model('base')
        self.language = language

    def transcribe(self, audio_path):
        return self.model.transcribe(audio_path, language=self.language)
