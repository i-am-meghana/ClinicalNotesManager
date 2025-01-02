from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Patient Model
class Patient(db.Model):
    __tablename__ = 'patients'
    patients_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    # Define the relationship to the Note model
    notes = db.relationship('Note', backref='patient', lazy=True)
    
    def __repr__(self):
        return f'<Patient {self.name}>'

# Notes Model
class Note(db.Model):
    __tablename__ = 'notes'
    notes_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    
    def __repr__(self):
        return f'<Note {self.id}>'


    def to_json(self):
        return {
            "notes_id" : self.notes_id,
            "content" : self.content,
            "timestamp" : self.timestamp,
            "patient_id" : self.patient_id,

            
        }
