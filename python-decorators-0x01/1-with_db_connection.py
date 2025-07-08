import sqlite3
import functools

# Decorator to log SQL queries
import sqlite3
import functools

# Task 0: Logging Database Queries decorator

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        if not query and len(args) > 0:
            query = args[0]
        print(f"Executing SQL Query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Task 1: Handle Database Connections with a Decorator

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            # Pass connection as first positional argument
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

if __name__ == "__main__":
    # Example usage
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)
    user = get_user_by_id(user_id=1)
    print(user) == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    for user in users:
        print(user)
