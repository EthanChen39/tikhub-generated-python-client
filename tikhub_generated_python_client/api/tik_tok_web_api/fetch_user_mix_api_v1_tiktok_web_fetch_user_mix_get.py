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
    mix_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 30,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["mixId"] = mix_id

    params["cursor"] = cursor

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_user_mix",
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
    mix_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 30,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的合辑列表/Get user mix list

     # [中文]
    ### 用途:
    - 获取用户的合辑列表
    ### 参数:
    - mixId: 合辑id
    - cursor: 翻页游标
    - count: 每页数量
    ### 返回:
    - 用户的合辑列表

    # [English]
    ### Purpose:
    - Get user mix list
    ### Parameters:
    - mixId: Mix id
    - cursor: Page cursor
    - count: Number per page
    ### Return:
    - User mix list

    # [示例/Eample]
    mixId = \"7101538765474106158\"
    cursor = 0
    count = 30

    Args:
        mix_id (str): 合辑id/Mix id
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        mix_id=mix_id,
        cursor=cursor,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    mix_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 30,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的合辑列表/Get user mix list

     # [中文]
    ### 用途:
    - 获取用户的合辑列表
    ### 参数:
    - mixId: 合辑id
    - cursor: 翻页游标
    - count: 每页数量
    ### 返回:
    - 用户的合辑列表

    # [English]
    ### Purpose:
    - Get user mix list
    ### Parameters:
    - mixId: Mix id
    - cursor: Page cursor
    - count: Number per page
    ### Return:
    - User mix list

    # [示例/Eample]
    mixId = \"7101538765474106158\"
    cursor = 0
    count = 30

    Args:
        mix_id (str): 合辑id/Mix id
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        mix_id=mix_id,
        cursor=cursor,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    mix_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 30,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的合辑列表/Get user mix list

     # [中文]
    ### 用途:
    - 获取用户的合辑列表
    ### 参数:
    - mixId: 合辑id
    - cursor: 翻页游标
    - count: 每页数量
    ### 返回:
    - 用户的合辑列表

    # [English]
    ### Purpose:
    - Get user mix list
    ### Parameters:
    - mixId: Mix id
    - cursor: Page cursor
    - count: Number per page
    ### Return:
    - User mix list

    # [示例/Eample]
    mixId = \"7101538765474106158\"
    cursor = 0
    count = 30

    Args:
        mix_id (str): 合辑id/Mix id
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        mix_id=mix_id,
        cursor=cursor,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    mix_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 30,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的合辑列表/Get user mix list

     # [中文]
    ### 用途:
    - 获取用户的合辑列表
    ### 参数:
    - mixId: 合辑id
    - cursor: 翻页游标
    - count: 每页数量
    ### 返回:
    - 用户的合辑列表

    # [English]
    ### Purpose:
    - Get user mix list
    ### Parameters:
    - mixId: Mix id
    - cursor: Page cursor
    - count: Number per page
    ### Return:
    - User mix list

    # [示例/Eample]
    mixId = \"7101538765474106158\"
    cursor = 0
    count = 30

    Args:
        mix_id (str): 合辑id/Mix id
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            mix_id=mix_id,
            cursor=cursor,
            count=count,
        )
    ).parsed
