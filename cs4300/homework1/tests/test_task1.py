import task1

def test_task1(capsys):
    task1.main()
    out, err = capsys.readouterr()
    assert out.strip() == "Hello, World!"