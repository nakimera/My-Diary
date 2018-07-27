[![Build Status](https://travis-ci.org/nakimera/My-Diary.svg?branch=develop)](https://travis-ci.org/nakimera/My-Diary)
[![Coverage Status](https://coveralls.io/repos/github/nakimera/My-Diary/badge.svg?branch=develop)](https://coveralls.io/github/nakimera/My-Diary?branch=develop)

# My-Diary
My Diary is an online journal where users can pen down their thoughts and feelings.  

## Getting started
You will need the following software running on your machine to get started

### Prerequisites

* Python 3.6
* pip

Download python from [here](https://www.python.org/getit/)  
Download pip from [here](https://pip.pypa.io/en/stable/reference/pip_download/)

### Installing

These are the steps on you how to get a development environment of the application running on your machine

* Make a directory on your computer

  ``` 
  $ mkdir my-diary 
  cd ~/my-diary
  ```

* Setup a virtual environment

Install a virtual environment via pip

``` $ pip install virtualenv ```

Create a virtual environment

```
$ virtualenv env 
```

Activate the virtual environment

```
$ my-diary/env/scripts/activate
```

Clone the project repo
'''
git clone https://github.com/nakimera/My-Diary.git
'''

Install requirements
'''
pip install -r requirements.txt
'''

Run the development server
'''
$ python run.py
'''

The app should now be running on http://localhost:5000

The following endpoints can be tested

| METHOD       | Endpoint           | Description  |
| ------------- |:-------------:| -----|
| GET      | /api/v1/entries | Get all entries
| GET      | /api/v1/entries/id      | Get specific entry using an id |
| POST | /api/v1/entries      | Create a new entry |
| PUT      | /api/v1/entries/id      | Modify a specific entry using an id |

### How to run tests
- Install pytest 
'''
$ pip install pytest
'''
 - Run tests
 '''
$ cd ~/my-diary/tests
$ pytest test_entry.py
 '''

## Deployment  sites
The user interfaces are hosted on github pages at https://nakimera.github.io/My-Diary/

The api is hosted on heroku at https://npdiary-api-heroku.herokuapp.com/
