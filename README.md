# easytest

## Extremely simple Python unit testing

Stemmed from a need to quickly test a single function multiple times, this one-file script adds easy unit testing to functions.

---

## Requirements

- [`colorama`](https://pypi.org/project/colorama/) package

---

## Usage

1. Ensure [Git is installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your computer. Open up a terminal, and type `git clone https://github.com/TriG-Tbh/easytest.git` to download the files.

   Once they're downloaded, type `cd easytest` to enter the folder they were installed to.

   Type `pip install -r requirements.txt` to install the required modules.

2. Copy `easytest.py` into the folder containing your code, and add

   ```python
   import easytest
   ```

   to the beginning of the file containing the functions you need to test.

3. For each function you want to test, add right before the declaration line:

   ```python
   @easytest.test(params=["list of parameters"], stdin="inputted string", stdout="outputted string", return_val=value_to_return)
   ```

   `params`: if your function needs data passed as parameters, pass them through this parameter as a list. If parameters are manually set (i.e. `x=5`), add those parameters to the end of the list (using the same example, `[..., 5]`), in the same order that they appear in the definition line

   `stdin`: if your function gets input through `input()`, set that input through this parameter. This defaults to `""`.

   `stdout`: if you need to check printed ouput, set the desired output through this paramter. This defaults to `""`.

   `return_val`: if your function returns a value, set the expected return value through this parameter. This defaults to `None`.

   A test **must** have either `stdout` or `return_val` defined in order for it to work.

4. If you want to add linebreaks between sections of code, add:

   ```python
   easytest.linebreak()
   ```

   between them.

5. Once all of your tests have been set, at the very end of your file, add:

   ```python
   easytest.render(time_limit=time)
   ```

   to run all tests.

   `time_limit`: next to each test will be an approximate runtime (in seconds). If you want to set a limit for all tests to run in, set this parameter to whatever

6. If you need to toggle your tests on and off throughout the whole script, add:
   ```python
   easytest.toggle()
   ```

---

## Example output

`example.py`:

```python
import easytest

@easytest.test(stdin="5", stdout="10")
def myfunc():
    x = int(input())
    print(x + 5)

easytest.linebreak()

@easytest.test(params=[5, 3], stdout="10")
def myfunc2(x, test=0):
    print(x + test)

easytest.render()
```

`output`:

```
[ * ] Beginning tests
---
[ ✓ ] Test passed: myfunc (0.0s)

[ X ] Test failed: myfunc2 (0.0s)
        Expected: 10
        Returned: 8
---
[ * ] All tests complete (0.0s).
[ * ] 1/2 tests passed.
```

---

## Issues

If there are somehow any issues with the code, use the [Issues tab](https://github.com/TriG-Tbh/easytest/issues) to report them.

If you want to submit changes, use the [Pull requests tab](https://github.com/TriG-Tbh/easytest/issues).

---

## License

This project is licensed under the terms of the [MIT License](https://opensource.org/licenses/MIT).

Full license text can be found in `LICENSE.txt`.
