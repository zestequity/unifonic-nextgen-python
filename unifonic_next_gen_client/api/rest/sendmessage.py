from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...types import UNSET, Unset
from typing import Optional
from typing import cast
from typing import Union
from ...models.sendresponse import Sendresponse
from typing import Dict



def _get_kwargs(
    *,
    client: Client,
    app_sid: str,
    sender_id: str,
    body: str,
    recipient: int,
    response_type: Union[Unset, None, str] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,
    status_callback: Union[Unset, None, str] = UNSET,
    async_: Union[Unset, None, bool] = False,

) -> Dict[str, Any]:
    url = "{}/rest/SMS/messages".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["AppSid"] = app_sid


    params["SenderID"] = sender_id


    params["Body"] = body


    params["Recipient"] = recipient


    params["responseType"] = response_type


    params["CorrelationID"] = correlation_id


    params["baseEncode"] = base_encode


    params["statusCallback"] = status_callback


    params["async"] = async_



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Sendresponse]]:
    if response.status_code == 200:
        response_200 = Sendresponse.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, response.json())
        return response_401
    if response.status_code == 449:
        response_449 = cast(Any, response.json())
        return response_449
    if response.status_code == 480:
        response_480 = cast(Any, response.json())
        return response_480
    if response.status_code == 482:
        response_482 = cast(Any, response.json())
        return response_482
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Sendresponse]]:
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
    body: str,
    recipient: int,
    response_type: Union[Unset, None, str] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,
    status_callback: Union[Unset, None, str] = UNSET,
    async_: Union[Unset, None, bool] = False,

) -> Response[Union[Any, Sendresponse]]:
    """Send message

     Unifonic Send API allows you to send  text messages to users around the globe through simple RESTful
    APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.
        sender_id (str):  Example: sender.
        body (str):  Example: Test.
        recipient (int):  Example: 966505980169.
        response_type (Union[Unset, None, str]):  Example: JSON.
        correlation_id (Union[Unset, None, str]):  Example: CorrelationID.
        base_encode (Union[Unset, None, bool]):  Example: True.
        status_callback (Union[Unset, None, str]):  Example: sent.
        async_ (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Sendresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
app_sid=app_sid,
sender_id=sender_id,
body=body,
recipient=recipient,
response_type=response_type,
correlation_id=correlation_id,
base_encode=base_encode,
status_callback=status_callback,
async_=async_,

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
    body: str,
    recipient: int,
    response_type: Union[Unset, None, str] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,
    status_callback: Union[Unset, None, str] = UNSET,
    async_: Union[Unset, None, bool] = False,

) -> Optional[Union[Any, Sendresponse]]:
    """Send message

     Unifonic Send API allows you to send  text messages to users around the globe through simple RESTful
    APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.
        sender_id (str):  Example: sender.
        body (str):  Example: Test.
        recipient (int):  Example: 966505980169.
        response_type (Union[Unset, None, str]):  Example: JSON.
        correlation_id (Union[Unset, None, str]):  Example: CorrelationID.
        base_encode (Union[Unset, None, bool]):  Example: True.
        status_callback (Union[Unset, None, str]):  Example: sent.
        async_ (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Sendresponse]]
    """


    return sync_detailed(
        client=client,
app_sid=app_sid,
sender_id=sender_id,
body=body,
recipient=recipient,
response_type=response_type,
correlation_id=correlation_id,
base_encode=base_encode,
status_callback=status_callback,
async_=async_,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    app_sid: str,
    sender_id: str,
    body: str,
    recipient: int,
    response_type: Union[Unset, None, str] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,
    status_callback: Union[Unset, None, str] = UNSET,
    async_: Union[Unset, None, bool] = False,

) -> Response[Union[Any, Sendresponse]]:
    """Send message

     Unifonic Send API allows you to send  text messages to users around the globe through simple RESTful
    APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.
        sender_id (str):  Example: sender.
        body (str):  Example: Test.
        recipient (int):  Example: 966505980169.
        response_type (Union[Unset, None, str]):  Example: JSON.
        correlation_id (Union[Unset, None, str]):  Example: CorrelationID.
        base_encode (Union[Unset, None, bool]):  Example: True.
        status_callback (Union[Unset, None, str]):  Example: sent.
        async_ (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Sendresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
app_sid=app_sid,
sender_id=sender_id,
body=body,
recipient=recipient,
response_type=response_type,
correlation_id=correlation_id,
base_encode=base_encode,
status_callback=status_callback,
async_=async_,

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
    body: str,
    recipient: int,
    response_type: Union[Unset, None, str] = UNSET,
    correlation_id: Union[Unset, None, str] = UNSET,
    base_encode: Union[Unset, None, bool] = UNSET,
    status_callback: Union[Unset, None, str] = UNSET,
    async_: Union[Unset, None, bool] = False,

) -> Optional[Union[Any, Sendresponse]]:
    """Send message

     Unifonic Send API allows you to send  text messages to users around the globe through simple RESTful
    APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.
        sender_id (str):  Example: sender.
        body (str):  Example: Test.
        recipient (int):  Example: 966505980169.
        response_type (Union[Unset, None, str]):  Example: JSON.
        correlation_id (Union[Unset, None, str]):  Example: CorrelationID.
        base_encode (Union[Unset, None, bool]):  Example: True.
        status_callback (Union[Unset, None, str]):  Example: sent.
        async_ (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Sendresponse]]
    """


    return (await asyncio_detailed(
        client=client,
app_sid=app_sid,
sender_id=sender_id,
body=body,
recipient=recipient,
response_type=response_type,
correlation_id=correlation_id,
base_encode=base_encode,
status_callback=status_callback,
async_=async_,

    )).parsed
