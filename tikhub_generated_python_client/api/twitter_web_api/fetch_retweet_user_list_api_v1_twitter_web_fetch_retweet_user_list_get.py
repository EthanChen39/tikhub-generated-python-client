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
    tweet_id: str,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["tweet_id"] = tweet_id

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/twitter/web/fetch_retweet_user_list",
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
    tweet_id: str,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""转推用户列表/ReTweet User list

     # [中文]
    ### 用途:
    - 获取转推用户列表
    ### 参数:
    - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的
    1808168603721650364。
    - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
    ### 返回:
    - 转推用户列表

    # [English]
    ### Purpose:
    - Get ReTweet User list
    ### Parameters:
    - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in
    https://x.com/elonmusk/status/1808168603721650364
    - cursor: Cursor, default is None, used for paging, obtained from the last request
    ### Return:
    - ReTweet User list

    # [示例/Example]
    tweet_id = \"1808168603721650364\"
    cursor = None

    Args:
        tweet_id (str): 推文ID/Tweet ID
        cursor (Union[Unset, str]): 游标/Cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        tweet_id=tweet_id,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    tweet_id: str,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""转推用户列表/ReTweet User list

     # [中文]
    ### 用途:
    - 获取转推用户列表
    ### 参数:
    - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的
    1808168603721650364。
    - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
    ### 返回:
    - 转推用户列表

    # [English]
    ### Purpose:
    - Get ReTweet User list
    ### Parameters:
    - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in
    https://x.com/elonmusk/status/1808168603721650364
    - cursor: Cursor, default is None, used for paging, obtained from the last request
    ### Return:
    - ReTweet User list

    # [示例/Example]
    tweet_id = \"1808168603721650364\"
    cursor = None

    Args:
        tweet_id (str): 推文ID/Tweet ID
        cursor (Union[Unset, str]): 游标/Cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        tweet_id=tweet_id,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    tweet_id: str,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""转推用户列表/ReTweet User list

     # [中文]
    ### 用途:
    - 获取转推用户列表
    ### 参数:
    - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的
    1808168603721650364。
    - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
    ### 返回:
    - 转推用户列表

    # [English]
    ### Purpose:
    - Get ReTweet User list
    ### Parameters:
    - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in
    https://x.com/elonmusk/status/1808168603721650364
    - cursor: Cursor, default is None, used for paging, obtained from the last request
    ### Return:
    - ReTweet User list

    # [示例/Example]
    tweet_id = \"1808168603721650364\"
    cursor = None

    Args:
        tweet_id (str): 推文ID/Tweet ID
        cursor (Union[Unset, str]): 游标/Cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        tweet_id=tweet_id,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    tweet_id: str,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""转推用户列表/ReTweet User list

     # [中文]
    ### 用途:
    - 获取转推用户列表
    ### 参数:
    - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的
    1808168603721650364。
    - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
    ### 返回:
    - 转推用户列表

    # [English]
    ### Purpose:
    - Get ReTweet User list
    ### Parameters:
    - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in
    https://x.com/elonmusk/status/1808168603721650364
    - cursor: Cursor, default is None, used for paging, obtained from the last request
    ### Return:
    - ReTweet User list

    # [示例/Example]
    tweet_id = \"1808168603721650364\"
    cursor = None

    Args:
        tweet_id (str): 推文ID/Tweet ID
        cursor (Union[Unset, str]): 游标/Cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            tweet_id=tweet_id,
            cursor=cursor,
        )
    ).parsed
