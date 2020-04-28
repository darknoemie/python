import psycopg2
#from macpath import sep

class BaseDAO:
    
     
     # Creation de la propriete CNX
    def _getCnx(self):
        return self._cnx

    def _setCnx(self,value):
        self._cnx = value

    cnx=property(_getCnx, _setCnx)
   
     # Creation de la propriete fields
    def _getFields(self):
        return self._fields

    def _setFields(self,value):
        self._fields = value

    fields=property(_getFields, _setFields)
   
    # Creation de la propriete tableName
    def _getTableName(self):
        return self._tableName

    def _setTableName(self,value):
        self._tableName = value

    tablename=property(_getTableName, _setTableName)
    
      # Creation de la propriete id
    def _getId(self):
        return self._id

    def _setId(self,value):
        self._id = value

    id=property(_getId, _setId)
    
    def __init__(self):
        # print('Constructeur de BaseDAO')
        self._cnx = psycopg2.connect(host="localhost",database="postgres", user="navpi", password="secret")
        self._fields =[]
        self._tableName=''
        self._id=''
        
        
    def buildFieldsList(self):
        str = ''
        sep = '' 
        for f in self._fields:
            str +=sep
            str +=f
            sep=','
        return str       
        
    def getById(self,id):
        str = self.buildFieldsList()
        sql = "select "+str +" from "+self._tableName+" where "+self._id+"="+repr(id)
        cursor = self._cnx.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        result={}
        cpt=0
        for f in self._fields:
            result[f]=row[cpt]
            cpt+=1
        return result
    
        
    def getAll(self):
        str = self.buildFieldsList()
        sql = "select "+str +" from "+self._tableName
        cursor = self._cnx.cursor()
        cursor.execute(sql)
        # Retourne une liste de tuples
        rows = cursor.fetchall()
        #print(rows)
        liste=[]
        cptligne=0
        for row in rows:
            # print(row)
            result={}
            cpt=0
            for f in self._fields:
               result[f]=row[cpt]
               cpt+=1
            liste.append(result)
        return liste
        
        
    # entity doit être un dictionnaire     
    def save(self,entity):
        sql = "insert into "+self._tableName
        # +"listedeschamps" + "values(%s)"
        values='('
        listValues=[]
        colnames='('
        sep=''
        for k,v in entity.items():
            colnames+=sep+k
            listValues.append(entity[k])
            values+=sep+'%s'
            sep=','
        colnames+=')'
        values+=')'
        sql+=colnames+" values "+values+" RETURNING " + self.id +";"
        cursor = self._cnx.cursor()
        cursor.execute(sql, listValues)
        # Recupere l'identifiant genere
        id = cursor.fetchone()[0]
        # valide les changements dans la base de donnees
        self._cnx.commit()
        # ferme la communication avec la base de donnees.
        cursor.close()
        return id
    
    def update(self, entity):
        listOfFields=[]
        listOfValues=[]
        strValues=[]
        for k,v in entity.items():
            if k != self._id:
                listOfFields.append(k+'=%s')
                listOfValues.append(str(v))
        sql="update {0} set {1} where {2}={3}".format(self.tablename 
                                                      ,','.join(listOfFields)
                                                      ,self.id
                                                      ,entity[self.id])
        cursor = self._cnx.cursor()
        cursor.execute(sql,listOfValues)
        self._cnx.commit()
        cursor.close()
    
    def delete(self, entity):
        # créer une requete delete
        sql="delete from {0} where {1}={2}".format(self.tablename,self.id,entity[self.id])
        
        cursor = self._cnx.cursor()
        cursor.execute(sql)
        self._cnx.commit()
        cursor.close()
        
        