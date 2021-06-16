from threading import ThreadError
from typing import Any, Callable, Optional

import_t0: Any
logger: Any

class LabbenchDeprecationWarning(DeprecationWarning): ...

def show_messages(minimum_level: Any, colors: bool = ...) -> None: ...

class Ownable:
    __objclass__: Any = ...
    def __init__(self) -> None: ...
    __name__: Any = ...
    def __set_name__(self, owner_cls: Any, name: Any) -> None: ...
    def __get__(self, owner: Any, owner_cls: Optional[Any] = ...): ...
    def __owner_init__(self, owner: Any) -> None: ...
    def __owner_subclass__(self, owner_cls: Any): ...

class ConcurrentException(Exception): ...
class OwnerThreadException(ThreadError): ...
class ThreadEndedByMaster(ThreadError): ...

def hide_in_traceback(func: Any): ...

class _filtered_exc_info:
    lb_wrapped: Any = ...
    def __init__(self, wrapped: Any) -> None: ...
    def __call__(self): ...

def sleep(seconds: Any, tick: float = ...) -> None: ...
def check_hanging_thread() -> None: ...
def retry(exception_or_exceptions: Any, tries: int = ..., delay: int = ..., backoff: int = ..., exception_func: Any = ...): ...
def until_timeout(exception_or_exceptions: Any, timeout: Any, delay: int = ..., backoff: int = ..., exception_func: Any = ...): ...
def kill_by_name(*names: Any) -> None: ...
def hash_caller(call_depth: int = ...): ...
def stopwatch(desc: str=..., threshold: float=...) -> Any: ...

class Call:
    func: Any = ...
    name: Any = ...
    args: Any = ...
    kws: Any = ...
    queue: Any = ...
    def __init__(self, func: Any, *args: Any, **kws: Any) -> None: ...
    result: Any = ...
    traceback: Any = ...
    def __call__(self): ...
    def set_queue(self, queue: Any) -> None: ...
    @classmethod
    def wrap_list_to_dict(cls, name_func_pairs: Any): ...

class MultipleContexts:
    abort: bool = ...
    __name__: str = ...
    objs: Any = ...
    params: Any = ...
    call_handler: Any = ...
    exc: Any = ...
    def __init__(self, call_handler: Callable[[dict, list, dict], dict], params: dict, objs: list) -> None: ...
    def enter(self, name: Any, context: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *exc: Any) -> None: ...

def concurrently(*objs: Any, **kws: Any): ...
def sequentially(*objs: Any, **kws: Any): ...

class ThreadDelegate:
    def __init__(self, sandbox: Any, obj: Any, dir_: Any, repr_: Any) -> None: ...
    def __call__(self, *args: Any, **kws: Any): ...
    def __getattribute__(self, name: Any): ...
    def __dir__(self): ...
    def __setattr__(self, name: Any, value: Any): ...

class ThreadSandbox:
    __repr_root__: str = ...
    __dir_root__: Any = ...
    def __init__(self, factory: Any, should_sandbox_func: Optional[Any] = ...) -> None: ...
    def __getattr__(self, name: Any): ...
    def __setattr__(self, name: Any, value: Any): ...
    def __del__(self) -> None: ...
    def __dir__(self): ...

class ConfigStore:
    @classmethod
    def all(cls): ...
    @classmethod
    def frame(cls): ...

# Names in __all__ with no definition:
#   _force_full_traceback
#   timeout_itercopy_func
