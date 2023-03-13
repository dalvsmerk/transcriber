# Watch .mp3 audio -> Transcribe -> Send to Whatsapp

## Installation

1. Install dependencies
```shell
pip install -r requirements.txt
```

2. Rename `.env.example` to `.env`
3. Specify name of Whatsapp group in `.env` file where to send transcriptions. For example:
```
WHATSAPP_GROUP_NAME=Name of Whatsapp group
WHISPER_LANGUAGE=en
```


## How to use

1. Run the script, where `<dir>` is the folder with audio files.
```shell
python watch.py <dir>
```

For example
```shell
python watch.py C:\Folder\Data
```

2. Google Chrome window with web Whatsapp will be open, login there using your account (link device).
3. Here you can collapse the window with Whatsapp and the script will control that window to send messages to the Whatsapp group.

## How it works
This script will watch for creation of new files in `<dir>` and its subdirectories
and send transcriptions as messages to the Whatsapp group in format:
```
<file name>

<transcription line 1>
<transcription line 2>
<transcription line N>
```

## Why not use Whatsapp Cloud API

Currently, Whatsapp Cloud API does not support sending messages to group chats (event for Business accounts).
