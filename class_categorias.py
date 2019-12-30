from db_conn import ConexionDB

class categoria:
    def __init__(self):
        self.__cod = ""
        self.__nombre = ""
        self.db = ConexionDB()
    
    def listado_categorias(self):
        query = "SELECT COD,NOMBRE FROM CATEGORIAS ORDER BY NOMBRE"
        return self.db.ejecutar(query)