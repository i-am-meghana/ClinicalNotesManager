from app import app,db
from flask import request, jsonify
from models import Note


@app.route("/api/notes", methods = ["GET"])
def get_notes():
    notes = Note.query.all()
    
    result = [note.to_json() for note in notes]
    return jsonify(result), 200


@app.route('/api/notes' , methods=['POST'])
def create_note():
    try:
        # Get the content from the incoming JSON request
        # Get the content of the note from the request body
        data = request.json
        content = data.get('content')
        
        if not content:
            return jsonify({"error": "Note content is required"}), 400

        new_note = Note(content = content) #,patient_id=patient)
        db.session.add(new_note)
        db.session.commit()

        return jsonify({"message": "Note added successfully", "note": new_note.to_json()}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
