# NTBBloodbath | PyBase v0.3.1
# Usage example file (for v0.3.1).

# Lets import PySQL Class from PyBase Package
from pysql import PySQL

# Lets define our database name (with default db_path).
# We can activate Debugging by setting debug to True.
db = PySQL(database = "prueba", debug = True)

# Lets create a table called users with two columns;
# username and languages and their values.
db.create(objects = {
    "table": {
        "name": "users",
        "columns": {
            "username": {
                "type": "text",
                "value": "bloodbath"
            }, 
            "languages": {
                "type": "text", 
                "value": ["Ruby", "Python", "JavaScript"]
            },
        }
    }
})

# Lets delete the value JavaScript from languages table in users table
db.delete(table = "users", objects = {
    "column": "languages",
    "element": "JavaScript"
})

# Lets delete the entire table
db.delete(table = "users")
