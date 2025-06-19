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
    sort_type: Union[Unset, str] = "_0",
    publish_time: Union[Unset, str] = "_0",
    filter_duration: Union[Unset, str] = "_0",
    page: Union[Unset, int] = 1,
    search_id: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["sort_type"] = sort_type

    params["publish_time"] = publish_time

    params["filter_duration"] = filter_duration

    params["page"] = page

    params["search_id"] = search_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/fetch_video_search_result_v2",
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
    sort_type: Union[Unset, str] = "_0",
    publish_time: Union[Unset, str] = "_0",
    filter_duration: Union[Unset, str] = "_0",
    page: Union[Unset, int] = 1,
    search_id: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated,
    see the documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。
    - 收费标准为：0.01$每次请求。
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - sort_type:
        - 排序类型，可用值如下：
        - _0 :综合(General)
        - _1 :最多点赞(More likes)
        - _2 :最新发布(New)
    - publish_time：
        - 发布时间，可用值如下：
        - _0 :不限(No Limit)
        - _1 :一天之内(last 1 day)
        - _7 :一周之内(last 1 week)
        - _180 :半年之内(last half year)
    - filter_duration：
        - 视频时长，可用值如下：
        - _0 :不限(No Limit)
        - _1 :1分钟以下(1 minute and below)
        - _2 :1-5分钟 (1-5 minutes)
        - _3 :5分钟以上(5 minutes more)
    - page: 页码
        - 默认从1开始，然后依次递增加1
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 视频搜索结果V2

    # [English]
    ### Purpose:
    - Get video search results of specified keywords V2, this interface has better stability and higher
    cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is
    recommended to use this interface.
    - The charging standard is: $0.01 per request.
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - sort_type:
        - Sort type, available values are as follows:
        - _0 : General
        - _1 : More likes
        - _2 : New
    - publish_time:
        - Publish time, available values are as follows:
        - _0 : No Limit
        - _1 : last 1 day
        - _7 : last 1 week
        - _180 : last half year
    - filter_duration:
        - Duration filter, available values are as follows:
        - _0 : No Limit
        - _1 : 1 minute and below
        - _2 : 1-5 minutes
        - _3 : 5 minutes more
    - page: Page
        - Start from 1 by default, then increase by 1 each time
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - Video search results V2

    # [示例/Example]
    keyword = \"中华娘\"
    sort_type = \"_0\"
    publish_time = \"_0\"
    filter_duration = \"_0\"
    page = 1
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '_0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '_0'.
        filter_duration (Union[Unset, str]): 视频时长/Duration filter Default: '_0'.
        page (Union[Unset, int]): 页码/Page Default: 1.
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
        sort_type=sort_type,
        publish_time=publish_time,
        filter_duration=filter_duration,
        page=page,
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
    sort_type: Union[Unset, str] = "_0",
    publish_time: Union[Unset, str] = "_0",
    filter_duration: Union[Unset, str] = "_0",
    page: Union[Unset, int] = 1,
    search_id: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated,
    see the documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。
    - 收费标准为：0.01$每次请求。
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - sort_type:
        - 排序类型，可用值如下：
        - _0 :综合(General)
        - _1 :最多点赞(More likes)
        - _2 :最新发布(New)
    - publish_time：
        - 发布时间，可用值如下：
        - _0 :不限(No Limit)
        - _1 :一天之内(last 1 day)
        - _7 :一周之内(last 1 week)
        - _180 :半年之内(last half year)
    - filter_duration：
        - 视频时长，可用值如下：
        - _0 :不限(No Limit)
        - _1 :1分钟以下(1 minute and below)
        - _2 :1-5分钟 (1-5 minutes)
        - _3 :5分钟以上(5 minutes more)
    - page: 页码
        - 默认从1开始，然后依次递增加1
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 视频搜索结果V2

    # [English]
    ### Purpose:
    - Get video search results of specified keywords V2, this interface has better stability and higher
    cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is
    recommended to use this interface.
    - The charging standard is: $0.01 per request.
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - sort_type:
        - Sort type, available values are as follows:
        - _0 : General
        - _1 : More likes
        - _2 : New
    - publish_time:
        - Publish time, available values are as follows:
        - _0 : No Limit
        - _1 : last 1 day
        - _7 : last 1 week
        - _180 : last half year
    - filter_duration:
        - Duration filter, available values are as follows:
        - _0 : No Limit
        - _1 : 1 minute and below
        - _2 : 1-5 minutes
        - _3 : 5 minutes more
    - page: Page
        - Start from 1 by default, then increase by 1 each time
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - Video search results V2

    # [示例/Example]
    keyword = \"中华娘\"
    sort_type = \"_0\"
    publish_time = \"_0\"
    filter_duration = \"_0\"
    page = 1
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '_0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '_0'.
        filter_duration (Union[Unset, str]): 视频时长/Duration filter Default: '_0'.
        page (Union[Unset, int]): 页码/Page Default: 1.
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
        sort_type=sort_type,
        publish_time=publish_time,
        filter_duration=filter_duration,
        page=page,
        search_id=search_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    sort_type: Union[Unset, str] = "_0",
    publish_time: Union[Unset, str] = "_0",
    filter_duration: Union[Unset, str] = "_0",
    page: Union[Unset, int] = 1,
    search_id: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated,
    see the documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。
    - 收费标准为：0.01$每次请求。
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - sort_type:
        - 排序类型，可用值如下：
        - _0 :综合(General)
        - _1 :最多点赞(More likes)
        - _2 :最新发布(New)
    - publish_time：
        - 发布时间，可用值如下：
        - _0 :不限(No Limit)
        - _1 :一天之内(last 1 day)
        - _7 :一周之内(last 1 week)
        - _180 :半年之内(last half year)
    - filter_duration：
        - 视频时长，可用值如下：
        - _0 :不限(No Limit)
        - _1 :1分钟以下(1 minute and below)
        - _2 :1-5分钟 (1-5 minutes)
        - _3 :5分钟以上(5 minutes more)
    - page: 页码
        - 默认从1开始，然后依次递增加1
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 视频搜索结果V2

    # [English]
    ### Purpose:
    - Get video search results of specified keywords V2, this interface has better stability and higher
    cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is
    recommended to use this interface.
    - The charging standard is: $0.01 per request.
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - sort_type:
        - Sort type, available values are as follows:
        - _0 : General
        - _1 : More likes
        - _2 : New
    - publish_time:
        - Publish time, available values are as follows:
        - _0 : No Limit
        - _1 : last 1 day
        - _7 : last 1 week
        - _180 : last half year
    - filter_duration:
        - Duration filter, available values are as follows:
        - _0 : No Limit
        - _1 : 1 minute and below
        - _2 : 1-5 minutes
        - _3 : 5 minutes more
    - page: Page
        - Start from 1 by default, then increase by 1 each time
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - Video search results V2

    # [示例/Example]
    keyword = \"中华娘\"
    sort_type = \"_0\"
    publish_time = \"_0\"
    filter_duration = \"_0\"
    page = 1
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '_0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '_0'.
        filter_duration (Union[Unset, str]): 视频时长/Duration filter Default: '_0'.
        page (Union[Unset, int]): 页码/Page Default: 1.
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
        sort_type=sort_type,
        publish_time=publish_time,
        filter_duration=filter_duration,
        page=page,
        search_id=search_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    sort_type: Union[Unset, str] = "_0",
    publish_time: Union[Unset, str] = "_0",
    filter_duration: Union[Unset, str] = "_0",
    page: Union[Unset, int] = 1,
    search_id: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated,
    see the documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的视频搜索结果V2，此接口稳定性更好，收费更贵，当`/api/v1/douyin/web/fetch_video_search_result`接口不稳定时，建议使用此接口。
    - 收费标准为：0.01$每次请求。
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - sort_type:
        - 排序类型，可用值如下：
        - _0 :综合(General)
        - _1 :最多点赞(More likes)
        - _2 :最新发布(New)
    - publish_time：
        - 发布时间，可用值如下：
        - _0 :不限(No Limit)
        - _1 :一天之内(last 1 day)
        - _7 :一周之内(last 1 week)
        - _180 :半年之内(last half year)
    - filter_duration：
        - 视频时长，可用值如下：
        - _0 :不限(No Limit)
        - _1 :1分钟以下(1 minute and below)
        - _2 :1-5分钟 (1-5 minutes)
        - _3 :5分钟以上(5 minutes more)
    - page: 页码
        - 默认从1开始，然后依次递增加1
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 视频搜索结果V2

    # [English]
    ### Purpose:
    - Get video search results of specified keywords V2, this interface has better stability and higher
    cost, when the `/api/v1/douyin/web/fetch_video_search_result` interface is unstable, it is
    recommended to use this interface.
    - The charging standard is: $0.01 per request.
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - sort_type:
        - Sort type, available values are as follows:
        - _0 : General
        - _1 : More likes
        - _2 : New
    - publish_time:
        - Publish time, available values are as follows:
        - _0 : No Limit
        - _1 : last 1 day
        - _7 : last 1 week
        - _180 : last half year
    - filter_duration:
        - Duration filter, available values are as follows:
        - _0 : No Limit
        - _1 : 1 minute and below
        - _2 : 1-5 minutes
        - _3 : 5 minutes more
    - page: Page
        - Start from 1 by default, then increase by 1 each time
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - Video search results V2

    # [示例/Example]
    keyword = \"中华娘\"
    sort_type = \"_0\"
    publish_time = \"_0\"
    filter_duration = \"_0\"
    page = 1
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        sort_type (Union[Unset, str]): 排序类型/Sort type Default: '_0'.
        publish_time (Union[Unset, str]): 发布时间/Publish time Default: '_0'.
        filter_duration (Union[Unset, str]): 视频时长/Duration filter Default: '_0'.
        page (Union[Unset, int]): 页码/Page Default: 1.
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
            sort_type=sort_type,
            publish_time=publish_time,
            filter_duration=filter_duration,
            page=page,
            search_id=search_id,
        )
    ).parsed
