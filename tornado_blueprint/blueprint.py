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


class Blueprint(object):
    """
    This is the blueprint class. It has a similar interface to a tornado
    application, but must be registered on the root application later.
    """

    def __init__(self, name, url_prefix="", **settings):
        """
        """
        # The unique name of the blueprint. Used internally to resolve
        # addresses and paths (especially templates).
        self.name = name
        self.url_prefix = url_prefix

        # todo:
        #   This dictionary should extend the application settings.
        self.settings = settings

        self._handlers = list()
        return None

    def add_handlers(self, host_pattern, host_handlers):
        """
        """
        self._handlers.extend(
            (host_pattern, handler) for handler in host_handlers
        )
        return None
