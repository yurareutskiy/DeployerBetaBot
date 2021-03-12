from dotenv import load_dotenv

import os

def setup():
    load_dotenv()
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER")
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    print("Port:", os.environ.get("PORT"))