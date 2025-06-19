from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    room_id: str,
    author_id: str,
    limit: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["room_id"] = room_id

    params["author_id"] = author_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_live_room_product_result",
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
    room_id: str,
    author_id: str,
    limit: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""抖音直播间商品信息/Douyin live room product information

     # [中文]
    ### 用途:
    - 抖音直播间商品信息
    ### 参数:
    - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie，如获取失败请手动过一次验证码)
    - room_id: 直播间room_id
    - author_id: 作者id
    - limit: 数量
    ### 返回:
    - 商品信息

    # [English]
    ### Purpose:
    - Douyin live room product information
    ### Parameters:
    - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own
    Cookie, if the acquisition fails, please manually pass the captcha code once)
    - room_id: Room room_id
    - author_id: Author id
    - limit: Number
    ### Return:
    - Product information

    # [示例/Example]
    cookie = \"YOUR_COOKIE\"
    room_id = \"7356742011975715619\"
    author_id = \"2207432981615527\"
    limit = 20

    Args:
        room_id (str): 直播间room_id/Room room_id
        author_id (str): 作者id/Author id
        limit (Union[Unset, int]): 数量/Number Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        author_id=author_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    room_id: str,
    author_id: str,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""抖音直播间商品信息/Douyin live room product information

     # [中文]
    ### 用途:
    - 抖音直播间商品信息
    ### 参数:
    - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie，如获取失败请手动过一次验证码)
    - room_id: 直播间room_id
    - author_id: 作者id
    - limit: 数量
    ### 返回:
    - 商品信息

    # [English]
    ### Purpose:
    - Douyin live room product information
    ### Parameters:
    - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own
    Cookie, if the acquisition fails, please manually pass the captcha code once)
    - room_id: Room room_id
    - author_id: Author id
    - limit: Number
    ### Return:
    - Product information

    # [示例/Example]
    cookie = \"YOUR_COOKIE\"
    room_id = \"7356742011975715619\"
    author_id = \"2207432981615527\"
    limit = 20

    Args:
        room_id (str): 直播间room_id/Room room_id
        author_id (str): 作者id/Author id
        limit (Union[Unset, int]): 数量/Number Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        room_id=room_id,
        author_id=author_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    room_id: str,
    author_id: str,
    limit: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""抖音直播间商品信息/Douyin live room product information

     # [中文]
    ### 用途:
    - 抖音直播间商品信息
    ### 参数:
    - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie，如获取失败请手动过一次验证码)
    - room_id: 直播间room_id
    - author_id: 作者id
    - limit: 数量
    ### 返回:
    - 商品信息

    # [English]
    ### Purpose:
    - Douyin live room product information
    ### Parameters:
    - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own
    Cookie, if the acquisition fails, please manually pass the captcha code once)
    - room_id: Room room_id
    - author_id: Author id
    - limit: Number
    ### Return:
    - Product information

    # [示例/Example]
    cookie = \"YOUR_COOKIE\"
    room_id = \"7356742011975715619\"
    author_id = \"2207432981615527\"
    limit = 20

    Args:
        room_id (str): 直播间room_id/Room room_id
        author_id (str): 作者id/Author id
        limit (Union[Unset, int]): 数量/Number Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        author_id=author_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    room_id: str,
    author_id: str,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""抖音直播间商品信息/Douyin live room product information

     # [中文]
    ### 用途:
    - 抖音直播间商品信息
    ### 参数:
    - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie，如获取失败请手动过一次验证码)
    - room_id: 直播间room_id
    - author_id: 作者id
    - limit: 数量
    ### 返回:
    - 商品信息

    # [English]
    ### Purpose:
    - Douyin live room product information
    ### Parameters:
    - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own
    Cookie, if the acquisition fails, please manually pass the captcha code once)
    - room_id: Room room_id
    - author_id: Author id
    - limit: Number
    ### Return:
    - Product information

    # [示例/Example]
    cookie = \"YOUR_COOKIE\"
    room_id = \"7356742011975715619\"
    author_id = \"2207432981615527\"
    limit = 20

    Args:
        room_id (str): 直播间room_id/Room room_id
        author_id (str): 作者id/Author id
        limit (Union[Unset, int]): 数量/Number Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            room_id=room_id,
            author_id=author_id,
            limit=limit,
        )
    ).parsed
