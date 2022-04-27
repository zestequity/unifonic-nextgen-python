from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset





T = TypeVar("T", bound="Sendscheduledmessagesresponse")

@attr.s(auto_attribs=True)
class Sendscheduledmessagesresponse:
    """Schedules one message to be sent in the future.

    Example:
        {'success': True, 'message': '', 'errorCode': 'ER-00', 'Status': 'Accepted'}

    Attributes:
        success (bool): The request sent successfully Example: True.
        message (str): The Error message if its false, Null if its true Example: {'message': 'Missing parameter
            AppSid'}.
        error_code (str): The error code if there is any Example: {'errorCode': 'ER-02'}.
        status (str): Accepted or Rejected Example: {'Status': 'Rejected'}.
    """

    success: bool
    message: str
    error_code: str
    status: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        success = self.success
        message = self.message
        error_code = self.error_code
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "message": message,
            "errorCode": error_code,
            "Status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        success = d.pop("success")

        message = d.pop("message")

        error_code = d.pop("errorCode")

        status = d.pop("Status")

        sendscheduledmessagesresponse = cls(
            success=success,
            message=message,
            error_code=error_code,
            status=status,
        )

        sendscheduledmessagesresponse.additional_properties = d
        return sendscheduledmessagesresponse

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
