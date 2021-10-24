# Flask App API
# Python Flask Application 

Practical Flask API APP.

## Installation

Use the package Homebrew [python3](https://docs.brew.sh/Homebrew-and-Python) to install python.
Set Up Python package and installation on MacOS [Opensource:](https://opensource.com/article/19/5/python-3-default-mac)
```bash
python3 -m pip install --upgrade setuptools
```

```bash
python3 -m pip install --upgrade pip
```

update pip version
```bash
pip install --upgrade pip 
```

Create Python Environment on your Flask Project
```bash
 python3 -m venv <./venv ==> your venv name >     
```

Activate venv
```bash
 source venv/bin/activate
 or
 . venv/bin/activate       
```
Deactivate venv
```bash
 deactivate       
```

Save all the packages in the file with pip commands
```bash
 pip freeze > requirements.txt      
```

## Usage

```python
from flask import Flask

app = Flask(__name__)

@app.route('/') # represent to homepage
def home():
    return 'running server on port 5500...'

app.run(port=5500)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
