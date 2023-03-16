import whisper


class Whisper:
    def __init__(self, language='en'):
        self.model = whisper.load_model('small')
        self.language = language

    def transcribe(self, audio_path):
        return whisper.transcribe(self.model, audio_path, language=self.language, 
                                  task='transcribe', temperature=0, fp16=False)
