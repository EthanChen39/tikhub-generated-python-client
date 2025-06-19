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
    message_content: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["message_content"] = message_content

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/zhihu/web/fetch_ai_search",
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
    message_content: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎AI搜索/Get Zhihu AI Search

     # [中文]
    ### 用途:
    - 获取知乎AI搜索
    ### 参数:
    - message_content: 搜索内容
    ### 返回:
    - 知乎AI搜索消息ID，用于请求搜索结果

    # [English]
    ### Purpose:
    - Get Zhihu AI Search
    ### Parameters:
    - message_content: Search Content
    ### Returns:
    - Zhihu AI Search Message ID for requesting search results

    # [示例/Example]
    message_content = \"deepseek\"

    Args:
        message_content (str): 搜索内容/Search Content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        message_content=message_content,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    message_content: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎AI搜索/Get Zhihu AI Search

     # [中文]
    ### 用途:
    - 获取知乎AI搜索
    ### 参数:
    - message_content: 搜索内容
    ### 返回:
    - 知乎AI搜索消息ID，用于请求搜索结果

    # [English]
    ### Purpose:
    - Get Zhihu AI Search
    ### Parameters:
    - message_content: Search Content
    ### Returns:
    - Zhihu AI Search Message ID for requesting search results

    # [示例/Example]
    message_content = \"deepseek\"

    Args:
        message_content (str): 搜索内容/Search Content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        message_content=message_content,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    message_content: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎AI搜索/Get Zhihu AI Search

     # [中文]
    ### 用途:
    - 获取知乎AI搜索
    ### 参数:
    - message_content: 搜索内容
    ### 返回:
    - 知乎AI搜索消息ID，用于请求搜索结果

    # [English]
    ### Purpose:
    - Get Zhihu AI Search
    ### Parameters:
    - message_content: Search Content
    ### Returns:
    - Zhihu AI Search Message ID for requesting search results

    # [示例/Example]
    message_content = \"deepseek\"

    Args:
        message_content (str): 搜索内容/Search Content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        message_content=message_content,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    message_content: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎AI搜索/Get Zhihu AI Search

     # [中文]
    ### 用途:
    - 获取知乎AI搜索
    ### 参数:
    - message_content: 搜索内容
    ### 返回:
    - 知乎AI搜索消息ID，用于请求搜索结果

    # [English]
    ### Purpose:
    - Get Zhihu AI Search
    ### Parameters:
    - message_content: Search Content
    ### Returns:
    - Zhihu AI Search Message ID for requesting search results

    # [示例/Example]
    message_content = \"deepseek\"

    Args:
        message_content (str): 搜索内容/Search Content

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            message_content=message_content,
        )
    ).parsed
