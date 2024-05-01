from flask import Flask
from app.routes.views import main
from sqlalchemy_utils import database_exists, create_database
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exc, text
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('app.config.config.Config')

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
    conn = engine.connect()

    # Check and create the database if it doesn't exist
    try:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {app.config['MYSQL_DB']}"))
        print(f"Checked/created the database '{app.config['MYSQL_DB']}' successfully.")
    except exc.SQLAlchemyError as e:
        print(f"Failed to check/create database: {e}")
    
    conn.close()

    # Update URI to include the database now
    app.config['SQLALCHEMY_DATABASE_URI'] += app.config['MYSQL_DB']
    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.views import main  # Assuming you have this structure
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    
    return app