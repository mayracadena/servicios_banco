import openpyxl
from datetime import datetime
from conexion import Database

def extraer_informacion(directorio, hoja):
    #se carga el excel y especificando el nombre de la hoja
    wb = openpyxl.load_workbook(directorio)
    sheet = wb[hoja]

    # recorrer el excel
    for row in sheet.iter_rows(values_only=True):
        for cell in row:
            # se mira si la celda esta vacia
            if cell is None:
                yield None
            # se formatea las fechas para poder insertarlas a la base de datos
            elif isinstance(cell, datetime):
                yield cell.strftime("%d-%m-%Y")
            else:
                yield cell