from main import add

print(add(2, 3))
print("Hello world")

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 3) == 0
