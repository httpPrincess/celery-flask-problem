from app import db

class Request(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  
  def __repr__(self):
        return '<User %r>' % self.name
      
  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name
      }
  
  