from productcatalog.product import Product


class Cart:
    def __init__(self):
        self.__products = {}

    def add_product(self, product: Product, quantity: int) -> None:
        if product.get_uuid() in self.__products:
            self.__products[product.get_uuid()]['quantity'] += quantity
        else:
            self.__products[product.get_uuid()] = {
                'product': product,
                'quantity': quantity
            }

    def remove_product(self, product: Product, quantity: int) -> None:
        if product.get_uuid() in self.__products:
            if self.__products[product.get_uuid()]['quantity'] > quantity:
                self.__products[product.get_uuid()]['quantity'] -= quantity
            else:
                del self.__products[product.get_uuid()]

    def is_empty(self) -> bool:
        return len(self.__products) == 0

    def get_items_count(self) -> int:
        return len(self.__products)

    def is_in_cart(self, product: Product) -> bool:
        return product.get_uuid() in self.__products

    def get_total(self) -> int:
        total = 0
        for product_uuid in self.__products:
            product = self.__products[product_uuid]['product']
            total += product.get_price() * self.__products[product.get_uuid()]['quantity']
        return total

    def get_products(self) -> dict:
        return self.__products
