import task2

def test_task2(capsys):
    assert task2.task2(5) == 6
    assert task2.task2(5.2) == 5.3
    assert task2.task2("hello") == "hellotest" #shows that string data type can be sent in