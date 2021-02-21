# Benchmark tests - PyBase v1.0.0
# Latest benchmark: v1.0.0.dev5

import time
import pytest

from pybase_db.pybase_db import PyBase


def db_creation():
    PyBase(database="bench", db_type="json")


def insertion_write_mode():
    # Special thanks to Velikaz per the example json
    # provided for doing the benchmark test ♥
    #
    # NOTE: this is the insert in mode write,
    #       below is the insert in append mode.
    objects = {
        "703482970077659197": {
            "canal": "732673349779718248",
            "title": "Dirttooo",
            "desc": "Bienvendo a {server}",
            "desccolor": "#00f9ff",
            "titlecolor": "#00f9ff",
            "mcolor": "#00ffd5",
            "gcanal": "721520429726040145",
            "gfondo":
            "https://cdn.discordapp.com/attachments/721520429726040145/721891962676052098/unknown.png",
            "datos": {
                "rolb": "729110021282988092"
            },
            "gtitle": "asdads",
            "msgw": "sasadsadsad",
            "rcolor": "#42ff00",
            "ucolor": "#ffffff",
            "rol": "729141832029700126"
        },
        "716465688377557023": {
            "fondo":
            "https://cdn.discordapp.com/attachments/716468290851176489/721948154152615987/unknown.png",
            "titulo": "",
            "mensaje": "",
            "color": "",
            "rol": "735273493050032148",
            "canal": "733072755112542329",
            "gcanal": "716468290851176489",
            "gfondo":
            "https://cdn.discordapp.com/attachments/721520429726040145/721891962676052098/unknown.png",
            "title": "¡Bienvenid@!",
            "msgw": "holasdasd"
        },
        "721501732043096126": {
            "fondo":
            "https://cdn.discordapp.com/attachments/721506140575498240/721968560972234812/2Q.png",
            "msgw":
            "Cayo {user} ¡¡¡Que onda Master!!! Te damos la bienvenida a {server} Esperamos que la pases recontra bien",
            "desc": "Bienvenido capo",
            "canal": "721506140575498240",
            "mcolor": "#a338ff"
        },
        "222864538716864513": {
            "gfondo":
            "https://vignette.wikia.nocookie.net/kakegurui/images/9/91/YumemiOnstage.jpg/revision/latest?cb=20190328191626",
            "canal": "383828356849991682",
            "gcanal": "222906506541137930",
            "gmcolor": "#FF0000",
            "desccolor": "#00C0C0"
        },
        "616396960349421568": {
            "canal": "721992401232855080"
        },
        "723191976693858345": {
            "canal":
            "723191976693858348",
            "fondo":
            "https://cdn.discordapp.com/attachments/721506140575498240/721968560972234812/2Q.png"
        },
        "415346195544801291": {
            "canal": "674509574618873896"
        },
        "739864270803828840": {
            "canal": "740221252333076591",
            "fondo":
            "https://www.valuehost.com.br/blog/wp-content/uploads/2015/03/servers.jpg",
            "desc": "Hosting & VPS",
            "msgw": "¡Nuevo miembro en SigloHost!",
            "gcanal": "740021948918136844"
        },
        "737185866652319755": {
            "canal": "741447943256801290",
            "title": "Awoo",
            "fondo":
            "https://cdn.discordapp.com/attachments/741447943256801290/742080136370716682/argentina.png",
            "msgw": "Hi",
            "desc": "{server}",
            "owner": []
        },
        "740358198497640619": {
            "rol": "741730087719927848",
            "canal": "743111862190866443"
        },
        "770376448342753320": {
            "canal": "770376448342753324",
            "fondo":
            "https://cdn.discordapp.com/attachments/770376448342753324/770380362814586900/unknown.png",
            "title": "Centauri",
            "gcanal": "770376448342753324"
        }
    }

    db = PyBase(database="bench", db_type="json")
    db.insert(content=objects, mode="w")


def insertion_append_mode():
    db = PyBase(database="bench", db_type="json")
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


def delete():
    db = PyBase(database="bench", db_type="json")
    db.delete("770376448342753320")


def fetch():
    db = PyBase(database="bench", db_type="json")
    db.fetch("737185866652319755.title")


def get_one():
    db = PyBase(database="bench", db_type="json")
    db.get("737185866652319755")


def get_all():
    db = PyBase(database="bench", db_type="json")
    db.get()


def push():
    db = PyBase(database="bench", db_type="json")
    db.push(key="737185866652319755.owner", element="Unknown")


def update():
    db = PyBase(database="bench", db_type="json")
    db.update(key="737185866652319755.title", new_value="New amazing title!")


def rename():
    db = PyBase(database="bench", db_type="json")
    db.rename(key="737185866652319755.title", new_name="guild_title")


### RUN BENCHMARK
def test_db_creation(benchmark):
    benchmark(db_creation)


def test_insertion_write_mode(benchmark):
    benchmark(insertion_write_mode)


def test_insertion_append_mode(benchmark):
    benchmark(insertion_append_mode)


def test_delete(benchmark):
    # Just one iteration or will fail
    benchmark.pedantic(delete, iterations=1)


def test_fetch(benchmark):
    benchmark(fetch)


def test_get_one(benchmark):
    benchmark(get_one)


def test_get_all(benchmark):
    benchmark(get_all)


def test_push(benchmark):
    benchmark(push)


def test_update(benchmark):
    benchmark(update)


def test_rename(benchmark):
    benchmark(rename)
