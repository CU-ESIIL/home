# Starting with Python

## Sell It
Python is a flexible language with a rich ecosystem of libraries for data
science, web apps, and automation. Its clean syntax reads like English and it
runs on every major operating system, making it a great first language for
researchers and analysts.

## Show It
A minimal script prints a message, but even this tiny example demonstrates the
language's readability:

```python
print("Hello, OASIS!")
```

## Do It
1. **Install Python.** Download Python from the
   [official site](https://www.python.org/) or install a distribution like
   [Anaconda](https://www.anaconda.com/download) that bundles common tools.
2. **Create an environment.** Use `conda create -n myenv python` or
   `python -m venv myenv` to keep project packages isolated.
3. **Activate the environment.** Run `conda activate myenv` or on macOS/Linux
   `source myenv/bin/activate` (Windows: `myenv\Scripts\activate`).
4. **Install a package.** Try `pip install pandas` to see how dependencies are
   added.
5. **Run the script.** Save the example above as `hello.py` and execute
   `python hello.py`.

## Review It
Check `python --version` and run `pip list` to view installed packages. When
you're done, deactivate the environment with `conda deactivate` or
`deactivate` so your base system stays clean.

