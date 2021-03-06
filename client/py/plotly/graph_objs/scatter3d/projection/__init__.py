
from anvil.util import WrappedObject, WrappedList
from anvil.server import serializable_type


@serializable_type
class X(WrappedObject):
    _name = "X"
    _module = "plotly.graph_objs.scatter3d.projection"

@serializable_type
class Y(WrappedObject):
    _name = "Y"
    _module = "plotly.graph_objs.scatter3d.projection"

@serializable_type
class Z(WrappedObject):
    _name = "Z"
    _module = "plotly.graph_objs.scatter3d.projection"


__all__ = [
    'X',
    'Y',
    'Z',
]