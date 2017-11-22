#!/usr/local/bin/python3.4
# -*- coding: utf8 -*-

from pyngr import Pyngr

if __name__ == '__main__':
    app = Pyngr("this is a hook")
    app.import_config("config.json")
#    app.new_website("https://hug33k.fr")
    app.run(debug=True)
