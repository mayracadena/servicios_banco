from conexion import Database

#funcion insertar usuario
def insertar_usuario(identificador, nombre, email, celular, tipo_persona):
    db = Database()
    try:
        db.connect()
        sql_usuario_existencia = "SELECT * FROM usuario WHERE identificador = %s"
        paramet1 = (str(identificador),)
        result1 = db.execute_query(sql_usuario_existencia, paramet1)

        if not result1:  # Si no existe el usuario

            sql_usuario = "INSERT INTO usuario (nombre, identificador, email, celular, tipo_persona) VALUES (%s, %s, %s, %s, %s)"
            paramet2 = (nombre, str(identificador), email, str(celular), tipo_persona)
            result2 = db.execute_query(sql_usuario, paramet2)

            return bool(result2)  
        else:
            return True  # El usuario ya existe

    except Exception as e:
        print(f"Error al insertar usuario: {e}")
        return False
    finally:
        db.disconnect()
        
#funcion insertar transaccion
def insertar_transaccion(serial_banco, fecha, identificador, concepto):
    db = Database()
    try:
        db.connect()
        sql_usuario_existencia = "SELECT id FROM usuario WHERE identificador = %s"
        paramet1 = (str(identificador),)
        result1 = db.execute_query(sql_usuario_existencia, paramet1)

        sql_concepto_existencia = "SELECT id FROM producto WHERE concepto = %s"
        paramet2 = (str(concepto),)
        result2 = db.execute_query(sql_concepto_existencia, paramet2)

        fk_usuario = result1[0][0] if result1 else None  
        fk_producto = result2[0][0] if result2 else None

        if fk_usuario is not None and fk_producto is not None:
            
            sql_producto = "INSERT INTO transaccion (serial_banco, fecha, fk_producto, fk_usuario) VALUES (%s, %s, %s, %s)"
            paramet3 = (str(serial_banco), fecha, fk_producto, fk_usuario)
            result3 = db.execute_query(sql_producto, paramet3)
            if result3:
                return True
            else:
                return False
        else:
            print("No se encontraron ambos IDs.")
            return False
    
    except Exception as e:
        print(f"Error al insertar transaccion: {e}")
        return False
    finally:
        db.disconnect()

def consulta_transaccion(serial_banco):
    db = Database()
    try:
        db.connect()
        sql_transaccion_existencia = "SELECT * FROM transaccion WHERE serial_banco = %s"
        parametro = (str(serial_banco),)
        resultado = db.execute_query(sql_transaccion_existencia, parametro)

        if resultado:
            return True
        else:
            return False

    except Exception as e:
        print(f"Error al buscar la transaccion: {e}")
        return False
    finally:
        db.disconnect()