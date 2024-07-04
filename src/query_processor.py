import psycopg2

class Connection:
    """
    This class focuses on the connections to the PostgreSQL database.
    It uses the psycopg2 library to connect to the PostgreSQL database.
    """

    @staticmethod
    def connect_db():
        """
        Connect to the PostgreSQL database using psycopg2.

        Returns:
            psycopg2.extensions.connection: A connection object to the PostgreSQL database.
        """
        return psycopg2.connect(
            dbname="demo", 
            user="postgres", 
            password="", 
            host="localhost", 
            port="5432"
        )


class Query:
    """
    A class to handle database queries.

    Methods
    -------
    execute_query(query, params=None):
        Executes a given SQL query with optional parameters.
        
    query_engine():
        Starts the query engine to accept user queries and handle them.
    """

    @staticmethod
    def execute_query(query, params=None):
        """
        Execute a given SQL query with optional parameters.

        Parameters:
        query (str): The SQL query to be executed.
        params (tuple, optional): Parameters to be used in the SQL query.

        Returns:
        list: Results of the query if it is a SELECT statement.
        str: A success message for non-SELECT queries.

        Raises:
        Exception: If an error occurs during the execution of the query.
        """
        with Connection.connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)  # Use the params argument here
                if query.strip().upper().startswith("SELECT"):
                    results = cur.fetchall()
                    return results
                conn.commit()  # Commit for INSERT, UPDATE, DELETE
                return "Query executed successfully."

    @staticmethod
    def query_engine():
        """
        Start the query engine to accept user SQL queries and handle them.

        The function runs in a loop, prompting the user for a SQL query or
        the command 'exit' to quit. It handles parameterized queries and
        prints the results of the queries.

        Example:
        >>> Query.query_engine()
        Enter your SQL query or 'exit' to quit: SELECT * FROM table;
        (1, 'Alice')
        (2, 'Bob')
        """
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
