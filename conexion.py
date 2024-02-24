import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Joe2022098',
                             port= 3306,
                             database='base_de_datos_prueba')

cursor=connection.cursor()
crear_tabla_vuelos = """
CREATE TABLE IF NOT EXISTS vuelos(
    numero_vuelo INT PRIMARY KEY,
    origen VARCHAR(20),
    destino VARCHAR(20),
    fecha_salida DATETIME,
    fecha_llegada DATETIME,
    duracion_total_min INT,
    tiene_escala BOOLEAN,
    duracion_escala_min INT,
    compañia_operadora VARCHAR(255),
    num_pasajeros INT,
    num_plazas_libres INT  
);
"""

cursor.execute(crear_tabla_vuelos)
connection.commit()

