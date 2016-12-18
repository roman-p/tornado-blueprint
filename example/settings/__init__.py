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

class Profile(RequestHandler):
    """
    Returns the page for the account settings.
    """

    def get(self):
        print("settings:profile:get")
        if False:
            self.write("Settings - Profile")
            print(self.reverse_url(".profile"))
            return None
        self.render(".profile.html")
        return None

class Timezone(RequestHandler):
    """
    Returns the page for the account settings.
    """

    def get(self):
        print("settings:profile:timezone:get")
        if False:
            self.write("Settings - Profile - Timezone")
            print(self.reverse_url(".timezone"))
            return None
        self.render(".timezone.html")
        return None

def make_profile_blueprint():
    curr_dir = os.path.abspath(os.path.dirname(__file__))

    blueprint = Blueprint(
        name="profile",
        url_prefix="/profile",
        template_path=os.path.join(curr_dir, "templates"),
    )
    blueprint.add_handlers(
        ".*",
        [
            tornado.web.url("/", Profile, name="index"),
            tornado.web.url("/timezone", Timezone, name="timezone")
        ]
    )

    return blueprint

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

    #add child blueprints in parent initialization
    sub_blueprint = make_profile_blueprint()
    blueprint.register_blueprint(sub_blueprint)

    return blueprint
