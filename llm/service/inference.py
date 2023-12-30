import os
import string

from openai import OpenAI

from llm.utils.const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT


class InferenceService:
    def __init__(self):
        self.__model = os.getenv('OPENAI_MODEL', 'text-davinci-003')
        self.__openai_client = OpenAI()
        self.__prompt_template = 'Who won GOTY in {year}?'
        self.__prompt_template_name = 'Quien es {nombre}?'

    def __inference(self, prompt):
        return CLEAN_TEXT(self.__openai_client.completions.create(
            model=self.__model,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        ).choices[0].text)

    def invoke(self, year: str) -> str:
        prompt = self.__prompt_template.format(year=year)
        return self.__inference(prompt)

    def invoke_name(self, nombre: str) -> str:
        prompt = self.__prompt_template_name.format(nombre=nombre)
        return self.__inference(prompt)