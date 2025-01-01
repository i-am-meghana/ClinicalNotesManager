##setup flask project - MVC
    - [ ] how to setup flask project- need env, file srutcture
    - [ ] setup mysql and integrate it with flask using sqlalchemy

##Notes CRUD- Notes can be Created, edited, deleted, and viewed
    - [ ] notes table- notes_id,content,created_by,updated_by
    - [ ] notes POST api endpoint - accepts content and userid and saves it in db and returns the created notes
    - [ ] notes GET api endpoint - fetches all notes associated with auth user

##user auth-Users can log in/sign up with different roles (e.g., admin, clinician, assistant).
    - [ ] user table-id,username,password,role
    - [ ] registration api enpoint- accepts data, validates input, stores data
    - [ ] login api endpoint - validates credentialss and returns a token for authenticated users

##assigning to specific users

##role-based permissions- only specific roles can edit or delete a note.

##file upload for PDF or images (store in a database or local directory)







Stretch Features (For Future Iterations):

    Version history of notes.

    Selectable templates.

    Search and filter functionality.


role-based authentication, file handling, and CRUD operations
