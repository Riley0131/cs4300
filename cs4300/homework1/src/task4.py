def calculate_discount(price, disc):
    if (price > 0 and disc > 0): #ensure that prices and discount are valid positive numbers
        return round(price * (1 - (disc / 100)), 2)