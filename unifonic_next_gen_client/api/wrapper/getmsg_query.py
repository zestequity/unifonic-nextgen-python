from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...types import UNSET, Unset
from typing import Optional
from typing import cast
from typing import Union
from ...models.get_message_queryresponse import GetMessageQueryresponse
from typing import Dict



def _get_kwargs(
    *,
    client: Client,
    appsid: str,
    msgid: int,
    to: Union[Unset, None, int] = UNSET,

) -> Dict[str, Any]:
    url = "{}/wrapper/msgQuery".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["appsid"] = appsid


    params["msgid"] = msgid


    params["to"] = to



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetMessageQueryresponse]]:
    if response.status_code == 200:
        response_200 = GetMessageQueryresponse.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, response.json())
        return response_401
    if response.status_code == 402:
        response_402 = cast(Any, response.json())
        return response_402
    if response.status_code == 432:
        response_432 = cast(Any, response.json())
        return response_432
    if response.status_code == 452:
        response_452 = cast(Any, response.json())
        return response_452
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetMessageQueryresponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    appsid: str,
    msgid: int,
    to: Union[Unset, None, int] = UNSET,

) -> Response[Union[Any, GetMessageQueryresponse]]:
    """Get msgQuery

     Unifonic Get message query API allows you to get details of specified message.

    Args:
        appsid (str):  Example:  Use your own appsid.
        msgid (int):  Example: 3200017901931.
        to (Union[Unset, None, int]):  Example: 966505980169.

    Returns:
        Response[Union[Any, GetMessageQueryresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
appsid=appsid,
msgid=msgid,
to=to,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    appsid: str,
    msgid: int,
    to: Union[Unset, None, int] = UNSET,

) -> Optional[Union[Any, GetMessageQueryresponse]]:
    """Get msgQuery

     Unifonic Get message query API allows you to get details of specified message.

    Args:
        appsid (str):  Example:  Use your own appsid.
        msgid (int):  Example: 3200017901931.
        to (Union[Unset, None, int]):  Example: 966505980169.

    Returns:
        Response[Union[Any, GetMessageQueryresponse]]
    """


    return sync_detailed(
        client=client,
appsid=appsid,
msgid=msgid,
to=to,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    appsid: str,
    msgid: int,
    to: Union[Unset, None, int] = UNSET,

) -> Response[Union[Any, GetMessageQueryresponse]]:
    """Get msgQuery

     Unifonic Get message query API allows you to get details of specified message.

    Args:
        appsid (str):  Example:  Use your own appsid.
        msgid (int):  Example: 3200017901931.
        to (Union[Unset, None, int]):  Example: 966505980169.

    Returns:
        Response[Union[Any, GetMessageQueryresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
appsid=appsid,
msgid=msgid,
to=to,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    appsid: str,
    msgid: int,
    to: Union[Unset, None, int] = UNSET,

) -> Optional[Union[Any, GetMessageQueryresponse]]:
    """Get msgQuery

     Unifonic Get message query API allows you to get details of specified message.

    Args:
        appsid (str):  Example:  Use your own appsid.
        msgid (int):  Example: 3200017901931.
        to (Union[Unset, None, int]):  Example: 966505980169.

    Returns:
        Response[Union[Any, GetMessageQueryresponse]]
    """


    return (await asyncio_detailed(
        client=client,
appsid=appsid,
msgid=msgid,
to=to,

    )).parsed
