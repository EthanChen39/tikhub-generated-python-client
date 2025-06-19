from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    group_id: str,
    offset: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["group_id"] = group_id

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/toutiao/app/get_comments",
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
    group_id: str,
    offset: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定作品的评论/Get comments of specified post

     # [中文]
    ### 用途:
    - 获取指定作品的评论
    ### 参数:
    - group_id: 作品ID，可以从链接中获取
        - 例如: https://www.toutiao.com/i7453372680222523931/
    - offset: 偏移量，用于分页，默认为0，然后每次加20
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Get comments of specified post
    ### Parameters:
    - group_id: Post ID, can be obtained from the link
        - For example: https://www.toutiao.com/i7453372680222523931/
    - offset: Offset, used for pagination, default is 0, then add 20 each time
    ### Return:
    - Comment list

    # [示例/Example]
    group_id = \"7453372680222523931\"
    offset = \"0\"

    Args:
        group_id (str): 作品ID/Post ID
        offset (str): 偏移量/Offset

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_id: str,
    offset: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定作品的评论/Get comments of specified post

     # [中文]
    ### 用途:
    - 获取指定作品的评论
    ### 参数:
    - group_id: 作品ID，可以从链接中获取
        - 例如: https://www.toutiao.com/i7453372680222523931/
    - offset: 偏移量，用于分页，默认为0，然后每次加20
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Get comments of specified post
    ### Parameters:
    - group_id: Post ID, can be obtained from the link
        - For example: https://www.toutiao.com/i7453372680222523931/
    - offset: Offset, used for pagination, default is 0, then add 20 each time
    ### Return:
    - Comment list

    # [示例/Example]
    group_id = \"7453372680222523931\"
    offset = \"0\"

    Args:
        group_id (str): 作品ID/Post ID
        offset (str): 偏移量/Offset

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        group_id=group_id,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_id: str,
    offset: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定作品的评论/Get comments of specified post

     # [中文]
    ### 用途:
    - 获取指定作品的评论
    ### 参数:
    - group_id: 作品ID，可以从链接中获取
        - 例如: https://www.toutiao.com/i7453372680222523931/
    - offset: 偏移量，用于分页，默认为0，然后每次加20
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Get comments of specified post
    ### Parameters:
    - group_id: Post ID, can be obtained from the link
        - For example: https://www.toutiao.com/i7453372680222523931/
    - offset: Offset, used for pagination, default is 0, then add 20 each time
    ### Return:
    - Comment list

    # [示例/Example]
    group_id = \"7453372680222523931\"
    offset = \"0\"

    Args:
        group_id (str): 作品ID/Post ID
        offset (str): 偏移量/Offset

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_id: str,
    offset: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定作品的评论/Get comments of specified post

     # [中文]
    ### 用途:
    - 获取指定作品的评论
    ### 参数:
    - group_id: 作品ID，可以从链接中获取
        - 例如: https://www.toutiao.com/i7453372680222523931/
    - offset: 偏移量，用于分页，默认为0，然后每次加20
    ### 返回:
    - 评论列表

    # [English]
    ### Purpose:
    - Get comments of specified post
    ### Parameters:
    - group_id: Post ID, can be obtained from the link
        - For example: https://www.toutiao.com/i7453372680222523931/
    - offset: Offset, used for pagination, default is 0, then add 20 each time
    ### Return:
    - Comment list

    # [示例/Example]
    group_id = \"7453372680222523931\"
    offset = \"0\"

    Args:
        group_id (str): 作品ID/Post ID
        offset (str): 偏移量/Offset

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id=group_id,
            offset=offset,
        )
    ).parsed
