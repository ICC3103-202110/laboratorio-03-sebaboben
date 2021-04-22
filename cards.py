from random import sample

class Cards:

    def __init__(self):
        self.hands = []
        self.deck = ["Asesino","Embajador","Condesa","Capitan","Duque"]*3
        self.withdrawed = []

    @property
    def hands(self):
        return self.__hands

    @property
    def deck(self):
        return self.__deck
    
    @property
    def withdrawed(self):
        return self.__withdrawed
            
    @hands.setter
    def hands(self,x):
        self.__hands = x

    @deck.setter
    def deck(self,x):
        if len(x) > 0:
            self.__deck = x

    @withdrawed.setter
    def withdrawed(self,x):
        self.__withdrawed = x
    

    #Metodos

    def shuffle_deck(self):
        d = self.__deck
        d = sample(d,k = len(d))
        self.deck = d

    def distribute_cards(self, nplayers):
        for i in range(nplayers):
            l_togo = []
            for x in range(2):
                l_togo.append(self.__deck.pop(0))
            self.__hands.append(l_togo)

    def changecard(self,player,card):
        top_deck = self.__deck.pop(0)
        hand_card = self.__hands[player].pop(card)
        self.__hands[player].append(top_deck)
        self.__deck.append(hand_card)
        self.shuffle_deck()


    def exchange(self,player):
        tradeables = []
        x = 0
        while x < len(self.__hands[player]):
            tradeables.append(self.__hands[player][x])
            x += 1
        tradeables.append(self.__deck.pop(0))  
        tradeables.append(self.__deck.pop(1))

        print("Escoje el numero de 2 cartas para devolver al deck: ")
        x = 0
        while x < len(tradeables):
            print(str(x+1)+".- "+ tradeables[x])
            x += 1
        
        card1 = int(input("Primera carta: ")) -1
        card2 = int(input("Segunda carta: ")) -1

        while card1 == card2:
            card2 = int(input("Segunda carta: ")) -1

        card1=tradeables[card1]
        card2=tradeables[card2]

        self.__deck.append(card1)
        self.__deck.append(card2)
        self.shuffle_deck
        
        tradeables.remove(card1)
        tradeables.remove(card2)

        self.__hands[player]= tradeables


    
            

    
