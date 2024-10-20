from pathlib import Path

ENCODING = "UTF-8"

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

FRONTEND_DIR = PROJECT_DIR.joinpath('web/')

CLIENT_DIR = PROJECT_DIR.joinpath('client/')

BACKEND_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = BACKEND_DIR.joinpath('api/templates/')
STATIC_DIR = BACKEND_DIR.joinpath('api/statics/')

ENV_FILE = BACKEND_DIR.joinpath('.env')
