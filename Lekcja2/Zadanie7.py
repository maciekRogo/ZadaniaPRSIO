"""Napisz dekorator validate_division , który będzie sprawdzał, czy dzielnik (drugi argument
funkcji) nie jest równy zero, zanim wykona operację dzielenia. Jeśli dzielnik wynosi zero,
funkcja powinna zwrócić komunikat: "Dzielenie przez zero jest niemożliwe" . Zastosuj
dekorator do funkcji divide(x, y) .


Funkcja divide(x, y) ma zwracać wynik dzielenia x / y .
Jeśli y == 0 , dekorator powinien zwrócić komunikat o błędzie zamiast wykonać
funkcję.
"""

def validate_division(func):
    def wrapper(x,y):
        if y==0:
            return "Dzielenie przez zero jest niemożliwe"
        else:
            return func(x,y)
    return wrapper
@validate_division
def divide(x,y):
    return x/y
print(divide(5,2))

