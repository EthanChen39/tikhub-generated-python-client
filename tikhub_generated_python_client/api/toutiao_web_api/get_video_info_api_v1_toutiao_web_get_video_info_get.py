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
        "url": "/api/v1/toutiao/web/get_video_info",
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
    r"""获取指定视频的信息/Get information of specified video

     # [中文]
    ### 用途:
    - 获取指定视频的信息
    ### 参数:
    - aweme_id: 作品ID，可以从链接中获取
        - 例如: https://www.toutiao.com/video/7431543350882206242/
    ### 返回:
    - 作品信息

    # [English]
    ### Purpose:
    - Get information of specified video
    ### Parameters:
    - item_id: Post ID, can be obtained from the link
        - For example: https://www.toutiao.com/video/7431543350882206242/
    ### Return:
    - Post information

    # [示例/Example]
    aweme_id = \"7431543350882206242\"

    Args:
        aweme_id (str): 作品ID/Post ID

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
    r"""获取指定视频的信息/Get information of specified video

     # [中文]
    ### 用途:
    - 获取指定视频的信息
    ### 参数:
    - aweme_id: 作品ID，可以从链接中获取
        - 例如: https://www.toutiao.com/video/7431543350882206242/
    ### 返回:
    - 作品信息

    # [English]
    ### Purpose:
    - Get information of specified video
    ### Parameters:
    - item_id: Post ID, can be obtained from the link
        - For example: https://www.toutiao.com/video/7431543350882206242/
    ### Return:
    - Post information

    # [示例/Example]
    aweme_id = \"7431543350882206242\"

    Args:
        aweme_id (str): 作品ID/Post ID

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
    r"""获取指定视频的信息/Get information of specified video

     # [中文]
    ### 用途:
    - 获取指定视频的信息
    ### 参数:
    - aweme_id: 作品ID，可以从链接中获取
        - 例如: https://www.toutiao.com/video/7431543350882206242/
    ### 返回:
    - 作品信息

    # [English]
    ### Purpose:
    - Get information of specified video
    ### Parameters:
    - item_id: Post ID, can be obtained from the link
        - For example: https://www.toutiao.com/video/7431543350882206242/
    ### Return:
    - Post information

    # [示例/Example]
    aweme_id = \"7431543350882206242\"

    Args:
        aweme_id (str): 作品ID/Post ID

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
    r"""获取指定视频的信息/Get information of specified video

     # [中文]
    ### 用途:
    - 获取指定视频的信息
    ### 参数:
    - aweme_id: 作品ID，可以从链接中获取
        - 例如: https://www.toutiao.com/video/7431543350882206242/
    ### 返回:
    - 作品信息

    # [English]
    ### Purpose:
    - Get information of specified video
    ### Parameters:
    - item_id: Post ID, can be obtained from the link
        - For example: https://www.toutiao.com/video/7431543350882206242/
    ### Return:
    - Post information

    # [示例/Example]
    aweme_id = \"7431543350882206242\"

    Args:
        aweme_id (str): 作品ID/Post ID

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
