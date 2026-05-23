import re


class TextCleaner:

    @staticmethod
    def clean_text(text):

        text = re.sub(r'\s+', ' ', text)

        text = re.sub(r'Page \d+', '', text)

        text = text.strip()

        return text
