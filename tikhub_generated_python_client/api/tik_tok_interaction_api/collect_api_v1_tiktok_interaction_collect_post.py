from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collect_request import CollectRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: CollectRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/interaction/collect",
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
    body: CollectRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""收藏/Collect

     # [中文]
    ### 用途:
    - 使用用户Cookie收藏指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。
    ### 注意:
    - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。
    - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。
    - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。
    - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。
    ### 参数:
    - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295
    - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。
    - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。
    - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。
    - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：
        - 代理IP:端口
        - 用户名:密码@代理IP:端口
    ### 返回:
    - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。

    # [English]
    ### Purpose:
    - Collect a specified video using user cookies, please try to use TikTok accounts in the United
    States as much as possible, and use proxy IPs in the United States when obtaining cookies.
    ### Note:
    - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is
    valid, otherwise the request will not be made normally.
    - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and
    it is recommended to use proxy IPs for requests.
    - The final result of the interactive interface may be affected by the TikTok risk control system,
    and in most cases it is related to the account you are using, for example, a newly registered
    account may not be able to follow users or like videos, and we cannot handle risk control issues
    based on accounts.
    - Please do not use interactive interfaces to harass others, or engage in illegal or irregular
    operations, otherwise we will stop providing services to you, and all responsibilities will be borne
    by you.
    ### Parameters:
    - aweme_id: Video id, which can be obtained from the sharing link, for example:
    https://www.tiktok.com/@username/video/7419966340443819295
    - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie
    information, please use URL-encoded Cookie string when submitting.
    - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need
    to customize the device id, please use the device information interface to get the device id.
    - iid: Device install id, optional, if not filled in, it will be automatically generated, if you
    need to customize the device iid, please use the device information interface to get the device iid.
    - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not
    recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or
    bans, support the following formats:
        - Proxy IP:Port
        - Username:Password@Proxy IP:Port
    ### Return:
    - Like results, comment data and device information, please keep the device information, such as the
    `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent
    replacement of device information may cause account exceptions or bans.

    # [示例/Example]
    ```python
    # Python Code
    cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\")
    payload = {
        \"aweme_id\": \"7419966340443819295\",
        \"cookie\": cookie,
        \"proxy\": \"\",
    }
    ```

    Args:
        body (CollectRequest):

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
    body: CollectRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""收藏/Collect

     # [中文]
    ### 用途:
    - 使用用户Cookie收藏指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。
    ### 注意:
    - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。
    - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。
    - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。
    - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。
    ### 参数:
    - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295
    - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。
    - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。
    - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。
    - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：
        - 代理IP:端口
        - 用户名:密码@代理IP:端口
    ### 返回:
    - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。

    # [English]
    ### Purpose:
    - Collect a specified video using user cookies, please try to use TikTok accounts in the United
    States as much as possible, and use proxy IPs in the United States when obtaining cookies.
    ### Note:
    - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is
    valid, otherwise the request will not be made normally.
    - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and
    it is recommended to use proxy IPs for requests.
    - The final result of the interactive interface may be affected by the TikTok risk control system,
    and in most cases it is related to the account you are using, for example, a newly registered
    account may not be able to follow users or like videos, and we cannot handle risk control issues
    based on accounts.
    - Please do not use interactive interfaces to harass others, or engage in illegal or irregular
    operations, otherwise we will stop providing services to you, and all responsibilities will be borne
    by you.
    ### Parameters:
    - aweme_id: Video id, which can be obtained from the sharing link, for example:
    https://www.tiktok.com/@username/video/7419966340443819295
    - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie
    information, please use URL-encoded Cookie string when submitting.
    - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need
    to customize the device id, please use the device information interface to get the device id.
    - iid: Device install id, optional, if not filled in, it will be automatically generated, if you
    need to customize the device iid, please use the device information interface to get the device iid.
    - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not
    recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or
    bans, support the following formats:
        - Proxy IP:Port
        - Username:Password@Proxy IP:Port
    ### Return:
    - Like results, comment data and device information, please keep the device information, such as the
    `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent
    replacement of device information may cause account exceptions or bans.

    # [示例/Example]
    ```python
    # Python Code
    cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\")
    payload = {
        \"aweme_id\": \"7419966340443819295\",
        \"cookie\": cookie,
        \"proxy\": \"\",
    }
    ```

    Args:
        body (CollectRequest):

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
    body: CollectRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""收藏/Collect

     # [中文]
    ### 用途:
    - 使用用户Cookie收藏指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。
    ### 注意:
    - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。
    - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。
    - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。
    - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。
    ### 参数:
    - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295
    - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。
    - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。
    - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。
    - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：
        - 代理IP:端口
        - 用户名:密码@代理IP:端口
    ### 返回:
    - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。

    # [English]
    ### Purpose:
    - Collect a specified video using user cookies, please try to use TikTok accounts in the United
    States as much as possible, and use proxy IPs in the United States when obtaining cookies.
    ### Note:
    - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is
    valid, otherwise the request will not be made normally.
    - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and
    it is recommended to use proxy IPs for requests.
    - The final result of the interactive interface may be affected by the TikTok risk control system,
    and in most cases it is related to the account you are using, for example, a newly registered
    account may not be able to follow users or like videos, and we cannot handle risk control issues
    based on accounts.
    - Please do not use interactive interfaces to harass others, or engage in illegal or irregular
    operations, otherwise we will stop providing services to you, and all responsibilities will be borne
    by you.
    ### Parameters:
    - aweme_id: Video id, which can be obtained from the sharing link, for example:
    https://www.tiktok.com/@username/video/7419966340443819295
    - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie
    information, please use URL-encoded Cookie string when submitting.
    - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need
    to customize the device id, please use the device information interface to get the device id.
    - iid: Device install id, optional, if not filled in, it will be automatically generated, if you
    need to customize the device iid, please use the device information interface to get the device iid.
    - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not
    recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or
    bans, support the following formats:
        - Proxy IP:Port
        - Username:Password@Proxy IP:Port
    ### Return:
    - Like results, comment data and device information, please keep the device information, such as the
    `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent
    replacement of device information may cause account exceptions or bans.

    # [示例/Example]
    ```python
    # Python Code
    cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\")
    payload = {
        \"aweme_id\": \"7419966340443819295\",
        \"cookie\": cookie,
        \"proxy\": \"\",
    }
    ```

    Args:
        body (CollectRequest):

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
    body: CollectRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""收藏/Collect

     # [中文]
    ### 用途:
    - 使用用户Cookie收藏指定视频，当前请尽可能使用美国地区的TikTok账号，并且在获取Cookie时请使用美国地区的代理IP。
    ### 注意:
    - 交互类接口都需要使用用户的Cookie，因此请确保你的Cookie是有效的，否则将无法正常请求。
    - 交互类的接口可能会导致账号异常或封禁，因此请谨慎使用，建议使用代理IP进行请求。
    - 交互类接口的最终结果可能会受到TikTok风控系统的影响，大多数情况跟你所使用的账号有关，比如新注册的账号可能无法关注用户或点赞视频，我们无法处理基于账号的风控问题。
    - 请不要使用交互类接口对他人造成骚扰，或进行违法违规的操作，否则我们将会停止对你的服务，并且所有责任由你自己承担。
    ### 参数:
    - aweme_id: 视频id，可以从分享链接中获取，例如：https://www.tiktok.com/@username/video/7419966340443819295
    - cookie: 用户Cookie，可以从浏览器中登录自己的TikTok账号，然后复制Cookie信息，提交时请使用URL编码Cookie字符串。
    - device_id: 设备id，可选，如果不填写则会自动生成，如果需要自定义设备id，请使用设备信息接口获取设备id。
    - iid: 设备安装id，可选，如果不填写则会自动生成，如果需要自定义设备iid，请使用设备信息接口获取设备iid。
    - proxy: 代理IP，可选，如果不填写则会使用服务器IP进行请求（不推荐），建议使用代理IP进行请求防止账号异常获被封禁，支持格式如下：
        - 代理IP:端口
        - 用户名:密码@代理IP:端口
    ### 返回:
    - 点赞结果以及评论数据和设备信息，请自行保留设备信息，如请求时使用的`device_id`以及`iid`，以便后续调用接口时使用，频繁更换设备信息可能会导致账号异常或封禁。

    # [English]
    ### Purpose:
    - Collect a specified video using user cookies, please try to use TikTok accounts in the United
    States as much as possible, and use proxy IPs in the United States when obtaining cookies.
    ### Note:
    - Interactive interfaces all need to use the user's Cookie, so please make sure that your Cookie is
    valid, otherwise the request will not be made normally.
    - Interactive interfaces may cause account exceptions or bans, so please use them with caution, and
    it is recommended to use proxy IPs for requests.
    - The final result of the interactive interface may be affected by the TikTok risk control system,
    and in most cases it is related to the account you are using, for example, a newly registered
    account may not be able to follow users or like videos, and we cannot handle risk control issues
    based on accounts.
    - Please do not use interactive interfaces to harass others, or engage in illegal or irregular
    operations, otherwise we will stop providing services to you, and all responsibilities will be borne
    by you.
    ### Parameters:
    - aweme_id: Video id, which can be obtained from the sharing link, for example:
    https://www.tiktok.com/@username/video/7419966340443819295
    - cookie: User Cookie, you can log in to your TikTok account in the browser and then copy the Cookie
    information, please use URL-encoded Cookie string when submitting.
    - device_id: Device id, optional, if not filled in, it will be automatically generated, if you need
    to customize the device id, please use the device information interface to get the device id.
    - iid: Device install id, optional, if not filled in, it will be automatically generated, if you
    need to customize the device iid, please use the device information interface to get the device iid.
    - proxy: Proxy IP, optional, if not filled in, the server IP will be used for the request (not
    recommended), it is recommended to use a proxy IP for the request to prevent account exceptions or
    bans, support the following formats:
        - Proxy IP:Port
        - Username:Password@Proxy IP:Port
    ### Return:
    - Like results, comment data and device information, please keep the device information, such as the
    `device_id` and `iid` used when requesting, for subsequent calls to the interface, frequent
    replacement of device information may cause account exceptions or bans.

    # [示例/Example]
    ```python
    # Python Code
    cookie = urllib.parse.quote(\"Your_Cookie_From_Browser\")
    payload = {
        \"aweme_id\": \"7419966340443819295\",
        \"cookie\": cookie,
        \"proxy\": \"\",
    }
    ```

    Args:
        body (CollectRequest):

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
