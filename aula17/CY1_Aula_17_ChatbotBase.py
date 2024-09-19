#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def saudacoes(nome):
    import random
    frases = [" Bom dia! Meu nome e {}. como vai voce?".format(nome),
                "ola!", "oi, tudo bem?"]
    print(frases[random.randint(0,2)])

def recebeTexto(nome):
    texto = "Cliente: " + input("Cliente: ")
    palavraProibida = ["boco"]
    for p in palavraProibida:
        if p in texto:
            print("{}: nao vem nao! me respeite!". format(nome))
            return recebeTexto(nome)
        return texto

def buscaResposta(nome, texto):
    with open("CY1_Aula_17_BaseConhecimento.txt","a+") as base:
        base.seek(0)
        while True:
            viu = base.readline()
            if viu!= "":
                if texto.replace("Cliente: ","") == "Tchau":
                    print(" {}: volte sempre!".format(nome))
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximalinha = base.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha

            else:
                print("{}: me desculpe, nao sei o que falar".format(nome))
                base.write("\n{}".format(texto))
                resposta_user = input(("{}: o que esperava?\n".format(nome)))
                base.write("\nChatbot: {}".format(resposta_user))
                return "hum..."

def exibeResposta(resposta, nome):
    print(resposta.replace("chatbot", nome))
    if resposta == "fim":
        return "fim"
    return " continua"

