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
    url_query: str,
    comment_id: Union[Unset, str] = "",
    offset: Union[Unset, str] = "0",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["url"] = url_query

    params["comment_id"] = comment_id

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/wechat_mp/web/fetch_mp_article_comment_list",
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
    url_query: str,
    comment_id: Union[Unset, str] = "",
    offset: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号文章评论列表/Get Wechat MP Article Comment List

     # [中文]
    ### 用途:
    - 获取微信公众号文章评论列表
    ### 参数:
    - url: 文章链接
    - comment_id: 评论ID
    - offset: 偏移量
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Get Wechat MP Article Comment List
    ### Parameters:
    - url: Article URL
    - comment_id: Comment ID
    - offset: Offset
    ### Returns:
    - Comment List

    # [示例/Example]
    url = \"https://mp.weixin.qq.com/s/Ko5V9jw9kwL8TO6Q7J3UqQ\"
    comment_id = \"\"
    offset = \"0\"

    Args:
        url_query (str): 文章链接/Article URL
        comment_id (Union[Unset, str]): 评论ID/Comment ID Default: ''.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
        comment_id=comment_id,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    url_query: str,
    comment_id: Union[Unset, str] = "",
    offset: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号文章评论列表/Get Wechat MP Article Comment List

     # [中文]
    ### 用途:
    - 获取微信公众号文章评论列表
    ### 参数:
    - url: 文章链接
    - comment_id: 评论ID
    - offset: 偏移量
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Get Wechat MP Article Comment List
    ### Parameters:
    - url: Article URL
    - comment_id: Comment ID
    - offset: Offset
    ### Returns:
    - Comment List

    # [示例/Example]
    url = \"https://mp.weixin.qq.com/s/Ko5V9jw9kwL8TO6Q7J3UqQ\"
    comment_id = \"\"
    offset = \"0\"

    Args:
        url_query (str): 文章链接/Article URL
        comment_id (Union[Unset, str]): 评论ID/Comment ID Default: ''.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        url_query=url_query,
        comment_id=comment_id,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    url_query: str,
    comment_id: Union[Unset, str] = "",
    offset: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号文章评论列表/Get Wechat MP Article Comment List

     # [中文]
    ### 用途:
    - 获取微信公众号文章评论列表
    ### 参数:
    - url: 文章链接
    - comment_id: 评论ID
    - offset: 偏移量
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Get Wechat MP Article Comment List
    ### Parameters:
    - url: Article URL
    - comment_id: Comment ID
    - offset: Offset
    ### Returns:
    - Comment List

    # [示例/Example]
    url = \"https://mp.weixin.qq.com/s/Ko5V9jw9kwL8TO6Q7J3UqQ\"
    comment_id = \"\"
    offset = \"0\"

    Args:
        url_query (str): 文章链接/Article URL
        comment_id (Union[Unset, str]): 评论ID/Comment ID Default: ''.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
        comment_id=comment_id,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    url_query: str,
    comment_id: Union[Unset, str] = "",
    offset: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号文章评论列表/Get Wechat MP Article Comment List

     # [中文]
    ### 用途:
    - 获取微信公众号文章评论列表
    ### 参数:
    - url: 文章链接
    - comment_id: 评论ID
    - offset: 偏移量
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Get Wechat MP Article Comment List
    ### Parameters:
    - url: Article URL
    - comment_id: Comment ID
    - offset: Offset
    ### Returns:
    - Comment List

    # [示例/Example]
    url = \"https://mp.weixin.qq.com/s/Ko5V9jw9kwL8TO6Q7J3UqQ\"
    comment_id = \"\"
    offset = \"0\"

    Args:
        url_query (str): 文章链接/Article URL
        comment_id (Union[Unset, str]): 评论ID/Comment ID Default: ''.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            url_query=url_query,
            comment_id=comment_id,
            offset=offset,
        )
    ).parsed
