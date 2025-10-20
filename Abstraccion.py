from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass


# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")

#otra instancia de cada clase
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass


class Avion(Vehiculo):
    pass


auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
auto1 = Auto("Toyota", "Camry", 2025, "Blanco")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
moto1 = Moto("Kawasaki", "ninja", 2024, "verde")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
camion1 = Camion("Kenworth", "T480", 2020, "Blanco")
avion1= Avion("Boeing", "777", 2017, "Blanco")
avion1= Avion("Airbus", "A320", 2019, "Blanco")

# Visualización
print(auto1)
print(moto1)
print(camion1)
print(avion1)