## GeneaFamily
(Care: Project is actually in progress)
__GeneaFamily__ is a Django project for make a family tree.
This project is written in Python 3.6 and made with Django 1.11.

#### Current features:
**C/U/D/R** == Create/Update/Delete/Read.

- C/U/D/R a member
- C/U/D/R a event type (Not a event)

#### Next feature:
- Assign an event to a member (Birth, Death...)

#### How to install:
Clone this repo:
`git clone git@github.com:Hugo-prod/GeneaFamily.git`

Go in the repo:
`cd GeneaFamily`

Make a python environment with VirtualEnv:
`virtualenv .venv`

Active the environment:
`.venv/bin/activate`

Download and install the libs:
`pip install -r requirements.txt`

Make migrations:
`./manage.py makemigrations`

Make DB:
`./manage.py migrate`

Load a few datas (Important ! ):
`./manage.py loaddata GeneaFamily/fixtures/EventType.json`

Launch server:
`./manager.py runserver`

Now, open your browser (`localhost:8000`) and make your Genealogy Tree.

#### Apps used:
- Django-Bootstrap4 (for form) [depot](https://github.com/zostera/django-bootstrap4)
- Django-AutoSlug [depot](https://github.com/neithere/django-autoslug/)