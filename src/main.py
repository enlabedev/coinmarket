#!/usr/bin/python
# -*- coding: utf-8 -*-
from core.config import conFlask

if __name__ == '__main__':
    # Create app.
    server = conFlask()

    # Run app. For production use another web server.
    # Set debug and use_reloader parameters as False.
    server.run()