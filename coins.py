class Coins:

    def __init__(self):
        self.players_coins = [2,2,2,2]

    #Getters y Setters

    @property
    def players_coins(self):
        return self.__players_coins

    @players_coins.setter
    def players_coins(self,x):
        self.__players_coins = x
    

    #Metodos
    
    def lost(self,player,amount):

        if (self.__players_coins[player-1] - amount) < 0:
            self.__players_coins[player-1] = 0
        else:
            self.__players_coins[player-1] -= amount

    def adquired(self,player,amount):

        if (self.__players_coins[player-1]+amount) > 10:
            self.__players_coins[player-1] = 10
        else:
            self.__players_coins[player-1] += amount