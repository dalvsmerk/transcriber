import whisper
from noise_reduction import read_audio, reduce_noise


class Whisper:
    def __init__(self, logging, language='en'):
        self.model = whisper.load_model('small')
        self.language = language
        self.logging = logging

    def transcribe(self, audio_path):
        # whisper ~/git/transcribe/data/2022-03-13/harvard.wav --language English --fp16 False --output_format json
        self.logging.log(self.logging.INFO, "Transcribing '{}'...".format(audio_path))

        recording, sample_rate = read_audio(audio_path)
        recording_clean = reduce_noise(recording, sample_rate)

        return whisper.transcribe(self.model, recording_clean, language=self.language, 
                                  task='transcribe', temperature=0, fp16=False)
