# PyBase — Changelog
This is a detailed and complete changelog of the different versions of PyBase.
> Note: **This changelog contains the changes from version 0.4.0 onwards.**

------

- v1.0.0
  - Breaking changes:
    - `exists` method has been removed because it was useless (PyBase Class).
    - `fetch` method has been changed to be simpler and more dev-friendly (PyBase Class)!
  - Another changes under the hood and bug fixes:
    - Added `push` method. Push a item into a list inside your database without having a headache (PyBase Class)!
    - Added `update` method. Update the values of your keys inside the database (PyBase Class).
    - Now the init doesn't raise errors when the specified path doesn't exists. Instead, it tries to create the path (PyBase Class).
    - Now `insert` method have a parameter called `mode`. Now when inserting data to an existing key the old data will not be overwritten (PyBase Class)!
    - The `debug` parameter has been added to the init, now you can see what happens behind the curtains (PyBase Class)!
    - The `stats` parameter has been added to the init, now you can see how much CPU and RAM is consuming PyBase (PyBase Class)!
    - Dependencies have been updated and `psutil` added to dependencies.

> **Notes about v1.0.0**:
> 
> 1. Since the documentation will change and isn't ready yet,
> you can see the changes by comparing the usage example of
> the [development](https://github.com/NTBBloodbath/PyBase/blob/development/examples/basic_usage_example.py) branch with that of [master](https://github.com/NTBBloodbath/PyBase/blob/master/examples/basic_usage.py).
> 
> 2. Since version 1.0.0 is under development, it isn't ready
> yet and therefore this changelog notes may change and there's
> no release yet. If you want to test it, you'll have to compile it yourself.
> 
> 3. Since the `stats` parameter is part of the `debug`, you'll
> need to set both parameters to `True` for it to work. Statistics
> are currently sent every two minutes.

---

- [v0.4.0](https://github.com/NTBBloodbath/PyBase/releases/tag/v0.4.0)
    - Added `get` method, see [docs](https://ntbbloodbath.github.io/PyBase/docs/0.4/#gettable-str-objects-dict--none) for usage example (PySQL class)
    - Bug fixes when adding lists inside the DB (PySQL class)
    - Logs changed to rich library logs (PyBase and PySQL classes)
    - Traceback changed to rich library traceback (PyBase and PySQL classes)
    - Now you can get values through several keys separated by a period (PyBase class)
