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
    keyword: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/instagram/web_app/fetch_search_hashtags_by_keyword_v2",
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
    keyword: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索话题V2/Search hashtags by keyword V2

     # [中文]
    ### 用途:
    - 搜索话题V2
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - keyword: 关键词
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search hashtags by query V2
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - keyword: Query
    ### Return:
    - Search result

    # [示例/Example]
    keyword = \"instagram\"

    Args:
        keyword (str): 关键词/Query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索话题V2/Search hashtags by keyword V2

     # [中文]
    ### 用途:
    - 搜索话题V2
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - keyword: 关键词
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search hashtags by query V2
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - keyword: Query
    ### Return:
    - Search result

    # [示例/Example]
    keyword = \"instagram\"

    Args:
        keyword (str): 关键词/Query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索话题V2/Search hashtags by keyword V2

     # [中文]
    ### 用途:
    - 搜索话题V2
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - keyword: 关键词
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search hashtags by query V2
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - keyword: Query
    ### Return:
    - Search result

    # [示例/Example]
    keyword = \"instagram\"

    Args:
        keyword (str): 关键词/Query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索话题V2/Search hashtags by keyword V2

     # [中文]
    ### 用途:
    - 搜索话题V2
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - keyword: 关键词
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search hashtags by query V2
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - keyword: Query
    ### Return:
    - Search result

    # [示例/Example]
    keyword = \"instagram\"

    Args:
        keyword (str): 关键词/Query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword=keyword,
        )
    ).parsed
