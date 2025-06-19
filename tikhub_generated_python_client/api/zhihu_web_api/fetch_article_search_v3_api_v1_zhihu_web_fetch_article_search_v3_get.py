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
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
    show_all_topics: Union[Unset, int] = 0,
    search_source: Union[Unset, str] = "Normal",
    search_hash_id: Union[Unset, str] = "",
    vertical: Union[Unset, str] = "",
    sort: Union[Unset, str] = "",
    time_interval: Union[Unset, str] = "",
    vertical_info: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["offset"] = offset

    params["limit"] = limit

    params["show_all_topics"] = show_all_topics

    params["search_source"] = search_source

    params["search_hash_id"] = search_hash_id

    params["vertical"] = vertical

    params["sort"] = sort

    params["time_interval"] = time_interval

    params["vertical_info"] = vertical_info

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/zhihu/web/fetch_article_search_v3",
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
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
    show_all_topics: Union[Unset, int] = 0,
    search_source: Union[Unset, str] = "Normal",
    search_hash_id: Union[Unset, str] = "",
    vertical: Union[Unset, str] = "",
    sort: Union[Unset, str] = "",
    time_interval: Union[Unset, str] = "",
    vertical_info: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎文章搜索V3/Get Zhihu Article Search V3

     # [中文]
    ### 用途:
    - 获取知乎文章搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页文章数量
    - show_all_topics: 显示所有主题，
        - 0 不显示话题
        - 1 显示话题
    - search_source: 搜索来源
        - Filter 过滤参数生效
        - Normal 为普通结果
    - search_hash_id: 搜索哈希ID，用于过滤重复搜索结果
    - vertical: 空 不限类型
        - answer 只看回答
        - article 只看文章
        - zvideo 只看视频
    - sort: 空 综合排序
        - upvoted_count 最多赞同
        - created_time 最新发布
    - time_interval: 时间间隔
        - 空 不限时间
        - a_day 一天内
        - a_week 一周内
        - a_month 一个月内
        - three_months 三个月内
        - half_a_year 半年内
        - a_year 一年内
    - vertical_info: 垂类信息
        - 0,0,0,0,0,0,0,0,0,0,0,0 不限类型，不会设置勿填
    ### 返回:
    - 知乎文章搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Article Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of articles per page
    - show_all_topics: Show all topics
        - 0 Do not show topics
        - 1 Show topics
    - search_source: Search Source
        - Filter parameter takes effect
        - Normal is normal result
    - search_hash_id: Search Hash ID, used to filter duplicate search results
    - vertical: Empty unlimited type
        - answer only see answers
        - article only see articles
        - zvideo only see videos
    - sort: Empty comprehensive sorting
        - upvoted_count most upvoted
        - created_time latest release
    - time_interval: Time interval
        - Empty unlimited time
        - a_day within a day
        - a_week within a week
        - a_month within a month
        - three_months within three months
        - half_a_year within half a year
        - a_year within a year
    - vertical_info: Vertical information
        - 0,0,0,0,0,0,0,0,0,0,0,0 unlimited type, do not set do not fill
    ### Returns:
    - Zhihu Article Search V3

    # [示例/Example]
    # 默认搜索，综合排序，不限时间
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"20\"
    show_all_topics = 0
    search_source = \"Normal\"
    search_hash_id = \"\"
    vertical = \"\"
    sort = \"\"
    time_interval = \"\"
    vertical_info = \"\"

    # 只看回答，最多赞同，三月内
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"20\"
    show_all_topics = 0
    search_source = \"Filter\"
    search_hash_id = \"\"
    vertical = \"answer\"
    sort = \"upvoted_count\"
    time_interval = \"three_months\"
    vertical_info = \"0,0,0,0,0,0,0,0,0,0,0,0\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '20'.
        show_all_topics (Union[Unset, int]): 显示所有主题/Show all topics Default: 0.
        search_source (Union[Unset, str]): 搜索来源/Search Source Default: 'Normal'.
        search_hash_id (Union[Unset, str]): 搜索哈希ID/Search Hash ID Default: ''.
        vertical (Union[Unset, str]): 垂类/Vertical Type Default: ''.
        sort (Union[Unset, str]): 排序/Sort Default: ''.
        time_interval (Union[Unset, str]): 时间间隔/Time Interval Default: ''.
        vertical_info (Union[Unset, str]): 垂类信息/Vertical Info Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        limit=limit,
        show_all_topics=show_all_topics,
        search_source=search_source,
        search_hash_id=search_hash_id,
        vertical=vertical,
        sort=sort,
        time_interval=time_interval,
        vertical_info=vertical_info,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
    show_all_topics: Union[Unset, int] = 0,
    search_source: Union[Unset, str] = "Normal",
    search_hash_id: Union[Unset, str] = "",
    vertical: Union[Unset, str] = "",
    sort: Union[Unset, str] = "",
    time_interval: Union[Unset, str] = "",
    vertical_info: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎文章搜索V3/Get Zhihu Article Search V3

     # [中文]
    ### 用途:
    - 获取知乎文章搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页文章数量
    - show_all_topics: 显示所有主题，
        - 0 不显示话题
        - 1 显示话题
    - search_source: 搜索来源
        - Filter 过滤参数生效
        - Normal 为普通结果
    - search_hash_id: 搜索哈希ID，用于过滤重复搜索结果
    - vertical: 空 不限类型
        - answer 只看回答
        - article 只看文章
        - zvideo 只看视频
    - sort: 空 综合排序
        - upvoted_count 最多赞同
        - created_time 最新发布
    - time_interval: 时间间隔
        - 空 不限时间
        - a_day 一天内
        - a_week 一周内
        - a_month 一个月内
        - three_months 三个月内
        - half_a_year 半年内
        - a_year 一年内
    - vertical_info: 垂类信息
        - 0,0,0,0,0,0,0,0,0,0,0,0 不限类型，不会设置勿填
    ### 返回:
    - 知乎文章搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Article Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of articles per page
    - show_all_topics: Show all topics
        - 0 Do not show topics
        - 1 Show topics
    - search_source: Search Source
        - Filter parameter takes effect
        - Normal is normal result
    - search_hash_id: Search Hash ID, used to filter duplicate search results
    - vertical: Empty unlimited type
        - answer only see answers
        - article only see articles
        - zvideo only see videos
    - sort: Empty comprehensive sorting
        - upvoted_count most upvoted
        - created_time latest release
    - time_interval: Time interval
        - Empty unlimited time
        - a_day within a day
        - a_week within a week
        - a_month within a month
        - three_months within three months
        - half_a_year within half a year
        - a_year within a year
    - vertical_info: Vertical information
        - 0,0,0,0,0,0,0,0,0,0,0,0 unlimited type, do not set do not fill
    ### Returns:
    - Zhihu Article Search V3

    # [示例/Example]
    # 默认搜索，综合排序，不限时间
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"20\"
    show_all_topics = 0
    search_source = \"Normal\"
    search_hash_id = \"\"
    vertical = \"\"
    sort = \"\"
    time_interval = \"\"
    vertical_info = \"\"

    # 只看回答，最多赞同，三月内
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"20\"
    show_all_topics = 0
    search_source = \"Filter\"
    search_hash_id = \"\"
    vertical = \"answer\"
    sort = \"upvoted_count\"
    time_interval = \"three_months\"
    vertical_info = \"0,0,0,0,0,0,0,0,0,0,0,0\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '20'.
        show_all_topics (Union[Unset, int]): 显示所有主题/Show all topics Default: 0.
        search_source (Union[Unset, str]): 搜索来源/Search Source Default: 'Normal'.
        search_hash_id (Union[Unset, str]): 搜索哈希ID/Search Hash ID Default: ''.
        vertical (Union[Unset, str]): 垂类/Vertical Type Default: ''.
        sort (Union[Unset, str]): 排序/Sort Default: ''.
        time_interval (Union[Unset, str]): 时间间隔/Time Interval Default: ''.
        vertical_info (Union[Unset, str]): 垂类信息/Vertical Info Default: ''.

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
        limit=limit,
        show_all_topics=show_all_topics,
        search_source=search_source,
        search_hash_id=search_hash_id,
        vertical=vertical,
        sort=sort,
        time_interval=time_interval,
        vertical_info=vertical_info,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
    show_all_topics: Union[Unset, int] = 0,
    search_source: Union[Unset, str] = "Normal",
    search_hash_id: Union[Unset, str] = "",
    vertical: Union[Unset, str] = "",
    sort: Union[Unset, str] = "",
    time_interval: Union[Unset, str] = "",
    vertical_info: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎文章搜索V3/Get Zhihu Article Search V3

     # [中文]
    ### 用途:
    - 获取知乎文章搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页文章数量
    - show_all_topics: 显示所有主题，
        - 0 不显示话题
        - 1 显示话题
    - search_source: 搜索来源
        - Filter 过滤参数生效
        - Normal 为普通结果
    - search_hash_id: 搜索哈希ID，用于过滤重复搜索结果
    - vertical: 空 不限类型
        - answer 只看回答
        - article 只看文章
        - zvideo 只看视频
    - sort: 空 综合排序
        - upvoted_count 最多赞同
        - created_time 最新发布
    - time_interval: 时间间隔
        - 空 不限时间
        - a_day 一天内
        - a_week 一周内
        - a_month 一个月内
        - three_months 三个月内
        - half_a_year 半年内
        - a_year 一年内
    - vertical_info: 垂类信息
        - 0,0,0,0,0,0,0,0,0,0,0,0 不限类型，不会设置勿填
    ### 返回:
    - 知乎文章搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Article Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of articles per page
    - show_all_topics: Show all topics
        - 0 Do not show topics
        - 1 Show topics
    - search_source: Search Source
        - Filter parameter takes effect
        - Normal is normal result
    - search_hash_id: Search Hash ID, used to filter duplicate search results
    - vertical: Empty unlimited type
        - answer only see answers
        - article only see articles
        - zvideo only see videos
    - sort: Empty comprehensive sorting
        - upvoted_count most upvoted
        - created_time latest release
    - time_interval: Time interval
        - Empty unlimited time
        - a_day within a day
        - a_week within a week
        - a_month within a month
        - three_months within three months
        - half_a_year within half a year
        - a_year within a year
    - vertical_info: Vertical information
        - 0,0,0,0,0,0,0,0,0,0,0,0 unlimited type, do not set do not fill
    ### Returns:
    - Zhihu Article Search V3

    # [示例/Example]
    # 默认搜索，综合排序，不限时间
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"20\"
    show_all_topics = 0
    search_source = \"Normal\"
    search_hash_id = \"\"
    vertical = \"\"
    sort = \"\"
    time_interval = \"\"
    vertical_info = \"\"

    # 只看回答，最多赞同，三月内
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"20\"
    show_all_topics = 0
    search_source = \"Filter\"
    search_hash_id = \"\"
    vertical = \"answer\"
    sort = \"upvoted_count\"
    time_interval = \"three_months\"
    vertical_info = \"0,0,0,0,0,0,0,0,0,0,0,0\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '20'.
        show_all_topics (Union[Unset, int]): 显示所有主题/Show all topics Default: 0.
        search_source (Union[Unset, str]): 搜索来源/Search Source Default: 'Normal'.
        search_hash_id (Union[Unset, str]): 搜索哈希ID/Search Hash ID Default: ''.
        vertical (Union[Unset, str]): 垂类/Vertical Type Default: ''.
        sort (Union[Unset, str]): 排序/Sort Default: ''.
        time_interval (Union[Unset, str]): 时间间隔/Time Interval Default: ''.
        vertical_info (Union[Unset, str]): 垂类信息/Vertical Info Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        limit=limit,
        show_all_topics=show_all_topics,
        search_source=search_source,
        search_hash_id=search_hash_id,
        vertical=vertical,
        sort=sort,
        time_interval=time_interval,
        vertical_info=vertical_info,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
    show_all_topics: Union[Unset, int] = 0,
    search_source: Union[Unset, str] = "Normal",
    search_hash_id: Union[Unset, str] = "",
    vertical: Union[Unset, str] = "",
    sort: Union[Unset, str] = "",
    time_interval: Union[Unset, str] = "",
    vertical_info: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎文章搜索V3/Get Zhihu Article Search V3

     # [中文]
    ### 用途:
    - 获取知乎文章搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页文章数量
    - show_all_topics: 显示所有主题，
        - 0 不显示话题
        - 1 显示话题
    - search_source: 搜索来源
        - Filter 过滤参数生效
        - Normal 为普通结果
    - search_hash_id: 搜索哈希ID，用于过滤重复搜索结果
    - vertical: 空 不限类型
        - answer 只看回答
        - article 只看文章
        - zvideo 只看视频
    - sort: 空 综合排序
        - upvoted_count 最多赞同
        - created_time 最新发布
    - time_interval: 时间间隔
        - 空 不限时间
        - a_day 一天内
        - a_week 一周内
        - a_month 一个月内
        - three_months 三个月内
        - half_a_year 半年内
        - a_year 一年内
    - vertical_info: 垂类信息
        - 0,0,0,0,0,0,0,0,0,0,0,0 不限类型，不会设置勿填
    ### 返回:
    - 知乎文章搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Article Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of articles per page
    - show_all_topics: Show all topics
        - 0 Do not show topics
        - 1 Show topics
    - search_source: Search Source
        - Filter parameter takes effect
        - Normal is normal result
    - search_hash_id: Search Hash ID, used to filter duplicate search results
    - vertical: Empty unlimited type
        - answer only see answers
        - article only see articles
        - zvideo only see videos
    - sort: Empty comprehensive sorting
        - upvoted_count most upvoted
        - created_time latest release
    - time_interval: Time interval
        - Empty unlimited time
        - a_day within a day
        - a_week within a week
        - a_month within a month
        - three_months within three months
        - half_a_year within half a year
        - a_year within a year
    - vertical_info: Vertical information
        - 0,0,0,0,0,0,0,0,0,0,0,0 unlimited type, do not set do not fill
    ### Returns:
    - Zhihu Article Search V3

    # [示例/Example]
    # 默认搜索，综合排序，不限时间
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"20\"
    show_all_topics = 0
    search_source = \"Normal\"
    search_hash_id = \"\"
    vertical = \"\"
    sort = \"\"
    time_interval = \"\"
    vertical_info = \"\"

    # 只看回答，最多赞同，三月内
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"20\"
    show_all_topics = 0
    search_source = \"Filter\"
    search_hash_id = \"\"
    vertical = \"answer\"
    sort = \"upvoted_count\"
    time_interval = \"three_months\"
    vertical_info = \"0,0,0,0,0,0,0,0,0,0,0,0\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '20'.
        show_all_topics (Union[Unset, int]): 显示所有主题/Show all topics Default: 0.
        search_source (Union[Unset, str]): 搜索来源/Search Source Default: 'Normal'.
        search_hash_id (Union[Unset, str]): 搜索哈希ID/Search Hash ID Default: ''.
        vertical (Union[Unset, str]): 垂类/Vertical Type Default: ''.
        sort (Union[Unset, str]): 排序/Sort Default: ''.
        time_interval (Union[Unset, str]): 时间间隔/Time Interval Default: ''.
        vertical_info (Union[Unset, str]): 垂类信息/Vertical Info Default: ''.

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
            limit=limit,
            show_all_topics=show_all_topics,
            search_source=search_source,
            search_hash_id=search_hash_id,
            vertical=vertical,
            sort=sort,
            time_interval=time_interval,
            vertical_info=vertical_info,
        )
    ).parsed
