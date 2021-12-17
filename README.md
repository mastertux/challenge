# Qulture Rocks Challenge

> Challenge executed in Fastapi

## Project setup
```sh
pip install poetry
poetry install
```

### Database Setup
```
Open file alembic.ini and add this line
sqlalchemy.url =  postgresql://tulio:tulio@localhost/qulture

Run this command 
alembic upgrade head
```

### Run Project
```
uvicorn challenge.main:app --host 0.0.0.0 --port 8000
```

## Endpoints

### Tags
- `GET /tags`: Get list of tags
- `GET /tags/:id`: Get a single tag
- `POST /tags`: Create tag
- `PUT /tags`: Update list of tag
- `DELETE /tags`: Delete a tag

### Segments
- `GET /segments`: Get list of segments
- `GET /segments/:id`: Get a single segment
- `POST /segments`: Create a segment
- `DELETE /segments`: Delete a segment

### Users
- `GET /users`: Get list of users
- `GET /users/:id`: Get a single user
- `POST /users`: Create a user 
- `PUT /users`: Update a user
- `DELETE /users`: Delete a user

## Test

```sh
pytest
```

### Attention
``` 
At the endpoint of / users has an option to pass a filter on the search. This filter must be sent in the same format as ansi sql. 
Ex: (first_name = 'test' and last_name = 'test 2') or (email = 'teste@teste.com')
```

### Deployed
```
The project is running in aws in this address http://18.191.237.232/docs
```