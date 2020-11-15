#       NTBBloodbath | PyBase v1.0.0       #
############################################
# PyBase is distributed under MIT License. #

# dependencies (packages/modules)
import datetime
import json
import os
import pathlib
import pickle
from threading import Thread
from time import sleep

import toml
import yaml
from rich.console import Console
from rich.traceback import install

from .utils import Utils
from .version import __version__

install() # Use Rich traceback handler as the default error handler
console = Console()


class PyBase:
    """
    PyBase Main Class

    ...

    Attributes
    ----------

    Methods
    -------
    delete(obj)
        Delete a object from the database established in PyBase init.
    fetch(key: str=None)
        Fetch a key inside the database established in PyBase init.
    get(key: str=None)
        Read the database file established in PyBase init to to access its objects.
    insert(content: dict, mode: str="w")
        Insert a dictionary content inside the given database file.
    push(key: str=None, element=None)
        Push a new element to a list inside the database.
    update(key: str=None, new_value=None)
        Update the value of a key inside the database.
    """
    def __init__(self,
                 database: str,
                 db_type: str,
                 db_path: str = pathlib.Path().absolute()):
        """
        Define the database to use and create it if it doesn't exist.

        ...

        Parameters
        ----------
        database : str
            The name of the database without extension.
        db_type : str
            The database type.
            Available types: yaml, json, toml, bytes
            Note: To use SQLite3, use the PySQL module.
        db_path : str, optional
            The path where the database is located (default is current working directory).
            Example: /home/bloodbath/Desktop/PyBase

        Raises
        ------
        TypeError
            If database or db_type isn't a String.
        ValueError
            If the given db_type isn't a valid type (JSON, YAML, TOML, Bytes).
        """

        self.__path = db_path

        # Search for config file
        Utils().search_config()

        if type(database) != str:
            raise TypeError('database must be a String.')
        elif type(db_type) != str:
            raise TypeError('db_type must be a String.')
        elif type(db_type) == str:
            self.__EXTENSION = '.' + db_type.lower()
            self.__DB = (f'{self.__path}/{database}{self.__EXTENSION}')

            if Utils().debug:
                console.log(
                    f"[DEBUG]: Using PyBase v{__version__}"
                )

            if os.path.exists(self.__path) is False:
                if Utils().debug:
                    sleep(0.5)
                    console.log(
                        "[DEBUG]: The established path doesn't exist. Trying to create it ..."
                    )
                try:
                    pathlib.Path(self.__path).mkdir(parents=True,
                                                    exist_ok=True)
                except Exception:
                    console.print_exception()
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="w") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                            )
            if os.path.exists(Utils().logs_location) is False:
                if Utils().debug:
                    sleep(0.5)
                    console.log(
                        "[DEBUG]: The established logs location doesn't exist. Trying to create it ..."
                    )
                try:
                    pathlib.Path(Utils().logs_location).mkdir(parents=True,
                                                             exist_ok=True)
                except Exception:
                    console.print_exception()
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                            )

            # Search for old logs files and delete them every 20m
            if Utils().logs_enabled:
                def search_old_logs():
                    Utils().delete_old_logs()
                    sleep(Utils().time_to_seconds("1m"))

                delete_old_logs = Thread(target = search_old_logs)
                delete_old_logs.daemon = True
                delete_old_logs.start()
            
            if Utils().debug:
                sleep(0.5)
                console.log(
                    f"[DEBUG]: Searching if the database ({self.__DB}) exists ..."
                )
            if db_type.lower() == 'json':
                if os.path.exists(self.__DB) is False:
                    if Utils().debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG]: Trying to create the database file ({self.__DB}) ..."
                        )
                    try:
                        with open(self.__DB, mode='w+',
                                  encoding='utf-8') as json_file:
                            json.dump({}, json_file)
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                "[DEBUG]: The database file was created successfully."
                            )
                        if Utils().logs_enabled:
                            if len(os.listdir(Utils().logs_location)) == 0:
                                with open(f"{Utils().logs_location}/logfile_{datetime.datetime.utcnow().strftime('%Y-%m-%d')}.log", mode="w") as log_file:
                                    log_file.write(
                                        f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                        + "========================\n"
                                        + f"The database was created successfully\n({self.__DB}).\n\n"
                                    )
                    except Exception as err:
                        console.print_exception()
                        if Utils().logs_enabled:
                            with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                log_file.write(
                                    f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                    + "========================\n"
                                    + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                                )
            elif db_type.lower() == 'yaml':
                if os.path.exists(self.__DB) is False:
                    if Utils().debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG]: Trying to create the database file ({self.__DB}) ..."
                        )
                    try:
                        with open(self.__DB, mode='w+',
                                  encoding='utf-8') as yaml_file:
                            yaml.dump({}, yaml_file)
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                "[DEBUG]: The database file was created successfully."
                            )
                    except Exception as err:
                        console.print_exception()
                        if Utils().logs_enabled:
                            with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                log_file.write(
                                    f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                    + "========================\n"
                                    + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                                )
            elif db_type.lower() == 'toml':
                if os.path.exists(self.__DB) is False:
                    if Utils().debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG]: Trying to create the database file ({self.__DB}) ..."
                        )
                    try:
                        with open(self.__DB, mode='w+',
                                  encoding='utf-8') as toml_file:
                            toml.dump({}, toml_file)
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                "[DEBUG]: The database file was created successfully."
                            )
                        if Utils().logs_enabled:
                            if len(os.listdir(Utils().logs_location)) == 0:
                                with open(f"{Utils().logs_location}/logfile_{datetime.datetime.utcnow().strftime('%Y-%m-%d')}.log", mode="w") as log_file:
                                    log_file.write(
                                        f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                        + "========================\n"
                                        + f"The database was created successfully\n({self.__DB}).\n\n"
                                    )
                    except Exception as err:
                        console.print_exception()
                        if Utils().logs_enabled:
                            with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                log_file.write(
                                    f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                    + "========================\n"
                                    + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                                )
            elif db_type.lower() == "bytes":
                if not os.path.exists(self.__DB):
                    if Utils().debug:
                        sleep(0.5)
                        console.log(
                            f"[DEBUG]: Trying to create the database file ({self.__DB}) ..."
                        )
                    try:
                        with open(self.__DB, mode="wb") as bytes_file:
                            pickle.dump({}, bytes_file)
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                "[DEBUG]: The database file was created successfully."
                            )
                        if Utils().logs_enabled:
                            if len(os.listdir(Utils().logs_location)) == 0:
                                with open(f"{Utils().logs_location}/logfile_{datetime.datetime.utcnow().strftime('%Y-%m-%d')}.log", mode="w") as log_file:
                                    log_file.write(
                                        f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                        + "========================\n"
                                        + f"The database was created successfully\n({self.__DB}).\n\n"
                                    )
                    except Exception as err:
                        console.print_exception()
                        if Utils().logs_enabled:
                            with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                log_file.write(
                                    f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                    + "========================\n"
                                    + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                                )
            else:
                raise ValueError('db_type must be JSON, YAML, TOML or Bytes.')
        if Utils().stats_enabled:
            try:
                Utils().interval(Utils().send_stats, Utils().time_to_seconds(Utils().stats_interval))
            except Exception as err:
                console.print_exception()
                if Utils().logs_enabled:
                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                        log_file.write(
                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                            + "========================\n"
                            + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                        )

    def delete(self, obj):
        """
        Delete a object from the database established in PyBase init.

        ...

        Parameters
        ----------
        obj
            The object which will be deleted from the database.

        Raises
        ------
        KeyError
            If key isn't found.
        ValueError
            If obj doesn't have a value (is equal to zero or None).
        """

        if len(obj) == 0 or obj is None:
            raise ValueError('obj must have a value (str, int, float, bool).')
        else:
            if self.__EXTENSION == '.json':
                try:
                    with open(self.__DB, encoding='utf-8') as json_file:
                        data = json.load(json_file)
                        data.pop(obj)
                    with open(self.__DB, encoding="utf-8", mode="w") as json_file:
                        json.dump(data, json_file, indent=4, sort_keys=True)
                        Utils().close_file_delete(json_file)
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"{obj} key have been removed from the database.\n\n"
                            )
                except KeyError as err:
                    console.print_exception()
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                            )
            elif self.__EXTENSION == '.yaml':
                try:
                    with open(self.__DB, encoding='utf-8') as yaml_file:
                        data = yaml.safe_load(yaml_file)
                        data.pop(obj)
                    with open(self.__DB, encoding='utf-8', mode='w') as yaml_file:
                        yaml.dump(data, yaml_file, sort_keys=True)
                        Utils().close_file_delete(yaml_file)
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"{obj} key have been removed from the database.\n\n"
                            )
                except KeyError as err:
                    console.print_exception()
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                            )
            elif self.__EXTENSION == '.toml':
                try:
                    with open(self.__DB, encoding='utf-8') as toml_file:
                        data = toml.load(toml_file)
                        data.pop(obj)
                    with open(self.__DB, encoding='utf-8', mode='w') as toml_file:
                        toml.dump(data, toml_file)
                        Utils().close_file_delete(toml_file)
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"{obj} key have been removed from the database.\n\n"
                            )
                except KeyError as err:
                    console.print_exception()
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                            )
            elif self.__EXTENSION == '.bytes':
                try:
                    with open(self.__DB, mode="rb") as bytes_file:
                        data = pickle.load(bytes_file)
                        data.pop(obj)
                    with open(self.__DB, mode="wb") as bytes_file:
                        pickle.dump(data, bytes_file)
                        Utils().close_file_delete(bytes_file)
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"{obj} key have been removed from the database.\n\n"
                            )
                except KeyError as err:
                    console.print_exception()
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                            )


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
            if Utils().debug:
                sleep(0.5)
                console.log(f"[DEBUG]: Searching for the key {key} ...")
            try:
                if self.__EXTENSION == ".json":
                    if key is None:
                        with open(self.__DB, mode="r+",
                                  encoding="utf-8") as json_file:
                            data = json.load(json_file) or {}
                            Utils().close_file_delete(json_file)
                            if Utils().debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its type is {type(data)}."
                                )
                            if Utils().logs_enabled:
                                with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                    log_file.write(
                                        f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                        + "========================\n"
                                        + f"{key} key have been obtained from the database and its value is {type(data)}.\n\n"
                                    )
                            return type(data)
                    else:
                        with open(self.__DB, mode="r+",
                                  encoding="utf-8") as json_file:
                            data = json.load(json_file) or {}
                            Utils().close_file_delete(json_file)
                            if Utils().util_split(key, data):
                                if Utils().debug:
                                    sleep(0.5)
                                    console.log(
                                        f"[DEBUG]: {key} was found and its type is {type(data)}"
                                    )
                                if Utils().logs_enabled:
                                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                        log_file.write(
                                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                            + "========================\n"
                                            + f"{key} key have been obtained from the database and its value is {type(data)}.\n\n"
                                        )
                                return type(Utils().util_split(key, data))
                            else:
                                raise KeyError(
                                    f"\"{key}\" Does not exist in the file")
                elif self.__EXTENSION == ".yaml":
                    if key is None:
                        with open(self.__DB, mode='r+',
                                  encoding='utf-8') as yaml_file:
                            data = yaml.safe_load(yaml_file) or {}
                            Utils().close_file_delete(yaml_file)
                            if Utils().debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its type is {type(data)}."
                                )
                            if Utils().logs_enabled:
                                with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                    log_file.write(
                                        f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                        + "========================\n"
                                        + f"{key} key have been obtained from the database and its value is {type(data)}.\n\n"
                                    )
                            return type(data)
                    else:
                        with open(self.__DB, mode='r+',
                                  encoding='utf-8') as yaml_file:
                            data = yaml.safe_load(yaml_file) or {}
                            Utils().close_file_delete(yaml_file)
                            if Utils().util_split(key, data):
                                if Utils().debug:
                                    sleep(0.5)
                                    console.log(
                                        f"[DEBUG]: {key} was found and its type is {type(data)}"
                                    )
                                if Utils().logs_enabled:
                                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                        log_file.write(
                                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                            + "========================\n"
                                            + f"{key} key have been obtained from the database and its value is {type(data)}.\n\n"
                                        )
                                return type(Utils().util_split(key, data))
                            else:
                                raise KeyError(
                                    f"\"{key}\" Does not exist in the file")
                elif self.__EXTENSION == ".toml":
                    if key is None:
                        with open(self.__DB, mode="r+",
                                  encoding="utf-8") as toml_file:
                            data = toml.load(toml_file) or {}
                            Utils().close_file_delete(toml_file)
                            if Utils().debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its type is {type(data)}."
                                )
                            if Utils().logs_enabled:
                                with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                    log_file.write(
                                        f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                        + "========================\n"
                                        + f"{key} key have been obtained from the database and its value is {type(data)}.\n\n"
                                    )
                            return type(data)
                    else:
                        with open(self.__DB, mode="r+",
                                  encoding="utf-8") as toml_file:
                            data = toml.load(toml_file) or {}
                            Utils().close_file_delete(toml_file)
                            if Utils().util_split(key, data):
                                if Utils().debug:
                                    sleep(0.5)
                                    console.log(
                                        f"[DEBUG]: {key} was found and its type is {type(data)}"
                                    )
                                if Utils().logs_enabled:
                                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                        log_file.write(
                                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                            + "========================\n"
                                            + f"{key} key have been obtained from the database and its value is {type(data)}.\n\n"
                                        )
                                return type(Utils().util_split(key, data))
                            else:
                                raise KeyError(
                                    f"\"{key}\" Does not exist in the file")
                elif self.__EXTENSION == ".bytes":
                    if key is None:
                        with open(self.__DB, mode="rb") as bytes_file:
                            data = pickle.load(bytes_file)
                            Utils().close_file_delete(bytes_file)
                            if Utils().debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its type is {type(data)}."
                                )
                            if Utils().logs_enabled:
                                with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                    log_file.write(
                                        f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                        + "========================\n"
                                        + f"{key} key have been obtained from the database and its value is {type(data)}.\n\n"
                                    )
                            return type(data)
                    else:
                        with open(self.__DB, mode='rb') as bytes_file:
                            data = pickle.load(bytes_file) or {}
                            Utils().close_file_delete(bytes_file)
                            if Utils().util_split(key, data):
                                if Utils().debug:
                                    sleep(0.5)
                                    console.log(
                                        f"[DEBUG]: {key} was found and its type is {type(data)}"
                                    )
                                if Utils().logs_enabled:
                                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                                        log_file.write(
                                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                            + "========================\n"
                                            + f"{key} key have been obtained from the database and its value is {type(data)}.\n\n"
                                        )
                                return type(Utils().util_split(key, data))
                            else:
                                raise KeyError(
                                    f"\"{key}\" Does not exist in the file")
            except Exception as err:
                console.print_exception()
                if Utils().logs_enabled:
                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                        log_file.write(
                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                            + "========================\n"
                            + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                        )

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

        if Utils().debug:
            sleep(0.5)
            console.log(
                f"[DEBUG]: Trying to get the key {key} from the database ...")
        try:
            if self.__EXTENSION == ".json":
                if key is None:
                    with open(self.__DB, mode="r+",
                              encoding="utf-8") as json_file:
                        data = json.load(json_file) or {}
                        Utils().close_file_delete(json_file)
                        if Utils().debug:
                            sleep(0.5)
                            console.log(f"[DEBUG]: {key} was found.")
                        return data
                else:
                    with open(self.__DB, mode="r+",
                              encoding="utf-8") as json_file:
                        data = json.load(json_file) or {}
                        Utils().close_file_delete(json_file)
                        if Utils().util_split(key, data):
                            if Utils().debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its value is {Utils().util_split(key, data)}."
                                )
                            return Utils().util_split(key, data)
                        else:
                            raise KeyError(
                                f"\"{key}\" Does not exist in the file")
            elif self.__EXTENSION == ".yaml":
                if key is None:
                    with open(self.__DB, mode='r+',
                              encoding='utf-8') as yaml_file:
                        data = yaml.safe_load(yaml_file) or {}
                        Utils().close_file_delete(yaml_file)
                        if Utils().debug:
                            sleep(0.5)
                            console.log(f"[DEBUG]: {key} was found.")
                        return data
                else:
                    with open(self.__DB, mode='r+',
                              encoding='utf-8') as yaml_file:
                        data = yaml.safe_load(yaml_file) or {}
                        Utils().close_file_delete(yaml_file)
                        if Utils().util_split(key, data):
                            if Utils().debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its value is {Utils().util_split(key, data)}."
                                )
                            return Utils().util_split(key, data)
                        else:
                            raise KeyError(
                                f"\"{key}\" Does not exist in the file")
            elif self.__EXTENSION == ".toml":
                if key is None:
                    with open(self.__DB, mode="r+",
                              encoding="utf-8") as toml_file:
                        data = toml.load(toml_file) or {}
                        Utils().close_file_delete(toml_file)
                        if Utils().debug:
                            sleep(0.5)
                            console.log(f"[DEBUG]: {key} was found.")
                        return data
                else:
                    with open(self.__DB, mode="r+",
                              encoding="utf-8") as toml_file:
                        data = toml.load(toml_file) or {}
                        Utils().close_file_delete(toml_file)
                        if Utils().util_split(key, data):
                            if Utils().debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its value is {Utils().util_split(key, data)}."
                                )
                            return Utils().util_split(key, data)
                        else:
                            raise KeyError(
                                f"\"{key}\" Does not exist in the file")
            elif self.__EXTENSION == ".bytes":
                if key is None:
                    with open(self.__DB, mode="rb") as bytes_file:
                        data = pickle.load(bytes_file)
                        Utils().close_file_delete(bytes_file)
                        if Utils().debug:
                            sleep(0.5)
                            console.log(f"[DEBUG]: {key} was found.")
                        return data
                else:
                    with open(self.__DB, mode='rb') as bytes_file:
                        data = pickle.load(bytes_file) or {}
                        Utils().close_file_delete(bytes_file)
                        if Utils().util_split(key, data):
                            if Utils().debug:
                                sleep(0.5)
                                console.log(
                                    f"[DEBUG]: {key} was found and its value is {Utils().util_split(key, data)}."
                                )
                            return Utils().util_split(key, data)
                        else:
                            raise KeyError(
                                f"\"{key}\" Does not exist in the file")
        except Exception as err:
            console.print_exception()
            if Utils().logs_enabled:
                with open(f"{Utils().current_logs()}", mode="a") as log_file:
                    log_file.write(
                        f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                        + "========================\n"
                        + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                    )

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
            if Utils().debug:
                sleep(0.5)
                console.log(
                    f"[DEBUG]: Trying to insert {content} in {'write' if mode == 'w' else 'append'} mode inside the database ..."
                )
            if self.__EXTENSION == '.json':
                try:
                    if mode == "w":
                        with open(self.__DB, encoding='utf-8') as json_file:
                            data = json.load(json_file)
                            data.update(content)
                        with open(self.__DB, encoding='utf-8', mode='w') as json_file:
                            json.dump(data,
                                      json_file,
                                      indent=4,
                                      sort_keys=True)
                            Utils().close_file_delete(json_file)
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
                        with open(self.__DB, encoding='utf-8', mode='w') as json_file:
                            json.dump(data,
                                      json_file,
                                      indent=4,
                                      sort_keys=True)
                            Utils().close_file_delete(json_file)
                    if Utils().debug:
                        sleep(0.5)
                        console.log(
                            "[DEBUG]: The data was successfully inserted inside the database."
                        )
                except Exception as err:
                    console.print_exception()
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                            )
            elif self.__EXTENSION == '.yaml':
                try:
                    if mode == "w":
                        with open(self.__DB, encoding='utf-8') as yaml_file:
                            data = yaml.safe_load(yaml_file)
                            data.update(content)
                        with open(self.__DB, encoding='utf-8', mode='w') as yaml_file:
                            yaml.dump(data, yaml_file, sort_keys=True)
                            Utils().close_file_delete(yaml_file)
                    elif mode == "a":
                        with open(self.__DB, encoding='utf-8') as yaml_file:
                            data = yaml.safe_load(yaml_file)
                            for new_key in content:
                                for original_key in data:
                                    if new_key in original_key:
                                        data[original_key].update(
                                            content[new_key])
                                    else:
                                        data.update(
                                            {new_key: content[new_key]})
                                        break
                        with open(self.__DB, encoding='utf-8', mode='w') as yaml_file:
                            yaml.dump(data, yaml_file, sort_keys=True)
                            Utils().close_file_delete(yaml_file)
                    if Utils().debug:
                        sleep(0.5)
                        console.log(
                            "[DEBUG]: The data was successfully inserted inside the database."
                        )
                except Exception as err:
                    console.print_exception()
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                            )
            elif self.__EXTENSION == '.toml':
                try:
                    if mode == "w":
                        with open(self.__DB, encoding="utf-8") as toml_file:
                            data = toml.load(toml_file) or {}
                            data.update(content)
                        with open(self.__DB, encoding='utf-8', mode="w") as toml_file:
                            toml.dump(data, toml_file)
                            Utils().close_file_delete(toml_file)
                    if mode == "a":
                        with open(self.__DB, encoding="utf-8") as toml_file:
                            data = toml.load(toml_file)
                            for new_key in content:
                                for original_key in data:
                                    if new_key in original_key:
                                        data[original_key].update(
                                            content[new_key])
                                    else:
                                        data.update(
                                            {new_key: content[new_key]})
                                        break
                        with open(self.__DB, encoding='utf-8', mode='w') as toml_file:
                            toml.dump(data, toml_file)
                            Utils().close_file_delete(toml_file)
                    if Utils().debug:
                        sleep(0.5)
                        console.log(
                            "[DEBUG]: The data was successfully inserted inside the database."
                        )
                except Exception as err:
                    console.print_exception()
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                            )
            elif self.__EXTENSION == '.bytes':
                try:
                    if mode == "w":
                        with open(self.__DB, mode="rb") as bytes_file:
                            data = pickle.load(bytes_file) or {}
                            data.update(content)
                        with open(self.__DB, mode="wb") as bytes_file:
                            pickle.dump(data, bytes_file)
                            Utils().close_file_delete(bytes_file)
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
                            Utils().close_file_delete(bytes_file)
                    if Utils().debug:
                        sleep(0.5)
                        console.log(
                            "[DEBUG]: The data was successfully inserted inside the database."
                        )
                except Exception as err:
                    console.print_exception()
                    if Utils().logs_enabled:
                        with open(f"{Utils().current_logs()}", mode="a") as log_file:
                            log_file.write(
                                f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                                + "========================\n"
                                + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                            )

    def push(self, key: str = None, element=None):
        """
        Push a new element to an Array (list) inside the database.

        ...

        Parameters
        ----------
        key : str
            The List to which the data will be pushed.
        element
            The element that'll be pushed to the List.

        Raises
        ------
        TypeError
            If key isn't a String.
        KeyError
            If the given key doesn't exists.
        ValueError
            If the given key isn't a List.
        """

        if type(key) is not str:
            raise TypeError('key must be a String')
        if Utils().debug:
            sleep(0.5)
            console.log(f"[DEBUG]: Trying to push {element} into {key} ...")
        if self.__EXTENSION == ".json":
            try:
                with open(self.__DB, encoding="utf-8") as json_file:
                    data = json.load(json_file)
                    if Utils().util_split(key, data) or Utils().util_split(
                            key, data) is None or Utils().util_split(
                                key, data) == []:
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                f"[DEBUG]: {key} was found. Trying to push ..."
                            )
                        Utils().util_split(key, data).append(element)
                    else:
                        raise KeyError(
                            f"\"{key}\" Does not exist in the file or is not a list"
                        )
                with open(self.__DB, encoding="utf-8", mode="w") as json_file:
                    json.dump(data, json_file, indent=4, sort_keys=True)
                    Utils().close_file_delete(json_file)
            except Exception as err:
                console.print_exception()
                if Utils().logs_enabled:
                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                        log_file.write(
                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                            + "========================\n"
                            + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                        )
        elif self.__EXTENSION == ".yaml":
            try:
                with open(self.__DB, encoding="utf-8") as yaml_file:
                    data = yaml.safe_load(yaml_file)
                    if Utils().util_split(key, data) or Utils().util_split(
                            key, data) is None or Utils().util_split(
                                key, data) == []:
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                f"[DEBUG]: {key} was found. Trying to push ..."
                            )
                        Utils().util_split(key, data).append(element)
                    else:
                        raise KeyError(
                            f"\"{key}\" Does not exist in the file or is not a list"
                        )
                with open(self.__DB, encoding="utf-8", mode="w") as yaml_file:
                    yaml.dump(data, yaml_file, sort_keys=True)
                    Utils().close_file_delete(yaml_file)
            except Exception as err:
                console.print_exception()
                if Utils().logs_enabled:
                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                        log_file.write(
                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                            + "========================\n"
                            + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                        )
        elif self.__EXTENSION == ".toml":
            try:
                with open(self.__DB, encoding="utf-8") as toml_file:
                    data = toml.load(toml_file)
                    if Utils().util_split(key, data) or Utils().util_split(
                            key, data) is None or Utils().util_split(
                                key, data) == []:
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                f"[DEBUG]: {key} was found. Trying to push ..."
                            )
                        Utils().util_split(key, data).append(element)
                    else:
                        raise KeyError(
                            f"\"{key}\" Does not exist in the file or is not a list"
                        )
                with open(self.__DB, encoding="utf-8", mode="w") as toml_file:
                    toml.dump(data, toml_file)
                    Utils().close_file_delete(toml_file)
            except Exception as err:
                console.print_exception()
                if Utils().logs_enabled:
                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                        log_file.write(
                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                            + "========================\n"
                            + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                        )
        elif self.__EXTENSION == ".bytes":
            try:
                with open(self.__DB) as bytes_file:
                    data = pickle.load(bytes_file)
                    if Utils().util_split(key, data) or Utils().util_split(
                            key, data) is None or Utils().util_split(
                                key, data) == []:
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                f"[DEBUG]: {key} was found. Trying to push ..."
                            )
                        Utils().util_split(key, data).append(element)
                    else:
                        raise KeyError(
                            f"\"{key}\" Does not exist in the file or is not a list"
                        )
                with open(self.__DB, mode="wb") as bytes_file:
                    pickle.dump(data, bytes_file)
                    Utils().close_file_delete(bytes_file)
            except Exception as err:
                console.print_exception()
                if Utils().logs_enabled:
                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                        log_file.write(
                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                            + "========================\n"
                            + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                        )

    def update(self, key: str = None, new_value=None):
        """
        Update the value of a key inside the database.

        ...

        Parameters
        ----------
        key : str
            The key that'll be updated.
        new_value
            The new value of the key.

        Raises
        ------
        TypeError
            If key isn't a String.
        KeyError
            If the given key doesn't exists.
        """

        if type(key) is not str:
            raise TypeError('key must be a String')
        if Utils().debug:
            sleep(0.5)
            console.log(f"[DEBUG]: Trying to change the value of {key} ...")
        if self.__EXTENSION == ".json":
            try:
                with open(self.__DB, encoding="utf-8") as json_file:
                    data = json.load(json_file)
                    if Utils().util_split(key, data):
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                f"[DEBUG]: {key} was found. Trying to set the new value ..."
                            )
                        obj = Utils().util_split(key, data)
                        obj = new_value
                    else:
                        raise KeyError(
                            f"\"{key}\" Does not exist in the file.")
                with open(self.__DB, encoding="utf-8", mode="w") as json_file:
                    json.dump(data, json_file, indent=4, sort_keys=True)
                    Utils().close_file_delete(json_file)
            except Exception as err:
                console.print_exception()
                if Utils().logs_enabled:
                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                        log_file.write(
                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                            + "========================\n"
                            + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                        )
        elif self.__EXTENSION == ".yaml":
            try:
                with open(self.__DB, encoding="utf-8") as yaml_file:
                    data = yaml.safe_load(yaml_file)
                    if Utils().util_split(key, data):
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                f"[DEBUG]: {key} was found. Trying to set the new value ..."
                            )
                        obj = Utils().util_split(key, data)
                        obj = new_value
                with open(self.__DB, encoding="utf-8", mode="w") as yaml_file:
                    yaml.dump(data, yaml_file, sort_keys=True)
                    Utils().close_file_delete(yaml_file)
            except Exception as err:
                console.print_exception()
                if Utils().logs_enabled:
                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                        log_file.write(
                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                            + "========================\n"
                            + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                        )
        elif self.__EXTENSION == ".toml":
            try:
                with open(self.__DB, encoding="utf-8") as toml_file:
                    data = toml.load(toml_file)
                    if Utils().util_split(key, data):
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                f"[DEBUG]: {key} was found. Trying to set the new value ..."
                            )
                        obj = Utils().util_split(key, data)
                        obj = new_value
                    else:
                        raise KeyError(
                            f"\"{key}\" Does not exist in the file.")
                with open(self.__DB, encoding="utf-8", mode="w") as toml_file:
                    toml.dump(data, toml_file)
                    Utils().close_file_delete(toml_file)
            except Exception as err:
                console.print_exception()
                if Utils().logs_enabled:
                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                        log_file.write(
                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                            + "========================\n"
                            + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                        )
        elif self.__EXTENSION == ".bytes":
            try:
                with open(self.__DB, mode="rb") as bytes_file:
                    data = pickle.load(bytes_file)
                    if Utils().util_split(key, data):
                        if Utils().debug:
                            sleep(0.5)
                            console.log(
                                f"[DEBUG]: {key} was found. Trying to set the new value ..."
                            )
                        obj = Utils().util_split(key, data)
                        obj = new_value
                with open(self.__DB, mode="wb") as bytes_file:
                    pickle.dump(data, bytes_file)
                    Utils().close_file_delete(bytes_file)
            except Exception as err:
                console.print_exception()
                if Utils().logs_enabled:
                    with open(f"{Utils().current_logs()}", mode="a") as log_file:
                        log_file.write(
                            f"\033[1m{datetime.datetime.utcnow().strftime('%c')}\033[0m\n"
                            + "========================\n"
                            + f"\033[0;31mAn error has occurred.\n{err}\033[0m\n\n"
                        )
