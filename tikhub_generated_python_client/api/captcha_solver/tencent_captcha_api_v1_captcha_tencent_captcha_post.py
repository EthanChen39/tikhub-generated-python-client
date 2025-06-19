from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_tencent_captcha_api_v1_captcha_tencent_captcha_post import (
    BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/captcha/tencent_captcha",
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
    body: BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""Tencent Captcha Solver/Tencent验证码解决器

     # [中文]
    ### 用途:
    - Tencent Captcha验证码解决器
    ### 参数:
    - app_id: 在HTML中可以找到网站对应的app_id
    - url: 需要解决验证码的URL
    - proxy: 默认为None
    ### 返回:
    - 返回验证码解决结果

    # [English]
    ### Purpose:
    - Tencent Captcha solver
    ### Parameters:
    - app_id: The app_id corresponding to the website can be found in the HTML
    - url: URL that needs to solve the captcha
    - proxy: Default is None
    ### Return:
    - Return the captcha solution result

    # [Example/示例]
    app_id = \"10000000\"
    url = \"https://www.tencent.com/\"
    proxy = None

    Args:
        body (BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost):

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
    body: BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""Tencent Captcha Solver/Tencent验证码解决器

     # [中文]
    ### 用途:
    - Tencent Captcha验证码解决器
    ### 参数:
    - app_id: 在HTML中可以找到网站对应的app_id
    - url: 需要解决验证码的URL
    - proxy: 默认为None
    ### 返回:
    - 返回验证码解决结果

    # [English]
    ### Purpose:
    - Tencent Captcha solver
    ### Parameters:
    - app_id: The app_id corresponding to the website can be found in the HTML
    - url: URL that needs to solve the captcha
    - proxy: Default is None
    ### Return:
    - Return the captcha solution result

    # [Example/示例]
    app_id = \"10000000\"
    url = \"https://www.tencent.com/\"
    proxy = None

    Args:
        body (BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost):

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
    body: BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""Tencent Captcha Solver/Tencent验证码解决器

     # [中文]
    ### 用途:
    - Tencent Captcha验证码解决器
    ### 参数:
    - app_id: 在HTML中可以找到网站对应的app_id
    - url: 需要解决验证码的URL
    - proxy: 默认为None
    ### 返回:
    - 返回验证码解决结果

    # [English]
    ### Purpose:
    - Tencent Captcha solver
    ### Parameters:
    - app_id: The app_id corresponding to the website can be found in the HTML
    - url: URL that needs to solve the captcha
    - proxy: Default is None
    ### Return:
    - Return the captcha solution result

    # [Example/示例]
    app_id = \"10000000\"
    url = \"https://www.tencent.com/\"
    proxy = None

    Args:
        body (BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost):

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
    body: BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""Tencent Captcha Solver/Tencent验证码解决器

     # [中文]
    ### 用途:
    - Tencent Captcha验证码解决器
    ### 参数:
    - app_id: 在HTML中可以找到网站对应的app_id
    - url: 需要解决验证码的URL
    - proxy: 默认为None
    ### 返回:
    - 返回验证码解决结果

    # [English]
    ### Purpose:
    - Tencent Captcha solver
    ### Parameters:
    - app_id: The app_id corresponding to the website can be found in the HTML
    - url: URL that needs to solve the captcha
    - proxy: Default is None
    ### Return:
    - Return the captcha solution result

    # [Example/示例]
    app_id = \"10000000\"
    url = \"https://www.tencent.com/\"
    proxy = None

    Args:
        body (BodyTencentCaptchaApiV1CaptchaTencentCaptchaPost):

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
