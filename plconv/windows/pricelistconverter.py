from gi.repository import Gtk
from plconv.widgets.supplier_listbox_row import SupplierListBoxRow
from plconv.models.supplier import Supplier
from plconv.data.suppliers import suppliers


@Gtk.Template.from_file('plconv/windows/pricelistconverter.glade')
class PricelistConverterWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'PricelistConverterWindow'

    supplier_list_box = Gtk.Template.Child()
    supplier_stack = Gtk.Template.Child()

    def _register_supplier(self, supplier: Supplier):
        self.supplier_list_box.add(SupplierListBoxRow(supplier))
        supplier_widget = supplier.widget(supplier)
        supplier_widget.show()
        self.supplier_stack.add_named(supplier_widget, supplier.id)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for supplier in suppliers:
            self._register_supplier(Supplier(**supplier))

    @Gtk.Template.Callback(name='on_row_selected')
    def on_row_selected(self, list_box, row: SupplierListBoxRow):
        self.supplier_stack.set_visible_child_name(row.supplier.id)
