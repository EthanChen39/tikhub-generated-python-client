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
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, str] = "0",
    publish_time: Union[Unset, str] = "0",
    filter_duration: Union[Unset, str] = "0",
    content_type: Union[Unset, str] = "0",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["offset"] = offset

    params["count"] = count

    params["sort_type"] = sort_type

    params["publish_time"] = publish_time

    params["filter_duration"] = filter_duration

    params["content_type"] = content_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/fetch_general_search_result",
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
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, str] = "0",
    publish_time: Union[Unset, str] = "0",
    filter_duration: Union[Unset, str] = "0",
    content_type: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated,
    see the documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的综合搜索结果
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量，请保持默认，否则会出现BUG。
    - sort_type: 0:综合排序 1:最多点赞 2:最新发布
    - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年
    - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上
    - content_type: 0:不限 1:视频 2:图片 3:文章
    ### 返回:
    - 综合搜索结果

    # [English]
    ### Purpose:
    - Get comprehensive search results of specified keywords
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number Please keep the default, otherwise there will be BUG.
    - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
    - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year
    - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes
    - content_type: 0: Unlimited 1: Video 2: Picture 3: Article
    ### Return:
    - Comprehensive search results

    # [示例/Example]
    keyword = \"中华娘\"
    offset = 0
    count = 20
    sort_type = \"0\"
    publish_time = \"0\"
    filter_duration = \"0\"
    content_type = \"0\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '0'.
        filter_duration (Union[Unset, str]): 时长/Duration Default: '0'.
        content_type (Union[Unset, str]): 内容类型/Content type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        count=count,
        sort_type=sort_type,
        publish_time=publish_time,
        filter_duration=filter_duration,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, str] = "0",
    publish_time: Union[Unset, str] = "0",
    filter_duration: Union[Unset, str] = "0",
    content_type: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated,
    see the documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的综合搜索结果
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量，请保持默认，否则会出现BUG。
    - sort_type: 0:综合排序 1:最多点赞 2:最新发布
    - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年
    - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上
    - content_type: 0:不限 1:视频 2:图片 3:文章
    ### 返回:
    - 综合搜索结果

    # [English]
    ### Purpose:
    - Get comprehensive search results of specified keywords
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number Please keep the default, otherwise there will be BUG.
    - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
    - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year
    - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes
    - content_type: 0: Unlimited 1: Video 2: Picture 3: Article
    ### Return:
    - Comprehensive search results

    # [示例/Example]
    keyword = \"中华娘\"
    offset = 0
    count = 20
    sort_type = \"0\"
    publish_time = \"0\"
    filter_duration = \"0\"
    content_type = \"0\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '0'.
        filter_duration (Union[Unset, str]): 时长/Duration Default: '0'.
        content_type (Union[Unset, str]): 内容类型/Content type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        offset=offset,
        count=count,
        sort_type=sort_type,
        publish_time=publish_time,
        filter_duration=filter_duration,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, str] = "0",
    publish_time: Union[Unset, str] = "0",
    filter_duration: Union[Unset, str] = "0",
    content_type: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated,
    see the documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的综合搜索结果
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量，请保持默认，否则会出现BUG。
    - sort_type: 0:综合排序 1:最多点赞 2:最新发布
    - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年
    - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上
    - content_type: 0:不限 1:视频 2:图片 3:文章
    ### 返回:
    - 综合搜索结果

    # [English]
    ### Purpose:
    - Get comprehensive search results of specified keywords
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number Please keep the default, otherwise there will be BUG.
    - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
    - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year
    - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes
    - content_type: 0: Unlimited 1: Video 2: Picture 3: Article
    ### Return:
    - Comprehensive search results

    # [示例/Example]
    keyword = \"中华娘\"
    offset = 0
    count = 20
    sort_type = \"0\"
    publish_time = \"0\"
    filter_duration = \"0\"
    content_type = \"0\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '0'.
        filter_duration (Union[Unset, str]): 时长/Duration Default: '0'.
        content_type (Union[Unset, str]): 内容类型/Content type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        count=count,
        sort_type=sort_type,
        publish_time=publish_time,
        filter_duration=filter_duration,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, str] = "0",
    publish_time: Union[Unset, str] = "0",
    filter_duration: Union[Unset, str] = "0",
    content_type: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated,
    see the documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的综合搜索结果
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量，请保持默认，否则会出现BUG。
    - sort_type: 0:综合排序 1:最多点赞 2:最新发布
    - publish_time: 0:不限 1:最近一天 7:最近一周 180:最近半年
    - filter_duration: 0:不限 0-1:1分钟以内 1-5:1-5分钟 5-10000:5分钟以上
    - content_type: 0:不限 1:视频 2:图片 3:文章
    ### 返回:
    - 综合搜索结果

    # [English]
    ### Purpose:
    - Get comprehensive search results of specified keywords
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number Please keep the default, otherwise there will be BUG.
    - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
    - publish_time: 0: Unlimited 1: Last day 7: Last week 180: Last half year
    - filter_duration: 0: Unlimited 0-1: Within 1 minute 1-5: 1-5 minutes 5-10000: More than 5 minutes
    - content_type: 0: Unlimited 1: Video 2: Picture 3: Article
    ### Return:
    - Comprehensive search results

    # [示例/Example]
    keyword = \"中华娘\"
    offset = 0
    count = 20
    sort_type = \"0\"
    publish_time = \"0\"
    filter_duration = \"0\"
    content_type = \"0\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '0'.
        filter_duration (Union[Unset, str]): 时长/Duration Default: '0'.
        content_type (Union[Unset, str]): 内容类型/Content type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword=keyword,
            offset=offset,
            count=count,
            sort_type=sort_type,
            publish_time=publish_time,
            filter_duration=filter_duration,
            content_type=content_type,
        )
    ).parsed
