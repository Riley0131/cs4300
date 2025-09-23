def task2(x):
    #different cases for input type
    if type(x) == int:
        return x+1
    elif type(x) == float:
        return x+0.1
    elif type(x) == str:
        return (x + "test")

