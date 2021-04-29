from . import _traits, util
from typing import Any, Optional

def list_devices(depth: int=...):
    ...


class DisconnectedBackend():
    name: Any = ...

    def __init__(self, dev: Any) -> None:
        ...

    def __getattr__(self, key: Any) -> None:
        ...
    str: Any = ...


class AttributeDefinition():
    bool: Any = ...
    float: Any = ...
    int: Any = ...
    complex: Any = ...
    str: Any = ...
    bytes: Any = ...
    list: Any = ...
    tuple: Any = ...
    dict: Any = ...
    Path: Any = ...
    DataFrame: Any = ...
    Series: Any = ...
    array: Any = ...
    ndarray: Any = ...
    NetworkAddress: Any = ...

    def __init__(self, role: Any) -> None:
        ...
property: Any
value: Any
datareturn: Any


class AdjustStub():
    ...


class Device(_traits.HasTraits, util.Ownable):

    def __init__(self, resource: str='str'):
        ...
    resource: Any = ...
    concurrency: Any = ...
    backend: Any = ...

    def open(self) -> None:
        ...

    def close(self) -> None:
        ...
    __children__: Any = ...

    @classmethod
    def __init_subclass__(cls) -> None:
        ...

    def __open_wrapper__(self) -> None:
        ...

    def __owner_init__(self, owner: Any) -> None:
        ...

    def __close_wrapper__(self) -> None:
        ...

    def __imports__(self) -> None:
        ...

    def __enter__(self):
        ...

    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None:
        ...

    def __del__(self) -> None:
        ...

    def connected(self):
        ...
