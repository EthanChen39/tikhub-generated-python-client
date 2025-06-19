from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post import (
    BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/billboard/fetch_hot_calendar_list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取活动日历/Fetch activity calendar

     # [中文]
    ### 用途:
    - 获取活动日历
    ### 参数:
    - city_code: 城市编码，从城市列表获取，空为全部
    - category_code: 热点榜分类编码，从热点榜分类获取，空为全部
    - end_date: 快照结束时间 格式10位时间戳
    - start_date: 快照开始时间 格式10位时间戳
    ### 返回:
    - 活动日历

    # [English]
    ### Purpose:
    - Get the activity calendar
    ### Parameters:
    - city_code: City code, get from city list, empty for all
    - category_code: Hot list category code, get from hot list category, empty for all
    - end_date: Snapshot end time format 10 digit timestamp
    - start_date: Snapshot start time format 10 digit timestamp
    ### Return:
    - Activity calendar

    Args:
        body (BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取活动日历/Fetch activity calendar

     # [中文]
    ### 用途:
    - 获取活动日历
    ### 参数:
    - city_code: 城市编码，从城市列表获取，空为全部
    - category_code: 热点榜分类编码，从热点榜分类获取，空为全部
    - end_date: 快照结束时间 格式10位时间戳
    - start_date: 快照开始时间 格式10位时间戳
    ### 返回:
    - 活动日历

    # [English]
    ### Purpose:
    - Get the activity calendar
    ### Parameters:
    - city_code: City code, get from city list, empty for all
    - category_code: Hot list category code, get from hot list category, empty for all
    - end_date: Snapshot end time format 10 digit timestamp
    - start_date: Snapshot start time format 10 digit timestamp
    ### Return:
    - Activity calendar

    Args:
        body (BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取活动日历/Fetch activity calendar

     # [中文]
    ### 用途:
    - 获取活动日历
    ### 参数:
    - city_code: 城市编码，从城市列表获取，空为全部
    - category_code: 热点榜分类编码，从热点榜分类获取，空为全部
    - end_date: 快照结束时间 格式10位时间戳
    - start_date: 快照开始时间 格式10位时间戳
    ### 返回:
    - 活动日历

    # [English]
    ### Purpose:
    - Get the activity calendar
    ### Parameters:
    - city_code: City code, get from city list, empty for all
    - category_code: Hot list category code, get from hot list category, empty for all
    - end_date: Snapshot end time format 10 digit timestamp
    - start_date: Snapshot start time format 10 digit timestamp
    ### Return:
    - Activity calendar

    Args:
        body (BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取活动日历/Fetch activity calendar

     # [中文]
    ### 用途:
    - 获取活动日历
    ### 参数:
    - city_code: 城市编码，从城市列表获取，空为全部
    - category_code: 热点榜分类编码，从热点榜分类获取，空为全部
    - end_date: 快照结束时间 格式10位时间戳
    - start_date: 快照开始时间 格式10位时间戳
    ### 返回:
    - 活动日历

    # [English]
    ### Purpose:
    - Get the activity calendar
    ### Parameters:
    - city_code: City code, get from city list, empty for all
    - category_code: Hot list category code, get from hot list category, empty for all
    - end_date: Snapshot end time format 10 digit timestamp
    - start_date: Snapshot start time format 10 digit timestamp
    ### Return:
    - Activity calendar

    Args:
        body (BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
