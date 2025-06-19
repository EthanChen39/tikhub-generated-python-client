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
    billboard_type: str,
    snapshot_time: Union[Unset, str] = "20250106151500",
    start_date: Union[Unset, str] = "",
    end_date: Union[Unset, str] = "",
    keyword: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["billboard_type"] = billboard_type

    params["snapshot_time"] = snapshot_time

    params["start_date"] = start_date

    params["end_date"] = end_date

    params["keyword"] = keyword

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/billboard/fetch_hot_category_list",
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
    billboard_type: str,
    snapshot_time: Union[Unset, str] = "20250106151500",
    start_date: Union[Unset, str] = "",
    end_date: Union[Unset, str] = "",
    keyword: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取热点榜分类/Fetch hot list category

     # [中文]
    ### 用途:
    - 获取热点榜分类的id与热度
    - 注意：使用start_date和end_date参数需要移除snapshot_time参数才可以生效
    ### 参数:
    - billboard_type: 榜单类型
        - rise 上升热点榜
        - city 城市热点榜
        - total 热点总榜
    - snapshot_time: 快照时间
    - start_date: 快照开始时间
    - end_date: 快照结束时间
    - keyword: 热点搜索词
    ### 返回:
    - 热点榜分类

    # [English]
    ### Purpose:
    - Get the id and popularity of the hot list category
    - Note: Using start_date and end_date parameters requires removing the snapshot_time parameter
    - Note: snapshot_time and start_date, end_date parameters cannot be empty at the same time
    ### Parameters:
    - billboard_type: Billboard type
        - rise Rising hot list
        - city City hot list
        - total Total hot list
    - snapshot_time: Snapshot time
    - start_date: Snapshot start time
    - end_date: Snapshot end time
    - keyword: Hot search term
    ### Return:
    - Hot category list

    Args:
        billboard_type (str): 榜单类型
        snapshot_time (Union[Unset, str]): 快照时间 格式yyyyMMddHHmmss Default: '20250106151500'.
        start_date (Union[Unset, str]): 快照开始时间 格式yyyyMMdd Default: ''.
        end_date (Union[Unset, str]): 快照结束时间 格式yyyyMMdd Default: ''.
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        billboard_type=billboard_type,
        snapshot_time=snapshot_time,
        start_date=start_date,
        end_date=end_date,
        keyword=keyword,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    billboard_type: str,
    snapshot_time: Union[Unset, str] = "20250106151500",
    start_date: Union[Unset, str] = "",
    end_date: Union[Unset, str] = "",
    keyword: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取热点榜分类/Fetch hot list category

     # [中文]
    ### 用途:
    - 获取热点榜分类的id与热度
    - 注意：使用start_date和end_date参数需要移除snapshot_time参数才可以生效
    ### 参数:
    - billboard_type: 榜单类型
        - rise 上升热点榜
        - city 城市热点榜
        - total 热点总榜
    - snapshot_time: 快照时间
    - start_date: 快照开始时间
    - end_date: 快照结束时间
    - keyword: 热点搜索词
    ### 返回:
    - 热点榜分类

    # [English]
    ### Purpose:
    - Get the id and popularity of the hot list category
    - Note: Using start_date and end_date parameters requires removing the snapshot_time parameter
    - Note: snapshot_time and start_date, end_date parameters cannot be empty at the same time
    ### Parameters:
    - billboard_type: Billboard type
        - rise Rising hot list
        - city City hot list
        - total Total hot list
    - snapshot_time: Snapshot time
    - start_date: Snapshot start time
    - end_date: Snapshot end time
    - keyword: Hot search term
    ### Return:
    - Hot category list

    Args:
        billboard_type (str): 榜单类型
        snapshot_time (Union[Unset, str]): 快照时间 格式yyyyMMddHHmmss Default: '20250106151500'.
        start_date (Union[Unset, str]): 快照开始时间 格式yyyyMMdd Default: ''.
        end_date (Union[Unset, str]): 快照结束时间 格式yyyyMMdd Default: ''.
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        billboard_type=billboard_type,
        snapshot_time=snapshot_time,
        start_date=start_date,
        end_date=end_date,
        keyword=keyword,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    billboard_type: str,
    snapshot_time: Union[Unset, str] = "20250106151500",
    start_date: Union[Unset, str] = "",
    end_date: Union[Unset, str] = "",
    keyword: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取热点榜分类/Fetch hot list category

     # [中文]
    ### 用途:
    - 获取热点榜分类的id与热度
    - 注意：使用start_date和end_date参数需要移除snapshot_time参数才可以生效
    ### 参数:
    - billboard_type: 榜单类型
        - rise 上升热点榜
        - city 城市热点榜
        - total 热点总榜
    - snapshot_time: 快照时间
    - start_date: 快照开始时间
    - end_date: 快照结束时间
    - keyword: 热点搜索词
    ### 返回:
    - 热点榜分类

    # [English]
    ### Purpose:
    - Get the id and popularity of the hot list category
    - Note: Using start_date and end_date parameters requires removing the snapshot_time parameter
    - Note: snapshot_time and start_date, end_date parameters cannot be empty at the same time
    ### Parameters:
    - billboard_type: Billboard type
        - rise Rising hot list
        - city City hot list
        - total Total hot list
    - snapshot_time: Snapshot time
    - start_date: Snapshot start time
    - end_date: Snapshot end time
    - keyword: Hot search term
    ### Return:
    - Hot category list

    Args:
        billboard_type (str): 榜单类型
        snapshot_time (Union[Unset, str]): 快照时间 格式yyyyMMddHHmmss Default: '20250106151500'.
        start_date (Union[Unset, str]): 快照开始时间 格式yyyyMMdd Default: ''.
        end_date (Union[Unset, str]): 快照结束时间 格式yyyyMMdd Default: ''.
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        billboard_type=billboard_type,
        snapshot_time=snapshot_time,
        start_date=start_date,
        end_date=end_date,
        keyword=keyword,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    billboard_type: str,
    snapshot_time: Union[Unset, str] = "20250106151500",
    start_date: Union[Unset, str] = "",
    end_date: Union[Unset, str] = "",
    keyword: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取热点榜分类/Fetch hot list category

     # [中文]
    ### 用途:
    - 获取热点榜分类的id与热度
    - 注意：使用start_date和end_date参数需要移除snapshot_time参数才可以生效
    ### 参数:
    - billboard_type: 榜单类型
        - rise 上升热点榜
        - city 城市热点榜
        - total 热点总榜
    - snapshot_time: 快照时间
    - start_date: 快照开始时间
    - end_date: 快照结束时间
    - keyword: 热点搜索词
    ### 返回:
    - 热点榜分类

    # [English]
    ### Purpose:
    - Get the id and popularity of the hot list category
    - Note: Using start_date and end_date parameters requires removing the snapshot_time parameter
    - Note: snapshot_time and start_date, end_date parameters cannot be empty at the same time
    ### Parameters:
    - billboard_type: Billboard type
        - rise Rising hot list
        - city City hot list
        - total Total hot list
    - snapshot_time: Snapshot time
    - start_date: Snapshot start time
    - end_date: Snapshot end time
    - keyword: Hot search term
    ### Return:
    - Hot category list

    Args:
        billboard_type (str): 榜单类型
        snapshot_time (Union[Unset, str]): 快照时间 格式yyyyMMddHHmmss Default: '20250106151500'.
        start_date (Union[Unset, str]): 快照开始时间 格式yyyyMMdd Default: ''.
        end_date (Union[Unset, str]): 快照结束时间 格式yyyyMMdd Default: ''.
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            billboard_type=billboard_type,
            snapshot_time=snapshot_time,
            start_date=start_date,
            end_date=end_date,
            keyword=keyword,
        )
    ).parsed
