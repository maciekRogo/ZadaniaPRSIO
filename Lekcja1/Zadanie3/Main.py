class Box:
    def __init__(self,width):
        self.width = width
        self.height = width*2

    def join_diagonal(self, other_box):
        return Box(self.width + other_box.width), self.height + other_box.height
    def join_horizontal(self, other_box):
        return Box(self.width + other_box.width),self.height if self.height > other_box.height else other_box.height
    def join_vertical(self, other_box):
        return Box(self.width if self.width > other_box.width else other_box.width), self.height + other_box.height



# Funkcja testująca poprawność działania metod
def test_box_operations():
#     # Tworzymy dwa pudełka o znanych szerokościach
     box1 = Box(5)
     box2 = Box(3)

     # Test połączenia diagonalnego
     diagonal_box, diagonal_height = box1.join_diagonal(box2)
     if diagonal_box.width == 8 and diagonal_height == 16:
         print("Test połączenia diagonalnego: SUKCES")
     else:
         print(f"Test połączenia diagonalnego: PORAŻKA (Oczekiwano: szerokość 8, wysokość 16, "
               f"Otrzymano: szerokość {diagonal_box.width}, wysokość {diagonal_height})")

     # Test połączenia poziomego
     horizontal_box, horizontal_height = box1.join_horizontal(box2)
     if horizontal_box.width == 8 and horizontal_height == 10:
         print("Test połączenia poziomego: SUKCES")
     else:
         print(f"Test połączenia poziomego: PORAŻKA (Oczekiwano: szerokość 8, wysokość 10, "
              f"Otrzymano: szerokość {horizontal_box.width}, wysokość {horizontal_height})")

     # Test połączenia pionowego
     vertical_box, vertical_height = box1.join_vertical(box2)
     if vertical_box.width == 5 and vertical_height == 16:
         print("Test połączenia pionowego: SUKCES")
     else:
         print(f"Test połączenia pionowego: PORAŻKA (Oczekiwano: szerokość 5, wysokość 16, "f"Otrzymano: szerokość {vertical_box.width}, wysokość {vertical_height})")

    #print("Wszystko działa, brawo")

test_box_operations()