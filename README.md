# DHBW-Python-WeatherApp
### getting started
In this project, we are using `python3.8`. First you have to create a virutal environment. Navigate to the root of this project and create one.
## for Windows

```shell 
py -m venv env
```

After it is created, activate the virtual environment
```shell 
.\env\Scripts\activate
```

Now install all packages needed.
```shell 
pip install -r Organisation/requirements.txt
```

Keep in mind to update `requirements.txt` when adding dependencies. To get a list of all current dependencies run:
```shell 
pip freeze
```
To exit use this command:
```shell 
deactivate
```

## for Mac and Linux

```shell 
python3 -m venv env
```

After it is created, activate the virtual environment
```shell 
source env/bin/activate
```

Now install all packages needed.
```shell 
pip install -r Organisation/requirements.txt
```

Keep in mind to update `requirements.txt` when adding dependencies. To get a list of all current dependencies run:
```shell 
pip freeze
```
To exit use this command:
```shell 
deactivate
```
