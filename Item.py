from collections.abc import Callable
class Item:
    IsConsumable: bool
    IsClothing: bool
    Function: Callable
    Quantity: int
    Weight: float

    def __init__(self, _consumable, _clothing, _function, _quantity, _weight):
        self.IsConsumable = _consumable
        self.IsClothing = _clothing
        self.Function = _function
        self.Quantity = _quantity
        self.Weight = _weight
