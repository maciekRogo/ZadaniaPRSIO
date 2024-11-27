# products_sorter.py


class ProductsSorter:

    @staticmethod
    def sort(products):
        # Można wykorzystać algorytm sortowania przez wstawianie
        copy = []
        for i in range(0, len(products)):
            copy.append(products[i].price)
        products = sorted(copy)
        print(products)
        return products

    @staticmethod
    def most_expensive(products):
        return None

    @staticmethod
    def the_cheapest(products):
        return None

    @staticmethod
    def the_cheapest_n(products, n):
        return None