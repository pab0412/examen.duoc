# Nota: Los metodos actualizar y eliminar estan hechos con CodeGPT :deadinside:

import csv

def crear_persona(run:str, nombre:str, edad:int):
    with open("people_list.csv", "a", newline="", encoding="utf-8") as archivoCsv:
        read = csv.writer(archivoCsv)
        nuevo = [
            [run, nombre, edad]
        ]
        
        read.writerows(nuevo)

def leer_persona(run:str):
    with open("people_list.csv", mode="r", encoding="utf-8") as archivoCsv:
        read = csv.DictReader(archivoCsv)
        for r in read:
            if r["DNI"] == run:
                print("RUT: ", r["DNI"])
                print("Nombre: ", r["Nombre"])
                print("Edad: ", r["Edad"])
                
def eliminar_persona(run: str):
    with open("people_list.csv", "r", newline="", encoding="utf-8") as archivoCsv:
        leer = csv.DictReader(archivoCsv)
        lista = [persona for persona in leer]
        
        for l in lista:
            if l["DNI"] == run:
                lista.remove(l)
                break
    
        with open("people_list.csv", "w", newline="", encoding="utf-8") as archivoCsv: 
            writer = csv.DictWriter(archivoCsv, fieldnames=["DNI", "Nombre", "Edad"])
            writer.writeheader()
            writer.writerows(lista)
            
def actualizar_persona(run:str, nuevo_rut:str, nombre:str, edad:int):
    with open("people_list.csv", "r", newline="", encoding="utf-8") as archivoCsv:
        leer = csv.DictReader(archivoCsv)
        lista = [persona for persona in leer]
        
        for l in lista:
            if l["DNI"] == run:
                l["DNI"] = nuevo_rut
                l["Nombre"] = nombre
                l["Edad"] = edad
                break
    
    with open("people_list.csv", mode="w", newline="", encoding="utf8") as archivoCsv:
        escribir = csv.DictWriter(archivoCsv, fieldnames=["DNI","Nombre","Edad"])
        escribir.writeheader()
        escribir.writerows(lista)

rut = input("Ingrese el rut: ")
nuevo = input("Ingrese la nueva identidad: ")
nom = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
actualizar_persona(rut, nuevo, nom, edad)