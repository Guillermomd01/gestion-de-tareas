from sqlalchemy import Column, Integer, String, Boolean, Date


import db

class Tarea (db.Base):
    __tablename__='tarea' #poner nombre a la tabla
    __table_args__={'sqlite_autoincrement':True} #nos a seguramos de que id sea unico
    #creamos las columnas de la tabla y sus atributos
    id= Column(Integer,primary_key=True) #Automaticamente esta PK se convierte en un autoincremental
    contenido = Column(String(200),nullable=False)
    hecha = Column(Boolean,default=False)
    fecha = Column(Date)


    def __init__(self,contenido,hecha,fecha):
        self.contenido= contenido
        self.hecha = hecha
        self.fecha= fecha

    def __str__(self):
        return 'Tarea({}: {} ({}))'.format(self.id,self.contenido, self.hecha)
