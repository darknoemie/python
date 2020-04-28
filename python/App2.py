#!/usr/bin/python3

import postgres.Bme280DAO as Bme280DAO

dao=Bme280DAO.Bme280DAO()

entity={}
entity['timestampmesure']='2020-04-23 12:35:02'
entity['temperature']='23.45'
entity['humidity']='65.78'
entity['pression']='101236.00'
lastid=dao.save(entity)
print("save retourne lastid="+repr(lastid))

