from db_conn import ConexionDB

class profesional:
    def __init__(self, cod, identificador, apellido1, apellido2, nombre, categoria, centro, area, imagen):
        self.cod = cod
        self.identificador = identificador
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.nombre = nombre
        self.categoria = categoria
        self.centro = centro
        self.area = area
        self.imagen = imagen
        self.db = ConexionDB()
        self.cadena_busqueda = """ 
            SELECT COD,IDENTIFICADOR,APELLIDO1,APELLIDO2,NOMBRE,CATEGORIA,CENTRO,AREA,IMAGEN FROM PROFESIONAL 
        """

    def nuevo_profesional(self):
        query = """ INSERT INTO PROFESIONAL (IDENTIFICADOR,APELLIDO1,APELLIDO2,NOMBRE,CATEGORIA,CENTRO,AREA,IMAGEN) 
        VALUES (?,?,?,?,?,?,?,?)
        """
        valores = (self.identificador,self.apellido1,self.apellido2,self.nombre,\
            self.categoria,self.centro,self.area, self.imagen)
        self.db.ejecutar(query, valores)

    def seleccionar_profesional(self):
        query = self.cadena_busqueda + " WHERE COD=?"
        valores = (self.cod)
        return self.db.ejecutar(query, valores)
    
    def busca_apellidos(self,ape1, ape2):
        if len(ape2)>1:
            ape1 = '%' + ape1 + '%'
            ape2 = '%' + ape2 + '%'
            query = self.cadena_busqueda + " WHERE APELLIDO1 LIKE ? AND APELLIDO2 LIKE ? ORDER BY APELLIDO1,APELLIDO2"
            valores = (ape1,ape2)
        else :
            query = self.cadena_busqueda + " WHERE APELLIDO1 LIKE ? ORDER BY APELLIDO1,APELLIDO2"
            ape1 = '%' + ape1 + '%'
            valores = (ape1)
        return self.db.ejecutar(query, valores)

    def busca_dni(self,identificador):
        query = self.cadena_busqueda + " WHERE IDENTIFICADOR=?"
        valores = identificador
        return self.db.ejecutar(query, valores)

    def modifica_profesional(self):
        query = """UPDATE PROFESIONAL SET IDENTIFICADOR=?, APELLIDO1=?, 
            APELLIDO2=?, NOMBRE=?, CATEGORIA=?, CENTRO=?,AREA=?,IMAGEN=? WHERE COD=?
        
        """
        valores = (self.identificador, self.apellido1, self.apellido2, self.nombre,\
             self.categoria, self.centro, self.area, self.imagen, self.cod)
        self.db.ejecutar(query, valores)

    def elimina_profesional(self):
        query = "DELETE FROM PROFESIONAL WHERE COD=?"
        valores = (self.cod)
        self.db.ejecutar(query, valores)

