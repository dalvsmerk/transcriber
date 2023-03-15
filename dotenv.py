def load_dotenv():
    env = dict()

    with open('.env', mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            pair = line.replace('\n', '').split('=')
            env[pair[0]] = pair[1]

    return env
