#!/usr/bin/env python3

# std
import os
import sys

# third party
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# local
sys.path.insert(
    0, os.path.abspath(os.path.join("../", os.path.dirname(__file__)))
)
import tornado_blueprint


class IndexHandler(tornado_blueprint.RequestHandler):
    """
    The *global* index page.

    URL: /
    """

    def get(self):
        """
        """
        print("index:get")
        if False:
            self.write("Index")
            return None
        self.render("index.html")
        return None


def make_application():
    """
    Creates the whole tornado application.
    """
    application = tornado_blueprint.Application(
        [
            tornado.web.url(r"/", IndexHandler, name="index"),
        ],
        debug = True,
        template_path = "templates",
    )

    # Register the dashboard blueprint.
    import dashboard
    dashboard_blueprint = dashboard.make_blueprint()
    application.register_blueprint(dashboard_blueprint)

    import settings
    settings_blueprint = settings.make_blueprint()
    application.register_blueprint(settings_blueprint)
    return application


def main():
    """
    Runs the test application.
    """
    application = make_application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    return None


if __name__ == "__main__":
    main()
