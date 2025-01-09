import anthropic
from config import API_KEY, MODEL, MAX_TOKENS


class CodeTranslator:
    """
    Handles translation of code using Anthropics API.
    """

    def __init__(self, api_key: str = API_KEY, model: str = MODEL):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    def translate_code(
        self, source_code: str, source_lang: str, target_lang: str
    ) -> str:
        """
        Translates code from one language to another using the Anthropics API.
        :param source_code: Code to be translated.
        :param source_lang: Source language.
        :param target_lang: Target language.
        :return: Translated code as a string.
        """
        prompt = (
            f"Translate the following code from {source_lang} to {target_lang}. "
            "Ensure that the translated code is syntactically correct and idiomatic.\n\n"
            f"Source Code:\n{source_code}"
        )

        response = self.client.messages.create(
            model=self.model,
            max_tokens=MAX_TOKENS,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
