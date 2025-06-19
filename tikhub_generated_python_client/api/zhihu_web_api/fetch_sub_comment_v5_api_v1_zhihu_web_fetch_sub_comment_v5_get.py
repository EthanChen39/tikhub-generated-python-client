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
    comment_id: str,
    order_by: Union[Unset, str] = "score",
    limit: Union[Unset, str] = "20",
    offset: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["comment_id"] = comment_id

    params["order_by"] = order_by

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/zhihu/web/fetch_sub_comment_v5",
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
    comment_id: str,
    order_by: Union[Unset, str] = "score",
    limit: Union[Unset, str] = "20",
    offset: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎子评论区V5/Get Zhihu Sub Comment V5

     # [中文]
    ### 用途:
    - 获取知乎子评论区V5
    ### 参数:
    - comment_id: 评论ID
    - order_by: 排序
        - score 最热排序
        - ts 最新排序
    - limit: 每页评论数量
    - offset: 偏移量/页码
    ### 返回:
    - 知乎子评论区V5

    # [English]
    ### Purpose:
    - Get Zhihu Sub Comment V5
    ### Parameters:
    - comment_id: Comment ID
    - order_by: Sort
        - score Hottest Sort
        - ts Latest Sort
    - limit: Number of comments per page
    - offset: Offset/Page Number
    ### Returns:
    - Zhihu Sub Comment V5

    # [示例/Example]
    comment_id = \"11100789728\"
    order_by = \"score\"
    limit = \"20\"
    offset = \"\"

    Args:
        comment_id (str): 评论ID/Comment ID
        order_by (Union[Unset, str]): 排序/Sort Default: 'score'.
        limit (Union[Unset, str]): 每页评论数量/Number of comments per page Default: '20'.
        offset (Union[Unset, str]): 偏移量/Offset Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        comment_id=comment_id,
        order_by=order_by,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    comment_id: str,
    order_by: Union[Unset, str] = "score",
    limit: Union[Unset, str] = "20",
    offset: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎子评论区V5/Get Zhihu Sub Comment V5

     # [中文]
    ### 用途:
    - 获取知乎子评论区V5
    ### 参数:
    - comment_id: 评论ID
    - order_by: 排序
        - score 最热排序
        - ts 最新排序
    - limit: 每页评论数量
    - offset: 偏移量/页码
    ### 返回:
    - 知乎子评论区V5

    # [English]
    ### Purpose:
    - Get Zhihu Sub Comment V5
    ### Parameters:
    - comment_id: Comment ID
    - order_by: Sort
        - score Hottest Sort
        - ts Latest Sort
    - limit: Number of comments per page
    - offset: Offset/Page Number
    ### Returns:
    - Zhihu Sub Comment V5

    # [示例/Example]
    comment_id = \"11100789728\"
    order_by = \"score\"
    limit = \"20\"
    offset = \"\"

    Args:
        comment_id (str): 评论ID/Comment ID
        order_by (Union[Unset, str]): 排序/Sort Default: 'score'.
        limit (Union[Unset, str]): 每页评论数量/Number of comments per page Default: '20'.
        offset (Union[Unset, str]): 偏移量/Offset Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        comment_id=comment_id,
        order_by=order_by,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    comment_id: str,
    order_by: Union[Unset, str] = "score",
    limit: Union[Unset, str] = "20",
    offset: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎子评论区V5/Get Zhihu Sub Comment V5

     # [中文]
    ### 用途:
    - 获取知乎子评论区V5
    ### 参数:
    - comment_id: 评论ID
    - order_by: 排序
        - score 最热排序
        - ts 最新排序
    - limit: 每页评论数量
    - offset: 偏移量/页码
    ### 返回:
    - 知乎子评论区V5

    # [English]
    ### Purpose:
    - Get Zhihu Sub Comment V5
    ### Parameters:
    - comment_id: Comment ID
    - order_by: Sort
        - score Hottest Sort
        - ts Latest Sort
    - limit: Number of comments per page
    - offset: Offset/Page Number
    ### Returns:
    - Zhihu Sub Comment V5

    # [示例/Example]
    comment_id = \"11100789728\"
    order_by = \"score\"
    limit = \"20\"
    offset = \"\"

    Args:
        comment_id (str): 评论ID/Comment ID
        order_by (Union[Unset, str]): 排序/Sort Default: 'score'.
        limit (Union[Unset, str]): 每页评论数量/Number of comments per page Default: '20'.
        offset (Union[Unset, str]): 偏移量/Offset Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        comment_id=comment_id,
        order_by=order_by,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    comment_id: str,
    order_by: Union[Unset, str] = "score",
    limit: Union[Unset, str] = "20",
    offset: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎子评论区V5/Get Zhihu Sub Comment V5

     # [中文]
    ### 用途:
    - 获取知乎子评论区V5
    ### 参数:
    - comment_id: 评论ID
    - order_by: 排序
        - score 最热排序
        - ts 最新排序
    - limit: 每页评论数量
    - offset: 偏移量/页码
    ### 返回:
    - 知乎子评论区V5

    # [English]
    ### Purpose:
    - Get Zhihu Sub Comment V5
    ### Parameters:
    - comment_id: Comment ID
    - order_by: Sort
        - score Hottest Sort
        - ts Latest Sort
    - limit: Number of comments per page
    - offset: Offset/Page Number
    ### Returns:
    - Zhihu Sub Comment V5

    # [示例/Example]
    comment_id = \"11100789728\"
    order_by = \"score\"
    limit = \"20\"
    offset = \"\"

    Args:
        comment_id (str): 评论ID/Comment ID
        order_by (Union[Unset, str]): 排序/Sort Default: 'score'.
        limit (Union[Unset, str]): 每页评论数量/Number of comments per page Default: '20'.
        offset (Union[Unset, str]): 偏移量/Offset Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            comment_id=comment_id,
            order_by=order_by,
            limit=limit,
            offset=offset,
        )
    ).parsed
