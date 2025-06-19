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
    language_code: Union[Unset, str] = "en",
    country_code: Union[Unset, str] = "us",
    section: Union[Unset, str] = "Now",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["language_code"] = language_code

    params["country_code"] = country_code

    params["section"] = section

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/youtube/web/get_trending_videos",
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
    language_code: Union[Unset, str] = "en",
    country_code: Union[Unset, str] = "us",
    section: Union[Unset, str] = "Now",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取趋势视频/Get trending videos

     # [中文]
    ### 用途:
    - 获取趋势视频。
    ### 参数:
    - language_code: 语言代码，默认为en。
    - country_code: 国家代码，默认为us。
    - section: 类型，默认为Now，可选值为Music, Gaming, Movies。
    ### 返回:
    - 趋势视频。

    # [English]
    ### Purpose:
    - Get trending videos.
    ### Parameters:
    - language_code: Language code, default is en.
    - country_code: Country code, default is us.
    - section: Section, default is Now, optional values are Music, Gaming, Movies.
    ### Returns:
    - Trending videos.

    # [示例/Example]

    Args:
        language_code (Union[Unset, str]): 语言代码/Language code Default: 'en'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'us'.
        section (Union[Unset, str]): 类型/Section Default: 'Now'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        language_code=language_code,
        country_code=country_code,
        section=section,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    language_code: Union[Unset, str] = "en",
    country_code: Union[Unset, str] = "us",
    section: Union[Unset, str] = "Now",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取趋势视频/Get trending videos

     # [中文]
    ### 用途:
    - 获取趋势视频。
    ### 参数:
    - language_code: 语言代码，默认为en。
    - country_code: 国家代码，默认为us。
    - section: 类型，默认为Now，可选值为Music, Gaming, Movies。
    ### 返回:
    - 趋势视频。

    # [English]
    ### Purpose:
    - Get trending videos.
    ### Parameters:
    - language_code: Language code, default is en.
    - country_code: Country code, default is us.
    - section: Section, default is Now, optional values are Music, Gaming, Movies.
    ### Returns:
    - Trending videos.

    # [示例/Example]

    Args:
        language_code (Union[Unset, str]): 语言代码/Language code Default: 'en'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'us'.
        section (Union[Unset, str]): 类型/Section Default: 'Now'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        language_code=language_code,
        country_code=country_code,
        section=section,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    language_code: Union[Unset, str] = "en",
    country_code: Union[Unset, str] = "us",
    section: Union[Unset, str] = "Now",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取趋势视频/Get trending videos

     # [中文]
    ### 用途:
    - 获取趋势视频。
    ### 参数:
    - language_code: 语言代码，默认为en。
    - country_code: 国家代码，默认为us。
    - section: 类型，默认为Now，可选值为Music, Gaming, Movies。
    ### 返回:
    - 趋势视频。

    # [English]
    ### Purpose:
    - Get trending videos.
    ### Parameters:
    - language_code: Language code, default is en.
    - country_code: Country code, default is us.
    - section: Section, default is Now, optional values are Music, Gaming, Movies.
    ### Returns:
    - Trending videos.

    # [示例/Example]

    Args:
        language_code (Union[Unset, str]): 语言代码/Language code Default: 'en'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'us'.
        section (Union[Unset, str]): 类型/Section Default: 'Now'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        language_code=language_code,
        country_code=country_code,
        section=section,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    language_code: Union[Unset, str] = "en",
    country_code: Union[Unset, str] = "us",
    section: Union[Unset, str] = "Now",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取趋势视频/Get trending videos

     # [中文]
    ### 用途:
    - 获取趋势视频。
    ### 参数:
    - language_code: 语言代码，默认为en。
    - country_code: 国家代码，默认为us。
    - section: 类型，默认为Now，可选值为Music, Gaming, Movies。
    ### 返回:
    - 趋势视频。

    # [English]
    ### Purpose:
    - Get trending videos.
    ### Parameters:
    - language_code: Language code, default is en.
    - country_code: Country code, default is us.
    - section: Section, default is Now, optional values are Music, Gaming, Movies.
    ### Returns:
    - Trending videos.

    # [示例/Example]

    Args:
        language_code (Union[Unset, str]): 语言代码/Language code Default: 'en'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'us'.
        section (Union[Unset, str]): 类型/Section Default: 'Now'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            language_code=language_code,
            country_code=country_code,
            section=section,
        )
    ).parsed
