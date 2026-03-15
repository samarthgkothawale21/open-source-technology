import random

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    


    def book(self, fro, to):
        print(f"Your ticket is booked in trainNo: {self.trainNo} from {fro} to {to}")

    def getInfo(self):
        print(f" your train no : {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Your ticket fare in train {self.trainNo}  from {fro} to {to} is: {random.randint(300, 1000)}")

t = Train(12250)
t.book("Pune","Delhi")
t. getInfo ()
t.getfare("Pune","Delhi")