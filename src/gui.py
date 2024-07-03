import tkinter as tk
from tkinter import ttk
from query_processor import Query


class QueryApp:
    """
    A class to create a GUI application for executing SQL queries.

    Methods
    -------
    run_query():
        Executes the query entered in the input bar and displays the results.
    """

    def __init__(self, master):
        """
        Initialize the QueryApp with the master window.

        Parameters:
        master (tk.Tk): The main window of the application.
        """
        self.master = master
        master.title("Query Search")

        # Create a frame for the input bar
        self.frame = ttk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        # Create the input bar
        self.input_bar = ttk.Entry(self.frame, width=50)
        self.input_bar.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)

        # Create the button to run the query engine
        self.run_button = ttk.Button(self.frame, text="Search", command=self.run_query)
        self.run_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create a frame for the output
        self.output_frame = ttk.Frame(master)
        self.output_frame.pack(padx=10, pady=10)

        # Create the text widget for the output
        self.output_text = tk.Text(self.output_frame)
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def run_query(self):
        """
        Execute the query entered in the input bar and display the results.
        """
        query = self.input_bar.get()
        results = Query.execute_query(query)
        self.output_text.delete("1.0", tk.END)
        if isinstance(results, list):
            for row in results:
                self.output_text.insert(tk.END, str(row) + "\n")
        else:
            self.output_text.insert(tk.END, str(results) + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = QueryApp(root)
    root.mainloop()
