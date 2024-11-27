class Pesel:
    def __init__(self, pesel):
        self.pesel = pesel

    def pokaz_informacje(self):
        pesel = self.pesel
        tabpes = list(map(int, self.pesel[:10]))
        tabwag = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        s = 0
        for i, data in enumerate(tabpes):
            a = tabpes[i] * tabwag[i]
            s += a
        #print(s)
        M = int(s % 10)
        R = int(pesel[10])
        P = int(pesel[9])
        if M == 0 and R == 0:
            print("PESEL jest poprawny")
        if (10 - M == R):
            print("PESEL jest poprawny")
        else:
            print("PESEL jest niepoprawny")
        if(P%2 == 0):
            print("Płeć: Kobieta")
        else:
            print("Płeć: Mężczyzna")


