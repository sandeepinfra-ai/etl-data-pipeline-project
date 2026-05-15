from sqlalchemy import create_engine
from dotenv import load_dotenv
import urllib.parse
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

def load_data(data):
    data.to_sql(
        name="employees",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data Loaded Successfully into PostgreSQL")