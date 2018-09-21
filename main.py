def run():
    # Your code goes here.
    #global temperaturearray 
    #temperaturearray = []
    def addReading():
        #temperaturearray = []
        str_temp = float(input("What was the temperature?\n"))
        temperaturearray.append(str_temp)
        #return 
    def editReading():
        #temperaturearray = []
        int_editPosition = int(input("Edit reading at which position?\n"))
        temperaturearray.pop(int_editPosition - 1)
        #if statement if user goes outside number
        float_newValue = input("What should the value be instead?\n")
        temperaturearray.insert(int_editPosition - 1, float_newValue)
    def printReading():
        int_valueNum = 0
        while int_valueNum <= len(temperaturearray) - 1:
            print(str(int_valueNum + 1) + ": " + str(temperaturearray[int_valueNum]))
            int_valueNum = int_valueNum + 1
        #return
    def removeReading():
        int_removePosition = input("Remove reading at which position?\n")
        int_removePosition = int(int_removePosition)
        temperaturearray.pop(int_removePosition)
    def listofFunctions():
        print("[A]dd a reading.\n[E]dit a reading.\n[P]rint existing readings.\n[R]emove a reading.\n[Q]uit.")
        #return
    
    #start of program
    temperaturearray = []
    int_runFunction = print("What should the program do?")
    listofFunctions()
    int_askUser = input()
    while int_askUser != "Q":
        if int_askUser == "A":
            addReading()
        elif int_askUser == "E":
            editReading()
        elif int_askUser == "P":
            printReading()
        elif int_askUser == "R":
            removeReading()
        int_runFunction = print("What should the program do?")
        listofFunctions()
        int_askUser = input()
    print("Goodbye!")
# Don't change anything below this line.
if __name__ == "__main__":
    run()
