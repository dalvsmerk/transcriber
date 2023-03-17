import os
import json
# import whisper
from file_utils import parse_filename
from dotenv import is_windows


class Whisper:
    def __init__(self, logging, language='en'):
        # self.model = whisper.load_model('small')
        self.language = language
        self.logging = logging

    def transcribe(self, audio_path):
        # whisper ~/git/transcribe/data/2022-03-13/harvard.wav --language English --fp16 False --output_format json
        # return whisper.transcribe(self.model, audio_path, language=self.language, 
        #                           task='transcribe', temperature=0, fp16=False)
        self.logging.log(self.logging.INFO, "Transcribing '{}'...".format(audio_path))

        path = audio_path

        if is_windows():
            # Escape spaces
            path = path.replace(' ', '\\ ')

        script = "whisper '{}' --language {} --fp16 False --output_format json".format(path, self.language)
        exit_code = os.system(script)

        if exit_code != 0:
            raise Exception('Error running whisper')
        
        result_path = parse_filename(audio_path) + '.json'
        
        with open(result_path, mode='r', encoding='utf-8') as f:
            result = json.load(f)

        os.remove(result_path)

        self.logging.log(self.logging.INFO, 'Transcription is done')

        return self.normalize_result(result)

    def normalize_result(self, result):
        result['text'] = result['text'].encode('utf-8').decode('utf-8')

        for idx, _ in enumerate(result['segments']):
            text = result['segments'][idx]['text']
            result['segments'][idx]['text'] = text.encode('utf-8').decode('utf-8')

        return result
        
