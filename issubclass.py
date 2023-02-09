import builtins
import importlib.metadata
from typing import TYPE_CHECKING, Tuple, Type, TypeVar, Union

__version__ = importlib.metadata.version("issubclass")

T = TypeVar("T", bound=Type[object])

if TYPE_CHECKING:
    issubclass = builtins.issubclass # pragma: no cover

else:

    def issubclass(cls: type, other: Union[T, Tuple[T, ...]]) -> bool:
        try:
            return builtins.issubclass(cls, other)
        except TypeError:
            return False
