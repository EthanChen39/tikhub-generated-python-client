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
    douyin_user_fans: Union[Unset, str] = "",
    douyin_user_type: Union[Unset, str] = "",
    search_id: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["offset"] = offset

    params["count"] = count

    params["douyin_user_fans"] = douyin_user_fans

    params["douyin_user_type"] = douyin_user_type

    params["search_id"] = search_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_user_search_result",
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
    douyin_user_fans: Union[Unset, str] = "",
    douyin_user_type: Union[Unset, str] = "",
    search_id: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果(废弃，替代接口请参考下方文档)/Get user search results of specified keywords (deprecated, please
    refer to the following document for replacement interface)

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - douyin_user_fans: 留空:不限, \"0_1k\": 1000以下, \"1k_1w\": 1000-1万, \"1w_10w\": 1w-10w, \"10w_100w\":
    10w-100w，\"100w_\": 100w以上
    - douyin_user_type: 留空:不限, \"common_user\": 普通用户, \"enterprise_user\": 企业认证, \"personal_user\": 个人认证
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 用户搜索结果

    # [English]
    ### Purpose:
    - Get user search results of specified keywords
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - douyin_user_fans: Leave blank: Unlimited, \"0_1k\": Below 1000, \"1k_1w\": 1000-10,000,
    \"1w_10w\": 10,000-100,000, \"10w_100w\": 100,000-1 million, \"100w_\": More than 1 million
    - douyin_user_type: Leave blank: Unlimited, \"common_user\": Ordinary user, \"enterprise_user\":
    Enterprise certification, \"personal_user\": Personal certification
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - User search results

    # [示例/Example]
    keyword = \"动漫\"
    offset = 0
    count = 20
    douyin_user_fans = \"\"
    douyin_user_type = \"\"
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        douyin_user_fans (Union[Unset, str]): 粉丝数/Fans Default: ''.
        douyin_user_type (Union[Unset, str]): 用户类型/User type Default: ''.
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
        douyin_user_fans=douyin_user_fans,
        douyin_user_type=douyin_user_type,
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
    douyin_user_fans: Union[Unset, str] = "",
    douyin_user_type: Union[Unset, str] = "",
    search_id: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果(废弃，替代接口请参考下方文档)/Get user search results of specified keywords (deprecated, please
    refer to the following document for replacement interface)

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - douyin_user_fans: 留空:不限, \"0_1k\": 1000以下, \"1k_1w\": 1000-1万, \"1w_10w\": 1w-10w, \"10w_100w\":
    10w-100w，\"100w_\": 100w以上
    - douyin_user_type: 留空:不限, \"common_user\": 普通用户, \"enterprise_user\": 企业认证, \"personal_user\": 个人认证
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 用户搜索结果

    # [English]
    ### Purpose:
    - Get user search results of specified keywords
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - douyin_user_fans: Leave blank: Unlimited, \"0_1k\": Below 1000, \"1k_1w\": 1000-10,000,
    \"1w_10w\": 10,000-100,000, \"10w_100w\": 100,000-1 million, \"100w_\": More than 1 million
    - douyin_user_type: Leave blank: Unlimited, \"common_user\": Ordinary user, \"enterprise_user\":
    Enterprise certification, \"personal_user\": Personal certification
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - User search results

    # [示例/Example]
    keyword = \"动漫\"
    offset = 0
    count = 20
    douyin_user_fans = \"\"
    douyin_user_type = \"\"
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        douyin_user_fans (Union[Unset, str]): 粉丝数/Fans Default: ''.
        douyin_user_type (Union[Unset, str]): 用户类型/User type Default: ''.
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
        douyin_user_fans=douyin_user_fans,
        douyin_user_type=douyin_user_type,
        search_id=search_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    douyin_user_fans: Union[Unset, str] = "",
    douyin_user_type: Union[Unset, str] = "",
    search_id: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果(废弃，替代接口请参考下方文档)/Get user search results of specified keywords (deprecated, please
    refer to the following document for replacement interface)

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - douyin_user_fans: 留空:不限, \"0_1k\": 1000以下, \"1k_1w\": 1000-1万, \"1w_10w\": 1w-10w, \"10w_100w\":
    10w-100w，\"100w_\": 100w以上
    - douyin_user_type: 留空:不限, \"common_user\": 普通用户, \"enterprise_user\": 企业认证, \"personal_user\": 个人认证
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 用户搜索结果

    # [English]
    ### Purpose:
    - Get user search results of specified keywords
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - douyin_user_fans: Leave blank: Unlimited, \"0_1k\": Below 1000, \"1k_1w\": 1000-10,000,
    \"1w_10w\": 10,000-100,000, \"10w_100w\": 100,000-1 million, \"100w_\": More than 1 million
    - douyin_user_type: Leave blank: Unlimited, \"common_user\": Ordinary user, \"enterprise_user\":
    Enterprise certification, \"personal_user\": Personal certification
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - User search results

    # [示例/Example]
    keyword = \"动漫\"
    offset = 0
    count = 20
    douyin_user_fans = \"\"
    douyin_user_type = \"\"
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        douyin_user_fans (Union[Unset, str]): 粉丝数/Fans Default: ''.
        douyin_user_type (Union[Unset, str]): 用户类型/User type Default: ''.
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
        douyin_user_fans=douyin_user_fans,
        douyin_user_type=douyin_user_type,
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
    douyin_user_fans: Union[Unset, str] = "",
    douyin_user_type: Union[Unset, str] = "",
    search_id: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果(废弃，替代接口请参考下方文档)/Get user search results of specified keywords (deprecated, please
    refer to the following document for replacement interface)

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - douyin_user_fans: 留空:不限, \"0_1k\": 1000以下, \"1k_1w\": 1000-1万, \"1w_10w\": 1w-10w, \"10w_100w\":
    10w-100w，\"100w_\": 100w以上
    - douyin_user_type: 留空:不限, \"common_user\": 普通用户, \"enterprise_user\": 企业认证, \"personal_user\": 个人认证
    - search_id: 搜索id，第一次请求时为空，第二次翻页时需要提供，需要从上一次请求的返回响应中获取。
        - 例如: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### 返回:
    - 用户搜索结果

    # [English]
    ### Purpose:
    - Get user search results of specified keywords
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - douyin_user_fans: Leave blank: Unlimited, \"0_1k\": Below 1000, \"1k_1w\": 1000-10,000,
    \"1w_10w\": 10,000-100,000, \"10w_100w\": 100,000-1 million, \"100w_\": More than 1 million
    - douyin_user_type: Leave blank: Unlimited, \"common_user\": Ordinary user, \"enterprise_user\":
    Enterprise certification, \"personal_user\": Personal certification
    - search_id: Search id, empty for the first request, need to provide for the second paging, need to
    get it from the return response of the last request.
        - For example: search_id = \"2024083107320448E367ECDCCC6B71F7F3\"
        - JSON Path-1 : $.data.extra.logid
        - JSON Path-2 : $.data.log_pb.impr_id
    ### Return:
    - User search results

    # [示例/Example]
    keyword = \"动漫\"
    offset = 0
    count = 20
    douyin_user_fans = \"\"
    douyin_user_type = \"\"
    search_id = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        douyin_user_fans (Union[Unset, str]): 粉丝数/Fans Default: ''.
        douyin_user_type (Union[Unset, str]): 用户类型/User type Default: ''.
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
            douyin_user_fans=douyin_user_fans,
            douyin_user_type=douyin_user_type,
            search_id=search_id,
        )
    ).parsed
