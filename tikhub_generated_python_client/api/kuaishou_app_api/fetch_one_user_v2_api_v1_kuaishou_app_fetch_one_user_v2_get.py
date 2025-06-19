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
    user_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/kuaishou/app/fetch_one_user_v2",
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
    user_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个用户数据V2/Get single user data V2

     # [中文]
    ### 用途:
    - 获取单个用户数据 V2
    - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
    ### 参数:
    - user_id: 支持`eid`或`userId`，eid是用户主页链接中的一部分，user_id则可以从不同的接口中获取。
    - 两种用户ID都可以使用，下面是两种用户ID的示例，这两个ID都指向同一个用户：
        - eid = \"3xz63mn6fngqtiq\"
        - userId = \"228905802\"
    ### 返回:
    - 用户数据

    # [English]
    ### Purpose:
    - Fetch single user data V2
    - This API is more expensive, but more stable, please check the price list in the user background
    for specific prices.
    ### Parameters:
    - user_id: Supports `eid` or `userId`, `eid` is part of the user profile link, and `user_id` can be
    obtained from different interfaces.
    - Both user IDs can be used, here are examples of the two user IDs, both of which point to the same
    user:
        - eid = \"3xz63mn6fngqtiq\"
        - userId = \"228905802\"
    ### Returns:
    - User data

    # [示例/Example]
    user_id = \"3xz63mn6fngqtiq\"

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个用户数据V2/Get single user data V2

     # [中文]
    ### 用途:
    - 获取单个用户数据 V2
    - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
    ### 参数:
    - user_id: 支持`eid`或`userId`，eid是用户主页链接中的一部分，user_id则可以从不同的接口中获取。
    - 两种用户ID都可以使用，下面是两种用户ID的示例，这两个ID都指向同一个用户：
        - eid = \"3xz63mn6fngqtiq\"
        - userId = \"228905802\"
    ### 返回:
    - 用户数据

    # [English]
    ### Purpose:
    - Fetch single user data V2
    - This API is more expensive, but more stable, please check the price list in the user background
    for specific prices.
    ### Parameters:
    - user_id: Supports `eid` or `userId`, `eid` is part of the user profile link, and `user_id` can be
    obtained from different interfaces.
    - Both user IDs can be used, here are examples of the two user IDs, both of which point to the same
    user:
        - eid = \"3xz63mn6fngqtiq\"
        - userId = \"228905802\"
    ### Returns:
    - User data

    # [示例/Example]
    user_id = \"3xz63mn6fngqtiq\"

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个用户数据V2/Get single user data V2

     # [中文]
    ### 用途:
    - 获取单个用户数据 V2
    - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
    ### 参数:
    - user_id: 支持`eid`或`userId`，eid是用户主页链接中的一部分，user_id则可以从不同的接口中获取。
    - 两种用户ID都可以使用，下面是两种用户ID的示例，这两个ID都指向同一个用户：
        - eid = \"3xz63mn6fngqtiq\"
        - userId = \"228905802\"
    ### 返回:
    - 用户数据

    # [English]
    ### Purpose:
    - Fetch single user data V2
    - This API is more expensive, but more stable, please check the price list in the user background
    for specific prices.
    ### Parameters:
    - user_id: Supports `eid` or `userId`, `eid` is part of the user profile link, and `user_id` can be
    obtained from different interfaces.
    - Both user IDs can be used, here are examples of the two user IDs, both of which point to the same
    user:
        - eid = \"3xz63mn6fngqtiq\"
        - userId = \"228905802\"
    ### Returns:
    - User data

    # [示例/Example]
    user_id = \"3xz63mn6fngqtiq\"

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个用户数据V2/Get single user data V2

     # [中文]
    ### 用途:
    - 获取单个用户数据 V2
    - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
    ### 参数:
    - user_id: 支持`eid`或`userId`，eid是用户主页链接中的一部分，user_id则可以从不同的接口中获取。
    - 两种用户ID都可以使用，下面是两种用户ID的示例，这两个ID都指向同一个用户：
        - eid = \"3xz63mn6fngqtiq\"
        - userId = \"228905802\"
    ### 返回:
    - 用户数据

    # [English]
    ### Purpose:
    - Fetch single user data V2
    - This API is more expensive, but more stable, please check the price list in the user background
    for specific prices.
    ### Parameters:
    - user_id: Supports `eid` or `userId`, `eid` is part of the user profile link, and `user_id` can be
    obtained from different interfaces.
    - Both user IDs can be used, here are examples of the two user IDs, both of which point to the same
    user:
        - eid = \"3xz63mn6fngqtiq\"
        - userId = \"228905802\"
    ### Returns:
    - User data

    # [示例/Example]
    user_id = \"3xz63mn6fngqtiq\"

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
        )
    ).parsed
