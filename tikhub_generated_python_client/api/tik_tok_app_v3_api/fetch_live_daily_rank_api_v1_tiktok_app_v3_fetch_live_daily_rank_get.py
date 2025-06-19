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
    anchor_id: Union[Unset, str] = "6952422426752205830",
    room_id: Union[Unset, str] = "7380221319910312750",
    rank_type: Union[Unset, int] = 8,
    region_type: Union[Unset, int] = 1,
    gap_interval: Union[Unset, int] = 0,
    cookie: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["anchor_id"] = anchor_id

    params["room_id"] = room_id

    params["rank_type"] = rank_type

    params["region_type"] = region_type

    params["gap_interval"] = gap_interval

    params["cookie"] = cookie

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_live_daily_rank",
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
    anchor_id: Union[Unset, str] = "6952422426752205830",
    room_id: Union[Unset, str] = "7380221319910312750",
    rank_type: Union[Unset, int] = 8,
    region_type: Union[Unset, int] = 1,
    gap_interval: Union[Unset, int] = 0,
    cookie: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取直播每日榜单数据/Get live daily rank data

     # [中文]
    ### 用途:
    - 获取直播每日榜单数据
    ### 参数:
    - anchor_id: 主播id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的主播id。
    - room_id: 直播间id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的id。
    - rank_type: 榜单类型
        - `0`: 每小时排行榜
        - `1`: 每周排行榜
        - `5`: 新星排行榜
        - `6`: 销售排行榜
        - `8`: 每日排行榜
        - `10`: 游戏排行榜
        - `11`: 每日游戏排行榜
        - `12`: 名人堂排行榜
        - `13`: 冠军赛排行榜
        - `14`: 每日新秀排行榜
        - `15`: 人气直播榜
        - `16`: D5段位榜
        - `20`: 绝地求生排行榜
        - `21`: 王者荣耀排行榜
        - `22`: Free Fire 排行榜
        - `1001`: 联盟竞赛排行榜
        - `-1`: 未知排行榜
    - region_type: 地区类型，使用默认值即可，具体含义不明。
    - gap_interval: 时间间隔，使用默认值代表当天，使用-1代表排名记录。
    - cookie: 用户自己的cookie，可选参数，用于接口不可用时使用。
    ### 返回:
    - 直播每日榜单数据

    # [English]
    ### Purpose:
    - Get live daily rank data
    ### Parameters:
    - anchor_id: Anchor id, which can be obtained from the live room information interface, use the
    default value, this parameter will affect the returned data, you can try different anchor ids of
    different live rooms.
    - room_id: Live room id, which can be obtained from the live room information interface, use the
    default value, this parameter will affect the returned data, you can try different room ids of
    different live rooms.
    - rank_type: Rank type
        - `0`: Hourly Rank
        - `1`: Weekly Rank
        - `5`: Rookie Star Rank
        - `6`: Sale Rank
        - `8`: Daily Rank
        - `10`: Game Rank
        - `11`: Daily Game Rank
        - `12`: Hall of Fame Rank
        - `13`: Champion Tournament Rank
        - `14`: Daily Rookie Star Rank
        - `15`: Popular Live Stream Rank
        - `16`: D5 Level Rank
        - `20`: PUBG Rank
        - `21`: MLBB Rank
        - `22`: Free Fire Rank
        - `1001`: League Campaign Rank
        - `-1`: Unknown Rank

    - region_type: Region type, use the default value, the specific meaning is unknown.
    - gap_interval: Time interval, use the default value to represent the current day, use -1 to
    represent the ranking record.
    - cookie: User's own cookie, optional parameter, used when the interface is not available.
    ### Return:
    - Live daily rank data

    Args:
        anchor_id (Union[Unset, str]): 主播id/Anchor id Default: '6952422426752205830'.
        room_id (Union[Unset, str]): 直播间id/Live room id Default: '7380221319910312750'.
        rank_type (Union[Unset, int]): 榜单类型/Rank type Default: 8.
        region_type (Union[Unset, int]): 地区类型/Region type Default: 1.
        gap_interval (Union[Unset, int]): 时间间隔/Time interval Default: 0.
        cookie (Union[Unset, str]): 用户自己的cookie/User's own cookie Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        anchor_id=anchor_id,
        room_id=room_id,
        rank_type=rank_type,
        region_type=region_type,
        gap_interval=gap_interval,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    anchor_id: Union[Unset, str] = "6952422426752205830",
    room_id: Union[Unset, str] = "7380221319910312750",
    rank_type: Union[Unset, int] = 8,
    region_type: Union[Unset, int] = 1,
    gap_interval: Union[Unset, int] = 0,
    cookie: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取直播每日榜单数据/Get live daily rank data

     # [中文]
    ### 用途:
    - 获取直播每日榜单数据
    ### 参数:
    - anchor_id: 主播id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的主播id。
    - room_id: 直播间id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的id。
    - rank_type: 榜单类型
        - `0`: 每小时排行榜
        - `1`: 每周排行榜
        - `5`: 新星排行榜
        - `6`: 销售排行榜
        - `8`: 每日排行榜
        - `10`: 游戏排行榜
        - `11`: 每日游戏排行榜
        - `12`: 名人堂排行榜
        - `13`: 冠军赛排行榜
        - `14`: 每日新秀排行榜
        - `15`: 人气直播榜
        - `16`: D5段位榜
        - `20`: 绝地求生排行榜
        - `21`: 王者荣耀排行榜
        - `22`: Free Fire 排行榜
        - `1001`: 联盟竞赛排行榜
        - `-1`: 未知排行榜
    - region_type: 地区类型，使用默认值即可，具体含义不明。
    - gap_interval: 时间间隔，使用默认值代表当天，使用-1代表排名记录。
    - cookie: 用户自己的cookie，可选参数，用于接口不可用时使用。
    ### 返回:
    - 直播每日榜单数据

    # [English]
    ### Purpose:
    - Get live daily rank data
    ### Parameters:
    - anchor_id: Anchor id, which can be obtained from the live room information interface, use the
    default value, this parameter will affect the returned data, you can try different anchor ids of
    different live rooms.
    - room_id: Live room id, which can be obtained from the live room information interface, use the
    default value, this parameter will affect the returned data, you can try different room ids of
    different live rooms.
    - rank_type: Rank type
        - `0`: Hourly Rank
        - `1`: Weekly Rank
        - `5`: Rookie Star Rank
        - `6`: Sale Rank
        - `8`: Daily Rank
        - `10`: Game Rank
        - `11`: Daily Game Rank
        - `12`: Hall of Fame Rank
        - `13`: Champion Tournament Rank
        - `14`: Daily Rookie Star Rank
        - `15`: Popular Live Stream Rank
        - `16`: D5 Level Rank
        - `20`: PUBG Rank
        - `21`: MLBB Rank
        - `22`: Free Fire Rank
        - `1001`: League Campaign Rank
        - `-1`: Unknown Rank

    - region_type: Region type, use the default value, the specific meaning is unknown.
    - gap_interval: Time interval, use the default value to represent the current day, use -1 to
    represent the ranking record.
    - cookie: User's own cookie, optional parameter, used when the interface is not available.
    ### Return:
    - Live daily rank data

    Args:
        anchor_id (Union[Unset, str]): 主播id/Anchor id Default: '6952422426752205830'.
        room_id (Union[Unset, str]): 直播间id/Live room id Default: '7380221319910312750'.
        rank_type (Union[Unset, int]): 榜单类型/Rank type Default: 8.
        region_type (Union[Unset, int]): 地区类型/Region type Default: 1.
        gap_interval (Union[Unset, int]): 时间间隔/Time interval Default: 0.
        cookie (Union[Unset, str]): 用户自己的cookie/User's own cookie Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        anchor_id=anchor_id,
        room_id=room_id,
        rank_type=rank_type,
        region_type=region_type,
        gap_interval=gap_interval,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    anchor_id: Union[Unset, str] = "6952422426752205830",
    room_id: Union[Unset, str] = "7380221319910312750",
    rank_type: Union[Unset, int] = 8,
    region_type: Union[Unset, int] = 1,
    gap_interval: Union[Unset, int] = 0,
    cookie: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取直播每日榜单数据/Get live daily rank data

     # [中文]
    ### 用途:
    - 获取直播每日榜单数据
    ### 参数:
    - anchor_id: 主播id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的主播id。
    - room_id: 直播间id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的id。
    - rank_type: 榜单类型
        - `0`: 每小时排行榜
        - `1`: 每周排行榜
        - `5`: 新星排行榜
        - `6`: 销售排行榜
        - `8`: 每日排行榜
        - `10`: 游戏排行榜
        - `11`: 每日游戏排行榜
        - `12`: 名人堂排行榜
        - `13`: 冠军赛排行榜
        - `14`: 每日新秀排行榜
        - `15`: 人气直播榜
        - `16`: D5段位榜
        - `20`: 绝地求生排行榜
        - `21`: 王者荣耀排行榜
        - `22`: Free Fire 排行榜
        - `1001`: 联盟竞赛排行榜
        - `-1`: 未知排行榜
    - region_type: 地区类型，使用默认值即可，具体含义不明。
    - gap_interval: 时间间隔，使用默认值代表当天，使用-1代表排名记录。
    - cookie: 用户自己的cookie，可选参数，用于接口不可用时使用。
    ### 返回:
    - 直播每日榜单数据

    # [English]
    ### Purpose:
    - Get live daily rank data
    ### Parameters:
    - anchor_id: Anchor id, which can be obtained from the live room information interface, use the
    default value, this parameter will affect the returned data, you can try different anchor ids of
    different live rooms.
    - room_id: Live room id, which can be obtained from the live room information interface, use the
    default value, this parameter will affect the returned data, you can try different room ids of
    different live rooms.
    - rank_type: Rank type
        - `0`: Hourly Rank
        - `1`: Weekly Rank
        - `5`: Rookie Star Rank
        - `6`: Sale Rank
        - `8`: Daily Rank
        - `10`: Game Rank
        - `11`: Daily Game Rank
        - `12`: Hall of Fame Rank
        - `13`: Champion Tournament Rank
        - `14`: Daily Rookie Star Rank
        - `15`: Popular Live Stream Rank
        - `16`: D5 Level Rank
        - `20`: PUBG Rank
        - `21`: MLBB Rank
        - `22`: Free Fire Rank
        - `1001`: League Campaign Rank
        - `-1`: Unknown Rank

    - region_type: Region type, use the default value, the specific meaning is unknown.
    - gap_interval: Time interval, use the default value to represent the current day, use -1 to
    represent the ranking record.
    - cookie: User's own cookie, optional parameter, used when the interface is not available.
    ### Return:
    - Live daily rank data

    Args:
        anchor_id (Union[Unset, str]): 主播id/Anchor id Default: '6952422426752205830'.
        room_id (Union[Unset, str]): 直播间id/Live room id Default: '7380221319910312750'.
        rank_type (Union[Unset, int]): 榜单类型/Rank type Default: 8.
        region_type (Union[Unset, int]): 地区类型/Region type Default: 1.
        gap_interval (Union[Unset, int]): 时间间隔/Time interval Default: 0.
        cookie (Union[Unset, str]): 用户自己的cookie/User's own cookie Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        anchor_id=anchor_id,
        room_id=room_id,
        rank_type=rank_type,
        region_type=region_type,
        gap_interval=gap_interval,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    anchor_id: Union[Unset, str] = "6952422426752205830",
    room_id: Union[Unset, str] = "7380221319910312750",
    rank_type: Union[Unset, int] = 8,
    region_type: Union[Unset, int] = 1,
    gap_interval: Union[Unset, int] = 0,
    cookie: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取直播每日榜单数据/Get live daily rank data

     # [中文]
    ### 用途:
    - 获取直播每日榜单数据
    ### 参数:
    - anchor_id: 主播id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的主播id。
    - room_id: 直播间id，可以从直播间信息接口获取，使用默认值即可，该参数会影响返回的数据，你可以尝试不同直播间的id。
    - rank_type: 榜单类型
        - `0`: 每小时排行榜
        - `1`: 每周排行榜
        - `5`: 新星排行榜
        - `6`: 销售排行榜
        - `8`: 每日排行榜
        - `10`: 游戏排行榜
        - `11`: 每日游戏排行榜
        - `12`: 名人堂排行榜
        - `13`: 冠军赛排行榜
        - `14`: 每日新秀排行榜
        - `15`: 人气直播榜
        - `16`: D5段位榜
        - `20`: 绝地求生排行榜
        - `21`: 王者荣耀排行榜
        - `22`: Free Fire 排行榜
        - `1001`: 联盟竞赛排行榜
        - `-1`: 未知排行榜
    - region_type: 地区类型，使用默认值即可，具体含义不明。
    - gap_interval: 时间间隔，使用默认值代表当天，使用-1代表排名记录。
    - cookie: 用户自己的cookie，可选参数，用于接口不可用时使用。
    ### 返回:
    - 直播每日榜单数据

    # [English]
    ### Purpose:
    - Get live daily rank data
    ### Parameters:
    - anchor_id: Anchor id, which can be obtained from the live room information interface, use the
    default value, this parameter will affect the returned data, you can try different anchor ids of
    different live rooms.
    - room_id: Live room id, which can be obtained from the live room information interface, use the
    default value, this parameter will affect the returned data, you can try different room ids of
    different live rooms.
    - rank_type: Rank type
        - `0`: Hourly Rank
        - `1`: Weekly Rank
        - `5`: Rookie Star Rank
        - `6`: Sale Rank
        - `8`: Daily Rank
        - `10`: Game Rank
        - `11`: Daily Game Rank
        - `12`: Hall of Fame Rank
        - `13`: Champion Tournament Rank
        - `14`: Daily Rookie Star Rank
        - `15`: Popular Live Stream Rank
        - `16`: D5 Level Rank
        - `20`: PUBG Rank
        - `21`: MLBB Rank
        - `22`: Free Fire Rank
        - `1001`: League Campaign Rank
        - `-1`: Unknown Rank

    - region_type: Region type, use the default value, the specific meaning is unknown.
    - gap_interval: Time interval, use the default value to represent the current day, use -1 to
    represent the ranking record.
    - cookie: User's own cookie, optional parameter, used when the interface is not available.
    ### Return:
    - Live daily rank data

    Args:
        anchor_id (Union[Unset, str]): 主播id/Anchor id Default: '6952422426752205830'.
        room_id (Union[Unset, str]): 直播间id/Live room id Default: '7380221319910312750'.
        rank_type (Union[Unset, int]): 榜单类型/Rank type Default: 8.
        region_type (Union[Unset, int]): 地区类型/Region type Default: 1.
        gap_interval (Union[Unset, int]): 时间间隔/Time interval Default: 0.
        cookie (Union[Unset, str]): 用户自己的cookie/User's own cookie Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            anchor_id=anchor_id,
            room_id=room_id,
            rank_type=rank_type,
            region_type=region_type,
            gap_interval=gap_interval,
            cookie=cookie,
        )
    ).parsed
