
import postgres.BaseDAO as BaseDAO

class Bme280DAO(BaseDAO.BaseDAO):
        
 
    def __init__(self):
        super().__init__()
        # print('Constructeur de ClientDAO')
        # Liste des noms de champs
        self.fields = ['timestampmesure','creele','temperature','humidity','pression']   
        self.tablename = 'bme280'
        self.id = 'timestampmesure'
        
    def getById(self,id):
#       cursor = self.cnx.cursor()
#       cursor.execute("SELECT id,raison FROM client where id="+repr(id))
#       print("The number of parts: ", cursor.rowcount)
#       row = cursor.fetchone()
#       return row
        return super().getById(id)
        
    def getAll(self):
        return super().getAll()
    
    def save(self,entity):
        return super().save(entity)