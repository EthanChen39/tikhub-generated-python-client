from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    original_url: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["original_url"] = original_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pipixia/app/fetch_short_url",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    if response.status_code == 200:
        response_200 = ResponseModel.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    original_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""生成短连接/Generate short URL

     # [中文]
    ### 用途:
    - 生成短连接。
    ### 参数:
    - original_url: 原始链接，可以是任意链接。
    ### 返回:
    - 短连接

    # [English]
    ### Purpose:
    - Generate short URL.
    ### Parameters:
    - original_url: Original URL, can be any link.
    ### Return:
    - Short URL

    # [示例/Example]
    original_url = \"https://h5.pipix.com/item/7385813877985909043\"

    Args:
        original_url (str): 原始链接/Original URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        original_url=original_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    original_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""生成短连接/Generate short URL

     # [中文]
    ### 用途:
    - 生成短连接。
    ### 参数:
    - original_url: 原始链接，可以是任意链接。
    ### 返回:
    - 短连接

    # [English]
    ### Purpose:
    - Generate short URL.
    ### Parameters:
    - original_url: Original URL, can be any link.
    ### Return:
    - Short URL

    # [示例/Example]
    original_url = \"https://h5.pipix.com/item/7385813877985909043\"

    Args:
        original_url (str): 原始链接/Original URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        original_url=original_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    original_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""生成短连接/Generate short URL

     # [中文]
    ### 用途:
    - 生成短连接。
    ### 参数:
    - original_url: 原始链接，可以是任意链接。
    ### 返回:
    - 短连接

    # [English]
    ### Purpose:
    - Generate short URL.
    ### Parameters:
    - original_url: Original URL, can be any link.
    ### Return:
    - Short URL

    # [示例/Example]
    original_url = \"https://h5.pipix.com/item/7385813877985909043\"

    Args:
        original_url (str): 原始链接/Original URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        original_url=original_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    original_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""生成短连接/Generate short URL

     # [中文]
    ### 用途:
    - 生成短连接。
    ### 参数:
    - original_url: 原始链接，可以是任意链接。
    ### 返回:
    - 短连接

    # [English]
    ### Purpose:
    - Generate short URL.
    ### Parameters:
    - original_url: Original URL, can be any link.
    ### Return:
    - Short URL

    # [示例/Example]
    original_url = \"https://h5.pipix.com/item/7385813877985909043\"

    Args:
        original_url (str): 原始链接/Original URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            original_url=original_url,
        )
    ).parsed
