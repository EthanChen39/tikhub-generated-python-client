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
    aweme_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    current_region: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aweme_id"] = aweme_id

    params["cursor"] = cursor

    params["count"] = count

    params["current_region"] = current_region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_post_comment",
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
    aweme_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    current_region: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品的评论列表/Get video comments

     # [中文]
    ### 用途:
    - 获取作品的评论列表
    ### 参数:
    - aweme_id: 作品id
    - cursor: 翻页游标
    - count: 每页数量
    - current_region: 当前地区，默认为空。
    ### 返回:
    - 作品的评论列表

    # [English]
    ### Purpose:
    - Get video comments
    ### Parameters:
    - aweme_id: Video id
    - cursor: Page cursor
    - count: Number per page
    - current_region: Current region, default is empty.
    ### Return:
    - Video comments

    # [示例/Eample]
    aweme_id = \"7304809083817774382\"
    cursor = 0
    count = 20
    current_region = \"\"

    Args:
        aweme_id (str): 作品id/Video id
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        current_region (Union[Unset, str]): 当前地区/Current region Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_id=aweme_id,
        cursor=cursor,
        count=count,
        current_region=current_region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    current_region: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品的评论列表/Get video comments

     # [中文]
    ### 用途:
    - 获取作品的评论列表
    ### 参数:
    - aweme_id: 作品id
    - cursor: 翻页游标
    - count: 每页数量
    - current_region: 当前地区，默认为空。
    ### 返回:
    - 作品的评论列表

    # [English]
    ### Purpose:
    - Get video comments
    ### Parameters:
    - aweme_id: Video id
    - cursor: Page cursor
    - count: Number per page
    - current_region: Current region, default is empty.
    ### Return:
    - Video comments

    # [示例/Eample]
    aweme_id = \"7304809083817774382\"
    cursor = 0
    count = 20
    current_region = \"\"

    Args:
        aweme_id (str): 作品id/Video id
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        current_region (Union[Unset, str]): 当前地区/Current region Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        aweme_id=aweme_id,
        cursor=cursor,
        count=count,
        current_region=current_region,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    current_region: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品的评论列表/Get video comments

     # [中文]
    ### 用途:
    - 获取作品的评论列表
    ### 参数:
    - aweme_id: 作品id
    - cursor: 翻页游标
    - count: 每页数量
    - current_region: 当前地区，默认为空。
    ### 返回:
    - 作品的评论列表

    # [English]
    ### Purpose:
    - Get video comments
    ### Parameters:
    - aweme_id: Video id
    - cursor: Page cursor
    - count: Number per page
    - current_region: Current region, default is empty.
    ### Return:
    - Video comments

    # [示例/Eample]
    aweme_id = \"7304809083817774382\"
    cursor = 0
    count = 20
    current_region = \"\"

    Args:
        aweme_id (str): 作品id/Video id
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        current_region (Union[Unset, str]): 当前地区/Current region Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_id=aweme_id,
        cursor=cursor,
        count=count,
        current_region=current_region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    current_region: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品的评论列表/Get video comments

     # [中文]
    ### 用途:
    - 获取作品的评论列表
    ### 参数:
    - aweme_id: 作品id
    - cursor: 翻页游标
    - count: 每页数量
    - current_region: 当前地区，默认为空。
    ### 返回:
    - 作品的评论列表

    # [English]
    ### Purpose:
    - Get video comments
    ### Parameters:
    - aweme_id: Video id
    - cursor: Page cursor
    - count: Number per page
    - current_region: Current region, default is empty.
    ### Return:
    - Video comments

    # [示例/Eample]
    aweme_id = \"7304809083817774382\"
    cursor = 0
    count = 20
    current_region = \"\"

    Args:
        aweme_id (str): 作品id/Video id
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        current_region (Union[Unset, str]): 当前地区/Current region Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            aweme_id=aweme_id,
            cursor=cursor,
            count=count,
            current_region=current_region,
        )
    ).parsed
