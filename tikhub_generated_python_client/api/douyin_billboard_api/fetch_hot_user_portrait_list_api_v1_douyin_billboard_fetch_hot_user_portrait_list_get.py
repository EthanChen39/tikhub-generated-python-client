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
    option: Union[Unset, str] = "4",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aweme_id"] = aweme_id

    params["option"] = option

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/billboard/fetch_hot_user_portrait_list",
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
    option: Union[Unset, str] = "4",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only

     # [中文]
    ### 用途:
    - 获取作品点赞观众画像
    ### 参数:
    - aweme_id: 作品id
    - option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
    ### 返回:
    - 作品点赞观众画像

    # [English]
    ### Purpose:
    - Get the work like audience portrait
    ### Parameters:
    - aweme_id: Work id
    - option: Option
        - 1 Mobile price
        - 2 Gender distribution
        - 3 Age distribution
        - 4 Regional distribution - province
        - 5 Regional distribution - city
        - 6 City level
        - 7 Mobile brand distribution
    ### Return:
    - Work like audience portrait

    Args:
        aweme_id (str): 作品id
        option (Union[Unset, str]): 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
            Default: '4'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_id=aweme_id,
        option=option,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
    option: Union[Unset, str] = "4",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only

     # [中文]
    ### 用途:
    - 获取作品点赞观众画像
    ### 参数:
    - aweme_id: 作品id
    - option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
    ### 返回:
    - 作品点赞观众画像

    # [English]
    ### Purpose:
    - Get the work like audience portrait
    ### Parameters:
    - aweme_id: Work id
    - option: Option
        - 1 Mobile price
        - 2 Gender distribution
        - 3 Age distribution
        - 4 Regional distribution - province
        - 5 Regional distribution - city
        - 6 City level
        - 7 Mobile brand distribution
    ### Return:
    - Work like audience portrait

    Args:
        aweme_id (str): 作品id
        option (Union[Unset, str]): 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
            Default: '4'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        aweme_id=aweme_id,
        option=option,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
    option: Union[Unset, str] = "4",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only

     # [中文]
    ### 用途:
    - 获取作品点赞观众画像
    ### 参数:
    - aweme_id: 作品id
    - option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
    ### 返回:
    - 作品点赞观众画像

    # [English]
    ### Purpose:
    - Get the work like audience portrait
    ### Parameters:
    - aweme_id: Work id
    - option: Option
        - 1 Mobile price
        - 2 Gender distribution
        - 3 Age distribution
        - 4 Regional distribution - province
        - 5 Regional distribution - city
        - 6 City level
        - 7 Mobile brand distribution
    ### Return:
    - Work like audience portrait

    Args:
        aweme_id (str): 作品id
        option (Union[Unset, str]): 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
            Default: '4'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_id=aweme_id,
        option=option,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
    option: Union[Unset, str] = "4",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only

     # [中文]
    ### 用途:
    - 获取作品点赞观众画像
    ### 参数:
    - aweme_id: 作品id
    - option: 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
    ### 返回:
    - 作品点赞观众画像

    # [English]
    ### Purpose:
    - Get the work like audience portrait
    ### Parameters:
    - aweme_id: Work id
    - option: Option
        - 1 Mobile price
        - 2 Gender distribution
        - 3 Age distribution
        - 4 Regional distribution - province
        - 5 Regional distribution - city
        - 6 City level
        - 7 Mobile brand distribution
    ### Return:
    - Work like audience portrait

    Args:
        aweme_id (str): 作品id
        option (Union[Unset, str]): 选项，1 手机价格分布 2 性别分布 3 年龄分布 4 地域分布-省份 5 地域分布-城市 6 城市等级 7 手机品牌分布
            Default: '4'.

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
            option=option,
        )
    ).parsed
