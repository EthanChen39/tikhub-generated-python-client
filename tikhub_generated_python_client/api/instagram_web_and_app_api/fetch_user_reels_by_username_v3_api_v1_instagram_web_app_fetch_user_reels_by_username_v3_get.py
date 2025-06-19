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
    username: str,
    count: Union[Unset, int] = 20,
    max_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["username"] = username

    params["count"] = count

    params["max_id"] = max_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/instagram/web_app/fetch_user_reels_by_username_v3",
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
    username: str,
    count: Union[Unset, int] = 20,
    max_id: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据用户名获取用户的Reels数据V3/Get user reels by username V3

     # [中文]
    ### 用途:
    - 根据Instagram用户名获取用户的Reels数据V3，支持高并发
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - username: Instagram用户名
    - count: 每页数量
    - max_id: 翻页游标，用于翻页，第一页不需要传值，后续页需要传入上一页的返回值。
    ### 返回:
    - 用户的Reels数据

    # [English]
    ### Purpose:
    - Get user reels by Instagram username V3
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - username: Instagram username
    - count: Count per page
    - max_id: Pagination token, no need to pass value for the first request, pass the return value of
    the previous page for subsequent pages.
    ### Return:
    - User reels data

    # [示例/Example]
    username = \"instagram\"
    count = 10
    max_id = None

    Args:
        username (str): Instagram用户名/Instagram username
        count (Union[Unset, int]): 每页数量/Count per page Default: 20.
        max_id (Union[Unset, str]): 翻页游标/Page token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        username=username,
        count=count,
        max_id=max_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    username: str,
    count: Union[Unset, int] = 20,
    max_id: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据用户名获取用户的Reels数据V3/Get user reels by username V3

     # [中文]
    ### 用途:
    - 根据Instagram用户名获取用户的Reels数据V3，支持高并发
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - username: Instagram用户名
    - count: 每页数量
    - max_id: 翻页游标，用于翻页，第一页不需要传值，后续页需要传入上一页的返回值。
    ### 返回:
    - 用户的Reels数据

    # [English]
    ### Purpose:
    - Get user reels by Instagram username V3
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - username: Instagram username
    - count: Count per page
    - max_id: Pagination token, no need to pass value for the first request, pass the return value of
    the previous page for subsequent pages.
    ### Return:
    - User reels data

    # [示例/Example]
    username = \"instagram\"
    count = 10
    max_id = None

    Args:
        username (str): Instagram用户名/Instagram username
        count (Union[Unset, int]): 每页数量/Count per page Default: 20.
        max_id (Union[Unset, str]): 翻页游标/Page token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        username=username,
        count=count,
        max_id=max_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    username: str,
    count: Union[Unset, int] = 20,
    max_id: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据用户名获取用户的Reels数据V3/Get user reels by username V3

     # [中文]
    ### 用途:
    - 根据Instagram用户名获取用户的Reels数据V3，支持高并发
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - username: Instagram用户名
    - count: 每页数量
    - max_id: 翻页游标，用于翻页，第一页不需要传值，后续页需要传入上一页的返回值。
    ### 返回:
    - 用户的Reels数据

    # [English]
    ### Purpose:
    - Get user reels by Instagram username V3
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - username: Instagram username
    - count: Count per page
    - max_id: Pagination token, no need to pass value for the first request, pass the return value of
    the previous page for subsequent pages.
    ### Return:
    - User reels data

    # [示例/Example]
    username = \"instagram\"
    count = 10
    max_id = None

    Args:
        username (str): Instagram用户名/Instagram username
        count (Union[Unset, int]): 每页数量/Count per page Default: 20.
        max_id (Union[Unset, str]): 翻页游标/Page token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        username=username,
        count=count,
        max_id=max_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    username: str,
    count: Union[Unset, int] = 20,
    max_id: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据用户名获取用户的Reels数据V3/Get user reels by username V3

     # [中文]
    ### 用途:
    - 根据Instagram用户名获取用户的Reels数据V3，支持高并发
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - username: Instagram用户名
    - count: 每页数量
    - max_id: 翻页游标，用于翻页，第一页不需要传值，后续页需要传入上一页的返回值。
    ### 返回:
    - 用户的Reels数据

    # [English]
    ### Purpose:
    - Get user reels by Instagram username V3
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - username: Instagram username
    - count: Count per page
    - max_id: Pagination token, no need to pass value for the first request, pass the return value of
    the previous page for subsequent pages.
    ### Return:
    - User reels data

    # [示例/Example]
    username = \"instagram\"
    count = 10
    max_id = None

    Args:
        username (str): Instagram用户名/Instagram username
        count (Union[Unset, int]): 每页数量/Count per page Default: 20.
        max_id (Union[Unset, str]): 翻页游标/Page token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            username=username,
            count=count,
            max_id=max_id,
        )
    ).parsed
