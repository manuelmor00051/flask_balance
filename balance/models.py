from balance import FICHERO
import csv
from datetime import date, datetime

class ValidationError(Exception): #creo mi error de esta forma.
    pass

class Movimiento():
    def __init__(self, diccionario):
        try:
            self.fecha = date.fromisoformat(diccionario["fecha"])
        except ValueError:
            raise ValidationError("Formato de fecha incorrecto")
        ahora = datetime.now()
        if self.fecha.strftime("%Y%m%d") > ahora.strftime("%Y%m%d"):
            raise ValidationError("La fecha no puede tener valor de futuro")
        self.concepto = diccionario["concepto"]

        if self.concepto == "":
            raise ValidationError("Informe el concepto")

        try:
            self.es_ingreso = diccionario["ingreso_gasto"]
        except KeyError:
            raise ValidationError("Informe tipo de movimiento Ingreso/Gasto")
        
        try:
            self.cantidad = float(diccionario["cantidad"])
        except ValueError:
            raise ValidationError("La cantidad debe de ser un número")

        if self.cantidad <= 0:
            raise ValidationError("La cantidad debe de ser superior a 0")

class ListaMovimientos():
    def __init__(self):
        self.movimientos = []

    def leer(self):
        self.movimientos = []
        fichero = open(FICHERO, 'r')
        dreader = csv.DictReader(fichero)
        for linea in dreader:
            self.movimientos.append(linea)
        fichero.close()

    def escribir(self):
        if len(self.movimientos) == 0:
            return

        fichero = open(FICHERO, 'w')
        nombres_campo = list(self.movimientos[0].keys())
        dwriter = csv.DictWriter(fichero, fieldnames = nombres_campo) #escribimos un diccionario con las claves que hay en fieldnames, se escribe con un for y xxx.writerow() en fichero
        dwriter.writeheader()
        for movimiento in self.movimientos:
            dwriter.writerow(movimiento)
            print(dwriter)
        fichero.close()

    def anyadir(self, valor): #con esta funcion añadimos un movimiento en forma de diccionario
        movimiento = {}
        movimiento["fecha"] = valor["fecha"]
        movimiento["concepto"] = valor["concepto"]
        movimiento["ingreso_gasto"] = valor["ingreso_gasto"]
        movimiento["cantidad"] = valor["cantidad"]
        self.movimientos.append(movimiento)