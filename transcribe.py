import sys
import time
import logging
import whisper
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

model = whisper.load_model('base')

class AudioFileEventHandler(PatternMatchingEventHandler):
    def __init__(self):
        super(AudioFileEventHandler, self).__init__(patterns=['*.mp3', '*.wav'])

    def on_created(self, event):
        if not event.is_directory:
            result = model.transcribe(event.src_path, language='en')
            logging.log(logging.INFO, result['text'])

        return super().on_created(event)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    logging.log(logging.INFO, 'watcher started')
    
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = AudioFileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
