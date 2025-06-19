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
    start_date: str,
    end_date: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["kolId"] = kol_id

    params["startDate"] = start_date

    params["endDate"] = end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/xingtu/kol_daily_fans_v1",
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
    start_date: str,
    end_date: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol粉丝趋势V1/Get kol Daily Fans V1

     # [中文]
    ### 用途:
    - 获取kol粉丝趋势V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - startDate: 开始日期，格式为：yyyy-MM-dd
    - endDate: 结束日期，格式为：yyyy-MM-dd
    ### 返回:
    - kol粉丝趋势

    # [English]
    ### Purpose:
    - Get kol Daily Fans V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - startDate: Start date, format: yyyy-MM-dd
    - endDate: End date, format: yyyy-MM-dd
    ### Return:
    - kol Daily Fans

    # [示例/Example]
    kolId = \"7048929565493690398\"
    startDate = \"2024-12-01\"
    endDate = \"2025-01-01\"

    Args:
        kol_id (str): 用户的kolId/User kolId
        start_date (str): 开始日期/Start Date
        end_date (str): 结束日期/End Date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        kol_id=kol_id,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    kol_id: str,
    start_date: str,
    end_date: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol粉丝趋势V1/Get kol Daily Fans V1

     # [中文]
    ### 用途:
    - 获取kol粉丝趋势V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - startDate: 开始日期，格式为：yyyy-MM-dd
    - endDate: 结束日期，格式为：yyyy-MM-dd
    ### 返回:
    - kol粉丝趋势

    # [English]
    ### Purpose:
    - Get kol Daily Fans V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - startDate: Start date, format: yyyy-MM-dd
    - endDate: End date, format: yyyy-MM-dd
    ### Return:
    - kol Daily Fans

    # [示例/Example]
    kolId = \"7048929565493690398\"
    startDate = \"2024-12-01\"
    endDate = \"2025-01-01\"

    Args:
        kol_id (str): 用户的kolId/User kolId
        start_date (str): 开始日期/Start Date
        end_date (str): 结束日期/End Date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        kol_id=kol_id,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    kol_id: str,
    start_date: str,
    end_date: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol粉丝趋势V1/Get kol Daily Fans V1

     # [中文]
    ### 用途:
    - 获取kol粉丝趋势V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - startDate: 开始日期，格式为：yyyy-MM-dd
    - endDate: 结束日期，格式为：yyyy-MM-dd
    ### 返回:
    - kol粉丝趋势

    # [English]
    ### Purpose:
    - Get kol Daily Fans V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - startDate: Start date, format: yyyy-MM-dd
    - endDate: End date, format: yyyy-MM-dd
    ### Return:
    - kol Daily Fans

    # [示例/Example]
    kolId = \"7048929565493690398\"
    startDate = \"2024-12-01\"
    endDate = \"2025-01-01\"

    Args:
        kol_id (str): 用户的kolId/User kolId
        start_date (str): 开始日期/Start Date
        end_date (str): 结束日期/End Date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        kol_id=kol_id,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    kol_id: str,
    start_date: str,
    end_date: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol粉丝趋势V1/Get kol Daily Fans V1

     # [中文]
    ### 用途:
    - 获取kol粉丝趋势V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - startDate: 开始日期，格式为：yyyy-MM-dd
    - endDate: 结束日期，格式为：yyyy-MM-dd
    ### 返回:
    - kol粉丝趋势

    # [English]
    ### Purpose:
    - Get kol Daily Fans V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - startDate: Start date, format: yyyy-MM-dd
    - endDate: End date, format: yyyy-MM-dd
    ### Return:
    - kol Daily Fans

    # [示例/Example]
    kolId = \"7048929565493690398\"
    startDate = \"2024-12-01\"
    endDate = \"2025-01-01\"

    Args:
        kol_id (str): 用户的kolId/User kolId
        start_date (str): 开始日期/Start Date
        end_date (str): 结束日期/End Date

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
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
