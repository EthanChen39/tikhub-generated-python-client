from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/net_ease_cloud_music/app/decrypt_post_payload",
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: str,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""解密POST请求中的16进制payload/Decrypt the 16-bit payload in the POST request

     # [中文]
    ### 用途:
    - 解密网易云音乐APP POST请求中的16进制payload。
    ### 参数:
    - payload: 16进制payload。
    ### 返回:
    - 解密后的payload

    # [English]
    ### Purpose:
    - Decrypt the 16-bit payload in the POST request of NetEase Cloud Music APP.
    ### Parameters:
    - payload: 16-bit payload.
    ### Returns:
    - Decrypted payload

    # [示例/Example]
    payload = \"4AEEAB033C3F4068DBB74379B8C889D2187585FBBBC7CA1ADA7D10714AA139AE279A615DE7B87483A83A9091
    ED52D70B70DA02A7FE8A20317AA40F0FF461AC33DB77371E30F9C7F57783E800559AE08DD1E10EFC9CDC69D6815ADCDBF5A7
    D3006AA3B102FBE7296AB0DB9EA5C46AD12B\"

    Args:
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""解密POST请求中的16进制payload/Decrypt the 16-bit payload in the POST request

     # [中文]
    ### 用途:
    - 解密网易云音乐APP POST请求中的16进制payload。
    ### 参数:
    - payload: 16进制payload。
    ### 返回:
    - 解密后的payload

    # [English]
    ### Purpose:
    - Decrypt the 16-bit payload in the POST request of NetEase Cloud Music APP.
    ### Parameters:
    - payload: 16-bit payload.
    ### Returns:
    - Decrypted payload

    # [示例/Example]
    payload = \"4AEEAB033C3F4068DBB74379B8C889D2187585FBBBC7CA1ADA7D10714AA139AE279A615DE7B87483A83A9091
    ED52D70B70DA02A7FE8A20317AA40F0FF461AC33DB77371E30F9C7F57783E800559AE08DD1E10EFC9CDC69D6815ADCDBF5A7
    D3006AA3B102FBE7296AB0DB9EA5C46AD12B\"

    Args:
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: str,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""解密POST请求中的16进制payload/Decrypt the 16-bit payload in the POST request

     # [中文]
    ### 用途:
    - 解密网易云音乐APP POST请求中的16进制payload。
    ### 参数:
    - payload: 16进制payload。
    ### 返回:
    - 解密后的payload

    # [English]
    ### Purpose:
    - Decrypt the 16-bit payload in the POST request of NetEase Cloud Music APP.
    ### Parameters:
    - payload: 16-bit payload.
    ### Returns:
    - Decrypted payload

    # [示例/Example]
    payload = \"4AEEAB033C3F4068DBB74379B8C889D2187585FBBBC7CA1ADA7D10714AA139AE279A615DE7B87483A83A9091
    ED52D70B70DA02A7FE8A20317AA40F0FF461AC33DB77371E30F9C7F57783E800559AE08DD1E10EFC9CDC69D6815ADCDBF5A7
    D3006AA3B102FBE7296AB0DB9EA5C46AD12B\"

    Args:
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""解密POST请求中的16进制payload/Decrypt the 16-bit payload in the POST request

     # [中文]
    ### 用途:
    - 解密网易云音乐APP POST请求中的16进制payload。
    ### 参数:
    - payload: 16进制payload。
    ### 返回:
    - 解密后的payload

    # [English]
    ### Purpose:
    - Decrypt the 16-bit payload in the POST request of NetEase Cloud Music APP.
    ### Parameters:
    - payload: 16-bit payload.
    ### Returns:
    - Decrypted payload

    # [示例/Example]
    payload = \"4AEEAB033C3F4068DBB74379B8C889D2187585FBBBC7CA1ADA7D10714AA139AE279A615DE7B87483A83A9091
    ED52D70B70DA02A7FE8A20317AA40F0FF461AC33DB77371E30F9C7F57783E800559AE08DD1E10EFC9CDC69D6815ADCDBF5A7
    D3006AA3B102FBE7296AB0DB9EA5C46AD12B\"

    Args:
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
