import ipdb
from seeds import *
from sqlalchemy import create_engine
from models import *

if __name__ == '__main__':
    auditions = session.query(Audition).all()
    roles = session.query(Role).all()
    

    a1 = auditions[0]
    a2 = auditions[1]
    a3 = auditions[2]
    r1= roles[0]

    ipdb.set_trace()