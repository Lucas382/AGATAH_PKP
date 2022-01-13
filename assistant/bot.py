import json

class Bot():
    def __init__(self, bot_name):
        try:
            memory = open(bot_name+'.json', 'r')
        except FileNotFoundError:
            memory = open(bot_name+'.json', 'w')
            memory.write('["Lucas"]')
            memory.close()
            memory = open(bot_name+'.json', 'r')

        self.phrase = {'oi': 'Olá, qual o seu nome?', 'tchau': 'tchau'}
        self.known_names = json.load(memory)
        memory.close()
        self.bot_name = bot_name
        self.history = []

    def bot_speaker(self, phrase):
        print(phrase)
        self.history.append(phrase)

    def bot_listener(self):
        phrase = input('>: ')
        phrase = phrase.lower()
        phrase = phrase.replace('é', 'eh')
        return phrase

    def bot_tinker(self, phrase):
        if phrase in self.phrase:
            return self.phrase[phrase]
        if phrase == 'aprende':
            key = input('Digite a frase a ser aprendida: ')
            resp = input('Digite a resposta a frase aprendida: ')
            self.phrase[key] = resp
            return 'Aprendido'
        if self.history[-1] == 'Olá, qual o seu nome?':
            name = self.get_name(phrase)
            resp = self.response_name(name)
            return resp
        try:
            resp = eval(phrase)
            return resp
        except:
            pass
        return 'Não entendi ?_? '

    def get_name(self, name):
        if 'o meu nome eh ' in name:
            name = name[14:]
        name = name.title()
        return name

    def response_name(self, name):
        if name in self.known_names:
            phrase = 'Eaew '
        else:
            phrase = 'Muito prazer '
            self.known_names.append(name)
            with open(self.bot_name+'.json', 'w') as data:
                json.dump(self.known_names, data)

        return phrase+name
