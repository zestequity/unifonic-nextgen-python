from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset





T = TypeVar("T", bound="SendWrapperresponse")

@attr.s(auto_attribs=True)
class SendWrapperresponse:
    """Sends message to one or more recipients.

    Example:
        {'Error': '0', 'MessageID': '3200017901931'}

    Attributes:
        error (str): The default error code Example: 0.
        message_id (str): A unique ID that identifies a message Example: 3200017901931.
    """

    error: str
    message_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        message_id = self.message_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "Error": error,
            "MessageID": message_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("Error")

        message_id = d.pop("MessageID")

        send_wrapperresponse = cls(
            error=error,
            message_id=message_id,
        )

        send_wrapperresponse.additional_properties = d
        return send_wrapperresponse

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
