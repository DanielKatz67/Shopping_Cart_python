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
    #         continue
    #     if action == 'checkout':
    #         print(f'The total of the purchase is {store.checkout()}.')
    #         print('Thank you for shopping with us!')
    #         return
    #     if action == 'exit':
    #         print('Goodbye!')
    #         return
    #     getattr(store, action)(params)
    
    #     action, params = read_input()

    # #personal testing:
    # shopping_cart = ShoppingCart()

    # # Create some test items
    # item1 = Item("Soap", 5, ["cleaning", "hygiene"], "A bar of soap for daily use")
    # item2 = Item("Shampoo", 10, ["haircare", "beauty"], "Shampoo for shiny hair")
    # item3 = Item("Toothpaste", 3, ["dental", "hygiene"], "Fluoride toothpaste for teeth")

    # # Add items to the shopping cart
    # try:
    #     shopping_cart.add_item(item1)
    #     shopping_cart.add_item(item2)
    #     shopping_cart.add_item(item3)
    #     print("Items added successfully")
    # except errors.ItemAlreadyExistsError as e:
    #     print(e)

    # # Display the contents of the cart
    # print("Shopping Cart Contents:\n", shopping_cart)

    # # # Remove an item
    # # try:
    # #     shopping_cart.remove_item("Shampoo")
    # #     print("Shampoo removed from the cart")
    # # except errors.ItemNotExistError as e:
    # #     print(e)

    # # # Display the contents of the cart after removal
    # # print("Shopping Cart Contents after removal:\n", shopping_cart)

    # subtotal = shopping_cart.get_subtotal()
    # print(subtotal)

    # word = "soupA"
    # print(f"The word: {word}")
    # print(word.find("sop"))

    filtered_word = "soup"
    list = ["soup", "banna", "soup A", "soupB"]
    filtered_list = [word for word in list if word.find(filtered_word) != -1]
    print(list)
    print(filtered_list)

  

if __name__ == '__main__':
    main()
