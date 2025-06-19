from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    uid: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["uid"] = uid

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/net_ease_cloud_music/app/fetch_user_playlist",
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
    uid: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取用户歌单/Get user playlist

     # [中文]
    ### 用途:
    - 获取用户歌单。
    ### 参数:
    - uid: 用户ID。
    - offset: 偏移量，第一次搜索传递0，第二次传递20，第三次传递40，以此类推。
    - limit: 每页数量，保持默认即可。
    ### 返回:
    - 用户歌单

    # [English]
    ### Purpose:
    - Get user playlist.
    ### Parameters:
    - uid: User ID.
    - offset: Offset, pass 0 for the first search, 20 for the second search, 40 for the third search,
    and so on.
    - limit: Number per page, keep the default.
    ### Returns:
    - User playlist

    # [示例/Example]
    uid = \"254132915\"
    offset = \"0\"
    limit = \"20\"

    Args:
        uid (str): 用户ID/User ID
        offset (Union[Unset, str]): 偏移量，保持默认即可/Offset, keep the default Default: '0'.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    uid: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取用户歌单/Get user playlist

     # [中文]
    ### 用途:
    - 获取用户歌单。
    ### 参数:
    - uid: 用户ID。
    - offset: 偏移量，第一次搜索传递0，第二次传递20，第三次传递40，以此类推。
    - limit: 每页数量，保持默认即可。
    ### 返回:
    - 用户歌单

    # [English]
    ### Purpose:
    - Get user playlist.
    ### Parameters:
    - uid: User ID.
    - offset: Offset, pass 0 for the first search, 20 for the second search, 40 for the third search,
    and so on.
    - limit: Number per page, keep the default.
    ### Returns:
    - User playlist

    # [示例/Example]
    uid = \"254132915\"
    offset = \"0\"
    limit = \"20\"

    Args:
        uid (str): 用户ID/User ID
        offset (Union[Unset, str]): 偏移量，保持默认即可/Offset, keep the default Default: '0'.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        uid=uid,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    uid: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取用户歌单/Get user playlist

     # [中文]
    ### 用途:
    - 获取用户歌单。
    ### 参数:
    - uid: 用户ID。
    - offset: 偏移量，第一次搜索传递0，第二次传递20，第三次传递40，以此类推。
    - limit: 每页数量，保持默认即可。
    ### 返回:
    - 用户歌单

    # [English]
    ### Purpose:
    - Get user playlist.
    ### Parameters:
    - uid: User ID.
    - offset: Offset, pass 0 for the first search, 20 for the second search, 40 for the third search,
    and so on.
    - limit: Number per page, keep the default.
    ### Returns:
    - User playlist

    # [示例/Example]
    uid = \"254132915\"
    offset = \"0\"
    limit = \"20\"

    Args:
        uid (str): 用户ID/User ID
        offset (Union[Unset, str]): 偏移量，保持默认即可/Offset, keep the default Default: '0'.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    uid: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "20",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取用户歌单/Get user playlist

     # [中文]
    ### 用途:
    - 获取用户歌单。
    ### 参数:
    - uid: 用户ID。
    - offset: 偏移量，第一次搜索传递0，第二次传递20，第三次传递40，以此类推。
    - limit: 每页数量，保持默认即可。
    ### 返回:
    - 用户歌单

    # [English]
    ### Purpose:
    - Get user playlist.
    ### Parameters:
    - uid: User ID.
    - offset: Offset, pass 0 for the first search, 20 for the second search, 40 for the third search,
    and so on.
    - limit: Number per page, keep the default.
    ### Returns:
    - User playlist

    # [示例/Example]
    uid = \"254132915\"
    offset = \"0\"
    limit = \"20\"

    Args:
        uid (str): 用户ID/User ID
        offset (Union[Unset, str]): 偏移量，保持默认即可/Offset, keep the default Default: '0'.
        limit (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            uid=uid,
            offset=offset,
            limit=limit,
        )
    ).parsed
