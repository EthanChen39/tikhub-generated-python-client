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
    aweme_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aweme_id"] = aweme_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/open_douyin_app_to_video_detail",
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
    aweme_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified
    video details page

     # [中文]
    ### 用途:
    - 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页。

    ### 参数:
    - aweme_id: 作品id

    ### 返回:
    - 分享链接

    # [English]
    ### Purpose:
    - Generate Douyin share link, call Douyin APP, and jump to the specified video

    ### Parameters:
    - aweme_id: Video id

    ### Return:
    - Share link

    # [示例/Example]
    aweme_id = \"7197598285882789120\"

    Args:
        aweme_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_id=aweme_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified
    video details page

     # [中文]
    ### 用途:
    - 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页。

    ### 参数:
    - aweme_id: 作品id

    ### 返回:
    - 分享链接

    # [English]
    ### Purpose:
    - Generate Douyin share link, call Douyin APP, and jump to the specified video

    ### Parameters:
    - aweme_id: Video id

    ### Return:
    - Share link

    # [示例/Example]
    aweme_id = \"7197598285882789120\"

    Args:
        aweme_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        aweme_id=aweme_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified
    video details page

     # [中文]
    ### 用途:
    - 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页。

    ### 参数:
    - aweme_id: 作品id

    ### 返回:
    - 分享链接

    # [English]
    ### Purpose:
    - Generate Douyin share link, call Douyin APP, and jump to the specified video

    ### Parameters:
    - aweme_id: Video id

    ### Return:
    - Share link

    # [示例/Example]
    aweme_id = \"7197598285882789120\"

    Args:
        aweme_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_id=aweme_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified
    video details page

     # [中文]
    ### 用途:
    - 生成抖音分享链接，唤起抖音APP，跳转指定作品详情页。

    ### 参数:
    - aweme_id: 作品id

    ### 返回:
    - 分享链接

    # [English]
    ### Purpose:
    - Generate Douyin share link, call Douyin APP, and jump to the specified video

    ### Parameters:
    - aweme_id: Video id

    ### Return:
    - Share link

    # [示例/Example]
    aweme_id = \"7197598285882789120\"

    Args:
        aweme_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            aweme_id=aweme_id,
        )
    ).parsed
