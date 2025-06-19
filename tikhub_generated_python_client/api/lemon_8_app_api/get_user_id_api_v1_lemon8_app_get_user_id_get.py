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
    share_text: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["share_text"] = share_text

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/lemon8/app/get_user_id",
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
    share_text: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""通过分享链接获取用户ID/Get user ID through sharing link

     # [中文]
    ### 用途:
    - 通过分享链接获取用户ID
    ### 参数:
    - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
    ### 返回:
    - 用户ID

    # [English]
    ### Purpose:
    - Get user ID through sharing link
    ### Parameters:
    - share_text: Share link, supports long links and short links, can be obtained and copied from the
    share button on the web and APP.
    ### Return:
    - User ID

    # [示例/Example]
    share_text = \"https://www.lemon8-app.com/lemon8cars?region=us\"
    share_text = \"https://v.lemon8-app.com/al/OgZrsUppx\"

    Args:
        share_text (str): 分享链接/Share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        share_text=share_text,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    share_text: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""通过分享链接获取用户ID/Get user ID through sharing link

     # [中文]
    ### 用途:
    - 通过分享链接获取用户ID
    ### 参数:
    - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
    ### 返回:
    - 用户ID

    # [English]
    ### Purpose:
    - Get user ID through sharing link
    ### Parameters:
    - share_text: Share link, supports long links and short links, can be obtained and copied from the
    share button on the web and APP.
    ### Return:
    - User ID

    # [示例/Example]
    share_text = \"https://www.lemon8-app.com/lemon8cars?region=us\"
    share_text = \"https://v.lemon8-app.com/al/OgZrsUppx\"

    Args:
        share_text (str): 分享链接/Share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        share_text=share_text,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    share_text: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""通过分享链接获取用户ID/Get user ID through sharing link

     # [中文]
    ### 用途:
    - 通过分享链接获取用户ID
    ### 参数:
    - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
    ### 返回:
    - 用户ID

    # [English]
    ### Purpose:
    - Get user ID through sharing link
    ### Parameters:
    - share_text: Share link, supports long links and short links, can be obtained and copied from the
    share button on the web and APP.
    ### Return:
    - User ID

    # [示例/Example]
    share_text = \"https://www.lemon8-app.com/lemon8cars?region=us\"
    share_text = \"https://v.lemon8-app.com/al/OgZrsUppx\"

    Args:
        share_text (str): 分享链接/Share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        share_text=share_text,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    share_text: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""通过分享链接获取用户ID/Get user ID through sharing link

     # [中文]
    ### 用途:
    - 通过分享链接获取用户ID
    ### 参数:
    - share_text: 分享链接，支持长链接和短链接，可以从网页端以及APP中的分享按钮获取并复制。
    ### 返回:
    - 用户ID

    # [English]
    ### Purpose:
    - Get user ID through sharing link
    ### Parameters:
    - share_text: Share link, supports long links and short links, can be obtained and copied from the
    share button on the web and APP.
    ### Return:
    - User ID

    # [示例/Example]
    share_text = \"https://www.lemon8-app.com/lemon8cars?region=us\"
    share_text = \"https://v.lemon8-app.com/al/OgZrsUppx\"

    Args:
        share_text (str): 分享链接/Share link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            share_text=share_text,
        )
    ).parsed
