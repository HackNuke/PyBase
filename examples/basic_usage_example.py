# NTBBloodbath | PyBase v1.0.0
# Usage example file (for v1.0.0).

# Lets import PyBase Class from PyBase Package
from pybase_db import PyBase

# Lets define our database name and format (with default db_path).
# db_type isn't case sensitive. You can use JSON and json and it'll be valid.
db = PyBase("example", "JSON", debug=True, stats=True)  # => ./example.json

# Lets define and add some content to our database.
pybase_info = {"pybase": "awesomeness", "version": "1.0.0"}

# Lets insert the defined dict inside our database.
db.insert(pybase_info,
          mode="w")  # => {'pybase': 'awesomeness', 'version': '1.0.0'}

# Lets delete an object inside our database cuz it's useless.
db.delete('pybase')  # => {'version': '1.0.0'}

# Lets insert more data cuz that's funny!
db.insert(content={"guilds": {}, "ownerID": 1234567890}, mode="w")

# Lets insert some data inside the guilds key
db.insert(content={
    "guilds": {
        "12345": {
            "name": "First guild"
        },
        "67890": {
            "name": "Second guild"
        }
    }
},
          mode="a")

# Lets fetch an object inside our database and display its type.
# It's useful to debug and manipulate the data dynamically.
db.fetch('version')  # => <class 'str'>

# Gets the corresponding value according to the specified key
db.get("version")  # => '1.0.0'

# New data of the new update
pybase_update = {"pybase": {"newVersion": {"version": "1.0.0"}}}
db.insert(pybase_update)

# Get all data from db
db.get()  # => {'pybase': {'newVersion': {'version': '1.0.0'}}, 'version': '1.0.0'}

# Get the values using its key
db.get("pybase")  # => {'newVersion': {'version': '1.0.0'}}

# Get a value of a key separated by a period (.)
db.get("pybase.newVersion")  # => {'version': '1.0.0'}

# Several
db.get("pybase.newVersion.version")  # => 1.0.0
