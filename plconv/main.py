import sys
import gi
import logging

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio
from plconv.windows.pricelistconverter import PricelistConverterWindow

VERSION = '1.0'
pkgdatadir = 'data'
logging.basicConfig(level=logging.DEBUG)


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.pharmstudio.pricelistconverter',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = PricelistConverterWindow(application=self)
        win.present()


def main(version):
    app = Application()
    return app.run(sys.argv)


if __name__ == '__main__':
    sys.exit(main(VERSION))
