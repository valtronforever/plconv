from gi.repository import Gtk, GLib, GObject
from pathlib import Path
import concurrent.futures
import logging
import traceback
from models.supplier import Supplier


def get_documents_path():
    return GLib.get_user_special_dir(GLib.USER_DIRECTORY_DOCUMENTS)


@Gtk.Template.from_file('plconv/widgets/layout_basic.glade')
class LayoutBasic(Gtk.Box):
    __gtype_name__ = 'LayoutBasic'

    supplier: Supplier
    in_path = Gtk.Template.Child()
    out_path = Gtk.Template.Child()
    convert_button = Gtk.Template.Child()

    proc = GObject.Property(type=bool, default=False)

    def __init__(self, supplier: Supplier, **kwargs):
        super().__init__(**kwargs)
        self.supplier = supplier
        self.out_path.set_current_folder(get_documents_path())
        self.in_path.connect('file-set', self.render_button_sensivity)
        self.out_path.connect('file-set', self.render_button_sensivity)
        self.connect('notify::proc', self.render_button_sensivity)
        self.render_button_sensivity()

    @Gtk.Template.Callback(name='on_convert_button_clicked')
    def on_convert_button_clicked(self, button):
        self.proc = True
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(
                self.supplier.convert,
                Path(self.in_path.get_filename()),
                Path(self.out_path.get_filename()),
            )
            future.add_done_callback(self.on_execution_complete)

    def show_success_message(self):
        dialog = Gtk.MessageDialog(
            transient_for=self.get_toplevel(),
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Завершено!",
        )
        dialog.format_secondary_text(
            "Преобразование успешно завершено."
        )
        dialog.run()
        dialog.destroy()

    def show_error_message(self, err):
        dialog = Gtk.MessageDialog(
            transient_for=self.get_toplevel(),
            flags=0,
            message_type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.CANCEL,
            text=f"Ошибка: {type(err).__name__}",
        )
        dialog.format_secondary_text(
            "\r\n".join([
                str(err),
                ''.join(traceback.format_tb(err.__traceback__))
            ])
        )
        dialog.run()
        dialog.destroy()

    def on_execution_complete(self, future):
        self.proc = False
        if future.exception():
            logging.error(type(future.exception()).__name__)
            logging.error(future.exception())
            logging.error(''.join(traceback.format_tb(future.exception().__traceback__)))
            GLib.idle_add(self.show_error_message, future.exception())
        else:
            GLib.idle_add(self.show_success_message)

    def render_button_sensivity(self, *args, **kwargs):
        if self.in_path.get_filename() is not None and \
           self.out_path.get_filename() is not None and \
           not self.proc:
            self.convert_button.set_sensitive(True)
        else:
            self.convert_button.set_sensitive(False)
