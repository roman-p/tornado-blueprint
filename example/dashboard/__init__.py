#!/usr/bin/env python3

import os
import sys

import tornado
import tornado.web
from tornado_blueprint import RequestHandler, Blueprint


class Index(RequestHandler):
    """
    Returns the index page of the dashboard blueprint.
    """

    def get(self):
        print("dashboard:index:get")
        if False:
            self.write("Dashboard - Index")
            return None
        self.render(".index.html")
        return None


def make_blueprint():
    """
    Creates the blueprint for the dashboard.
    """
    curr_dir = os.path.abspath(os.path.dirname(__file__))

    blueprint = Blueprint(
        name = "dashboard",
        url_prefix = "/dashboard",
        template_path = os.path.join(curr_dir, "templates"),
    )
    blueprint.add_handlers(
        ".*",
        [
            tornado.web.url("/", Index, name="index"),
        ]
    )
    return blueprint
