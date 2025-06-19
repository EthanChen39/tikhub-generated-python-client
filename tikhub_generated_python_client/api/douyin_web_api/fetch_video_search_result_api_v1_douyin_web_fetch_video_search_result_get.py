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
    search_id: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["offset"] = offset

    params["count"] = count

    params["sort_type"] = sort_type

    params["publish_time"] = publish_time

    params["filter_duration"] = filter_duration

    params["search_id"] = search_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_video_search_result",
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
    search_id: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的视频搜索结果/Get video search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的视频搜索结果，此接口有概率失败，如果失败请使用同样的参数重新请求 1-3次，目前的失败率在5%以下。
    - 此接口收费相较于其他搜索接口便宜，但是稳定性差，需要配合重试机制使用。
    - 请求价格：0.001$ / 次
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量，第一次请求时为0，后续从返回数据中获取，用于翻页。
        - 例如: offset = 10
        - JSON Path-1 : $.data.cursor
    - count: 数量，默认为10，建议保持不变。
    - sort_type:
        - 0:综合排序
        - 1:最多点赞
        - 2:最新发布
    - publish_time:
        - 0:不限
        - 1:最近一天
        - 7:最近一周
        - 180:最近半年
    - filter_duration:
        - 0:不限 0-1:1分钟以内
        - 1-5:1-5分钟
        - 5-10000:5分钟以上
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 视频搜索结果

    # [English]
    ### Purpose:
    - Get video search results of specified keywords, this interface may fail, if it fails, please use
    the same parameters to request 1-3 times again, the current failure rate is below 5%.
    - This interface is cheaper than other search interfaces, but the stability is poor and needs to be
    used with a retry mechanism.
    - Request price: 0.001$ / time
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset, 0 for the first request, get from the returned data later, used for paging.
        - For example: offset = 10
        - JSON Path-1 : $.data.cursor
    - count: Number, default is 10, it is recommended to keep it unchanged.
    - sort_type:
        - 0: Comprehensive sorting
        - 1: Most likes
        - 2: Latest release
    - publish_time:
        - 0: Unlimited
        - 1: Last day
        - 7: Last week
        - 180: Last half year
    - filter_duration:
        - 0: Unlimited
        - 0-1: Within 1 minute
        - 1-5: 1-5 minutes
        - 5-10000: More than 5 minutes
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - Video search results

    # [示例/Example]
    keyword = \"游戏\"
    offset = 0
    count = 10
    sort_type = \"0\"
    publish_time = \"0\"
    filter_duration = \"0\"
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '0'.
        filter_duration (Union[Unset, str]): 视频时长/Duration filter Default: '0'.
        search_id (Union[Unset, str]): 搜索id，翻页时需要提供/Search id, need to provide when paging
            Default: ''.

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
        search_id=search_id,
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
    search_id: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的视频搜索结果/Get video search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的视频搜索结果，此接口有概率失败，如果失败请使用同样的参数重新请求 1-3次，目前的失败率在5%以下。
    - 此接口收费相较于其他搜索接口便宜，但是稳定性差，需要配合重试机制使用。
    - 请求价格：0.001$ / 次
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量，第一次请求时为0，后续从返回数据中获取，用于翻页。
        - 例如: offset = 10
        - JSON Path-1 : $.data.cursor
    - count: 数量，默认为10，建议保持不变。
    - sort_type:
        - 0:综合排序
        - 1:最多点赞
        - 2:最新发布
    - publish_time:
        - 0:不限
        - 1:最近一天
        - 7:最近一周
        - 180:最近半年
    - filter_duration:
        - 0:不限 0-1:1分钟以内
        - 1-5:1-5分钟
        - 5-10000:5分钟以上
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 视频搜索结果

    # [English]
    ### Purpose:
    - Get video search results of specified keywords, this interface may fail, if it fails, please use
    the same parameters to request 1-3 times again, the current failure rate is below 5%.
    - This interface is cheaper than other search interfaces, but the stability is poor and needs to be
    used with a retry mechanism.
    - Request price: 0.001$ / time
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset, 0 for the first request, get from the returned data later, used for paging.
        - For example: offset = 10
        - JSON Path-1 : $.data.cursor
    - count: Number, default is 10, it is recommended to keep it unchanged.
    - sort_type:
        - 0: Comprehensive sorting
        - 1: Most likes
        - 2: Latest release
    - publish_time:
        - 0: Unlimited
        - 1: Last day
        - 7: Last week
        - 180: Last half year
    - filter_duration:
        - 0: Unlimited
        - 0-1: Within 1 minute
        - 1-5: 1-5 minutes
        - 5-10000: More than 5 minutes
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - Video search results

    # [示例/Example]
    keyword = \"游戏\"
    offset = 0
    count = 10
    sort_type = \"0\"
    publish_time = \"0\"
    filter_duration = \"0\"
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '0'.
        filter_duration (Union[Unset, str]): 视频时长/Duration filter Default: '0'.
        search_id (Union[Unset, str]): 搜索id，翻页时需要提供/Search id, need to provide when paging
            Default: ''.

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
        search_id=search_id,
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
    search_id: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的视频搜索结果/Get video search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的视频搜索结果，此接口有概率失败，如果失败请使用同样的参数重新请求 1-3次，目前的失败率在5%以下。
    - 此接口收费相较于其他搜索接口便宜，但是稳定性差，需要配合重试机制使用。
    - 请求价格：0.001$ / 次
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量，第一次请求时为0，后续从返回数据中获取，用于翻页。
        - 例如: offset = 10
        - JSON Path-1 : $.data.cursor
    - count: 数量，默认为10，建议保持不变。
    - sort_type:
        - 0:综合排序
        - 1:最多点赞
        - 2:最新发布
    - publish_time:
        - 0:不限
        - 1:最近一天
        - 7:最近一周
        - 180:最近半年
    - filter_duration:
        - 0:不限 0-1:1分钟以内
        - 1-5:1-5分钟
        - 5-10000:5分钟以上
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 视频搜索结果

    # [English]
    ### Purpose:
    - Get video search results of specified keywords, this interface may fail, if it fails, please use
    the same parameters to request 1-3 times again, the current failure rate is below 5%.
    - This interface is cheaper than other search interfaces, but the stability is poor and needs to be
    used with a retry mechanism.
    - Request price: 0.001$ / time
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset, 0 for the first request, get from the returned data later, used for paging.
        - For example: offset = 10
        - JSON Path-1 : $.data.cursor
    - count: Number, default is 10, it is recommended to keep it unchanged.
    - sort_type:
        - 0: Comprehensive sorting
        - 1: Most likes
        - 2: Latest release
    - publish_time:
        - 0: Unlimited
        - 1: Last day
        - 7: Last week
        - 180: Last half year
    - filter_duration:
        - 0: Unlimited
        - 0-1: Within 1 minute
        - 1-5: 1-5 minutes
        - 5-10000: More than 5 minutes
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - Video search results

    # [示例/Example]
    keyword = \"游戏\"
    offset = 0
    count = 10
    sort_type = \"0\"
    publish_time = \"0\"
    filter_duration = \"0\"
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '0'.
        filter_duration (Union[Unset, str]): 视频时长/Duration filter Default: '0'.
        search_id (Union[Unset, str]): 搜索id，翻页时需要提供/Search id, need to provide when paging
            Default: ''.

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
        search_id=search_id,
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
    search_id: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的视频搜索结果/Get video search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的视频搜索结果，此接口有概率失败，如果失败请使用同样的参数重新请求 1-3次，目前的失败率在5%以下。
    - 此接口收费相较于其他搜索接口便宜，但是稳定性差，需要配合重试机制使用。
    - 请求价格：0.001$ / 次
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量，第一次请求时为0，后续从返回数据中获取，用于翻页。
        - 例如: offset = 10
        - JSON Path-1 : $.data.cursor
    - count: 数量，默认为10，建议保持不变。
    - sort_type:
        - 0:综合排序
        - 1:最多点赞
        - 2:最新发布
    - publish_time:
        - 0:不限
        - 1:最近一天
        - 7:最近一周
        - 180:最近半年
    - filter_duration:
        - 0:不限 0-1:1分钟以内
        - 1-5:1-5分钟
        - 5-10000:5分钟以上
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 视频搜索结果

    # [English]
    ### Purpose:
    - Get video search results of specified keywords, this interface may fail, if it fails, please use
    the same parameters to request 1-3 times again, the current failure rate is below 5%.
    - This interface is cheaper than other search interfaces, but the stability is poor and needs to be
    used with a retry mechanism.
    - Request price: 0.001$ / time
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset, 0 for the first request, get from the returned data later, used for paging.
        - For example: offset = 10
        - JSON Path-1 : $.data.cursor
    - count: Number, default is 10, it is recommended to keep it unchanged.
    - sort_type:
        - 0: Comprehensive sorting
        - 1: Most likes
        - 2: Latest release
    - publish_time:
        - 0: Unlimited
        - 1: Last day
        - 7: Last week
        - 180: Last half year
    - filter_duration:
        - 0: Unlimited
        - 0-1: Within 1 minute
        - 1-5: 1-5 minutes
        - 5-10000: More than 5 minutes
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - Video search results

    # [示例/Example]
    keyword = \"游戏\"
    offset = 0
    count = 10
    sort_type = \"0\"
    publish_time = \"0\"
    filter_duration = \"0\"
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '0'.
        filter_duration (Union[Unset, str]): 视频时长/Duration filter Default: '0'.
        search_id (Union[Unset, str]): 搜索id，翻页时需要提供/Search id, need to provide when paging
            Default: ''.

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
            search_id=search_id,
        )
    ).parsed
