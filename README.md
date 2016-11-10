# telavivmakers.org

Main web application for [telavivmakers.org](https://www.telavivmakers.org) website

## Dev

Make sure you have Python 3.x installed, and ideally a virtualenv setup:

```bash
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

To run the SCSS styles, you'll need the `scss` ruby gem installed:

```bash
$ scss --watch tami/static/css/scss/:tami/static/css
```

## License

[GPLv3](LICENSE)
