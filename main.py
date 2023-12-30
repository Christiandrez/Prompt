from dotenv import load_dotenv
import re

import os

from llm.service.inference import InferenceService
from llm.utils.const import CLEAN_TEXT

if __name__ == '__main__':
    load_dotenv('secrets/.env')
    #print(os.getenv('OPENAI_API_KEY'))
    print(InferenceService().invoke('2017'))

    print(f'Ingrese un nombre: ')
    nombre = input()
    nombre_result = InferenceService().invoke_name(nombre)
    print(f"Quien es {nombre}: {nombre_result}")

    print(f'Ingrese el numero para cambiar a binario: ')
    numero = input()
    numero_result = InferenceService().invoke_binario(numero)
    print(f"El numero {numero} en binario es: {numero_result}")