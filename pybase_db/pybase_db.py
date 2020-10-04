#       NTBBloodbath | PyBase v0.5.0       #
############################################
# PyBase is distributed under MIT License. #

# dependencies (packages/modules)
import json
import os
import pathlib
import pickle
import threading
from time import sleep

import psutil
import yaml
from rich.console import Console
from rich.traceback import install

install()  # Use Rich traceback handler as the default error handler
console = Console()


class PyBase:
    """
    PyBase Main Class

    ...

    Attributes
    ----------

    Methods
    -------
    delete(key: str=None)
        Delete a object from the database established in PyBase init.
    fetch(key: str=None)
        Fetch a key inside the database established in PyBase init.
    insert(content: dict, mode: str="w")
        Insert a dictionary content inside the given database file.
    get(key: str=None)
        Read the database file established in PyBase init to to access its objects.

    TODO:
        Add more useful methods.
    """
    def __init__(self,
                 database: str,
                 db_type: str,
                 db_path: str = pathlib.Path().absolute(),
                 debug: bool = False,
                 stats: bool = False):
        """
        Define the database to use and create it if it doesn't exist.

        ...

        Parameters
        ----------
        database : str
            The name of the database without extension.
        db_type : str
            The database type.
            Available types: yaml, json, bytes
            Note: To use SQLite3, use the PySQL module.
        db_path : str, optional
            The path where the database is located (default is current working directory).
            Example: /home/bloodbath/Desktop/PyBase
        debug : bool, optional
            Debug messages. See what's happening in your database behind the curtains!
            Default: False
        stats : bool, optional
            Stadistics messages. See how much CPU and RAM PyBase is using every minute (in percentage)!
            Default: False
            Note: You must have debug enabled to use the statistics!

        Raises
        ------
        TypeError
            If database or db_type isn't a String.
            If debug isn't a Boolean.
            If stats isn't a Boolean.
        ValueError
            If the given db_type isn't a valid type (JSON, YAML, Bytes).
        FileNotFoundError
            If the given path wasn't found.
        """

        self.__path = db_path  # private path variable to clean code.

        if isinstance(debug, bool):
            self.__debug = debug
        else:
            raise TypeError('debug must be a Boolean.')
        if isinstance(stats, bool):
            self.__stats = stats
        else:
            raise TypeError('stats must be a Boolean.')

        if type(database) != str:
            raise TypeError('database must be a String.')
        elif type(db_type) != str:
            raise TypeError('db_type must be a String.')
        elif os.path.exists(db_path) is not True:
            raise FileNotFoundError(
                f'The path ({self.__path}) wasn\'t found. Please check that the path exists.'
            )
        elif type(db_type) == str:
            self.__EXTENSION = '.' + db_type.lower()
            self.__DB = (f'{self.__path}/{database}{self.__EXTENSION}')
            if self.__debug:
                console.log(
                    f"[DEBUG]: Searching if the database ({self.__DB}) exists ..."
                )
            if db_type.lower() == 'json':
                if os.path.exists(self.__DB) is False:
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG]: Trying to create the database file ({self.__DB}) ..."
                        )
                    try:
                        with open(self.__DB, mode='w+',
                                  encoding='utf-8') as json_file:
                            json.dump({}, json_file)
                        if self.__debug:
                            sleep(0.5)
                            console.log(
                                "[DEBUG]: The database file was created successfully."
                            )
                    except Exception:
                        console.print_exception()
            elif db_type.lower() == 'yaml':
                if os.path.exists(self.__DB) is False:
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG]: Trying to create the database file ({self.__DB}) ..."
                        )
                    try:
                        with open(self.__DB, mode='w+',
                                  encoding='utf-8') as yaml_file:
                            yaml.dump({}, yaml_file)
                        if self.__debug:
                            sleep(0.5)
                            console.log(
                                "[DEBUG]: The database file was created successfully."
                            )
                    except Exception:
                        console.print_exception()
            elif db_type.lower() == "bytes":
                if not os.path.exists(self.__DB):
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG]: Trying to create the database file ({self.__DB}) ..."
                        )
                    try:
                        with open(self.__DB, mode="wb") as bytes_file:
                            pickle.dump({}, bytes_file)
                        if self.__debug:
                            sleep(0.5)
                            console.log(
                                "[DEBUG]: The database file was created successfully."
                            )
                    except Exception:
                        console.print_exception()
            else:
                raise ValueError('db_type must be JSON, YAML or Bytes.')
        if self.__debug and self.__stats:
            try:
                self.__interval(self.__send_stats, 60)
            except Exception:
                console.print_exception()

    def delete(self, key: str = None):
        """
        Delete a object from the database established in PyBase init.

        ...

        Parameters
        ----------
        key : str
            The object which will be deleted from the database.
            Default: None

        Raises
        ------
        KeyError
            If the given key isn't found.
        ValueError
            If key isn't a String.
        """

        if len(key) == 0 or key is None:
            raise ValueError('key must be a String.')
        else:
            if self.__EXTENSION == '.json':
                try:
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG]: Trying to delete the {key} key ...")
                    with open(self.__DB, encoding='utf-8') as json_file:
                        data = json.load(
                            json_file)  # Pass JSON to Python objects.
                        if self.__util_split(key, data):
                            data.pop(key)  # Delete the given object.
                        else:
                            raise KeyError(
                                f"\"{key}\" Does not exist in the file")
                    with open(self.__DB, mode='w',
                              encoding='utf-8') as json_file:
                        json.dump(data, json_file, indent=4,
                                  sort_keys=True)  # Save
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG] The key {key} was successfully deleted.")
                except KeyError:
                    console.print_exception()
            elif self.__EXTENSION == '.yaml':
                try:
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG]: Trying to delete the {key} key ...")
                    with open(self.__DB, encoding='utf-8') as yaml_file:
                        data = yaml.load(yaml_file, Loader=yaml.FullLoader)
                        if self.__util_split(key, data):
                            data.pop(key)
                        else:
                            raise KeyError(
                                f"\"{key}\" Does not exist in the file")
                    with open(self.__DB, mode='w',
                              encoding='utf-8') as yaml_file:
                        yaml.dump(data, yaml_file, sort_keys=True)
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG] The key {key} was successfully deleted.")
                except KeyError:
                    console.print_exception()
            elif self.__EXTENSION == '.bytes':
                try:
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG]: Trying to delete the {key} key ...")
                    with open(self.__DB, mode="rb") as bytes_file:
                        data = pickle.load(bytes_file)
                        if self.__util_split(key, data):
                            data.pop(key)
                        else:
                            raise KeyError(
                                f"\"{key}\" Does not exist in the file")
                    with open(self.__DB, mode="wb") as bytes_file:
                        pickle.dump(data, bytes_file)
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG] The key {key} was successfully deleted.")
                except KeyError:
                    console.print_exception()

    def fetch(self, key: str = None):
        """
        Fetch a key and its sub_objects inside the database established in PyBase init.

        ...

        Parameters
        ----------
        key : str
            The key which will be fetched inside the database.
            Default: None

        Raises
        ------
        TypeError
            If key isn't a String
        KeyError
           When the key does not exist in the specified file type

        Returns
        -------
        str
            If the object is a String.
        int
            If the object is a Integer.
        float
            If the object is a Float.
        bool
            If the object is a Boolean.
        list / tuple
            If the object is a list or a tuple.
        dict
            If the object is a dict.
        """
        if type(key) != str:
            raise TypeError('key must be a String.')
        else:
            if self.__debug:
                sleep(0.5)
                console.log(f"[DEBUG]: Searching for the key {key} ...")
            try:
                if self.__EXTENSION == ".json":
                    if key is None:
                        with open(self.__DB, mode="r+",
                                  encoding="utf-8") as json_file:
                            data = json.load(json_file) or {}
                            self.__close_file_delete(json_file)
                            if self.__debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its type is {type(data)}."
                                )
                            return type(data)
                    else:
                        with open(self.__DB, mode="r+",
                                  encoding="utf-8") as json_file:
                            data = json.load(json_file) or {}
                            self.__close_file_delete(json_file)
                            if self.__util_split(key, data):
                                if self.__debug:
                                    sleep(0.5)
                                    console.log(
                                        f"[DEBUG]: {key} was found and its type is {type(data)}"
                                    )
                                return type(self.__util_split(key, data))
                            else:
                                raise KeyError(
                                    f"\"{key}\" Does not exist in the file")
                elif self.__EXTENSION == ".yaml":
                    if key is None:
                        with open(self.__DB, mode='r+',
                                  encoding='utf-8') as yaml_file:
                            data = yaml.load(yaml_file,
                                             Loader=yaml.FullLoader) or {}
                            self.__close_file_delete(yaml_file)
                            if self.__debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its type is {type(data)}."
                                )
                            return type(data)
                    else:
                        with open(self.__DB, mode='r+',
                                  encoding='utf-8') as yaml_file:
                            data = yaml.load(yaml_file,
                                             Loader=yaml.FullLoader) or {}
                            self.__close_file_delete(yaml_file)
                            if self.__util_split(key, data):
                                if self.__debug:
                                    sleep(0.5)
                                    console.log(
                                        f"[DEBUG]: {key} was found and its type is {type(data)}"
                                    )
                                return type(self.__util_split(key, data))
                            else:
                                raise KeyError(
                                    f"\"{key}\" Does not exist in the file")
                elif self.__EXTENSION == ".bytes":
                    if key is None:
                        with open(self.__DB, mode="rb") as bytes_file:
                            data = pickle.load(bytes_file)
                            self.__close_file_delete(bytes_file)
                            if self.__debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its type is {type(data)}."
                                )
                            return type(data)
                    else:
                        with open(self.__DB, mode='rb') as bytes_file:
                            data = pickle.load(bytes_file) or {}
                            self.__close_file_delete(bytes_file)
                            if self.__util_split(key, data):
                                if self.__debug:
                                    sleep(0.5)
                                    console.log(
                                        f"[DEBUG]: {key} was found and its type is {type(data)}"
                                    )
                                return type(self.__util_split(key, data))
                            else:
                                raise KeyError(
                                    f"\"{key}\" Does not exist in the file")
            except Exception:
                console.print_exception()

    def insert(self, content: dict, mode: str = "w"):
        """
        Insert a dictionary content inside the database file established in PyBase init.

        ...

        Parameters
        ----------
        content : dict
            The content which will be inserted inside the database.
        mode : str, optional
            The way the data will be inserted ("w" for write and "a" for append).
            Default: "w"

        Raises
        ------
        TypeError
            If content isn't a dictionary.
            If mode isn't a String.
        ValueError
            If mode isn't equal to "w" or "a"
        """

        if type(content) != dict:
            raise TypeError('content must be a dictionary.')
        if type(mode) != str:
            raise TypeError('mode must be a String.')
        if mode != "w" and mode != "a":
            raise ValueError('mode must be "w" or "a".')
        else:
            if self.__debug:
                sleep(0.5)
                console.log(
                    f"[DEBUG]: Trying to insert {content} in mode {mode} inside the database ..."
                )
            if self.__EXTENSION == '.json':
                try:
                    if mode == "w":
                        with open(self.__DB, encoding='utf-8') as json_file:
                            data = json.load(json_file)
                            data.update(content)
                        with open(self.__DB, mode='w',
                                  encoding='utf-8') as json_file:
                            json.dump(data,
                                      json_file,
                                      indent=4,
                                      sort_keys=True)
                    elif mode == "a":
                        with open(self.__DB, encoding='utf-8') as json_file:
                            data = json.load(json_file)
                            for new_key in content:
                                for original_key in data:
                                    if new_key in original_key:
                                        data[original_key].update(
                                            content[new_key])
                                    else:
                                        data.update(
                                            {new_key: content[new_key]})
                                        break
                        with open(self.__DB, mode='w',
                                  encoding='utf-8') as json_file:
                            json.dump(data,
                                      json_file,
                                      indent=4,
                                      sort_keys=True)
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            "[DEBUG]: The data was successfully inserted inside the database."
                        )
                except Exception:
                    console.print_exception()
            elif self.__EXTENSION == '.yaml':
                try:
                    if mode == "w":
                        with open(self.__DB, encoding='utf-8') as yaml_file:
                            data = yaml.load(yaml_file, Loader=yaml.FullLoader)
                            data.update(content)
                        with open(self.__DB, mode='w',
                                  encoding='utf-8') as yaml_file:
                            yaml.dump(data, yaml_file, sort_keys=True)
                    elif mode == "a":
                        with open(self.__DB, encoding='utf-8') as yaml_file:
                            data = yaml.load(yaml_file, Loader=yaml.FullLoader)
                            for new_key in content:
                                for original_key in data:
                                    if new_key in original_key:
                                        data[original_key].update(
                                            content[new_key])
                                    else:
                                        data.update(
                                            {new_key: content[new_key]})
                                        break
                        with open(self.__DB, mode='w',
                                  encoding='utf-8') as yaml_file:
                            yaml.dump(data, yaml_file, sort_keys=True)
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            "[DEBUG]: The data was successfully inserted inside the database."
                        )
                except Exception:
                    console.print_exception()
            elif self.__EXTENSION == '.bytes':
                try:
                    if mode == "w":
                        with open(self.__DB, mode="rb") as bytes_file:
                            data = pickle.load(bytes_file) or {}
                            data.update(content)
                        with open(self.__DB, mode='wb') as bytes_file:
                            pickle.dump(data, bytes_file)
                    if mode == "a":
                        with open(self.__DB, mode="rb") as bytes_file:
                            data = pickle.load(bytes_file)
                            for new_key in content:
                                for original_key in data:
                                    if new_key in original_key:
                                        data[original_key].update(
                                            content[new_key])
                                    else:
                                        data.update(
                                            {new_key: content[new_key]})
                                        break
                        with open(self.__DB, mode="wb") as bytes_file:
                            pickle.dump(data, bytes_file)
                    if self.__debug:
                        sleep(0.5)
                        console.log(
                            "[DEBUG]: The data was successfully inserted inside the database."
                        )
                except Exception:
                    console.print_exception()

    def get(self, key: str = None):
        """
        Read the database file established in PyBase init to access its objects or values ​​using the key.

        ...

        Parameters
        ----------
        key : str, optional
            The key of the first value of the dictionary
            Default: None

        Raises
        ------
        KeyError
            When the key does not exist in the specified file type

        Returns
        -------
        dict
            A dictionary which contains all the database objects.
        """

        if self.__debug:
            sleep(0.5)
            console.log(
                f"[DEBUG]: Trying to get the key {key} from the database ...")
        try:
            if self.__EXTENSION == ".json":
                if key is None:
                    with open(self.__DB, mode="r+",
                              encoding="utf-8") as json_file:
                        data = json.load(json_file) or {}
                        self.__close_file_delete(json_file)
                        if self.__debug:
                            sleep(0.5)
                            console.log(f"[DEBUG]: {key} was found.")
                        return data
                else:
                    with open(self.__DB, mode="r+",
                              encoding="utf-8") as json_file:
                        data = json.load(json_file) or {}
                        self.__close_file_delete(json_file)
                        if self.__util_split(key, data):
                            if self.__debug:
                                sleep(0.5)
                                console.log(f"[DEBUG]: {key} was found and its value is {self.__util_split(key, data)}.")
                            return self.__util_split(key, data)
                        else:
                            raise KeyError(
                                f"\"{key}\" Does not exist in the file")
            elif self.__EXTENSION == ".yaml":
                if key is None:
                    with open(self.__DB, mode='r+',
                              encoding='utf-8') as yaml_file:
                        data = yaml.load(yaml_file,
                                         Loader=yaml.FullLoader) or {}
                        self.__close_file_delete(yaml_file)
                        if self.__debug:
                            sleep(0.5)
                            console.log(f"[DEBUG]: {key} was found.")
                        return data
                else:
                    with open(self.__DB, mode='r+',
                              encoding='utf-8') as yaml_file:
                        data = yaml.load(yaml_file,
                                         Loader=yaml.FullLoader) or {}
                        self.__close_file_delete(yaml_file)
                        if self.__util_split(key, data):
                            if self.__debug:
                                sleep(0.5)
                                console.log(f"[DEBUG]: {key} was found and its value is {self.__util_split(key, data)}.")
                            return self.__util_split(key, data)
                        else:
                            raise KeyError(
                                f"\"{key}\" Does not exist in the file")
            elif self.__EXTENSION == ".bytes":
                if key is None:
                    with open(self.__DB, mode="rb") as bytes_file:
                        data = pickle.load(bytes_file)
                        self.__close_file_delete(bytes_file)
                        if self.__debug:
                            sleep(0.5)
                            console.log(f"[DEBUG]: {key} was found.")
                        return data
                else:
                    with open(self.__DB, mode='rb') as bytes_file:
                        data = pickle.load(bytes_file) or {}
                        self.__close_file_delete(bytes_file)
                        if self.__util_split(key, data):
                            if self.__debug:
                                sleep(0.5)
                                console.log(f"[DEBUG]: {key} was found and its value is {self.__util_split(key, data)}.")
                            return self.__util_split(key, data)
                        else:
                            raise KeyError(
                                f"\"{key}\" Does not exist in the file")
        except Exception:
            console.print_exception()

    def __close_file_delete(self, file):
        """
        Method only for the class, close the open file and erase it from memory (slightly better performance)
        ...

        Parameters
        ----------
        file
            an open (or closed) file

        Raises
        ------
        """
        try:
            close_file = file.close()
            if close_file is None:
                del (file)
        except Exception:
            console.print_exception()

    def __util_split(self, key: str, data: dict):
        """
        Method only for the class, split dict from key specific
        ...

        Parameters
        ----------
        key : str
            The key of the dictionary
        data : dict
            The content.

        Raises
        ------
        TypeError
            key is not a str or data is not a dict

        """
        if type(key) != str:
            raise TypeError(f"the type of {key} is invalid.")
        elif type(data) != dict:
            raise TypeError(f'data "{data}" must be a dictionary.')

        args = key.split(".")
        dataObject = data
        for keys in args:
            if keys not in dataObject.keys():
                return False
            elif keys == args[len(args) - 1]:
                return dataObject[keys]
            else:
                dataObject = dataObject[keys]

    def __send_stats(self):
        pybase_process   = psutil.Process(os.getpid())                 # Get PyBase process ID
        pybase_cpu_usage = pybase_process.cpu_percent(interval=1.0)    # CPU Usage in percentage
        pybase_ram_usage = round(pybase_process.memory_percent(), 1)   # Memory usage in percentage
        console.log(f"""[DEBUG]: Showing PyBase Usage stadistics ...
         CPU Usage: {pybase_cpu_usage}%
         RAM Usage: {pybase_ram_usage}%""")

    def __interval(self, func, sec):
        def func_wrapper():
            self.__interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t
