from lib.shoe import Shoe

def test_shoe_initialization():
    shoe = Shoe("Nike", "Air Max", 42)
    assert shoe.brand == "Nike"
    assert shoe.model == "Air Max"
    assert shoe.size == 42

def test_shoe_attribute_modification():
    shoe = Shoe("Adidas", "Ultraboost", 40)
    shoe.brand = "Puma"
    shoe.model = "Speed"
    shoe.size = 41
    assert shoe.brand == "Puma"
    assert shoe.model == "Speed"
    assert shoe.size == 41
