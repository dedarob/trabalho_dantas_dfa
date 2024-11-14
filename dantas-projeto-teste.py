from langdetect import detect
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound


text = "Ich bin Roberto aus Brasilien"
lang = detect(text)
print(lang)

def guess_language(code):
    try:
        lexer = guess_lexer(code)
        return lexer.name
    except ClassNotFound:
        return "Unknown"

code = """def soma(a, b):
    return a + b

num1 = 5
num2 = 7
resultado = soma(num1, num2)

print(f'A soma de {num1} e {num2} é {resultado}')

"""
print(guess_language(code))

