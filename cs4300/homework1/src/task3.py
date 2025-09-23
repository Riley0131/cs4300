# Create a new file named task3.py. Create an if statement to check if a given number is positive,
# negative, or zero. Implement a for loop to print the first 10 prime numbers (you may need to
# research how to calculate prime numbers). Create a while loop to find the sum of all numbers from
# 1 to 100. Write pytest test cases to verify the correctness of your code for each control structure

#checks if a number is positive, negative or zero
def polarityCheck(value):
    if value == 0:
        return "zero"
    elif value < 0:
        return "negative"
    elif value > 0:
        return "positive"


def primeNum(n):
    num = 2
    count = 0
    while count < n:
        for i in range(2, int(num**.5)+1):
            if num % i == 0:
                break
        else:
            print(num)
            count+=1
        num+=1

def sums():
    i = 1
    sum = 0
    while i <= 100:
        sum += i
        i+=1

    return sum