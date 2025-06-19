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
    location_id: str,
    pagination_token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["location_id"] = location_id

    params["pagination_token"] = pagination_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/instagram/web_app/fetch_location_posts_by_location_id_v2",
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
    location_id: str,
    pagination_token: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据地点ID获取地点相关的帖子V2/Get location posts by location ID V2

     # [中文]
    ### 用途:
    - 根据Instagram地点ID获取地点相关的帖子V2
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - location_id: Instagram地点ID
    - pagination_token: 分页token，第一次请求不需要传值，后续页需要传入上一页的返回值。
    ### 返回:
    - 地点相关的帖子数据

    # [English]
    ### Purpose:
    - Get location posts by Instagram location ID V2
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - location_id: Instagram location ID
    - pagination_token: Pagination token, no need to pass value for the first request, pass the return
    value of the previous page for subsequent pages.
    ### Return:
    - Location posts data

    # [示例/Example]
    location_id = \"115412053922647\"
    pagination_token = None

    Args:
        location_id (str): Instagram地点ID/Instagram location ID
        pagination_token (Union[Unset, str]): 分页token/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        pagination_token=pagination_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    location_id: str,
    pagination_token: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据地点ID获取地点相关的帖子V2/Get location posts by location ID V2

     # [中文]
    ### 用途:
    - 根据Instagram地点ID获取地点相关的帖子V2
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - location_id: Instagram地点ID
    - pagination_token: 分页token，第一次请求不需要传值，后续页需要传入上一页的返回值。
    ### 返回:
    - 地点相关的帖子数据

    # [English]
    ### Purpose:
    - Get location posts by Instagram location ID V2
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - location_id: Instagram location ID
    - pagination_token: Pagination token, no need to pass value for the first request, pass the return
    value of the previous page for subsequent pages.
    ### Return:
    - Location posts data

    # [示例/Example]
    location_id = \"115412053922647\"
    pagination_token = None

    Args:
        location_id (str): Instagram地点ID/Instagram location ID
        pagination_token (Union[Unset, str]): 分页token/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        location_id=location_id,
        pagination_token=pagination_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    location_id: str,
    pagination_token: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据地点ID获取地点相关的帖子V2/Get location posts by location ID V2

     # [中文]
    ### 用途:
    - 根据Instagram地点ID获取地点相关的帖子V2
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - location_id: Instagram地点ID
    - pagination_token: 分页token，第一次请求不需要传值，后续页需要传入上一页的返回值。
    ### 返回:
    - 地点相关的帖子数据

    # [English]
    ### Purpose:
    - Get location posts by Instagram location ID V2
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - location_id: Instagram location ID
    - pagination_token: Pagination token, no need to pass value for the first request, pass the return
    value of the previous page for subsequent pages.
    ### Return:
    - Location posts data

    # [示例/Example]
    location_id = \"115412053922647\"
    pagination_token = None

    Args:
        location_id (str): Instagram地点ID/Instagram location ID
        pagination_token (Union[Unset, str]): 分页token/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        pagination_token=pagination_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    location_id: str,
    pagination_token: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据地点ID获取地点相关的帖子V2/Get location posts by location ID V2

     # [中文]
    ### 用途:
    - 根据Instagram地点ID获取地点相关的帖子V2
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - location_id: Instagram地点ID
    - pagination_token: 分页token，第一次请求不需要传值，后续页需要传入上一页的返回值。
    ### 返回:
    - 地点相关的帖子数据

    # [English]
    ### Purpose:
    - Get location posts by Instagram location ID V2
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - location_id: Instagram location ID
    - pagination_token: Pagination token, no need to pass value for the first request, pass the return
    value of the previous page for subsequent pages.
    ### Return:
    - Location posts data

    # [示例/Example]
    location_id = \"115412053922647\"
    pagination_token = None

    Args:
        location_id (str): Instagram地点ID/Instagram location ID
        pagination_token (Union[Unset, str]): 分页token/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            location_id=location_id,
            pagination_token=pagination_token,
        )
    ).parsed
