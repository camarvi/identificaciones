import pyodbc

class ConexionDB:
    def __init__(self,server='xxxxx',database='xxxxx',usuario='xxxx',password='xxxxx'):
        self.server = server
        self.database = database
        self.usuario = usuario
        self.password = password

    def conectar(self):
        self.db = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.usuario+';PWD='+self.password)

    def abrir_cursor(self):
        self.cursor = self.db.cursor()

    def ejecutar_consulta(self, query, parametros=''):
        if parametros !='':
            self.cursor.execute(query, parametros)
        else:
            self.cursor.execute(query)

    def traer_datos(self):
        try:
            self.rows = self.cursor.fetchall()
        except:
            self.rows = ""

    def enviar_commit(self, query):
        sql = query.lower()
        es_select = sql.count('select')
        if es_select < 1 :
            self.db.commit()

    def cerrar_cursor(self):
        self.cursor.close()

    def ejecutar(self, query, values=''):
        if (self.server and self.usuario and self.password and self.database and query):
            self.conectar()
            self.abrir_cursor()
            self.ejecutar_consulta(query, values)
            self.enviar_commit(query)
            self.traer_datos()
            self.cerrar_cursor()
            return self.rows


