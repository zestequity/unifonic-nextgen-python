from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...types import UNSET, Unset
from typing import Optional
from typing import cast
from typing import Union
from typing import Dict
from ...models.send_wrapperresponse import SendWrapperresponse



def _get_kwargs(
    *,
    client: Client,
    appsid: str,
    msg: str,
    to: int,
    sender: str,
    base_encode: Union[Unset, None, bool] = False,
    encoding: Union[Unset, None, str] = 'UCS2',

) -> Dict[str, Any]:
    url = "{}/wrapper/sendSMS.php".format(
        client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["appsid"] = appsid


    params["msg"] = msg


    params["to"] = to


    params["sender"] = sender


    params["baseEncode"] = base_encode


    params["encoding"] = encoding



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, SendWrapperresponse]]:
    if response.status_code == 200:
        response_200 = SendWrapperresponse.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, response.json())
        return response_401
    if response.status_code == 402:
        response_402 = cast(Any, response.json())
        return response_402
    if response.status_code == 459:
        response_459 = cast(Any, response.json())
        return response_459
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, SendWrapperresponse]]:
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
    msg: str,
    to: int,
    sender: str,
    base_encode: Union[Unset, None, bool] = False,
    encoding: Union[Unset, None, str] = 'UCS2',

) -> Response[Union[Any, SendWrapperresponse]]:
    """Send message

     Unifonic Send Wrapper API allows you to send  text messages to  multiple users at the same time

    Args:
        appsid (str):  Example: Use your own appsid.
        msg (str):  Example: Test.
        to (int):  Example: 966505980169.
        sender (str):  Example: sender.
        base_encode (Union[Unset, None, bool]):
        encoding (Union[Unset, None, str]):  Default: 'UCS2'. Example: GSM7.

    Returns:
        Response[Union[Any, SendWrapperresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
appsid=appsid,
msg=msg,
to=to,
sender=sender,
base_encode=base_encode,
encoding=encoding,

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
    msg: str,
    to: int,
    sender: str,
    base_encode: Union[Unset, None, bool] = False,
    encoding: Union[Unset, None, str] = 'UCS2',

) -> Optional[Union[Any, SendWrapperresponse]]:
    """Send message

     Unifonic Send Wrapper API allows you to send  text messages to  multiple users at the same time

    Args:
        appsid (str):  Example: Use your own appsid.
        msg (str):  Example: Test.
        to (int):  Example: 966505980169.
        sender (str):  Example: sender.
        base_encode (Union[Unset, None, bool]):
        encoding (Union[Unset, None, str]):  Default: 'UCS2'. Example: GSM7.

    Returns:
        Response[Union[Any, SendWrapperresponse]]
    """


    return sync_detailed(
        client=client,
appsid=appsid,
msg=msg,
to=to,
sender=sender,
base_encode=base_encode,
encoding=encoding,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    appsid: str,
    msg: str,
    to: int,
    sender: str,
    base_encode: Union[Unset, None, bool] = False,
    encoding: Union[Unset, None, str] = 'UCS2',

) -> Response[Union[Any, SendWrapperresponse]]:
    """Send message

     Unifonic Send Wrapper API allows you to send  text messages to  multiple users at the same time

    Args:
        appsid (str):  Example: Use your own appsid.
        msg (str):  Example: Test.
        to (int):  Example: 966505980169.
        sender (str):  Example: sender.
        base_encode (Union[Unset, None, bool]):
        encoding (Union[Unset, None, str]):  Default: 'UCS2'. Example: GSM7.

    Returns:
        Response[Union[Any, SendWrapperresponse]]
    """


    kwargs = _get_kwargs(
        client=client,
appsid=appsid,
msg=msg,
to=to,
sender=sender,
base_encode=base_encode,
encoding=encoding,

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
    msg: str,
    to: int,
    sender: str,
    base_encode: Union[Unset, None, bool] = False,
    encoding: Union[Unset, None, str] = 'UCS2',

) -> Optional[Union[Any, SendWrapperresponse]]:
    """Send message

     Unifonic Send Wrapper API allows you to send  text messages to  multiple users at the same time

    Args:
        appsid (str):  Example: Use your own appsid.
        msg (str):  Example: Test.
        to (int):  Example: 966505980169.
        sender (str):  Example: sender.
        base_encode (Union[Unset, None, bool]):
        encoding (Union[Unset, None, str]):  Default: 'UCS2'. Example: GSM7.

    Returns:
        Response[Union[Any, SendWrapperresponse]]
    """


    return (await asyncio_detailed(
        client=client,
appsid=appsid,
msg=msg,
to=to,
sender=sender,
base_encode=base_encode,
encoding=encoding,

    )).parsed
