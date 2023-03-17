import platform

CP1251 = 'cp1251'
UTF8 = 'utf-8'

def is_windows():
    return platform.system() == 'Windows'


def get_platform_encoding():
    return CP1251 if is_windows() else UTF8


def try_decode_windows(text):
    if is_windows():
        return text.encode(CP1251).decode(UTF8)

    return text


def load_dotenv():
    env = dict()

    with open('.env', mode='r', encoding=get_platform_encoding()) as f:
        for line in f.readlines():
            line = try_decode_windows(line)
            pair = line.replace('\r', '').replace('\n', '').split('=')
            env[pair[0]] = pair[1]

    return env
