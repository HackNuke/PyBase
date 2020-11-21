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
    - Added optionally logs. Now you can have a register of what was happening to your database (enabled by default).
    - Config file was added (**see [example config](./examples/pybase.yaml)**). Now debugging (debug, stats) and logs are configurations instead of parameters.
    - `exists` method has been removed because it was considered useless (PyBase Class).
    - `fetch` method has been changed to be simpler and more dev-friendly (PyBase Class)!
  - Another changes under the hood and bug fixes:
    - Added full support for TOML files (PyBase Class).
    - Added `push` method. Push a item into a list inside your database without having a headache (PyBase Class)!
    - Added `update` method. Update the values of your keys inside the database (PyBase Class).
    - Now the init doesn't raise errors when the specified path doesn't exists. Instead, it tries to create the path.
    - Now the `insert` method have a parameter called `mode`. Now when inserting data to an existing key the old data will not be overwritten (PyBase Class)!
    - The `debug` parameter has been added to the config, now you can see what happens behind the curtains!
    - The `stats` parameter has been added to the config, now you can see how much CPU and RAM is consuming PyBase!
    - Some methods were optimized in both modules.
    - Dependencies have been updated and now they are managed by renovate-bot so they are always up to date!
    - Added `psutil` to dependencies.

> **Notes about v1.0.0**:
> 
> 1. Since the documentation will change and isn't ready yet,
> you can see the changes by comparing the usage example of
> the [development](https://github.com/NTBBloodbath/PyBase/blob/development/examples/basic_usage_example.py) branch with that of [master](https://github.com/NTBBloodbath/PyBase/blob/master/examples/basic_usage.py).
> 
> 2. Since version 1.0.0 is under development, it isn't ready
> yet and therefore this changelog notes may change and if there's
> no release yet with the newest changes, you'll have to compile it yourself.
> See [Building](https://github.com/NTBBloodbath/PyBase#building).
> 
> 3. Statistics are currently sent every two minutes by default.

---

- [v0.4.0](https://github.com/NTBBloodbath/PyBase/releases/tag/v0.4.0)
    - Added `get` method, see [docs](https://ntbbloodbath.github.io/PyBase/docs/0.4/#gettable-str-objects-dict--none) for usage example (PySQL class)
    - Bug fixes when adding lists inside the DB (PySQL class)
    - Logs changed to rich library logs (PyBase and PySQL classes)
    - Traceback changed to rich library traceback (PyBase and PySQL classes)
    - Now you can get values through several keys separated by a period (PyBase class)
