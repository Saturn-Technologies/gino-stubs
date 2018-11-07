# Stubs for gino.declarative (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import (
    Any,
    Optional,
    Union,
    TypeVar,
    Callable,
    Dict,
    Tuple,
    Type,
    Generic,
    TypeVar,
    Iterator,
    overload,
)
from sqlalchemy import MetaData, Column, Table
from collections import OrderedDict
from .schema import GinoSchemaVisitor

_FuncType = Callable[..., Any]
_F = TypeVar('_F', bound=_FuncType)
_T = TypeVar('_T')
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

class ColumnAttribute(Generic[_T]):
    prop_name: str = ...
    column: Column[_T] = ...
    def __init__(self, prop_name: str, column: Column[_T]) -> None: ...
    @overload
    def __get__(self, instance: None, owner: Any) -> Column[_T]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> _T: ...
    def __set__(self, instance: Any, value: _T) -> None: ...
    def __delete__(self, instance: Any) -> None: ...

class InvertDict(Dict[_KT, _VT]):
    @overload
    def invert_get(self, k: _VT) -> Optional[_KT]: ...
    @overload
    def invert_get(self, k: _VT, default: Union[_KT, _T]) -> Union[_KT, _T]: ...

class ModelType(type):
    def __iter__(cls) -> Iterator[Column[Any]]: ...
    def __getattr__(cls, item: Any) -> Any: ...
    @classmethod
    def __prepare__(
        metacls: Any, name: Any, bases: Any, **kwargs: Any
    ) -> OrderedDict[Any, Any]: ...
    def __new__(
        metacls: Any, name: Any, bases: Any, namespace: Any, **kwargs: Any
    ) -> Any: ...

def declared_attr(m: _F) -> _F: ...

class Model:
    __metadata__: MetaData = ...
    __table__: Table = ...
    __attr_factory__: Any = ...
    __values__: Dict[str, Any] = ...

    gino: GinoSchemaVisitor
    _column_name_map: InvertDict[str, str]
    def __init__(self) -> None: ...
    def insert(self, values=None, inline=False, **kwargs) -> Any: ...
    def join(self, right, onclause=None, isouter=False, full=False) -> Any: ...
    def outerjoin(self, right, onclause=None, full=False) -> Any: ...

def declarative_base(
    metadata: MetaData, model_classes: Tuple[Type[Any], ...] = ..., name: str = ...
) -> Any: ...
