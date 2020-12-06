# PyBase – Manager for NoSQL and SQL databases.
#==============================================#
# PyBase is distributed under MIT License.     #

import datetime
import json
import math
import os
import pathlib
import threading
from time import sleep

import psutil
import toml
import yaml
from rich.console import Console
from rich.traceback import install

install() # Use Rich traceback handler as the default error handler
console = Console()


class Utils:
    """
    PyBase main utilities class

    ...

    Attributes
    ----------

    Methods
    -------
    search_config
        Search for a PyBase's configuration file.
    """

    # Default configuration.
    # It'll be used if there's no configuration file.
    debug = False
    stats_enabled = False
    stats_interval = "2m"
    logs_enabled = True
    logs_location = "./tmp"
    logs_life_cycle = "7d"

    @classmethod
    def search_config(cls):
        files = [f for f in os.listdir(pathlib.Path().absolute()) if os.path.isfile(f)]

        for dir_file in files:
            if dir_file == "pybase.json":
                with open(dir_file, encoding="utf-8", mode="r") as config_file:
                    config = json.load(config_file)

                    if "debugging" in config:
                        if "enabled" in config["debugging"]:
                            if isinstance(config["debugging"]["enabled"], bool):
                                cls.debug = config["debugging"]["enabled"]
                            else:
                                raise TypeError(
                                    'enabled must be a Boolean in the debugging key inside config file.'
                                )
                        else:
                            cls.debug = False
                        if "stats" in config["debugging"]:
                            if isinstance(config["debugging"]["stats"], dict):
                                if "enabled" in config["debugging"]["stats"]:
                                    if isinstance(config["debugging"]["stats"]["enabled"], bool):
                                        cls.stats_enabled = config["debugging"]["stats"]["enabled"]
                                    else:
                                        raise TypeError(
                                            'enabled must be a Boolean in the stats key inside the debugging key of the config file.'
                                        )
                                else:
                                    cls.stats_enabled = False
                                if "interval" in config["debugging"]["stats"]:
                                    if isinstance(config["debugging"]["stats"]["interval"], str):
                                        cls.stats_interval = config["debugging"]["stats"]["interval"]
                                    else:
                                        raise TypeError(
                                            'interval must be a String in the stats key inside the debugging key of the config file.'
                                        )
                                else:
                                    cls.stats_interval = "2m"
                            else:
                                raise TypeError(
                                    'stats must be a dictionary in the debugging key inside config file.'
                                )
                        else:
                            cls.stats_enabled = False
                            cls.stats_interval = "2m"
                    else:
                        if "debug" in config:
                            raise KeyError(
                                'debug must be inside the debugging key in the config file.'
                            )
                        elif "stats" in config:
                            raise KeyError(
                                'stats must be inside the debugging key in the config file.'
                            )

                    if "logs" in config:
                        if "enabled" in config["logs"]:
                            if isinstance(config["logs"]["enabled"], bool):
                                cls.logs_enabled = config["logs"]["enabled"]
                            else:
                                raise KeyError(
                                    'enabled must be a Boolean in the logs key inside config file.'
                                )
                        else:
                            cls.logs_enabled = True
                        if "location" in config["logs"]:
                            if isinstance(config["logs"]["location"], str):
                                cls.logs_location = config["logs"]["location"]
                            else:
                                raise KeyError(
                                    'location must be a String in the logs key inside the config file.'
                                )
                        else:
                            cls.logs_location = pathlib.Path().absolute() + "/tmp"
                        if "life_cycle" in config["logs"]:
                            if isinstance(config["logs"]["life_cycle"], str):
                                cls.logs_life_cycle = config["logs"]["life_cycle"]
                            else:
                                raise KeyError(
                                    'life_cycle must be a String in the logs key inside the config file.'
                                )
                        else:
                            cls.logs_life_cycle = "7d"
                    else:
                        if "enabled" in config:
                            raise KeyError(
                                'enabled must be inside the debugging or logs key in the config file.'
                            )
                        elif "interval" in config:
                            raise KeyError(
                                'interval must be inside the stats key in the debugging key of the config file.'
                            )
                        elif "location" in config:
                            raise KeyError(
                                'location must be inside the logs key in the config file.'
                            )
                        elif "life_cycle" in config:
                            raise KeyError(
                                'life_cycle must be inside the logs key in the config file.'
                            )
            elif dir_file == "pybase.yaml" or dir_file == "pybase.yml":
                with open(dir_file, encoding="utf-8", mode="r") as config_file:
                    config = yaml.safe_load(config_file)

                    if "debugging" in config:
                        if "enabled" in config["debugging"]:
                            if isinstance(config["debugging"]["enabled"], bool):
                                cls.debug = config["debugging"]["enabled"]
                            else:
                                raise TypeError(
                                    'enabled must be a Boolean in the debugging key inside config file.'
                                )
                        else:
                            cls.debug = False
                        if "stats" in config["debugging"]:
                            if isinstance(config["debugging"]["stats"], dict):
                                if "enabled" in config["debugging"]["stats"]:
                                    if isinstance(config["debugging"]["stats"]["enabled"], bool):
                                        cls.stats_enabled = config["debugging"]["stats"]["enabled"]
                                    else:
                                        raise TypeError(
                                            'enabled must be a Boolean in the stats key inside the debugging key of the config file.'
                                        )
                                else:
                                    cls.stats_enabled = False
                                if "interval" in config["debugging"]["stats"]:
                                    if isinstance(config["debugging"]["stats"]["interval"], str):
                                        cls.stats_interval = config["debugging"]["stats"]["interval"]
                                    else:
                                        raise TypeError(
                                            'interval must be a String in the stats key inside the debugging key of the config file.'
                                        )
                                else:
                                    cls.stats_interval = "2m"
                            else:
                                raise TypeError(
                                    'stats must be a dictionary in the debugging key inside config file.'
                                )
                        else:
                            cls.stats_enabled = False
                            cls.stats_interval = "2m"
                    else:
                        if "debug" in config:
                            raise KeyError(
                                'debug must be inside the debugging key in the config file.'
                            )
                        elif "stats" in config:
                            raise KeyError(
                                'stats must be inside the debugging key in the config file.'
                            )

                    if "logs" in config:
                        if "enabled" in config["logs"]:
                            if isinstance(config["logs"]["enabled"], bool):
                                cls.logs_enabled = config["logs"]["enabled"]
                            else:
                                raise KeyError(
                                    'enabled must be a Boolean in the logs key inside config file.'
                                )
                        else:
                            cls.logs_enabled = True
                        if "location" in config["logs"]:
                            if isinstance(config["logs"]["location"], str):
                                cls.logs_location = config["logs"]["location"]
                            else:
                                raise KeyError(
                                    'location must be a String in the logs key inside the config file.'
                                )
                        else:
                            cls.logs_location = pathlib.Path().absolute() + "/tmp"
                        if "life_cycle" in config["logs"]:
                            if isinstance(config["logs"]["life_cycle"], str):
                                cls.logs_life_cycle = config["logs"]["life_cycle"]
                            else:
                                raise KeyError(
                                    'life_cycle must be a String in the logs key inside the config file.'
                                )
                        else:
                            cls.logs_life_cycle = "7d"
                    else:
                        if "enabled" in config:
                            raise KeyError(
                                'enabled must be inside the debugging or logs key in the config file.'
                            )
                        elif "interval" in config:
                            raise KeyError(
                                'interval must be inside the stats key in the debugging key of the config file.'
                            )
                        elif "location" in config:
                            raise KeyError(
                                'location must be inside the logs key in the config file.'
                            )
                        elif "life_cycle" in config:
                            raise KeyError(
                                'life_cycle must be inside the logs key in the config file.'
                            )
            elif dir_file == "pybase.toml":
                with open(dir_file, encoding="utf-8", mode="r") as config_file:
                    config = toml.load(config_file)

                    if "debugging" in config:
                        if "enabled" in config["debugging"]:
                            if isinstance(config["debugging"]["enabled"], bool):
                                cls.debug = config["debugging"]["enabled"]
                            else:
                                raise TypeError(
                                    'enabled must be a Boolean in the debugging key inside config file.'
                                )
                        else:
                            cls.debug = False
                        if "stats" in config["debugging"]:
                            if isinstance(config["debugging"]["stats"], dict):
                                if "enabled" in config["debugging"]["stats"]:
                                    if isinstance(config["debugging"]["stats"]["enabled"], bool):
                                        cls.stats_enabled = config["debugging"]["stats"]["enabled"]
                                    else:
                                        raise TypeError(
                                            'enabled must be a Boolean in the stats key inside the debugging key of the config file.'
                                        )
                                else:
                                    cls.stats_enabled = False
                                if "interval" in config["debugging"]["stats"]:
                                    if isinstance(config["debugging"]["stats"]["interval"], str):
                                        cls.stats_interval = config["debugging"]["stats"]["interval"]
                                    else:
                                        raise TypeError(
                                            'interval must be a String in the stats key inside the debugging key of the config file.'
                                        )
                                else:
                                    cls.stats_interval = "2m"
                            else:
                                raise TypeError(
                                    'stats must be a dictionary in the debugging key inside config file.'
                                )
                        else:
                            cls.stats_enabled = False
                            cls.stats_interval = "2m"
                    else:
                        if "debug" in config:
                            raise KeyError(
                                'debug must be inside the debugging key in the config file.'
                            )
                        elif "stats" in config:
                            raise KeyError(
                                'stats must be inside the debugging key in the config file.'
                            )

                    if "logs" in config:
                        if "enabled" in config["logs"]:
                            if isinstance(config["logs"]["enabled"], bool):
                                cls.logs_enabled = config["logs"]["enabled"]
                            else:
                                raise KeyError(
                                    'enabled must be a Boolean in the logs key inside config file.'
                                )
                        else:
                            cls.logs_enabled = True
                        if "location" in config["logs"]:
                            if isinstance(config["logs"]["location"], str):
                                cls.logs_location = config["logs"]["location"]
                            else:
                                raise KeyError(
                                    'location must be a String in the logs key inside the config file.'
                                )
                        else:
                            cls.logs_location = pathlib.Path().absolute() + "/tmp"
                        if "life_cycle" in config["logs"]:
                            if isinstance(config["logs"]["life_cycle"], str):
                                cls.logs_life_cycle = config["logs"]["life_cycle"]
                            else:
                                raise KeyError(
                                    'life_cycle must be a String in the logs key inside the config file.'
                                )
                        else:
                            cls.logs_life_cycle = "7d"
                    else:
                        if "enabled" in config:
                            raise KeyError(
                                'enabled must be inside the debugging or logs key in the config file.'
                            )
                        elif "interval" in config:
                            raise KeyError(
                                'interval must be inside the stats key in the debugging key of the config file.'
                            )
                        elif "location" in config:
                            raise KeyError(
                                'location must be inside the logs key in the config file.'
                            )
                        elif "life_cycle" in config:
                            raise KeyError(
                                'life_cycle must be inside the logs key in the config file.'
                            )

    def close_file_delete(self, file):
        """
        Method for close the open file and erase it from memory (slightly better performance)
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

    def util_split(self, key: str, data: dict):
        """
        Method for split dict from key specific
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

    def util_split_delete(self, key: str, data: dict):
        """
        Method for split dict from key specific and then delete the key.
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
                del dataObject[keys]
            else:
                dataObject = dataObject[keys]
        return dataObject

    def send_stats(self):
        """
        Method for send statistics of usage.
        """

        pybase_process = psutil.Process(os.getpid())  # Get PyBase process ID
        pybase_cpu_usage = pybase_process.cpu_percent(
            interval=1.0) # CPU Usage in percentage
        pybase_ram_usage = round(pybase_process.memory_percent(),
                                 1) # Memory usage in percentage
        console.log(f"""[DEBUG]: Showing PyBase Usage statistics ...
         CPU Usage: {pybase_cpu_usage}%
         RAM Usage: {pybase_ram_usage}%""")

    def current_logs(self):
        """
        Method for search the log file based on the logs life cycle.
        """

        for logs in os.listdir(os.path.abspath(self.logs_location)):
            if (datetime.datetime.utcnow() - datetime.datetime.fromtimestamp(os.path.getctime(os.path.abspath(self.logs_location) + "/" + logs))).seconds <= self.time_to_seconds(self.logs_life_cycle):
                return f"{os.path.abspath(self.logs_location)}/{logs}"


    def delete_old_logs(self):
        """
        Method for delete log files that are 7 days or more old.
        """

        if self.debug:
            sleep(0.5)
            console.log("[DEBUG]: Searching for old log files ...")
        for logs in os.listdir(os.path.abspath(self.logs_location)):
            if (datetime.datetime.utcnow() - datetime.datetime.fromtimestamp(os.path.getctime(os.path.abspath(self.logs_location) + "/" + logs))).seconds >= self.time_to_seconds(self.logs_life_cycle):
                if self.debug:
                    sleep(0.5)
                    console.log(f"[DEBUG]: Deleting old log file {logs} ...")
                try:
                    os.remove(os.path.abspath(self.logs_location) + "/" + logs)
                except Exception:
                    console.print_exception()

    def interval(self, func, sec):
        def func_wrapper():
            self.interval(func, sec)
            func()

        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    def time_to_seconds(self, time):
        secs = 1
        mins = secs * 60
        hours = mins * 60
        days = hours * 24
        weeks = days * 7

        if "w" in time:
            time = int(time.replace("w", "")) if "." not in time else float(time.replace("w", ""))
            return time * weeks
        elif "d" in time:
            time = int(time.replace("d", "")) if "." not in time else float(time.replace("d", ""))
            return time * days
        elif "h" in time:
            time = int(time.replace("h", "")) if "." not in time else float(time.replace("h", ""))
            return time * hours
        elif "m" in time:
            time = int(time.replace("m", "")) if "." not in time else float(time.replace("m", ""))
            return time * mins
