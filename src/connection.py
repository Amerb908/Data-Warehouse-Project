#Implementing a query engine using BigQuery from Google Cloud
import psycopg2
from psycopg2 import sql
from query_processor import *

# Function to connect to the PostgreSQL database
class Connection:
    def connect_db():
        return psycopg2.connect(
            dbname="User_Information", 
            user="postgres", 
            password="", 
            host="localhost", 
            port="5432"
        )
