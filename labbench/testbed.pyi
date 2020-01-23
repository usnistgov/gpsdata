from labbench.testbed import *
import labbench
import builtins

class Device(labbench.core.HasStates):
    def open(self) -> None: ...
    def close(self) -> None: ...
    def __init__(self, resource: str = '', *, concurrency_support: bool = True) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __open_wrapper__(self) -> None: ...
    def __close_wrapper__(self) -> None: ...
    def __imports__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type_, value, traceback) -> None: ...
    def __del__(self) -> None: ...
    def __repr__(self) -> None: ...
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def __str__(self) -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

class Host(labbench.core.Device):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def metadata(self) -> None: ...
    def _Host__python_module_versions(self) -> None: ...
    @Unicode(help=' Get a timestamp of the current time\n        ')
    def time(self) -> None: ...
    def time(func) -> None: ...
    @Unicode(help=' Get the current host log contents.\n        ')
    def log(self) -> None: ...
    def log(func) -> None: ...
    @Unicode(help=' Try to determine the current commit hash of the current git repo\n        ',cache=True)
    def git_commit_id(self) -> None: ...
    def git_commit_id(func) -> None: ...
    @Unicode(help=' Try to identify the remote URL of the repository of the current git repo\n        ',cache=True)
    def git_remote_url(self) -> None: ...
    def git_remote_url(func) -> None: ...
    @Unicode(help=' Get the name of the current host\n        ',cache=True)
    def hostname(self) -> None: ...
    def hostname(func) -> None: ...
    @Unicode(help=' URL for browsing the current git repository\n        ',cache=True)
    def git_browse_url(self) -> None: ...
    def git_browse_url(func) -> None: ...
    def __init__(self, resource: str = '', *, concurrency_support: bool = True) -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass

class Email(labbench.core.Device):
    @Bool(help=' are we connected? ')
    def connected(self) -> None: ...
    def connected(func) -> None: ...
    def _send(self, subject, body) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def send_summary(self) -> None: ...
    def __init__(self, resource: str = 'smtp.nist.gov', *, concurrency_support: bool = True, port: int = 25, sender: str = 'myemail@nist.gov', recipients: list = ['myemail@nist.gov'], success_message: str = 'Test finished normally', failure_message: str = 'Exception ended test early') -> None: ...
    def __init_wrapped__(self, **settings) -> None: ...
    pass
