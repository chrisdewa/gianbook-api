import tomllib as toml

with open('config.toml', 'rb') as f:
    CONFIG = toml.load(f)

DB_URL = CONFIG['DB']['url']