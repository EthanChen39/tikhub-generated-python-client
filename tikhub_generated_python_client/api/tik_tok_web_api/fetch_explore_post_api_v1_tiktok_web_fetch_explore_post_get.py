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
    category_type: Union[Unset, str] = "120",
    count: Union[Unset, int] = 16,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["categoryType"] = category_type

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_explore_post",
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
    category_type: Union[Unset, str] = "120",
    count: Union[Unset, int] = 16,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取探索作品数据/Get explore video data

     # [中文]
    ### 用途:
    - 获取探索作品数据
    ### 参数:
    - categoryType: 作品分类
        - 100: 动画与漫画
        - 101: 表演
        - 102: 美容护理
        - 103: 游戏
        - 104: 喜剧
        - 105: 日常生活
        - 106: 家庭
        - 107: 情感关系
        - 108: 戏剧
        - 109: 穿搭
        - 110: 对口型
        - 111: 美食
        - 112: 运动
        - 113: 动物
        - 114: 社会
        - 115: 汽车
        - 116: 教育
        - 117: 健身和健康
        - 118: 科技
        - 119: 唱歌跳舞
        - 120: 全部
    - count: 每页数量
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get explore video data
    ### Parameters:
    - categoryType: Video category
        - 100: Animation and comics
        - 101: Performance
        - 102: Beauty care
        - 103: Game
        - 104: Comedy
        - 105: Daily life
        - 106: Family
        - 107: Emotional relationship
        - 108: Drama
        - 109: Dress up
        - 110: Dubbing
        - 111: Food
        - 112: Sports
        - 113: Animals
        - 114: Society
        - 115: Car
        - 116: Education
        - 117: Fitness and health
        - 118: Technology
        - 119: Singing and dancing
        - 120: All
    - count: Number per page
    ### Return:
    - Video data

    # [示例/Example]
    categoryType = \"120\"
    count = 16

    Args:
        category_type (Union[Unset, str]): 作品分类/Video category Default: '120'.
        count (Union[Unset, int]): 每页数量/Number per page Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        category_type=category_type,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    category_type: Union[Unset, str] = "120",
    count: Union[Unset, int] = 16,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取探索作品数据/Get explore video data

     # [中文]
    ### 用途:
    - 获取探索作品数据
    ### 参数:
    - categoryType: 作品分类
        - 100: 动画与漫画
        - 101: 表演
        - 102: 美容护理
        - 103: 游戏
        - 104: 喜剧
        - 105: 日常生活
        - 106: 家庭
        - 107: 情感关系
        - 108: 戏剧
        - 109: 穿搭
        - 110: 对口型
        - 111: 美食
        - 112: 运动
        - 113: 动物
        - 114: 社会
        - 115: 汽车
        - 116: 教育
        - 117: 健身和健康
        - 118: 科技
        - 119: 唱歌跳舞
        - 120: 全部
    - count: 每页数量
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get explore video data
    ### Parameters:
    - categoryType: Video category
        - 100: Animation and comics
        - 101: Performance
        - 102: Beauty care
        - 103: Game
        - 104: Comedy
        - 105: Daily life
        - 106: Family
        - 107: Emotional relationship
        - 108: Drama
        - 109: Dress up
        - 110: Dubbing
        - 111: Food
        - 112: Sports
        - 113: Animals
        - 114: Society
        - 115: Car
        - 116: Education
        - 117: Fitness and health
        - 118: Technology
        - 119: Singing and dancing
        - 120: All
    - count: Number per page
    ### Return:
    - Video data

    # [示例/Example]
    categoryType = \"120\"
    count = 16

    Args:
        category_type (Union[Unset, str]): 作品分类/Video category Default: '120'.
        count (Union[Unset, int]): 每页数量/Number per page Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        category_type=category_type,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category_type: Union[Unset, str] = "120",
    count: Union[Unset, int] = 16,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取探索作品数据/Get explore video data

     # [中文]
    ### 用途:
    - 获取探索作品数据
    ### 参数:
    - categoryType: 作品分类
        - 100: 动画与漫画
        - 101: 表演
        - 102: 美容护理
        - 103: 游戏
        - 104: 喜剧
        - 105: 日常生活
        - 106: 家庭
        - 107: 情感关系
        - 108: 戏剧
        - 109: 穿搭
        - 110: 对口型
        - 111: 美食
        - 112: 运动
        - 113: 动物
        - 114: 社会
        - 115: 汽车
        - 116: 教育
        - 117: 健身和健康
        - 118: 科技
        - 119: 唱歌跳舞
        - 120: 全部
    - count: 每页数量
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get explore video data
    ### Parameters:
    - categoryType: Video category
        - 100: Animation and comics
        - 101: Performance
        - 102: Beauty care
        - 103: Game
        - 104: Comedy
        - 105: Daily life
        - 106: Family
        - 107: Emotional relationship
        - 108: Drama
        - 109: Dress up
        - 110: Dubbing
        - 111: Food
        - 112: Sports
        - 113: Animals
        - 114: Society
        - 115: Car
        - 116: Education
        - 117: Fitness and health
        - 118: Technology
        - 119: Singing and dancing
        - 120: All
    - count: Number per page
    ### Return:
    - Video data

    # [示例/Example]
    categoryType = \"120\"
    count = 16

    Args:
        category_type (Union[Unset, str]): 作品分类/Video category Default: '120'.
        count (Union[Unset, int]): 每页数量/Number per page Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        category_type=category_type,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category_type: Union[Unset, str] = "120",
    count: Union[Unset, int] = 16,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取探索作品数据/Get explore video data

     # [中文]
    ### 用途:
    - 获取探索作品数据
    ### 参数:
    - categoryType: 作品分类
        - 100: 动画与漫画
        - 101: 表演
        - 102: 美容护理
        - 103: 游戏
        - 104: 喜剧
        - 105: 日常生活
        - 106: 家庭
        - 107: 情感关系
        - 108: 戏剧
        - 109: 穿搭
        - 110: 对口型
        - 111: 美食
        - 112: 运动
        - 113: 动物
        - 114: 社会
        - 115: 汽车
        - 116: 教育
        - 117: 健身和健康
        - 118: 科技
        - 119: 唱歌跳舞
        - 120: 全部
    - count: 每页数量
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get explore video data
    ### Parameters:
    - categoryType: Video category
        - 100: Animation and comics
        - 101: Performance
        - 102: Beauty care
        - 103: Game
        - 104: Comedy
        - 105: Daily life
        - 106: Family
        - 107: Emotional relationship
        - 108: Drama
        - 109: Dress up
        - 110: Dubbing
        - 111: Food
        - 112: Sports
        - 113: Animals
        - 114: Society
        - 115: Car
        - 116: Education
        - 117: Fitness and health
        - 118: Technology
        - 119: Singing and dancing
        - 120: All
    - count: Number per page
    ### Return:
    - Video data

    # [示例/Example]
    categoryType = \"120\"
    count = 16

    Args:
        category_type (Union[Unset, str]): 作品分类/Video category Default: '120'.
        count (Union[Unset, int]): 每页数量/Number per page Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            category_type=category_type,
            count=count,
        )
    ).parsed
