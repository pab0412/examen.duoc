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
        columna = [row for row in leer]
        
        for row in columna:
            if row["DNI"] == run:
                columna.remove(row)
                break
    
        with open("people_list.csv", "w", newline="", encoding="utf-8") as archivoCsv: 
            writer = csv.DictWriter(archivoCsv, fieldnames=["DNI", "Nombre", "Edad"])
            writer.writeheader()
            writer.writerows(columna)
            
def actualizar_persona(run:str, nombre:str, edad:int):
    with open("people_list.csv", "r", newline="", encoding="utf-8") as archivoCsv:
        leer = csv.DictReader(archivoCsv)
        columna = [c for c in leer]
        
    for cl in columna:
        if cl["DNI"] == run:
            cl["Nombre"] = nombre
            cl["Edad"] = edad
            break
        
    # Actualizar información
    with open("people_list.csv", "w", newline="", encoding="utf-8") as archivoCsv:
        writer = csv.DictWriter(archivoCsv, fieldnames=["DNI", "Nombre", "Edad"])
        writer.writeheader()
        writer.writerows(columna)

