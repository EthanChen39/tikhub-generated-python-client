from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post import (
    BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/billboard/fetch_hot_account_list",
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
    body: BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门账号/Fetch hot account list

     # [中文]
    ### 用途:
    - 获取热门账号
    ### 参数:
    - date_window: 时间窗口，格式 小时，默认24小时
    - page_num: 页码，默认1
    - page_size: 每页数量，默认20
    - query_tag: 子级垂类标签，空则为全部，多个标签需传入
    {\"value\": \"{顶级垂类标签id}\", \"children\": [
        {\"value\": \"{子级垂类标签id}\"},
        {\"value\": \"{子级垂类标签id}\"}
    ]}
    ### 返回:
    - 热门账号

    # [English]
    ### Purpose:
    - Get the hot account
    ### Parameters:
    - date_window: Time window, format hour, default 24 hours
    - page_num: Page number, default 1
    - page_size: Number of items per page, default 20
    - query_tag: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
    {\"value\": \"{top-level vertical category id}\", \"children\": [
        {\"value\": \"{sub-level vertical category id}\"},
        {\"value\": \"{sub-level vertical category id}\"}
    ]}
    ### Return:
    - Hot account

    Args:
        body (BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost):

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
    body: BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门账号/Fetch hot account list

     # [中文]
    ### 用途:
    - 获取热门账号
    ### 参数:
    - date_window: 时间窗口，格式 小时，默认24小时
    - page_num: 页码，默认1
    - page_size: 每页数量，默认20
    - query_tag: 子级垂类标签，空则为全部，多个标签需传入
    {\"value\": \"{顶级垂类标签id}\", \"children\": [
        {\"value\": \"{子级垂类标签id}\"},
        {\"value\": \"{子级垂类标签id}\"}
    ]}
    ### 返回:
    - 热门账号

    # [English]
    ### Purpose:
    - Get the hot account
    ### Parameters:
    - date_window: Time window, format hour, default 24 hours
    - page_num: Page number, default 1
    - page_size: Number of items per page, default 20
    - query_tag: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
    {\"value\": \"{top-level vertical category id}\", \"children\": [
        {\"value\": \"{sub-level vertical category id}\"},
        {\"value\": \"{sub-level vertical category id}\"}
    ]}
    ### Return:
    - Hot account

    Args:
        body (BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost):

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
    body: BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门账号/Fetch hot account list

     # [中文]
    ### 用途:
    - 获取热门账号
    ### 参数:
    - date_window: 时间窗口，格式 小时，默认24小时
    - page_num: 页码，默认1
    - page_size: 每页数量，默认20
    - query_tag: 子级垂类标签，空则为全部，多个标签需传入
    {\"value\": \"{顶级垂类标签id}\", \"children\": [
        {\"value\": \"{子级垂类标签id}\"},
        {\"value\": \"{子级垂类标签id}\"}
    ]}
    ### 返回:
    - 热门账号

    # [English]
    ### Purpose:
    - Get the hot account
    ### Parameters:
    - date_window: Time window, format hour, default 24 hours
    - page_num: Page number, default 1
    - page_size: Number of items per page, default 20
    - query_tag: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
    {\"value\": \"{top-level vertical category id}\", \"children\": [
        {\"value\": \"{sub-level vertical category id}\"},
        {\"value\": \"{sub-level vertical category id}\"}
    ]}
    ### Return:
    - Hot account

    Args:
        body (BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost):

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
    body: BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门账号/Fetch hot account list

     # [中文]
    ### 用途:
    - 获取热门账号
    ### 参数:
    - date_window: 时间窗口，格式 小时，默认24小时
    - page_num: 页码，默认1
    - page_size: 每页数量，默认20
    - query_tag: 子级垂类标签，空则为全部，多个标签需传入
    {\"value\": \"{顶级垂类标签id}\", \"children\": [
        {\"value\": \"{子级垂类标签id}\"},
        {\"value\": \"{子级垂类标签id}\"}
    ]}
    ### 返回:
    - 热门账号

    # [English]
    ### Purpose:
    - Get the hot account
    ### Parameters:
    - date_window: Time window, format hour, default 24 hours
    - page_num: Page number, default 1
    - page_size: Number of items per page, default 20
    - query_tag: Sub-level vertical category tag, empty for all, multiple tags need to be passed in
    {\"value\": \"{top-level vertical category id}\", \"children\": [
        {\"value\": \"{sub-level vertical category id}\"},
        {\"value\": \"{sub-level vertical category id}\"}
    ]}
    ### Return:
    - Hot account

    Args:
        body (BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost):

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
