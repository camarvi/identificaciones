from db_conn import ConexionDB

class area:
    def __init__(self):
        self.cod = ""
        self.area = ""
        self.db = ConexionDB()

    def listado_areas(self):
        query = "SELECT COD,AREA FROM AREA_IDENTIDAD ORDER BY AREA"
        return self.db.ejecutar(query)