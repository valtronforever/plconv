from gi.repository import Gtk
from typing import Type, Callable, List, Optional
from pydantic import BaseModel, Field
from pathlib import Path


class Base(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class InFileParam(Base):
    label: str
    filepath: Optional[Path] = None
    data: dict = Field(default_factory=dict)


class OutFileParam(Base):
    path: Optional[Path] = None
    name: str


class ConvertParams(Base):
    in_params: List[InFileParam]
    out_params: OutFileParam


class Supplier(Base):
    id: str
    name: str
    widget: Type[Gtk.Widget]
    convert: Callable
    params: Optional[ConvertParams] = None
