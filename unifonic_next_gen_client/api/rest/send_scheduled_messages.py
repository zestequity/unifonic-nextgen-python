from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...types import UNSET, Unset
from typing import Optional
from typing import cast
from typing import Union
from typing import Dict
from ...models.sendscheduledmessagesresponse import Sendscheduledmessagesresponse



def _get_kwargs(
    *,
    client: Client,
    app_sid: str,
    sender_id: str,
    recipient: int,
    body: str,
    time_scheduled: str,
    response_type: Union[Unset, None, str] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Dict[str, Any]:
    url = "{}/rest/SMS/messages/scheduledmessages".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["AppSid"] = app_sid


    params["SenderID"] = sender_id


    params["Recipient"] = recipient


    params["Body"] = body


    params["TimeScheduled"] = time_scheduled


    params["responseType"] = response_type


    params["CorrelationID"] = correlation_id


    params["baseEncode"] = base_encode



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Sendscheduledmessagesresponse]]:
    if response.status_code == 200:
        response_200 = Sendscheduledmessagesresponse.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, response.json())
        return response_401
    if response.status_code == 406:
        response_406 = cast(Any, response.json())
        return response_406
    if response.status_code == 449:
        response_449 = cast(Any, response.json())
        return response_449
    if response.status_code == 451:
        response_451 = cast(Any, response.json())
        return response_451
    if response.status_code == 480:
        response_480 = cast(Any, response.json())
        return response_480
    if response.status_code == 482:
        response_482 = cast(Any, response.json())
        return response_482
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Sendscheduledmessagesresponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    app_sid: str,
    sender_id: str,
    recipient: int,
    body: str,
    time_scheduled: str,
    response_type: Union[Unset, None, str] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Response[Union[Any, Sendscheduledmessagesresponse]]:
    """Send Scheduled Messages

     Unifonic Send Scheduled API allows you to schedule text messages to users around the globe through
    simple RESTful API to be sent in future.

    Args:
        app_sid (str):  Example: Use your own AppSid.
        sender_id (str):  Example: sender.
        recipient (int):  Example: 966505980169.
        body (str):  Example: Test.
        time_scheduled (str):  Example: Sun, 12 Apr 2020 11:53:00 GMT.
        response_type (Union[Unset, None, str]):  Example: Json.
        correlation_id (Union[Unset, None, str]):  Example: CorrelationID.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, Sendscheduledmessagesresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
app_sid=app_sid,
sender_id=sender_id,
recipient=recipient,
body=body,
time_scheduled=time_scheduled,
response_type=response_type,
correlation_id=correlation_id,
base_encode=base_encode,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    app_sid: str,
    sender_id: str,
    recipient: int,
    body: str,
    time_scheduled: str,
    response_type: Union[Unset, None, str] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Optional[Union[Any, Sendscheduledmessagesresponse]]:
    """Send Scheduled Messages

     Unifonic Send Scheduled API allows you to schedule text messages to users around the globe through
    simple RESTful API to be sent in future.

    Args:
        app_sid (str):  Example: Use your own AppSid.
        sender_id (str):  Example: sender.
        recipient (int):  Example: 966505980169.
        body (str):  Example: Test.
        time_scheduled (str):  Example: Sun, 12 Apr 2020 11:53:00 GMT.
        response_type (Union[Unset, None, str]):  Example: Json.
        correlation_id (Union[Unset, None, str]):  Example: CorrelationID.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, Sendscheduledmessagesresponse]]
    """


    return sync_detailed(
        client=client,
app_sid=app_sid,
sender_id=sender_id,
recipient=recipient,
body=body,
time_scheduled=time_scheduled,
response_type=response_type,
correlation_id=correlation_id,
base_encode=base_encode,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    app_sid: str,
    sender_id: str,
    recipient: int,
    body: str,
    time_scheduled: str,
    response_type: Union[Unset, None, str] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Response[Union[Any, Sendscheduledmessagesresponse]]:
    """Send Scheduled Messages

     Unifonic Send Scheduled API allows you to schedule text messages to users around the globe through
    simple RESTful API to be sent in future.

    Args:
        app_sid (str):  Example: Use your own AppSid.
        sender_id (str):  Example: sender.
        recipient (int):  Example: 966505980169.
        body (str):  Example: Test.
        time_scheduled (str):  Example: Sun, 12 Apr 2020 11:53:00 GMT.
        response_type (Union[Unset, None, str]):  Example: Json.
        correlation_id (Union[Unset, None, str]):  Example: CorrelationID.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, Sendscheduledmessagesresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
app_sid=app_sid,
sender_id=sender_id,
recipient=recipient,
body=body,
time_scheduled=time_scheduled,
response_type=response_type,
correlation_id=correlation_id,
base_encode=base_encode,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    app_sid: str,
    sender_id: str,
    recipient: int,
    body: str,
    time_scheduled: str,
    response_type: Union[Unset, None, str] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Optional[Union[Any, Sendscheduledmessagesresponse]]:
    """Send Scheduled Messages

     Unifonic Send Scheduled API allows you to schedule text messages to users around the globe through
    simple RESTful API to be sent in future.

    Args:
        app_sid (str):  Example: Use your own AppSid.
        sender_id (str):  Example: sender.
        recipient (int):  Example: 966505980169.
        body (str):  Example: Test.
        time_scheduled (str):  Example: Sun, 12 Apr 2020 11:53:00 GMT.
        response_type (Union[Unset, None, str]):  Example: Json.
        correlation_id (Union[Unset, None, str]):  Example: CorrelationID.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, Sendscheduledmessagesresponse]]
    """


    return (await asyncio_detailed(
        client=client,
app_sid=app_sid,
sender_id=sender_id,
recipient=recipient,
body=body,
time_scheduled=time_scheduled,
response_type=response_type,
correlation_id=correlation_id,
base_encode=base_encode,

    )).parsed
