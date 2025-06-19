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
    api_key: str,
    invite_code: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["api_key"] = api_key

    params["invite_code"] = invite_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/interaction/apply",
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
    client: Union[AuthenticatedClient, Client],
    api_key: str,
    invite_code: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)

     # [通知]
    - 此接口已经废弃，用户现在无需手动申请调用权限，只需要在用户后台更新API Key的对应权限即可，即API Key对应的的Scope。
    # [中文]
    ### 接口用途:
    - 申请使用TikTok交互API的接口权限（Scope），请在使用交互类接口之前申请，否则将无法正常请求。
    ### 申请流程:
    - 申请接口权限需要邀请码，如果你没有邀请码，可以在Discord服务器中联系管理员获取。
    - Discord服务器链接: [TikHub Discord](https://discord.gg/aMEAS8Xsvz)
    ### 申请须知:
    - 此权限仅限于当前提交的API Key，不可跨API Key使用。
    - 用户需要使用美国地区注册且有效的的TikTok账号进行登录，否则保证将无法正常请求。
    - 用户需要使用美国地区的代理IP进行获取Cookie，否则将保证无法正常请求。
    - 用户需要使用美国地区的代理IP进行请求，否则将无法保证正常请求。
    ### 用户守则以及责任:
    - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。
    - 请不要将接口权限分享给他人，否则我们将会停止对你的服务。
    - 接口请求目前暂时定为每秒5次请求。
    ### 返回:
    - 申请结果以及申请的邀请码，请自行保留邀请码，以便后续使用。

    # [Notice]
    - This interface has been deprecated, users no longer need to apply for permission to call the API,
    just update the corresponding permission of the API Key in the user background, that is, the Scope
    corresponding to the API Key.
    # [English]
    ### Purpose:
    - Apply for the interface permission (Scope) of TikTok Interaction API, please apply before using
    the interactive interface, otherwise the request will not be made normally.
    ### Application process:
    - Applying for interface permissions requires an invitation code, if you do not have an invitation
    code, you can contact the administrator on the Discord server.
    - Discord server link: [TikHub Discord](https://discord.gg/aMEAS8Xsvz)
    ### Application notes:
    - This permission is limited to the API Key submitted, and cannot be used across API Keys.
    - Users need to log in with a registered and valid TikTok account in the United States, otherwise
    the request will not be made normally.
    - Users need to use a proxy IP in the United States to obtain cookies, otherwise the request will
    not be made normally.
    - Users need to use a proxy IP in the United States for requests, otherwise the request will not be
    made normally.
    ### User guidelines and responsibilities:
    - Please do not use interactive interfaces to harass others, or engage in illegal or irregular
    operations, otherwise we will stop providing services to you, and all responsibilities will be borne
    by you.
    - Please do not share the interface permission with others, otherwise we will stop providing
    services to you.
    - The interface request is currently set to 5 requests per second.
    ### Return:
    - Application results and the invitation code applied for, please keep the invitation code for
    subsequent use.

    # [示例/Example]
    ```python
    # Python Code
    invite_code = \"Your_Invite_Code\"
    ```

    Args:
        api_key (str):
        invite_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        invite_code=invite_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: str,
    invite_code: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)

     # [通知]
    - 此接口已经废弃，用户现在无需手动申请调用权限，只需要在用户后台更新API Key的对应权限即可，即API Key对应的的Scope。
    # [中文]
    ### 接口用途:
    - 申请使用TikTok交互API的接口权限（Scope），请在使用交互类接口之前申请，否则将无法正常请求。
    ### 申请流程:
    - 申请接口权限需要邀请码，如果你没有邀请码，可以在Discord服务器中联系管理员获取。
    - Discord服务器链接: [TikHub Discord](https://discord.gg/aMEAS8Xsvz)
    ### 申请须知:
    - 此权限仅限于当前提交的API Key，不可跨API Key使用。
    - 用户需要使用美国地区注册且有效的的TikTok账号进行登录，否则保证将无法正常请求。
    - 用户需要使用美国地区的代理IP进行获取Cookie，否则将保证无法正常请求。
    - 用户需要使用美国地区的代理IP进行请求，否则将无法保证正常请求。
    ### 用户守则以及责任:
    - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。
    - 请不要将接口权限分享给他人，否则我们将会停止对你的服务。
    - 接口请求目前暂时定为每秒5次请求。
    ### 返回:
    - 申请结果以及申请的邀请码，请自行保留邀请码，以便后续使用。

    # [Notice]
    - This interface has been deprecated, users no longer need to apply for permission to call the API,
    just update the corresponding permission of the API Key in the user background, that is, the Scope
    corresponding to the API Key.
    # [English]
    ### Purpose:
    - Apply for the interface permission (Scope) of TikTok Interaction API, please apply before using
    the interactive interface, otherwise the request will not be made normally.
    ### Application process:
    - Applying for interface permissions requires an invitation code, if you do not have an invitation
    code, you can contact the administrator on the Discord server.
    - Discord server link: [TikHub Discord](https://discord.gg/aMEAS8Xsvz)
    ### Application notes:
    - This permission is limited to the API Key submitted, and cannot be used across API Keys.
    - Users need to log in with a registered and valid TikTok account in the United States, otherwise
    the request will not be made normally.
    - Users need to use a proxy IP in the United States to obtain cookies, otherwise the request will
    not be made normally.
    - Users need to use a proxy IP in the United States for requests, otherwise the request will not be
    made normally.
    ### User guidelines and responsibilities:
    - Please do not use interactive interfaces to harass others, or engage in illegal or irregular
    operations, otherwise we will stop providing services to you, and all responsibilities will be borne
    by you.
    - Please do not share the interface permission with others, otherwise we will stop providing
    services to you.
    - The interface request is currently set to 5 requests per second.
    ### Return:
    - Application results and the invitation code applied for, please keep the invitation code for
    subsequent use.

    # [示例/Example]
    ```python
    # Python Code
    invite_code = \"Your_Invite_Code\"
    ```

    Args:
        api_key (str):
        invite_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        api_key=api_key,
        invite_code=invite_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: str,
    invite_code: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)

     # [通知]
    - 此接口已经废弃，用户现在无需手动申请调用权限，只需要在用户后台更新API Key的对应权限即可，即API Key对应的的Scope。
    # [中文]
    ### 接口用途:
    - 申请使用TikTok交互API的接口权限（Scope），请在使用交互类接口之前申请，否则将无法正常请求。
    ### 申请流程:
    - 申请接口权限需要邀请码，如果你没有邀请码，可以在Discord服务器中联系管理员获取。
    - Discord服务器链接: [TikHub Discord](https://discord.gg/aMEAS8Xsvz)
    ### 申请须知:
    - 此权限仅限于当前提交的API Key，不可跨API Key使用。
    - 用户需要使用美国地区注册且有效的的TikTok账号进行登录，否则保证将无法正常请求。
    - 用户需要使用美国地区的代理IP进行获取Cookie，否则将保证无法正常请求。
    - 用户需要使用美国地区的代理IP进行请求，否则将无法保证正常请求。
    ### 用户守则以及责任:
    - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。
    - 请不要将接口权限分享给他人，否则我们将会停止对你的服务。
    - 接口请求目前暂时定为每秒5次请求。
    ### 返回:
    - 申请结果以及申请的邀请码，请自行保留邀请码，以便后续使用。

    # [Notice]
    - This interface has been deprecated, users no longer need to apply for permission to call the API,
    just update the corresponding permission of the API Key in the user background, that is, the Scope
    corresponding to the API Key.
    # [English]
    ### Purpose:
    - Apply for the interface permission (Scope) of TikTok Interaction API, please apply before using
    the interactive interface, otherwise the request will not be made normally.
    ### Application process:
    - Applying for interface permissions requires an invitation code, if you do not have an invitation
    code, you can contact the administrator on the Discord server.
    - Discord server link: [TikHub Discord](https://discord.gg/aMEAS8Xsvz)
    ### Application notes:
    - This permission is limited to the API Key submitted, and cannot be used across API Keys.
    - Users need to log in with a registered and valid TikTok account in the United States, otherwise
    the request will not be made normally.
    - Users need to use a proxy IP in the United States to obtain cookies, otherwise the request will
    not be made normally.
    - Users need to use a proxy IP in the United States for requests, otherwise the request will not be
    made normally.
    ### User guidelines and responsibilities:
    - Please do not use interactive interfaces to harass others, or engage in illegal or irregular
    operations, otherwise we will stop providing services to you, and all responsibilities will be borne
    by you.
    - Please do not share the interface permission with others, otherwise we will stop providing
    services to you.
    - The interface request is currently set to 5 requests per second.
    ### Return:
    - Application results and the invitation code applied for, please keep the invitation code for
    subsequent use.

    # [示例/Example]
    ```python
    # Python Code
    invite_code = \"Your_Invite_Code\"
    ```

    Args:
        api_key (str):
        invite_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        invite_code=invite_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    api_key: str,
    invite_code: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)

     # [通知]
    - 此接口已经废弃，用户现在无需手动申请调用权限，只需要在用户后台更新API Key的对应权限即可，即API Key对应的的Scope。
    # [中文]
    ### 接口用途:
    - 申请使用TikTok交互API的接口权限（Scope），请在使用交互类接口之前申请，否则将无法正常请求。
    ### 申请流程:
    - 申请接口权限需要邀请码，如果你没有邀请码，可以在Discord服务器中联系管理员获取。
    - Discord服务器链接: [TikHub Discord](https://discord.gg/aMEAS8Xsvz)
    ### 申请须知:
    - 此权限仅限于当前提交的API Key，不可跨API Key使用。
    - 用户需要使用美国地区注册且有效的的TikTok账号进行登录，否则保证将无法正常请求。
    - 用户需要使用美国地区的代理IP进行获取Cookie，否则将保证无法正常请求。
    - 用户需要使用美国地区的代理IP进行请求，否则将无法保证正常请求。
    ### 用户守则以及责任:
    - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。
    - 请不要将接口权限分享给他人，否则我们将会停止对你的服务。
    - 接口请求目前暂时定为每秒5次请求。
    ### 返回:
    - 申请结果以及申请的邀请码，请自行保留邀请码，以便后续使用。

    # [Notice]
    - This interface has been deprecated, users no longer need to apply for permission to call the API,
    just update the corresponding permission of the API Key in the user background, that is, the Scope
    corresponding to the API Key.
    # [English]
    ### Purpose:
    - Apply for the interface permission (Scope) of TikTok Interaction API, please apply before using
    the interactive interface, otherwise the request will not be made normally.
    ### Application process:
    - Applying for interface permissions requires an invitation code, if you do not have an invitation
    code, you can contact the administrator on the Discord server.
    - Discord server link: [TikHub Discord](https://discord.gg/aMEAS8Xsvz)
    ### Application notes:
    - This permission is limited to the API Key submitted, and cannot be used across API Keys.
    - Users need to log in with a registered and valid TikTok account in the United States, otherwise
    the request will not be made normally.
    - Users need to use a proxy IP in the United States to obtain cookies, otherwise the request will
    not be made normally.
    - Users need to use a proxy IP in the United States for requests, otherwise the request will not be
    made normally.
    ### User guidelines and responsibilities:
    - Please do not use interactive interfaces to harass others, or engage in illegal or irregular
    operations, otherwise we will stop providing services to you, and all responsibilities will be borne
    by you.
    - Please do not share the interface permission with others, otherwise we will stop providing
    services to you.
    - The interface request is currently set to 5 requests per second.
    ### Return:
    - Application results and the invitation code applied for, please keep the invitation code for
    subsequent use.

    # [示例/Example]
    ```python
    # Python Code
    invite_code = \"Your_Invite_Code\"
    ```

    Args:
        api_key (str):
        invite_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
            invite_code=invite_code,
        )
    ).parsed
