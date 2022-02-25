from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(
 __name__,
 template_folder="./templates",
 static_folder="./static",
)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/nastya_db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Session = sessionmaker(engine)
