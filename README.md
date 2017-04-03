Notifications
=============

manage notifications with ease. Built with pain.


Setting up the developer environment
====================================

```
$ git clone git@github.com:sayanchowdhury/notifications.git
$ cd notifications
$ mkvirtualenv notifications
$ pip install -r requirements.txt
$ sudo npm install stylus -g
$ cp notifications/settings.py.sample notifications/settings.py
$ ./manage.py migrate
$ ./manage.py compilestylus
```

Generating Github tokens and setting up Social App
--------------------------------------------------

App registration (get your key and secret here)
    https://github.com/settings/applications/new

Development callback URL
    http://localhost:8000/accounts/github/login/callback/

Now start your server, visit your admin pages (e.g. http://localhost:8000/admin/)
and follow these steps:

- Add a Site for your domain, matching settings.SITE_ID
- Add `Social App`(`socialaccount` app) for Github Provider


Start the development server: `http://localhost:8000/`
