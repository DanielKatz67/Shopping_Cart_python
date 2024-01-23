import yaml

from item import Item
from shopping_cart import ShoppingCart

#Do not alter this code!
class Store:
    def __init__(self, path):
        with open(path) as inventory:
            items_raw = yaml.load(inventory, Loader=yaml.FullLoader)['items']
        self._items = self._convert_to_item_objects(items_raw)
        self._shopping_cart = ShoppingCart()

    @staticmethod
    def _convert_to_item_objects(items_raw):
        return [Item(item['name'],
                     int(item['price']),
                     item['hashtags'],
                     item['description'])
                for item in items_raw]

    def get_items(self) -> list:
        return self._items

    def search_by_name(self, item_name: str) -> list:
        """
        * Arguments: the current instance of Store and an instance of str.
        * Return value: a sorted list of all the items that match the search 
        term. The sort order is described below.

        * The items in the returned list must contain the given phrase and 
        not exactly match it. For example, when searching for "soap", 
        items such as "dish soap" and "body soap" should be returned.

        Search results:
        * For both search functions, the list returned must not include items which are
        already in the current shopping cart. The result list should be ordered as follows.

            * Let the list of all items in the current shopping cart be Items, and let the
            list of all hashtags of Items be Tags (note that Tags may have duplicates).
            * An item i1 would be before item i2 in the result list if i1 has more
            common hashtagswith Tags than i2.
                * If both i1 and i2 have the same number of common hashtags with Tags,
                than i1 would appear before i2 if i1.name appears before i2.name in
                the lexicographic order.
                
        Example:
        * Let Tags = [h1, h1, h2, h3] and let the following be in the result list:
            * i1 = {name="item c", hashtags=[h2, h3]}
            * i2 = {name="item b", hashtags=[h1]}
            * i3 = {name="item a", hashtags=[h2]}
        * The result list would be i2, i1, i3 in this order. i1 appears before i3, 
        because i1 has more common hashtags with Tags (i1 has two which are h2 and h3, 
        whereas i3, only has one h2). i2 appears before i1 because both have two common 
        hashtags with Tags (h1 is counted twice) and i2.name appears before i1.name in 
        the lexicographic order.

        * Items i1, i2, i3, and two more items to create such a hashtags list, are given
        in the provided items file.
        """
       match_items = [item for item in self.get_items() if item.getName().find(item_name) != -1]


    def search_by_hashtag(self, hashtag: str) -> list:
        """
        * Arguments: the current instance of Store and an instance of str.
        * Return value: a sorted list of all the items matching the search 
        criterion. The sort order is described in "search_by_name".
        * The items in the returned list must have the given hashtag in 
        their hashtag list. For example, when searching 
        for the hashtag "paper", items with hashtags such as "tissue paper" 
        must *** not *** be returned.
        """
        # TODO: Complete
        pass

    def add_item(self, item_name: str):
        """
        Adds an item with the given name to the customer’s shopping cart.
        * Arguments: the current instance of Store and an instance of str.
        * Exceptions: if no such item exists, raises ItemNotExistError. 
        If there are multiple items matching the given name, raises TooManyMatchesError. 
        If the given item is already in the shopping cart, raises ItemAlreadyExistsError.
        * To ease the search for the customers, not the whole item’s name must be given, 
        but rather a distinct substring. For example, when adding "soap" to the cart, 
        if an item such as "body soap" exists, and no other item with the substring "soap" 
        in its name, "body soap" should be added to the list.
        * You may assume that no two items exist such that one's name is a substring of the other.
        """
        # TODO: Complete
        pass

    def remove_item(self, item_name: str):
        """
        * Removes an item with the given name from the customer’s shopping cart.
        * Arguments: the current instance of Store and an instance of str.
        * Exceptions: if no such item exists, raises ItemNotExistError. 
        If there are multiple items matching the given name, raises TooManyMatchesError.
        * In a similar fashion to add_item, here too, not the whole item’s name 
        must be given for it to be removed.
        """
        # TODO: Complete
        pass

    def checkout(self) -> int:
        """
        * Returns the total price of all the items in the costumer’s shopping cart.
        """
        # TODO: Complete
        pass
