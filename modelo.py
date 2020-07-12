
from sqlalchemy import create_engine
from connector import *
# conexion
#engine = create_engine('sqlite:///libros.db', echo=True)
#engine = create_engine( 'mysql+pymysql://root:Admin1234@localhost/taller1' )
# sesion


# insertamos autores
autor_1 = Asistencia('lola garcia','jose garcia','programacion')
autor_2 = Asistencia('pedro zuares','jose garcia','etica')
autor_3 = Asistencia('pedro zuares','jose garcia','etica')
autor_4 = Asistencia('pedro zuares','jose garcia','etica')
lista_autores = (autor_1, autor_2,autor_3, autor_4)
session.add_all(lista_autores)
session.commit()
