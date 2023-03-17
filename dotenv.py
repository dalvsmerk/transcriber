import platform

CP1252 = 'cp1252'
UTF8 = 'utf-8'

def is_windows():
    return platform.system() == 'Windows'


def get_platform_encoding():
    return CP1252 if is_windows() else UTF8


def try_decode_windows(text):
    if is_windows():
        return text.encode(CP1252).decode(UTF8)

    return text


def load_dotenv():
    env = dict()

    newline = '\r\n' if is_windows() else '\n'

    with open('.env', mode='r', encoding=get_platform_encoding()) as f:
        for line in f.readlines():
            line = try_decode_windows(line)
            pair = line.replace(newline, '').split('=')
            env[pair[0]] = pair[1]

    return env
