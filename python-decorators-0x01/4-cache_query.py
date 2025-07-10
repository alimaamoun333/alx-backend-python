import sqlite3
import functools

# Simple in-memory cache
query_cache = {}

# Reuse the connection decorator from earlier
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    """
    Decorator that caches results of database queries based on the query string.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Determine the query string
        query = kwargs.get('query')
        if not query and args:
            # assume first arg after conn is the query
            query = args[1] if len(args) > 1 else None

        if query in query_cache:
            print(f"[CACHE HIT] Returning cached result for: {query}")
            return query_cache[query]

        # Not cached: execute and cache
        result = func(*args, **kwargs)
        query_cache[query] = result
        print(f"[CACHE MISS] Caching result for: {query}")
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    # First call: cache miss
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(users)

    # Second call: cache hit
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(users_again)
