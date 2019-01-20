.. image:: https://travis-ci.org/emilkey/phone.svg?branch=master
    :target: https://travis-ci.org/emilkey/phone

.. image:: https://img.shields.io/badge/quality-alpha-orange.svg

phone
=====

This is a simple `Flask`_ application for forwarding phone calls and hosting a conference bridge. It's meant to be
hosted on `Google App Engine`_ (standard environment). It uses `Twilio`_ for phone system integration.


Deployment & Configuration
--------------------------

General steps for deployment:

#. Clone this repository
#. Configure the phone number to which your calls will be forwarded in app.yaml (format "+1xxxyyyzzzz")
#. Download the `Google Cloud SDK`_
#. Ensure the App Engine Python components are installed: ``gcloud components install app-engine-python``
#. Initialize project (or create project, if none exists): ``gcloud init``
#. Deploy to App Engine: ``gcloud app deploy app.yaml --project <project_name>``
#. Log into your Twilio account, purchase a number (if you don't already have one), and configure it to accept incoming
   voice calls with a webhook: "https://<your-project>.appspot.com/call/forward"

This app can also be run on your own server using `gunicorn`_: ``gunicorn phone:gunicorn_app``

Note that you will incur hosting charges from Google and usage charges from Twilio based on the volume of calls you
receive.


.. _Flask: https://http://flask.pocoo.org
.. _Twilio: https://www.twilio.com
.. _Google App Engine: https://cloud.google.com/appengine/docs/python/
.. _Google Cloud SDK: https://cloud.google.com/sdk/docs/
.. _gunicorn: https://gunicorn.org/
