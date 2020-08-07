class food():
    def __init__(self,type1):
        self.type1 = type1
    def __str__(self):
        return "I'm a {}".format(self.type1)


def func(x):
    if(x>=0):
        return x**3
    return 0

myFood = food('banana')
print(myFood)

