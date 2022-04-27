from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset





T = TypeVar("T", bound="GetMessageQueryresponse")

@attr.s(auto_attribs=True)
class GetMessageQueryresponse:
    """Gets details of specified message

    Example:
        {'STATUS05': 'The message has been sent successfully'}

    Attributes:
        status05 (str): The message statues Example: "The message has been sent successfully".
    """

    status05: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        status05 = self.status05

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "STATUS05": status05,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status05 = d.pop("STATUS05")

        get_message_queryresponse = cls(
            status05=status05,
        )

        get_message_queryresponse.additional_properties = d
        return get_message_queryresponse

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
