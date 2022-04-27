from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast
from ..models.stop_scheduled_messagesresponse_data import StopScheduledMessagesresponseData
from typing import Dict




T = TypeVar("T", bound="StopScheduledMessagesresponse")

@attr.s(auto_attribs=True)
class StopScheduledMessagesresponse:
    """Delete (Stops) scheduled message,If MessageID is specified, only one message is stopped.  Otherwise all messages are
stopped

    Example:
        {'success': 'true', 'message': '', 'errorCode': 'ER-00', 'data': {}}

    Attributes:
        success (str): The request sent successfully Example: true.
        message (str): The Error message if its false, Null if its true Example: {'message': 'Missing parameter
            AppSid'}.
        error_code (str): Error Code if there is an error Example: {'errorCode': 'ER-02'}.
        data (StopScheduledMessagesresponseData): Message id, Time created, correlation id., status, number of units,
            cost, balance, Recipient Example: {'data': {}}.
    """

    success: str
    message: str
    error_code: str
    data: StopScheduledMessagesresponseData
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

        data = StopScheduledMessagesresponseData.from_dict(d.pop("data"))




        stop_scheduled_messagesresponse = cls(
            success=success,
            message=message,
            error_code=error_code,
            data=data,
        )

        stop_scheduled_messagesresponse.additional_properties = d
        return stop_scheduled_messagesresponse

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
