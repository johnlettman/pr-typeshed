# Stubs for collections

# Based on http://docs.python.org/2.7/library/collections.html

# TODO more abstract base classes (interfaces in mypy)

# NOTE: These are incomplete!

from typing import (
    Any, Dict, Generic, TypeVar, Iterable, Tuple, Callable, Mapping, overload, Iterator,
    Sized, Optional, List, Set, Sequence, Union, Reversible, MutableMapping, MutableSequence
)
import typing

_T = TypeVar('_T')
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

# namedtuple is special-cased in the type checker; the initializer is ignored.
namedtuple = ...  # type: Any

class deque(Sized, Iterable[_T], Reversible[_T], Generic[_T]):
    def __init__(self, iterable: Iterable[_T] = ...,
                 maxlen: int = ...) -> None: ...
    @property
    def maxlen(self) -> Optional[int]: ...
    def append(self, x: _T) -> None: ...
    def appendleft(self, x: _T) -> None: ...
    def clear(self) -> None: ...
    def count(self, x: _T) -> int: ...
    def extend(self, iterable: Iterable[_T]) -> None: ...
    def extendleft(self, iterable: Iterable[_T]) -> None: ...
    def pop(self) -> _T: ...
    def popleft(self) -> _T: ...
    def remove(self, value: _T) -> None: ...
    def reverse(self) -> None: ...
    def rotate(self, n: int) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __str__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __getitem__(self, i: int) -> _T: ...
    def __setitem__(self, i: int, x: _T) -> None: ...
    def __contains__(self, o: _T) -> bool: ...
    def __reversed__(self) -> Iterator[_T]: ...

class Counter(Dict[_T, int], Generic[_T]):
    # TODO: __init__ keyword arguments
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Mapping: Mapping[_T, int]) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[_T]) -> None: ...
    def elements(self) -> Iterator[_T]: ...
    def most_common(self, n: int = ...) -> List[_T]: ...
    @overload
    def subtract(self, mapping: Mapping[_T, int]) -> None: ...
    @overload
    def subtract(self, iterable: Iterable[_T]) -> None: ...
    # The Iterable[Tuple[...]] argument type is not actually desirable
    # (the tuples will be added as keys, breaking type safety) but
    # it's included so that the signature is compatible with
    # Dict.update. Not sure if we should use '# type: ignore' instead
    # and omit the type from the union.
    @overload
    def update(self, m: Mapping[_T, int], **kwargs: _VT) -> None: ...
    @overload
    def update(self, m: Union[Iterable[_T], Iterable[Tuple[_T, int]]], **kwargs: _VT) -> None: ...

class OrderedDict(Dict[_KT, _VT], Generic[_KT, _VT]):
    def popitem(self, last: bool = ...) -> Tuple[_KT, _VT]: ...
    def move_to_end(self, key: _KT, last: bool = ...) -> None: ...

class defaultdict(Dict[_KT, _VT], Generic[_KT, _VT]):
    default_factory = ...  # type: Callable[[], _VT]
    # TODO: __init__ keyword args
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, map: Mapping[_KT, _VT]) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[Tuple[_KT, _VT]]) -> None: ...
    @overload
    def __init__(self, default_factory: Callable[[], _VT]) -> None: ...
    @overload
    def __init__(self, default_factory: Callable[[], _VT],
                 map: Mapping[_KT, _VT]) -> None: ...
    @overload
    def __init__(self, default_factory: Callable[[], _VT],
                 iterable: Iterable[Tuple[_KT, _VT]]) -> None: ...
    def __missing__(self, key: _KT) -> _VT: ...
