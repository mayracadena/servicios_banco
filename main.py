import os
import pandas as pd

from registros_excel import ManejoExcel
from consultas import insertar_transaccion, insertar_usuario

#CONFIGURACIONES GENERALES
#directorios (son rutas relativas a la ruta de mi proyecto)
directorio = 'ejemplo_excel'
directorio_general = os.path.join(os.getcwd(), directorio)

archivo_prueba = 'ejemplo_datos_banco.xlsx'

# Especificar el orden de las columnas
orden_columnas = ['concepto','valor','serial banco', 'fecha', 'nombre','identificador','email','celular', 'tipo persona']


archivo = ManejoExcel(directorio_general).listar_archivos_xlsx()
#print(archivo)

# Almacenar datos de usuarios y transacciones
usuarios = []
transacciones = []

for i in archivo:
    
    directorio_especifico= os.path.join(os.getcwd(), directorio, i)
    if os.path.exists(directorio_especifico):
        reader = ManejoExcel(directorio_especifico)
        leerExcel = reader.leer_excel()
        nombreColumnas = reader.get_nombres_columnas()
        datosOrganizados = reader.datos_organizados(orden_columnas)
        #print(datosOrganizados)
        #captura de los datos para su inserción a la base de datos
        for fila in datosOrganizados:
            # Reemplazar NaN con None
            for key in fila.keys():
                if pd.isna(fila[key]):  # Verifica si el valor es NaN
                    fila[key] = None  # Cambia NaN por None
           
            concepto = fila['concepto']
            valor = fila['valor']
            serial_banco = fila['serial banco']
            fecha = fila['fecha']
            nombre = fila['nombre']
            identificador = fila['identificador']
            email = fila['email']if fila['email'] is not None else None
            celular = fila['celular'] if fila['celular'] is not None else None 
            t_perso = fila['tipo persona']

            if t_perso == 'natural':
                tipo_persona = True
            else:
                tipo_persona = False

            # Almacenar usuario
            usuario = {
                'identificador': identificador,
                'nombre': nombre,
                'email': email,
                'celular': celular,
                'tipo_persona': tipo_persona
            }
            usuarios.append(usuario)

            # Almacenar transacción
            transaccion = {
                'serial_banco': fila['serial banco'],
                'fecha': fila['fecha'],
                'identificador': fila['identificador'],
                'concepto': fila['concepto']
            }
            transacciones.append(transaccion)

            
            
            

#ingresar usuarios
print("se comienza a insertar usuario")
for usuario in usuarios:
    
    inser1 = insertar_usuario(usuario['identificador'], usuario['nombre'], usuario['email'], usuario['celular'], usuario['tipo_persona'])
print("se comienza a insertar transaccion")
#ingresar transacciones
for transaccion in transacciones:
    insertar_transaccion(transaccion['serial_banco'], transaccion['fecha'], transaccion['identificador'], transaccion['concepto'])