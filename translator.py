import anthropic
from config import API_KEY, MODEL, MAX_TOKENS


class CodeTranslator:
    """
    Handles translation of code using Anthropics API.
    """

    def __init__(self, api_key: str = API_KEY, model: str = MODEL, token_limit=50):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model
        self.token_limit = token_limit

    def get_token_count(self, text: str) -> int:
        """
        Fetch the token count for a given text using Anthropic's tokenization.
        :param text: The input text.
        :return: The number of tokens in the text.
        """
        try:
            response = self.client.messages.count_tokens(
                model="claude-3-5-sonnet-20241022",
                messages=[{"role": "user", "content": text}],
            )
            return response.input_tokens
        except Exception:
            # print(f"Error fetching token count: {e}")
            return 0

    def split_into_chunks(self, text: str, max_tokens: int):
        """
        Split the text into chunks that do not exceed the token limit.
        :param text: The input text to split.
        :param max_tokens: Maximum tokens allowed per chunk.
        :return: List of text chunks.
        """

        def is_definition_line(line: str) -> bool:
            """Check if line starts a new class or function definition."""
            stripped = line.strip()
            return (
                stripped.startswith("class ")
                or stripped.startswith("def ")
                or stripped.startswith("@")
            )

        lines = text.splitlines()
        chunks = []
        current_chunk = []
        current_token_count = 0

        for line in lines:
            line_token_count = self.get_token_count(line)

            if current_token_count + line_token_count > max_tokens and (
                is_definition_line(line) or not current_chunk
            ):
                if current_chunk:
                    chunks.append("\n".join(current_chunk))
                current_chunk = [line]
                current_token_count = line_token_count
            else:
                current_chunk.append(line)
                current_token_count += line_token_count

        # Add the last chunk if exists
        if current_chunk:
            chunks.append("\n".join(current_chunk))

        return chunks

    def translate_chunk(
        self, chunk: str, source_lang: str, target_lang: str, max_retries: int = 3
    ) -> str:
        """
        Translate a single chunk of code.
        :param chunk: Code chunk to translate.
        :param source_lang: Source programming language.
        :param target_lang: Target programming language.
        :return: Translated chunk.
        """
        prompt = f"""You are an expert programmer specializing in translating code from {source_lang} to {target_lang}. 
        Translate the code while maintaining its functionality and following best practices in {target_lang}.
        Preserve comments and documentation when possible, translating them appropriately.
        Only output the translated code without any explanations or markdown formatting."""

        retries = 0
        while retries < max_retries:
            try:
                message = self.client.messages.create(
                    model=self.model,
                    max_tokens=MAX_TOKENS,
                    system=prompt,
                    messages=[
                        {
                            "role": "user",
                            "content": f"Translate this {source_lang} code to {target_lang}:\n\n{chunk}",
                        }
                    ],
                )
                return message.content[0].text
            except Exception as e:
                retries += 1
                if retries == max_retries:
                    raise Exception(
                        f"Failed to translate chunk after {max_retries} attempts: {str(e)}"
                    )

    def translate_code(
        self, source_code: str, source_lang: str, target_lang: str
    ) -> str:
        """
        Translate the source code, splitting it if necessary based on token count.
        :param source_code: Full source code.
        :param source_lang: Source programming language.
        :param target_lang: Target programming language.
        :return: Translated code.
        """
        token_count = self.get_token_count(source_code)

        if token_count <= self.token_limit:
            # Translate the full code if within the limit
            return self.translate_chunk(source_code, source_lang, target_lang)

        chunks = self.split_into_chunks(
            source_code, self.token_limit - 500
        )  # Reserve tokens for prompt
        translated_chunks = []

        for chunk in chunks:
            translated_chunk = self.translate_chunk(chunk, source_lang, target_lang)
            translated_chunks.append(translated_chunk)

        return "\n\n".join(translated_chunks)
