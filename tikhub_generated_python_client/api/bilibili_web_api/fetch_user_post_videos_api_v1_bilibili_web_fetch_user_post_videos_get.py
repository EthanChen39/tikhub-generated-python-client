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
    uid: str,
    pn: Union[Unset, int] = 1,
    order: Union[Unset, str] = "pubdate",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["uid"] = uid

    params["pn"] = pn

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/bilibili/web/fetch_user_post_videos",
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
    uid: str,
    pn: Union[Unset, int] = 1,
    order: Union[Unset, str] = "pubdate",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户发布的视频数据
    ### 参数:
    - uid: 用户UID
    - pn: 页码
    - order: 排序方式
        - pubdate 最新发布
        - click 最多播放
        - stow 最多收藏
    ### 返回:
    - 用户发布的视频数据

    # [English]
    ### Purpose:
    - Get user post video data
    ### Parameters:
    - uid: User UID
    - pn: Page number
    - order: Order method
        - pubdate Latest release
        - click Most played
        - stow Most collection
    ### Return:
    - User posted video data

    # [示例/Example]
    uid = \"178360345\"
    pn = 1
    order = \"pubdate\"

    Args:
        uid (str): 用户UID
        pn (Union[Unset, int]): 页码/Page number Default: 1.
        order (Union[Unset, str]): 排序方式/Order method Default: 'pubdate'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        pn=pn,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    uid: str,
    pn: Union[Unset, int] = 1,
    order: Union[Unset, str] = "pubdate",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户发布的视频数据
    ### 参数:
    - uid: 用户UID
    - pn: 页码
    - order: 排序方式
        - pubdate 最新发布
        - click 最多播放
        - stow 最多收藏
    ### 返回:
    - 用户发布的视频数据

    # [English]
    ### Purpose:
    - Get user post video data
    ### Parameters:
    - uid: User UID
    - pn: Page number
    - order: Order method
        - pubdate Latest release
        - click Most played
        - stow Most collection
    ### Return:
    - User posted video data

    # [示例/Example]
    uid = \"178360345\"
    pn = 1
    order = \"pubdate\"

    Args:
        uid (str): 用户UID
        pn (Union[Unset, int]): 页码/Page number Default: 1.
        order (Union[Unset, str]): 排序方式/Order method Default: 'pubdate'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        uid=uid,
        pn=pn,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    uid: str,
    pn: Union[Unset, int] = 1,
    order: Union[Unset, str] = "pubdate",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户发布的视频数据
    ### 参数:
    - uid: 用户UID
    - pn: 页码
    - order: 排序方式
        - pubdate 最新发布
        - click 最多播放
        - stow 最多收藏
    ### 返回:
    - 用户发布的视频数据

    # [English]
    ### Purpose:
    - Get user post video data
    ### Parameters:
    - uid: User UID
    - pn: Page number
    - order: Order method
        - pubdate Latest release
        - click Most played
        - stow Most collection
    ### Return:
    - User posted video data

    # [示例/Example]
    uid = \"178360345\"
    pn = 1
    order = \"pubdate\"

    Args:
        uid (str): 用户UID
        pn (Union[Unset, int]): 页码/Page number Default: 1.
        order (Union[Unset, str]): 排序方式/Order method Default: 'pubdate'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        pn=pn,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    uid: str,
    pn: Union[Unset, int] = 1,
    order: Union[Unset, str] = "pubdate",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户发布的视频数据
    ### 参数:
    - uid: 用户UID
    - pn: 页码
    - order: 排序方式
        - pubdate 最新发布
        - click 最多播放
        - stow 最多收藏
    ### 返回:
    - 用户发布的视频数据

    # [English]
    ### Purpose:
    - Get user post video data
    ### Parameters:
    - uid: User UID
    - pn: Page number
    - order: Order method
        - pubdate Latest release
        - click Most played
        - stow Most collection
    ### Return:
    - User posted video data

    # [示例/Example]
    uid = \"178360345\"
    pn = 1
    order = \"pubdate\"

    Args:
        uid (str): 用户UID
        pn (Union[Unset, int]): 页码/Page number Default: 1.
        order (Union[Unset, str]): 排序方式/Order method Default: 'pubdate'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            uid=uid,
            pn=pn,
            order=order,
        )
    ).parsed
