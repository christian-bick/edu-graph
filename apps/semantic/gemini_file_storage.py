import os
from tkinter.font import names

import google.generativeai as gemini

gemini.configure(api_key=os.environ["API_KEY_GEMINI"])

class GeminiFileStorage:

    @staticmethod
    def upload(name, mime_type, file):
        return gemini.upload_file(
            path=file,
            name=name,
            mime_type=mime_type
        )

    @staticmethod
    def get(name):
        return gemini.get_file(name=name)