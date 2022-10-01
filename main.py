# -*- coding: utf-8 -*- 
import random
import os
from pygame import mixer

# função usada para atualizar as perguntas e adicionar perguntas novas
def update_file(quest, choices):
    name = 'perguntas.txt'
    file = open(name, 'a')
    file.write("\n" + quest + "\n")
    choice = choices.split('/')
    for x in choice:
        file.write(x + "\n")
    
# função que pega os dados do arquivo e coloca dentro de uma lista
def read_file():
    question = []
    questions = []
    file = open('perguntas.txt', 'r')
    lines = file.readlines()
    file.close()
    # adiciona uma pergunta a uma lista, e essa lista a uma lista maior com todas as perguntas
    for line in lines:
        question.append(line)
        if len(question) == 5:
            questions.append(question)
            question = []
    return questions
# função que sorteia as perguntas automaticamente
def sort_quests(quests):
    quest = random.choice(quests)
    return quest
# função que verifica se a resposta está correta
def verification_answer(ans, quest):
    if ans in quest[4]:
        verification = True
    else:
        verification = False
    return verification

# função que analisa e atribui pontuação ao jogador
def pontuation(quest, score, player):
    ranking = []
    if "FACIL" in quest[0]:
        score += 5
    elif "MEDIO" in quest[0]:
        score += 10
    elif "DIFICIL" in quest [0]:
        score += 15
    global finalScore
    finalScore += score
    ranking.append(player)
    ranking.append(finalScore)
    return ranking

# função que cria a lista com os nome e pontuação de cada jogador
def listMaker(player, score):
    playerScore = []
    playerScore.append(player)
    playerScore.append(score)
    return playerScore

# função que cria a lista final com a pontuação dos jogadores
def fileMaker(finalList):
    filesize = os.path.getsize("rank.txt")
    file = open('rank.txt', 'r')
    if (filesize == 0):
        file = open('rank.txt', 'w')
        file.write(str(finalList))
        file.close
    else:
        file = open('rank.txt', 'a')
        file.write(str(finalList))
        file.close
# carregando a música do jogo

mixer.init()
mixer.music.load('musica.mp3')
mixer.music.set_volume(6)
mixer.music.play()
# início do programa
while True:
    print("Digite 1 para jogar somente 1 jogador \nDigite 2 para jogar 2 jogadores")
    decision_player = int(input())
    # para escolher se vai ser 1 ou 2 jogadores para o quiz
    if decision_player == 1:
        player_1 = input("Digite o nome do jogador: ")
        two_players = False
        break
    elif decision_player == 2:
        player_1 = input("Digite o nome do jogador 1: ")
        player_2 = input("Digite o nome do jogador 2: ")
        two_players = True
        break
    # para não sair do loop até que ele digite o valor correto!
    else:
        print("Digite um valor válido!")
player1_Score = 0
player2_Score = 0
score_1 = 0
score_2 = 0
answer = 5
rank = []
finalScore = 0
# menu inicial do quiz com todas as opções disponíveis para o jogador!
while answer != 0: 
    print("Bem vindo ao nosso quiz!")
    print("Menu: \n1- Para iniciar o quiz \n2- Para adicionar perguntas \n0- Para sair do jogo!")
    answer = int(input())
    quest_answ = read_file()
    n = len(quest_answ)
    # analisa a quantidade de jogadores, caso seja só um abrirá um jogo com todas as perguntas
    if not two_players: 
        if answer == 1:
            for x in range (0, 8):
                pergunta = sort_quests(quest_answ)
                quest_answ.remove(pergunta)
                for line in (range(0, len(pergunta) - 1)):
                    print(f"{pergunta[line]}", end ='')
                
                resp = input().upper()
                if resp == '0':
                    answer = 0
                    break
                correct = verification_answer(resp, pergunta)
                if resp == " ":
                    correct = False
                if correct:
                    print("Você acertou!")
                    rank = pontuation(pergunta, score_1, player_1)
                    player1_Score = rank[1]
                    listMaker(player_1, player1_Score)
                    print(player1_Score)
                    print(rank)
                else:
                    print("Você errou!")
    # caso sejam dois jogadores abrirá um código que dividirá as perguntas entre esses jogadores
    elif two_players:
        if answer == 1:
            print(f"Vamos às 6 perguntas do jogador {player_1}! \nPrepare-se!")
            for x in range(0, 6):
                pergunta = sort_quests(quest_answ)
                quest_answ.remove(pergunta)
                for line in (range(0, len(pergunta) - 1)):
                    print(f"{pergunta[line]}", end ='')
                
                resp = input().upper()
                if resp == '0':
                    answer = 0
                    break
                correct = verification_answer(resp, pergunta)
                if resp == " ":
                    correct = False
                
                if correct:
                    print("Você acertou!")
                    rank = pontuation(pergunta, score_1, player_1)
                    player1_Score = rank[1]
                    listMaker(player_1, player1_Score)
                else:
                    print("Você errou!")
            print(f"Obrigado por jogar {player_1} agora é a vez do seu oponente!")
            print(f"Vamos às 6 perguntas do jogador {player_2}! \nPrepara-se!")
            finalScore = 0
            print(finalScore)
            for x in range(0, 6):
                pergunta = sort_quests(quest_answ)
                quest_answ.remove(pergunta)
                for line in (range(0, len(pergunta) - 1)):
                    print(f"{pergunta[line]}", end ='')
                
                resp = input().upper()
                if resp == '0':
                    answer = 0
                    break
                correct = verification_answer(resp, pergunta)
                if correct:
                    print("Você acertou!")
                    rank = pontuation(pergunta, score_2, player_2)
                    player2_Score = rank[1]
                    listMaker(player_2, player2_Score)                 
                else:
                    print("Você errou!")
            if player2_Score > player1_Score:
                print(f"O jogador {player_2} foi o grande vencedor da partida!")
            else:
                print(f"O jogador {player_1} foi o grande vencedor da partida!")
                
                
            

    # para caso o jogador queira adicionar uma pergunta ao jogo direto no arquivo de texto!
    if answer == 2:
        question = input("Digite a pergunta que deseja inserir no nosso banco de dados: [Lembre-se de colocar a dificuldade ao lado como FACIL, MEDIO, DIFICIL]")
        print("Siga esse modelo para as alternativas - [A - São Paulo/B- Rio de Janeiro/C- Alemanha/C")
        print("Alternativas separadas por vírgula e no final a resposta correta em letra maiúscula!")
        choices = input("Digite as alternativas que deseja inserir e a resposta correta seguindo o modelo acima: ")
        update_file(question, choices)
    # encerra o programa e mostra o ranking final
    if answer == 0:
        print("Obrigado por jogar!")
        print('|JOGADOR|**************|PONTOS|')
        finalP1 = []
        finalP1 = listMaker(player_1, player1_Score)
        fileMaker(finalP1)
        print(f'  {player_1} ------------------> {player1_Score}')
        if(two_players == True):
            finalP2 = []
            finalP2 = listMaker(player_2, player2_Score)
            fileMaker(finalP2)
            print(f'  {player_2} ------------------> {player2_Score}')