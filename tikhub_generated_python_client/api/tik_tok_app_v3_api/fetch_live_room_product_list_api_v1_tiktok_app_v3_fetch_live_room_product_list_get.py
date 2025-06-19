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
    room_id: str,
    author_id: str,
    page_size: Union[Unset, int] = 15,
    offset: Union[Unset, int] = 0,
    region: Union[Unset, str] = "US",
    cookie: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["room_id"] = room_id

    params["author_id"] = author_id

    params["page_size"] = page_size

    params["offset"] = offset

    params["region"] = region

    params["cookie"] = cookie

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_live_room_product_list",
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
    room_id: str,
    author_id: str,
    page_size: Union[Unset, int] = 15,
    offset: Union[Unset, int] = 0,
    region: Union[Unset, str] = "US",
    cookie: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播间商品列表数据/Get live room product list data

     # [中文]
    ### 用途:
    - 获取直播间商品列表数据
    ### 参数:
    - room_id: 直播间id，必填参数。
    - author_id: 主播id，必填参数。
    - page_size: 每页数量，可选参数，默认为15。
    - offset: 翻页游标，可选参数，默认为0，每次翻页增加15。
    - region: 地区，可选参数，默认为`US`，如果使用其他地区，如：`VN`，请自行携带Cookie，否则无法获取数据。
    - cookie: 用户自己的cookie，可选参数，用于爬取除`US`以外的地区数据。
    ### 参数获取:
    - 第一步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"`接口获取直播间id（room_id）。
    - 第二步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"`接口获取直播间信息。
    - 第三步：使用第二步返回的JSON数据中使用JSONPATH获取`$.data.data.owner.id_str`字段的值作为主播id（author_id）。
    ### 返回:
    - 直播间商品列表数据

    # [English]
    ### Purpose:
    - Get live room product list data
    ### Parameters:
    - room_id: Live room id, required parameter.
    - author_id: Anchor id, required parameter.
    - page_size: Number per page, optional parameter, default is 15.
    - offset: Page turning cursor, optional parameter, default is 0, increasing by 15 each time.
    - region: Region, optional parameter, default is `US`, if you use other regions, such as: `VN`,
    please bring your own Cookie, otherwise you will not be able to get data.
    - cookie: User's own cookie, optional parameter, used to crawl data from regions other than `US`.
    ### Get Parameters:
    - Step 1: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"` to get the
    live room id (room_id).
    - Step 2: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"` to get
    the live room information.
    - Step 3: Use the JSONPATH in the JSON data returned in the second step to get the value of the
    field `$.data.data.owner.id_str` as the anchor id (author_id).
    ### Return:
    - Live room product list data

    # [示例/Example]
    room_id = \"7420741353250507562\"
    author_id = \"7408859677050274859\"
    page_size = 15
    offset = 0

    Args:
        room_id (str): 直播间id/Live room id
        author_id (str): 主播id/Anchor id
        page_size (Union[Unset, int]): 数量/Number Default: 15.
        offset (Union[Unset, int]): 数量/Number Default: 0.
        region (Union[Unset, str]): 地区/Region Default: 'US'.
        cookie (Union[Unset, str]): 用户自己的cookie/User's own cookie Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        author_id=author_id,
        page_size=page_size,
        offset=offset,
        region=region,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    room_id: str,
    author_id: str,
    page_size: Union[Unset, int] = 15,
    offset: Union[Unset, int] = 0,
    region: Union[Unset, str] = "US",
    cookie: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播间商品列表数据/Get live room product list data

     # [中文]
    ### 用途:
    - 获取直播间商品列表数据
    ### 参数:
    - room_id: 直播间id，必填参数。
    - author_id: 主播id，必填参数。
    - page_size: 每页数量，可选参数，默认为15。
    - offset: 翻页游标，可选参数，默认为0，每次翻页增加15。
    - region: 地区，可选参数，默认为`US`，如果使用其他地区，如：`VN`，请自行携带Cookie，否则无法获取数据。
    - cookie: 用户自己的cookie，可选参数，用于爬取除`US`以外的地区数据。
    ### 参数获取:
    - 第一步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"`接口获取直播间id（room_id）。
    - 第二步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"`接口获取直播间信息。
    - 第三步：使用第二步返回的JSON数据中使用JSONPATH获取`$.data.data.owner.id_str`字段的值作为主播id（author_id）。
    ### 返回:
    - 直播间商品列表数据

    # [English]
    ### Purpose:
    - Get live room product list data
    ### Parameters:
    - room_id: Live room id, required parameter.
    - author_id: Anchor id, required parameter.
    - page_size: Number per page, optional parameter, default is 15.
    - offset: Page turning cursor, optional parameter, default is 0, increasing by 15 each time.
    - region: Region, optional parameter, default is `US`, if you use other regions, such as: `VN`,
    please bring your own Cookie, otherwise you will not be able to get data.
    - cookie: User's own cookie, optional parameter, used to crawl data from regions other than `US`.
    ### Get Parameters:
    - Step 1: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"` to get the
    live room id (room_id).
    - Step 2: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"` to get
    the live room information.
    - Step 3: Use the JSONPATH in the JSON data returned in the second step to get the value of the
    field `$.data.data.owner.id_str` as the anchor id (author_id).
    ### Return:
    - Live room product list data

    # [示例/Example]
    room_id = \"7420741353250507562\"
    author_id = \"7408859677050274859\"
    page_size = 15
    offset = 0

    Args:
        room_id (str): 直播间id/Live room id
        author_id (str): 主播id/Anchor id
        page_size (Union[Unset, int]): 数量/Number Default: 15.
        offset (Union[Unset, int]): 数量/Number Default: 0.
        region (Union[Unset, str]): 地区/Region Default: 'US'.
        cookie (Union[Unset, str]): 用户自己的cookie/User's own cookie Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        room_id=room_id,
        author_id=author_id,
        page_size=page_size,
        offset=offset,
        region=region,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    room_id: str,
    author_id: str,
    page_size: Union[Unset, int] = 15,
    offset: Union[Unset, int] = 0,
    region: Union[Unset, str] = "US",
    cookie: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播间商品列表数据/Get live room product list data

     # [中文]
    ### 用途:
    - 获取直播间商品列表数据
    ### 参数:
    - room_id: 直播间id，必填参数。
    - author_id: 主播id，必填参数。
    - page_size: 每页数量，可选参数，默认为15。
    - offset: 翻页游标，可选参数，默认为0，每次翻页增加15。
    - region: 地区，可选参数，默认为`US`，如果使用其他地区，如：`VN`，请自行携带Cookie，否则无法获取数据。
    - cookie: 用户自己的cookie，可选参数，用于爬取除`US`以外的地区数据。
    ### 参数获取:
    - 第一步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"`接口获取直播间id（room_id）。
    - 第二步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"`接口获取直播间信息。
    - 第三步：使用第二步返回的JSON数据中使用JSONPATH获取`$.data.data.owner.id_str`字段的值作为主播id（author_id）。
    ### 返回:
    - 直播间商品列表数据

    # [English]
    ### Purpose:
    - Get live room product list data
    ### Parameters:
    - room_id: Live room id, required parameter.
    - author_id: Anchor id, required parameter.
    - page_size: Number per page, optional parameter, default is 15.
    - offset: Page turning cursor, optional parameter, default is 0, increasing by 15 each time.
    - region: Region, optional parameter, default is `US`, if you use other regions, such as: `VN`,
    please bring your own Cookie, otherwise you will not be able to get data.
    - cookie: User's own cookie, optional parameter, used to crawl data from regions other than `US`.
    ### Get Parameters:
    - Step 1: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"` to get the
    live room id (room_id).
    - Step 2: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"` to get
    the live room information.
    - Step 3: Use the JSONPATH in the JSON data returned in the second step to get the value of the
    field `$.data.data.owner.id_str` as the anchor id (author_id).
    ### Return:
    - Live room product list data

    # [示例/Example]
    room_id = \"7420741353250507562\"
    author_id = \"7408859677050274859\"
    page_size = 15
    offset = 0

    Args:
        room_id (str): 直播间id/Live room id
        author_id (str): 主播id/Anchor id
        page_size (Union[Unset, int]): 数量/Number Default: 15.
        offset (Union[Unset, int]): 数量/Number Default: 0.
        region (Union[Unset, str]): 地区/Region Default: 'US'.
        cookie (Union[Unset, str]): 用户自己的cookie/User's own cookie Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        author_id=author_id,
        page_size=page_size,
        offset=offset,
        region=region,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    room_id: str,
    author_id: str,
    page_size: Union[Unset, int] = 15,
    offset: Union[Unset, int] = 0,
    region: Union[Unset, str] = "US",
    cookie: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播间商品列表数据/Get live room product list data

     # [中文]
    ### 用途:
    - 获取直播间商品列表数据
    ### 参数:
    - room_id: 直播间id，必填参数。
    - author_id: 主播id，必填参数。
    - page_size: 每页数量，可选参数，默认为15。
    - offset: 翻页游标，可选参数，默认为0，每次翻页增加15。
    - region: 地区，可选参数，默认为`US`，如果使用其他地区，如：`VN`，请自行携带Cookie，否则无法获取数据。
    - cookie: 用户自己的cookie，可选参数，用于爬取除`US`以外的地区数据。
    ### 参数获取:
    - 第一步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"`接口获取直播间id（room_id）。
    - 第二步：使用接口`f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"`接口获取直播间信息。
    - 第三步：使用第二步返回的JSON数据中使用JSONPATH获取`$.data.data.owner.id_str`字段的值作为主播id（author_id）。
    ### 返回:
    - 直播间商品列表数据

    # [English]
    ### Purpose:
    - Get live room product list data
    ### Parameters:
    - room_id: Live room id, required parameter.
    - author_id: Anchor id, required parameter.
    - page_size: Number per page, optional parameter, default is 15.
    - offset: Page turning cursor, optional parameter, default is 0, increasing by 15 each time.
    - region: Region, optional parameter, default is `US`, if you use other regions, such as: `VN`,
    please bring your own Cookie, otherwise you will not be able to get data.
    - cookie: User's own cookie, optional parameter, used to crawl data from regions other than `US`.
    ### Get Parameters:
    - Step 1: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/web/get_live_room_id\"` to get the
    live room id (room_id).
    - Step 2: Use the interface `f\"{TikHub_Domain}/api/v1/tiktok/app/v3/fetch_live_room_info\"` to get
    the live room information.
    - Step 3: Use the JSONPATH in the JSON data returned in the second step to get the value of the
    field `$.data.data.owner.id_str` as the anchor id (author_id).
    ### Return:
    - Live room product list data

    # [示例/Example]
    room_id = \"7420741353250507562\"
    author_id = \"7408859677050274859\"
    page_size = 15
    offset = 0

    Args:
        room_id (str): 直播间id/Live room id
        author_id (str): 主播id/Anchor id
        page_size (Union[Unset, int]): 数量/Number Default: 15.
        offset (Union[Unset, int]): 数量/Number Default: 0.
        region (Union[Unset, str]): 地区/Region Default: 'US'.
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
            room_id=room_id,
            author_id=author_id,
            page_size=page_size,
            offset=offset,
            region=region,
            cookie=cookie,
        )
    ).parsed
