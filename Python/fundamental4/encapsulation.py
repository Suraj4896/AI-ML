class BankAccount:
    def __init__(self, name, balance, id):
        self.name = name #public by default
        self._balance = balance #protected
        self.__id = id #private
    
    def get_id(self):
        return self.__id
    
    def set_id(self, newId):
        self.__id = newId
        