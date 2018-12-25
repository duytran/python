# python
The python workshop

## Project Organization
---

```
    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── docs               <- The document relative training python
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
```

## Quick start
-----------

- Python 3.6
- [virtualenv](https://virtualenv.pypa.io/en/stable/)
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

[See instruction](./docs/python-install-macOS.md)

### Setting up

**I. Setup environment**

```
$ mkvirtualenv -p $(pyenv root)/versions/3.6.0/bin/python3.6 python
```

Activate the environment

```
$ source ./.activate.sh
```