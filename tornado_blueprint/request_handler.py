#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2015 Benedikt Schmitt <benedikt@benediktschmitt.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# third party
import tornado.web

# local
from .template_loader import TemplateLoader


class RequestHandler(tornado.web.RequestHandler):
    """
    """

    def __init__(self, application, request, blueprint=None, **kargs):
        """
        """
        super().__init__(application=application, request=request, **kargs)
        self.blueprint = blueprint
        return None

    @property
    def settings(self):
        """
        First lookup the blueprints settings and then the application settings.
        """
        if self.blueprint:
            # Please note, that the blueprint will lookup its own settings and
            # then the application settings. Take a look at the blueprint class
            # for this.
            return self.blueprint.settings
        return self.application.settings

    def require_settings(self, name, feature="this feature"):
        """
        Raises an exception if the given app setting is not defined.
        """
        # Overridden with respect to the new resolution order of
        # *self.settings* (blueprint then application).
        if not self.settings.get(name):
            raise Exception("You must define the '%s' setting in your "
                            "application to use %s" % (name, feature))
        return None


    # template stuff
    # ~~~~~~~~~~~~~~

    def get_template_path(self):
        """
        Returns the path to the template folder.
        """
        return self.settings.get("template_path")

    def get_template_namespace(self):
        """
        We add the *blueprint* object to the template namespace.
        """
        namespace = super().get_template_namespace()
        namespace["blueprint"] = self.blueprint
        return namespace

    def create_template_loader(self, template_path):
        """
        We use our own :class:`TemplateLoader` class. This loader first
        looks up the template folder of the blueprint and then the application's
        template folder.
        """
        settings = self.settings
        kargs = dict()
        if "autoescape" in settings:
            # autoescape=None means "no escaping", so we have to be sure
            # to only pass this kwarg if the user asked for it.
            kwargs["autoescape"] = settings["autoescape"]
        if "template_whitespace" in settings:
            kwargs["whitespace"] = settings["template_whitespace"]

        # Create the loader.
        loader = TemplateLoader(
            application=self.application, blueprint=self.blueprint, **kargs
        )
        return loader

    def render_string(self, template_name, **kargs):
        """
        .. todo::

            Check if we need to override this method.
        """
        if template_name.startswith("."):
            template_name = self.blueprint.name + template_name
        return super().render_string(template_name, **kargs)

    def static_url(self, path, include_host=None, **kargs):
        """
        .. todo::

            Use the StaticFileHandler of the blueprint. Check if we can
            achieve this, without overriding this method.
        """
        return super().static_url(path, include_host, **kargs)

    def reverse_url(self, name, *args):
        """
        Alias for `Application.reverse_url`, but allows you to specify a
        name in the current blueprint with a simple *.* prefix.

        .. code-block::

            >>> # Index handler of the current blueprint
            >>> reverse_url(".index")
            ...
            >>> # Index handler of the blueprint *authentication*
            >>> reverse_url("authentication.index")
            ...
            >>> # Gloabl index handler
            >>> reverse_url("index")
        """
        if name.startswith("."):
            name = self.blueprint.name + name
        return super().reverse_url(name, *args)
