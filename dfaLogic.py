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

    def processo(self, stringInput): #essencialmente o cerebro fica nessa funcao aqui e na estrutura de estados
        self.reset()
        for i in stringInput:
            if i in self.alfabeto['hiragana']:
                result = 'hiragana'
                print('por enquanto esta em japa')
            elif i in self.alfabeto['russo']:
                result = 'russo'
                print('por enquanto esta em russo')
            elif i in self.alfabeto['alfabeto_ingles']:
                result = 'alfabeto_ingles'
                print('por enquanto esta em ingles')
            else:
                result = 'outro'
            self.estadoAtual = self.transicao[self.estadoAtual].get(result, -1)
            if self.estadoAtual == -1:
                return False
        return self.estadoAtual in self.estadoAceitar


estados = {0, 1, 2, 3}
alfabeto = {
    'hiragana': [
        'あ', 'い', 'う', 'え', 'お',
        'か', 'き', 'く', 'け', 'こ',
        'さ', 'し', 'す', 'せ', 'そ',
        'た', 'ち', 'つ', 'て', 'と',
        'な', 'に', 'ぬ', 'ね', 'の',
        'は', 'ひ', 'ふ', 'へ', 'ほ',
        'ま', 'み', 'む', 'め', 'も',
        'や', 'ゆ', 'よ',
        'ら', 'り', 'る', 'れ', 'ろ',
        'わ', 'を',
        'ん'
    ],
    'russo': [
        'а', 'б', 'в', 'г', 'д',
        'е', 'ё', 'ж', 'з', 'и',
        'й', 'к', 'л', 'м', 'н',
        'о', 'п', 'р', 'с', 'т',
        'у', 'ф', 'х', 'ц', 'ч',
        'ш', 'щ', 'ъ', 'ы', 'ь',
        'э', 'ю', 'я'
    ],
    'alfabeto_ingles': [chr(i) for i in range(97, 123)]  # a até z
}

#estados aqui
transicao = {
    0: {  # detecta primeiro se é japa ou ingles ou russo (escalavel)
        'hiragana': 1,
        'alfabeto_ingles': 2,
        'russo': 3,
        'outro': 1
    },
    1: {
        'hiragana': 1,
        'alfabeto_ingles': -1,
        'russo': -1,    # enquanto for japa vai continuando
        'outro': 1
    },
    2: {
        'hiragana': -1,
        'russo': -1,
        'alfabeto_ingles': 2 # enquanto for ingles vai continuando, ingles vai ser o threshold,
        # esse estado aqui já faz errorhandling pra ver se o usuario nao ta misturando linguas
    },
    3: {
        'russo': 3,
        'alfabeto_ingles': -1,
        'hiragana': -1   # enquanto for russo vai continuando
    }
}

estadoInici = 0
estadoAceitar = {1, 2, 3}
dfa = DFA(alfabeto, estados, transicao, estadoInici, estadoAceitar)

stringInput = 'こんにちは世界'    #aqui nois vai ter que trocar pelo input do usuario dentro da gui fazuelykkkkkkk
print(dfa.processo(stringInput))  #ai vai retorna a leitura de cada char que detectou na transicao de estados mais
                                    #o resultado final que vai ser true:(tudo na lingua inicial) / false:(houve mistura de linguas)
