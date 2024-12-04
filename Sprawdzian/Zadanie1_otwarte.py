# Funkcja sprawdzająca płeć na podstawie numeru PESEL
def sprawdz_plec(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        raise ValueError("Numer PESEL musi składać się z 11 cyfr")

    przedostatnia_cyfra = int(pesel[9])
    if przedostatnia_cyfra % 2 == 0:
        return 'K'  # Kobieta
    else:
        return 'M'  # Mężczyzna


# Funkcja sprawdzająca poprawność sumy kontrolnej
def sprawdz_sume_kontrolna(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        raise ValueError("Numer PESEL musi składać się z 11 cyfr")

    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum(int(pesel[i]) * wagi[i] for i in range(10))

    kontrolna = (10 - (suma % 10)) % 10  # Obliczenie cyfry kontrolnej
    return kontrolna == int(pesel[10])  # Porównanie z jedenastą cyfrą


# Program główny
def main():
    try:
        pesel = input("Podaj numer PESEL: ")

        # Sprawdzanie płci
        plec = sprawdz_plec(pesel)
        if plec == 'K':
            print("Płeć: Kobieta")
        else:
            print("Płeć: Mężczyzna")

        # Sprawdzanie sumy kontrolnej
        if sprawdz_sume_kontrolna(pesel):
            print("Numer PESEL jest poprawny.")
        else:
            print("Numer PESEL jest niepoprawny - błąd sumy kontrolnej.")

    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    main()
