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
    related_live_tag: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["related_live_tag"] = related_live_tag

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_live_recommend",
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
    related_live_tag: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播间首页推荐列表/Get live room homepage recommendation list

     # [中文]
    ### 用途:
    - 获取直播间首页推荐列表
    ### 参数:
    - related_live_tag: 相关直播标签
    ### 返回:
    - 直播间首页推荐列表

    # [English]
    ### Purpose:
    - Get live room homepage recommendation list
    ### Parameters:
    - related_live_tag: Related live tag
    ### Return:
    - Live room homepage recommendation list

    # [示例/Example]
    related_live_tag = \"VALORANT\"

    Args:
        related_live_tag (str): 相关直播标签/Related live tag

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        related_live_tag=related_live_tag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    related_live_tag: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播间首页推荐列表/Get live room homepage recommendation list

     # [中文]
    ### 用途:
    - 获取直播间首页推荐列表
    ### 参数:
    - related_live_tag: 相关直播标签
    ### 返回:
    - 直播间首页推荐列表

    # [English]
    ### Purpose:
    - Get live room homepage recommendation list
    ### Parameters:
    - related_live_tag: Related live tag
    ### Return:
    - Live room homepage recommendation list

    # [示例/Example]
    related_live_tag = \"VALORANT\"

    Args:
        related_live_tag (str): 相关直播标签/Related live tag

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        related_live_tag=related_live_tag,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    related_live_tag: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播间首页推荐列表/Get live room homepage recommendation list

     # [中文]
    ### 用途:
    - 获取直播间首页推荐列表
    ### 参数:
    - related_live_tag: 相关直播标签
    ### 返回:
    - 直播间首页推荐列表

    # [English]
    ### Purpose:
    - Get live room homepage recommendation list
    ### Parameters:
    - related_live_tag: Related live tag
    ### Return:
    - Live room homepage recommendation list

    # [示例/Example]
    related_live_tag = \"VALORANT\"

    Args:
        related_live_tag (str): 相关直播标签/Related live tag

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        related_live_tag=related_live_tag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    related_live_tag: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播间首页推荐列表/Get live room homepage recommendation list

     # [中文]
    ### 用途:
    - 获取直播间首页推荐列表
    ### 参数:
    - related_live_tag: 相关直播标签
    ### 返回:
    - 直播间首页推荐列表

    # [English]
    ### Purpose:
    - Get live room homepage recommendation list
    ### Parameters:
    - related_live_tag: Related live tag
    ### Return:
    - Live room homepage recommendation list

    # [示例/Example]
    related_live_tag = \"VALORANT\"

    Args:
        related_live_tag (str): 相关直播标签/Related live tag

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            related_live_tag=related_live_tag,
        )
    ).parsed
