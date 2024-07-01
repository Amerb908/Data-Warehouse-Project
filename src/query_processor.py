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
    # Function to execute a query with parameters
    def execute_query(query, params=None):
        with Connection.connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)  # Use the params argument here
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
            # Check if parameters are needed
            if '?' in query:
                params = input("Enter the parameters for your query, separated by commas: ")
                params = params.split(',')  # Split the parameters by comma and pass as tuple
                params = tuple([param.strip() for param in params])  # Strip spaces
            else:
                params = None

            try:
                results = Query.execute_query(query, params)
                if isinstance(results, list):
                    for row in results:
                        print(row)
                else:
                    print(results)
            except Exception as error:
                print("An error occurred:", error)
                

