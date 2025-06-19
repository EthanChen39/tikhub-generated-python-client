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
    share_url: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["share_url"] = share_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_one_video_by_share_url",
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
    share_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据分享链接获取单个作品数据/Get single video data by sharing link

     # [中文]
    ### 用途:
    - 根据分享链接获取单个作品数据 （本质上基于 `/fetch_one_video` 接口实现，建议有能力自行获取视频ID以提升接口响应速度）
    - 返回的视频画质比APP接口高一些，但是响应字段没有APP接口多。
    ### 参数:
    - share_url: 分享链接
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data by sharing link (Essentially implemented based on the `/fetch_one_video`
    interface, it is recommended to obtain the video ID by yourself to improve the interface response
    speed)
    - The returned video quality is higher than the APP interface, but the response fields are not as
    many as the APP interface.
    ### Parameters:
    - share_url: Share link
    ### Return:
    - Video data

    # [示例/Example]
    share_url = \"https://v.douyin.com/e3x2fjE/\"

    Args:
        share_url (str): 分享链接/Share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        share_url=share_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    share_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据分享链接获取单个作品数据/Get single video data by sharing link

     # [中文]
    ### 用途:
    - 根据分享链接获取单个作品数据 （本质上基于 `/fetch_one_video` 接口实现，建议有能力自行获取视频ID以提升接口响应速度）
    - 返回的视频画质比APP接口高一些，但是响应字段没有APP接口多。
    ### 参数:
    - share_url: 分享链接
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data by sharing link (Essentially implemented based on the `/fetch_one_video`
    interface, it is recommended to obtain the video ID by yourself to improve the interface response
    speed)
    - The returned video quality is higher than the APP interface, but the response fields are not as
    many as the APP interface.
    ### Parameters:
    - share_url: Share link
    ### Return:
    - Video data

    # [示例/Example]
    share_url = \"https://v.douyin.com/e3x2fjE/\"

    Args:
        share_url (str): 分享链接/Share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        share_url=share_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    share_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据分享链接获取单个作品数据/Get single video data by sharing link

     # [中文]
    ### 用途:
    - 根据分享链接获取单个作品数据 （本质上基于 `/fetch_one_video` 接口实现，建议有能力自行获取视频ID以提升接口响应速度）
    - 返回的视频画质比APP接口高一些，但是响应字段没有APP接口多。
    ### 参数:
    - share_url: 分享链接
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data by sharing link (Essentially implemented based on the `/fetch_one_video`
    interface, it is recommended to obtain the video ID by yourself to improve the interface response
    speed)
    - The returned video quality is higher than the APP interface, but the response fields are not as
    many as the APP interface.
    ### Parameters:
    - share_url: Share link
    ### Return:
    - Video data

    # [示例/Example]
    share_url = \"https://v.douyin.com/e3x2fjE/\"

    Args:
        share_url (str): 分享链接/Share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        share_url=share_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    share_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据分享链接获取单个作品数据/Get single video data by sharing link

     # [中文]
    ### 用途:
    - 根据分享链接获取单个作品数据 （本质上基于 `/fetch_one_video` 接口实现，建议有能力自行获取视频ID以提升接口响应速度）
    - 返回的视频画质比APP接口高一些，但是响应字段没有APP接口多。
    ### 参数:
    - share_url: 分享链接
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data by sharing link (Essentially implemented based on the `/fetch_one_video`
    interface, it is recommended to obtain the video ID by yourself to improve the interface response
    speed)
    - The returned video quality is higher than the APP interface, but the response fields are not as
    many as the APP interface.
    ### Parameters:
    - share_url: Share link
    ### Return:
    - Video data

    # [示例/Example]
    share_url = \"https://v.douyin.com/e3x2fjE/\"

    Args:
        share_url (str): 分享链接/Share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            share_url=share_url,
        )
    ).parsed
