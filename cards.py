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
        shuffle_deck()
            

    
