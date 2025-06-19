from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_account_health_request import GetAccountHealthRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetAccountHealthRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_account_health_status",
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
    body: GetAccountHealthRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号健康状态/Get Creator Account Health Status

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的健康状况信息，包括过去 90 天内的健康评分（风险等级）以及当前累计的违规积分数量。
    - 关于违规积分：
        - 违规积分是 TikTok 用于衡量账号健康状况的重要指标。
        - 违规积分越高，账号健康状况越差，可能面临限流、禁播、封禁等处罚。
        - 违规积分将直接影响账号的曝光量和推荐量。

    ### 累计违规积分对应的惩罚等级：
    | 分数范围  | 惩罚措施                                                | 惩罚时长 |
    | --------- | --------------------------------------------------------- | -------- |
    | 9-11      | 警告（Warning）                                           | 无       |
    | 12-14     | 暂停电商权限（视频、直播、商品展示功能）                  | 24 小时  |
    | 15-17     | 暂停电商权限                                              | 48 小时  |
    | 18-20     | 暂停电商权限                                              | 72 小时  |
    | 21-23     | 暂停电商权限                                              | 1 周     |
    | 24 及以上 | 永久移除电商权限，封禁 TikTok Shop 创作者账号             | 永久禁用 |

    ### 备注:
    - 此接口仅适用于已开通 TikTok Shop 的创作者账号。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `risk_info`（健康状态信息）:
      - `risk_level_text`: 当前风险等级描述（如 Healthy）
      - `light_color`: 健康状态浅色展示色值（rgba 格式）
      - `dark_color`: 健康状态深色展示色值（rgba 格式）
    - `vio_score_rule_learn_url`: 查看违规积分规则说明的链接
    - `is_show_score`: 是否展示违规积分（布尔值）
    - `violation_score`: 当前违规积分数量
    - `creator_status`: 创作者账号状态码（0=正常）

    # [English]
    ### Purpose:
    - Retrieve the health status of a TikTok Shop creator account, including the health score over the
    past 90 days and the current number of accumulated violation points.
    - About violation points:
        - Violation points are key metrics used by TikTok to measure the health of a creator account.
        - Higher violation points indicate worse account health, and may lead to restrictions such as
    reduced exposure, suspension, or account bans.
        - Violation points directly impact the account’s visibility and recommendation on the platform.

    ### Punishment Levels for Accumulated Violation Points:
    | Score Range | Punishment Measures                                       | Duration         |
    | ----------- | ---------------------------------------------------------- | ---------------- |
    | 9-11        | Warning                                                     | None             |
    | 12-14       | E-commerce permissions suspended (video, live, product showcase) | 24 hours
    |
    | 15-17       | E-commerce permissions suspended                           | 48 hours         |
    | 18-20       | E-commerce permissions suspended                           | 72 hours         |
    | 21-23       | E-commerce permissions suspended                           | 1 week           |
    | 24+         | Permanent removal of e-commerce permissions and banning of TikTok Shop creator
    account | Permanently disabled |

    ### Notes:
    - This API is only applicable to TikTok Shop creator accounts.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - proxy: Optional HTTP proxy address, can be omitted if not needed
        - Example format: `http://username:password@host:port`

    ### Response:
    - `risk_info`: Account health status:
      - `risk_level_text`: Current health level description (e.g., Healthy)
      - `light_color`: Light color code for health level display (RGBA format)
      - `dark_color`: Dark color code for health level display (RGBA format)
    - `vio_score_rule_learn_url`: URL to learn more about violation point rules
    - `is_show_score`: Whether to display violation points (boolean)
    - `violation_score`: Current violation score
    - `creator_status`: Creator account status code (0 = normal)

    # [示例/Example]
    ```json
    payload = {
        \"cookie\": \"your_cookie\"
    }

    Args:
        body (GetAccountHealthRequest):

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
    body: GetAccountHealthRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号健康状态/Get Creator Account Health Status

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的健康状况信息，包括过去 90 天内的健康评分（风险等级）以及当前累计的违规积分数量。
    - 关于违规积分：
        - 违规积分是 TikTok 用于衡量账号健康状况的重要指标。
        - 违规积分越高，账号健康状况越差，可能面临限流、禁播、封禁等处罚。
        - 违规积分将直接影响账号的曝光量和推荐量。

    ### 累计违规积分对应的惩罚等级：
    | 分数范围  | 惩罚措施                                                | 惩罚时长 |
    | --------- | --------------------------------------------------------- | -------- |
    | 9-11      | 警告（Warning）                                           | 无       |
    | 12-14     | 暂停电商权限（视频、直播、商品展示功能）                  | 24 小时  |
    | 15-17     | 暂停电商权限                                              | 48 小时  |
    | 18-20     | 暂停电商权限                                              | 72 小时  |
    | 21-23     | 暂停电商权限                                              | 1 周     |
    | 24 及以上 | 永久移除电商权限，封禁 TikTok Shop 创作者账号             | 永久禁用 |

    ### 备注:
    - 此接口仅适用于已开通 TikTok Shop 的创作者账号。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `risk_info`（健康状态信息）:
      - `risk_level_text`: 当前风险等级描述（如 Healthy）
      - `light_color`: 健康状态浅色展示色值（rgba 格式）
      - `dark_color`: 健康状态深色展示色值（rgba 格式）
    - `vio_score_rule_learn_url`: 查看违规积分规则说明的链接
    - `is_show_score`: 是否展示违规积分（布尔值）
    - `violation_score`: 当前违规积分数量
    - `creator_status`: 创作者账号状态码（0=正常）

    # [English]
    ### Purpose:
    - Retrieve the health status of a TikTok Shop creator account, including the health score over the
    past 90 days and the current number of accumulated violation points.
    - About violation points:
        - Violation points are key metrics used by TikTok to measure the health of a creator account.
        - Higher violation points indicate worse account health, and may lead to restrictions such as
    reduced exposure, suspension, or account bans.
        - Violation points directly impact the account’s visibility and recommendation on the platform.

    ### Punishment Levels for Accumulated Violation Points:
    | Score Range | Punishment Measures                                       | Duration         |
    | ----------- | ---------------------------------------------------------- | ---------------- |
    | 9-11        | Warning                                                     | None             |
    | 12-14       | E-commerce permissions suspended (video, live, product showcase) | 24 hours
    |
    | 15-17       | E-commerce permissions suspended                           | 48 hours         |
    | 18-20       | E-commerce permissions suspended                           | 72 hours         |
    | 21-23       | E-commerce permissions suspended                           | 1 week           |
    | 24+         | Permanent removal of e-commerce permissions and banning of TikTok Shop creator
    account | Permanently disabled |

    ### Notes:
    - This API is only applicable to TikTok Shop creator accounts.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - proxy: Optional HTTP proxy address, can be omitted if not needed
        - Example format: `http://username:password@host:port`

    ### Response:
    - `risk_info`: Account health status:
      - `risk_level_text`: Current health level description (e.g., Healthy)
      - `light_color`: Light color code for health level display (RGBA format)
      - `dark_color`: Dark color code for health level display (RGBA format)
    - `vio_score_rule_learn_url`: URL to learn more about violation point rules
    - `is_show_score`: Whether to display violation points (boolean)
    - `violation_score`: Current violation score
    - `creator_status`: Creator account status code (0 = normal)

    # [示例/Example]
    ```json
    payload = {
        \"cookie\": \"your_cookie\"
    }

    Args:
        body (GetAccountHealthRequest):

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
    body: GetAccountHealthRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号健康状态/Get Creator Account Health Status

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的健康状况信息，包括过去 90 天内的健康评分（风险等级）以及当前累计的违规积分数量。
    - 关于违规积分：
        - 违规积分是 TikTok 用于衡量账号健康状况的重要指标。
        - 违规积分越高，账号健康状况越差，可能面临限流、禁播、封禁等处罚。
        - 违规积分将直接影响账号的曝光量和推荐量。

    ### 累计违规积分对应的惩罚等级：
    | 分数范围  | 惩罚措施                                                | 惩罚时长 |
    | --------- | --------------------------------------------------------- | -------- |
    | 9-11      | 警告（Warning）                                           | 无       |
    | 12-14     | 暂停电商权限（视频、直播、商品展示功能）                  | 24 小时  |
    | 15-17     | 暂停电商权限                                              | 48 小时  |
    | 18-20     | 暂停电商权限                                              | 72 小时  |
    | 21-23     | 暂停电商权限                                              | 1 周     |
    | 24 及以上 | 永久移除电商权限，封禁 TikTok Shop 创作者账号             | 永久禁用 |

    ### 备注:
    - 此接口仅适用于已开通 TikTok Shop 的创作者账号。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `risk_info`（健康状态信息）:
      - `risk_level_text`: 当前风险等级描述（如 Healthy）
      - `light_color`: 健康状态浅色展示色值（rgba 格式）
      - `dark_color`: 健康状态深色展示色值（rgba 格式）
    - `vio_score_rule_learn_url`: 查看违规积分规则说明的链接
    - `is_show_score`: 是否展示违规积分（布尔值）
    - `violation_score`: 当前违规积分数量
    - `creator_status`: 创作者账号状态码（0=正常）

    # [English]
    ### Purpose:
    - Retrieve the health status of a TikTok Shop creator account, including the health score over the
    past 90 days and the current number of accumulated violation points.
    - About violation points:
        - Violation points are key metrics used by TikTok to measure the health of a creator account.
        - Higher violation points indicate worse account health, and may lead to restrictions such as
    reduced exposure, suspension, or account bans.
        - Violation points directly impact the account’s visibility and recommendation on the platform.

    ### Punishment Levels for Accumulated Violation Points:
    | Score Range | Punishment Measures                                       | Duration         |
    | ----------- | ---------------------------------------------------------- | ---------------- |
    | 9-11        | Warning                                                     | None             |
    | 12-14       | E-commerce permissions suspended (video, live, product showcase) | 24 hours
    |
    | 15-17       | E-commerce permissions suspended                           | 48 hours         |
    | 18-20       | E-commerce permissions suspended                           | 72 hours         |
    | 21-23       | E-commerce permissions suspended                           | 1 week           |
    | 24+         | Permanent removal of e-commerce permissions and banning of TikTok Shop creator
    account | Permanently disabled |

    ### Notes:
    - This API is only applicable to TikTok Shop creator accounts.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - proxy: Optional HTTP proxy address, can be omitted if not needed
        - Example format: `http://username:password@host:port`

    ### Response:
    - `risk_info`: Account health status:
      - `risk_level_text`: Current health level description (e.g., Healthy)
      - `light_color`: Light color code for health level display (RGBA format)
      - `dark_color`: Dark color code for health level display (RGBA format)
    - `vio_score_rule_learn_url`: URL to learn more about violation point rules
    - `is_show_score`: Whether to display violation points (boolean)
    - `violation_score`: Current violation score
    - `creator_status`: Creator account status code (0 = normal)

    # [示例/Example]
    ```json
    payload = {
        \"cookie\": \"your_cookie\"
    }

    Args:
        body (GetAccountHealthRequest):

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
    body: GetAccountHealthRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号健康状态/Get Creator Account Health Status

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的健康状况信息，包括过去 90 天内的健康评分（风险等级）以及当前累计的违规积分数量。
    - 关于违规积分：
        - 违规积分是 TikTok 用于衡量账号健康状况的重要指标。
        - 违规积分越高，账号健康状况越差，可能面临限流、禁播、封禁等处罚。
        - 违规积分将直接影响账号的曝光量和推荐量。

    ### 累计违规积分对应的惩罚等级：
    | 分数范围  | 惩罚措施                                                | 惩罚时长 |
    | --------- | --------------------------------------------------------- | -------- |
    | 9-11      | 警告（Warning）                                           | 无       |
    | 12-14     | 暂停电商权限（视频、直播、商品展示功能）                  | 24 小时  |
    | 15-17     | 暂停电商权限                                              | 48 小时  |
    | 18-20     | 暂停电商权限                                              | 72 小时  |
    | 21-23     | 暂停电商权限                                              | 1 周     |
    | 24 及以上 | 永久移除电商权限，封禁 TikTok Shop 创作者账号             | 永久禁用 |

    ### 备注:
    - 此接口仅适用于已开通 TikTok Shop 的创作者账号。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `risk_info`（健康状态信息）:
      - `risk_level_text`: 当前风险等级描述（如 Healthy）
      - `light_color`: 健康状态浅色展示色值（rgba 格式）
      - `dark_color`: 健康状态深色展示色值（rgba 格式）
    - `vio_score_rule_learn_url`: 查看违规积分规则说明的链接
    - `is_show_score`: 是否展示违规积分（布尔值）
    - `violation_score`: 当前违规积分数量
    - `creator_status`: 创作者账号状态码（0=正常）

    # [English]
    ### Purpose:
    - Retrieve the health status of a TikTok Shop creator account, including the health score over the
    past 90 days and the current number of accumulated violation points.
    - About violation points:
        - Violation points are key metrics used by TikTok to measure the health of a creator account.
        - Higher violation points indicate worse account health, and may lead to restrictions such as
    reduced exposure, suspension, or account bans.
        - Violation points directly impact the account’s visibility and recommendation on the platform.

    ### Punishment Levels for Accumulated Violation Points:
    | Score Range | Punishment Measures                                       | Duration         |
    | ----------- | ---------------------------------------------------------- | ---------------- |
    | 9-11        | Warning                                                     | None             |
    | 12-14       | E-commerce permissions suspended (video, live, product showcase) | 24 hours
    |
    | 15-17       | E-commerce permissions suspended                           | 48 hours         |
    | 18-20       | E-commerce permissions suspended                           | 72 hours         |
    | 21-23       | E-commerce permissions suspended                           | 1 week           |
    | 24+         | Permanent removal of e-commerce permissions and banning of TikTok Shop creator
    account | Permanently disabled |

    ### Notes:
    - This API is only applicable to TikTok Shop creator accounts.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - proxy: Optional HTTP proxy address, can be omitted if not needed
        - Example format: `http://username:password@host:port`

    ### Response:
    - `risk_info`: Account health status:
      - `risk_level_text`: Current health level description (e.g., Healthy)
      - `light_color`: Light color code for health level display (RGBA format)
      - `dark_color`: Dark color code for health level display (RGBA format)
    - `vio_score_rule_learn_url`: URL to learn more about violation point rules
    - `is_show_score`: Whether to display violation points (boolean)
    - `violation_score`: Current violation score
    - `creator_status`: Creator account status code (0 = normal)

    # [示例/Example]
    ```json
    payload = {
        \"cookie\": \"your_cookie\"
    }

    Args:
        body (GetAccountHealthRequest):

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
