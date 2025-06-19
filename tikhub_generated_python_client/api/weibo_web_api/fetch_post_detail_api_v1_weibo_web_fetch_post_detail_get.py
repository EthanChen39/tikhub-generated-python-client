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
    id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/weibo/web/fetch_post_detail",
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
    id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据
    ### 参数:
    - id: 作品id，从分享链接中获取
     - https://weibo.com/5819018196/5092682368025584
     - 作品id为：5092682368025584
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data
    ### Parameters:
    - id: Post id, obtained from the sharing link
        - https://weibo.com/5819018196/5092682368025584
        - The post id is: 5092682368025584
    ### Return:
    - Post data

    # [示例/Example]
    id = \"5092682368025584\"

    Args:
        id (str): 作品id/Post id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据
    ### 参数:
    - id: 作品id，从分享链接中获取
     - https://weibo.com/5819018196/5092682368025584
     - 作品id为：5092682368025584
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data
    ### Parameters:
    - id: Post id, obtained from the sharing link
        - https://weibo.com/5819018196/5092682368025584
        - The post id is: 5092682368025584
    ### Return:
    - Post data

    # [示例/Example]
    id = \"5092682368025584\"

    Args:
        id (str): 作品id/Post id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据
    ### 参数:
    - id: 作品id，从分享链接中获取
     - https://weibo.com/5819018196/5092682368025584
     - 作品id为：5092682368025584
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data
    ### Parameters:
    - id: Post id, obtained from the sharing link
        - https://weibo.com/5819018196/5092682368025584
        - The post id is: 5092682368025584
    ### Return:
    - Post data

    # [示例/Example]
    id = \"5092682368025584\"

    Args:
        id (str): 作品id/Post id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据/Get single video data

     # [中文]
    ### 用途:
    - 获取单个作品数据
    ### 参数:
    - id: 作品id，从分享链接中获取
     - https://weibo.com/5819018196/5092682368025584
     - 作品id为：5092682368025584
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data
    ### Parameters:
    - id: Post id, obtained from the sharing link
        - https://weibo.com/5819018196/5092682368025584
        - The post id is: 5092682368025584
    ### Return:
    - Post data

    # [示例/Example]
    id = \"5092682368025584\"

    Args:
        id (str): 作品id/Post id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
