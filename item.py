class Item:
    def __init__(self, item_name: str, item_price: int, item_hashtags: list, item_description: str):
        self.name = item_name
        self.price = item_price
        self.hashtags = item_hashtags
        self.description = item_description

    def __str__(self) -> str:
        return f'Name:\t\t\t\t{self.name}\n' \
               f'Price:\t\t\t\t{self.price}\n' \
               f'Hashtags:{self.hashtags}\n' \
               f'Description:\t\t\t{self.description}'
    
    def getPrice(self) -> int:
        """
        Returns the price of the item.
        """
        return self.price
    
    def getName(self) -> str:
        """
        Retrns the name of the item.
        """
        return self.name
    
    def getHashtags(self) -> list:
        """
        Retrns the hashtags of the item.
        """
        return self.hashtags