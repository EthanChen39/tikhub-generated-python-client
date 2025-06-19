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
    lasttime: Union[Unset, str] = "0",
    pagesize: Union[Unset, str] = "20",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["uid"] = uid

    params["lasttime"] = lasttime

    params["pagesize"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/net_ease_cloud_music/app/fetch_user_followers",
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
    lasttime: Union[Unset, str] = "0",
    pagesize: Union[Unset, str] = "20",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取用户粉丝列表/Fetch user followers

     # [中文]
    ### 用途:
    - 获取用户粉丝列表。
    ### 参数:
    - uid: 用户ID。
    - lasttime: 时间戳，用于翻页，第一页不需要传递，第二页传递第一页返回的最后一条动态的时间戳，或者查看返回的Next_Page_lasttime字段。
    - pagesize: 每页数量，保持默认即可。
    ### 返回:
    - 用户粉丝列表

    # [English]
    ### Purpose:
    - Fetch user followers.
    ### Parameters:
    - uid: User ID.
    - lasttime: Time stamp, used for paging, no need to pass on the first page, pass the time stamp of
    the last event returned on the first page on the second page, or check the Next_Page_lasttime field
    returned.
    - pagesize: Number per page, keep the default.
    ### Returns:
    - User followers list

    # [示例/Example]
    uid = \"254132915\"
    lasttime = \"0\"
    pagesize = \"20\"

    Args:
        uid (str): 用户ID/User ID
        lasttime (Union[Unset, str]): 时间戳，用于翻页，第一页不需要传递/Time stamp, used for paging, no need to
            pass on the first page Default: '0'.
        pagesize (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        lasttime=lasttime,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    uid: str,
    lasttime: Union[Unset, str] = "0",
    pagesize: Union[Unset, str] = "20",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取用户粉丝列表/Fetch user followers

     # [中文]
    ### 用途:
    - 获取用户粉丝列表。
    ### 参数:
    - uid: 用户ID。
    - lasttime: 时间戳，用于翻页，第一页不需要传递，第二页传递第一页返回的最后一条动态的时间戳，或者查看返回的Next_Page_lasttime字段。
    - pagesize: 每页数量，保持默认即可。
    ### 返回:
    - 用户粉丝列表

    # [English]
    ### Purpose:
    - Fetch user followers.
    ### Parameters:
    - uid: User ID.
    - lasttime: Time stamp, used for paging, no need to pass on the first page, pass the time stamp of
    the last event returned on the first page on the second page, or check the Next_Page_lasttime field
    returned.
    - pagesize: Number per page, keep the default.
    ### Returns:
    - User followers list

    # [示例/Example]
    uid = \"254132915\"
    lasttime = \"0\"
    pagesize = \"20\"

    Args:
        uid (str): 用户ID/User ID
        lasttime (Union[Unset, str]): 时间戳，用于翻页，第一页不需要传递/Time stamp, used for paging, no need to
            pass on the first page Default: '0'.
        pagesize (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        uid=uid,
        lasttime=lasttime,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    uid: str,
    lasttime: Union[Unset, str] = "0",
    pagesize: Union[Unset, str] = "20",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取用户粉丝列表/Fetch user followers

     # [中文]
    ### 用途:
    - 获取用户粉丝列表。
    ### 参数:
    - uid: 用户ID。
    - lasttime: 时间戳，用于翻页，第一页不需要传递，第二页传递第一页返回的最后一条动态的时间戳，或者查看返回的Next_Page_lasttime字段。
    - pagesize: 每页数量，保持默认即可。
    ### 返回:
    - 用户粉丝列表

    # [English]
    ### Purpose:
    - Fetch user followers.
    ### Parameters:
    - uid: User ID.
    - lasttime: Time stamp, used for paging, no need to pass on the first page, pass the time stamp of
    the last event returned on the first page on the second page, or check the Next_Page_lasttime field
    returned.
    - pagesize: Number per page, keep the default.
    ### Returns:
    - User followers list

    # [示例/Example]
    uid = \"254132915\"
    lasttime = \"0\"
    pagesize = \"20\"

    Args:
        uid (str): 用户ID/User ID
        lasttime (Union[Unset, str]): 时间戳，用于翻页，第一页不需要传递/Time stamp, used for paging, no need to
            pass on the first page Default: '0'.
        pagesize (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        lasttime=lasttime,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    uid: str,
    lasttime: Union[Unset, str] = "0",
    pagesize: Union[Unset, str] = "20",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取用户粉丝列表/Fetch user followers

     # [中文]
    ### 用途:
    - 获取用户粉丝列表。
    ### 参数:
    - uid: 用户ID。
    - lasttime: 时间戳，用于翻页，第一页不需要传递，第二页传递第一页返回的最后一条动态的时间戳，或者查看返回的Next_Page_lasttime字段。
    - pagesize: 每页数量，保持默认即可。
    ### 返回:
    - 用户粉丝列表

    # [English]
    ### Purpose:
    - Fetch user followers.
    ### Parameters:
    - uid: User ID.
    - lasttime: Time stamp, used for paging, no need to pass on the first page, pass the time stamp of
    the last event returned on the first page on the second page, or check the Next_Page_lasttime field
    returned.
    - pagesize: Number per page, keep the default.
    ### Returns:
    - User followers list

    # [示例/Example]
    uid = \"254132915\"
    lasttime = \"0\"
    pagesize = \"20\"

    Args:
        uid (str): 用户ID/User ID
        lasttime (Union[Unset, str]): 时间戳，用于翻页，第一页不需要传递/Time stamp, used for paging, no need to
            pass on the first page Default: '0'.
        pagesize (Union[Unset, str]): 每页数量，保持默认即可/Number per page, keep the default Default: '20'.

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
            lasttime=lasttime,
            pagesize=pagesize,
        )
    ).parsed
