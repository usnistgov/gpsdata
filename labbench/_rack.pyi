from . import util as util
from pathlib import Path
from typing import Any
EMPTY: Any
BASIC_TYPES: Any

def null_context(owner: Any) -> None:
    ...


class Step():
    __wrapped__: Any = ...
    owner: Any = ...
    __doc__: Any = ...
    __name__: Any = ...
    __qualname__: Any = ...

    def __init__(self, owner: Any, name: Any):
        ...
    dependencies: Any = ...
    args: Any = ...
    parameters: Any = ...

    def introspect(self) -> None:
        ...

    def extended_signature(self):
        ...

    def extended_args(self):
        ...

    def extended_call(self, *args: Any, **kws: Any):
        ...

    def __call__(self, *args: Any, **kws: Any):
        ...

    def __and__(self, other: Any):
        ...

    def __rand__(self, other: Any):
        ...


class SequencedMethod(util.Ownable):

    def __call__(self, **kwargs: Any):
        ...

    @classmethod
    def to_template(cls, path: Any) -> None:
        ...
    results: Any = ...

    def from_csv(self, path: Any) -> None:
        ...


class OwnerContextAdapter():
    owner: Any = ...

    def __init__(self, owner: Any) -> None:
        ...

    def __enter__(self) -> None:
        ...

    def __exit__(self, *exc_info: Any) -> None:
        ...

def recursive_devices(top: Any):
    ...

def recursive_owner_managers(top: Any):
    ...

def owner_context_manager(top: Any):
    ...


class Owner():

    def __init_subclass__(cls: Any, ordered_entry: list=...) -> Any:
        ...

    def __init__(self, **devices: Any) -> None:
        ...

    def __setattr__(self, key: Any, obj: Any) -> None:
        ...

    @property
    def __enter__(self):
        ...

    @property
    def __exit__(self):
        ...

def __call__():
    ...


class Sequence(util.Ownable):
    spec: Any = ...

    def __init__(self, **specification: Any):
        ...

    def __owner_subclass__(self, testbed_cls: Any):
        ...


class notify():

    @classmethod
    def clear(cls) -> None:
        ...

    @classmethod
    def return_event(cls: Any, returned: dict) -> Any:
        ...

    @classmethod
    def call_event(cls: Any, parameters: dict) -> Any:
        ...

    @classmethod
    def observe_returns(cls, handler: Any) -> None:
        ...

    @classmethod
    def observe_calls(cls, handler: Any) -> None:
        ...

    @classmethod
    def unobserve_returns(cls, handler: Any) -> None:
        ...

    @classmethod
    def unobserve_calls(cls, handler: Any) -> None:
        ...


class RackMeta(type):

    def take_module(cls, module: Any):
        ...

    def __enter__(cls) -> None:
        ...

    def __exit__(cls, *exc_info: Any) -> None:
        ...


class Rack(Owner, util.Ownable, metaclass=RackMeta):

    def __init__():
        ...

    def __init_subclass__(cls, ordered_entry: Any=...) -> None:
        ...

    def __owner_init__(self, owner: Any) -> None:
        ...

    def __getattribute__(self, item: Any):
        ...

    def __getitem__(self, item: Any):
        ...

    def __len__(self):
        ...

    def __iter__(self) -> Any:
        ...


class Configuration(util.Ownable):
    path: Any = ...

    def __init__(self, root_path: Path) -> None:
        ...

    def __owner_subclass__(self, owner_cls: Any):
        ...

    def make_templates(self) -> None:
        ...

    def parameters(self, cls: Any):
        ...
