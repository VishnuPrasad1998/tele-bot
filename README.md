# telebot
This is a chatbot made for fun with the help of Django and Django Channels. It was built over an existing chatbot by Vaisagh. For reference 
[Check it out](https://github.com/vaisaghvt/django-bot-server-tutorial)
Features:
1. Authentication
2. Click counts displayed on homepage itself.
3. Chatbot whick responds to our action.

[Click here](https://postimg.cc/gallery/mHWDWck) to see the screenshots of the webapp.

Setup:
1. Clone the repo
```git clone https://github.com/VishnuPrasad1998/telebot.git```
2. Inside telebot folder, first grab a virtualenv and activate it
```
virtualenv venv
source ven/bin/activate
```
3. Install all packages
```
pip install -r requirements.txt
```
4. Add your PostgreSQL credentials to settings.py(Only if you are using it for development in local machine other wise use dotenv)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<Your-DB-name>',
        'USER': '<Name=of-the-user>',
        'PASSWORD': '<Password>',
        'HOST': 'localhost'
    }
}
```
5. Migrate these changes
```
python manage.py makemigrations
python manage.py migrate
```
6. To create super user
```
python manage.py createsuperuser
```
8. To runserver(by default on port 8000)
```
python manage.py runserver
```
9. To run tests
```
./manage.py test chat/
```
You are good to go...
This is version1 so UI is a mess and features like count update can be made real time.
