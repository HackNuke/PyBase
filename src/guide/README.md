# Introduction

![Undraw Analysis](../static/img/undraw_Analysis_re_w2vd.png)

Here you will find information about PyBase, how to install
and integrate it with your different projects.

::: warning
In this guide we use and recommend using the current
development version (1.0.0.dev1) of PyBase.
:::

## What is PyBase?
PyBase is a DataBase Manager for multiple filetypes including SQLite3.

It's focused on the ease and effectiveness for the administration of databases.

## Why you should use PyBase?
**If you want to store static data** (JSON, YAML, TOML, Bytes) **or store a database
in SQLite3, the best thing would be to use an administrator that simplifies your
tasks and helps you with a good organization and efficiently.**

PyBase does exactly that, allows you to create such databases with just one method,
and simplifies the task of manipulating __their__ data!

### Features
To write ...

#### Benchmark
PyBase is made to be fast, and what better proof than a benchmarking test?

::: tip Benchmark source
You can see the code used for the test in [tests](https://github.com/PyBase/PyBase/blob/development/tests/benchmark.py)
:::

```
creating        took 0.002 seconds to complete its execution.

insert_1        took 0.004 seconds to complete its execution.

insert_2        took 0.004 seconds to complete its execution.

deleting        took 0.008 seconds to complete its execution.

fetching        took 0.003 seconds to complete its execution.

getting_one     took 0.003 seconds to complete its execution.

getting_all     took 0.003 seconds to complete its execution.

pushing_1       took 0.005 seconds to complete its execution.

updating        took 0.004 seconds to complete its execution.
```
