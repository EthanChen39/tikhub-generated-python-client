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
    cell_id: str,
    cell_type: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cell_id"] = cell_id

    params["cell_type"] = cell_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pipixia/app/fetch_post_detail",
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
    cell_id: str,
    cell_type: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据，支持图文、视频等。
    ### 参数:
    - cell_id: 作品id，可以从分享链接中获取。
    - cell_type: 作品类型，1为视频，多大数保持默认值即可。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data, support photo, video, etc.
    ### Parameters:
    - cell_id: AKA video id, can be obtained from the share link.
    - cell_type: Video type, 1 for video, keep the default value for other types.
    ### Return:
    - Video data

    # [示例/Example]
    cell_id = \"7411193113223371043\"

    Args:
        cell_id (str): 作品id/Video id
        cell_type (Union[Unset, int]): 作品类型/Video type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        cell_id=cell_id,
        cell_type=cell_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cell_id: str,
    cell_type: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据，支持图文、视频等。
    ### 参数:
    - cell_id: 作品id，可以从分享链接中获取。
    - cell_type: 作品类型，1为视频，多大数保持默认值即可。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data, support photo, video, etc.
    ### Parameters:
    - cell_id: AKA video id, can be obtained from the share link.
    - cell_type: Video type, 1 for video, keep the default value for other types.
    ### Return:
    - Video data

    # [示例/Example]
    cell_id = \"7411193113223371043\"

    Args:
        cell_id (str): 作品id/Video id
        cell_type (Union[Unset, int]): 作品类型/Video type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        cell_id=cell_id,
        cell_type=cell_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cell_id: str,
    cell_type: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据，支持图文、视频等。
    ### 参数:
    - cell_id: 作品id，可以从分享链接中获取。
    - cell_type: 作品类型，1为视频，多大数保持默认值即可。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data, support photo, video, etc.
    ### Parameters:
    - cell_id: AKA video id, can be obtained from the share link.
    - cell_type: Video type, 1 for video, keep the default value for other types.
    ### Return:
    - Video data

    # [示例/Example]
    cell_id = \"7411193113223371043\"

    Args:
        cell_id (str): 作品id/Video id
        cell_type (Union[Unset, int]): 作品类型/Video type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        cell_id=cell_id,
        cell_type=cell_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cell_id: str,
    cell_type: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据，支持图文、视频等。
    ### 参数:
    - cell_id: 作品id，可以从分享链接中获取。
    - cell_type: 作品类型，1为视频，多大数保持默认值即可。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data, support photo, video, etc.
    ### Parameters:
    - cell_id: AKA video id, can be obtained from the share link.
    - cell_type: Video type, 1 for video, keep the default value for other types.
    ### Return:
    - Video data

    # [示例/Example]
    cell_id = \"7411193113223371043\"

    Args:
        cell_id (str): 作品id/Video id
        cell_type (Union[Unset, int]): 作品类型/Video type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            cell_id=cell_id,
            cell_type=cell_type,
        )
    ).parsed
