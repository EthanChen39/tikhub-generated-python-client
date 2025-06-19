from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    keywords: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
    field_type_: Union[Unset, str] = "1",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keywords"] = keywords

    params["offset"] = offset

    params["limit"] = limit

    params["_type"] = field_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/net_ease_cloud_music/app/search_v1",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    keywords: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
    field_type_: Union[Unset, str] = "1",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""搜索接口V1/Search interface V1

     # [中文]
    ### 用途:
    - 搜索接口V1。
    ### 参数:
    - keywords: 关键词。
    - offset: 偏移量，第一次搜索传递0，第二次传递20，第三次传递40，以此类推。
    - limit: 每页数量，保持默认即可。
    - _type: 搜索类型
        **搜索类型 (`type`)**：
        * 单曲搜索：`\"type\":\"1\"`
        * 歌手搜索：`\"type\":\"100\"`
        * 专辑搜索：`\"type\":\"10\"`
        * 歌单搜索：`\"type\":\"1000\"`
        * MV搜索：`\"type\":\"1004\"`
        * 主播电台搜索：`\"type\":\"1009\"`
        * 用户搜索：`\"type\":\"1002\"`
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search interface V1.
    ### Parameters:
    - keywords: Keywords.
    - offset: Offset, pass 0 for the first search, 20 for the second search, 40 for the third search,
    and so on.
    - limit: Number per page, keep the default.
    - _type: Search type
        **Search type (`type`)**:
        * Single search: `\"type\":\"1\"`
        * Singer search: `\"type\":\"100\"`
        * Album search: `\"type\":\"10\"`
        * Playlist search: `\"type\":\"1000\"`
        * MV search: `\"type\":\"1004\"`
        * Anchor radio search: `\"type\":\"1009\"`
        * User search: `\"type\":\"1002\"`
    ### Returns:
    - Search results

    # [示例/Example]
    keywords = \"周杰伦\"
    offset = \"0\"
    limit = \"20\"
    _type = \"1\"

    Args:
        keywords (str): 关键词/Keywords
        offset (Union[Unset, str]): 偏移量，保持默认即可/Offset, keep the default Default: '0'.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.
        field_type_ (Union[Unset, str]): 搜索类型/Search type Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        keywords=keywords,
        offset=offset,
        limit=limit,
        field_type_=field_type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keywords: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
    field_type_: Union[Unset, str] = "1",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""搜索接口V1/Search interface V1

     # [中文]
    ### 用途:
    - 搜索接口V1。
    ### 参数:
    - keywords: 关键词。
    - offset: 偏移量，第一次搜索传递0，第二次传递20，第三次传递40，以此类推。
    - limit: 每页数量，保持默认即可。
    - _type: 搜索类型
        **搜索类型 (`type`)**：
        * 单曲搜索：`\"type\":\"1\"`
        * 歌手搜索：`\"type\":\"100\"`
        * 专辑搜索：`\"type\":\"10\"`
        * 歌单搜索：`\"type\":\"1000\"`
        * MV搜索：`\"type\":\"1004\"`
        * 主播电台搜索：`\"type\":\"1009\"`
        * 用户搜索：`\"type\":\"1002\"`
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search interface V1.
    ### Parameters:
    - keywords: Keywords.
    - offset: Offset, pass 0 for the first search, 20 for the second search, 40 for the third search,
    and so on.
    - limit: Number per page, keep the default.
    - _type: Search type
        **Search type (`type`)**:
        * Single search: `\"type\":\"1\"`
        * Singer search: `\"type\":\"100\"`
        * Album search: `\"type\":\"10\"`
        * Playlist search: `\"type\":\"1000\"`
        * MV search: `\"type\":\"1004\"`
        * Anchor radio search: `\"type\":\"1009\"`
        * User search: `\"type\":\"1002\"`
    ### Returns:
    - Search results

    # [示例/Example]
    keywords = \"周杰伦\"
    offset = \"0\"
    limit = \"20\"
    _type = \"1\"

    Args:
        keywords (str): 关键词/Keywords
        offset (Union[Unset, str]): 偏移量，保持默认即可/Offset, keep the default Default: '0'.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.
        field_type_ (Union[Unset, str]): 搜索类型/Search type Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        keywords=keywords,
        offset=offset,
        limit=limit,
        field_type_=field_type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keywords: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
    field_type_: Union[Unset, str] = "1",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""搜索接口V1/Search interface V1

     # [中文]
    ### 用途:
    - 搜索接口V1。
    ### 参数:
    - keywords: 关键词。
    - offset: 偏移量，第一次搜索传递0，第二次传递20，第三次传递40，以此类推。
    - limit: 每页数量，保持默认即可。
    - _type: 搜索类型
        **搜索类型 (`type`)**：
        * 单曲搜索：`\"type\":\"1\"`
        * 歌手搜索：`\"type\":\"100\"`
        * 专辑搜索：`\"type\":\"10\"`
        * 歌单搜索：`\"type\":\"1000\"`
        * MV搜索：`\"type\":\"1004\"`
        * 主播电台搜索：`\"type\":\"1009\"`
        * 用户搜索：`\"type\":\"1002\"`
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search interface V1.
    ### Parameters:
    - keywords: Keywords.
    - offset: Offset, pass 0 for the first search, 20 for the second search, 40 for the third search,
    and so on.
    - limit: Number per page, keep the default.
    - _type: Search type
        **Search type (`type`)**:
        * Single search: `\"type\":\"1\"`
        * Singer search: `\"type\":\"100\"`
        * Album search: `\"type\":\"10\"`
        * Playlist search: `\"type\":\"1000\"`
        * MV search: `\"type\":\"1004\"`
        * Anchor radio search: `\"type\":\"1009\"`
        * User search: `\"type\":\"1002\"`
    ### Returns:
    - Search results

    # [示例/Example]
    keywords = \"周杰伦\"
    offset = \"0\"
    limit = \"20\"
    _type = \"1\"

    Args:
        keywords (str): 关键词/Keywords
        offset (Union[Unset, str]): 偏移量，保持默认即可/Offset, keep the default Default: '0'.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.
        field_type_ (Union[Unset, str]): 搜索类型/Search type Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        keywords=keywords,
        offset=offset,
        limit=limit,
        field_type_=field_type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keywords: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
    field_type_: Union[Unset, str] = "1",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""搜索接口V1/Search interface V1

     # [中文]
    ### 用途:
    - 搜索接口V1。
    ### 参数:
    - keywords: 关键词。
    - offset: 偏移量，第一次搜索传递0，第二次传递20，第三次传递40，以此类推。
    - limit: 每页数量，保持默认即可。
    - _type: 搜索类型
        **搜索类型 (`type`)**：
        * 单曲搜索：`\"type\":\"1\"`
        * 歌手搜索：`\"type\":\"100\"`
        * 专辑搜索：`\"type\":\"10\"`
        * 歌单搜索：`\"type\":\"1000\"`
        * MV搜索：`\"type\":\"1004\"`
        * 主播电台搜索：`\"type\":\"1009\"`
        * 用户搜索：`\"type\":\"1002\"`
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search interface V1.
    ### Parameters:
    - keywords: Keywords.
    - offset: Offset, pass 0 for the first search, 20 for the second search, 40 for the third search,
    and so on.
    - limit: Number per page, keep the default.
    - _type: Search type
        **Search type (`type`)**:
        * Single search: `\"type\":\"1\"`
        * Singer search: `\"type\":\"100\"`
        * Album search: `\"type\":\"10\"`
        * Playlist search: `\"type\":\"1000\"`
        * MV search: `\"type\":\"1004\"`
        * Anchor radio search: `\"type\":\"1009\"`
        * User search: `\"type\":\"1002\"`
    ### Returns:
    - Search results

    # [示例/Example]
    keywords = \"周杰伦\"
    offset = \"0\"
    limit = \"20\"
    _type = \"1\"

    Args:
        keywords (str): 关键词/Keywords
        offset (Union[Unset, str]): 偏移量，保持默认即可/Offset, keep the default Default: '0'.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.
        field_type_ (Union[Unset, str]): 搜索类型/Search type Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            keywords=keywords,
            offset=offset,
            limit=limit,
            field_type_=field_type_,
        )
    ).parsed
