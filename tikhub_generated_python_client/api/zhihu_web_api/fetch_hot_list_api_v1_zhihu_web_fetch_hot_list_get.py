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
    limit: Union[Unset, str] = "50",
    desktop: Union[Unset, str] = "true",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["desktop"] = desktop

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/zhihu/web/fetch_hot_list",
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
    limit: Union[Unset, str] = "50",
    desktop: Union[Unset, str] = "true",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎首页热榜/Get Zhihu Hot List

     # [中文]
    ### 用途:
    - 获取知乎首页热榜
    ### 参数:
    - limit: 每页文章数量
    - desktop: 是否为桌面端
    ### 返回:
    - 知乎首页热榜

    # [English]
    ### Purpose:
    - Get Zhihu Hot List
    ### Parameters:
    - limit: Number of articles per page
    - desktop: Is it a desktop
    ### Returns:
    - Zhihu Hot List

    # [示例/Example]
    limit = \"50\"
    desktop = \"true\"

    Args:
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '50'.
        desktop (Union[Unset, str]): 是否为桌面端/Is it a desktop Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        desktop=desktop,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, str] = "50",
    desktop: Union[Unset, str] = "true",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎首页热榜/Get Zhihu Hot List

     # [中文]
    ### 用途:
    - 获取知乎首页热榜
    ### 参数:
    - limit: 每页文章数量
    - desktop: 是否为桌面端
    ### 返回:
    - 知乎首页热榜

    # [English]
    ### Purpose:
    - Get Zhihu Hot List
    ### Parameters:
    - limit: Number of articles per page
    - desktop: Is it a desktop
    ### Returns:
    - Zhihu Hot List

    # [示例/Example]
    limit = \"50\"
    desktop = \"true\"

    Args:
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '50'.
        desktop (Union[Unset, str]): 是否为桌面端/Is it a desktop Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        desktop=desktop,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, str] = "50",
    desktop: Union[Unset, str] = "true",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎首页热榜/Get Zhihu Hot List

     # [中文]
    ### 用途:
    - 获取知乎首页热榜
    ### 参数:
    - limit: 每页文章数量
    - desktop: 是否为桌面端
    ### 返回:
    - 知乎首页热榜

    # [English]
    ### Purpose:
    - Get Zhihu Hot List
    ### Parameters:
    - limit: Number of articles per page
    - desktop: Is it a desktop
    ### Returns:
    - Zhihu Hot List

    # [示例/Example]
    limit = \"50\"
    desktop = \"true\"

    Args:
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '50'.
        desktop (Union[Unset, str]): 是否为桌面端/Is it a desktop Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        desktop=desktop,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, str] = "50",
    desktop: Union[Unset, str] = "true",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎首页热榜/Get Zhihu Hot List

     # [中文]
    ### 用途:
    - 获取知乎首页热榜
    ### 参数:
    - limit: 每页文章数量
    - desktop: 是否为桌面端
    ### 返回:
    - 知乎首页热榜

    # [English]
    ### Purpose:
    - Get Zhihu Hot List
    ### Parameters:
    - limit: Number of articles per page
    - desktop: Is it a desktop
    ### Returns:
    - Zhihu Hot List

    # [示例/Example]
    limit = \"50\"
    desktop = \"true\"

    Args:
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '50'.
        desktop (Union[Unset, str]): 是否为桌面端/Is it a desktop Default: 'true'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            desktop=desktop,
        )
    ).parsed
