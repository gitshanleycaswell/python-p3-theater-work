from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///auditions.db')
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

session.query(Audition).delete()
session.query(Role).delete()

r1=Role(character_name="Ione")
session.add(r1)
session.commit()

a1 = Audition(actor="Spencer", location="Hollywood", phone=2342342343, hired=False, role_id=r1.id)
a2 = Audition(actor="Lindsay Lohen", location="New York", phone=234234234, hired=False, role_id=r1.id)
a3 = Audition(actor="Jessica Love Hewitt", location="Santa Monica", phone=2342342343, hired=False, role_id=r1.id)
session.add_all([a1, a2, a3])
session.commit()






