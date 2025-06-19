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
    user_profile_url: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_profile_url"] = user_profile_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/toutiao/app/get_user_id",
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
    user_profile_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""从头条用户主页获取用户user_id/Get user_id from user profile

     # [中文]
    ### 用途:
    - 从头条用户主页获取用户user_id
    ### 参数:
    - user_profile_url: 用户主页链接
        - 例如: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-
    8ineO5UaB4L-djqkYDgB6TkAdMvrmW/
    ### 返回:
    - 用户ID

    # [English]
    ### Purpose:
    - Get user_id from user profile
    ### Parameters:
    - user_profile_url: User profile URL
        - For example: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSG
    t-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/
    ### Return:
    - User ID

    # [示例/Example]
    user_profile_url = \"https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbG
    SGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/\"

    Args:
        user_profile_url (str): 用户主页链接/User profile URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_profile_url=user_profile_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_profile_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""从头条用户主页获取用户user_id/Get user_id from user profile

     # [中文]
    ### 用途:
    - 从头条用户主页获取用户user_id
    ### 参数:
    - user_profile_url: 用户主页链接
        - 例如: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-
    8ineO5UaB4L-djqkYDgB6TkAdMvrmW/
    ### 返回:
    - 用户ID

    # [English]
    ### Purpose:
    - Get user_id from user profile
    ### Parameters:
    - user_profile_url: User profile URL
        - For example: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSG
    t-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/
    ### Return:
    - User ID

    # [示例/Example]
    user_profile_url = \"https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbG
    SGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/\"

    Args:
        user_profile_url (str): 用户主页链接/User profile URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        user_profile_url=user_profile_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_profile_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""从头条用户主页获取用户user_id/Get user_id from user profile

     # [中文]
    ### 用途:
    - 从头条用户主页获取用户user_id
    ### 参数:
    - user_profile_url: 用户主页链接
        - 例如: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-
    8ineO5UaB4L-djqkYDgB6TkAdMvrmW/
    ### 返回:
    - 用户ID

    # [English]
    ### Purpose:
    - Get user_id from user profile
    ### Parameters:
    - user_profile_url: User profile URL
        - For example: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSG
    t-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/
    ### Return:
    - User ID

    # [示例/Example]
    user_profile_url = \"https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbG
    SGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/\"

    Args:
        user_profile_url (str): 用户主页链接/User profile URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_profile_url=user_profile_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_profile_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""从头条用户主页获取用户user_id/Get user_id from user profile

     # [中文]
    ### 用途:
    - 从头条用户主页获取用户user_id
    ### 参数:
    - user_profile_url: 用户主页链接
        - 例如: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSGt-
    8ineO5UaB4L-djqkYDgB6TkAdMvrmW/
    ### 返回:
    - 用户ID

    # [English]
    ### Purpose:
    - Get user_id from user profile
    ### Parameters:
    - user_profile_url: User profile URL
        - For example: https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbGSG
    t-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/
    ### Return:
    - User ID

    # [示例/Example]
    user_profile_url = \"https://www.toutiao.com/c/user/token/MS4wLjABAAAAwK6echNksY69R8l2vcZudupfhTItbG
    SGt-8ineO5UaB4L-djqkYDgB6TkAdMvrmW/\"

    Args:
        user_profile_url (str): 用户主页链接/User profile URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_profile_url=user_profile_url,
        )
    ).parsed
