from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast
from typing import Dict
from ..models.get_messages_detailsresponse_data import GetMessagesDetailsresponseData




T = TypeVar("T", bound="GetMessagesDetailsresponse")

@attr.s(auto_attribs=True)
class GetMessagesDetailsresponse:
    """Gets details of messages with optional filters. Returns paginated messages, next page or previous page

    Example:
        {'success': True, 'message': '', 'errorCode': 'ER-00', 'data': {'messages': [{'MessageID': 3200017891896,
            'CorrelationID': '', 'Status': 'Sent', 'MessageBody': 'test', 'Country': 'World', 'DLR': 'Sent',
            'NumberOfUnits': 0, 'Cost': 0, 'SenderID': 'sender', 'Recipient': '966505980169', 'DateCreated': '2018-05-14
            08:20:25.580', 'DateSent': '2018-05-14 08:20:25.621'}], 'CurrencyCode': '', 'TotalTextMessages': 1, 'Next': '',
            'Prev': ''}}

    Attributes:
        success (bool): The request sent successfully Example: True.
        message (str): The Error message if its false, Null if its true Example: {'message': ''}.
        error_code (str): the error code if there is any Example: {'errorCode': 'ER-00'}.
        data (GetMessagesDetailsresponseData): Message id, Time created, correlation id., status, number of units, cost,
            balance, Recipient
    """

    success: bool
    message: str
    error_code: str
    data: GetMessagesDetailsresponseData
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        success = self.success
        message = self.message
        error_code = self.error_code
        data = self.data.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "message": message,
            "errorCode": error_code,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        success = d.pop("success")

        message = d.pop("message")

        error_code = d.pop("errorCode")

        data = GetMessagesDetailsresponseData.from_dict(d.pop("data"))




        get_messages_detailsresponse = cls(
            success=success,
            message=message,
            error_code=error_code,
            data=data,
        )

        get_messages_detailsresponse.additional_properties = d
        return get_messages_detailsresponse

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
