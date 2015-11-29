#!/usr/bin/env python3

import os
import sys

import tornado
import tornado.web
from tornado_blueprint import RequestHandler, Blueprint


class Index(RequestHandler):
    """
    Returns the index page of the settigns blueprint.
    """

    def get(self):
        print("settings:index:get")
        if False:
            self.write("Settings - Index")
            return None
        self.render(".index.html")
        return None


class Account(RequestHandler):
    """
    Returns the page for the account settings.
    """

    def get(self):
        print("settings:account:get")
        if False:
            self.write("Settings - Account")
            print(self.reverse_url(".account"))
            return None
        self.render(".account.html")
        return None


def make_blueprint():
    """
    Creates the blueprint for the settings.
    """
    curr_dir = os.path.abspath(os.path.dirname(__file__))

    blueprint = Blueprint(
        name = "settings",
        url_prefix = "/settings",
        template_path = os.path.join(curr_dir, "templates"),
    )
    blueprint.add_handlers(
        ".*",
        [
            tornado.web.url("/", Index, name="index"),
            tornado.web.url("/account", Account, name="account")
        ]
    )
    return blueprint
