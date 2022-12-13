# django_reservation_system

Django projects that has displays a reservations their check in time, check out time and rental it's linked to.


## Local Setup

To run this projects locally 

- setup env
    `python3 -m venv env`

- enable env
    `source env/bin/activate`

- install dependencies 
    `pip install -r requirements.txt`

- go into main_app director
    `cd main_app`

- run any outstanding migrations
    `python manage.py migrate`

- seed project with test data
    `python manage.py loaddata reservations/fixtures/rentals.json`

- run dev server
    `python manage.py runserver`

- see results
   open browser at http://127.0.0.1:8000/reservations/

## Possible Improvements

- Change db to another db that won't have the same locking issues as sqllite something like postgres

- Possible pagination for fetching on reservations in views

- More Meta data like constraints on Models

- Larger fixtures with more data to cover more use cases

- Improve visuals on template