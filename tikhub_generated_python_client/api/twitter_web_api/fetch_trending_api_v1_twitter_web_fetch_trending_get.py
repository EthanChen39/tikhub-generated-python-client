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
    country: Union[Unset, str] = "UnitedStates",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["country"] = country

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/twitter/web/fetch_trending",
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
    country: Union[Unset, str] = "UnitedStates",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""趋势/Trending

     # [中文]
    ### 用途:
    - 获取趋势
    ### 参数:
    - country: 国家，默认为UnitedStates，其他可选值见下方
        - China
        - India
        - Japan
        - Russia
        - Germany
        - Indonesia
        - Brazil
        - France
        - UnitedKingdom
        - Turkey
        - Italy
        - Mexico
        - SouthKorea
        - Canada
        - Spain
        - SaudiArabia
        - Egypt
        - Australia
        - Poland
        - Iran
        - Pakistan
        - Vietnam
        - Nigeria
        - Bangladesh
        - Netherlands
        - Argentina
        - Philippines
        - Malaysia
        - Colombia
        - UniteArabEmirates
        - Romania
        - Belgium
        - Switzerland
        - Singapore
        - Sweden
        - Norway
        - Austria
        - Kazakhstan
        - Algeria
        - Chile
        - Czechia
        - Peru
        - Iraq
        - Israel
        - Ukraine
        - Denmark
        - Portugal
        - Hungary
        - Greece
        - Finland
        - NewZealand
        - Belarus
        - Slovakia
        - Serbia
        - Lithuania
        - Luxembourg
        - Estonia

    ### 返回:
    - 趋势

    # [English]
    ### Purpose:
    - Get Trending
    ### Parameters:
    - country: Country, default is UnitedStates, other optional values are as follows
        - China
        - India
        - Japan
        - Russia
        - Germany
        - Indonesia
        - Brazil
        - France
        - UnitedKingdom
        - Turkey
        - Italy
        - Mexico
        - SouthKorea
        - Canada
        - Spain
        - SaudiArabia
        - Egypt
        - Australia
        - Poland
        - Iran
        - Pakistan
        - Vietnam
        - Nigeria
        - Bangladesh
        - Netherlands
        - Argentina
        - Philippines
        - Malaysia
        - Colombia
        - UniteArabEmirates
        - Romania
        - Belgium
        - Switzerland
        - Singapore
        - Sweden
        - Norway
        - Austria
        - Kazakhstan
        - Algeria
        - Chile
        - Czechia
        - Peru

    ### Return:
    - Trending

    # [示例/Example]
    country = \"UnitedStates\"

    Args:
        country (Union[Unset, str]): 国家/Country Default: 'UnitedStates'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        country=country,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, str] = "UnitedStates",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""趋势/Trending

     # [中文]
    ### 用途:
    - 获取趋势
    ### 参数:
    - country: 国家，默认为UnitedStates，其他可选值见下方
        - China
        - India
        - Japan
        - Russia
        - Germany
        - Indonesia
        - Brazil
        - France
        - UnitedKingdom
        - Turkey
        - Italy
        - Mexico
        - SouthKorea
        - Canada
        - Spain
        - SaudiArabia
        - Egypt
        - Australia
        - Poland
        - Iran
        - Pakistan
        - Vietnam
        - Nigeria
        - Bangladesh
        - Netherlands
        - Argentina
        - Philippines
        - Malaysia
        - Colombia
        - UniteArabEmirates
        - Romania
        - Belgium
        - Switzerland
        - Singapore
        - Sweden
        - Norway
        - Austria
        - Kazakhstan
        - Algeria
        - Chile
        - Czechia
        - Peru
        - Iraq
        - Israel
        - Ukraine
        - Denmark
        - Portugal
        - Hungary
        - Greece
        - Finland
        - NewZealand
        - Belarus
        - Slovakia
        - Serbia
        - Lithuania
        - Luxembourg
        - Estonia

    ### 返回:
    - 趋势

    # [English]
    ### Purpose:
    - Get Trending
    ### Parameters:
    - country: Country, default is UnitedStates, other optional values are as follows
        - China
        - India
        - Japan
        - Russia
        - Germany
        - Indonesia
        - Brazil
        - France
        - UnitedKingdom
        - Turkey
        - Italy
        - Mexico
        - SouthKorea
        - Canada
        - Spain
        - SaudiArabia
        - Egypt
        - Australia
        - Poland
        - Iran
        - Pakistan
        - Vietnam
        - Nigeria
        - Bangladesh
        - Netherlands
        - Argentina
        - Philippines
        - Malaysia
        - Colombia
        - UniteArabEmirates
        - Romania
        - Belgium
        - Switzerland
        - Singapore
        - Sweden
        - Norway
        - Austria
        - Kazakhstan
        - Algeria
        - Chile
        - Czechia
        - Peru

    ### Return:
    - Trending

    # [示例/Example]
    country = \"UnitedStates\"

    Args:
        country (Union[Unset, str]): 国家/Country Default: 'UnitedStates'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        country=country,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, str] = "UnitedStates",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""趋势/Trending

     # [中文]
    ### 用途:
    - 获取趋势
    ### 参数:
    - country: 国家，默认为UnitedStates，其他可选值见下方
        - China
        - India
        - Japan
        - Russia
        - Germany
        - Indonesia
        - Brazil
        - France
        - UnitedKingdom
        - Turkey
        - Italy
        - Mexico
        - SouthKorea
        - Canada
        - Spain
        - SaudiArabia
        - Egypt
        - Australia
        - Poland
        - Iran
        - Pakistan
        - Vietnam
        - Nigeria
        - Bangladesh
        - Netherlands
        - Argentina
        - Philippines
        - Malaysia
        - Colombia
        - UniteArabEmirates
        - Romania
        - Belgium
        - Switzerland
        - Singapore
        - Sweden
        - Norway
        - Austria
        - Kazakhstan
        - Algeria
        - Chile
        - Czechia
        - Peru
        - Iraq
        - Israel
        - Ukraine
        - Denmark
        - Portugal
        - Hungary
        - Greece
        - Finland
        - NewZealand
        - Belarus
        - Slovakia
        - Serbia
        - Lithuania
        - Luxembourg
        - Estonia

    ### 返回:
    - 趋势

    # [English]
    ### Purpose:
    - Get Trending
    ### Parameters:
    - country: Country, default is UnitedStates, other optional values are as follows
        - China
        - India
        - Japan
        - Russia
        - Germany
        - Indonesia
        - Brazil
        - France
        - UnitedKingdom
        - Turkey
        - Italy
        - Mexico
        - SouthKorea
        - Canada
        - Spain
        - SaudiArabia
        - Egypt
        - Australia
        - Poland
        - Iran
        - Pakistan
        - Vietnam
        - Nigeria
        - Bangladesh
        - Netherlands
        - Argentina
        - Philippines
        - Malaysia
        - Colombia
        - UniteArabEmirates
        - Romania
        - Belgium
        - Switzerland
        - Singapore
        - Sweden
        - Norway
        - Austria
        - Kazakhstan
        - Algeria
        - Chile
        - Czechia
        - Peru

    ### Return:
    - Trending

    # [示例/Example]
    country = \"UnitedStates\"

    Args:
        country (Union[Unset, str]): 国家/Country Default: 'UnitedStates'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        country=country,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, str] = "UnitedStates",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""趋势/Trending

     # [中文]
    ### 用途:
    - 获取趋势
    ### 参数:
    - country: 国家，默认为UnitedStates，其他可选值见下方
        - China
        - India
        - Japan
        - Russia
        - Germany
        - Indonesia
        - Brazil
        - France
        - UnitedKingdom
        - Turkey
        - Italy
        - Mexico
        - SouthKorea
        - Canada
        - Spain
        - SaudiArabia
        - Egypt
        - Australia
        - Poland
        - Iran
        - Pakistan
        - Vietnam
        - Nigeria
        - Bangladesh
        - Netherlands
        - Argentina
        - Philippines
        - Malaysia
        - Colombia
        - UniteArabEmirates
        - Romania
        - Belgium
        - Switzerland
        - Singapore
        - Sweden
        - Norway
        - Austria
        - Kazakhstan
        - Algeria
        - Chile
        - Czechia
        - Peru
        - Iraq
        - Israel
        - Ukraine
        - Denmark
        - Portugal
        - Hungary
        - Greece
        - Finland
        - NewZealand
        - Belarus
        - Slovakia
        - Serbia
        - Lithuania
        - Luxembourg
        - Estonia

    ### 返回:
    - 趋势

    # [English]
    ### Purpose:
    - Get Trending
    ### Parameters:
    - country: Country, default is UnitedStates, other optional values are as follows
        - China
        - India
        - Japan
        - Russia
        - Germany
        - Indonesia
        - Brazil
        - France
        - UnitedKingdom
        - Turkey
        - Italy
        - Mexico
        - SouthKorea
        - Canada
        - Spain
        - SaudiArabia
        - Egypt
        - Australia
        - Poland
        - Iran
        - Pakistan
        - Vietnam
        - Nigeria
        - Bangladesh
        - Netherlands
        - Argentina
        - Philippines
        - Malaysia
        - Colombia
        - UniteArabEmirates
        - Romania
        - Belgium
        - Switzerland
        - Singapore
        - Sweden
        - Norway
        - Austria
        - Kazakhstan
        - Algeria
        - Chile
        - Czechia
        - Peru

    ### Return:
    - Trending

    # [示例/Example]
    country = \"UnitedStates\"

    Args:
        country (Union[Unset, str]): 国家/Country Default: 'UnitedStates'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            country=country,
        )
    ).parsed
