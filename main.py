'''
TODO: LOS DATOS PARA CONECTARSE A LA BASE DE DATOS ES MEJOR TENERLOS GUARDADOS EN UN 
      ARCHIVO 'config.py'.
'''

import mysql.connector
from mysql.connector import errorcode # para 'error handling'.


class Serie:
    def __init__(self) -> None:
        pass


def mainMenu() -> int:
    option:int
    print(":::::::::::::: Series ::::::::::::::")
    print("1) Agregar serie nueva")
    print("2) Ver datos de serie existente")
    print("3) Modificar datos de serie existente")
    print("4) Eliminar serie")
    option = input('>> ')
    return option


def createDatabase(cursor, DB_NAME) -> int:
    '''Intenta crear una base de datos. Si lo logra devuelve 1, sino devuelve 0.'''
    try:
        cursor.execute(f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
    except mysql.connector.Error as err:
        print(f"{err}: FALLO AL CREAR LA BASE DE DATOS.")
        return 0
    return 1


def connect2database() -> None:
    '''Se conecta con la base de datos. Si no existe, intenta crearla. Devuelve None.'''
    db_name:str = 'seriesdb'
    # declaro los args para conectarme a la base de datos
    connection_args:dict = {'user':'root',
                            'password':'23bruno12481632',
                            'host':'localhost',
                            'database':db_name}
    
    # intenta crear una conexión con la base de datos
    try:
        cnx = mysql.connector.connect(**connection_args) # crea una conexión (cnx).
    except mysql.connector.Error as err: # errores comunes...
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(f'{err.errno}-{err}: HAY UN ERROR EN EL USUARIO O EN LA CONTRASEÑA.')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f'{err.errno}-{err}: LA BASE DE DATOS NO EXISTE.')
        else:
            print(err)
    else:
        cnx.close() # no cierra la conexión en realidad.
        return

    cursor = cnx.cursor() # crea un cursor a partir de la conexión (para hacer operaciones).

    # cambia a la base de datos 'seriesdb'
    try:
        cursor.execute(f"USE {db_name}")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            # si la base de datos no existe, intenta crearla...
            if (createDatabase(cursor, db_name) == 1):
                print(f"BASE DE DATOS {db_name} CREADA EXITOSAMENTE.")
            cnx.database = db_name
        else:
            print(err)
        return
    
    print(f'Conexión establecida correctamente con base de datos {db_name}')
    return




# MAIN ##############################################################################################################

def main():

    option:int = mainMenu()
    match option:
        case 1:
            pass
        case 2:
            pass
        case _:
            pass

if __name__=='__main__':
    main()