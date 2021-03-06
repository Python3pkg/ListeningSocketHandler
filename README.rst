ListeningSocketHandler
======================

The opposite of logging.handlers.SocketHandler

.. image:: https://travis-ci.org/bencord0/ListeningSocketHandler.png?branch=master

Installation
------------
    $ pip install ListeningSocketHandler

Example Usage
-------------

1. Create a logger

    >>> import logging
    >>> from ListeningSocketHandler import ListeningSocketHandler
    >>> log = logging.getLogger()
    >>> log.setLevel(logging.DEBUG)

2. Create some handlers

    A normal StreamHandler that outputs to stderr and
    a ListeningSocketHandler bound to port 12345.

    >>> sh = logging.StreamHandler()
    >>> sh.setLevel(logging.WARN)
    >>> lh = ListeningSocketHandler(12345)
    >>> lh.setLevel(logging.DEBUG)

3. Add handlers to the logger

    >>> log.addHandler(sh)
    >>> log.addHandler(lh)

4. Log some things

    >>> log.info("An informational message")
    >>> log.warn("A warning message")
    A warning message

5. Connect to the logger, and log more detailed events

    In a new shell, connect to the logger.

    $ telnet localhost 12345

    Back in python, use different log levels.

    >>> log.critical("A critical message")
    A critical message
    >>> log.debug("A debugging message")

    Watch the detailed stream in the telnet session.

    A critical message
    A debugging message

Making it work with Django
--------------------------

1. Install the handler

    $ pip install LoggingSocketHandler

2. Add the ListeningSocketHandler to the LOGGING dict

    LOGGING = {
        ...
        'handlers': {
            'listeningsocket': {
                'level': 'DEBUG',
                'class': 'ListeningSocketHandler.ListeningSocketHandler',
            },
            ...
        },
        'loggers': {
            'myapp': {
                'handlers': ['listeningsocket'],
                'level': 'DEBUG',
                'propagate': True,
            },
            ...
        },
    }

3. Run the server, and check the logs

    $ ./manage.py runserver
    ListeningSocketHandler on port: 40955
    ListeningSocketHandler on port: 49830
    Validating models...

    0 errors found
    Django version 1.4.2, using settings 'myproject.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

the default runserver is stupid, use foreman instead.

    $ foreman start
    17:55:11 web.1     | started with pid 24927
    17:55:13 web.1     | ListeningSocketHandler on port: 36688
    17:55:13 web.1     | Validating models...
    17:55:13 web.1     |
    17:55:13 web.1     | 0 errors found
    17:55:13 web.1     | Django version 1.4.2, using settings 'myproject.settings'
    17:55:13 web.1     | Development server is running at http://0.0.0.0:5000/
    17:55:13 web.1     | Quit the server with CONTROL-C.

4. Connect to the socket (telnet, netcat etc.)

    $ telnet localhost 36688
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.

5. Use django normally, and watch the detailed logs scroll past your terminal,
   or pipe them to a file for later analysis.

   $ ncat localhost 36688 > detailed-log.txt
   ^C

   Refresh the view, or perform the task to reproduce your bug, then break out
   with Control-C when you've got the logs that you want.


