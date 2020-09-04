import os

from application import create_app

### python manage.py seed_db  to init database

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    app.run(debug=True)
