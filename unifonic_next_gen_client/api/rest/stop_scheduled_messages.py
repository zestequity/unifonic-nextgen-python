from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...types import UNSET, Unset
from typing import Optional
from ...models.stop_scheduled_messagesresponse import StopScheduledMessagesresponse
from typing import cast
from typing import Union
from typing import Dict



def _get_kwargs(
    *,
    client: Client,
    app_sid: str,
    message_id: Union[Unset, None, int] = UNSET,
    response_format: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Dict[str, Any]:
    url = "{}/rest/SMS/messages/scheduledmessages".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["AppSid"] = app_sid


    params["MessageID"] = message_id


    params["responseFormat"] = response_format


    params["baseEncode"] = base_encode



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StopScheduledMessagesresponse]]:
    if response.status_code == 200:
        response_200 = StopScheduledMessagesresponse.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, response.json())
        return response_401
    if response.status_code == 455:
        response_455 = cast(Any, response.json())
        return response_455
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StopScheduledMessagesresponse]]:
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
    message_id: Union[Unset, None, int] = UNSET,
    response_format: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Response[Union[Any, StopScheduledMessagesresponse]]:
    """Stop Scheduled Messages

     Unifonic Stop scheduled messages API allows you to Delete (Stops) scheduled message,If MessageID is
    specified only one message is stopped, Otherwise all messages are stopped through simple RESTful
    APIs.

    Args:
        app_sid (str):  Example: Use your own AppSid.
        message_id (Union[Unset, None, int]):  Example: 3200017891896.
        response_format (Union[Unset, None, str]):  Example: json.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, StopScheduledMessagesresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
app_sid=app_sid,
message_id=message_id,
response_format=response_format,
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
    message_id: Union[Unset, None, int] = UNSET,
    response_format: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Optional[Union[Any, StopScheduledMessagesresponse]]:
    """Stop Scheduled Messages

     Unifonic Stop scheduled messages API allows you to Delete (Stops) scheduled message,If MessageID is
    specified only one message is stopped, Otherwise all messages are stopped through simple RESTful
    APIs.

    Args:
        app_sid (str):  Example: Use your own AppSid.
        message_id (Union[Unset, None, int]):  Example: 3200017891896.
        response_format (Union[Unset, None, str]):  Example: json.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, StopScheduledMessagesresponse]]
    """


    return sync_detailed(
        client=client,
app_sid=app_sid,
message_id=message_id,
response_format=response_format,
base_encode=base_encode,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    app_sid: str,
    message_id: Union[Unset, None, int] = UNSET,
    response_format: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Response[Union[Any, StopScheduledMessagesresponse]]:
    """Stop Scheduled Messages

     Unifonic Stop scheduled messages API allows you to Delete (Stops) scheduled message,If MessageID is
    specified only one message is stopped, Otherwise all messages are stopped through simple RESTful
    APIs.

    Args:
        app_sid (str):  Example: Use your own AppSid.
        message_id (Union[Unset, None, int]):  Example: 3200017891896.
        response_format (Union[Unset, None, str]):  Example: json.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, StopScheduledMessagesresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
app_sid=app_sid,
message_id=message_id,
response_format=response_format,
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
    message_id: Union[Unset, None, int] = UNSET,
    response_format: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Optional[Union[Any, StopScheduledMessagesresponse]]:
    """Stop Scheduled Messages

     Unifonic Stop scheduled messages API allows you to Delete (Stops) scheduled message,If MessageID is
    specified only one message is stopped, Otherwise all messages are stopped through simple RESTful
    APIs.

    Args:
        app_sid (str):  Example: Use your own AppSid.
        message_id (Union[Unset, None, int]):  Example: 3200017891896.
        response_format (Union[Unset, None, str]):  Example: json.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, StopScheduledMessagesresponse]]
    """


    return (await asyncio_detailed(
        client=client,
app_sid=app_sid,
message_id=message_id,
response_format=response_format,
base_encode=base_encode,

    )).parsed
