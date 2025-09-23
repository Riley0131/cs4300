import task4

assert task4.calculate_discount(100, 20) == 80 #case using whole numbers
assert task4.calculate_discount(105, 13.5) == 90.83  #case using a float for the discount
assert task4.calculate_discount(19.2, 2) == 18.82 #case using a float for the price
assert task4.calculate_discount(15.26, 10.5) == 13.66 #case using two floats