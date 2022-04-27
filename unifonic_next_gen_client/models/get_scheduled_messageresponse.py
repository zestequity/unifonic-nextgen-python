from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast
from typing import Dict
from ..models.get_scheduled_messageresponse_data import GetScheduledMessageresponseData




T = TypeVar("T", bound="GetScheduledMessageresponse")

@attr.s(auto_attribs=True)
class GetScheduledMessageresponse:
    """GetsDetails of specified scheduled message, If MessageID is specified, only one message is returned,Otherwise all
messages(paginated) are queried.

    Example:
        {'success': True, 'message': '', 'errorCode': 'ER-00', 'data': {'messages': [{'MessageID': 3200017891899,
            'Status': 'Stopped', 'MessageBody': 'Test', 'SenderID': 'sender', 'Recipient': '966505980169', 'DateCreated':
            '2018-05-14 08:24:20.051', 'TimeScheduled': '2020-04-12 11:50:00'}, {'MessageID': 3200017891882, 'Status':
            'Stopped', 'MessageBody': 'Test', 'SenderID': 'sender', 'Recipient': '966505980169', 'DateCreated': '2018-05-14
            08:04:32.604', 'TimeScheduled': '2020-04-12 11:50:00'}, {'MessageID': 3200017891543, 'Status': 'Rejected',
            'MessageBody': 'Body6', 'SenderID': '', 'Recipient': '', 'DateCreated': '2018-05-13 09:11:16.450',
            'TimeScheduled': ''}, {'MessageID': 3200017891541, 'Status': 'Stopped', 'MessageBody': 'success4', 'SenderID':
            'AltSender', 'Recipient': '966555696176', 'DateCreated': '2018-05-13 09:09:49.876', 'TimeScheduled': '2018-09-22
            11:46:00'}, {'MessageID': 3200017891540, 'Status': 'Rejected', 'MessageBody': 'success4', 'SenderID': '',
            'Recipient': '', 'DateCreated': '2018-05-13 09:09:40.891', 'TimeScheduled': ''}, {'MessageID': 3200017891537,
            'Status': 'Rejected', 'MessageBody': 'success4', 'SenderID': '', 'Recipient': '', 'DateCreated': '2018-05-13
            09:03:12.833', 'TimeScheduled': ''}, {'MessageID': 3200017891536, 'Status': 'Stopped', 'MessageBody':
            'success4', 'SenderID': 'sender', 'Recipient': '966555696176', 'DateCreated': '2018-05-13 09:03:03.145',
            'TimeScheduled': '2018-09-22 11:46:00'}, {'MessageID': 3200017891535, 'Status': 'Stopped', 'MessageBody':
            'Body6', 'SenderID': 'AltSender', 'Recipient': '966505980169', 'DateCreated': '2018-05-13 09:01:36.155',
            'TimeScheduled': '2020-04-12 11:53:00'}, {'MessageID': 3200017891530, 'Status': 'Rejected', 'MessageBody':
            'h545454', 'SenderID': '', 'Recipient': '', 'DateCreated': '2018-05-13 08:53:40.551', 'TimeScheduled': ''},
            {'MessageID': 3200017891529, 'Status': 'Rejected', 'MessageBody': 'h', 'SenderID': '', 'Recipient': '',
            'DateCreated': '2018-05-13 08:51:04.005', 'TimeScheduled': ''}, {'MessageID': 3200017891527, 'Status':
            'Stopped', 'MessageBody': 'h', 'SenderID': 'AltSender', 'Recipient': '966505980169', 'DateCreated': '2018-05-13
            08:48:48.225', 'TimeScheduled': '2023-12-07 03:04:00'}, {'MessageID': 3200017891523, 'Status': 'Rejected',
            'MessageBody': 'h', 'SenderID': '', 'Recipient': '', 'DateCreated': '2018-05-13 08:47:53.420', 'TimeScheduled':
            ''}, {'MessageID': 3200017891522, 'Status': 'Rejected', 'MessageBody': '', 'SenderID': '', 'Recipient': '',
            'DateCreated': '2018-05-13 08:46:52.311', 'TimeScheduled': ''}, {'MessageID': 3200017891501, 'Status':
            'Stopped', 'MessageBody': 'Body6', 'SenderID': 'AltSender', 'Recipient': '966505980169', 'DateCreated':
            '2018-05-13 08:15:12.055', 'TimeScheduled': '2020-04-12 11:53:00'}, {'MessageID': 3200017891500, 'Status':
            'Stopped', 'MessageBody': 'Body6', 'SenderID': 'AltSender', 'Recipient': '966505980169', 'DateCreated':
            '2018-05-13 08:12:52.369', 'TimeScheduled': '2020-04-12 11:53:00'}, {'MessageID': 3200017891496, 'Status':
            'Rejected', 'MessageBody': 'Team', 'SenderID': '', 'Recipient': '', 'DateCreated': '2018-05-13 08:10:53.740',
            'TimeScheduled': ''}, {'MessageID': 3200017891495, 'Status': 'Rejected', 'MessageBody': '', 'SenderID': '',
            'Recipient': '', 'DateCreated': '2018-05-13 08:10:48.342', 'TimeScheduled': ''}, {'MessageID': 3200017891494,
            'Status': 'Stopped', 'MessageBody': 'Body6', 'SenderID': 'AltSender', 'Recipient': '966505980169',
            'DateCreated': '2018-05-13 08:08:27.709', 'TimeScheduled': '2020-04-12 11:53:00'}, {'MessageID': 3200017891493,
            'Status': 'Rejected', 'MessageBody': 'Body6', 'SenderID': '', 'Recipient': '', 'DateCreated': '2018-05-13
            08:08:18.874', 'TimeScheduled': ''}, {'MessageID': 3200017891492, 'Status': 'Stopped', 'MessageBody': 'Body6',
            'SenderID': 'AltSender', 'Recipient': '966505980169', 'DateCreated': '2018-05-13 08:07:31.727', 'TimeScheduled':
            '2020-04-12 11:53:00'}], 'TotalTextMessages': 20, 'Next': 'http://basic.unifonic.com/rest/SMS/2017-08-
            01/messages/scheduledmessages?AppSid=6v253153s1g7831s5&beforeSid=966505980169,7,AltSender,3200017891492,,2018-
            05-13%2008:07:31.727&Limit=20', 'Prev': ''}}

    Attributes:
        success (bool): The request sent successfully Example: True.
        message (str): The Error message if its false, Null if its true Example: {'message': ''}.
        error_code (str): the error code if there is any Example: {'errorCode': 'ER-00'}.
        data (GetScheduledMessageresponseData): Message id, Time created, correlation id., status, number of units,
            cost, balance, Recipient
    """

    success: bool
    message: str
    error_code: str
    data: GetScheduledMessageresponseData
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

        data = GetScheduledMessageresponseData.from_dict(d.pop("data"))




        get_scheduled_messageresponse = cls(
            success=success,
            message=message,
            error_code=error_code,
            data=data,
        )

        get_scheduled_messageresponse.additional_properties = d
        return get_scheduled_messageresponse

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
