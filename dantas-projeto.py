import tkinter as tk
from tkinter import messagebox

class DFA:
    def __init__(self, alfabeto, estados, transicao, estadoInici, estadoAceitar):
        self.alfabeto = alfabeto
        self.estados = estados
        self.transicao = transicao
        self.estadoInici = estadoInici
        self.estadoAceitar = estadoAceitar
        self.estadoAtual = estadoInici

    def reset(self):
        self.estadoAtual = self.estadoInici

    def processo(self, stringInput):
        self.reset()
        tokens = stringInput.split()  # Divide a entrada em palavras/tokens

        for token in tokens:
            if token in self.alfabeto['python']:
                result = 'python'
            elif token in self.alfabeto['java']:
                result = 'java'
            elif token in self.alfabeto['c']:
                result = 'c'
            elif any(char in self.alfabeto['hiragana'] for char in token):
                result = 'hiragana'
            elif any(char in self.alfabeto['russo'] for char in token):
                result = 'russo'
            elif all(char in self.alfabeto['alfabeto_ingles'] for char in token.lower()):
                result = 'alfabeto_ingles'
            else:
                result = 'outro'

            self.estadoAtual = self.transicao[self.estadoAtual].get(result, self.estadoAtual)
        return self.estadoAtual in self.estadoAceitar

def verificar_lingua():
    texto = entrada_texto.get("1.0", "end-1c")
    if not texto:
        messagebox.showinfo("Resultado", "Por favor, insira um texto.")
        return

    if dfa.processo(texto):
        if dfa.estadoAtual == 1:
            lingua = "Japonês (Hiragana)"
        elif dfa.estadoAtual == 2:
            lingua = "Alfabeto Latino/Romano"
        elif dfa.estadoAtual == 3:
            lingua = "Russo"
        elif dfa.estadoAtual == 4:
            lingua = "Python"
        elif dfa.estadoAtual == 5:
            lingua = "Java"
        elif dfa.estadoAtual == 6:
            lingua = "C"
        else:
            lingua = "Indefinido"
        messagebox.showinfo("Resultado", f"O texto está em {lingua}.")
    else:
        messagebox.showinfo("Resultado", "Não foi possível identificar o idioma ou linguagem.")

def apagar_texto():
    entrada_texto.delete("1.0", "end")

estados = {0, 1, 2, 3, 4, 5, 6}
alfabeto = {
    'hiragana': ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ',
                 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ',
                 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん'],
    'russo': ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
              'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'],
    'alfabeto_ingles': [chr(i) for i in range(97, 123)],  # a até z
    'python': ['def', 'import', 'self', ':', 'if', 'else', 'elif', 'for', 'in', 'print',
               'and', 'or', 'not', '=', '==', '(', ')', '[', ']', '{', '}', 'lambda'],
    'java': ['class', 'public', 'static', 'void', 'main', 'String', 'int', 'new', 'return',
             'import', 'package', 'if', 'else', 'for', 'while', 'boolean', '==', '{', '}'],
    'c': ['#include', 'int', 'main', 'printf', 'scanf', 'return', 'void', '{', '}', 'char',
          'if', 'else', 'for', 'while', 'switch', 'case', '==', ';']
}
transicao = {
    0: {'hiragana': 1, 'alfabeto_ingles': 2, 'russo': 3, 'python': 4, 'java': 5, 'c': 6, 'outro': 0},
    1: {'hiragana': 1, 'alfabeto_ingles': 1, 'russo': 1, 'python': 1, 'java': 1, 'c': 1, 'outro': 1},
    2: {'hiragana': 2, 'alfabeto_ingles': 2, 'russo': 2, 'python': 2, 'java': 2, 'c': 2, 'outro': 2},
    3: {'hiragana': 3, 'alfabeto_ingles': 3, 'russo': 3, 'python': 3, 'java': 3, 'c': 3, 'outro': 3},
    4: {'hiragana': 4, 'alfabeto_ingles': 4, 'russo': 4, 'python': 4, 'java': 4, 'c': 4, 'outro': 4},
    5: {'hiragana': 5, 'alfabeto_ingles': 5, 'russo': 5, 'python': 5, 'java': 5, 'c': 5, 'outro': 5},
    6: {'hiragana': 6, 'alfabeto_ingles': 6, 'russo': 6, 'python': 6, 'java': 6, 'c': 6, 'outro': 6}
}
estadoInici = 0
estadoAceitar = {1, 2, 3, 4, 5, 6}
dfa = DFA(alfabeto, estados, transicao, estadoInici, estadoAceitar)

# GUI
root = tk.Tk()
root.title("Detecção de Idiomas e Linguagens de Programação")
root.geometry("400x300")

titulo = tk.Label(root, text="Verificador de Linguagens", font=("Arial", 16))
titulo.pack(pady=10)

instrucao = tk.Label(root, text="Digite o texto ou código e clique em 'Processar'")
instrucao.pack()

entrada_texto = tk.Text(root, height=5, width=40)
entrada_texto.pack(pady=10)

botao_processar = tk.Button(root, text="Processar", command=verificar_lingua, bg="lightblue")
botao_processar.pack(pady=5)

botao_apagar = tk.Button(root, text="Apagar", command=apagar_texto, bg="lightgray")
botao_apagar.pack(pady=5)

root.mainloop()
