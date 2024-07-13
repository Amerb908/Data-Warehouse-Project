# Query Engine

## Overview

### Project Components

This project consists of two main components:
- A query processor to handle PostgreSQL database queries.
- A graphical user interface (GUI) built with Tkinter to execute these queries interactively.

### Files:
- `query_processor.py`: Contains the logic for connecting to the PostgreSQL database and executing queries.
- `gui.py`: Creates a Tkinter-based GUI for entering and executing SQL queries.

## Purpose

This project aims to simplify the process of interacting with a PostgreSQL database by providing:
- A structured way to execute SQL queries.
- A user-friendly GUI for executing queries without needing to use the command line or database management tools.

## Prerequisites

### Requirements
- Python 3.10
- PostgreSQL database
- Required Python packages: `psycopg2`, `tkinter`

### Installation

1. **Install PostgreSQL:**
   - Follow the instructions on the [official PostgreSQL website](https://www.postgresql.org/download/) to install PostgreSQL.

2. **Install Required Python Packages:**
   ```bash
   pip install psycopg2-binary
