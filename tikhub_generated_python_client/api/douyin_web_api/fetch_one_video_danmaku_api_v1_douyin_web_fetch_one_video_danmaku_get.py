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
    item_id: str,
    duration: int,
    end_time: int,
    start_time: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["item_id"] = item_id

    params["duration"] = duration

    params["end_time"] = end_time

    params["start_time"] = start_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_one_video_danmaku",
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
    item_id: str,
    duration: int,
    end_time: int,
    start_time: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品视频弹幕数据/Get single video danmaku data

     # [中文]
    ### 用途:
    - 获取单个作品视频弹幕数据
    ### 参数:
    - item_id: 作品id
    - duration: 视频总时长
    - end_time: 结束时间
    - start_time: 开始时间
    ### 返回:
    - 视频弹幕数据

    # [English]
    ### Purpose:
    - Get single video danmaku data
    ### Parameters:
    - item_id: Video id
    - duration: Video total duration
    - end_time: End time
    - start_time: Start time
    ### Return:
    - Video danmaku data

    # [示例/Example]
    item_id = \"7355433624046472498\"
    duration = 15134
    end_time = 15133
    start_time = 0

    Args:
        item_id (str): 作品id/Video id
        duration (int): 视频总时长/Video total duration
        end_time (int): 结束时间/End time
        start_time (int): 开始时间/Start time

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        duration=duration,
        end_time=end_time,
        start_time=start_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    item_id: str,
    duration: int,
    end_time: int,
    start_time: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品视频弹幕数据/Get single video danmaku data

     # [中文]
    ### 用途:
    - 获取单个作品视频弹幕数据
    ### 参数:
    - item_id: 作品id
    - duration: 视频总时长
    - end_time: 结束时间
    - start_time: 开始时间
    ### 返回:
    - 视频弹幕数据

    # [English]
    ### Purpose:
    - Get single video danmaku data
    ### Parameters:
    - item_id: Video id
    - duration: Video total duration
    - end_time: End time
    - start_time: Start time
    ### Return:
    - Video danmaku data

    # [示例/Example]
    item_id = \"7355433624046472498\"
    duration = 15134
    end_time = 15133
    start_time = 0

    Args:
        item_id (str): 作品id/Video id
        duration (int): 视频总时长/Video total duration
        end_time (int): 结束时间/End time
        start_time (int): 开始时间/Start time

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        item_id=item_id,
        duration=duration,
        end_time=end_time,
        start_time=start_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    item_id: str,
    duration: int,
    end_time: int,
    start_time: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品视频弹幕数据/Get single video danmaku data

     # [中文]
    ### 用途:
    - 获取单个作品视频弹幕数据
    ### 参数:
    - item_id: 作品id
    - duration: 视频总时长
    - end_time: 结束时间
    - start_time: 开始时间
    ### 返回:
    - 视频弹幕数据

    # [English]
    ### Purpose:
    - Get single video danmaku data
    ### Parameters:
    - item_id: Video id
    - duration: Video total duration
    - end_time: End time
    - start_time: Start time
    ### Return:
    - Video danmaku data

    # [示例/Example]
    item_id = \"7355433624046472498\"
    duration = 15134
    end_time = 15133
    start_time = 0

    Args:
        item_id (str): 作品id/Video id
        duration (int): 视频总时长/Video total duration
        end_time (int): 结束时间/End time
        start_time (int): 开始时间/Start time

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        duration=duration,
        end_time=end_time,
        start_time=start_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    item_id: str,
    duration: int,
    end_time: int,
    start_time: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品视频弹幕数据/Get single video danmaku data

     # [中文]
    ### 用途:
    - 获取单个作品视频弹幕数据
    ### 参数:
    - item_id: 作品id
    - duration: 视频总时长
    - end_time: 结束时间
    - start_time: 开始时间
    ### 返回:
    - 视频弹幕数据

    # [English]
    ### Purpose:
    - Get single video danmaku data
    ### Parameters:
    - item_id: Video id
    - duration: Video total duration
    - end_time: End time
    - start_time: Start time
    ### Return:
    - Video danmaku data

    # [示例/Example]
    item_id = \"7355433624046472498\"
    duration = 15134
    end_time = 15133
    start_time = 0

    Args:
        item_id (str): 作品id/Video id
        duration (int): 视频总时长/Video total duration
        end_time (int): 结束时间/End time
        start_time (int): 开始时间/Start time

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            item_id=item_id,
            duration=duration,
            end_time=end_time,
            start_time=start_time,
        )
    ).parsed
