from gi.repository import Gtk
from plconv.models.supplier import Supplier


@Gtk.Template.from_file('plconv/widgets/supplier_listbox_row.glade')
class SupplierListBoxRow(Gtk.ListBoxRow):
    __gtype_name__ = 'SupplierListBoxRow'

    supplier_name_label = Gtk.Template.Child()
    supplier: Supplier

    def __init__(self, supplier: Supplier, **kwargs):
        super().__init__(**kwargs)
        self.supplier = supplier
        self.supplier_name_label.set_text(self.supplier.name)
