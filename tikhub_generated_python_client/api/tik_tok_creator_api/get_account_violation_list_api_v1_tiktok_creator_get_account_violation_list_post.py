from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_violation_record_request import GetViolationRecordRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetViolationRecordRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_account_violation_list",
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
    body: GetViolationRecordRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号违规记录列表/Get Creator Account Violation Record List

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的违规记录信息，用于了解账号在运营期间的违规历史和处理情况。
    - 返回的违规记录包含违规类型、违规时间、违规原因、违规处理措施、申诉状态、是否可申诉等信息。
    - 支持分页查询，可按时间顺序获取多条违规记录。
    - 适用于创作者账号违规风险管理、账号健康监控和数据合规审计。

    ### 备注:
    - 此接口仅适用于 TikTok Shop 创作者账号。
    - 支持分页查询，每次默认返回最新的违规记录。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - page: 整数类型，页码，默认为第 1 页
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `records`（违规记录列表）:
      - `record_id`: 违规记录 ID
      - `violation_time`: 违规发生时间（Unix 时间戳）
      - `violation_info`:
        - `violation_reason`: 违规原因描述
        - `violation_detail`: 违规详情描述
        - `violation_suggestion`: 平台提供的整改建议
        - `policy_url`: 相关政策链接
        - `violation_type`: 违规类别（如视频违规）
      - `record_status`: 记录状态（1 表示有效）
      - `appeal_status`: 申诉状态（0=未申诉，1=已申诉）
      - `enforcement_title`: 平台针对违规采取的执行措施描述（例如扣分、佣金冻结等）
      - `appeal_valid_time`: 申诉有效截止时间（Unix 时间戳）
      - `can_appeal`: 是否允许发起申诉（布尔值）
    - `total`: 总违规记录数
    - `has_more`: 是否还有更多数据
    - `start_time`: 查询起始时间
    - `end_time`: 查询结束时间
    - `creator_status`: 创作者账号状态码（如 0=正常）

    # [English]
    ### Purpose:
    - Retrieve the violation history of a TikTok Shop creator account, providing details about past
    violations and corresponding enforcement actions.
    - The returned violation records include violation type, violation time, violation reasons,
    enforcement actions, appeal status, and eligibility for appeal.
    - Pagination is supported to retrieve multiple records in chronological order.
    - Suitable for creator account risk management, health monitoring, and compliance auditing.

    ### Notes:
    - This API is available only for TikTok Shop creator accounts.
    - Pagination is supported; by default, it retrieves the latest violation records.

    ### Parameters:
    - cookie: User's Cookie string for authentication
    - page: Integer, page number (default is `1`)
    - proxy: Optional HTTP proxy address, can be omitted if not needed
        - Example format: `http://username:password@host:port`

    ### Response:
    - `records`: List of violation records:
      - `record_id`: Unique ID of the violation record
      - `violation_time`: Time when the violation occurred (Unix timestamp)
      - `violation_info`:
        - `violation_reason`: Reason for the violation
        - `violation_detail`: Detailed description (may be empty)
        - `violation_suggestion`: Recommended corrective action
        - `policy_url`: Link to the related policy
        - `violation_type`: Type of violation (e.g., Video violation)
      - `record_status`: Record status (1 = active)
      - `appeal_status`: Appeal status (0 = not appealed, 1 = appealed)
      - `enforcement_title`: List of enforcement actions taken (e.g., point assignment, commission
    withholding)
      - `appeal_valid_time`: Deadline for submitting an appeal (Unix timestamp)
      - `can_appeal`: Whether the record is eligible for appeal (boolean)
    - `total`: Total number of violation records
    - `has_more`: Whether there are more records to fetch
    - `start_time`: Query start time
    - `end_time`: Query end time
    - `creator_status`: Creator account status code (e.g., 0 = normal)

    # [示例/Example]
    ```json
    {
        \"cookie\": \"your_cookie_here\",
        \"page\": 1
    }
    ```

    Args:
        body (GetViolationRecordRequest):

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
    body: GetViolationRecordRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号违规记录列表/Get Creator Account Violation Record List

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的违规记录信息，用于了解账号在运营期间的违规历史和处理情况。
    - 返回的违规记录包含违规类型、违规时间、违规原因、违规处理措施、申诉状态、是否可申诉等信息。
    - 支持分页查询，可按时间顺序获取多条违规记录。
    - 适用于创作者账号违规风险管理、账号健康监控和数据合规审计。

    ### 备注:
    - 此接口仅适用于 TikTok Shop 创作者账号。
    - 支持分页查询，每次默认返回最新的违规记录。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - page: 整数类型，页码，默认为第 1 页
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `records`（违规记录列表）:
      - `record_id`: 违规记录 ID
      - `violation_time`: 违规发生时间（Unix 时间戳）
      - `violation_info`:
        - `violation_reason`: 违规原因描述
        - `violation_detail`: 违规详情描述
        - `violation_suggestion`: 平台提供的整改建议
        - `policy_url`: 相关政策链接
        - `violation_type`: 违规类别（如视频违规）
      - `record_status`: 记录状态（1 表示有效）
      - `appeal_status`: 申诉状态（0=未申诉，1=已申诉）
      - `enforcement_title`: 平台针对违规采取的执行措施描述（例如扣分、佣金冻结等）
      - `appeal_valid_time`: 申诉有效截止时间（Unix 时间戳）
      - `can_appeal`: 是否允许发起申诉（布尔值）
    - `total`: 总违规记录数
    - `has_more`: 是否还有更多数据
    - `start_time`: 查询起始时间
    - `end_time`: 查询结束时间
    - `creator_status`: 创作者账号状态码（如 0=正常）

    # [English]
    ### Purpose:
    - Retrieve the violation history of a TikTok Shop creator account, providing details about past
    violations and corresponding enforcement actions.
    - The returned violation records include violation type, violation time, violation reasons,
    enforcement actions, appeal status, and eligibility for appeal.
    - Pagination is supported to retrieve multiple records in chronological order.
    - Suitable for creator account risk management, health monitoring, and compliance auditing.

    ### Notes:
    - This API is available only for TikTok Shop creator accounts.
    - Pagination is supported; by default, it retrieves the latest violation records.

    ### Parameters:
    - cookie: User's Cookie string for authentication
    - page: Integer, page number (default is `1`)
    - proxy: Optional HTTP proxy address, can be omitted if not needed
        - Example format: `http://username:password@host:port`

    ### Response:
    - `records`: List of violation records:
      - `record_id`: Unique ID of the violation record
      - `violation_time`: Time when the violation occurred (Unix timestamp)
      - `violation_info`:
        - `violation_reason`: Reason for the violation
        - `violation_detail`: Detailed description (may be empty)
        - `violation_suggestion`: Recommended corrective action
        - `policy_url`: Link to the related policy
        - `violation_type`: Type of violation (e.g., Video violation)
      - `record_status`: Record status (1 = active)
      - `appeal_status`: Appeal status (0 = not appealed, 1 = appealed)
      - `enforcement_title`: List of enforcement actions taken (e.g., point assignment, commission
    withholding)
      - `appeal_valid_time`: Deadline for submitting an appeal (Unix timestamp)
      - `can_appeal`: Whether the record is eligible for appeal (boolean)
    - `total`: Total number of violation records
    - `has_more`: Whether there are more records to fetch
    - `start_time`: Query start time
    - `end_time`: Query end time
    - `creator_status`: Creator account status code (e.g., 0 = normal)

    # [示例/Example]
    ```json
    {
        \"cookie\": \"your_cookie_here\",
        \"page\": 1
    }
    ```

    Args:
        body (GetViolationRecordRequest):

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
    body: GetViolationRecordRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号违规记录列表/Get Creator Account Violation Record List

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的违规记录信息，用于了解账号在运营期间的违规历史和处理情况。
    - 返回的违规记录包含违规类型、违规时间、违规原因、违规处理措施、申诉状态、是否可申诉等信息。
    - 支持分页查询，可按时间顺序获取多条违规记录。
    - 适用于创作者账号违规风险管理、账号健康监控和数据合规审计。

    ### 备注:
    - 此接口仅适用于 TikTok Shop 创作者账号。
    - 支持分页查询，每次默认返回最新的违规记录。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - page: 整数类型，页码，默认为第 1 页
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `records`（违规记录列表）:
      - `record_id`: 违规记录 ID
      - `violation_time`: 违规发生时间（Unix 时间戳）
      - `violation_info`:
        - `violation_reason`: 违规原因描述
        - `violation_detail`: 违规详情描述
        - `violation_suggestion`: 平台提供的整改建议
        - `policy_url`: 相关政策链接
        - `violation_type`: 违规类别（如视频违规）
      - `record_status`: 记录状态（1 表示有效）
      - `appeal_status`: 申诉状态（0=未申诉，1=已申诉）
      - `enforcement_title`: 平台针对违规采取的执行措施描述（例如扣分、佣金冻结等）
      - `appeal_valid_time`: 申诉有效截止时间（Unix 时间戳）
      - `can_appeal`: 是否允许发起申诉（布尔值）
    - `total`: 总违规记录数
    - `has_more`: 是否还有更多数据
    - `start_time`: 查询起始时间
    - `end_time`: 查询结束时间
    - `creator_status`: 创作者账号状态码（如 0=正常）

    # [English]
    ### Purpose:
    - Retrieve the violation history of a TikTok Shop creator account, providing details about past
    violations and corresponding enforcement actions.
    - The returned violation records include violation type, violation time, violation reasons,
    enforcement actions, appeal status, and eligibility for appeal.
    - Pagination is supported to retrieve multiple records in chronological order.
    - Suitable for creator account risk management, health monitoring, and compliance auditing.

    ### Notes:
    - This API is available only for TikTok Shop creator accounts.
    - Pagination is supported; by default, it retrieves the latest violation records.

    ### Parameters:
    - cookie: User's Cookie string for authentication
    - page: Integer, page number (default is `1`)
    - proxy: Optional HTTP proxy address, can be omitted if not needed
        - Example format: `http://username:password@host:port`

    ### Response:
    - `records`: List of violation records:
      - `record_id`: Unique ID of the violation record
      - `violation_time`: Time when the violation occurred (Unix timestamp)
      - `violation_info`:
        - `violation_reason`: Reason for the violation
        - `violation_detail`: Detailed description (may be empty)
        - `violation_suggestion`: Recommended corrective action
        - `policy_url`: Link to the related policy
        - `violation_type`: Type of violation (e.g., Video violation)
      - `record_status`: Record status (1 = active)
      - `appeal_status`: Appeal status (0 = not appealed, 1 = appealed)
      - `enforcement_title`: List of enforcement actions taken (e.g., point assignment, commission
    withholding)
      - `appeal_valid_time`: Deadline for submitting an appeal (Unix timestamp)
      - `can_appeal`: Whether the record is eligible for appeal (boolean)
    - `total`: Total number of violation records
    - `has_more`: Whether there are more records to fetch
    - `start_time`: Query start time
    - `end_time`: Query end time
    - `creator_status`: Creator account status code (e.g., 0 = normal)

    # [示例/Example]
    ```json
    {
        \"cookie\": \"your_cookie_here\",
        \"page\": 1
    }
    ```

    Args:
        body (GetViolationRecordRequest):

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
    body: GetViolationRecordRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者账号违规记录列表/Get Creator Account Violation Record List

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号的违规记录信息，用于了解账号在运营期间的违规历史和处理情况。
    - 返回的违规记录包含违规类型、违规时间、违规原因、违规处理措施、申诉状态、是否可申诉等信息。
    - 支持分页查询，可按时间顺序获取多条违规记录。
    - 适用于创作者账号违规风险管理、账号健康监控和数据合规审计。

    ### 备注:
    - 此接口仅适用于 TikTok Shop 创作者账号。
    - 支持分页查询，每次默认返回最新的违规记录。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - page: 整数类型，页码，默认为第 1 页
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `records`（违规记录列表）:
      - `record_id`: 违规记录 ID
      - `violation_time`: 违规发生时间（Unix 时间戳）
      - `violation_info`:
        - `violation_reason`: 违规原因描述
        - `violation_detail`: 违规详情描述
        - `violation_suggestion`: 平台提供的整改建议
        - `policy_url`: 相关政策链接
        - `violation_type`: 违规类别（如视频违规）
      - `record_status`: 记录状态（1 表示有效）
      - `appeal_status`: 申诉状态（0=未申诉，1=已申诉）
      - `enforcement_title`: 平台针对违规采取的执行措施描述（例如扣分、佣金冻结等）
      - `appeal_valid_time`: 申诉有效截止时间（Unix 时间戳）
      - `can_appeal`: 是否允许发起申诉（布尔值）
    - `total`: 总违规记录数
    - `has_more`: 是否还有更多数据
    - `start_time`: 查询起始时间
    - `end_time`: 查询结束时间
    - `creator_status`: 创作者账号状态码（如 0=正常）

    # [English]
    ### Purpose:
    - Retrieve the violation history of a TikTok Shop creator account, providing details about past
    violations and corresponding enforcement actions.
    - The returned violation records include violation type, violation time, violation reasons,
    enforcement actions, appeal status, and eligibility for appeal.
    - Pagination is supported to retrieve multiple records in chronological order.
    - Suitable for creator account risk management, health monitoring, and compliance auditing.

    ### Notes:
    - This API is available only for TikTok Shop creator accounts.
    - Pagination is supported; by default, it retrieves the latest violation records.

    ### Parameters:
    - cookie: User's Cookie string for authentication
    - page: Integer, page number (default is `1`)
    - proxy: Optional HTTP proxy address, can be omitted if not needed
        - Example format: `http://username:password@host:port`

    ### Response:
    - `records`: List of violation records:
      - `record_id`: Unique ID of the violation record
      - `violation_time`: Time when the violation occurred (Unix timestamp)
      - `violation_info`:
        - `violation_reason`: Reason for the violation
        - `violation_detail`: Detailed description (may be empty)
        - `violation_suggestion`: Recommended corrective action
        - `policy_url`: Link to the related policy
        - `violation_type`: Type of violation (e.g., Video violation)
      - `record_status`: Record status (1 = active)
      - `appeal_status`: Appeal status (0 = not appealed, 1 = appealed)
      - `enforcement_title`: List of enforcement actions taken (e.g., point assignment, commission
    withholding)
      - `appeal_valid_time`: Deadline for submitting an appeal (Unix timestamp)
      - `can_appeal`: Whether the record is eligible for appeal (boolean)
    - `total`: Total number of violation records
    - `has_more`: Whether there are more records to fetch
    - `start_time`: Query start time
    - `end_time`: Query end time
    - `creator_status`: Creator account status code (e.g., 0 = normal)

    # [示例/Example]
    ```json
    {
        \"cookie\": \"your_cookie_here\",
        \"page\": 1
    }
    ```

    Args:
        body (GetViolationRecordRequest):

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
