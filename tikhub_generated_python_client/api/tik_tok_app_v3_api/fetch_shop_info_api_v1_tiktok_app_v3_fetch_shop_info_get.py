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
    shop_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["shop_id"] = shop_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_shop_info",
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
    shop_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家信息数据/Get shop information data

     # [中文]
    ### 用途:
    - 获取商家信息数据
    ### 参数:
    - shop_id: 商家id,店铺id
    ### 返回:
    - 商家信息数据

    # [English]
    ### Purpose:
    - Get shop information data
    ### Parameters:
    - shop_id: Seller id, shop id
    ### Return:
    - Shop information data

    # [示例/Example]
    shop_id = \"8646942781241463007\"

    Args:
        shop_id (str): 商家id,店铺id/Seller id, shop id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        shop_id=shop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    shop_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家信息数据/Get shop information data

     # [中文]
    ### 用途:
    - 获取商家信息数据
    ### 参数:
    - shop_id: 商家id,店铺id
    ### 返回:
    - 商家信息数据

    # [English]
    ### Purpose:
    - Get shop information data
    ### Parameters:
    - shop_id: Seller id, shop id
    ### Return:
    - Shop information data

    # [示例/Example]
    shop_id = \"8646942781241463007\"

    Args:
        shop_id (str): 商家id,店铺id/Seller id, shop id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        shop_id=shop_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    shop_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家信息数据/Get shop information data

     # [中文]
    ### 用途:
    - 获取商家信息数据
    ### 参数:
    - shop_id: 商家id,店铺id
    ### 返回:
    - 商家信息数据

    # [English]
    ### Purpose:
    - Get shop information data
    ### Parameters:
    - shop_id: Seller id, shop id
    ### Return:
    - Shop information data

    # [示例/Example]
    shop_id = \"8646942781241463007\"

    Args:
        shop_id (str): 商家id,店铺id/Seller id, shop id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        shop_id=shop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    shop_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家信息数据/Get shop information data

     # [中文]
    ### 用途:
    - 获取商家信息数据
    ### 参数:
    - shop_id: 商家id,店铺id
    ### 返回:
    - 商家信息数据

    # [English]
    ### Purpose:
    - Get shop information data
    ### Parameters:
    - shop_id: Seller id, shop id
    ### Return:
    - Shop information data

    # [示例/Example]
    shop_id = \"8646942781241463007\"

    Args:
        shop_id (str): 商家id,店铺id/Seller id, shop id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            shop_id=shop_id,
        )
    ).parsed
