from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_creator_account_info_request import GetCreatorAccountInfoRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetCreatorAccountInfoRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_creator_account_info",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: GetCreatorAccountInfoRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号信息/Get Creator Account Info

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的基础信息，包括用户名、头像链接、账号ID、注册地区、绑定合作伙伴信息、权限列表等。
    - 可用于账号状态验证、账号信息展示、合作关系检查及后续业务逻辑处理。

    ### 备注:
    - 适用于所有 TikTok 创作者账号。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `user_id`: 用户ID（字符串）
    - `user_type`: 用户类型（数字，代表账号类型）
    - `register_region_id`: 注册地区代码（如 \"us\"）
    - `user_name`: 用户名
    - `avatar`: 头像信息对象
      - `uri`: 头像资源URI
      - `url_list`: 头像图片URL列表
    - `permission_list`: 权限列表（整数数组）
    - `partner_id`: 合作伙伴ID
    - `partner_name`: 合作伙伴名称
    - `shop_account_official`: 是否为官方认证店铺账号（布尔值）
    - `switch_info`: 功能开关信息（如直播功能开关，字符串格式）
    - `tt_uid`: TikTok UID（字符串）
    - `nick_name`: 昵称
    - `live_streamer_menu_experiment`: 直播菜单实验字段（字符串，可能为空）
    - `experiment_variants`: 实验变种配置（对象）

    # [English]
    ### Purpose:
    - Retrieve basic information of a TikTok Shop creator account, including username, avatar URLs,
    account ID, register region, partner binding info, and permission list.
    - Useful for verifying account status, displaying user profile data, checking partner binding
    status, and determining access permissions for business processes.

    ### Notes:
    - Applicable to all TikTok creator accounts.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - proxy: Optional HTTP proxy address, can be omitted if not used
        - Example format: `http://username:password@host:port`

    ### Return Content Description:
    - `user_id`: User ID (string)
    - `user_type`: User type (integer, indicates account type)
    - `register_region_id`: Registered region code (e.g., \"us\")
    - `user_name`: Username
    - `avatar`: Avatar info object
      - `uri`: Avatar resource URI
      - `url_list`: List of avatar image URLs
    - `permission_list`: Permission list (list of integers)
    - `partner_id`: Partner ID
    - `partner_name`: Partner name
    - `shop_account_official`: Whether it's an official shop account (boolean)
    - `switch_info`: Feature switch info (e.g., live event switch, string format)
    - `tt_uid`: TikTok UID (string)
    - `nick_name`: Nickname
    - `live_streamer_menu_experiment`: Live streamer menu experiment field (string, may be empty)
    - `experiment_variants`: Experiment variant configurations (object)

    # [示例/Example]
    ```json
    {
      \"cookie\": \"your_cookie\"
    }
    ```

    Args:
        body (GetCreatorAccountInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: GetCreatorAccountInfoRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号信息/Get Creator Account Info

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的基础信息，包括用户名、头像链接、账号ID、注册地区、绑定合作伙伴信息、权限列表等。
    - 可用于账号状态验证、账号信息展示、合作关系检查及后续业务逻辑处理。

    ### 备注:
    - 适用于所有 TikTok 创作者账号。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `user_id`: 用户ID（字符串）
    - `user_type`: 用户类型（数字，代表账号类型）
    - `register_region_id`: 注册地区代码（如 \"us\"）
    - `user_name`: 用户名
    - `avatar`: 头像信息对象
      - `uri`: 头像资源URI
      - `url_list`: 头像图片URL列表
    - `permission_list`: 权限列表（整数数组）
    - `partner_id`: 合作伙伴ID
    - `partner_name`: 合作伙伴名称
    - `shop_account_official`: 是否为官方认证店铺账号（布尔值）
    - `switch_info`: 功能开关信息（如直播功能开关，字符串格式）
    - `tt_uid`: TikTok UID（字符串）
    - `nick_name`: 昵称
    - `live_streamer_menu_experiment`: 直播菜单实验字段（字符串，可能为空）
    - `experiment_variants`: 实验变种配置（对象）

    # [English]
    ### Purpose:
    - Retrieve basic information of a TikTok Shop creator account, including username, avatar URLs,
    account ID, register region, partner binding info, and permission list.
    - Useful for verifying account status, displaying user profile data, checking partner binding
    status, and determining access permissions for business processes.

    ### Notes:
    - Applicable to all TikTok creator accounts.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - proxy: Optional HTTP proxy address, can be omitted if not used
        - Example format: `http://username:password@host:port`

    ### Return Content Description:
    - `user_id`: User ID (string)
    - `user_type`: User type (integer, indicates account type)
    - `register_region_id`: Registered region code (e.g., \"us\")
    - `user_name`: Username
    - `avatar`: Avatar info object
      - `uri`: Avatar resource URI
      - `url_list`: List of avatar image URLs
    - `permission_list`: Permission list (list of integers)
    - `partner_id`: Partner ID
    - `partner_name`: Partner name
    - `shop_account_official`: Whether it's an official shop account (boolean)
    - `switch_info`: Feature switch info (e.g., live event switch, string format)
    - `tt_uid`: TikTok UID (string)
    - `nick_name`: Nickname
    - `live_streamer_menu_experiment`: Live streamer menu experiment field (string, may be empty)
    - `experiment_variants`: Experiment variant configurations (object)

    # [示例/Example]
    ```json
    {
      \"cookie\": \"your_cookie\"
    }
    ```

    Args:
        body (GetCreatorAccountInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GetCreatorAccountInfoRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号信息/Get Creator Account Info

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的基础信息，包括用户名、头像链接、账号ID、注册地区、绑定合作伙伴信息、权限列表等。
    - 可用于账号状态验证、账号信息展示、合作关系检查及后续业务逻辑处理。

    ### 备注:
    - 适用于所有 TikTok 创作者账号。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `user_id`: 用户ID（字符串）
    - `user_type`: 用户类型（数字，代表账号类型）
    - `register_region_id`: 注册地区代码（如 \"us\"）
    - `user_name`: 用户名
    - `avatar`: 头像信息对象
      - `uri`: 头像资源URI
      - `url_list`: 头像图片URL列表
    - `permission_list`: 权限列表（整数数组）
    - `partner_id`: 合作伙伴ID
    - `partner_name`: 合作伙伴名称
    - `shop_account_official`: 是否为官方认证店铺账号（布尔值）
    - `switch_info`: 功能开关信息（如直播功能开关，字符串格式）
    - `tt_uid`: TikTok UID（字符串）
    - `nick_name`: 昵称
    - `live_streamer_menu_experiment`: 直播菜单实验字段（字符串，可能为空）
    - `experiment_variants`: 实验变种配置（对象）

    # [English]
    ### Purpose:
    - Retrieve basic information of a TikTok Shop creator account, including username, avatar URLs,
    account ID, register region, partner binding info, and permission list.
    - Useful for verifying account status, displaying user profile data, checking partner binding
    status, and determining access permissions for business processes.

    ### Notes:
    - Applicable to all TikTok creator accounts.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - proxy: Optional HTTP proxy address, can be omitted if not used
        - Example format: `http://username:password@host:port`

    ### Return Content Description:
    - `user_id`: User ID (string)
    - `user_type`: User type (integer, indicates account type)
    - `register_region_id`: Registered region code (e.g., \"us\")
    - `user_name`: Username
    - `avatar`: Avatar info object
      - `uri`: Avatar resource URI
      - `url_list`: List of avatar image URLs
    - `permission_list`: Permission list (list of integers)
    - `partner_id`: Partner ID
    - `partner_name`: Partner name
    - `shop_account_official`: Whether it's an official shop account (boolean)
    - `switch_info`: Feature switch info (e.g., live event switch, string format)
    - `tt_uid`: TikTok UID (string)
    - `nick_name`: Nickname
    - `live_streamer_menu_experiment`: Live streamer menu experiment field (string, may be empty)
    - `experiment_variants`: Experiment variant configurations (object)

    # [示例/Example]
    ```json
    {
      \"cookie\": \"your_cookie\"
    }
    ```

    Args:
        body (GetCreatorAccountInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GetCreatorAccountInfoRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号信息/Get Creator Account Info

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的基础信息，包括用户名、头像链接、账号ID、注册地区、绑定合作伙伴信息、权限列表等。
    - 可用于账号状态验证、账号信息展示、合作关系检查及后续业务逻辑处理。

    ### 备注:
    - 适用于所有 TikTok 创作者账号。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `user_id`: 用户ID（字符串）
    - `user_type`: 用户类型（数字，代表账号类型）
    - `register_region_id`: 注册地区代码（如 \"us\"）
    - `user_name`: 用户名
    - `avatar`: 头像信息对象
      - `uri`: 头像资源URI
      - `url_list`: 头像图片URL列表
    - `permission_list`: 权限列表（整数数组）
    - `partner_id`: 合作伙伴ID
    - `partner_name`: 合作伙伴名称
    - `shop_account_official`: 是否为官方认证店铺账号（布尔值）
    - `switch_info`: 功能开关信息（如直播功能开关，字符串格式）
    - `tt_uid`: TikTok UID（字符串）
    - `nick_name`: 昵称
    - `live_streamer_menu_experiment`: 直播菜单实验字段（字符串，可能为空）
    - `experiment_variants`: 实验变种配置（对象）

    # [English]
    ### Purpose:
    - Retrieve basic information of a TikTok Shop creator account, including username, avatar URLs,
    account ID, register region, partner binding info, and permission list.
    - Useful for verifying account status, displaying user profile data, checking partner binding
    status, and determining access permissions for business processes.

    ### Notes:
    - Applicable to all TikTok creator accounts.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - proxy: Optional HTTP proxy address, can be omitted if not used
        - Example format: `http://username:password@host:port`

    ### Return Content Description:
    - `user_id`: User ID (string)
    - `user_type`: User type (integer, indicates account type)
    - `register_region_id`: Registered region code (e.g., \"us\")
    - `user_name`: Username
    - `avatar`: Avatar info object
      - `uri`: Avatar resource URI
      - `url_list`: List of avatar image URLs
    - `permission_list`: Permission list (list of integers)
    - `partner_id`: Partner ID
    - `partner_name`: Partner name
    - `shop_account_official`: Whether it's an official shop account (boolean)
    - `switch_info`: Feature switch info (e.g., live event switch, string format)
    - `tt_uid`: TikTok UID (string)
    - `nick_name`: Nickname
    - `live_streamer_menu_experiment`: Live streamer menu experiment field (string, may be empty)
    - `experiment_variants`: Experiment variant configurations (object)

    # [示例/Example]
    ```json
    {
      \"cookie\": \"your_cookie\"
    }
    ```

    Args:
        body (GetCreatorAccountInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
