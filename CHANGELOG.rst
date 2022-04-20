Change Log
==========


Under development
~~~~~~~~~~~~~~~~~~
*

2022.04.20
~~~~~~~~~~
* Adds `SMTPDBEmailBackend` , a mixture between SMTP and DB mail backend.
* Remove south migrations
* Allow only superusers to access email body.


2021.11.29
~~~~~~~~~~
* Upgrade compatibility from the main fork to work with Django 3.2 +
* Add option on admin to (re)send the mail using the smtp backend