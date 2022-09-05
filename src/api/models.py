from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()


class MafiaMember(db.Model):
    __tablename__ = "mafia_member"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    boss = db.Column(db.String(120), unique=False, nullable=False)
    seniority = db.Column(db.Integer, unique=False, nullable=False)
    is_free = db.Column(db.Boolean(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "boss":self.boss,
            "seniority":self.seniority,
            "Is free":self.is_free
            # do not serialize the password, its a security breach
        }
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    

class Subordinate(db.Model):
    __tablename__ = "subordinate"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    subordinate = db.Column(db.String(120), unique=True, nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "subordinate":self.subordinate  
        }
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    


