# DJANGO

This is a user website boilerplate example that has all the form CRUD functionality implemented as well as a functional user managmet system based on roles 

## VirtualEnv users

I added a batch file to for easy launch if you are using Windows, just edit the activate.bat to your needs and install [Virtualenv](https://pypi.org/project/virtualenv/)

```bash
pip install --user virtualenv
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install django
pip install django-filter
```

For a fresh start delete the Sqlite database file **db.sqlite3**  and proceed to make the migrations.


```bash
python manage.py makemigrations
python manage.py migrate
```

Then if you are not using virtualenv execute this

```bash
python manage.py runserver
```

If you are utilizing my batch file just run it after editing the command

```bash
python manage.py runserver IP:port
```

To your needs