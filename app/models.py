from app import db

class Request(db.Model):
  __tablename__ = 'Request'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=False)
  status = db.Column(db.String(80), unique=False, default='created')
  
  def __repr__(self):
        return '<Request [%r] %r (%r)>' % (self.id, self.name, self.status)
      
  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'status': self.status
      }
  
  