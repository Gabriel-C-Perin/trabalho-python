from app import create_app
from app.database import db
import os

app = create_app()


if not os.path.exists('saude.db'):
    with app.app_context():
        db.create_all()
        print('Banco criado.')

if __name__ == "__main__":
    app.run(debug=True)