#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Prova():

    def __init__(self):
        self.questao = []
        self.resposta = []
        
    def mostra_Questoes(self):
        print(self.questao)

    def mostra_Respostas(self):
        print(self.resposta)


    def armazena_Questao_Resposta(self, novaQuestao,novaResposta):
        self.questao.append(novaQuestao)
        self.resposta.append(novaResposta)

