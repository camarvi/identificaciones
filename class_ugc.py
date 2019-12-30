from db_conn import ConexionDB

class ugc:
    def __init__(self):
        self.__cod_zbs = ""
        self.__zbs = ""
        self.db = ConexionDB()

    def listado_ugcs(self):
        query = "SELECT COD_ZBS,ZBS FROM ZONAS_BASICAS WHERE ACTIVO=1 ORDER BY ZBS"
        return self.db.ejecutar(query)

