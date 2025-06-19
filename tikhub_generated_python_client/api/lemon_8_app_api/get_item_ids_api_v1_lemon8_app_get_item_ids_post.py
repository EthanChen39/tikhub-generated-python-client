from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: list[Any],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/lemon8/app/get_item_ids",
    }

    _kwargs["json"] = body

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
    body: list[Any],
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""通过分享链接批量获取作品ID/Get post IDs in batch through sharing links

     # [中文]
    ### 用途:
    - 通过分享链接批量获取作品ID，一次最多获取10个
    ### 参数:
    - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
    ### 返回:
    - 作品ID列表

    # [English]
    ### Purpose:
    - Get post IDs in batch through sharing links, up to 10 at a time
    ### Parameters:
    - share_texts: Share links list, supports long links and short links, can be obtained and copied
    from the share button on the web and APP.
    ### Return:
    - Post IDs list

    # [示例/Example]
    share_texts = [
        \"https://www.lemon8-app.com/@deathlabs_/7445613324903006766\",
        \"https://v.lemon8-app.com/al/OghwFTppx\"
    ]

    Args:
        body (list[Any]): 分享链接列表/Share links list

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
    body: list[Any],
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""通过分享链接批量获取作品ID/Get post IDs in batch through sharing links

     # [中文]
    ### 用途:
    - 通过分享链接批量获取作品ID，一次最多获取10个
    ### 参数:
    - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
    ### 返回:
    - 作品ID列表

    # [English]
    ### Purpose:
    - Get post IDs in batch through sharing links, up to 10 at a time
    ### Parameters:
    - share_texts: Share links list, supports long links and short links, can be obtained and copied
    from the share button on the web and APP.
    ### Return:
    - Post IDs list

    # [示例/Example]
    share_texts = [
        \"https://www.lemon8-app.com/@deathlabs_/7445613324903006766\",
        \"https://v.lemon8-app.com/al/OghwFTppx\"
    ]

    Args:
        body (list[Any]): 分享链接列表/Share links list

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
    body: list[Any],
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""通过分享链接批量获取作品ID/Get post IDs in batch through sharing links

     # [中文]
    ### 用途:
    - 通过分享链接批量获取作品ID，一次最多获取10个
    ### 参数:
    - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
    ### 返回:
    - 作品ID列表

    # [English]
    ### Purpose:
    - Get post IDs in batch through sharing links, up to 10 at a time
    ### Parameters:
    - share_texts: Share links list, supports long links and short links, can be obtained and copied
    from the share button on the web and APP.
    ### Return:
    - Post IDs list

    # [示例/Example]
    share_texts = [
        \"https://www.lemon8-app.com/@deathlabs_/7445613324903006766\",
        \"https://v.lemon8-app.com/al/OghwFTppx\"
    ]

    Args:
        body (list[Any]): 分享链接列表/Share links list

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
    body: list[Any],
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""通过分享链接批量获取作品ID/Get post IDs in batch through sharing links

     # [中文]
    ### 用途:
    - 通过分享链接批量获取作品ID，一次最多获取10个
    ### 参数:
    - share_texts: 分享链接列表，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
    ### 返回:
    - 作品ID列表

    # [English]
    ### Purpose:
    - Get post IDs in batch through sharing links, up to 10 at a time
    ### Parameters:
    - share_texts: Share links list, supports long links and short links, can be obtained and copied
    from the share button on the web and APP.
    ### Return:
    - Post IDs list

    # [示例/Example]
    share_texts = [
        \"https://www.lemon8-app.com/@deathlabs_/7445613324903006766\",
        \"https://v.lemon8-app.com/al/OghwFTppx\"
    ]

    Args:
        body (list[Any]): 分享链接列表/Share links list

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
