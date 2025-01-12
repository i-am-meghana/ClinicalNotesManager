from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Notes Model
class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    
    def __repr__(self):
        return f'<Note {self.id}>'
 
    def to_json(self):
        return {
            "id" : self.id,
            "content" : self.note_text    
        }
