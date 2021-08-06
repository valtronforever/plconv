from gi.repository import Gtk
from pathlib import Path
from plconv.models.supplier import InFileParam


@Gtk.Template.from_file(str(Path(__file__).parents[0] / 'infilebox.glade'))
class InFileBox(Gtk.Box):
    __gtype_name__ = 'InFileBox'

    data = None

    label = Gtk.Template.Child()
    filepath = Gtk.Template.Child()
    params = None

    def __init__(self, params: InFileParam, **kwargs):
        super().__init__(**kwargs)
        self.params = params
        self.data = params.data
        self.label.set_text(params.label + ':')
