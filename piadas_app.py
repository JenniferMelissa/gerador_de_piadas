#pacotes instalados no prompt: pip install pyjokes(pacote de piadsa), depois, pip install deep_translator (para traduzir as pidas que sao geradas em ingles)
#tem imports que precisa pagar, nao sao de graca
#usa o from para importa a bliblioteca porque nao precisamos do pacote todo, so algumas partes, pois o pacote é pesado e com isso pesar o programa

#importar biblioteca
import pyjokes   #pip install pyjokes, precisa atualizar para ultima versao funcionar
from deep_translator import GoogleTranslator  # pip install deep_translator, precisa atualizar para ultima versao funcionar

#simplifica o comando
#surce: identifica o idioma da piada
tradutor = GoogleTranslator(source='auto', target='pt')

while True:
    #get é pegar o valor que ja existe, nesse caso, vai puxar a piada que ja existe
    piada = pyjokes.get_joke() 
    piada_traduziada = tradutor.translate(piada)

    print(piada_traduziada)

    repetir = input('Gerar outra piada s/n? ').lower()

    if repetir == 's':
        continue
    else:
        break

    