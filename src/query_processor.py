import psycopg2
from psycopg2 import sql

class Connection:
    """
    This class handles the connection to the PostgreSQL database using psycopg2.
    """

    @staticmethod
    def connect_db():
        """
        Connect to the PostgreSQL database.

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
        try:
            conn = Connection.connect_db()
            with conn:
                with conn.cursor() as cur:
                    cur.execute(query, params)
                    if query.strip().upper().startswith("SELECT"):
                        return cur.fetchall()
                    conn.commit()
                    return "Query executed successfully."
        except Exception as error:
            raise Exception(f"An error occurred: {error}")

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
                print("Exiting query engine. Have a nice day :).")
                break

            # Handle parameterized queries
            params = None
            if '%' in query:
                params_input = input("Enter the parameters for your query, separated by commas: ")
                params = tuple(param.strip() for param in params_input.split(','))

            try:
                results = Query.execute_query(query, params)
                if isinstance(results, list):
                    for row in results:
                        print(row)
                else:
                    print(results)
            except Exception as error:
                print(error)

