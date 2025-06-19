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
    category: str,
    max_behot_time: Union[Unset, str] = "",
    category_parameter: str,
    hashtag_name: str,
    sort_type: Union[Unset, str] = "0",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category"] = category

    params["max_behot_time"] = max_behot_time

    params["category_parameter"] = category_parameter

    params["hashtag_name"] = hashtag_name

    params["sort_type"] = sort_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/lemon8/app/fetch_topic_post_list",
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
    category: str,
    max_behot_time: Union[Unset, str] = "",
    category_parameter: str,
    hashtag_name: str,
    sort_type: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题作品列表/Get topic post list

     # [中文]
    ### 用途:
    - 获取话题作品列表
    ### 参数:
    - category: 话题分类 ID，可以从接口`/lemon8/app/fetch_topic_info`获取
    - max_behot_time: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的max_behot_time进行翻页。
    - category_parameter: 分类参数ID，可以从接口`/lemon8/app/fetch_topic_info`获取
    - hashtag_name: Hashtag名称，可以从接口`/lemon8/app/fetch_topic_info`获取
    - sort_type: 排序方式，0为默认排序，当前只支持使用默认排序，请不要传入其他值。
    ### 返回:
    - 作品列表

    # [English]
    ### Purpose:
    - Get topic post list
    ### Parameters:
    - category: Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info`
    - max_behot_time: Pagination parameter, can be obtained from the return result of the last request.
    It is empty for the first request, and the max_behot_time returned by the last request is used for
    subsequent requests.
    - category_parameter: Category parameter ID, can be obtained from the interface
    `/lemon8/app/fetch_topic_info`
    - hashtag_name: Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info`
    - sort_type: Sort type, 0 for default sort, currently only support default sort, please do not pass
    other values.
    ### Return:
    - Post list

    # [示例/Example]
    category = \"590\"
    max_behot_time = \"\"
    category_parameter = \"7174447913778593798\"
    hashtag_name = \"lemon8christmas\"
    sort_type = \"0\"

    Args:
        category (str): 话题分类 ID/Topic category ID
        max_behot_time (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.
        category_parameter (str): 分类参数/Category parameter
        hashtag_name (str): Hashtag名称/Hashtag name
        sort_type (Union[Unset, str]): 排序方式/Sort type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        category=category,
        max_behot_time=max_behot_time,
        category_parameter=category_parameter,
        hashtag_name=hashtag_name,
        sort_type=sort_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    category: str,
    max_behot_time: Union[Unset, str] = "",
    category_parameter: str,
    hashtag_name: str,
    sort_type: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题作品列表/Get topic post list

     # [中文]
    ### 用途:
    - 获取话题作品列表
    ### 参数:
    - category: 话题分类 ID，可以从接口`/lemon8/app/fetch_topic_info`获取
    - max_behot_time: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的max_behot_time进行翻页。
    - category_parameter: 分类参数ID，可以从接口`/lemon8/app/fetch_topic_info`获取
    - hashtag_name: Hashtag名称，可以从接口`/lemon8/app/fetch_topic_info`获取
    - sort_type: 排序方式，0为默认排序，当前只支持使用默认排序，请不要传入其他值。
    ### 返回:
    - 作品列表

    # [English]
    ### Purpose:
    - Get topic post list
    ### Parameters:
    - category: Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info`
    - max_behot_time: Pagination parameter, can be obtained from the return result of the last request.
    It is empty for the first request, and the max_behot_time returned by the last request is used for
    subsequent requests.
    - category_parameter: Category parameter ID, can be obtained from the interface
    `/lemon8/app/fetch_topic_info`
    - hashtag_name: Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info`
    - sort_type: Sort type, 0 for default sort, currently only support default sort, please do not pass
    other values.
    ### Return:
    - Post list

    # [示例/Example]
    category = \"590\"
    max_behot_time = \"\"
    category_parameter = \"7174447913778593798\"
    hashtag_name = \"lemon8christmas\"
    sort_type = \"0\"

    Args:
        category (str): 话题分类 ID/Topic category ID
        max_behot_time (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.
        category_parameter (str): 分类参数/Category parameter
        hashtag_name (str): Hashtag名称/Hashtag name
        sort_type (Union[Unset, str]): 排序方式/Sort type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        category=category,
        max_behot_time=max_behot_time,
        category_parameter=category_parameter,
        hashtag_name=hashtag_name,
        sort_type=sort_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category: str,
    max_behot_time: Union[Unset, str] = "",
    category_parameter: str,
    hashtag_name: str,
    sort_type: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题作品列表/Get topic post list

     # [中文]
    ### 用途:
    - 获取话题作品列表
    ### 参数:
    - category: 话题分类 ID，可以从接口`/lemon8/app/fetch_topic_info`获取
    - max_behot_time: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的max_behot_time进行翻页。
    - category_parameter: 分类参数ID，可以从接口`/lemon8/app/fetch_topic_info`获取
    - hashtag_name: Hashtag名称，可以从接口`/lemon8/app/fetch_topic_info`获取
    - sort_type: 排序方式，0为默认排序，当前只支持使用默认排序，请不要传入其他值。
    ### 返回:
    - 作品列表

    # [English]
    ### Purpose:
    - Get topic post list
    ### Parameters:
    - category: Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info`
    - max_behot_time: Pagination parameter, can be obtained from the return result of the last request.
    It is empty for the first request, and the max_behot_time returned by the last request is used for
    subsequent requests.
    - category_parameter: Category parameter ID, can be obtained from the interface
    `/lemon8/app/fetch_topic_info`
    - hashtag_name: Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info`
    - sort_type: Sort type, 0 for default sort, currently only support default sort, please do not pass
    other values.
    ### Return:
    - Post list

    # [示例/Example]
    category = \"590\"
    max_behot_time = \"\"
    category_parameter = \"7174447913778593798\"
    hashtag_name = \"lemon8christmas\"
    sort_type = \"0\"

    Args:
        category (str): 话题分类 ID/Topic category ID
        max_behot_time (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.
        category_parameter (str): 分类参数/Category parameter
        hashtag_name (str): Hashtag名称/Hashtag name
        sort_type (Union[Unset, str]): 排序方式/Sort type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        category=category,
        max_behot_time=max_behot_time,
        category_parameter=category_parameter,
        hashtag_name=hashtag_name,
        sort_type=sort_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category: str,
    max_behot_time: Union[Unset, str] = "",
    category_parameter: str,
    hashtag_name: str,
    sort_type: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题作品列表/Get topic post list

     # [中文]
    ### 用途:
    - 获取话题作品列表
    ### 参数:
    - category: 话题分类 ID，可以从接口`/lemon8/app/fetch_topic_info`获取
    - max_behot_time: 翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的max_behot_time进行翻页。
    - category_parameter: 分类参数ID，可以从接口`/lemon8/app/fetch_topic_info`获取
    - hashtag_name: Hashtag名称，可以从接口`/lemon8/app/fetch_topic_info`获取
    - sort_type: 排序方式，0为默认排序，当前只支持使用默认排序，请不要传入其他值。
    ### 返回:
    - 作品列表

    # [English]
    ### Purpose:
    - Get topic post list
    ### Parameters:
    - category: Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info`
    - max_behot_time: Pagination parameter, can be obtained from the return result of the last request.
    It is empty for the first request, and the max_behot_time returned by the last request is used for
    subsequent requests.
    - category_parameter: Category parameter ID, can be obtained from the interface
    `/lemon8/app/fetch_topic_info`
    - hashtag_name: Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info`
    - sort_type: Sort type, 0 for default sort, currently only support default sort, please do not pass
    other values.
    ### Return:
    - Post list

    # [示例/Example]
    category = \"590\"
    max_behot_time = \"\"
    category_parameter = \"7174447913778593798\"
    hashtag_name = \"lemon8christmas\"
    sort_type = \"0\"

    Args:
        category (str): 话题分类 ID/Topic category ID
        max_behot_time (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.
        category_parameter (str): 分类参数/Category parameter
        hashtag_name (str): Hashtag名称/Hashtag name
        sort_type (Union[Unset, str]): 排序方式/Sort type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            max_behot_time=max_behot_time,
            category_parameter=category_parameter,
            hashtag_name=hashtag_name,
            sort_type=sort_type,
        )
    ).parsed
