class HangingShape :
    instance: 'HangingShape' = None

    #add shape (composition)
    numOfTries = 0
    DefaultNumOfTries = 7

    def __init__(self):
        if HangingShape.instance is None :
            HangingShape.instance = self #?does it also apply to the children? if a child is created, so is HangingShape instance the child?


    def SetSelfAsNewView(self):
        HangingShape.instance = self
        return self

    def RenderNext(self, isCorrect : bool):
        if(not isCorrect):
            int(self.instance.numOfTries).__sub__(1)
            print("number of tries left is " + str(self.numOfTries))

    def ResetView(self, numOfTries = DefaultNumOfTries):
        self.instance.numOfTries = HangingShape.DefaultNumOfTries

    def ResetNumOfTries(self, num):
        self.instance.numOfTries = num
        return self

    def SetDefaultNumOfTries(self):
        print("Please choose your desired number of tries")
        num = input()
        if(num.isnumeric()):
            HangingShape.DefaultNumOfTries = num
            self.instance.numOfTries = HangingShape.DefaultNumOfTries
        else:
            print("You didn't type a number. Please choose one.")
            self.setDefaultNumOfTries(input(), 0)

        return self


    def setDefaultNumOfTries(self, num, iter):
        print("Please choose your desired number of tries")
        if (num.isnumeric()):
            self.DefaultNumOfTries = num
        elif(iter < 4):
            print("You didn't type a number. Please choose one.")
            iter+=1
            self.setDefaultNumOfTries(input(), iter)
