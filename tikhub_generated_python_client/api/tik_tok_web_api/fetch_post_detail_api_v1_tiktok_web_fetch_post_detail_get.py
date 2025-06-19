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
    item_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["itemId"] = item_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_post_detail",
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
    item_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据
    - 此接口无法用于视频下载，只能获取视频数据，访问此接口返回的视频链接会返回HTTP403报错。
    - 如果有视频下载需求，请使用 /api/v1/tiktok/app/v2/fetch_one_video 接口。
    ### 参数:
    - itemId: 作品id
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data
    - This interface cannot be used for video download, it can only get video data, and accessing the
    video link returned by this interface will return an HTTP403 error.
    - If you need to download videos, please use the /api/v1/tiktok/app/v2/fetch_one_video interface.
    ### Parameters:
    - itemId: Video id
    ### Return:
    - Video data

    # [示例/Example]
    itemId = \"7339393672959757570\"

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据
    - 此接口无法用于视频下载，只能获取视频数据，访问此接口返回的视频链接会返回HTTP403报错。
    - 如果有视频下载需求，请使用 /api/v1/tiktok/app/v2/fetch_one_video 接口。
    ### 参数:
    - itemId: 作品id
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data
    - This interface cannot be used for video download, it can only get video data, and accessing the
    video link returned by this interface will return an HTTP403 error.
    - If you need to download videos, please use the /api/v1/tiktok/app/v2/fetch_one_video interface.
    ### Parameters:
    - itemId: Video id
    ### Return:
    - Video data

    # [示例/Example]
    itemId = \"7339393672959757570\"

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        item_id=item_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据
    - 此接口无法用于视频下载，只能获取视频数据，访问此接口返回的视频链接会返回HTTP403报错。
    - 如果有视频下载需求，请使用 /api/v1/tiktok/app/v2/fetch_one_video 接口。
    ### 参数:
    - itemId: 作品id
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data
    - This interface cannot be used for video download, it can only get video data, and accessing the
    video link returned by this interface will return an HTTP403 error.
    - If you need to download videos, please use the /api/v1/tiktok/app/v2/fetch_one_video interface.
    ### Parameters:
    - itemId: Video id
    ### Return:
    - Video data

    # [示例/Example]
    itemId = \"7339393672959757570\"

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据
    - 此接口无法用于视频下载，只能获取视频数据，访问此接口返回的视频链接会返回HTTP403报错。
    - 如果有视频下载需求，请使用 /api/v1/tiktok/app/v2/fetch_one_video 接口。
    ### 参数:
    - itemId: 作品id
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data
    - This interface cannot be used for video download, it can only get video data, and accessing the
    video link returned by this interface will return an HTTP403 error.
    - If you need to download videos, please use the /api/v1/tiktok/app/v2/fetch_one_video interface.
    ### Parameters:
    - itemId: Video id
    ### Return:
    - Video data

    # [示例/Example]
    itemId = \"7339393672959757570\"

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            item_id=item_id,
        )
    ).parsed
