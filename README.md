# Build

To build the docs locally:
```
git clone https://github.com/CyVerse-learning-materials/foss.git

cd foss

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python -m mkdocs serve -a localhost:8000
```
Open a browser and go to https://localhost:8000 If something is already running on localhost:8000 just change the port in the command.
