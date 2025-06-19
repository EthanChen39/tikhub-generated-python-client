from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/web/fetch_query_user",
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""查询抖音用户基本信息/Query Douyin user basic information

     # [中文]
    ### 用途:
    - 查询抖音用户基本信息
    ### 参数:
    - cookie: 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。
    ### 返回:
    - 用户基本信息

    # [English]
    ### Purpose:
    - Query Douyin user basic information
    ### Parameters:
    - cookie: User ttwid Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface
    to get.
    ### Return:
    - User basic information

    # [示例/Example]
    cookie = \"ttwid=xxx;\"

    Args:
        body (str): 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。/User ttwid
            Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface to get.
            Default: 'ttwid=1%7CNBG4pKnnBr32xpXszWA57PAooMT-
            02MTYJCyYl0fayI%7C1746172842%7Ce2aa988d355d220eb2fe8fb7e7bb22a51a46a933f969f768c5315fa73e3
            72d5f;'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""查询抖音用户基本信息/Query Douyin user basic information

     # [中文]
    ### 用途:
    - 查询抖音用户基本信息
    ### 参数:
    - cookie: 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。
    ### 返回:
    - 用户基本信息

    # [English]
    ### Purpose:
    - Query Douyin user basic information
    ### Parameters:
    - cookie: User ttwid Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface
    to get.
    ### Return:
    - User basic information

    # [示例/Example]
    cookie = \"ttwid=xxx;\"

    Args:
        body (str): 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。/User ttwid
            Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface to get.
            Default: 'ttwid=1%7CNBG4pKnnBr32xpXszWA57PAooMT-
            02MTYJCyYl0fayI%7C1746172842%7Ce2aa988d355d220eb2fe8fb7e7bb22a51a46a933f969f768c5315fa73e3
            72d5f;'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""查询抖音用户基本信息/Query Douyin user basic information

     # [中文]
    ### 用途:
    - 查询抖音用户基本信息
    ### 参数:
    - cookie: 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。
    ### 返回:
    - 用户基本信息

    # [English]
    ### Purpose:
    - Query Douyin user basic information
    ### Parameters:
    - cookie: User ttwid Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface
    to get.
    ### Return:
    - User basic information

    # [示例/Example]
    cookie = \"ttwid=xxx;\"

    Args:
        body (str): 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。/User ttwid
            Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface to get.
            Default: 'ttwid=1%7CNBG4pKnnBr32xpXszWA57PAooMT-
            02MTYJCyYl0fayI%7C1746172842%7Ce2aa988d355d220eb2fe8fb7e7bb22a51a46a933f969f768c5315fa73e3
            72d5f;'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""查询抖音用户基本信息/Query Douyin user basic information

     # [中文]
    ### 用途:
    - 查询抖音用户基本信息
    ### 参数:
    - cookie: 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。
    ### 返回:
    - 用户基本信息

    # [English]
    ### Purpose:
    - Query Douyin user basic information
    ### Parameters:
    - cookie: User ttwid Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface
    to get.
    ### Return:
    - User basic information

    # [示例/Example]
    cookie = \"ttwid=xxx;\"

    Args:
        body (str): 用户ttwid Cookie，获取方式：调用`/api/v1/douyin/web/generate_ttwid`接口获取。/User ttwid
            Cookie, acquisition method: call `/api/v1/douyin/web/generate_ttwid` interface to get.
            Default: 'ttwid=1%7CNBG4pKnnBr32xpXszWA57PAooMT-
            02MTYJCyYl0fayI%7C1746172842%7Ce2aa988d355d220eb2fe8fb7e7bb22a51a46a933f969f768c5315fa73e3
            72d5f;'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
