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
    board_type: Union[Unset, str] = "0",
    board_sub_type: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["board_type"] = board_type

    params["board_sub_type"] = board_sub_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/fetch_hot_search_list",
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
    board_type: Union[Unset, str] = "0",
    board_sub_type: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取抖音热搜榜数据/Get Douyin hot search list data

     # [中文]
    ### 用途:
    - 获取抖音热榜数据，包括：
        - 热点榜
        - 种草榜
        - 娱乐榜
        - 社会榜
        - 挑战榜
    ### 参数:
    - board_type:
        - 0: 热点榜（默认）
        - 2: 其他榜单，如种草榜等，需要传入对应的board_sub_type参数。
    - board_sub_type:
        - 空字符串: 热点榜（默认）
        - seeding: 种草榜
        - 2: 娱乐榜
        - 4: 社会榜
        - hotspot_challenge: 挑战榜
    ### 返回:
    - 热搜榜数据

    # [English]
    ### Purpose:
    - Get Douyin hot search list data, including:
        - Hot search list
        - Seeding list
        - Entertainment list
        - Social list
        - Challenge list

    ### Parameters:
    - board_type:
        - 0: Hot search list (default)
        - 2: Other lists, such as seeding list, etc., need to pass in the corresponding board_sub_type
    parameter.
    - board_sub_type:
        - Empty string: Hot search list (default)
        - seeding: Seeding list
        - 2: Entertainment list
        - 4: Social list
        - hotspot_challenge: Challenge list
    ### Return:
    - Hot search list data

    # [示例/Example]
    - 获取热点榜数据
        - board_type = 0
        - board_sub_type = \"\"
    - 获取种草榜数据
        - board_type = 2
        - board_sub_type = \"seeding\"

    Args:
        board_type (Union[Unset, str]): 榜单类型/Board type Default: '0'.
        board_sub_type (Union[Unset, str]): 榜单子类型/Board sub type Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        board_type=board_type,
        board_sub_type=board_sub_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    board_type: Union[Unset, str] = "0",
    board_sub_type: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取抖音热搜榜数据/Get Douyin hot search list data

     # [中文]
    ### 用途:
    - 获取抖音热榜数据，包括：
        - 热点榜
        - 种草榜
        - 娱乐榜
        - 社会榜
        - 挑战榜
    ### 参数:
    - board_type:
        - 0: 热点榜（默认）
        - 2: 其他榜单，如种草榜等，需要传入对应的board_sub_type参数。
    - board_sub_type:
        - 空字符串: 热点榜（默认）
        - seeding: 种草榜
        - 2: 娱乐榜
        - 4: 社会榜
        - hotspot_challenge: 挑战榜
    ### 返回:
    - 热搜榜数据

    # [English]
    ### Purpose:
    - Get Douyin hot search list data, including:
        - Hot search list
        - Seeding list
        - Entertainment list
        - Social list
        - Challenge list

    ### Parameters:
    - board_type:
        - 0: Hot search list (default)
        - 2: Other lists, such as seeding list, etc., need to pass in the corresponding board_sub_type
    parameter.
    - board_sub_type:
        - Empty string: Hot search list (default)
        - seeding: Seeding list
        - 2: Entertainment list
        - 4: Social list
        - hotspot_challenge: Challenge list
    ### Return:
    - Hot search list data

    # [示例/Example]
    - 获取热点榜数据
        - board_type = 0
        - board_sub_type = \"\"
    - 获取种草榜数据
        - board_type = 2
        - board_sub_type = \"seeding\"

    Args:
        board_type (Union[Unset, str]): 榜单类型/Board type Default: '0'.
        board_sub_type (Union[Unset, str]): 榜单子类型/Board sub type Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        board_type=board_type,
        board_sub_type=board_sub_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    board_type: Union[Unset, str] = "0",
    board_sub_type: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取抖音热搜榜数据/Get Douyin hot search list data

     # [中文]
    ### 用途:
    - 获取抖音热榜数据，包括：
        - 热点榜
        - 种草榜
        - 娱乐榜
        - 社会榜
        - 挑战榜
    ### 参数:
    - board_type:
        - 0: 热点榜（默认）
        - 2: 其他榜单，如种草榜等，需要传入对应的board_sub_type参数。
    - board_sub_type:
        - 空字符串: 热点榜（默认）
        - seeding: 种草榜
        - 2: 娱乐榜
        - 4: 社会榜
        - hotspot_challenge: 挑战榜
    ### 返回:
    - 热搜榜数据

    # [English]
    ### Purpose:
    - Get Douyin hot search list data, including:
        - Hot search list
        - Seeding list
        - Entertainment list
        - Social list
        - Challenge list

    ### Parameters:
    - board_type:
        - 0: Hot search list (default)
        - 2: Other lists, such as seeding list, etc., need to pass in the corresponding board_sub_type
    parameter.
    - board_sub_type:
        - Empty string: Hot search list (default)
        - seeding: Seeding list
        - 2: Entertainment list
        - 4: Social list
        - hotspot_challenge: Challenge list
    ### Return:
    - Hot search list data

    # [示例/Example]
    - 获取热点榜数据
        - board_type = 0
        - board_sub_type = \"\"
    - 获取种草榜数据
        - board_type = 2
        - board_sub_type = \"seeding\"

    Args:
        board_type (Union[Unset, str]): 榜单类型/Board type Default: '0'.
        board_sub_type (Union[Unset, str]): 榜单子类型/Board sub type Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        board_type=board_type,
        board_sub_type=board_sub_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    board_type: Union[Unset, str] = "0",
    board_sub_type: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取抖音热搜榜数据/Get Douyin hot search list data

     # [中文]
    ### 用途:
    - 获取抖音热榜数据，包括：
        - 热点榜
        - 种草榜
        - 娱乐榜
        - 社会榜
        - 挑战榜
    ### 参数:
    - board_type:
        - 0: 热点榜（默认）
        - 2: 其他榜单，如种草榜等，需要传入对应的board_sub_type参数。
    - board_sub_type:
        - 空字符串: 热点榜（默认）
        - seeding: 种草榜
        - 2: 娱乐榜
        - 4: 社会榜
        - hotspot_challenge: 挑战榜
    ### 返回:
    - 热搜榜数据

    # [English]
    ### Purpose:
    - Get Douyin hot search list data, including:
        - Hot search list
        - Seeding list
        - Entertainment list
        - Social list
        - Challenge list

    ### Parameters:
    - board_type:
        - 0: Hot search list (default)
        - 2: Other lists, such as seeding list, etc., need to pass in the corresponding board_sub_type
    parameter.
    - board_sub_type:
        - Empty string: Hot search list (default)
        - seeding: Seeding list
        - 2: Entertainment list
        - 4: Social list
        - hotspot_challenge: Challenge list
    ### Return:
    - Hot search list data

    # [示例/Example]
    - 获取热点榜数据
        - board_type = 0
        - board_sub_type = \"\"
    - 获取种草榜数据
        - board_type = 2
        - board_sub_type = \"seeding\"

    Args:
        board_type (Union[Unset, str]): 榜单类型/Board type Default: '0'.
        board_sub_type (Union[Unset, str]): 榜单子类型/Board sub type Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            board_type=board_type,
            board_sub_type=board_sub_type,
        )
    ).parsed
