# thanatos
[![Build Status](https://travis-ci.org/evetrivia/thanatos.svg)](https://travis-ci.org/evetrivia/thanatos)
[![Coverage Status](https://coveralls.io/repos/evetrivia/thanatos/badge.svg)](https://coveralls.io/r/evetrivia/thanatos)
[![PyPI](http://img.shields.io/pypi/v/Thanatos.svg)](https://pypi.python.org/pypi/Thanatos)
[![Documentation Status](https://readthedocs.org/projects/thanatos/badge/)](https://thanatos.readthedocs.org/en/latest/)

Thanatos is a Python library for generating trivia questions for the sci-fi MMO [EVE Online](https://www.eveonline.com/). It
does require a MySQL database backend to operate and will download a selected list of DB tables. These tables come from
the [Static Data Export](https://developers.eveonline.com/resource/static-data-export).

## Example Usage
```python
import thanatos

# For default vagrant/cloud9 connection defaults
db = thanatos.database.db_utils.get_connection()

# Or provide your own connection details
connection_details = {
    'host': '127.0.0.1',
    'user': 'example',
    'password': 'some_secure_password',
    'database': 'some_db',
}

db = thanatos.database.db_utils.get_connection(connection_details)

# Asking a random question
question_class = thanatos.questions.question_utils.get_random_question()
question_instance = question_class(db)
question = question_instance.ask()

# Asking a specific question
question_instance = thanatos.questions.universe.BorderingRegionsQuestion(db)
question = question_instance.ask()

# Alternative way of asking a specific question
question_class = question_utils.get_question('borderingregionsquestion')
question_instance = question_class(db)
question = question_instance.ask()
```