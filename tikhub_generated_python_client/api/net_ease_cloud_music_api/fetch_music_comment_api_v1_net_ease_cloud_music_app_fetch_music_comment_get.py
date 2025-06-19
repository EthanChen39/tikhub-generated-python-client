from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    resource_id: str,
    before_time: Union[Unset, str] = "",
    limit: Union[Unset, str] = "30",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["resource_id"] = resource_id

    params["beforeTime"] = before_time

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/net_ease_cloud_music/app/fetch_music_comment",
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
    resource_id: str,
    before_time: Union[Unset, str] = "",
    limit: Union[Unset, str] = "30",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取歌曲评论/Fetch music comment

     # [中文]
    ### 用途:
    - 获取歌曲评论。
    ### 参数:
    - resource_id: 资源ID，可以是歌曲ID，专辑ID等。
    - beforeTime: 时间戳，用于翻页，第一页不需要传递，第二页传递第一页返回的最后一条评论的时间戳，或者查看返回的Next_Page_beforeTime字段。
    - limit: 每页数量，默认为30。
    ### 返回:
    - 歌曲评论

    # [English]
    ### Purpose:
    - Fetch music comment.
    ### Parameters:
    - resource_id: Resource ID, can be song ID, album ID, etc.
    - beforeTime: Time stamp, used for paging, no need to pass on the first page, pass the time stamp of
    the last comment returned on the first page on the second page, or check the Next_Page_beforeTime
    field returned.
    - limit: Number per page, default is 30.
    ### Returns:
    - Music comment

    # [示例/Example]
    resource_id = \"2135155051\"
    beforeTime = \"0\"
    limit = \"30\"

    Args:
        resource_id (str): 资源ID/Resource ID
        before_time (Union[Unset, str]): 时间戳，用于翻页，第一页不需要传递/Time stamp, used for paging, no need to
            pass on the first page Default: ''.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '30'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        before_time=before_time,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    resource_id: str,
    before_time: Union[Unset, str] = "",
    limit: Union[Unset, str] = "30",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取歌曲评论/Fetch music comment

     # [中文]
    ### 用途:
    - 获取歌曲评论。
    ### 参数:
    - resource_id: 资源ID，可以是歌曲ID，专辑ID等。
    - beforeTime: 时间戳，用于翻页，第一页不需要传递，第二页传递第一页返回的最后一条评论的时间戳，或者查看返回的Next_Page_beforeTime字段。
    - limit: 每页数量，默认为30。
    ### 返回:
    - 歌曲评论

    # [English]
    ### Purpose:
    - Fetch music comment.
    ### Parameters:
    - resource_id: Resource ID, can be song ID, album ID, etc.
    - beforeTime: Time stamp, used for paging, no need to pass on the first page, pass the time stamp of
    the last comment returned on the first page on the second page, or check the Next_Page_beforeTime
    field returned.
    - limit: Number per page, default is 30.
    ### Returns:
    - Music comment

    # [示例/Example]
    resource_id = \"2135155051\"
    beforeTime = \"0\"
    limit = \"30\"

    Args:
        resource_id (str): 资源ID/Resource ID
        before_time (Union[Unset, str]): 时间戳，用于翻页，第一页不需要传递/Time stamp, used for paging, no need to
            pass on the first page Default: ''.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '30'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        resource_id=resource_id,
        before_time=before_time,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    resource_id: str,
    before_time: Union[Unset, str] = "",
    limit: Union[Unset, str] = "30",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取歌曲评论/Fetch music comment

     # [中文]
    ### 用途:
    - 获取歌曲评论。
    ### 参数:
    - resource_id: 资源ID，可以是歌曲ID，专辑ID等。
    - beforeTime: 时间戳，用于翻页，第一页不需要传递，第二页传递第一页返回的最后一条评论的时间戳，或者查看返回的Next_Page_beforeTime字段。
    - limit: 每页数量，默认为30。
    ### 返回:
    - 歌曲评论

    # [English]
    ### Purpose:
    - Fetch music comment.
    ### Parameters:
    - resource_id: Resource ID, can be song ID, album ID, etc.
    - beforeTime: Time stamp, used for paging, no need to pass on the first page, pass the time stamp of
    the last comment returned on the first page on the second page, or check the Next_Page_beforeTime
    field returned.
    - limit: Number per page, default is 30.
    ### Returns:
    - Music comment

    # [示例/Example]
    resource_id = \"2135155051\"
    beforeTime = \"0\"
    limit = \"30\"

    Args:
        resource_id (str): 资源ID/Resource ID
        before_time (Union[Unset, str]): 时间戳，用于翻页，第一页不需要传递/Time stamp, used for paging, no need to
            pass on the first page Default: ''.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '30'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        resource_id=resource_id,
        before_time=before_time,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    resource_id: str,
    before_time: Union[Unset, str] = "",
    limit: Union[Unset, str] = "30",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取歌曲评论/Fetch music comment

     # [中文]
    ### 用途:
    - 获取歌曲评论。
    ### 参数:
    - resource_id: 资源ID，可以是歌曲ID，专辑ID等。
    - beforeTime: 时间戳，用于翻页，第一页不需要传递，第二页传递第一页返回的最后一条评论的时间戳，或者查看返回的Next_Page_beforeTime字段。
    - limit: 每页数量，默认为30。
    ### 返回:
    - 歌曲评论

    # [English]
    ### Purpose:
    - Fetch music comment.
    ### Parameters:
    - resource_id: Resource ID, can be song ID, album ID, etc.
    - beforeTime: Time stamp, used for paging, no need to pass on the first page, pass the time stamp of
    the last comment returned on the first page on the second page, or check the Next_Page_beforeTime
    field returned.
    - limit: Number per page, default is 30.
    ### Returns:
    - Music comment

    # [示例/Example]
    resource_id = \"2135155051\"
    beforeTime = \"0\"
    limit = \"30\"

    Args:
        resource_id (str): 资源ID/Resource ID
        before_time (Union[Unset, str]): 时间戳，用于翻页，第一页不需要传递/Time stamp, used for paging, no need to
            pass on the first page Default: ''.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '30'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            resource_id=resource_id,
            before_time=before_time,
            limit=limit,
        )
    ).parsed
