from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/billboard/fetch_content_tag",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ResponseModel]:
    if response.status_code == 200:
        response_200 = ResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseModel]:
    r""" 获取垂类内容标签/Fetch vertical content tags

     # [中文]
    ### 用途:
    - 获取垂类内容标签
    ### 参数:
    - 无
    ### 返回:
    - 垂类内容标签
    ### 注意:
    - 该接口用于获取垂类内容标签，用于query_tag参数构建
    ### 示例:
    已知顶级垂类内容标签 `美食`，它的顶级垂类id为 `628`；`美食` 的子垂类标签 `品酒教学`，它的子垂类id为 `62802`。
    那么构建标签查询参数为 `{\"value\": 628, \"children\": [{\"value\": 62808}]}`

    如果需要多个子垂类标签，所有的美食子垂类标签为 `{\"value\":628,\"children\":[{\"value\":62808},{\"value\":62804},{\"value\"
    :62806},{\"value\":62803},{\"value\":62802},{\"value\":62801},{\"value\":62811},{\"value\":62807},{\
    "value\":62805},{\"value\":62810}]}`

    # [English]
    ### Purpose:
    - Get vertical content tags
    ### Parameters:
    - None
    ### Return:
    - Vertical content tags
    ### Note:
    - This interface is used to obtain vertical content tags, used to construct the query_tag parameter
    ### Example:
    Given the top-level vertical content tag `Food`, its top-level vertical id is `628`; `Food`'s sub-
    vertical tag `Wine Tasting`, its sub-vertical id is `62802`.
    Then the constructed tag query parameter is `{\"value\": 628, \"children\": [{\"value\": 62808}]}`

    If you need multiple sub-vertical tags, all food sub-vertical tags are `{\"value\":628,\"children\":
    [{\"value\":62808},{\"value\":62804},{\"value\":62806},{\"value\":62803},{\"value\":62802},{\"value\
    ":62801},{\"value\":62811},{\"value\":62807},{\"value\":62805},{\"value\":62810}]}`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseModel]
     """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[ResponseModel]:
    r""" 获取垂类内容标签/Fetch vertical content tags

     # [中文]
    ### 用途:
    - 获取垂类内容标签
    ### 参数:
    - 无
    ### 返回:
    - 垂类内容标签
    ### 注意:
    - 该接口用于获取垂类内容标签，用于query_tag参数构建
    ### 示例:
    已知顶级垂类内容标签 `美食`，它的顶级垂类id为 `628`；`美食` 的子垂类标签 `品酒教学`，它的子垂类id为 `62802`。
    那么构建标签查询参数为 `{\"value\": 628, \"children\": [{\"value\": 62808}]}`

    如果需要多个子垂类标签，所有的美食子垂类标签为 `{\"value\":628,\"children\":[{\"value\":62808},{\"value\":62804},{\"value\"
    :62806},{\"value\":62803},{\"value\":62802},{\"value\":62801},{\"value\":62811},{\"value\":62807},{\
    "value\":62805},{\"value\":62810}]}`

    # [English]
    ### Purpose:
    - Get vertical content tags
    ### Parameters:
    - None
    ### Return:
    - Vertical content tags
    ### Note:
    - This interface is used to obtain vertical content tags, used to construct the query_tag parameter
    ### Example:
    Given the top-level vertical content tag `Food`, its top-level vertical id is `628`; `Food`'s sub-
    vertical tag `Wine Tasting`, its sub-vertical id is `62802`.
    Then the constructed tag query parameter is `{\"value\": 628, \"children\": [{\"value\": 62808}]}`

    If you need multiple sub-vertical tags, all food sub-vertical tags are `{\"value\":628,\"children\":
    [{\"value\":62808},{\"value\":62804},{\"value\":62806},{\"value\":62803},{\"value\":62802},{\"value\
    ":62801},{\"value\":62811},{\"value\":62807},{\"value\":62805},{\"value\":62810}]}`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseModel
     """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseModel]:
    r""" 获取垂类内容标签/Fetch vertical content tags

     # [中文]
    ### 用途:
    - 获取垂类内容标签
    ### 参数:
    - 无
    ### 返回:
    - 垂类内容标签
    ### 注意:
    - 该接口用于获取垂类内容标签，用于query_tag参数构建
    ### 示例:
    已知顶级垂类内容标签 `美食`，它的顶级垂类id为 `628`；`美食` 的子垂类标签 `品酒教学`，它的子垂类id为 `62802`。
    那么构建标签查询参数为 `{\"value\": 628, \"children\": [{\"value\": 62808}]}`

    如果需要多个子垂类标签，所有的美食子垂类标签为 `{\"value\":628,\"children\":[{\"value\":62808},{\"value\":62804},{\"value\"
    :62806},{\"value\":62803},{\"value\":62802},{\"value\":62801},{\"value\":62811},{\"value\":62807},{\
    "value\":62805},{\"value\":62810}]}`

    # [English]
    ### Purpose:
    - Get vertical content tags
    ### Parameters:
    - None
    ### Return:
    - Vertical content tags
    ### Note:
    - This interface is used to obtain vertical content tags, used to construct the query_tag parameter
    ### Example:
    Given the top-level vertical content tag `Food`, its top-level vertical id is `628`; `Food`'s sub-
    vertical tag `Wine Tasting`, its sub-vertical id is `62802`.
    Then the constructed tag query parameter is `{\"value\": 628, \"children\": [{\"value\": 62808}]}`

    If you need multiple sub-vertical tags, all food sub-vertical tags are `{\"value\":628,\"children\":
    [{\"value\":62808},{\"value\":62804},{\"value\":62806},{\"value\":62803},{\"value\":62802},{\"value\
    ":62801},{\"value\":62811},{\"value\":62807},{\"value\":62805},{\"value\":62810}]}`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseModel]
     """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[ResponseModel]:
    r""" 获取垂类内容标签/Fetch vertical content tags

     # [中文]
    ### 用途:
    - 获取垂类内容标签
    ### 参数:
    - 无
    ### 返回:
    - 垂类内容标签
    ### 注意:
    - 该接口用于获取垂类内容标签，用于query_tag参数构建
    ### 示例:
    已知顶级垂类内容标签 `美食`，它的顶级垂类id为 `628`；`美食` 的子垂类标签 `品酒教学`，它的子垂类id为 `62802`。
    那么构建标签查询参数为 `{\"value\": 628, \"children\": [{\"value\": 62808}]}`

    如果需要多个子垂类标签，所有的美食子垂类标签为 `{\"value\":628,\"children\":[{\"value\":62808},{\"value\":62804},{\"value\"
    :62806},{\"value\":62803},{\"value\":62802},{\"value\":62801},{\"value\":62811},{\"value\":62807},{\
    "value\":62805},{\"value\":62810}]}`

    # [English]
    ### Purpose:
    - Get vertical content tags
    ### Parameters:
    - None
    ### Return:
    - Vertical content tags
    ### Note:
    - This interface is used to obtain vertical content tags, used to construct the query_tag parameter
    ### Example:
    Given the top-level vertical content tag `Food`, its top-level vertical id is `628`; `Food`'s sub-
    vertical tag `Wine Tasting`, its sub-vertical id is `62802`.
    Then the constructed tag query parameter is `{\"value\": 628, \"children\": [{\"value\": 62808}]}`

    If you need multiple sub-vertical tags, all food sub-vertical tags are `{\"value\":628,\"children\":
    [{\"value\":62808},{\"value\":62804},{\"value\":62806},{\"value\":62803},{\"value\":62802},{\"value\
    ":62801},{\"value\":62811},{\"value\":62807},{\"value\":62805},{\"value\":62810}]}`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseModel
     """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
