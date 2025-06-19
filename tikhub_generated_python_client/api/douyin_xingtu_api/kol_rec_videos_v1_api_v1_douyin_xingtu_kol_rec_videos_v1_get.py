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
    kol_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["kolId"] = kol_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/xingtu/kol_rec_videos_v1",
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
    kol_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol内容表现V1/Get kol Rec Videos V1

     # [中文]
    ### 用途:
    - 获取kol内容表现V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    ### 返回:
    - kol内容表现

    # [English]
    ### Purpose:
    - Get kol Rec Videos V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    ### Return:
    - kol Rec Videos

    # [示例/Example]
    kolId = \"7048929565493690398\"

    Args:
        kol_id (str): 用户的kolId/User kolId

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        kol_id=kol_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    kol_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol内容表现V1/Get kol Rec Videos V1

     # [中文]
    ### 用途:
    - 获取kol内容表现V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    ### 返回:
    - kol内容表现

    # [English]
    ### Purpose:
    - Get kol Rec Videos V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    ### Return:
    - kol Rec Videos

    # [示例/Example]
    kolId = \"7048929565493690398\"

    Args:
        kol_id (str): 用户的kolId/User kolId

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        kol_id=kol_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    kol_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol内容表现V1/Get kol Rec Videos V1

     # [中文]
    ### 用途:
    - 获取kol内容表现V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    ### 返回:
    - kol内容表现

    # [English]
    ### Purpose:
    - Get kol Rec Videos V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    ### Return:
    - kol Rec Videos

    # [示例/Example]
    kolId = \"7048929565493690398\"

    Args:
        kol_id (str): 用户的kolId/User kolId

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        kol_id=kol_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    kol_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol内容表现V1/Get kol Rec Videos V1

     # [中文]
    ### 用途:
    - 获取kol内容表现V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    ### 返回:
    - kol内容表现

    # [English]
    ### Purpose:
    - Get kol Rec Videos V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    ### Return:
    - kol Rec Videos

    # [示例/Example]
    kolId = \"7048929565493690398\"

    Args:
        kol_id (str): 用户的kolId/User kolId

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            kol_id=kol_id,
        )
    ).parsed
