from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Boolean, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

engine = create_engine('sqlite:///auditions.db')
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__ = "auditions"

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean(), default=False)
    role_id = Column(Integer(), ForeignKey('roles.id'))

    role = relationship('Role', back_populates = 'auditions')

    def __repr__(self):
        return f'<Audition. Actor: {self.actor}, location: {self.location}>'
    
    def call_back(self):
        self.hired = True
    
class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())

    auditions = relationship('Audition')

    @property
    def actors(self):
        for audition in self.auditions:
            return audition.actor
        
    @property
    def locations(self):
        for audition in self.auditions:
            return audition.location

    @property    
    def lead(self):
        for audition in self.auditions:
            if audition.hired == True:
                return audition
        print('no actor has been hired for this role')

    @property
    def understudy(self):
        hired_count = 0
        for audition in self.auditions:
            if audition.hired == True:
                hired_count += 1
                if hired_count == 2:
                    return audition
                
        print('no actor has been hired for understudy for this role')



    def __repr__(self):
        return f'<Role {self.character_name}>'