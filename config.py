import os

HOST = "localhost" if "HOST" not in os.environ else os.environ.get("HOST")
PORT = 5432 if "PORT" not in os.environ else os.environ.get("PORT")
DB = "analysis_profile" if "DB" not in os.environ else os.environ.get("DB")
PASSWORD = "12345" if "PASSWORD" not in os.environ else os.environ.get("PASSWORD")
USER = "postgres" if "USER" not in os.environ else os.environ.get("USER")
