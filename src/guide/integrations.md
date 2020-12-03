# Integrations

![Undraw Setup](../static/img/undraw_Setup_re_y9w8.png)

Learn here how to integrate PyBase to your different projects!

> Note: you can find full integration examples in [our GitHub org](https://github.com/PyBase).

::: tip Read the docs
We highly recommend reading the [documentation](/docs/) for the version
you are using to better understand the code found in this section.
:::

---

## Discord.py
In this discord.py integration guide we will see how to store
the configuration of our bot and the servers it is on.

```py
# In our index file
from pybase_db import PyBase

# Let's define our database.
db = PyBase(database="config", db_type="toml", db_path="./db")

# Let's obtain our bot's token and prefix from the database.
token = db.get("token")
prefix = db.get("prefix")
```

> **Explanation:**
- **L#2** - We import the PyBase class from the pybase_db package
- **L#5** - We define our database, with name `config`, type `TOML` and located in the `db` folder (it will look something like this `./db/config.toml`)
- **L#8** - We obtain the value of the `token` key in our database
- **L#9** - We obtain the value of the `prefix` key in our database
