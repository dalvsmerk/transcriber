import sys
import time
import logging
from watchdog.observers import Observer
from dotenv import load_dotenv
from model import Whisper
from audio_handler import AudioFileEventHandler
from whatsapp import Whatsapp


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s]\t%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    watch_dir_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    env = load_dotenv()

    logging.log(logging.INFO, 'Loading Whisper...')
    model = Whisper(logging, language=env['WHISPER_LANGUAGE'])
    logging.log(logging.INFO, 'Whisper has loaded')
    
    logging.log(logging.INFO, 'Loading Whatsapp...')
    whatsapp = Whatsapp(logging, group_name=env['WHATSAPP_GROUP_NAME'])
    logging.log(logging.INFO, 'Whatsapp has loaded')

    event_handler = AudioFileEventHandler(model, whatsapp, logging)
    observer = Observer()
    observer.schedule(event_handler, watch_dir_path, recursive=True)
    observer.start()

    logging.log(logging.INFO, 'Watcher of "{}" directory started'.format(watch_dir_path))
    logging.log(logging.INFO, 
        'Transcriptions will be sent to "{}" Whatsapp group'
        .format(env['WHATSAPP_GROUP_NAME'])
    )

    try:
        while True:
            time.sleep(1)
    except:
        observer.stop()
        observer.join()

    try:
        whatsapp.close()
    except:
        logging.log(logging.INFO, 'Whatsapp has closed')
