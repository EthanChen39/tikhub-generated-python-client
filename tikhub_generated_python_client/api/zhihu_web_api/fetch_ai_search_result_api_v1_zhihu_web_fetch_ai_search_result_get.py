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
    message_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["message_id"] = message_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/zhihu/web/fetch_ai_search_result",
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
    message_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎AI搜索结果/Get Zhihu AI Search Result

     # [中文]
    ### 用途:
    - 获取知乎AI搜索结果
    ### 参数:
    - message_id: 消息ID
    ### 返回:
    - 知乎AI搜索结果

    # [English]
    ### Purpose:
    - Get Zhihu AI Search Result
    ### Parameters:
    - message_id: Message ID
    ### Returns:
    - Zhihu AI Search Result

    # [示例/Example]
    message_id = \"5f8b4f4a-0b7c-4d1b-8c4f-2e5c0d6c1b9d\"

    Args:
        message_id (str): 消息ID/Message ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    message_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎AI搜索结果/Get Zhihu AI Search Result

     # [中文]
    ### 用途:
    - 获取知乎AI搜索结果
    ### 参数:
    - message_id: 消息ID
    ### 返回:
    - 知乎AI搜索结果

    # [English]
    ### Purpose:
    - Get Zhihu AI Search Result
    ### Parameters:
    - message_id: Message ID
    ### Returns:
    - Zhihu AI Search Result

    # [示例/Example]
    message_id = \"5f8b4f4a-0b7c-4d1b-8c4f-2e5c0d6c1b9d\"

    Args:
        message_id (str): 消息ID/Message ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        message_id=message_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    message_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎AI搜索结果/Get Zhihu AI Search Result

     # [中文]
    ### 用途:
    - 获取知乎AI搜索结果
    ### 参数:
    - message_id: 消息ID
    ### 返回:
    - 知乎AI搜索结果

    # [English]
    ### Purpose:
    - Get Zhihu AI Search Result
    ### Parameters:
    - message_id: Message ID
    ### Returns:
    - Zhihu AI Search Result

    # [示例/Example]
    message_id = \"5f8b4f4a-0b7c-4d1b-8c4f-2e5c0d6c1b9d\"

    Args:
        message_id (str): 消息ID/Message ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    message_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎AI搜索结果/Get Zhihu AI Search Result

     # [中文]
    ### 用途:
    - 获取知乎AI搜索结果
    ### 参数:
    - message_id: 消息ID
    ### 返回:
    - 知乎AI搜索结果

    # [English]
    ### Purpose:
    - Get Zhihu AI Search Result
    ### Parameters:
    - message_id: Message ID
    ### Returns:
    - Zhihu AI Search Result

    # [示例/Example]
    message_id = \"5f8b4f4a-0b7c-4d1b-8c4f-2e5c0d6c1b9d\"

    Args:
        message_id (str): 消息ID/Message ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            message_id=message_id,
        )
    ).parsed
