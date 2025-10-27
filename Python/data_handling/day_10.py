#Fernet Symmetric encryption
# pypi for packages

import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_TIME = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE , "wb") as f :
            f.write(key)
    else:
        wi