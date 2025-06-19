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
    photo_id: str,
    pcursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["photo_id"] = photo_id

    params["pcursor"] = pcursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/kuaishou/app/fetch_one_video_comment",
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
    photo_id: str,
    pcursor: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品评论数据/Get single video comment data

     # [中文]
    ### 用途:
    - 获取单个作品评论数据
    ### 参数:
    - photo_id: 作品ID
    - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
    ### 返回:
    - 评论数据

    # [English]
    ### Purpose:
    - Fetch single video comment data
    ### Parameters:
    - photo_id: Photo ID
    - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned
    response for subsequent requests.
    ### Returns:
    - Comments data

    # [示例/Example]
    photo_id = \"3x7gxp2zhgjv832\"
    pcursor = None

    Args:
        photo_id (str):
        pcursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        photo_id=photo_id,
        pcursor=pcursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    photo_id: str,
    pcursor: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品评论数据/Get single video comment data

     # [中文]
    ### 用途:
    - 获取单个作品评论数据
    ### 参数:
    - photo_id: 作品ID
    - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
    ### 返回:
    - 评论数据

    # [English]
    ### Purpose:
    - Fetch single video comment data
    ### Parameters:
    - photo_id: Photo ID
    - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned
    response for subsequent requests.
    ### Returns:
    - Comments data

    # [示例/Example]
    photo_id = \"3x7gxp2zhgjv832\"
    pcursor = None

    Args:
        photo_id (str):
        pcursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        photo_id=photo_id,
        pcursor=pcursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    photo_id: str,
    pcursor: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品评论数据/Get single video comment data

     # [中文]
    ### 用途:
    - 获取单个作品评论数据
    ### 参数:
    - photo_id: 作品ID
    - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
    ### 返回:
    - 评论数据

    # [English]
    ### Purpose:
    - Fetch single video comment data
    ### Parameters:
    - photo_id: Photo ID
    - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned
    response for subsequent requests.
    ### Returns:
    - Comments data

    # [示例/Example]
    photo_id = \"3x7gxp2zhgjv832\"
    pcursor = None

    Args:
        photo_id (str):
        pcursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        photo_id=photo_id,
        pcursor=pcursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    photo_id: str,
    pcursor: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品评论数据/Get single video comment data

     # [中文]
    ### 用途:
    - 获取单个作品评论数据
    ### 参数:
    - photo_id: 作品ID
    - pcursor: 评论游标，第一次请求为空，后续请求使用返回响应中的pcursor值进行翻页。
    ### 返回:
    - 评论数据

    # [English]
    ### Purpose:
    - Fetch single video comment data
    ### Parameters:
    - photo_id: Photo ID
    - pcursor: Comment cursor, empty for the first request, and use the pcursor value in the returned
    response for subsequent requests.
    ### Returns:
    - Comments data

    # [示例/Example]
    photo_id = \"3x7gxp2zhgjv832\"
    pcursor = None

    Args:
        photo_id (str):
        pcursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            photo_id=photo_id,
            pcursor=pcursor,
        )
    ).parsed
