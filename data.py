from prettytable import PrettyTable as pt
class score_board:
    def __init__(self, __tpl:tuple, __name:str, __age:int, __scores:float):
        self.__tpl = __tpl
        self.__name = __name
        self.__age = __age
        self.__scores = __scores

# < Setter Getter
    @property
    def tpl(self):
        return self.__tpl

    @tpl.setter
    def tpl(self, __tpl):
        self.__tpl = __tpl

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, __name):
        self.__name = __name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, __age):
        self.__age = __age

    @property
    def scores(self):
        return self.__scores
    
    @scores.setter
    def scores(self, __scores):
        self.__scores = __scores
# End Setter Getter > 

# < Functions
    def choices(self):
        menuQ = [
                "[1] Show all data", 
                "[2] Select data", 
                "[3] Show selected data", 
                "[4] Change the Name", 
                "[5] Change the Age", 
                "[6] Change the Score", 
                "[0] Shut down"
                ]

        for i in menuQ:
            print(i)

    def showTable(self, index): # untuk menampilkan tuple ke prettytable
        colItems = ["#", "Name", "Age", "Score"]
        newPT = pt()
        newPT.field_names = colItems
        for r in self.__tpl:
            newPT.add_row(r)
        print(f"{newPT}\n")
        print(f"[i] Selected data is #{index}\n")

    def showSelected(self, index): # menampilkan data sesuai index yg dipilih
        colItems = ["#", "Name", "Age", "Score"]
        newPT = pt()
        newPT.field_names = colItems
        newPT.add_row([index, self.__name, self.__age, self.__scores])
        print(f"\n{newPT}\n")

    def editAttr1(self, index): # merubah atribut 1 yaitu name
        print(f"[i] Current Name : {self.__name}\n")
        newName = input("[=] New Name : ")
        if(newName.isdigit() or newName == ""):
            print(f"[!] Invalid Inputs! Name is reverted to {self.__name}\n")
        else:
            print(f"[i] Name changed from {self.__name} to {newName}\n")
            self.__name = newName
            self.__tpl[index][1] = self.__name
         
    def editAttr2(self, index): # merubah atribut 2 yaitu age
        print(f"[i] Current Age : {self.__age}\n")
        newAge = input("[=] New Age : ")
        if(newAge.isdigit()):
            print(f"[i] Age changed from {self.__age} to {newAge}\n")
            self.__age = newAge
            self.__tpl[index][2] = self.__age
        else:
            print(f"[!] Invalid Inputs! Age is reverted to {self.__age}\n")
        
    def editAttr3(self, index): # merubah atribut 3 yaitu score
        print(f"[i] Current Score : {self.__scores}\n")
        newScore = input("[=] New Score : ")
        if(newScore == ""):
            print(f"[!] Invalid Inputs! Score is reverted to {self.__scores}\n")
        elif(newScore.isalpha()):
            print(f"[!] Invalid Inputs! Score is reverted to {self.__scores}\n")
        elif(float(newScore) > 10.0):
            print(f"[!] Exceded maximum score! Score is reverted to {self.__scores}\n")
        elif(float(newScore) < 0.1):
            print(f"[!] Score is below 0.1! Score is reverted to {self.__scores}\n")
        else:
            print(f"[i] Score changed from {self.__scores} to {newScore}\n")
            self.__scores = newScore
            self.__tpl[index][3] = self.__scores    
# End Functions>