from app import app,db
from flask import request, jsonify
from models import Note


@app.route("/api/notes", methods = ["GET"])
def get_notes():
    notes = Note.query.all()
    
    result = [note.to_json() for note in notes]
    return jsonify(result), 200

#@app.route('/patients/<int:patient_id>/notes', methods=['POST'])
def create_note(patient_id):
    try:
        # Get the content from the incoming JSON request
        # Get the content of the note from the request body
        note_content = request.json.get('content')
        
        if not note_content:
            return jsonify({"error": "Note content is required"}), 400
 # Step 2: Find the patient from the database
        # Find the patient by the given patient_id
        #patient = Patient.query.get(patient_id)
 # Step 3: If patient doesn't exist, return an erro       
        #if not patient:
            #return jsonify({"error": "Patient not found"}), 404

  # Step 4: Create the new note, associate with the patient       # Create a new note for the patient
        new_note = Note(content=note_content) #,patient_id=patient)

  # Step 5: Save the new note in the database       # Add the new note to the session and commit the changes to the database
        db.session.add(new_note)
        db.session.commit()

 # Step 6: Send a response back to the client        # Return success message
        return jsonify({"message": "Note added successfully", "note": new_note.to_json()}), 201

    except Exception as e:
        # Rollback the session in case of an error and return the error message
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
