from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

import datetime
from ...types import UNSET, Unset
from typing import Optional
from typing import Union
from typing import cast
from dateutil.parser import isoparse
from ...models.get_messages_detailsresponse import GetMessagesDetailsresponse
from typing import Dict



def _get_kwargs(
    *,
    client: Client,
    app_sid: str,
    message_id: Union[Unset, None, int] = UNSET,
    sender_id: Union[Unset, None, str] = UNSET,
    recipient: Union[Unset, None, int] = UNSET,
    date_from: Union[Unset, None, datetime.date] = UNSET,
    date_to: Union[Unset, None, datetime.date] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Dict[str, Any]:
    url = "{}/rest/SMS/Messages/GetMessagesDetails".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["AppSid"] = app_sid


    params["MessageID"] = message_id


    params["senderID"] = sender_id


    params["Recipient"] = recipient


    json_date_from: Union[Unset, None, str] = UNSET
    if not isinstance(date_from, Unset):
        json_date_from = date_from.isoformat() if date_from else None

    params["dateFrom"] = json_date_from


    json_date_to: Union[Unset, None, str] = UNSET
    if not isinstance(date_to, Unset):
        json_date_to = date_to.isoformat() if date_to else None

    params["dateTo"] = json_date_to


    params["CorrelationID"] = correlation_id


    params["Limit"] = limit


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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetMessagesDetailsresponse]]:
    if response.status_code == 200:
        response_200 = GetMessagesDetailsresponse.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, response.json())
        return response_401
    if response.status_code == 432:
        response_432 = cast(Any, response.json())
        return response_432
    if response.status_code == 599:
        response_599 = cast(Any, response.json())
        return response_599
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetMessagesDetailsresponse]]:
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
    sender_id: Union[Unset, None, str] = UNSET,
    recipient: Union[Unset, None, int] = UNSET,
    date_from: Union[Unset, None, datetime.date] = UNSET,
    date_to: Union[Unset, None, datetime.date] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Response[Union[Any, GetMessagesDetailsresponse]]:
    """Get Message Details

     Unifonic Get message details API allows you to get details of messages with optional filters,returns
    paginated messages, next page or previous page through simple RESTful APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.
        message_id (Union[Unset, None, int]):  Example: 3200017891630.
        sender_id (Union[Unset, None, str]):  Example: sender.
        recipient (Union[Unset, None, int]):  Example: 966505980169.
        date_from (Union[Unset, None, datetime.date]):  Example: 2018-04-12.
        date_to (Union[Unset, None, datetime.date]):  Example: 2018-05-12.
        correlation_id (Union[Unset, None, str]):  Example: CorrrelationID.
        limit (Union[Unset, None, int]):  Example: 20.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, GetMessagesDetailsresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
app_sid=app_sid,
message_id=message_id,
sender_id=sender_id,
recipient=recipient,
date_from=date_from,
date_to=date_to,
correlation_id=correlation_id,
limit=limit,
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
    sender_id: Union[Unset, None, str] = UNSET,
    recipient: Union[Unset, None, int] = UNSET,
    date_from: Union[Unset, None, datetime.date] = UNSET,
    date_to: Union[Unset, None, datetime.date] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Optional[Union[Any, GetMessagesDetailsresponse]]:
    """Get Message Details

     Unifonic Get message details API allows you to get details of messages with optional filters,returns
    paginated messages, next page or previous page through simple RESTful APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.
        message_id (Union[Unset, None, int]):  Example: 3200017891630.
        sender_id (Union[Unset, None, str]):  Example: sender.
        recipient (Union[Unset, None, int]):  Example: 966505980169.
        date_from (Union[Unset, None, datetime.date]):  Example: 2018-04-12.
        date_to (Union[Unset, None, datetime.date]):  Example: 2018-05-12.
        correlation_id (Union[Unset, None, str]):  Example: CorrrelationID.
        limit (Union[Unset, None, int]):  Example: 20.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, GetMessagesDetailsresponse]]
    """


    return sync_detailed(
        client=client,
app_sid=app_sid,
message_id=message_id,
sender_id=sender_id,
recipient=recipient,
date_from=date_from,
date_to=date_to,
correlation_id=correlation_id,
limit=limit,
base_encode=base_encode,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    app_sid: str,
    message_id: Union[Unset, None, int] = UNSET,
    sender_id: Union[Unset, None, str] = UNSET,
    recipient: Union[Unset, None, int] = UNSET,
    date_from: Union[Unset, None, datetime.date] = UNSET,
    date_to: Union[Unset, None, datetime.date] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Response[Union[Any, GetMessagesDetailsresponse]]:
    """Get Message Details

     Unifonic Get message details API allows you to get details of messages with optional filters,returns
    paginated messages, next page or previous page through simple RESTful APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.
        message_id (Union[Unset, None, int]):  Example: 3200017891630.
        sender_id (Union[Unset, None, str]):  Example: sender.
        recipient (Union[Unset, None, int]):  Example: 966505980169.
        date_from (Union[Unset, None, datetime.date]):  Example: 2018-04-12.
        date_to (Union[Unset, None, datetime.date]):  Example: 2018-05-12.
        correlation_id (Union[Unset, None, str]):  Example: CorrrelationID.
        limit (Union[Unset, None, int]):  Example: 20.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, GetMessagesDetailsresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
app_sid=app_sid,
message_id=message_id,
sender_id=sender_id,
recipient=recipient,
date_from=date_from,
date_to=date_to,
correlation_id=correlation_id,
limit=limit,
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
    sender_id: Union[Unset, None, str] = UNSET,
    recipient: Union[Unset, None, int] = UNSET,
    date_from: Union[Unset, None, datetime.date] = UNSET,
    date_to: Union[Unset, None, datetime.date] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,

) -> Optional[Union[Any, GetMessagesDetailsresponse]]:
    """Get Message Details

     Unifonic Get message details API allows you to get details of messages with optional filters,returns
    paginated messages, next page or previous page through simple RESTful APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.
        message_id (Union[Unset, None, int]):  Example: 3200017891630.
        sender_id (Union[Unset, None, str]):  Example: sender.
        recipient (Union[Unset, None, int]):  Example: 966505980169.
        date_from (Union[Unset, None, datetime.date]):  Example: 2018-04-12.
        date_to (Union[Unset, None, datetime.date]):  Example: 2018-05-12.
        correlation_id (Union[Unset, None, str]):  Example: CorrrelationID.
        limit (Union[Unset, None, int]):  Example: 20.
        base_encode (Union[Unset, None, bool]):  Example: True.

    Returns:
        Response[Union[Any, GetMessagesDetailsresponse]]
    """


    return (await asyncio_detailed(
        client=client,
app_sid=app_sid,
message_id=message_id,
sender_id=sender_id,
recipient=recipient,
date_from=date_from,
date_to=date_to,
correlation_id=correlation_id,
limit=limit,
base_encode=base_encode,

    )).parsed
