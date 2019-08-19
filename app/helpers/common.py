import whois
import os


def secret_key():
    try:
        return os.environ.get("WHOIS_KEY")
    except Exception:
        return None


def validate_domain(domain):
    supported_domains = [
        item for item in dir(whois.tld_regexpr) if not item.startswith("__")
    ]
    top_level_domain = domain.split(".")[-1]
    if top_level_domain in supported_domains:
        return True
