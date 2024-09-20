import openpyxl
import os
import pandas as pd
from datetime import datetime


class ManejoExcel:
    def __init__(self, directorio):
        self.directorio = directorio
        self.data = None

    def leer_excel(self):
        self.data = pd.read_excel(self.directorio)

    def get_nombres_columnas(self):
        return list(self.data.columns)

    def get_datos(self, orden_columnas=None):
        if orden_columnas:
            return self.data[orden_columnas]
        else:
            return self.data

    def datos_organizados(self, orden_columnas):
        df_reorganizado = self.data.reindex(columns=orden_columnas)
    # Convierte el DataFrame reorganizado a una lista de diccionarios
        return df_reorganizado.to_dict(orient='records') 
        #return self.data.reindex(columns=orden_columnas)
    
    
    def listar_archivos_xlsx(self):
        
        archivos_xlsx = []
        
        # Recorre los archivos en el directorio
        for archivo in os.listdir(self.directorio):
            # Verifica si el archivo tiene la extensión .xlsx
            if archivo.endswith('.xlsx'):
                archivos_xlsx.append(archivo)
                
        return archivos_xlsx
    



