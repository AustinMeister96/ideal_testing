Instructions for setting up local development sever

Install python 3.9.12 (other version may work but haven't been tested yet)

Locate the requirements.txt file and run pip install -r requirements.txt

Next setup a mysql database named ideal_db with a user root and pass root and grant all permissions

Then cd into the directory with the manage.py file (should be /IDEAL_1/) and run python manage.py collectstatic (then type in y and press enter)

Next run 'python manage.py makemigrations'
Then run 'python manage.py migrate'

Next to start the server run 'python manage.py runserver' - this will start the development server at localhost:8000/

Mac Apple Silicon Notes

- To start Tailwind run: python3-intel64 manage.py tailwind start