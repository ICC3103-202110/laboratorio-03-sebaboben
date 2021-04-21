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
        withdrawed_card = int(input("Que carta deseas eliminar : \n1.-" + cards.hands[player][0]+ "\n2.-"+cards.hands[player][1]))
        cards.withdrawed.append(cards.hands[player].pop(withdrawed_card-1))
    else:
        cards.withdrawed.append(cards.hands[player].pop(0))
        print("El jugador"+ players.jugadores[player]+ "queda eliminado")
        players.deadplayers.append(players.jugadores[player])
    



def interface(x,p,c,k):
    showcards = input("Quieres ver tus cartas\n Si/No\n")
    if showcards.upper() == "SI":
        print("Tus cartas : {}".format(c.hands[x]))
    
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

    return response


        
def look_counter_def(player,players,cod):
    x = ["desafiante","contraatacante"]
    d = ["desafiar","contraatacar"]
    counter = []
    for i in players.jugadores:
        if i != players.jugadores[player]: 
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
            else:
                print(players.jugador[player] + " si posee la carta "+counter_card(1))
                print("\n"+players.jugadores[challenger]+ " ha perdido una carta de influencia")
                loose_influence(challenger,cards,players) 
                cards.changecard(player,cards.hands[player].index(counter_card(1))) 

        else:
            if counter_card(action) not in cards.hands[player]:
                print("\n"+players.jugadores[player]+ " ha perdido una carta de influencia")
                loose_influence(player,cards,players) 
            else:
                print(players.jugador[player] + " si posee la carta "+counter_card(1))
                print("\n"+players.jugadores[challenger]+ " ha perdido una carta de influencia")
                loose_influence(challenger,cards,players) 
                cards.changecard(player,cards.hands[player].index(counter_card(1)))    
        return 1

        



def action_played(player, action, players,cards,coins):
    action_names = ["Ingresos","Ayuda extranjera","Golpe","Duque-Impuestos","Asesino-Asesinato","Capitán-Extorsión","Embajador-Cambio"]

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
            if i != players.jugadores[player]: 
                print(i) 
        while attack not in players.jugadores 
            attack = input()
        attack_index = players.jugadores.index(attack)
        loose_influence(attack_index,cards,players)

    elif action ==3:
        interaction = counteraction(player,players,cards,action)
        if interaction == 0:
            coins.adquired(player,3)


    elif action == 4:

        


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

    for 

    while len(players.deadplayers) != (x-1):

        if cont == (x+1):
            cont = 0
            rounds += 1
            return print("Ronda "+ str(rounds) + "terminada")

        if players.jugadores[cont] in players.deadplayers:
            cont +=1    
        else:
            action = interface(cont,players,cards,coins)
            action_played(cont, action, players,cards, coins)




            cont += 1
    



    #while len(Players.__deadplayers) != (x-1):


main()

