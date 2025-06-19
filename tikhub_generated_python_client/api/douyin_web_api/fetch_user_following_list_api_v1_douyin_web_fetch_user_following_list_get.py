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
    sec_user_id: Union[Unset, str] = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70",
    max_time: Union[Unset, str] = "0",
    count: Union[Unset, int] = 20,
    source_type: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sec_user_id"] = sec_user_id

    params["max_time"] = max_time

    params["count"] = count

    params["source_type"] = source_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_user_following_list",
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
    sec_user_id: Union[Unset, str] = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70",
    max_time: Union[Unset, str] = "0",
    count: Union[Unset, int] = 20,
    source_type: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户关注列表/Get user following list

     # [中文]
    ### 用途:
    - 获取用户关注列表
    - 第一次请求时，max_time传`0`，source_type传`2`，然后会返回一个空的粉丝列表，里面包含了max_time，然后再次请求时，max_time传上一次请求返回的max_time，
    source_type传`1`，即可获取到粉丝列表。
    - 如果不按照上述方式请求，可能会导致返回数据包含重复数据。
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。
    - count: 数量，默认为20，建议保持不变。
    - source_type: 来源类型，默认为`1`，第一次请求时使用`2`作为来源类型，然后再次请求时使用`1`作为来源类型。
    ### 返回:
    - 关注列表

    # [English]
    ### Purpose:
    - Get user following list
    - When requesting for the first time, pass `0` for max_time, pass `2` for source_type, and an empty
    fans list will be returned, which contains max_time, then pass the max_time returned by the previous
    request for paging each time, pass `1` for source_type, you can get the fans list.
    - If you do not request according to the above method, it may cause the returned data to contain
    duplicate data.

    ### Parameters:
    - sec_user_id: User sec_user_id
    - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging.
    - count: Number, default is 20, it is recommended to keep it unchanged.
    - source_type: Source type, default is `1`, use `2` as the source type for the first request, and
    then use `1` as the source type for the subsequent request.
    ### Return:
    - Following list

    # [示例/Example]
    sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"
    max_time = \"0\"
    count = 20
    source_type = 2

    Args:
        sec_user_id (Union[Unset, str]): 用户sec_user_id/User sec_user_id Default:
            'MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70'.
        max_time (Union[Unset, str]): 最大时间戳/Maximum timestamp Default: '0'.
        count (Union[Unset, int]): 数量/Number Default: 20.
        source_type (Union[Unset, int]): 来源类型/Source type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_user_id=sec_user_id,
        max_time=max_time,
        count=count,
        source_type=source_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sec_user_id: Union[Unset, str] = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70",
    max_time: Union[Unset, str] = "0",
    count: Union[Unset, int] = 20,
    source_type: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户关注列表/Get user following list

     # [中文]
    ### 用途:
    - 获取用户关注列表
    - 第一次请求时，max_time传`0`，source_type传`2`，然后会返回一个空的粉丝列表，里面包含了max_time，然后再次请求时，max_time传上一次请求返回的max_time，
    source_type传`1`，即可获取到粉丝列表。
    - 如果不按照上述方式请求，可能会导致返回数据包含重复数据。
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。
    - count: 数量，默认为20，建议保持不变。
    - source_type: 来源类型，默认为`1`，第一次请求时使用`2`作为来源类型，然后再次请求时使用`1`作为来源类型。
    ### 返回:
    - 关注列表

    # [English]
    ### Purpose:
    - Get user following list
    - When requesting for the first time, pass `0` for max_time, pass `2` for source_type, and an empty
    fans list will be returned, which contains max_time, then pass the max_time returned by the previous
    request for paging each time, pass `1` for source_type, you can get the fans list.
    - If you do not request according to the above method, it may cause the returned data to contain
    duplicate data.

    ### Parameters:
    - sec_user_id: User sec_user_id
    - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging.
    - count: Number, default is 20, it is recommended to keep it unchanged.
    - source_type: Source type, default is `1`, use `2` as the source type for the first request, and
    then use `1` as the source type for the subsequent request.
    ### Return:
    - Following list

    # [示例/Example]
    sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"
    max_time = \"0\"
    count = 20
    source_type = 2

    Args:
        sec_user_id (Union[Unset, str]): 用户sec_user_id/User sec_user_id Default:
            'MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70'.
        max_time (Union[Unset, str]): 最大时间戳/Maximum timestamp Default: '0'.
        count (Union[Unset, int]): 数量/Number Default: 20.
        source_type (Union[Unset, int]): 来源类型/Source type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        sec_user_id=sec_user_id,
        max_time=max_time,
        count=count,
        source_type=source_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sec_user_id: Union[Unset, str] = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70",
    max_time: Union[Unset, str] = "0",
    count: Union[Unset, int] = 20,
    source_type: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户关注列表/Get user following list

     # [中文]
    ### 用途:
    - 获取用户关注列表
    - 第一次请求时，max_time传`0`，source_type传`2`，然后会返回一个空的粉丝列表，里面包含了max_time，然后再次请求时，max_time传上一次请求返回的max_time，
    source_type传`1`，即可获取到粉丝列表。
    - 如果不按照上述方式请求，可能会导致返回数据包含重复数据。
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。
    - count: 数量，默认为20，建议保持不变。
    - source_type: 来源类型，默认为`1`，第一次请求时使用`2`作为来源类型，然后再次请求时使用`1`作为来源类型。
    ### 返回:
    - 关注列表

    # [English]
    ### Purpose:
    - Get user following list
    - When requesting for the first time, pass `0` for max_time, pass `2` for source_type, and an empty
    fans list will be returned, which contains max_time, then pass the max_time returned by the previous
    request for paging each time, pass `1` for source_type, you can get the fans list.
    - If you do not request according to the above method, it may cause the returned data to contain
    duplicate data.

    ### Parameters:
    - sec_user_id: User sec_user_id
    - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging.
    - count: Number, default is 20, it is recommended to keep it unchanged.
    - source_type: Source type, default is `1`, use `2` as the source type for the first request, and
    then use `1` as the source type for the subsequent request.
    ### Return:
    - Following list

    # [示例/Example]
    sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"
    max_time = \"0\"
    count = 20
    source_type = 2

    Args:
        sec_user_id (Union[Unset, str]): 用户sec_user_id/User sec_user_id Default:
            'MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70'.
        max_time (Union[Unset, str]): 最大时间戳/Maximum timestamp Default: '0'.
        count (Union[Unset, int]): 数量/Number Default: 20.
        source_type (Union[Unset, int]): 来源类型/Source type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_user_id=sec_user_id,
        max_time=max_time,
        count=count,
        source_type=source_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sec_user_id: Union[Unset, str] = "MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70",
    max_time: Union[Unset, str] = "0",
    count: Union[Unset, int] = 20,
    source_type: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户关注列表/Get user following list

     # [中文]
    ### 用途:
    - 获取用户关注列表
    - 第一次请求时，max_time传`0`，source_type传`2`，然后会返回一个空的粉丝列表，里面包含了max_time，然后再次请求时，max_time传上一次请求返回的max_time，
    source_type传`1`，即可获取到粉丝列表。
    - 如果不按照上述方式请求，可能会导致返回数据包含重复数据。
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - max_time: 最大时间戳，默认为0，后续从返回数据中获取，用于翻页。
    - count: 数量，默认为20，建议保持不变。
    - source_type: 来源类型，默认为`1`，第一次请求时使用`2`作为来源类型，然后再次请求时使用`1`作为来源类型。
    ### 返回:
    - 关注列表

    # [English]
    ### Purpose:
    - Get user following list
    - When requesting for the first time, pass `0` for max_time, pass `2` for source_type, and an empty
    fans list will be returned, which contains max_time, then pass the max_time returned by the previous
    request for paging each time, pass `1` for source_type, you can get the fans list.
    - If you do not request according to the above method, it may cause the returned data to contain
    duplicate data.

    ### Parameters:
    - sec_user_id: User sec_user_id
    - max_time: Maximum timestamp, default is 0, get from the returned data later, used for paging.
    - count: Number, default is 20, it is recommended to keep it unchanged.
    - source_type: Source type, default is `1`, use `2` as the source type for the first request, and
    then use `1` as the source type for the subsequent request.
    ### Return:
    - Following list

    # [示例/Example]
    sec_user = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"
    max_time = \"0\"
    count = 20
    source_type = 2

    Args:
        sec_user_id (Union[Unset, str]): 用户sec_user_id/User sec_user_id Default:
            'MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70'.
        max_time (Union[Unset, str]): 最大时间戳/Maximum timestamp Default: '0'.
        count (Union[Unset, int]): 数量/Number Default: 20.
        source_type (Union[Unset, int]): 来源类型/Source type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            sec_user_id=sec_user_id,
            max_time=max_time,
            count=count,
            source_type=source_type,
        )
    ).parsed
