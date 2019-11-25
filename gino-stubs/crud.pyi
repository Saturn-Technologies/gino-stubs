from .api import GinoExecutor
from .declarative import Model, InvertDict
from .exceptions import NoSuchRowError
from .loader import AliasLoader, ModelLoader
from .engine import GinoEngine
from typing import (
    Any,
    Optional,
    Dict,
    Iterator,
    ClassVar,
    TypeVar,
    Type,
    Generic,
    overload,
)
from typing_extensions import Protocol, Final
from sqlalchemy.sql.dml import Update as _SAUpdate, Delete as _SADelete
from sqlalchemy.sql.selectable import Select as _SASelect, Alias as _SAAlias
from sqlalchemy.sql.elements import BooleanClauseList
from sqlalchemy.sql.schema import Column as _SAColumn

DEFAULT: Final[Any]

_T_co = TypeVar('_T_co', covariant=True)
_CM = TypeVar('_CM', bound=CRUDModel)

class _CreateWithoutInstance(Protocol[_T_co]):
    async def __call__(
        self, bind: Optional[GinoEngine] = ..., timeout: int = ..., **values: Any
    ) -> _T_co: ...

class _CreateWithInstance(Protocol[_T_co]):
    async def __call__(
        self, bind: Optional[GinoEngine] = ..., timeout: int = ...
    ) -> _T_co: ...

class _Create:
    @overload
    def __get__(
        self, instance: None, owner: Type[_CM]
    ) -> _CreateWithoutInstance[_CM]: ...
    @overload
    def __get__(self, instance: _CM, owner: Any) -> _CreateWithInstance[_CM]: ...

class _GinoSelect(_SASelect, Generic[_CM]):
    gino: GinoExecutor[_CM]

class _Query:
    @overload
    def __get__(self, instance: None, owner: Type[_CM]) -> _GinoSelect[_CM]: ...
    @overload
    def __get__(self, instance: _CM, owner: Any) -> _GinoSelect[_CM]: ...

class _SelectMethod(Protocol[_CM]):
    def __call__(self, *args: Any) -> _GinoSelect[_CM]: ...

class _Select:
    @overload
    def __get__(self, instance: None, owner: Type[_CM]) -> _SelectMethod[_CM]: ...
    @overload
    def __get__(self, instance: _CM, owner: Any) -> _SelectMethod[_CM]: ...

class _UpdateWithInstance(Protocol[_CM]):
    def __call__(self, **values: Any) -> UpdateRequest[_CM]: ...

class _GinoUpdate(_SAUpdate, Generic[_CM]):
    gino: GinoExecutor[_CM]

class _Update:
    @overload
    def __get__(self, instance: None, owner: Type[_CM]) -> _GinoUpdate[_CM]: ...
    @overload
    def __get__(self, instance: _CM, owner: Any) -> _UpdateWithInstance[_CM]: ...

class _DeleteWithInstance(Protocol):
    async def __call__(
        self, bind: Optional[GinoEngine] = ..., timeout: int = ...
    ) -> int: ...

class _GinoDelete(_SADelete, Generic[_CM]):
    gino: GinoExecutor[_CM]

class _Delete:
    @overload
    def __get__(self, instance: None, owner: Type[_CM]) -> _GinoDelete[_CM]: ...
    @overload
    def __get__(self, instance: _CM, owner: Any) -> _DeleteWithInstance: ...

class UpdateRequest(Generic[_CM]):
    _UR = TypeVar('_UR', bound='UpdateRequest[_CM]')
    async def apply(
        self: '_UR', bind: Optional[GinoEngine] = ..., timeout: int = ...
    ) -> '_UR': ...
    def update(self: '_UR', **values: Any) -> '_UR': ...

class Alias:
    model: Any = ...
    alias: _SAAlias = ...
    def __init__(
        self, model: Any, name: Optional[str] = ..., flat: bool = ...
    ) -> None: ...
    def __getattr__(self, item: Any) -> Any: ...
    def __iter__(self) -> Iterator[_SAColumn[Any]]: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def load(self, *column_names: Any, **relationships: Any) -> AliasLoader[Any]: ...
    def on(self, on_clause: Any) -> AliasLoader[Any]: ...

class CRUDModel(Model):
    create: ClassVar[_Create] = ...
    query: ClassVar[_Query] = ...
    update: ClassVar[_Update] = ...
    delete: ClassVar[_Delete] = ...
    select: ClassVar[_Select] = ...
    __profile__: Any = ...
    def __init__(self, **values: Any) -> None: ...
    @classmethod
    async def get(
        cls: Type[_CM], ident: Any, bind: Optional[GinoEngine] = ..., timeout: int = ...
    ) -> Optional[_CM]: ...
    def append_where_primary_key(
        self: _CM, q: _GinoSelect[_CM]
    ) -> _GinoSelect[_CM]: ...
    def lookup(self) -> BooleanClauseList: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def load(
        cls: Type[_CM], *column_names: Any, **relationships: Any
    ) -> ModelLoader[_CM]: ...
    @classmethod
    def on(cls: Type[_CM], on_clause: Any) -> ModelLoader[_CM]: ...
    @classmethod
    def distinct(cls: Type[_CM], *columns: Any) -> ModelLoader[_CM]: ...
    @classmethod
    def none_as_none(cls: Type[_CM], enabled: bool = ...) -> ModelLoader[_CM]: ...
    @classmethod
    def alias(
        cls, model: Any, name: Optional[str] = ..., flat: bool = ...
    ) -> Alias: ...
    @classmethod
    def in_query(cls, query: Any) -> Any: ...
