# implementing a query engine that can retrieve data concurrent to other queries running should be
# something you can at least design and implement a piece of.
import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
import threading


class DatabaseConnection:

    def __init__(self, host, database, user, password, port):
        
        self.connection = psycopg2.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
        self.connection.autocommit = True

    def execute_query(self, query):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query)
            if cursor.description:
                return cursor.fetchall()
            return "Query executed successfully."
    
    def close(self):
        self.connection.close()
        
def thread_function(db_params, query):
    db = DatabaseConnection(**db_params)
    result = db.execute_query(query)
    if isinstance(result, list):
        for row in result:
            print(row)
    else:
        print(result)
    db.close()
    
def main():
    
    db_params = {
        "host":"localhost",  # or other host if not local
        "database":"postgres",
        "user":"postgres",
        "password":"12345",
        "port": "5432"  # default PostgreSQL port
    }
    
    queries = [
        "SELECT * FROM public.people_id;",
        "SELECT * FROM public.people_id WHERE name = 'Amer Belal';"
    ]
    
    threads = []
    
    for query in queries:
        # Create a new thread for each query
        thread = threading.Thread(target=thread_function, args=(db_params, query))
        threads.append(thread)
        thread.start()  # Start the thread
    
    for thread in threads:
        thread.join()
        
if __name__ == "__main__":
    main()
