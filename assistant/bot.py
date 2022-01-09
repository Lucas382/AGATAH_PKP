from dataclasses import dataclass, field
from typing import List



@dataclass()
class Bot:
    bot_name: str = 'botolino'
    history: List[str] = field(default_factory=list)
    known_names: List[str] = field(default_factory=list)


    def bot_speaker(self, phrase):
        print(phrase)
        self.history.append(phrase)

    def bot_listener(self):
        phrase = input('>: ')
        phrase = phrase.lower()
        phrase = phrase.replace('é', 'eh')
        return phrase

    def bot_tinker(self, phrase):
        if phrase == 'oi':
            return 'Olá, qual o seu nome?'
        if self.history[-1] == 'Olá, qual o seu nome?':
            name = self.get_name(phrase)
            resp = self.response_name(name)
            return resp
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

        return phrase+name
