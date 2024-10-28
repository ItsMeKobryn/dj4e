Django for Everybody (DJ4E)
=============
This repository is an updated version of https://github.com/ab007shetty/dj4e with all the errors resolved.
It includes all the necessary files for the Django for Everybody course autograded tests.

I highly recommend you all to follow this video https://youtu.be/kQcEPy-xzGI?si=JRTNqv7Yf1S5FU4V


Running Locally
---------------

To test the sample applications on your local machine, ensure you have Django installed. Follow these steps:

1.Open your terminal or command prompt.

2.Navigate to the project directory .

    cd dj4e
3.Start the Django development server

    python3 manage.py runserver

And visit `http://localhost:8000`.

Deploying on PythonAnywhere
-------------------------
First Download this repository on your local machine , this should be dj4e-master.zip
and upload it in the files tab of pythonanywhere and unzip it with the help of console .

After you've checked out the code in the dj4-master directory and executed the necessary migrations 
and data loading scripts, you'll need to configure your application on PythonAnywhere:

1.Go to the Web tab on your PythonAnywhere dashboard.

2.Update the following configuration settings:

    Source code:                 /home/your-account/dj4e-master/mysite
    Working Directory:           /home/your-account/dj4-master/mysite

3.Use the following code for your `WSGI configuration file`:

    import os
    import sys

    path = os.path.expanduser('~/dj4e-master')
    if path not in sys.path:
        sys.path.insert(0, path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    from django.core.wsgi import get_wsgi_application
    from django.contrib.staticfiles.handlers import StaticFilesHandler
    application = StaticFilesHandler(get_wsgi_application())

Special Thanks
---------------
Anirudha B Shetty https://github.com/ab007shetty

Ashish Kumar https://www.youtube.com/@AshishKumar-dd1pi




