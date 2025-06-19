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
    cell_id: str,
    cell_type: Union[Unset, int] = 1,
    offset: Union[Unset, str] = "0",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cell_id"] = cell_id

    params["cell_type"] = cell_type

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pipixia/app/fetch_post_comment_list",
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
    cell_id: str,
    cell_type: Union[Unset, int] = 1,
    offset: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品评论列表/Get post comment list

     # [中文]
    ### 用途:
    - 获取作品的评论列表。
    ### 参数:
    - cell_id: 作品id，可以从分享链接中获取。
    - cell_type: 作品类型，1为视频，多大数保持默认值即可。
    - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。
    ### 返回:
    - 作品评论列表

    # [English]
    ### Purpose:
    - Get the comment list of a post.
    ### Parameters:
    - cell_id: AKA video id, can be obtained from the share link.
    - cell_type: Video type, 1 for video, keep the default value for other types.
    - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the
    previous page.
    ### Return:
    - Post comment list

    # [示例/Example]
    cell_id = \"7411193113223371043\"
    cell_type = 1
    offset = \"0\"

    Args:
        cell_id (str): 作品id/Video id
        cell_type (Union[Unset, int]): 作品类型/Video type Default: 1.
        offset (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        cell_id=cell_id,
        cell_type=cell_type,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cell_id: str,
    cell_type: Union[Unset, int] = 1,
    offset: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品评论列表/Get post comment list

     # [中文]
    ### 用途:
    - 获取作品的评论列表。
    ### 参数:
    - cell_id: 作品id，可以从分享链接中获取。
    - cell_type: 作品类型，1为视频，多大数保持默认值即可。
    - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。
    ### 返回:
    - 作品评论列表

    # [English]
    ### Purpose:
    - Get the comment list of a post.
    ### Parameters:
    - cell_id: AKA video id, can be obtained from the share link.
    - cell_type: Video type, 1 for video, keep the default value for other types.
    - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the
    previous page.
    ### Return:
    - Post comment list

    # [示例/Example]
    cell_id = \"7411193113223371043\"
    cell_type = 1
    offset = \"0\"

    Args:
        cell_id (str): 作品id/Video id
        cell_type (Union[Unset, int]): 作品类型/Video type Default: 1.
        offset (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        cell_id=cell_id,
        cell_type=cell_type,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cell_id: str,
    cell_type: Union[Unset, int] = 1,
    offset: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品评论列表/Get post comment list

     # [中文]
    ### 用途:
    - 获取作品的评论列表。
    ### 参数:
    - cell_id: 作品id，可以从分享链接中获取。
    - cell_type: 作品类型，1为视频，多大数保持默认值即可。
    - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。
    ### 返回:
    - 作品评论列表

    # [English]
    ### Purpose:
    - Get the comment list of a post.
    ### Parameters:
    - cell_id: AKA video id, can be obtained from the share link.
    - cell_type: Video type, 1 for video, keep the default value for other types.
    - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the
    previous page.
    ### Return:
    - Post comment list

    # [示例/Example]
    cell_id = \"7411193113223371043\"
    cell_type = 1
    offset = \"0\"

    Args:
        cell_id (str): 作品id/Video id
        cell_type (Union[Unset, int]): 作品类型/Video type Default: 1.
        offset (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        cell_id=cell_id,
        cell_type=cell_type,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cell_id: str,
    cell_type: Union[Unset, int] = 1,
    offset: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品评论列表/Get post comment list

     # [中文]
    ### 用途:
    - 获取作品的评论列表。
    ### 参数:
    - cell_id: 作品id，可以从分享链接中获取。
    - cell_type: 作品类型，1为视频，多大数保持默认值即可。
    - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。
    ### 返回:
    - 作品评论列表

    # [English]
    ### Purpose:
    - Get the comment list of a post.
    ### Parameters:
    - cell_id: AKA video id, can be obtained from the share link.
    - cell_type: Video type, 1 for video, keep the default value for other types.
    - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the
    previous page.
    ### Return:
    - Post comment list

    # [示例/Example]
    cell_id = \"7411193113223371043\"
    cell_type = 1
    offset = \"0\"

    Args:
        cell_id (str): 作品id/Video id
        cell_type (Union[Unset, int]): 作品类型/Video type Default: 1.
        offset (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            cell_id=cell_id,
            cell_type=cell_type,
            offset=offset,
        )
    ).parsed
