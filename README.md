# ICTF Gradings Portal

A Web UI to the ICTF Pipeline package that is built for heroku.

**WARNING: [THIS IS AN MVP](https://www.wikiwand.com/en/Minimum_viable_product)** wrapper for the [backend project](https://github.com/rlongo/ictf-gradings-paperwork).

## Starting the App (Dev)
```bash
python run.py
```

## Starting the App (Production)
```bash
gunicorn app:app
```

OR, if you have the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
```bash
heroku local
```
