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
    user_id: str,
    cursor: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/lemon8/app/fetch_user_following_list",
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
    user_id: str,
    cursor: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定用户的关注列表/Get following list of specified user

     # [中文]
    ### 用途:
    - 获取指定用户的关注列表
    ### 参数:
    - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取
    - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。
    ### 返回:
    - 关注列表

    # [English]
    ### Purpose:
    - Get following list of specified user
    ### Parameters:
    - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id`
    - cursor: Pagination parameter, can be obtained from the return result of the last request. It is
    empty for the first request, and the cursor returned by the last request is used for subsequent
    requests.
    ### Return:
    - Following list

    # [示例/Example]
    user_id = \"7428056850216862763\"

    Args:
        user_id (str): 用户ID/User ID
        cursor (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: str,
    cursor: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定用户的关注列表/Get following list of specified user

     # [中文]
    ### 用途:
    - 获取指定用户的关注列表
    ### 参数:
    - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取
    - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。
    ### 返回:
    - 关注列表

    # [English]
    ### Purpose:
    - Get following list of specified user
    ### Parameters:
    - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id`
    - cursor: Pagination parameter, can be obtained from the return result of the last request. It is
    empty for the first request, and the cursor returned by the last request is used for subsequent
    requests.
    ### Return:
    - Following list

    # [示例/Example]
    user_id = \"7428056850216862763\"

    Args:
        user_id (str): 用户ID/User ID
        cursor (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: str,
    cursor: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定用户的关注列表/Get following list of specified user

     # [中文]
    ### 用途:
    - 获取指定用户的关注列表
    ### 参数:
    - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取
    - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。
    ### 返回:
    - 关注列表

    # [English]
    ### Purpose:
    - Get following list of specified user
    ### Parameters:
    - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id`
    - cursor: Pagination parameter, can be obtained from the return result of the last request. It is
    empty for the first request, and the cursor returned by the last request is used for subsequent
    requests.
    ### Return:
    - Following list

    # [示例/Example]
    user_id = \"7428056850216862763\"

    Args:
        user_id (str): 用户ID/User ID
        cursor (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: str,
    cursor: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定用户的关注列表/Get following list of specified user

     # [中文]
    ### 用途:
    - 获取指定用户的关注列表
    ### 参数:
    - user_id: 用户ID，可以从接口`/lemon8/app/get_user_id`获取
    - cursor: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的cursor进行翻页。
    ### 返回:
    - 关注列表

    # [English]
    ### Purpose:
    - Get following list of specified user
    ### Parameters:
    - user_id: User ID, can be obtained from the interface `/lemon8/app/get_user_id`
    - cursor: Pagination parameter, can be obtained from the return result of the last request. It is
    empty for the first request, and the cursor returned by the last request is used for subsequent
    requests.
    ### Return:
    - Following list

    # [示例/Example]
    user_id = \"7428056850216862763\"

    Args:
        user_id (str): 用户ID/User ID
        cursor (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            cursor=cursor,
        )
    ).parsed
