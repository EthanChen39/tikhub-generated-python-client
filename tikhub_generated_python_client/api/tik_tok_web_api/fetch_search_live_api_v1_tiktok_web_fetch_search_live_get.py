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
    count: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    search_id: Union[Unset, str] = "",
    cookie: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["count"] = count

    params["offset"] = offset

    params["search_id"] = search_id

    params["cookie"] = cookie

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_search_live",
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
    count: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    search_id: Union[Unset, str] = "",
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索直播/Search live

     # [中文]
    ### 用途:
    - 搜索直播
    ### 参数:
    - keyword: 搜索关键词
    - count: 每页数量
    - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供)
    ### 返回:
    - 直播列表

    # [English]
    ### Purpose:
    - Search live
    ### Parameters:
    - keyword: Search keyword
    - count: Number per page
    - offset: Page cursor, 0 for the first request, need to provide for the second paging, generally the
    keyword of this value is offset or cursor.
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    - cookie: User cookie (If you need to search with your own account, or encounter an interface error,
    you can provide the cookie yourself, default is not required)
    ### Return:
    - Live list

    # [示例/Example]
    keyword = \"TikTok\"
    count = 20
    offset = 0
    search_id = \"\"

    Args:
        keyword (str): 搜索关键词/Search keyword
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        offset (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        search_id (Union[Unset, str]): 搜索id，翻页时需要提供/Search id, need to provide when paging
            Default: ''.
        cookie (Union[Unset, str]): 用户cookie(按需提供)/User cookie(if needed)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        count=count,
        offset=offset,
        search_id=search_id,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    count: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    search_id: Union[Unset, str] = "",
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索直播/Search live

     # [中文]
    ### 用途:
    - 搜索直播
    ### 参数:
    - keyword: 搜索关键词
    - count: 每页数量
    - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供)
    ### 返回:
    - 直播列表

    # [English]
    ### Purpose:
    - Search live
    ### Parameters:
    - keyword: Search keyword
    - count: Number per page
    - offset: Page cursor, 0 for the first request, need to provide for the second paging, generally the
    keyword of this value is offset or cursor.
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    - cookie: User cookie (If you need to search with your own account, or encounter an interface error,
    you can provide the cookie yourself, default is not required)
    ### Return:
    - Live list

    # [示例/Example]
    keyword = \"TikTok\"
    count = 20
    offset = 0
    search_id = \"\"

    Args:
        keyword (str): 搜索关键词/Search keyword
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        offset (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        search_id (Union[Unset, str]): 搜索id，翻页时需要提供/Search id, need to provide when paging
            Default: ''.
        cookie (Union[Unset, str]): 用户cookie(按需提供)/User cookie(if needed)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        count=count,
        offset=offset,
        search_id=search_id,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    count: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    search_id: Union[Unset, str] = "",
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索直播/Search live

     # [中文]
    ### 用途:
    - 搜索直播
    ### 参数:
    - keyword: 搜索关键词
    - count: 每页数量
    - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供)
    ### 返回:
    - 直播列表

    # [English]
    ### Purpose:
    - Search live
    ### Parameters:
    - keyword: Search keyword
    - count: Number per page
    - offset: Page cursor, 0 for the first request, need to provide for the second paging, generally the
    keyword of this value is offset or cursor.
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    - cookie: User cookie (If you need to search with your own account, or encounter an interface error,
    you can provide the cookie yourself, default is not required)
    ### Return:
    - Live list

    # [示例/Example]
    keyword = \"TikTok\"
    count = 20
    offset = 0
    search_id = \"\"

    Args:
        keyword (str): 搜索关键词/Search keyword
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        offset (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        search_id (Union[Unset, str]): 搜索id，翻页时需要提供/Search id, need to provide when paging
            Default: ''.
        cookie (Union[Unset, str]): 用户cookie(按需提供)/User cookie(if needed)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        count=count,
        offset=offset,
        search_id=search_id,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    count: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    search_id: Union[Unset, str] = "",
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索直播/Search live

     # [中文]
    ### 用途:
    - 搜索直播
    ### 参数:
    - keyword: 搜索关键词
    - count: 每页数量
    - offset: 翻页游标，第一次请求时为0，第二次请求时从上一次请求的返回响应中获取，一般这个值的关键字为offset或者cursor。
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"20240828035554C02011379EBB6A00E00B\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    - cookie: 用户cookie(如果你需要使用自己的账号搜索，或者遇到接口报错，可以自行提供cookie，默认不需要提供)
    ### 返回:
    - 直播列表

    # [English]
    ### Purpose:
    - Search live
    ### Parameters:
    - keyword: Search keyword
    - count: Number per page
    - offset: Page cursor, 0 for the first request, need to provide for the second paging, generally the
    keyword of this value is offset or cursor.
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"20240828035554C02011379EBB6A00E00B\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    - cookie: User cookie (If you need to search with your own account, or encounter an interface error,
    you can provide the cookie yourself, default is not required)
    ### Return:
    - Live list

    # [示例/Example]
    keyword = \"TikTok\"
    count = 20
    offset = 0
    search_id = \"\"

    Args:
        keyword (str): 搜索关键词/Search keyword
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        offset (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        search_id (Union[Unset, str]): 搜索id，翻页时需要提供/Search id, need to provide when paging
            Default: ''.
        cookie (Union[Unset, str]): 用户cookie(按需提供)/User cookie(if needed)

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
            count=count,
            offset=offset,
            search_id=search_id,
            cookie=cookie,
        )
    ).parsed
