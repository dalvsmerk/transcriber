from watchdog.events import PatternMatchingEventHandler
from file_utils import parse_filename


class AudioFileEventHandler(PatternMatchingEventHandler):
    def __init__(self, model, whatsapp, logging):
        super(AudioFileEventHandler, self).__init__(patterns=['*.mp3', '*.wav'])

        self.model = model
        self.whatsapp = whatsapp
        self.logging = logging

    def on_created(self, event):
        if not event.is_directory:
            try:
                result = self.model.transcribe(event.src_path)
                filename, message = self.formatMessage(event.src_path, result)
                
                self.logging.log(self.logging.INFO, filename + '\n' + message)

                self.whatsapp.sendGroupMessage(message, title=filename)
            except Exception as e:
                print(e)

        return super().on_created(event)
    
    def formatMessage(self, file_path, result):
        filename = parse_filename(file_path)
        message = ''

        for segment in result['segments']:
            message += segment['text'] + '\n'

        return filename, message
