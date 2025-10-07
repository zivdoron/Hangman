import operator


class HangingShape :
    instance: 'HangingShape' = None

    #add shape (composition)
    numOfAttempts = 0
    DefaultNumOfAttempts = 7

    def __init__(self):
        if HangingShape.instance is None :
            HangingShape.instance = self #?does it also apply to the children? if a child is created, so is HangingShape instance the child?


    def SetSelfAsNewView(self):
        HangingShape.instance = self
        return self

    def RenderNext(self, isCorrect : bool):
        if(not isCorrect):
            self.instance.numOfAttempts -= 1
            print("number of Attempts left is " + str(self.numOfAttempts))

    def ResetView(self, numOfAttempts = DefaultNumOfAttempts):
        self.instance.numOfAttempts = HangingShape.DefaultNumOfAttempts

    def ResetNumOfAttempts(self, num):
        self.instance.numOfAttempts = num
        return self

    def setDefaultNumOfAttempts(self, iter):
        print("Please choose your desired number of attempts")
        for i in range(iter):
            num = input()
            if num.isnumeric():
                HangingShape.DefaultNumOfAttempts = int(num)
                self.instance.numOfAttempts = HangingShape.DefaultNumOfAttempts
                return True
            elif iter != i:
                print("You didn't type a number. Please choose one.")
            else:
                print("Setting a default num of attempts")
                self.instance.numOfAttempts = HangingShape.DefaultNumOfAttempts

        return False
