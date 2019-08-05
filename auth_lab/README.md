## Create User model
- class User(db.Model) etc.
- handle passwords
    - hash, hash, HASH already!


## User Routes
- create a user (unprotected)
    - http POST :5000/api/v1/users username="momo" email="momo@momo.com" password="password"
- get all users 
     - http GET http://localhost:5000/api/v1/users Authorization:"Bearer REAL_TOKEN_POR_FAVOR"

- get one user
    - http GET http://localhost:5000/api/v1/users/2 Authorization:"Bearer REAL_TOKEN_POR_FAVOR"

- update a user
    - http PUT http://localhost:5000/api/v1/users/2 about_me="karaoke lover" Authorization:"Bearer REAL_TOKEN_POR_FAVOR"


## Token Routes
- generate a token
    - http --auth momo:password POST http://localhost:5000/api/v1/tokens

- revoke a token
    - http DELETE http://localhost:5000/api/v1/tokens Authorization:"Bearer REAL_TOKEN_POR_FAVOR"
