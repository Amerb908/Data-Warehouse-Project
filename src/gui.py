import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from query_processor import Query


class QueryApp:
    def __init__(self, master):
        self.master = master
        master.title("Query Search")

        # Create a frame for the input bar
        self.frame = ttk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        # Create the input bar
        self.input_bar = ttk.Entry(self.frame)
        self.input_bar.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)

        # Create the button to run the query engine
        self.run_button = ttk.Button(self.frame, text="Run", command=self.run_query)
        self.run_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create a frame for the output
        self.output_frame = ttk.Frame(master)
        self.output_frame.pack(padx=10, pady=10)

        # Create the text widget for the output
        self.output_text = tk.Text(self.output_frame)
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def run_query(self):
        query = self.input_bar.get()
        results = Query.execute_query(query)
        if isinstance(results, list):
            for row in results:
                self.output_text.insert(tk.END, str(row) + "\n")
        else:
            self.output_text.insert(tk.END, str(results) + "\n")

