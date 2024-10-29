import pytest
from try_cal import square

def main():
    test_square()
    test_negative()
    test_str()
    
def test_square():
        assert square(2) == 4
        assert square(3) == 9
def test_negative():
    assert square(-2) == 4
    assert  square(-3) == 9
    
def test_str():
    with pytest.raises(TypeError):          #pytest.raises () function is used to assert that certain conditions occur and typeerror  is used to check if the input is not of the correct type


        square('a')


if  __name__ == "__main__":
    main()