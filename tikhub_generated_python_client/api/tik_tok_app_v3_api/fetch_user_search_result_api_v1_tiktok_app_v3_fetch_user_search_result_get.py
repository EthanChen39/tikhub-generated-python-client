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
    user_search_follower_count: Union[Unset, str] = "",
    user_search_profile_type: Union[Unset, str] = "",
    user_search_other_pref: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["offset"] = offset

    params["count"] = count

    params["user_search_follower_count"] = user_search_follower_count

    params["user_search_profile_type"] = user_search_profile_type

    params["user_search_other_pref"] = user_search_other_pref

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_user_search_result",
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
    user_search_follower_count: Union[Unset, str] = "",
    user_search_profile_type: Union[Unset, str] = "",
    user_search_other_pref: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果/Get user search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - user_search_follower_count（根据粉丝数排序）:
        - 空-不限制，
        - ZERO_TO_ONE_K = 0-1K，
        - ONE_K_TO_TEN_K-1K = 1K-10K，
        - TEN_K_TO_ONE_H_K = 10K-100K，
        - ONE_H_K_PLUS = 100K以上
    - user_search_profile_type（根据账号类型排序）:
        - 空-不限制，
        - VERIFIED = 认证用户
    - user_search_other_pref（根据其他偏好排序）:
        - USERNAME = 根据用户名相关性
    ### 返回:
    - 用户搜索结果

    # [English]
    ### Purpose:
    - Get user search results of specified keywords
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - user_search_follower_count（Sort by number of followers）:
        - Empty-Unlimited,
        - ZERO_TO_ONE_K = 0-1K,
        - ONE_K_TO_TEN_K-1K = 1K-10K,
        - TEN_K_TO_ONE_H_K = 10K-100K,
        - ONE_H_K_PLUS = 100K and above
    - user_search_profile_type（Sort by account type）:
        - Empty-Unlimited,
        - VERIFIED = Verified user
    - user_search_other_pref（Sort by other preferences）:
        - USERNAME = Sort by username relevance
    ### Return:
    - User search results

    # [示例/Example]
    keyword = \"Cat\"
    offset = 0
    count = 20
    user_search_follower_count = \"\"
    user_search_profile_type = \"\"
    user_search_other_pref = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        user_search_follower_count (Union[Unset, str]): 根据粉丝数排序/Sort by number of followers
            Default: ''.
        user_search_profile_type (Union[Unset, str]): 根据账号类型排序/Sort by account type Default: ''.
        user_search_other_pref (Union[Unset, str]): 根据其他偏好排序/Sort by other preferences Default:
            ''.

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
        user_search_follower_count=user_search_follower_count,
        user_search_profile_type=user_search_profile_type,
        user_search_other_pref=user_search_other_pref,
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
    user_search_follower_count: Union[Unset, str] = "",
    user_search_profile_type: Union[Unset, str] = "",
    user_search_other_pref: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果/Get user search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - user_search_follower_count（根据粉丝数排序）:
        - 空-不限制，
        - ZERO_TO_ONE_K = 0-1K，
        - ONE_K_TO_TEN_K-1K = 1K-10K，
        - TEN_K_TO_ONE_H_K = 10K-100K，
        - ONE_H_K_PLUS = 100K以上
    - user_search_profile_type（根据账号类型排序）:
        - 空-不限制，
        - VERIFIED = 认证用户
    - user_search_other_pref（根据其他偏好排序）:
        - USERNAME = 根据用户名相关性
    ### 返回:
    - 用户搜索结果

    # [English]
    ### Purpose:
    - Get user search results of specified keywords
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - user_search_follower_count（Sort by number of followers）:
        - Empty-Unlimited,
        - ZERO_TO_ONE_K = 0-1K,
        - ONE_K_TO_TEN_K-1K = 1K-10K,
        - TEN_K_TO_ONE_H_K = 10K-100K,
        - ONE_H_K_PLUS = 100K and above
    - user_search_profile_type（Sort by account type）:
        - Empty-Unlimited,
        - VERIFIED = Verified user
    - user_search_other_pref（Sort by other preferences）:
        - USERNAME = Sort by username relevance
    ### Return:
    - User search results

    # [示例/Example]
    keyword = \"Cat\"
    offset = 0
    count = 20
    user_search_follower_count = \"\"
    user_search_profile_type = \"\"
    user_search_other_pref = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        user_search_follower_count (Union[Unset, str]): 根据粉丝数排序/Sort by number of followers
            Default: ''.
        user_search_profile_type (Union[Unset, str]): 根据账号类型排序/Sort by account type Default: ''.
        user_search_other_pref (Union[Unset, str]): 根据其他偏好排序/Sort by other preferences Default:
            ''.

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
        user_search_follower_count=user_search_follower_count,
        user_search_profile_type=user_search_profile_type,
        user_search_other_pref=user_search_other_pref,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    user_search_follower_count: Union[Unset, str] = "",
    user_search_profile_type: Union[Unset, str] = "",
    user_search_other_pref: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果/Get user search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - user_search_follower_count（根据粉丝数排序）:
        - 空-不限制，
        - ZERO_TO_ONE_K = 0-1K，
        - ONE_K_TO_TEN_K-1K = 1K-10K，
        - TEN_K_TO_ONE_H_K = 10K-100K，
        - ONE_H_K_PLUS = 100K以上
    - user_search_profile_type（根据账号类型排序）:
        - 空-不限制，
        - VERIFIED = 认证用户
    - user_search_other_pref（根据其他偏好排序）:
        - USERNAME = 根据用户名相关性
    ### 返回:
    - 用户搜索结果

    # [English]
    ### Purpose:
    - Get user search results of specified keywords
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - user_search_follower_count（Sort by number of followers）:
        - Empty-Unlimited,
        - ZERO_TO_ONE_K = 0-1K,
        - ONE_K_TO_TEN_K-1K = 1K-10K,
        - TEN_K_TO_ONE_H_K = 10K-100K,
        - ONE_H_K_PLUS = 100K and above
    - user_search_profile_type（Sort by account type）:
        - Empty-Unlimited,
        - VERIFIED = Verified user
    - user_search_other_pref（Sort by other preferences）:
        - USERNAME = Sort by username relevance
    ### Return:
    - User search results

    # [示例/Example]
    keyword = \"Cat\"
    offset = 0
    count = 20
    user_search_follower_count = \"\"
    user_search_profile_type = \"\"
    user_search_other_pref = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        user_search_follower_count (Union[Unset, str]): 根据粉丝数排序/Sort by number of followers
            Default: ''.
        user_search_profile_type (Union[Unset, str]): 根据账号类型排序/Sort by account type Default: ''.
        user_search_other_pref (Union[Unset, str]): 根据其他偏好排序/Sort by other preferences Default:
            ''.

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
        user_search_follower_count=user_search_follower_count,
        user_search_profile_type=user_search_profile_type,
        user_search_other_pref=user_search_other_pref,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    user_search_follower_count: Union[Unset, str] = "",
    user_search_profile_type: Union[Unset, str] = "",
    user_search_other_pref: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果/Get user search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - user_search_follower_count（根据粉丝数排序）:
        - 空-不限制，
        - ZERO_TO_ONE_K = 0-1K，
        - ONE_K_TO_TEN_K-1K = 1K-10K，
        - TEN_K_TO_ONE_H_K = 10K-100K，
        - ONE_H_K_PLUS = 100K以上
    - user_search_profile_type（根据账号类型排序）:
        - 空-不限制，
        - VERIFIED = 认证用户
    - user_search_other_pref（根据其他偏好排序）:
        - USERNAME = 根据用户名相关性
    ### 返回:
    - 用户搜索结果

    # [English]
    ### Purpose:
    - Get user search results of specified keywords
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - user_search_follower_count（Sort by number of followers）:
        - Empty-Unlimited,
        - ZERO_TO_ONE_K = 0-1K,
        - ONE_K_TO_TEN_K-1K = 1K-10K,
        - TEN_K_TO_ONE_H_K = 10K-100K,
        - ONE_H_K_PLUS = 100K and above
    - user_search_profile_type（Sort by account type）:
        - Empty-Unlimited,
        - VERIFIED = Verified user
    - user_search_other_pref（Sort by other preferences）:
        - USERNAME = Sort by username relevance
    ### Return:
    - User search results

    # [示例/Example]
    keyword = \"Cat\"
    offset = 0
    count = 20
    user_search_follower_count = \"\"
    user_search_profile_type = \"\"
    user_search_other_pref = \"\"

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        user_search_follower_count (Union[Unset, str]): 根据粉丝数排序/Sort by number of followers
            Default: ''.
        user_search_profile_type (Union[Unset, str]): 根据账号类型排序/Sort by account type Default: ''.
        user_search_other_pref (Union[Unset, str]): 根据其他偏好排序/Sort by other preferences Default:
            ''.

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
            user_search_follower_count=user_search_follower_count,
            user_search_profile_type=user_search_profile_type,
            user_search_other_pref=user_search_other_pref,
        )
    ).parsed
