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

The most recent results (using v1.0.0dev6) from a Benchmark test.

> Note: you can see the code used for this benchmark test in [test_benchmark.py](./test_benchmark.py)

```
------------------------------------------------------------------------------------- benchmark: 10 tests -------------------------------------------------------------------------------------
Name (time in ms)                 Min                Max               Mean             StdDev            Median                IQR            Outliers       OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_db_creation               2.6175 (1.0)       2.6808 (1.0)       2.6482 (1.0)       0.0292 (inf)      2.6438 (1.0)       0.0553 (inf)           2;0  377.6082 (1.0)           5         100
test_get_all                   2.6593 (1.02)      2.7053 (1.01)      2.6873 (1.01)      0.0228 (inf)      2.7018 (1.02)      0.0407 (inf)           1;0  372.1143 (0.99)          5         100
test_get_one                   2.6635 (1.02)      2.7286 (1.02)      2.7003 (1.02)      0.0248 (inf)      2.7080 (1.02)      0.0331 (inf)           2;0  370.3271 (0.98)          5         100
test_fetch                     2.7069 (1.03)      2.7752 (1.04)      2.7390 (1.03)      0.0317 (inf)      2.7308 (1.03)      0.0597 (inf)           2;0  365.0968 (0.97)          5         100
test_rename                    2.7777 (1.06)      2.8561 (1.07)      2.8152 (1.06)      0.0304 (inf)      2.8102 (1.06)      0.0454 (inf)           2;0  355.2170 (0.94)          5         100
test_update                    2.8282 (1.08)      3.3557 (1.25)      3.0942 (1.17)      0.2024 (inf)      3.0386 (1.15)      0.2811 (inf)           2;0  323.1875 (0.86)          5         100
test_insertion_write_mode      2.9862 (1.14)      3.1327 (1.17)      3.0634 (1.16)      0.0613 (inf)      3.0555 (1.16)      0.1046 (inf)           2;0  326.4370 (0.86)          5         100
test_insertion_append_mode     3.0196 (1.15)     32.6754 (12.19)    12.0666 (4.56)     13.2899 (inf)      3.1640 (1.20)     18.8930 (inf)           1;0   82.8733 (0.22)          5         100
test_delete                    3.1785 (1.21)      3.1785 (1.19)      3.1785 (1.20)      0.0000 (1.0)      3.1785 (1.20)      0.0000 (1.0)           0;0  314.6104 (0.83)          1           1
test_push                      3.3652 (1.29)     12.5492 (4.68)      6.5659 (2.48)      3.9559 (inf)      4.7048 (1.78)      6.0703 (inf)           1;0  152.3030 (0.40)          5         100
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

- Legend:
  - Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  - OPS: Operations Per Second, computed as 1 / Mean
  - See more in [glossary](https://pytest-benchmark.readthedocs.io/en/stable/glossary.html)
