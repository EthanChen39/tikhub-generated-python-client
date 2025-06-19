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
    keyword: str,
    platform_source: str,
    page: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["platformSource"] = platform_source

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/xingtu/search_kol_v1",
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
    keyword: str,
    platform_source: str,
    page: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""关键词搜索kol V1/Search Kol V1

     # [中文]
    ### 用途:
    - 关键词搜索kol V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - keyword: 关键词
    - platformSource:
        - 平台来源，支持以下参数:
        - _1 :抖音(douyin)
        - _2 :头条(toutiao)
        - _3 :西瓜(xigua)
    - page: 页码，从1开始
    ### 返回:
    - kol列表

    # [English]
    ### Purpose:
    - Search Kol V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - keyword: Keyword
    - platformSource:
        - Platform source, supports the following parameters:
        - _1 :Douyin
        - _2 :Toutiao
        - _3 :Xigua
    - page: Page number, starting from 1
    ### Return:
    - Kol List

    # [示例/Example]
    keyword = \"人工智能\"
    platformSource = \"_1\"
    page = 1

    Args:
        keyword (str): 关键词/Keyword
        platform_source (str): 平台来源/Platform Source
        page (int): 页码/Page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        platform_source=platform_source,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    platform_source: str,
    page: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""关键词搜索kol V1/Search Kol V1

     # [中文]
    ### 用途:
    - 关键词搜索kol V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - keyword: 关键词
    - platformSource:
        - 平台来源，支持以下参数:
        - _1 :抖音(douyin)
        - _2 :头条(toutiao)
        - _3 :西瓜(xigua)
    - page: 页码，从1开始
    ### 返回:
    - kol列表

    # [English]
    ### Purpose:
    - Search Kol V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - keyword: Keyword
    - platformSource:
        - Platform source, supports the following parameters:
        - _1 :Douyin
        - _2 :Toutiao
        - _3 :Xigua
    - page: Page number, starting from 1
    ### Return:
    - Kol List

    # [示例/Example]
    keyword = \"人工智能\"
    platformSource = \"_1\"
    page = 1

    Args:
        keyword (str): 关键词/Keyword
        platform_source (str): 平台来源/Platform Source
        page (int): 页码/Page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        platform_source=platform_source,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    platform_source: str,
    page: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""关键词搜索kol V1/Search Kol V1

     # [中文]
    ### 用途:
    - 关键词搜索kol V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - keyword: 关键词
    - platformSource:
        - 平台来源，支持以下参数:
        - _1 :抖音(douyin)
        - _2 :头条(toutiao)
        - _3 :西瓜(xigua)
    - page: 页码，从1开始
    ### 返回:
    - kol列表

    # [English]
    ### Purpose:
    - Search Kol V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - keyword: Keyword
    - platformSource:
        - Platform source, supports the following parameters:
        - _1 :Douyin
        - _2 :Toutiao
        - _3 :Xigua
    - page: Page number, starting from 1
    ### Return:
    - Kol List

    # [示例/Example]
    keyword = \"人工智能\"
    platformSource = \"_1\"
    page = 1

    Args:
        keyword (str): 关键词/Keyword
        platform_source (str): 平台来源/Platform Source
        page (int): 页码/Page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        platform_source=platform_source,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    platform_source: str,
    page: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""关键词搜索kol V1/Search Kol V1

     # [中文]
    ### 用途:
    - 关键词搜索kol V1
    - 该接口数据使用企业账号进行请求，收费较贵。
    - 价格：0.02$ / 次
    ### 参数:
    - keyword: 关键词
    - platformSource:
        - 平台来源，支持以下参数:
        - _1 :抖音(douyin)
        - _2 :头条(toutiao)
        - _3 :西瓜(xigua)
    - page: 页码，从1开始
    ### 返回:
    - kol列表

    # [English]
    ### Purpose:
    - Search Kol V1
    - The interface data is requested using an enterprise account, which is more expensive.
    - Price: 0.02$ / time
    ### Parameters:
    - keyword: Keyword
    - platformSource:
        - Platform source, supports the following parameters:
        - _1 :Douyin
        - _2 :Toutiao
        - _3 :Xigua
    - page: Page number, starting from 1
    ### Return:
    - Kol List

    # [示例/Example]
    keyword = \"人工智能\"
    platformSource = \"_1\"
    page = 1

    Args:
        keyword (str): 关键词/Keyword
        platform_source (str): 平台来源/Platform Source
        page (int): 页码/Page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword=keyword,
            platform_source=platform_source,
            page=page,
        )
    ).parsed
