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
    field_type_: str,
    field_range_: str,
    flow_type: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["kolId"] = kol_id

    params["_type"] = field_type_

    params["_range"] = field_range_

    params["flowType"] = flow_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/xingtu/kol_data_overview_v1",
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
    field_type_: str,
    field_range_: str,
    flow_type: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol数据概览V1/Get kol Data Overview V1

     # [中文]
    ### 用途:
    - 获取kol数据概览V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - _type: 类型, 支持以下参数:
        - _1 :个人视频(personal video)
        - _2 :星图视频(xingtu video)
    - _range: 范围, 支持以下参数:
        - _2 :近30天(last 30 days)
        - _3 :近90天(last 90 days)
    - flowType: 流量类型, 支持以下参数:
        - 1 : 默认(default)
    ### 返回:
    - kol数据概览

    # [English]
    ### Purpose:
    - Get kol Data Overview V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - _type: Type, supports the following parameters:
        - _1 :Personal Video
        - _2 :Xingtu Video
    - _range: Range, supports the following parameters:
        - _2 :Last 30 days
        - _3 :Last 90 days
    - flowType: Flow Type, supports the following parameters:
        - 1 : Default
    ### Return:
    - kol Data Overview

    # [示例/Example]
    kolId = \"7048929565493690398\"
    _type = \"_1\"
    _range = \"_2\"
    flowType = 1

    Args:
        kol_id (str): 用户的kolId/User kolId
        field_type_ (str): 类型/Type
        field_range_ (str): 范围/Range
        flow_type (int): 流量类型/Flow Type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        kol_id=kol_id,
        field_type_=field_type_,
        field_range_=field_range_,
        flow_type=flow_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    kol_id: str,
    field_type_: str,
    field_range_: str,
    flow_type: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol数据概览V1/Get kol Data Overview V1

     # [中文]
    ### 用途:
    - 获取kol数据概览V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - _type: 类型, 支持以下参数:
        - _1 :个人视频(personal video)
        - _2 :星图视频(xingtu video)
    - _range: 范围, 支持以下参数:
        - _2 :近30天(last 30 days)
        - _3 :近90天(last 90 days)
    - flowType: 流量类型, 支持以下参数:
        - 1 : 默认(default)
    ### 返回:
    - kol数据概览

    # [English]
    ### Purpose:
    - Get kol Data Overview V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - _type: Type, supports the following parameters:
        - _1 :Personal Video
        - _2 :Xingtu Video
    - _range: Range, supports the following parameters:
        - _2 :Last 30 days
        - _3 :Last 90 days
    - flowType: Flow Type, supports the following parameters:
        - 1 : Default
    ### Return:
    - kol Data Overview

    # [示例/Example]
    kolId = \"7048929565493690398\"
    _type = \"_1\"
    _range = \"_2\"
    flowType = 1

    Args:
        kol_id (str): 用户的kolId/User kolId
        field_type_ (str): 类型/Type
        field_range_ (str): 范围/Range
        flow_type (int): 流量类型/Flow Type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        kol_id=kol_id,
        field_type_=field_type_,
        field_range_=field_range_,
        flow_type=flow_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    kol_id: str,
    field_type_: str,
    field_range_: str,
    flow_type: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol数据概览V1/Get kol Data Overview V1

     # [中文]
    ### 用途:
    - 获取kol数据概览V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - _type: 类型, 支持以下参数:
        - _1 :个人视频(personal video)
        - _2 :星图视频(xingtu video)
    - _range: 范围, 支持以下参数:
        - _2 :近30天(last 30 days)
        - _3 :近90天(last 90 days)
    - flowType: 流量类型, 支持以下参数:
        - 1 : 默认(default)
    ### 返回:
    - kol数据概览

    # [English]
    ### Purpose:
    - Get kol Data Overview V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - _type: Type, supports the following parameters:
        - _1 :Personal Video
        - _2 :Xingtu Video
    - _range: Range, supports the following parameters:
        - _2 :Last 30 days
        - _3 :Last 90 days
    - flowType: Flow Type, supports the following parameters:
        - 1 : Default
    ### Return:
    - kol Data Overview

    # [示例/Example]
    kolId = \"7048929565493690398\"
    _type = \"_1\"
    _range = \"_2\"
    flowType = 1

    Args:
        kol_id (str): 用户的kolId/User kolId
        field_type_ (str): 类型/Type
        field_range_ (str): 范围/Range
        flow_type (int): 流量类型/Flow Type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        kol_id=kol_id,
        field_type_=field_type_,
        field_range_=field_range_,
        flow_type=flow_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    kol_id: str,
    field_type_: str,
    field_range_: str,
    flow_type: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取kol数据概览V1/Get kol Data Overview V1

     # [中文]
    ### 用途:
    - 获取kol数据概览V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - kolId: 用户的kolId, 可以从接口以下接口获取：
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - _type: 类型, 支持以下参数:
        - _1 :个人视频(personal video)
        - _2 :星图视频(xingtu video)
    - _range: 范围, 支持以下参数:
        - _2 :近30天(last 30 days)
        - _3 :近90天(last 90 days)
    - flowType: 流量类型, 支持以下参数:
        - 1 : 默认(default)
    ### 返回:
    - kol数据概览

    # [English]
    ### Purpose:
    - Get kol Data Overview V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - kolId: User kolId, can be obtained from the following interfaces:
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id`
        - `/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id`
    - _type: Type, supports the following parameters:
        - _1 :Personal Video
        - _2 :Xingtu Video
    - _range: Range, supports the following parameters:
        - _2 :Last 30 days
        - _3 :Last 90 days
    - flowType: Flow Type, supports the following parameters:
        - 1 : Default
    ### Return:
    - kol Data Overview

    # [示例/Example]
    kolId = \"7048929565493690398\"
    _type = \"_1\"
    _range = \"_2\"
    flowType = 1

    Args:
        kol_id (str): 用户的kolId/User kolId
        field_type_ (str): 类型/Type
        field_range_ (str): 范围/Range
        flow_type (int): 流量类型/Flow Type

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
            field_type_=field_type_,
            field_range_=field_range_,
            flow_type=flow_type,
        )
    ).parsed
