from main import add


def test_add():
    """testing out add function"""
    assert add(1, 2) == 3
    assert add(3, 3) == 6
    print("hello")


if __name__ == "__main__":
    test_add()
