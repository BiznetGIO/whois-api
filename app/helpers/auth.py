import os
from dotenv import load_dotenv


def load_env_file():
    home = os.path.expanduser("~")
    return load_dotenv("{}/.whois.env".format(home), override=True)


def secret_key():
    try:
        load_env_file()
        return os.environ.get("WHOIS_KEY")
    except FileNotFoundError:
        return None
