from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.challenge_post_request import ChallengePostRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: ChallengePostRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/web/fetch_challenge_posts",
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
    body: ChallengePostRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""话题作品/Challenge Posts

     # [中文]
    ### 用途:
    - 话题作品
    ### 参数:
    - challenge_id: 话题id
    - sort_type: 排序类型
        - 0:综合排序 1:最热排序 2:最新排序
    - cursor: 游标
    - count: 数量
    - cookie: 用户自行提供的Cookie，用于获取更多数据。
    ### 返回:
    - 话题作品

    # [English]
    ### Purpose:
    - Challenge Posts
    ### Parameters:
    - challenge_id: Challenge id
    - sort_type: Sort type
        - 0: Comprehensive sorting 1: Hottest sorting 2: Latest sorting
    - cursor: Cursor
    - count: Number
    - cookie: User provided Cookie, used to get more data
    ### Return:
    - Challenge Posts

    # [示例/Example]
    challenge_id = \"1750525814851611\"
    sort_type = 0
    offset = 0
    cursor = 0
    count = 20

    Args:
        body (ChallengePostRequest):

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
    body: ChallengePostRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""话题作品/Challenge Posts

     # [中文]
    ### 用途:
    - 话题作品
    ### 参数:
    - challenge_id: 话题id
    - sort_type: 排序类型
        - 0:综合排序 1:最热排序 2:最新排序
    - cursor: 游标
    - count: 数量
    - cookie: 用户自行提供的Cookie，用于获取更多数据。
    ### 返回:
    - 话题作品

    # [English]
    ### Purpose:
    - Challenge Posts
    ### Parameters:
    - challenge_id: Challenge id
    - sort_type: Sort type
        - 0: Comprehensive sorting 1: Hottest sorting 2: Latest sorting
    - cursor: Cursor
    - count: Number
    - cookie: User provided Cookie, used to get more data
    ### Return:
    - Challenge Posts

    # [示例/Example]
    challenge_id = \"1750525814851611\"
    sort_type = 0
    offset = 0
    cursor = 0
    count = 20

    Args:
        body (ChallengePostRequest):

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
    body: ChallengePostRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""话题作品/Challenge Posts

     # [中文]
    ### 用途:
    - 话题作品
    ### 参数:
    - challenge_id: 话题id
    - sort_type: 排序类型
        - 0:综合排序 1:最热排序 2:最新排序
    - cursor: 游标
    - count: 数量
    - cookie: 用户自行提供的Cookie，用于获取更多数据。
    ### 返回:
    - 话题作品

    # [English]
    ### Purpose:
    - Challenge Posts
    ### Parameters:
    - challenge_id: Challenge id
    - sort_type: Sort type
        - 0: Comprehensive sorting 1: Hottest sorting 2: Latest sorting
    - cursor: Cursor
    - count: Number
    - cookie: User provided Cookie, used to get more data
    ### Return:
    - Challenge Posts

    # [示例/Example]
    challenge_id = \"1750525814851611\"
    sort_type = 0
    offset = 0
    cursor = 0
    count = 20

    Args:
        body (ChallengePostRequest):

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
    body: ChallengePostRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""话题作品/Challenge Posts

     # [中文]
    ### 用途:
    - 话题作品
    ### 参数:
    - challenge_id: 话题id
    - sort_type: 排序类型
        - 0:综合排序 1:最热排序 2:最新排序
    - cursor: 游标
    - count: 数量
    - cookie: 用户自行提供的Cookie，用于获取更多数据。
    ### 返回:
    - 话题作品

    # [English]
    ### Purpose:
    - Challenge Posts
    ### Parameters:
    - challenge_id: Challenge id
    - sort_type: Sort type
        - 0: Comprehensive sorting 1: Hottest sorting 2: Latest sorting
    - cursor: Cursor
    - count: Number
    - cookie: User provided Cookie, used to get more data
    ### Return:
    - Challenge Posts

    # [示例/Example]
    challenge_id = \"1750525814851611\"
    sort_type = 0
    offset = 0
    cursor = 0
    count = 20

    Args:
        body (ChallengePostRequest):

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
