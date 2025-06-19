from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_info_response_model import UserInfoResponseModel
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tikhub/user/get_user_info",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UserInfoResponseModel]:
    if response.status_code == 200:
        response_200 = UserInfoResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UserInfoResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[UserInfoResponseModel]:
    r"""获取TikHub用户信息/Get TikHub user info

     # [中文]
    ### 用途:
    - 请求头中携带API Key请求此端点可以查询当前账户信息。
    ### 参数:
    - 请求头：{'Authorization': 'Bearer API_KEY'}
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Request this endpoint with API Key in the header to query the current account information.
    ### Parameters:
    - Headers: {'Authorization': 'Bearer API_KEY'}
    ### Return:
    - User information

    # [示例/Example]
    ```python
    response = {
          \"code\": 200,
          \"router\": \"/api/v1/tikhub/user/get_user_info\",
          \"api_key_data\": {
            \"api_key_name\": \"Develop Test\",
            \"api_key_scopes\": [
              \"/api/v1/tikhub/user/\"
            ],
            \"created_at\": \"2024-05-22T06:07:12.495520\",
            \"expires_at\": null,
            \"api_key_status\": 1
          },
          \"user_data\": {
            \"email\": \"example@example.com\",
            \"balance\": 100,
            \"free_credit\": 100,
            \"email_verified\": true,
            \"account_disabled\": false,
            \"is_active\": true
          }
        }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserInfoResponseModel]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[UserInfoResponseModel]:
    r"""获取TikHub用户信息/Get TikHub user info

     # [中文]
    ### 用途:
    - 请求头中携带API Key请求此端点可以查询当前账户信息。
    ### 参数:
    - 请求头：{'Authorization': 'Bearer API_KEY'}
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Request this endpoint with API Key in the header to query the current account information.
    ### Parameters:
    - Headers: {'Authorization': 'Bearer API_KEY'}
    ### Return:
    - User information

    # [示例/Example]
    ```python
    response = {
          \"code\": 200,
          \"router\": \"/api/v1/tikhub/user/get_user_info\",
          \"api_key_data\": {
            \"api_key_name\": \"Develop Test\",
            \"api_key_scopes\": [
              \"/api/v1/tikhub/user/\"
            ],
            \"created_at\": \"2024-05-22T06:07:12.495520\",
            \"expires_at\": null,
            \"api_key_status\": 1
          },
          \"user_data\": {
            \"email\": \"example@example.com\",
            \"balance\": 100,
            \"free_credit\": 100,
            \"email_verified\": true,
            \"account_disabled\": false,
            \"is_active\": true
          }
        }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserInfoResponseModel
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[UserInfoResponseModel]:
    r"""获取TikHub用户信息/Get TikHub user info

     # [中文]
    ### 用途:
    - 请求头中携带API Key请求此端点可以查询当前账户信息。
    ### 参数:
    - 请求头：{'Authorization': 'Bearer API_KEY'}
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Request this endpoint with API Key in the header to query the current account information.
    ### Parameters:
    - Headers: {'Authorization': 'Bearer API_KEY'}
    ### Return:
    - User information

    # [示例/Example]
    ```python
    response = {
          \"code\": 200,
          \"router\": \"/api/v1/tikhub/user/get_user_info\",
          \"api_key_data\": {
            \"api_key_name\": \"Develop Test\",
            \"api_key_scopes\": [
              \"/api/v1/tikhub/user/\"
            ],
            \"created_at\": \"2024-05-22T06:07:12.495520\",
            \"expires_at\": null,
            \"api_key_status\": 1
          },
          \"user_data\": {
            \"email\": \"example@example.com\",
            \"balance\": 100,
            \"free_credit\": 100,
            \"email_verified\": true,
            \"account_disabled\": false,
            \"is_active\": true
          }
        }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserInfoResponseModel]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[UserInfoResponseModel]:
    r"""获取TikHub用户信息/Get TikHub user info

     # [中文]
    ### 用途:
    - 请求头中携带API Key请求此端点可以查询当前账户信息。
    ### 参数:
    - 请求头：{'Authorization': 'Bearer API_KEY'}
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Request this endpoint with API Key in the header to query the current account information.
    ### Parameters:
    - Headers: {'Authorization': 'Bearer API_KEY'}
    ### Return:
    - User information

    # [示例/Example]
    ```python
    response = {
          \"code\": 200,
          \"router\": \"/api/v1/tikhub/user/get_user_info\",
          \"api_key_data\": {
            \"api_key_name\": \"Develop Test\",
            \"api_key_scopes\": [
              \"/api/v1/tikhub/user/\"
            ],
            \"created_at\": \"2024-05-22T06:07:12.495520\",
            \"expires_at\": null,
            \"api_key_status\": 1
          },
          \"user_data\": {
            \"email\": \"example@example.com\",
            \"balance\": 100,
            \"free_credit\": 100,
            \"email_verified\": true,
            \"account_disabled\": false,
            \"is_active\": true
          }
        }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserInfoResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
