from random import sample
from players import Players
from cards import Cards
from coins import Coins

#def add_to_deck(deck,card):

#def distribute_cards(deck, ,decc):
    
#def log_turs():

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




def counteraction(player,players,cards):

    counter = look_counter_def(player,players,1)  #index of player or -1 (no counter)  

    if counter == -1:
        print("No hay contraataque")
        return 0

    else:
        print(players.jugadores[counter] + " ha contraatacado al jugador " + players.jugadores[player]) 
        challenger = challenge(counter,players,cards)
        if challenger == 0:
            print("no hay desafio")
            return 1
        





def challenge(player,players,cards):

    challenger = look_counter_def(player,players, 0)

    if challenger == -1:
        return 0


def action_played(player, action, players,cards,coins):
    action_names = ["Ingresos","Ayuda extranjera","Golpe","Duque-Impuestos","sesino-Asesinato","Capitán-Extorsión","Embajador-Cambio"]

    if action == 0:
        coins.adquired(player,1)

    elif action == 1:
        interaction = counteraction(player,players,cards)
        if interaction == 0:
            coins.adquired(player,2)
        


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

