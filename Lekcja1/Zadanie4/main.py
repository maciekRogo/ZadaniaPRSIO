from pesel import Pesel
def main():
    try:
        pesel_input = input("Podaj numer PESEL (domyślnie 55030101193): ")
        if not pesel_input:
            pesel_input = "55030101193"

        # Tworzenie obiektu klasy Pesel
        pesel = Pesel(pesel_input)

        # Wywołanie metody pokazującej informacje o PESEL
        pesel.pokaz_informacje()

    except ValueError as e:
        print(f"Błąd: {e}")

if __name__ == "__main__":
    main()