# NTBBloodbath | PyBase v0.3.0
# Usage example file (for v0.3.0).

# Lets import PyBase Class from PyBase Package
from src.pybase_db import PyBase

# Lets define our database name and format (with default db_path).
# db_type isn't case sensitive. You can use JSON and json and it'll be valid.
db = PyBase("example", "JSON")  #=> ./example.json

# Lets define and add some content to our database.
pybase_info = {"pybase": "awesomeness", "version": "0.3.0"}

# Lets insert the defined dict inside our database.
db.insert(pybase_info)  #=> {'pybase': 'awesomeness', 'version': '0.3.0'}
print(db.get())

# Lets delete an object inside our database cuz it's useless.
db.delete('pybase')  #=> {'version': '0.3.0'}
print(db.get())

# Lets fetch an object inside our database and display its type.
# It's useful to debug and manipulate the data dynamically.
print(db.fetch('version'))

# Gets the corresponding value according to the specified key
print(db.get("version")) #=> '0.3.0'

# New data of the new update
pybase_update = {"pybase": {"newVersion": {"version": "0.3.1" } } }
db.insert(pybase_update)

# Get all data from db
print(db.get()) # => {'pybase': {'newVersion': {'version': '0.3.1'}}, 'version': '0.3.0'}

# Get the values ​​using its key
print(db.get("pybase"))# => {'newVersion': {'version': '0.3.1'}}

# Get a value of a key separated by a period (.)
print(db.get("pybase.newVersion")) # => {'version': '0.3.1'}

# Several
print(db.get("pybase.newVersion.version")) # => 0.3.1