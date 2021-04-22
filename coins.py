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
        before = self.players_coins[player]
        if (self.__players_coins[player] - amount) < 0:
            self.__players_coins[player] = 0
        else:
            self.__players_coins[player] -= amount
        after = self.players_coins[player]
        loss = before-after
        return loss


    def adquired(self,player,amount):

            self.__players_coins[player] += amount

    