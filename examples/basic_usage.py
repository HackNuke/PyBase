# NTBBloodbath | PyBase v0.1.0
# Usage example file (for v0.1.0).

# Lets import PyBase Class from PyBase Package
from pybase_db import PyBase

# Lets define our database name and format (with default db_path).
# db_type isn't case sensitive. You can use JSON and json and it'll be valid.
db = PyBase("example", "JSON")  #=> ./example.json
# Lets define and add some content to our database.
pybase_info = {"pybase": "awesomeness", "version": "0.1.0"}
# Lets insert the defined dict inside our database.
db.insert(pybase_info)  #=> {'pybase': 'awesomeness', 'version': '0.1.0'}
print(db.read())
# Lets delete an object inside our database cuz it's useless.
db.delete('pybase')  #=> {'version': '0.1.0'}
print(db.read())
# Lets fetch an object inside our database and display its type.
# It's useful to debug and manipulate the data dynamically.
print(db.fetch('version'))
