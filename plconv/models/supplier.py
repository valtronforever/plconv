from gi.repository import Gtk
from typing import Type, Callable
from pydantic import BaseModel


class Supplier(BaseModel):
    id: str
    name: str
    widget: Type[Gtk.Widget]
    convert: Callable

    class Config:
        arbitrary_types_allowed = True
