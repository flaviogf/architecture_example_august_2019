# Architecture Example August 2019.

Architecture Example August 2019.

## Tools
- Alembic
- Flask
- Flask-SQLAlchemy
- Marshmallow
- SQLAlchemy
- SwaggerUI

## How to use

- Create virtualenv and activate it
```sh
python3.7 -m venv venv && source venv/bin/activate
```

- Install pipenv
```sh
pip install pipenv
```

- Install dependencies
```sh
pipenv install -d
```

- Run tests
```sh
coverage run -m pytest && coverage report
```

- Configure .env file

- Run migrations
```sh
alembic upgrade head
```

- Run application
```sh
gunicorn -b 0.0.0.0:5000 manage:app
```

- Access http://localhost:5000
