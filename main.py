from item import Item
from shopping_cart import ShoppingCart
from store import Store
import errors

POSSIBLE_ACTIONS = [
    'search_by_name',
    'search_by_hashtag',
    'add_item',
    'remove_item',
    'checkout',
    'exit'
]

ITEMS_FILE = 'items.yml'


def read_input():
    line = input('What would you like to do?')
    args = line.split(' ')
    return args[0], ' '.join(args[1:])


def main():
    # store = Store(ITEMS_FILE)
    # action, params = read_input()
    # while action != 'exit':
    #     if action not in POSSIBLE_ACTIONS:
    #         print('No such action...')
    #     else:
    #         try:
    #             if action == 'checkout':
    #                 print(f'The total of the purchase is {store.checkout()}.')
    #                 print('Thank you for shopping with us!')
    #                 return
    #             elif action == 'exit':
    #                 print('Goodbye!')
    #                 return
    #             else:
    #                 result = getattr(store, action)(params)
    #                 if result is not None:
    #                     for item in result:
    #                         print(item)
    #         except errors.ItemNotExistError as e:
    #             print(e)
    #         except errors.TooManyMatchesError as e:
    #             print(e)
    #         except errors.ItemAlreadyExistsError as e:
    #             print(e)
    #     action, params = read_input()
    # print('Goodbye!')

    # #more tests:

    store = Store(ITEMS_FILE)



    # store = Store('itemsPersonalTest.yml')
    # print(store)
    #
    # # Add items to the shopping cart
    # try:
    #     store.add_item("i4")
    #     store.add_item("i5")
    #     print("Items added successfully\n")
    # except errors.ItemAlreadyExistsError as e:
    #     print(e)
    #
    # # Display the contents of the cart
    # print("Shopping Cart Contents:\n", store.getShoppingCart())
    #
    # # items_consists_i = store.search_by_name("i")
    # # print("After search by name 'i': ")
    # # for item in items_consists_i:
    # #     print(f"{item}\n--------------")
    #
    # items_with_H1 = store.search_by_hashtag("H1")
    # print("After search by hashtag 'H1': ")
    # for item in items_with_H1:
    #     print(f"{item}\n--------------")
    #
    # # # Remove an item
    # # try:
    # #     shopping_cart.remove_item("Shampoo")
    # #     print("Shampoo removed from the cart")
    # # except errors.ItemNotExistError as e:
    # #     print(e)
    # # # Display the contents of the cart after removal
    # # print("Shopping Cart Contents after removal:\n", shopping_cart)
    # #
    # # print(f"Total price: {store.checkout()}")


if __name__ == '__main__':
    main()
