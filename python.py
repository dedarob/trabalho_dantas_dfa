import tkinter as tk
from tkinter import messagebox
import re
from langdetect import detect, DetectorFactory

# Define um estado de consistência para a detecção
DetectorFactory.seed = 0

def detectar_linguagem(texto):
    try:
        # Detecta a língua natural (como espanhol, francês, etc.)
        lingua = detect(texto)
        if lingua == 'ja':
            return "Japonês (Hiragana)"
        elif lingua == 'ru':
            return "Russo"
        elif lingua == 'en':
            return "Inglês"
        elif lingua == 'es':
            return "Espanhol"
        elif lingua == 'fr':
            return "Francês"
        elif lingua == 'de':
            return "Alemão"
        elif lingua == 'pt':
            return "Português"
        else:
            return lingua
    except:
        return "Não foi possível identificar o idioma."

def detectar_linguagem_programacao(texto):
    # Dicionário de expressões regulares para palavras-chave de cada linguagem
    linguagens = {
        "Python": r"\b(def|import|lambda|print|class|self|__init__|return|with|async|await|yield|try|except|finally|for|while|if|elif|else|break|continue|list|dict|set|tuple)\b",
        "Java": r"\b(public|private|protected|class|void|static|new|import|package|return|extends|implements|try|catch|finally|throw|throws|interface|enum|for|while|if|else|switch|case|break|continue|synchronized|this|super|abstract|final|volatile|transient)\b",
        "C": r"\b(#include|printf|scanf|main|int|float|double|char|void|return|if|else|switch|case|for|while|do|struct|typedef|enum|union|const|sizeof|malloc|free|NULL|break|continue|goto|#define)\b",
        "JavaScript": r"\b(function|const|let|var|document|window|console|alert|return|if|else|switch|case|break|continue|for|while|do|async|await|try|catch|finally|class|this|new|export|import|default|from|let|const|var)\b",
        "Ruby": r"\b(def|end|puts|class|module|include|require|attr_accessor|attr_reader|attr_writer|yield|self|super|begin|rescue|ensure|if|elsif|else|unless|while|until|for|do|break|next|redo|retry)\b",
        "PHP": r"<\?php|\b(echo|print|if|else|elseif|endif|while|do|for|foreach|break|continue|switch|case|default|function|return|include|require|namespace|class|public|private|protected|static|new|try|catch|finally)\b",
        "Assembly": r"\b(mov|int|xor|section|db|dw|dd|global|equ|cmp|jmp|loop|nop|push|pop|ret|call|lea|inc|dec|add|sub|mul|div|shr|shl|and|or|xor|not|sti|cli|hlt|cmp|je|jne|jg|jl|jge|jle)\b"
    }

    # Inicializa os pontos para cada linguagem
    pontos = {linguagem: 0 for linguagem in linguagens}

    # Aumenta os pontos para cada correspondência encontrada
    for linguagem, padrao in linguagens.items():
        if re.search(padrao, texto, re.IGNORECASE):
            pontos[linguagem] += len(re.findall(padrao, texto, re.IGNORECASE))

    # Identifica a linguagem com mais pontos
    linguagem_detectada = max(pontos, key=pontos.get)
    if pontos[linguagem_detectada] == 0:
        return "Linguagem de Programação Indefinida"
    return linguagem_detectada

def verificar_lingua():
    texto = entrada_texto.get("1.0", "end-1c")
    if not texto:
        messagebox.showinfo("Resultado", "Por favor, insira um texto.")
        return

    linguagem = detectar_linguagem_programacao(texto)
    if linguagem != "Linguagem de Programação Indefinida":
        messagebox.showinfo("Resultado", f"O texto parece ser código em {linguagem}.")
    else:
        lingua = detectar_linguagem(texto)
        messagebox.showinfo("Resultado", f"O texto está em {lingua}.")

def apagar_texto():
    entrada_texto.delete("1.0", "end")

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
