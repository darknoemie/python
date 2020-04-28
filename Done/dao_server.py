import psycopg2


class BaseDAO:

    # Creation de la propriete CNX
    def _getCnx(self):
        return self._cnx

    def _setCnx(self, value):
        self._cnx = value

    cnx = property(_getCnx, _setCnx)

    # Creation de la propriete fields
    def _getFields(self):
        return self._fields

    def _setFields(self, value):
        self._fields = value

    fields = property(_getFields, _setFields)

    # Creation de la propriete tableName
    def _getTableName(self):
        return self._tableName

    def _setTableName(self, value):
        self._tableName = value

    tablename = property(_getTableName, _setTableName)

    # Creation de la propriete id
    def _getId(self):
        return self._id

    def _setId(self, value):
        self._id = value

    id = property(_getId, _setId)

    def __init__(self):
        # print('Constructeur de BaseDAO')
        self._cnx = psycopg2.connect(host="localhost", database="formation", user="postgres", password="aleria")
        self._fields = []
        self._tableName = ''
        self._id = ''

    def buildFieldsList(self):
        str = ''
        sep = ''
        for f in self._fields:
            str += sep
            str += f
            sep = ','
        return str

    def getById(self, id):
        str = self.buildFieldsList()
        sql = "select " + str + " from " + self._tableName + " where " + self._id + "=" + repr(id)
        cursor = self._cnx.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        result = {}
        cpt = 0
        for f in self._fields:
            result[f] = row[cpt]
            cpt += 1
        return result

    def getAll(self):
        str = self.buildFieldsList()
        sql = "select " + str + " from " + self._tableName
        cursor = self._cnx.cursor()
        cursor.execute(sql)
        # Retourne une liste de tuples
        rows = cursor.fetchall()
        # print(rows)
        liste = []
        cptligne = 0
        for row in rows:
            # print(row)
            result = {}
            cpt = 0
            for f in self._fields:
                result[f] = row[cpt]
                cpt += 1
            liste.append(result)
        return liste

    # entity doit être un dictionnaire
    def save(self, entity):
        sql = "insert into " + self._tableName
        # +"listedeschamps" + "values(%s)"
        values = '('
        listValues = []
        colnames = '('
        sep = ''
        for k, v in entity.items():
            colnames += sep + k
            listValues.append(entity[k])
            values += sep + '%s'
            sep = ','
        colnames += ')'
        values += ')'
        sql += colnames + " values " + values + " RETURNING id;"
        cursor = self._cnx.cursor()
        cursor.execute(sql, listValues)
        # Recupere l'identifiant genere
        id = cursor.fetchone()[0]
        # valide les changements dans la base de donnees
        self._cnx.commit()
        # ferme la communication avec la base de donnees.
        cursor.close()
        return id

    def delete(self, entity):
        sql = f"delete from {self._tableName} where {self.id}={entity[self.id]};"

        cursor = self._cnx.cursor()
        cursor.execute(sql)
        # valide les changements dans la base de donnees
        self._cnx.commit()
        # ferme la communication avec la base de donnees.
        cursor.close()
        return id

    def update(self, entity):
        sql = f"delete from {self._tableName} where {self.id}={entity[self.id]};"

        sql = f"update {self._tableName} set adresse2 ={{entity[self.id]}} where {self.id}={entity[self.id]};"


class ClientDAO(BaseDAO):

    def __init__(self):
        super().__init__()
        # print('Constructeur de ClientDAO')
        # Liste des noms de champs
        self.fields = ['id', 'mnemo', 'raison', 'adresse1', 'adresse2', 'codeinsee']
        self.tablename = 'client'
        self.id = 'id'

    def getById(self, id):
        #       cursor = self.cnx.cursor()
        #       cursor.execute("SELECT id,raison FROM client where id="+repr(id))
        #       print("The number of parts: ", cursor.rowcount)
        #       row = cursor.fetchone()
        #       return row
        return super().getById(id)

    def getAll(self):
        return super().getAll()

    def save(self, entity):
        return super().save(entity)


dao = ClientDAO()

obj = dao.getById(1)

print("getById retourne")
for k, v in obj.items():
    print('  [' + k + ']=' + repr(obj[k]))

print("getAll retourne")
obj = dao.getAll()

print(obj)

# On creer un dictionnaire vide
# ['id','mnemo','raison','adresse1','adresse2','codeinsee']
entity = {}
entity['mnemo'] = 'SFP'
entity['raison'] = 'Societe Francaise Petroleum'
entity['adresse1'] = '8 rue du quai'
entity['adresse2'] = ''
entity['codeinsee'] = '72115'
lastid = dao.save(entity)

print("save retourne lastid=" + repr(lastid))
entity['id'] = '6'
dao.delete(entity)
