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
    uid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["uid"] = uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid",
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
    uid: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID

     # [中文]
    ### 用途:
    - 通过抖音用户ID获取游客星图kolid
    - 价格：0.001$ / 次
    ### 参数:
    - uid: 用户ID, 可以从接口以下接口获取：
        - `/api/v1/douyin/web/fetch_user_profile_by_uid`
        - `/api/v1/douyin/web/fetch_user_profile_by_short_id`
        - `/api/v1/douyin/web/handler_user_profile`
        - `/api/v1/douyin/web/handler_user_profile_v2`
        - `/api/v1/douyin/web/handler_user_profile_v3`
        - `/api/v1/douyin/app/v3/handler_user_profile`
    ### 返回:
    - 游客星图kolid

    # [English]
    ### Purpose:
    - Get XingTu kolid by Douyin User ID
    - Price: 0.001$ / time
    ### Parameters:
    - uid: User ID, can be obtained from the following interfaces:
        - `/api/v1/douyin/web/fetch_user_profile_by_uid`
        - `/api/v1/douyin/web/fetch_user_profile_by_short_id`
        - `/api/v1/douyin/web/handler_user_profile`
        - `/api/v1/douyin/web/handler_user_profile_v2`
        - `/api/v1/douyin/web/handler_user_profile_v3`
        - `/api/v1/douyin/app/v3/handler_user_profile`
    ### Return:
    - XingTu kolid

    # [示例/Example]
    uid = \"70452002324\"

    Args:
        uid (str): 抖音用户ID/Douyin User ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        uid=uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    uid: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID

     # [中文]
    ### 用途:
    - 通过抖音用户ID获取游客星图kolid
    - 价格：0.001$ / 次
    ### 参数:
    - uid: 用户ID, 可以从接口以下接口获取：
        - `/api/v1/douyin/web/fetch_user_profile_by_uid`
        - `/api/v1/douyin/web/fetch_user_profile_by_short_id`
        - `/api/v1/douyin/web/handler_user_profile`
        - `/api/v1/douyin/web/handler_user_profile_v2`
        - `/api/v1/douyin/web/handler_user_profile_v3`
        - `/api/v1/douyin/app/v3/handler_user_profile`
    ### 返回:
    - 游客星图kolid

    # [English]
    ### Purpose:
    - Get XingTu kolid by Douyin User ID
    - Price: 0.001$ / time
    ### Parameters:
    - uid: User ID, can be obtained from the following interfaces:
        - `/api/v1/douyin/web/fetch_user_profile_by_uid`
        - `/api/v1/douyin/web/fetch_user_profile_by_short_id`
        - `/api/v1/douyin/web/handler_user_profile`
        - `/api/v1/douyin/web/handler_user_profile_v2`
        - `/api/v1/douyin/web/handler_user_profile_v3`
        - `/api/v1/douyin/app/v3/handler_user_profile`
    ### Return:
    - XingTu kolid

    # [示例/Example]
    uid = \"70452002324\"

    Args:
        uid (str): 抖音用户ID/Douyin User ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        uid=uid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    uid: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID

     # [中文]
    ### 用途:
    - 通过抖音用户ID获取游客星图kolid
    - 价格：0.001$ / 次
    ### 参数:
    - uid: 用户ID, 可以从接口以下接口获取：
        - `/api/v1/douyin/web/fetch_user_profile_by_uid`
        - `/api/v1/douyin/web/fetch_user_profile_by_short_id`
        - `/api/v1/douyin/web/handler_user_profile`
        - `/api/v1/douyin/web/handler_user_profile_v2`
        - `/api/v1/douyin/web/handler_user_profile_v3`
        - `/api/v1/douyin/app/v3/handler_user_profile`
    ### 返回:
    - 游客星图kolid

    # [English]
    ### Purpose:
    - Get XingTu kolid by Douyin User ID
    - Price: 0.001$ / time
    ### Parameters:
    - uid: User ID, can be obtained from the following interfaces:
        - `/api/v1/douyin/web/fetch_user_profile_by_uid`
        - `/api/v1/douyin/web/fetch_user_profile_by_short_id`
        - `/api/v1/douyin/web/handler_user_profile`
        - `/api/v1/douyin/web/handler_user_profile_v2`
        - `/api/v1/douyin/web/handler_user_profile_v3`
        - `/api/v1/douyin/app/v3/handler_user_profile`
    ### Return:
    - XingTu kolid

    # [示例/Example]
    uid = \"70452002324\"

    Args:
        uid (str): 抖音用户ID/Douyin User ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        uid=uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    uid: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID

     # [中文]
    ### 用途:
    - 通过抖音用户ID获取游客星图kolid
    - 价格：0.001$ / 次
    ### 参数:
    - uid: 用户ID, 可以从接口以下接口获取：
        - `/api/v1/douyin/web/fetch_user_profile_by_uid`
        - `/api/v1/douyin/web/fetch_user_profile_by_short_id`
        - `/api/v1/douyin/web/handler_user_profile`
        - `/api/v1/douyin/web/handler_user_profile_v2`
        - `/api/v1/douyin/web/handler_user_profile_v3`
        - `/api/v1/douyin/app/v3/handler_user_profile`
    ### 返回:
    - 游客星图kolid

    # [English]
    ### Purpose:
    - Get XingTu kolid by Douyin User ID
    - Price: 0.001$ / time
    ### Parameters:
    - uid: User ID, can be obtained from the following interfaces:
        - `/api/v1/douyin/web/fetch_user_profile_by_uid`
        - `/api/v1/douyin/web/fetch_user_profile_by_short_id`
        - `/api/v1/douyin/web/handler_user_profile`
        - `/api/v1/douyin/web/handler_user_profile_v2`
        - `/api/v1/douyin/web/handler_user_profile_v3`
        - `/api/v1/douyin/app/v3/handler_user_profile`
    ### Return:
    - XingTu kolid

    # [示例/Example]
    uid = \"70452002324\"

    Args:
        uid (str): 抖音用户ID/Douyin User ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            uid=uid,
        )
    ).parsed
