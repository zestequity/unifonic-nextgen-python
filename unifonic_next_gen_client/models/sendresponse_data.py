from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset





T = TypeVar("T", bound="SendresponseData")

@attr.s(auto_attribs=True)
class SendresponseData:
    """Message id, Time created, correlation id., status, number of units, cost, balance, Recipient

    Example:
        {'success': True, 'message': '', 'errorCode': 'ER-00', 'data': {'MessageID': 2000000205103, 'CorrelationID': '',
            'Status': 'Queued', 'NumberOfUnits': 0, 'Cost': 0, 'Balance': 0, 'Recipient': '966505980169', 'TimeCreated':
            '2018-05-21 08:17:47.839', 'CurrencyCode': ''}}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sendresponse_data = cls(
        )

        sendresponse_data.additional_properties = d
        return sendresponse_data

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
