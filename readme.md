setup flask project - MVC
    how to setup flask project- need env, file srutcture
    setup mysql and integrate it with flask using sqlalchemy

Notes CRUD- Notes can be Created, edited, deleted, and viewed
    
    notes table- notes_id,content,created_by,updated_by,deleted_at

    notes POST api endpoint for creating notes- accepts content and userid and saves it in db and returns the created notes
        accept title,content,created_by fields in the request body
        save the note to the database
        return a success message with the note id
        validation logic for input fields (e.g., non-empty title and content).

    notes GET api endpoint for reading notes- fetches all notes associated with auth user
        return the notes details as a json response including their notes_id, title, content
        handle errors(eg: note not found, Unauthorized access or invalid user credentials)

    notes PUT api endpoint for updating
        accept title and content in request body
        validate input and update the note in the database
        return a success message
        Handle validation errors for empty or invalid title or content
        

    notes DELETE endpoint
        mark note as deleted in the database
        return a success message
        Ensure the deleted notes are not returned in the GET requests.


Notes Table Schema:

    notes_id: Primary key (auto-incremented integer).
    content: Text field (stores the content of the note).
    created_by: Foreign key (stores user ID who created the note).
    updated_by: Foreign key (stores user ID who last updated the note).
    deleted_at: Timestamp (marks when the note was deleted, null if not deleted).


user auth-Users can log in/sign up with different roles (e.g., admin, clinician, assistant).
    user table-id,username,password,role
    registration api enpoint- accepts data, validates input, stores data
    login api endpoint - validates credentialss and returns a token for authenticated users

assigning to specific users

role-based permissions- only specific roles can edit or delete a note.

file upload for PDF or images (store in a database or local directory)



markup in git-look up
Add proper logging for debugging and monitoring API requests.
Write integration tests to ensure the end-to-end flow works as expected
Document the API endpoints (e.g., using OpenAPI/Swagger).
    Include details about the required parameters, responses, error codes, and request formats.
Optimize the performance of queries (e.g., consider indexing created_by and updated_by fields for faster lookups).
 Implement pagination or limits for the GET endpoint when fetching large amounts of notes.


Stretch Features (For Future Iterations):

    Version history of notes.

    Selectable templates.

    Search and filter functionality.


role-based authentication, file handling, and CRUD operations
