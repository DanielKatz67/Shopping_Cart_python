from item import Item
import errors


class ShoppingCart:
    def __init__(self):
        # Using a dictionary to store items with their names as keys
        self._items = {}

    def __str__(self):
        return '\n'.join(str(item)+"\n----------------------------------" for item in self._items.values())

    def add_item(self, item: Item):
        """
        * Adds the given item to the shopping cart.
        * Arguments: the current instance of ShoppingCart and an instance of Item.
        * Exceptions: if the item name already exists in the shopping cart, raises 
        ItemAlreadyExistsError.
        """
        if item.name in self._items:
            raise errors.ItemAlreadyExistsError(f"Item '{item.name}' already exists in the shopping cart.")
        self._items[item.name]=item

    def remove_item(self, item_name: str):
        """
        * Removes the item with the given name from the shopping cart
        * Aguments: the current instance of ShoppingCart and an instance of str.
        * Exceptions: if no item with the given name exists, raises ItemNotExistError.
        """
        if item_name not in self._items:
            raise errors.ItemNotExistError(f"Item '{item_name}' doesn't exist in the shopping cart.")
        del self._items[item_name]

    def get_subtotal(self) -> int:
        """
        * Returns the subtotal price of all the items currently in the shopping cart.
        """
        # self.items is a dictonary so the valus must be called
        prices = [item.getPrice() for item in self._items.values()]
        return sum(prices)

    def getCartItems(self) -> dict:
            """
            Retrns the items on the ShoppingCart.
            """
            return self._items