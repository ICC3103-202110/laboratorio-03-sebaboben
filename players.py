class Players:

    def __init__(self,x):
        self.jugadores = []
        self.numberplayers = x
        self.deadplayers = []

    @property
    def jugadores(self):
        return self.__jugadores

    @property
    def numberplayers(self):
        if self.__numberplayers==3 or self.__numberplayers==4:
            return self.__numberplayers
    
    @property
    def deadplayers(self):
        return self.__deadplayers

    @deadplayers.setter
    def deadplayers(self,x):
            self.__deadplayers = x

    @numberplayers.setter
    def numberplayers(self,x):
        if x == 3 or x ==4:
            self.__numberplayers = x
        #else:
        #    raise ValueError("Cantidad de jugadores no valida")

    @jugadores.setter
    def jugadores(self,x):
        self.__jugadores = x

    #Metodos
    def add_players(self):  #hacer una condicion para que no se repitan los nombres al ingresarlos
        while len(self.__jugadores) != self.__numberplayers:
            player = input("Ingrese nomnbre del jugador " + str(len(self.__jugadores)+1) + " : ") 
            self.__jugadores.append(player)

    
xdd = []
print(len(xdd))