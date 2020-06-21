#travsim challenge 1

```writing a RESTful api```

To run this project

Create a virtual enviroment and,
make sure that you have the required packages. check out the ```requirements.txt``` file.
Navigate to where there is the ```manage.py``` file and create a superuser using this command ```python manage.py createsuperuser```- once successfully created, you should give you access to the django admin.
While still where there is the ```manage.py``` file, run ```python manage.py runserver```. this will run the django server.
Go to your browser and type ```http://127.0.0.1:8000/admin``` go gain access and to the admin panel and edit the goods list. and type ```http://127.0.0.1:8000/goods``` to see the goods.json list

The API code is found in ```ts_challenge/challenge1/travsim/resapi/views.py```
