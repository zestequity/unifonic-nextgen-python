from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.get_scheduled_messageresponse import GetScheduledMessageresponse
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    client: Client,
    app_sid: str,

) -> Dict[str, Any]:
    url = "{}/rest/SMS/messages/scheduledmessages".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["AppSid"] = app_sid



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetScheduledMessageresponse]]:
    if response.status_code == 200:
        response_200 = GetScheduledMessageresponse.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, response.json())
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetScheduledMessageresponse]]:
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

) -> Response[Union[Any, GetScheduledMessageresponse]]:
    """Scheduled Message Details

     Unifonic Scheduled message details allows you to get details of scheduled messages through simple
    RESTful APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.

    Returns:
        Response[Union[Any, GetScheduledMessageresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
app_sid=app_sid,

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

) -> Optional[Union[Any, GetScheduledMessageresponse]]:
    """Scheduled Message Details

     Unifonic Scheduled message details allows you to get details of scheduled messages through simple
    RESTful APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.

    Returns:
        Response[Union[Any, GetScheduledMessageresponse]]
    """


    return sync_detailed(
        client=client,
app_sid=app_sid,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    app_sid: str,

) -> Response[Union[Any, GetScheduledMessageresponse]]:
    """Scheduled Message Details

     Unifonic Scheduled message details allows you to get details of scheduled messages through simple
    RESTful APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.

    Returns:
        Response[Union[Any, GetScheduledMessageresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
app_sid=app_sid,

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

) -> Optional[Union[Any, GetScheduledMessageresponse]]:
    """Scheduled Message Details

     Unifonic Scheduled message details allows you to get details of scheduled messages through simple
    RESTful APIs

    Args:
        app_sid (str):  Example: Use your own AppSid.

    Returns:
        Response[Union[Any, GetScheduledMessageresponse]]
    """


    return (await asyncio_detailed(
        client=client,
app_sid=app_sid,

    )).parsed
