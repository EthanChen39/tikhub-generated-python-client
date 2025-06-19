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
    screen_name: Union[Unset, str] = UNSET,
    rest_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["screen_name"] = screen_name

    params["rest_id"] = rest_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/twitter/web/fetch_user_profile",
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
    screen_name: Union[Unset, str] = UNSET,
    rest_id: Union[Unset, int] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户资料/Get user profile

     # [中文]
    ### 用途:
    - 获取用户资料
    ### 参数:
    - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。
    - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。
    ### 返回:
    - 用户资料

    # [English]
    ### Purpose:
    - Get user profile
    ### Parameters:
    - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link,
    for example: elonmusk in https://twitter.com/elonmusk
    - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored,
    only one of them can be selected.
    ### Return:
    - User profile

    # [示例/Example]
    screen_name = \"elonmusk\"

    Args:
        screen_name (Union[Unset, str]): 用户名/Screen Name
        rest_id (Union[Unset, int]): 用户ID（如果使用用户ID则会忽略用户名）/User ID (If the user ID is used, the
            user name will be ignored)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        screen_name=screen_name,
        rest_id=rest_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    screen_name: Union[Unset, str] = UNSET,
    rest_id: Union[Unset, int] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户资料/Get user profile

     # [中文]
    ### 用途:
    - 获取用户资料
    ### 参数:
    - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。
    - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。
    ### 返回:
    - 用户资料

    # [English]
    ### Purpose:
    - Get user profile
    ### Parameters:
    - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link,
    for example: elonmusk in https://twitter.com/elonmusk
    - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored,
    only one of them can be selected.
    ### Return:
    - User profile

    # [示例/Example]
    screen_name = \"elonmusk\"

    Args:
        screen_name (Union[Unset, str]): 用户名/Screen Name
        rest_id (Union[Unset, int]): 用户ID（如果使用用户ID则会忽略用户名）/User ID (If the user ID is used, the
            user name will be ignored)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        screen_name=screen_name,
        rest_id=rest_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    screen_name: Union[Unset, str] = UNSET,
    rest_id: Union[Unset, int] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户资料/Get user profile

     # [中文]
    ### 用途:
    - 获取用户资料
    ### 参数:
    - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。
    - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。
    ### 返回:
    - 用户资料

    # [English]
    ### Purpose:
    - Get user profile
    ### Parameters:
    - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link,
    for example: elonmusk in https://twitter.com/elonmusk
    - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored,
    only one of them can be selected.
    ### Return:
    - User profile

    # [示例/Example]
    screen_name = \"elonmusk\"

    Args:
        screen_name (Union[Unset, str]): 用户名/Screen Name
        rest_id (Union[Unset, int]): 用户ID（如果使用用户ID则会忽略用户名）/User ID (If the user ID is used, the
            user name will be ignored)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        screen_name=screen_name,
        rest_id=rest_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    screen_name: Union[Unset, str] = UNSET,
    rest_id: Union[Unset, int] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户资料/Get user profile

     # [中文]
    ### 用途:
    - 获取用户资料
    ### 参数:
    - screen_name: 用户名，例如：elonmusk，可以从用户主页链接中获取，例如：https://twitter.com/elonmusk 中的 elonmusk。
    - rest_id: 用户ID，例如：44196397，如果使用用户ID则会忽略用户名，两者只能选其一。
    ### 返回:
    - 用户资料

    # [English]
    ### Purpose:
    - Get user profile
    ### Parameters:
    - screen_name: Screen Name, for example: elonmusk, can be obtained from the user's homepage link,
    for example: elonmusk in https://twitter.com/elonmusk
    - rest_id: User ID, for example: 44196397, if the user ID is used, the username will be ignored,
    only one of them can be selected.
    ### Return:
    - User profile

    # [示例/Example]
    screen_name = \"elonmusk\"

    Args:
        screen_name (Union[Unset, str]): 用户名/Screen Name
        rest_id (Union[Unset, int]): 用户ID（如果使用用户ID则会忽略用户名）/User ID (If the user ID is used, the
            user name will be ignored)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            screen_name=screen_name,
            rest_id=rest_id,
        )
    ).parsed
