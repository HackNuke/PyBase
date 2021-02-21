# Benchmark tests

After v1.0.0.dev5 we are using [pytest-benchmark](https://github.com/ionelmc/pytest-benchmark) to do
our main benchmark testing because of all the functionality it provides.

If you can work with make, we recommend to you to run the benchmark tests from our Makefile (`make benchmark`).

---

## Alternative benchmark, aka Stress test

Instructions to do a _good_ stress test in PyBase:

- See the [generateBigJson.sh](./generateBigJson.sh) file and read the comments on it.
- Create a `bench_stress.py` file with the following structure and run it.

### bench_stress structure

```python
import time

# We will need to do a timer decorator like this one
def timer_func(func):
    def function_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{func}\ttook {time} seconds to complete its execution.\n"
        print(msg.format(func=func.__name__, time=round(runtime, 3)))
        return value

    return function_timer

# Then we will also need to do our functions with our timer decorator
@timer_func
def creating():
    PyBase(database="bench_stress", db_type="json")

# And finally, run our functions to see the results
creating()
```

---

## Results

The most recent results (using v1.0.0dev5) from a Benchmark test.

> Note: you can see the code used for this benchmark test in [test_benchmark.py](./test_benchmark.py)

```
----------------------------------------------------------------------------------- benchmark: 10 tests ------------------------------------------------------------------------------------
Name (time in ms)                 Min                Max              Mean            StdDev            Median               IQR            Outliers       OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_fetch                     2.7442 (1.0)       2.9323 (1.02)     2.8253 (1.00)     0.0761 (inf)      2.7897 (1.00)     0.1128 (inf)           2;0  353.9487 (1.00)          5         100
test_db_creation               2.7519 (1.00)      2.9266 (1.02)     2.8126 (1.0)      0.0706 (inf)      2.7803 (1.0)      0.0911 (inf)           1;0  355.5483 (1.0)           5         100
test_get_one                   2.7635 (1.01)      2.8698 (1.0)      2.8135 (1.00)     0.0385 (inf)      2.8137 (1.01)     0.0425 (inf)           2;0  355.4313 (1.00)          5         100
test_get_all                   2.7815 (1.01)      2.9127 (1.01)     2.8363 (1.01)     0.0501 (inf)      2.8285 (1.02)     0.0668 (inf)           2;0  352.5685 (0.99)          5         100
test_rename                    2.8621 (1.04)      2.9983 (1.04)     2.9313 (1.04)     0.0574 (inf)      2.9267 (1.05)     0.0998 (inf)           2;0  341.1452 (0.96)          5         100
test_insertion_append_mode     3.0786 (1.12)     23.8960 (8.33)     7.9006 (2.81)     9.0508 (inf)      3.1086 (1.12)     7.6320 (inf)           1;1  126.5725 (0.36)          5         100
test_insertion_write_mode      3.2113 (1.17)      7.2668 (2.53)     4.0357 (1.43)     1.8063 (inf)      3.2348 (1.16)     1.0293 (inf)           1;1  247.7859 (0.70)          5         100
test_push                      3.2200 (1.17)     14.2455 (4.96)     6.9626 (2.48)     4.4411 (inf)      6.8136 (2.45)     5.3698 (inf)           1;0  143.6243 (0.40)          5         100
test_delete                    3.4403 (1.25)      3.4403 (1.20)     3.4403 (1.22)     0.0000 (1.0)      3.4403 (1.24)     0.0000 (1.0)           0;0  290.6695 (0.82)          1           1
test_update                    3.5921 (1.31)     12.6126 (4.39)     5.4401 (1.93)     4.0101 (inf)      3.6484 (1.31)     2.3743 (inf)           1;1  183.8201 (0.52)          5         100
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
