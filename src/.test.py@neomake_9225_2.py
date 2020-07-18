#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pysql import PySQL

########

db = PySQL(database = "prueba", debug = False)
db.create(objects = {
    "table": {
        "name": "prueba",
        "elements": {
            "test": {
                "type": "text",
                "value": ["a", "b", "c"]
            }, 
            "prueba": {
                "type": "integer", 
                "value": 12345
            },
        }
    }
})

db.delete(table = "prueba")
