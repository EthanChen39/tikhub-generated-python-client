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
    item_id: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["item_id"] = item_id

    params["offset"] = offset

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xigua/app/v2/fetch_video_comment_list",
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
    item_id: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""视频评论列表/Video comment list

     # [中文]
    ### 用途:
    - 视频评论列表
    ### 参数:
    - item_id: 作品id
    - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset
    - count: 数量，默认20，建议保持默认。
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Video comment list
    ### Parameters:
    - item_id: Video id
    - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for
    subsequent requests
    - count: Quantity, default 20, it is recommended to keep the default.
    ### Return:
    - Comment list

    # [示例/Example]
    item_id: \"7354954305222377999\"

    Args:
        item_id (str): 作品id/Video id
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Count Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        offset=offset,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    item_id: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""视频评论列表/Video comment list

     # [中文]
    ### 用途:
    - 视频评论列表
    ### 参数:
    - item_id: 作品id
    - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset
    - count: 数量，默认20，建议保持默认。
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Video comment list
    ### Parameters:
    - item_id: Video id
    - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for
    subsequent requests
    - count: Quantity, default 20, it is recommended to keep the default.
    ### Return:
    - Comment list

    # [示例/Example]
    item_id: \"7354954305222377999\"

    Args:
        item_id (str): 作品id/Video id
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Count Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        item_id=item_id,
        offset=offset,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    item_id: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""视频评论列表/Video comment list

     # [中文]
    ### 用途:
    - 视频评论列表
    ### 参数:
    - item_id: 作品id
    - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset
    - count: 数量，默认20，建议保持默认。
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Video comment list
    ### Parameters:
    - item_id: Video id
    - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for
    subsequent requests
    - count: Quantity, default 20, it is recommended to keep the default.
    ### Return:
    - Comment list

    # [示例/Example]
    item_id: \"7354954305222377999\"

    Args:
        item_id (str): 作品id/Video id
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Count Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        offset=offset,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    item_id: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""视频评论列表/Video comment list

     # [中文]
    ### 用途:
    - 视频评论列表
    ### 参数:
    - item_id: 作品id
    - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset
    - count: 数量，默认20，建议保持默认。
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Video comment list
    ### Parameters:
    - item_id: Video id
    - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for
    subsequent requests
    - count: Quantity, default 20, it is recommended to keep the default.
    ### Return:
    - Comment list

    # [示例/Example]
    item_id: \"7354954305222377999\"

    Args:
        item_id (str): 作品id/Video id
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Count Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            item_id=item_id,
            offset=offset,
            count=count,
        )
    ).parsed
