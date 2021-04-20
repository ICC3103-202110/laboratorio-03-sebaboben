from random import sample
from players import Players
from cards import Cards
from coins import Coins

#def add_to_deck(deck,card):

#def distribute_cards(deck, ,decc):
    
#def log_turs():

def interface(x,p,c):

    print("Tus cartas : {}".format(c.hands[x]))
    if len(c.withdrawed) != 0: 
        print("Cartas descartadas {}".format(c.withdrawed))
    for i in p.jugadores:
        if i != p.jugadores[x]: #hacer una condicion para que no se repitan los nombres al ingresarlos
            print(i+" tiene "+ str(len(c.hands[p.jugadores.index(i)])) +"cartas")

    print("\nEscoge una accion: ")
    print("0. Ingresos")    
    print("1. Ayuda extranjera")
    print("2. Golpe")
    print("3. Duque-Impuestos") 
    print("4. Asesino-Asesinato")  
    print("5. Capitán-Extorsión")  
    print("6. Embajador-Cambio")    
      


    





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
            action = interface(cont,players,cards)




            cont += 1
    



    #while len(Players.__deadplayers) != (x-1):


main()

