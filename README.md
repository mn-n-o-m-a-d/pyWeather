# pyWeather app
Simple weather app using python-weather.
Enter a location to get current weather and a forecast.

## Use a Virtual Environment for Python-Weather:

### Navigate to your project folder
cd /path/to/your/project

### Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

### Install packages
pip install --upgrade pip
pip install python-weather pytest

### Run the project
python3.12 src/main.py 

### Deactivate Virtual Environment
deactivate

### Checkstyle before push
 + Format: ruff format --target-version=py312 .
 + Check:  ruff format --diff --target-version=py312