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
    sec_user_id: str,
    max_cursor: Union[Unset, str] = "0",
    count: Union[Unset, int] = 20,
    filter_type: Union[Unset, str] = "0",
    cookie: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sec_user_id"] = sec_user_id

    params["max_cursor"] = max_cursor

    params["count"] = count

    params["filter_type"] = filter_type

    params["cookie"] = cookie

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_user_post_videos",
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
    sec_user_id: str,
    max_cursor: Union[Unset, str] = "0",
    count: Union[Unset, int] = 20,
    filter_type: Union[Unset, str] = "0",
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户主页作品数据
    - 注意：请尽量使用APP的接口而不是WEB的接口，因为WEB的接口可能会被不稳定。
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - max_cursor: 翻页游标，第一次请求传0，然后每次请求传上一次请求返回的max_cursor进行翻页。
    - count: 最大数量，建议不要超过20
    - filter_type: 过滤类型，可选参数如下：
        - 0: 默认排序
        - 3: 热度排序
    - cookie: 用户网页版抖音Cookie(此接口可以接受用户提供自己的Cookie)
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user homepage video data
    - Note: Please try to use the APP interface instead of the WEB API, because the WEB API may be
    unstable.
    ### Parameters:
    - sec_user_id: User sec_user_id
    - max_cursor: Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by
    the previous request for paging each time.
    - count: Maximum count number, it is recommended not to exceed 20
    - filter_type: Filter type, optional parameters are as follows:
        - 0: Default sorting
        - 3: Sort by popularity
    - cookie: User's web version of Douyin Cookie (This interface can accept users to provide their own
    Cookie)
    ### Return:
    - User video data

    # [示例/Example]
    sec_user_id = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\"
    max_cursor = \"0\"
    counts = 20
    filter_type = \"0\"

    Args:
        sec_user_id (str): 用户sec_user_id/User sec_user_id
        max_cursor (Union[Unset, str]): 最大游标/Maximum cursor Default: '0'.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        filter_type (Union[Unset, str]): 过滤类型/Filter type Default: '0'.
        cookie (Union[Unset, str]): 用户网页版抖音Cookie/Your web version of Douyin Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_user_id=sec_user_id,
        max_cursor=max_cursor,
        count=count,
        filter_type=filter_type,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sec_user_id: str,
    max_cursor: Union[Unset, str] = "0",
    count: Union[Unset, int] = 20,
    filter_type: Union[Unset, str] = "0",
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户主页作品数据
    - 注意：请尽量使用APP的接口而不是WEB的接口，因为WEB的接口可能会被不稳定。
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - max_cursor: 翻页游标，第一次请求传0，然后每次请求传上一次请求返回的max_cursor进行翻页。
    - count: 最大数量，建议不要超过20
    - filter_type: 过滤类型，可选参数如下：
        - 0: 默认排序
        - 3: 热度排序
    - cookie: 用户网页版抖音Cookie(此接口可以接受用户提供自己的Cookie)
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user homepage video data
    - Note: Please try to use the APP interface instead of the WEB API, because the WEB API may be
    unstable.
    ### Parameters:
    - sec_user_id: User sec_user_id
    - max_cursor: Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by
    the previous request for paging each time.
    - count: Maximum count number, it is recommended not to exceed 20
    - filter_type: Filter type, optional parameters are as follows:
        - 0: Default sorting
        - 3: Sort by popularity
    - cookie: User's web version of Douyin Cookie (This interface can accept users to provide their own
    Cookie)
    ### Return:
    - User video data

    # [示例/Example]
    sec_user_id = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\"
    max_cursor = \"0\"
    counts = 20
    filter_type = \"0\"

    Args:
        sec_user_id (str): 用户sec_user_id/User sec_user_id
        max_cursor (Union[Unset, str]): 最大游标/Maximum cursor Default: '0'.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        filter_type (Union[Unset, str]): 过滤类型/Filter type Default: '0'.
        cookie (Union[Unset, str]): 用户网页版抖音Cookie/Your web version of Douyin Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        sec_user_id=sec_user_id,
        max_cursor=max_cursor,
        count=count,
        filter_type=filter_type,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sec_user_id: str,
    max_cursor: Union[Unset, str] = "0",
    count: Union[Unset, int] = 20,
    filter_type: Union[Unset, str] = "0",
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户主页作品数据
    - 注意：请尽量使用APP的接口而不是WEB的接口，因为WEB的接口可能会被不稳定。
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - max_cursor: 翻页游标，第一次请求传0，然后每次请求传上一次请求返回的max_cursor进行翻页。
    - count: 最大数量，建议不要超过20
    - filter_type: 过滤类型，可选参数如下：
        - 0: 默认排序
        - 3: 热度排序
    - cookie: 用户网页版抖音Cookie(此接口可以接受用户提供自己的Cookie)
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user homepage video data
    - Note: Please try to use the APP interface instead of the WEB API, because the WEB API may be
    unstable.
    ### Parameters:
    - sec_user_id: User sec_user_id
    - max_cursor: Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by
    the previous request for paging each time.
    - count: Maximum count number, it is recommended not to exceed 20
    - filter_type: Filter type, optional parameters are as follows:
        - 0: Default sorting
        - 3: Sort by popularity
    - cookie: User's web version of Douyin Cookie (This interface can accept users to provide their own
    Cookie)
    ### Return:
    - User video data

    # [示例/Example]
    sec_user_id = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\"
    max_cursor = \"0\"
    counts = 20
    filter_type = \"0\"

    Args:
        sec_user_id (str): 用户sec_user_id/User sec_user_id
        max_cursor (Union[Unset, str]): 最大游标/Maximum cursor Default: '0'.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        filter_type (Union[Unset, str]): 过滤类型/Filter type Default: '0'.
        cookie (Union[Unset, str]): 用户网页版抖音Cookie/Your web version of Douyin Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_user_id=sec_user_id,
        max_cursor=max_cursor,
        count=count,
        filter_type=filter_type,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sec_user_id: str,
    max_cursor: Union[Unset, str] = "0",
    count: Union[Unset, int] = 20,
    filter_type: Union[Unset, str] = "0",
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户主页作品数据
    - 注意：请尽量使用APP的接口而不是WEB的接口，因为WEB的接口可能会被不稳定。
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - max_cursor: 翻页游标，第一次请求传0，然后每次请求传上一次请求返回的max_cursor进行翻页。
    - count: 最大数量，建议不要超过20
    - filter_type: 过滤类型，可选参数如下：
        - 0: 默认排序
        - 3: 热度排序
    - cookie: 用户网页版抖音Cookie(此接口可以接受用户提供自己的Cookie)
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user homepage video data
    - Note: Please try to use the APP interface instead of the WEB API, because the WEB API may be
    unstable.
    ### Parameters:
    - sec_user_id: User sec_user_id
    - max_cursor: Paging cursor, pass 0 for the first request, and then pass the max_cursor returned by
    the previous request for paging each time.
    - count: Maximum count number, it is recommended not to exceed 20
    - filter_type: Filter type, optional parameters are as follows:
        - 0: Default sorting
        - 3: Sort by popularity
    - cookie: User's web version of Douyin Cookie (This interface can accept users to provide their own
    Cookie)
    ### Return:
    - User video data

    # [示例/Example]
    sec_user_id = \"MS4wLjABAAAANXSltcLCzDGmdNFI2Q_QixVTr67NiYzjKOIP5s03CAE\"
    max_cursor = \"0\"
    counts = 20
    filter_type = \"0\"

    Args:
        sec_user_id (str): 用户sec_user_id/User sec_user_id
        max_cursor (Union[Unset, str]): 最大游标/Maximum cursor Default: '0'.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        filter_type (Union[Unset, str]): 过滤类型/Filter type Default: '0'.
        cookie (Union[Unset, str]): 用户网页版抖音Cookie/Your web version of Douyin Cookie

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
            max_cursor=max_cursor,
            count=count,
            filter_type=filter_type,
            cookie=cookie,
        )
    ).parsed
