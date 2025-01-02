from app import app,db
from flask import request, jsonify
from models import Note


@app.route("/api/notes", methods = ["GET"])
def get_notes():
    notes = Note.query.all()
    
    result = [note.to_json() for note in notes]
    return jsonify(result), 200

@app.route('/patients/<int:patient_id>/notes', methods=['POST'])
#create a note in the database with this data
def create_note(patient_id):
    try:
        
        note_data = request.json.get('note_text')
        if not note_data:
            return jsonify({"error": "Note text is required"}), 400
        patient = Patient.query.get(patient_id)
        if not patient:
            return jsonify({"error": "Patient not found"}), 404
    
        new_note = Note(note_text=note_data, patient_id=patient_id)
        db.session.add(new_note)
        db.session.commit()
        return jsonify({"message": "Note added successfully"}), 201
        
        #whatever that is being used here to get data for the table. from where
        notes_id = data.get("notes_id")
        content = data.get("content")
       

        
        #we are putting the content into a new row right?
        new_note = Note(notes_id = notes_id, content = content, description = description, gender = gender, img_url = img_url)

        db.session.add(new_friend)
        db.session.commit()
        
        #shows up in bruno. 
        return jsonify({"msg": "Friend created succesfully"}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500


