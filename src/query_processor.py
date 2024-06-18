#Implementing a query engine using BigQuery from Google Cloud
import psycopg2

# Function to connect to the PostgreSQL database
class Connection:
    def connect_db():
        return psycopg2.connect(
            dbname="demo", 
            user="postgres", 
            password="", 
            host="localhost", 
            port="5432"
        )
class Query:
# Function to execute a query
    def execute_query(query):
        with Connection.connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                if query.strip().upper().startswith("SELECT"):
                    results = cur.fetchall()
                    return results
                conn.commit()  # Commit for INSERT, UPDATE, DELETE
                return "Query executed successfully."

    # Main function to handle query engine logic
    
    def query_engine():
        while True:
            query = input("Enter your SQL query or 'exit' to quit: ")
            if query.lower() == 'exit':
                print("Exiting query engine, have a nice day :).")
                break
            try:
                results = Query.execute_query(query)
                if isinstance(results, list):
                    for row in results:
                        print(row)
                else:
                    print(results)
            except Exception as e:
                print("An error occurred:", e)

