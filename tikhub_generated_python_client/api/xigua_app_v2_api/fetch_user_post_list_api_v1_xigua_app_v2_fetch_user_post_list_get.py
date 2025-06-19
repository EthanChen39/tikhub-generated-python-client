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
    max_behot_time: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params["max_behot_time"] = max_behot_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xigua/app/v2/fetch_user_post_list",
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
    max_behot_time: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取个人作品列表/Get user post list

     # [中文]
    ### 用途:
    - 获取个人作品列表
    ### 参数:
    - user_id: 用户id
    - max_behot_time: 最大行为时间，默认空，第一次请求传空，后续请求传上一次请求返回数据中的JSON中的值。
    - max_behot_time的值可以是JSON路径为：$.data.data.[-1].behot_time
    - 也就是data中的最后一个元素的cursor值
    ### 返回:
    - 作品列表

    # [English]
    ### Purpose:
    - Get user post list
    ### Parameters:
    - user_id: User id
    - max_behot_time: Maximum behavior time, default empty, pass empty for the first request, pass the
    max_behot_time returned by the previous request for subsequent requests
    - The value of max_behot_time can be the JSON path: $.data.data.[-1].behot_time
    - That is, the cursor value of the last element in data
    ### Return:
    - Post list

    # [示例/Example]
    user_id = \"1922379661976311\"
    max_behot_time = \"\"

    Args:
        user_id (str): 用户id/User id
        max_behot_time (Union[Unset, str]): 最大行为时间/Maximum behavior time

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_behot_time=max_behot_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: str,
    max_behot_time: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取个人作品列表/Get user post list

     # [中文]
    ### 用途:
    - 获取个人作品列表
    ### 参数:
    - user_id: 用户id
    - max_behot_time: 最大行为时间，默认空，第一次请求传空，后续请求传上一次请求返回数据中的JSON中的值。
    - max_behot_time的值可以是JSON路径为：$.data.data.[-1].behot_time
    - 也就是data中的最后一个元素的cursor值
    ### 返回:
    - 作品列表

    # [English]
    ### Purpose:
    - Get user post list
    ### Parameters:
    - user_id: User id
    - max_behot_time: Maximum behavior time, default empty, pass empty for the first request, pass the
    max_behot_time returned by the previous request for subsequent requests
    - The value of max_behot_time can be the JSON path: $.data.data.[-1].behot_time
    - That is, the cursor value of the last element in data
    ### Return:
    - Post list

    # [示例/Example]
    user_id = \"1922379661976311\"
    max_behot_time = \"\"

    Args:
        user_id (str): 用户id/User id
        max_behot_time (Union[Unset, str]): 最大行为时间/Maximum behavior time

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        max_behot_time=max_behot_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: str,
    max_behot_time: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取个人作品列表/Get user post list

     # [中文]
    ### 用途:
    - 获取个人作品列表
    ### 参数:
    - user_id: 用户id
    - max_behot_time: 最大行为时间，默认空，第一次请求传空，后续请求传上一次请求返回数据中的JSON中的值。
    - max_behot_time的值可以是JSON路径为：$.data.data.[-1].behot_time
    - 也就是data中的最后一个元素的cursor值
    ### 返回:
    - 作品列表

    # [English]
    ### Purpose:
    - Get user post list
    ### Parameters:
    - user_id: User id
    - max_behot_time: Maximum behavior time, default empty, pass empty for the first request, pass the
    max_behot_time returned by the previous request for subsequent requests
    - The value of max_behot_time can be the JSON path: $.data.data.[-1].behot_time
    - That is, the cursor value of the last element in data
    ### Return:
    - Post list

    # [示例/Example]
    user_id = \"1922379661976311\"
    max_behot_time = \"\"

    Args:
        user_id (str): 用户id/User id
        max_behot_time (Union[Unset, str]): 最大行为时间/Maximum behavior time

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_behot_time=max_behot_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: str,
    max_behot_time: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取个人作品列表/Get user post list

     # [中文]
    ### 用途:
    - 获取个人作品列表
    ### 参数:
    - user_id: 用户id
    - max_behot_time: 最大行为时间，默认空，第一次请求传空，后续请求传上一次请求返回数据中的JSON中的值。
    - max_behot_time的值可以是JSON路径为：$.data.data.[-1].behot_time
    - 也就是data中的最后一个元素的cursor值
    ### 返回:
    - 作品列表

    # [English]
    ### Purpose:
    - Get user post list
    ### Parameters:
    - user_id: User id
    - max_behot_time: Maximum behavior time, default empty, pass empty for the first request, pass the
    max_behot_time returned by the previous request for subsequent requests
    - The value of max_behot_time can be the JSON path: $.data.data.[-1].behot_time
    - That is, the cursor value of the last element in data
    ### Return:
    - Post list

    # [示例/Example]
    user_id = \"1922379661976311\"
    max_behot_time = \"\"

    Args:
        user_id (str): 用户id/User id
        max_behot_time (Union[Unset, str]): 最大行为时间/Maximum behavior time

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
            max_behot_time=max_behot_time,
        )
    ).parsed
