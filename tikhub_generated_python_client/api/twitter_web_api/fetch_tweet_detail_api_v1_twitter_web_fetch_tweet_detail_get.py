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
    tweet_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["tweet_id"] = tweet_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/twitter/web/fetch_tweet_detail",
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
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个推文数据/Get single tweet data

     # [中文]
    ### 用途:
    - 获取单个推文数据
    ### 参数:
    - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的
    1808168603721650364。
    ### 返回:
    - 推文数据

    # [English]
    ### Purpose:
    - Get single tweet data
    ### Parameters:
    - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in
    https://x.com/elonmusk/status/1808168603721650364
    ### Return:
    - Tweet data

    # [示例/Example]
    tweet_id = \"1808168603721650364\"

    Args:
        tweet_id (str): 推文ID/Tweet ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        tweet_id=tweet_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    tweet_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个推文数据/Get single tweet data

     # [中文]
    ### 用途:
    - 获取单个推文数据
    ### 参数:
    - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的
    1808168603721650364。
    ### 返回:
    - 推文数据

    # [English]
    ### Purpose:
    - Get single tweet data
    ### Parameters:
    - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in
    https://x.com/elonmusk/status/1808168603721650364
    ### Return:
    - Tweet data

    # [示例/Example]
    tweet_id = \"1808168603721650364\"

    Args:
        tweet_id (str): 推文ID/Tweet ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        tweet_id=tweet_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    tweet_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个推文数据/Get single tweet data

     # [中文]
    ### 用途:
    - 获取单个推文数据
    ### 参数:
    - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的
    1808168603721650364。
    ### 返回:
    - 推文数据

    # [English]
    ### Purpose:
    - Get single tweet data
    ### Parameters:
    - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in
    https://x.com/elonmusk/status/1808168603721650364
    ### Return:
    - Tweet data

    # [示例/Example]
    tweet_id = \"1808168603721650364\"

    Args:
        tweet_id (str): 推文ID/Tweet ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        tweet_id=tweet_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    tweet_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个推文数据/Get single tweet data

     # [中文]
    ### 用途:
    - 获取单个推文数据
    ### 参数:
    - tweet_id: 推文ID，可以从推文链接中获取。例如：https://x.com/elonmusk/status/1808168603721650364 中的
    1808168603721650364。
    ### 返回:
    - 推文数据

    # [English]
    ### Purpose:
    - Get single tweet data
    ### Parameters:
    - tweet_id: Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in
    https://x.com/elonmusk/status/1808168603721650364
    ### Return:
    - Tweet data

    # [示例/Example]
    tweet_id = \"1808168603721650364\"

    Args:
        tweet_id (str): 推文ID/Tweet ID

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
        )
    ).parsed
