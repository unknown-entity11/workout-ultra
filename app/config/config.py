class Config:
    SECRET_KEY = 'doofenschmirtz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Wow_bevice11'
    MYSQL_DB = 'workout_database'
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/"