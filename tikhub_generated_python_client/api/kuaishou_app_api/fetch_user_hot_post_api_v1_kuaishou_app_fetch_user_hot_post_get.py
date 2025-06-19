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
    pcursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params["pcursor"] = pcursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/kuaishou/app/fetch_user_hot_post",
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
    pcursor: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户热门作品数据/Get user hot post data

     # [中文]
    ### 用途:
    - 获取用户热门作品数据
    ### 参数:
    - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。
    - user_id 可以从获取单个用户数据接口中获取。
    - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get user hot post data
    ### Parameters:
    - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure
    digital ID.
    - user_id can be obtained from the get single user data interface.
    - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned
    response for subsequent requests.
    ### Returns:
    - Post data

    # [示例/Example]
    user_id = \"228905802\"
    pcursor = None

    Args:
        user_id (str):
        pcursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        pcursor=pcursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: str,
    pcursor: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户热门作品数据/Get user hot post data

     # [中文]
    ### 用途:
    - 获取用户热门作品数据
    ### 参数:
    - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。
    - user_id 可以从获取单个用户数据接口中获取。
    - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get user hot post data
    ### Parameters:
    - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure
    digital ID.
    - user_id can be obtained from the get single user data interface.
    - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned
    response for subsequent requests.
    ### Returns:
    - Post data

    # [示例/Example]
    user_id = \"228905802\"
    pcursor = None

    Args:
        user_id (str):
        pcursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        pcursor=pcursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: str,
    pcursor: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户热门作品数据/Get user hot post data

     # [中文]
    ### 用途:
    - 获取用户热门作品数据
    ### 参数:
    - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。
    - user_id 可以从获取单个用户数据接口中获取。
    - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get user hot post data
    ### Parameters:
    - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure
    digital ID.
    - user_id can be obtained from the get single user data interface.
    - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned
    response for subsequent requests.
    ### Returns:
    - Post data

    # [示例/Example]
    user_id = \"228905802\"
    pcursor = None

    Args:
        user_id (str):
        pcursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        pcursor=pcursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: str,
    pcursor: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户热门作品数据/Get user hot post data

     # [中文]
    ### 用途:
    - 获取用户热门作品数据
    ### 参数:
    - user_id: 用户ID，此接口只支持用户ID，不支持用户eid，也就是输入必须要是纯数字ID。
    - user_id 可以从获取单个用户数据接口中获取。
    - pcursor: 作品游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get user hot post data
    ### Parameters:
    - user_id: User ID, this API only supports user ID, not user eid, that is, the input must be a pure
    digital ID.
    - user_id can be obtained from the get single user data interface.
    - pcursor: Post cursor, empty for the first request, and use the pcursor value in the returned
    response for subsequent requests.
    ### Returns:
    - Post data

    # [示例/Example]
    user_id = \"228905802\"
    pcursor = None

    Args:
        user_id (str):
        pcursor (Union[Unset, str]):

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
            pcursor=pcursor,
        )
    ).parsed
