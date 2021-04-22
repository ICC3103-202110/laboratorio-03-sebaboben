from random import sample
from players import Players
from cards import Cards
from coins import Coins

def counter_card(action):

    if action == 1:
        return "Duque"
    elif action == 3:
        return "Duque"
    elif action == 5:      
        return ["Embajador","Capitan"]
    elif action == 4:      
        return "Condesa"
    elif action == 6:
        return "Embajador"
    elif action ==7:  #capitan-extorsion desafio
        return "Capitan"
    elif action==8:   #asesino-asesinar desafio  
        return "Asesino"

def loose_influence(player,cards,players):
    if len(cards.hands[player]) == 2:
        withdrawed_card = int(input("Que carta deseas eliminar : \n1.-" + cards.hands[player][0]+ "\n2.-"+cards.hands[player][1]+"\n"))
        cards.withdrawed.append(cards.hands[player].pop(withdrawed_card-1))
    else:
        cards.withdrawed.append(cards.hands[player].pop(0))
        print("El jugador "+ players.jugadores[player]+ " queda eliminado")
        players.deadplayers.append(players.jugadores[player])
    

def interface(x,p,c,k):
    showcards = input("Quieres ver tus cartas\n Si/No\n")
    if showcards.upper() == "SI":
        print("\nTus cartas : {}".format(c.hands[x]))
    
    if len(c.withdrawed) != 0: 
        print("Cartas descartadas {}".format(c.withdrawed))
    for i in p.jugadores:
        if i != p.jugadores[x]: #hacer una condicion para que no se repitan los nombres al ingresarlos
            print(i+" tiene "+ str(len(c.hands[p.jugadores.index(i)])) +" influencias y " + str(k.players_coins[p.jugadores.index(i)]) + " monedas") 

    if k.players_coins[x] >= 10: 
        print("Tienes 10 monedas, estas obligado a atacar")
        return 2

    print("\nAcciones: \n")
    print("0. Ingresos")    
    print("1. Ayuda extranjera")
    print("2. Golpe")
    print("3. Duque-Impuestos") 
    print("4. Asesino-Asesinato")  
    print("5. Capitán-Extorsión")  
    print("6. Embajador-Cambio")

    response = -1
    while response > 6 or response < 0:
        print("\nEscoge una accion: ")
        response = int(input())
        if response == 2 and k.players_coins[x] < 7 :
            print("No tienes suficientes monedas para realizar esta accion\n")
            response = -1
        elif response == 4 and k.players_coins[x] < 3:
            print("No tienes suficientes monedas para realizar esta accion\n")
            response = -1
        elif response == 5:
            extorted =[]
            for i in p.jugadores:
                if i != p.jugadores[x] and i not in p.deadplayers and k.players_coins[p.jugadores.index(i)] != 0: 
                    extorted.append(p.jugadores[x])
            if len(extorted) == 0:
                print("El resto de los jugadores no tienen monedas, no puedes ejecutar extorsion") 
                response = -1

    return response


        
def look_counter_def(player,players,cod):
    x = ["desafiante","contraatacante"]
    d = ["desafiar","contraatacar"]
    counter = []
    for i in players.jugadores:
        if i != players.jugadores[player] and i not in players.deadplayers: 
            value = input(i+ ", quieres " + d[cod] + " la accion del jugador "+ players.jugadores[player]+ "\n Si/No\n")
            if value.upper() == "SI":
                counter.append(players.jugadores.index(i))

    if len(counter) == 0:
        return -1
    elif len(counter) != 1:
        counter = sample(counter,k=1)
        print("El "+ x[cod] +" sorteado fue "+ players.jugadores[counter[0]])   

    return counter[0]    




def counteraction(player,players,cards,action):

    counter = look_counter_def(player,players,1)  #index of player or -1 (no counter)  

    if counter == -1:
        print("No hay contraataque")
        return 0

    else:
        print(players.jugadores[counter] + " ha contraatacado al jugador " + players.jugadores[player]) 
        challenger = challenge(counter,players,cards,action)
        if challenger == 0:
            print("no hay desafio")
            return 1
        
            

