import task3

def test_task3(capsys):
    #testing a positive number
    assert task3.polarityCheck(1) == "positive"
    #testing negative number
    assert task3.polarityCheck(-1) == "negative"
    #testing zero
    assert task3.polarityCheck(0) == "zero"
    

    #test prime numbers
    task3.primeNum(10)
    capture = capsys.readouterr()
    assert capture.out =="2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"

    #test sum of 1-100
    assert task3.sums() == 5050