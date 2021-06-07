# DHBW-Python-WeatherApp

## for Windows
### getting started
We are using `python3.9`. First you have to create a virutal environment. Navigate to the root of this project and create one.
```shell 
py -m virtualenv venv
```

```shell
virtualenv venv --python=python3.9
```
After it is created, activate the virtual environment
```shell 
venv\Scripts\activate.bat
```

```shell
source venv/bin/activate
```

Now install all packages needed.
```shell 
pip install -r Organisation/requirements.txt
```

Keep in mind to update `requirements.txt` when adding dependencies. To get a list of all current dependencies run this command:
```shell 
pip freeze
```
To exit use this command:
```shell 
deactivate
```