def challenge(player,players,cards,action):

    challenger = look_counter_def(player,players, 0)

    if challenger == -1:
        return 0
    else:
        if len(counter_card(action)) == 2:
            if counter_card(action)[0] not in cards.hands[player]  and  counter_card(action)[1] not in cards.hands[player]:
                print("\n"+players.jugadores[player]+ " ha perdido una carta de influencia")
                loose_influence(player,cards,players)   
                return 1               
            else:
                print(players.jugador[player] + " si posee la carta "+counter_card(action))
                print("\n"+players.jugadores[challenger]+ " ha perdido una carta de influencia")
                loose_influence(challenger,cards,players) 
                cards.changecard(player,cards.hands[player].index(counter_card(action)))
                return 2

        else:
            if counter_card(action) not in cards.hands[player]:
                print("\n"+players.jugadores[player]+ " ha perdido una carta de influencia")
                loose_influence(player,cards,players) 
                return 1
            else:
                print(players.jugadores[player] + " si posee la carta "+counter_card(action))
                print("\n"+players.jugadores[challenger]+ " ha perdido una carta de influencia")
                loose_influence(challenger,cards,players) 
                cards.changecard(player,cards.hands[player].index(counter_card(action))) 
                return 2

def action_played(player, action, players,cards,coins):

    if action == 0:
        coins.adquired(player,1)

    elif action == 1:
        interaction = counteraction(player,players,cards,action)
        if interaction == 0:
            coins.adquired(player,2)
    
    elif action == 2: 
        coins.lost(player,7)
        print("Que jugador quieres atacar")
        attack = ""
        for i in players.jugadores:
            if i != players.jugadores[player] and i not in players.deadplayers: 
                print(i) 
        while attack not in players.jugadores: 
            attack = input()
        attack_index = players.jugadores.index(attack)
        loose_influence(attack_index,cards,players)

    elif action ==3:
        interaction = challenge(player,players,cards,action)
        if interaction == 0:
            coins.adquired(player,3)

    elif action == 4:
        coins.lost(player,3)
        print("Que jugador quieres atacar")
        attack = ""
        for i in players.jugadores:
            if i != players.jugadores[player] and i not in players.deadplayers: 
                print(i) 
        while attack not in players.jugadores: 
            attack = input()


        interaction = counteraction(player,players,cards,action)
        
        if interaction == 0:
            interaction = challenge(player,players,cards,8)
            if interaction == 1:
                coins.adquired(player,3)
            else:
                loose_influence(attack,cards,players) 
        elif interaction == 1:
            print("Han contraatacado un Asesinato")


    elif action == 5:
        print("A cual jugador le deseas robar")
        attack = ""
        for i in players.jugadores:
            if i != players.jugadores[player] and i not in players.deadplayers and coins.players_coins[players.jugadores.index(i)] != 0: 
                print(i) 
        while attack not in players.jugadores: 
            attack = input()


        interaction = counteraction(player,players,cards,action)
        
        if interaction == 0:
            interaction = challenge(player,players,cards,7)
            if interaction == 0 or interaction == 1:
                coins.adquired(player,coins.lost(player,2))
        elif interaction == 1:
            print("Han contraatacado un Robo")
    
    elif action == 6:
        interaction = challenge(player,players,cards,action)    

        if interaction == 0 or interaction == 2:
            cards.exchange(player)
        


def main():
    
    cards = Cards()
    coins = Coins()

    x = int(input("Indique la cantidad de jugadores (3-4): "))
    players = Players(x)
    players.add_players()

    cards.shuffle_deck()
    cards.distribute_cards(x)
    
    cont = 0
    rounds = 0

    while len(players.deadplayers) != (x-1):

        if cont == (x):
            cont = 0
            rounds += 1
            print("\nRonda "+ str(rounds) + " terminada")


        if players.jugadores[cont] in players.deadplayers:
            cont +=1    
        else:
            print("\nEs el turno de "+ players.jugadores[cont]+"\n")
            action = interface(cont,players,cards,coins)
            action_played(cont, action, players,cards, coins)

            cont += 1
    
    for i in players.jugadores:
        if i not in players.deadplayers:
            print("\n"+ i +" ha ganado el juego")




main()

