# Stubs for struct

# Based on http://docs.python.org/3.2/library/struct.html

from typing import overload, Any, Tuple

class error(Exception): ...

def pack(fmt: str, *v: Any) -> bytes: ...
# TODO buffer type
def pack_into(fmt: str, buffer: Any, offset: int, *v: Any) -> None: ...

# TODO buffer type
def unpack(fmt: str, buffer: Any) -> Tuple[Any, ...]: ...
def unpack_from(fmt: str, buffer: Any, offset: int = ...) -> Tuple[Any, ...]: ...

def calcsize(fmt: str) -> int: ...

class Struct:
    format = b''
    size = 0

    def __init__(self, format: str) -> None: ...

    def pack(self, *v: Any) -> bytes: ...
    # TODO buffer type
    def pack_into(self, buffer: Any, offset: int, *v: Any) -> None: ...
    # TODO buffer type
    def unpack(self, buffer: Any) -> Tuple[Any, ...]: ...
    def unpack_from(self, buffer: Any, offset: int = ...) -> Tuple[Any, ...]: ...
