from itertools import product

from product import Product
from productsSorter import ProductsSorter
from discountCalculator import DiscountCalculator

"""Twoja firma dostała zlecenie na stworzenie oprogramowania dla dużego sklepu internetowego 
„PythonMarkt”. Jedną z podstawowych funkcjonalności będzie oprogramowanie koszyka zakupów, 
który potrafiłby uwzględniać różne promocje, rabaty oraz oferty specjalne, takie jak:

Jeśli wartość zamówienia jest większa niż np. 300 zł klient otrzymuje 5% zniżki na zakupione towary
"3 w cenie 2" - Jeśli klient kupi conajmniej 3 produkty to 3 najtańszy otrzymuje gratis
Jeśli wartość zamówienia przekracza wartość 200 zł klient otrzymuje firmowy kubek gratis
Twoim zadaniem jest zaimplementowanie logiki, operującej na obiektach typu ‘Product’, 
która umożliwiałaby:

Sortowanie kolekcji produktów po cenie
Wyszukiwanie najtańszego/najdroższego produktu w zadanej kolekcji produktów
Wyszukiwanie n najtańszych produktów w zadanej kolekcji produktów
Wyświetlanie w konsoli informacje o wszystkich produktach w zadanej kolekcji produktów
Aplikowanie opisanych powyżej rodzajów promocji na zadanej kolekcji produktów"""


def check_sorted_products(sorted_products):
    return (sorted_products[0].price == 100 and
            sorted_products[1].price == 200 and
            sorted_products[2].price == 300 and
            sorted_products[3].price == 500)

def main():
    # Przygotowanie obiektów
    products = [
        Product(300),
        Product(200),
        Product(100),
        Product(500)
    ]
    # Sortowanie produktów
    sorted_products = ProductsSorter.sort(products)
    if not check_sorted_products(sorted_products):
        print("Produkty nie są poprawnie posortowane")
        return

    # # Znalezienie najdroższego produktu
    # if ProductsSorter.most_expensive(products) != products[3]:
    #     print("Najdroższy produktem powinien być 'p4'")
    #     return

    # # Znalezienie najtańszego produktu
    # if ProductsSorter.the_cheapest(products) != products[2]:
    #     print("Najtańszym produktem powinien być 'p3'")
    #     return

    # # Znalezienie dwóch najtańszych produktów
    # cheapest_two = ProductsSorter.the_cheapest_n(products, 2)
    # if products[1] not in cheapest_two or products[2] not in cheapest_two:
    #     print("2 najtańsze produkty to 'p3' i 'p2'")
    #     return

    # # Inicjalizacja kalkulatora zniżek
    # calculator = DiscountCalculator(products)

    # # Dodanie darmowego kubka, jeśli suma cen przekracza 1000
    # calculator.add_free_company_glass(1000)
    # if len(products) != 5:
    #     print("Cena produktów jest wyższa niż 1000 - kubek powinien zostać dodany")
    #     return

    # # Obniżka o 10%, jeśli suma cen przekracza 1000
    # calculator.discount_by_percentage(1000, 0.1)
    # if not (products[0].price == 270 and products[1].price == 180 and
    #         products[2].price == 90 and products[3].price == 450):
    #     print("Ceny produktów powinny być obniżona o 10%")
    #     return

    # # Zasada "trzy za cenę dwóch"
    # calculator.three_for_price_of_two()
    # if products[2].price > 0:
    #     print("Produkt 'p3' powinien być za darmo.")
    #     return

    print("Wygląda na to, że jest ok. Koniec.")


if __name__ == "__main__":
    main()