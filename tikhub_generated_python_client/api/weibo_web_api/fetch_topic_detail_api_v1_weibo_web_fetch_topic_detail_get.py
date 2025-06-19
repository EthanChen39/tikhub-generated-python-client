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
    topic_name: str,
    page: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["topic_name"] = topic_name

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/weibo/web/fetch_topic_detail",
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
    topic_name: str,
    page: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题详情/Get topic details

     # [中文]
    ### 用途:
    - 获取话题详情
    ### 参数:
    - topic_name: 话题名称
    - page: 页数
    ### 返回:
    - 话题详情

    # [English]
    ### Purpose:
    - Get topic details
    ### Parameters:
    - topic_name: Topic name
    - page: Page number
    ### Return:
    - Topic details

    # [示例/Example]
    topic_name = \"游戏\"
    page = \"\"

    Args:
        topic_name (str): 话题名称/Topic name
        page (Union[Unset, str]): 页数/Page number Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        topic_name=topic_name,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    topic_name: str,
    page: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题详情/Get topic details

     # [中文]
    ### 用途:
    - 获取话题详情
    ### 参数:
    - topic_name: 话题名称
    - page: 页数
    ### 返回:
    - 话题详情

    # [English]
    ### Purpose:
    - Get topic details
    ### Parameters:
    - topic_name: Topic name
    - page: Page number
    ### Return:
    - Topic details

    # [示例/Example]
    topic_name = \"游戏\"
    page = \"\"

    Args:
        topic_name (str): 话题名称/Topic name
        page (Union[Unset, str]): 页数/Page number Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        topic_name=topic_name,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    topic_name: str,
    page: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题详情/Get topic details

     # [中文]
    ### 用途:
    - 获取话题详情
    ### 参数:
    - topic_name: 话题名称
    - page: 页数
    ### 返回:
    - 话题详情

    # [English]
    ### Purpose:
    - Get topic details
    ### Parameters:
    - topic_name: Topic name
    - page: Page number
    ### Return:
    - Topic details

    # [示例/Example]
    topic_name = \"游戏\"
    page = \"\"

    Args:
        topic_name (str): 话题名称/Topic name
        page (Union[Unset, str]): 页数/Page number Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        topic_name=topic_name,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    topic_name: str,
    page: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题详情/Get topic details

     # [中文]
    ### 用途:
    - 获取话题详情
    ### 参数:
    - topic_name: 话题名称
    - page: 页数
    ### 返回:
    - 话题详情

    # [English]
    ### Purpose:
    - Get topic details
    ### Parameters:
    - topic_name: Topic name
    - page: Page number
    ### Return:
    - Topic details

    # [示例/Example]
    topic_name = \"游戏\"
    page = \"\"

    Args:
        topic_name (str): 话题名称/Topic name
        page (Union[Unset, str]): 页数/Page number Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            topic_name=topic_name,
            page=page,
        )
    ).parsed
