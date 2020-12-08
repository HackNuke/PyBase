# Changelog
This is a detailed and complete changelog of the different versions of PyBase.
> Notes: 
> 
> 1. **This changelog contains the changes from version 0.4.0 onwards.**
> 
> 2. Version changelogs contain all unified changes from all development versions.

------

- v1.0.0
  - Breaking changes:
    - Global:
      - Added optionally logs. Now you can have a register of what was happening to your database (enabled by default).
      - Config file was added (**see [example config](https://github.com/PyBase/PyBase/blob/development/examples/pybase.yaml)**). Now debugging (debug, stats) and logs are configurations instead of parameters.
      - The `debug` parameter has been added to the config, now you can see what happens behind the curtains!
      - The `stats` parameter has been added to the config, now you can see how much CPU and RAM is consuming PyBase!
    - PyBase Class:
      - `exists` method has been removed because it was considered useless.
      - `fetch` and `delete` methods have been changed to be simpler and more dev-friendly!
  - Another changes under the hood and bug fixes:
    - Global:
      - Some methods were optimized in both modules.
      - Dependencies have been updated and now they are managed by dependa-bot so they are always up to date!
      - Added `psutil` to dependencies.
    - PyBase Class:
      - Added full support for TOML files.
      - Added `push` method, see [docs](https://pybase.netlify.app/docs/v1.0.0.html#pybase-push). Push a item into a list inside your database without having a headache!
      - Added `rename` method, see [docs](https://pybase.netlify.app/docs/v1.0.0.html#pybase-rename). Did you make a mistake in a character in the name of a key? Don't worry, you no longer have to manually open your database to fix it!
      - Added `update` method, see [docs](https://pybase.netlify.app/docs/v1.0.0.html#pybase-update). Update the values of your keys inside the database.
      - Now the init doesn't raise errors when the specified path doesn't exists. Instead, it tries to create the path.
      - Now the `insert` method have a parameter called `mode`. Now when inserting data to an existing key the old data will not be overwritten!

> **Notes about v1.0.0**:
>  
> 1. Since version 1.0.0 is under development, it isn't ready
> yet and therefore this changelog notes may change and if there's
> no release yet with the newest changes, you'll have to compile it yourself.
> See [Building](https://github.com/PyBase/PyBase#building).
> 
> 2. Statistics are currently sent every two minutes by default. You can change the time in the config file.
> 
> 3. Logs files are currently deleted after 7 days by default. You can change the life cycle in the config file.

---

- [v0.5.0](https://github.com/PyBase/PyBase/releases/tag/v0.5.0)
  - PyBase Class:
    - Added `has` method, see [docs](https://pybase.netlify.app/docs/v0.5.0.html#pybase-has)

---

- [v0.4.0](https://github.com/PyBase/PyBase/releases/tag/v0.4.0)
  - Global:
    - Logs changed to rich library logs
    - Traceback changed to rich library traceback
  - PyBase Class:
    - Now you can get values through several keys separated by a period
  - PySQL Class:
    - Added `get` method, see [docs](https://pybase.netlify.app/docs/v0.4.1.html#pysql-get)
    - Bug fixes when adding lists inside the DB
