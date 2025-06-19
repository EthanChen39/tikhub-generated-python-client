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
    aweme_type: int,
    item_id: str,
    cookie: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aweme_type"] = aweme_type

    params["item_id"] = item_id

    params["cookie"] = cookie

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/add_video_play_count",
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
    aweme_type: int,
    item_id: str,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID

     # [中文]
    ### 用途:
    - 根据视频ID来增加作品的播放数
    - 该接口默认使用游客Cookie，如果需要使用登录用户的Cookie，请在参数中传入。
    - 单一作品每次调用增加1次播放数，请求约 `1000` 次后会被抖音限制，需要等待一段时间（如：2小时后）后再继续调用。
    - 该限制是针对作品的，不是针对接口的，在未登录的情况下，使用不同IP的浏览器或在APP中浏览作品，该作品的播放数也不会增加。
    - 可以携带抖音网页端的Cookie来请求此接口，但是不保证一定有效，需要自行测试。
    - 上述的限制是根据测试结果得出的，具体限制可能会有所不同，仅供参考。
    ### 参数:
    - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。
    - item_id: 作品id，别名为aweme_id
    - cookie: 可选，默认使用游客Cookie
    ### 返回:
    - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。

    # [English]
    ### Purpose:
    - Increase the number of plays of the work according to the video ID
    - This interface uses guest Cookie by default. If you need to use the Cookie of the logged-in user,
    please pass it in the parameters.
    - Each call to a single work increases the number of plays by 1. After about `1000` calls, Douyin
    will restrict it. You need to wait for a period of time (such as 2 hours) before continuing to call.
    - This restriction is for the work, not for the interface. When browsing the work without logging
    in, using different IP browsers or browsing the work in the APP, the number of plays of the work
    will not increase.
    - You can carry the Cookie of the Douyin web page to request this interface, but it is not
    guaranteed to be effective and needs to be tested by yourself.
    - The above restrictions are based on test results, and the specific restrictions may vary, for
    reference only.
    ### Parameters:
    - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data
    interface.
    - item_id: Video id, alias aweme_id
    - cookie: Optional, use guest Cookie by default
    ### Return:
    - The current timestamp and status code. When the status code is 200, it means success, otherwise it
    is a failure. You can try to change another work id and call it again, or wait for a period of time
    and call it again.

    # [示例/Example]
    aweme_type = 0
    item_id = \"7197598285882789120\"
    cookie = None

    Args:
        aweme_type (int): 作品类型/Video type
        item_id (str): 作品id/Video id
        cookie (Union[Unset, str]): 可选，默认使用游客Cookie/Optional, use guest Cookie by default

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_type=aweme_type,
        item_id=item_id,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aweme_type: int,
    item_id: str,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID

     # [中文]
    ### 用途:
    - 根据视频ID来增加作品的播放数
    - 该接口默认使用游客Cookie，如果需要使用登录用户的Cookie，请在参数中传入。
    - 单一作品每次调用增加1次播放数，请求约 `1000` 次后会被抖音限制，需要等待一段时间（如：2小时后）后再继续调用。
    - 该限制是针对作品的，不是针对接口的，在未登录的情况下，使用不同IP的浏览器或在APP中浏览作品，该作品的播放数也不会增加。
    - 可以携带抖音网页端的Cookie来请求此接口，但是不保证一定有效，需要自行测试。
    - 上述的限制是根据测试结果得出的，具体限制可能会有所不同，仅供参考。
    ### 参数:
    - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。
    - item_id: 作品id，别名为aweme_id
    - cookie: 可选，默认使用游客Cookie
    ### 返回:
    - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。

    # [English]
    ### Purpose:
    - Increase the number of plays of the work according to the video ID
    - This interface uses guest Cookie by default. If you need to use the Cookie of the logged-in user,
    please pass it in the parameters.
    - Each call to a single work increases the number of plays by 1. After about `1000` calls, Douyin
    will restrict it. You need to wait for a period of time (such as 2 hours) before continuing to call.
    - This restriction is for the work, not for the interface. When browsing the work without logging
    in, using different IP browsers or browsing the work in the APP, the number of plays of the work
    will not increase.
    - You can carry the Cookie of the Douyin web page to request this interface, but it is not
    guaranteed to be effective and needs to be tested by yourself.
    - The above restrictions are based on test results, and the specific restrictions may vary, for
    reference only.
    ### Parameters:
    - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data
    interface.
    - item_id: Video id, alias aweme_id
    - cookie: Optional, use guest Cookie by default
    ### Return:
    - The current timestamp and status code. When the status code is 200, it means success, otherwise it
    is a failure. You can try to change another work id and call it again, or wait for a period of time
    and call it again.

    # [示例/Example]
    aweme_type = 0
    item_id = \"7197598285882789120\"
    cookie = None

    Args:
        aweme_type (int): 作品类型/Video type
        item_id (str): 作品id/Video id
        cookie (Union[Unset, str]): 可选，默认使用游客Cookie/Optional, use guest Cookie by default

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        aweme_type=aweme_type,
        item_id=item_id,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aweme_type: int,
    item_id: str,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID

     # [中文]
    ### 用途:
    - 根据视频ID来增加作品的播放数
    - 该接口默认使用游客Cookie，如果需要使用登录用户的Cookie，请在参数中传入。
    - 单一作品每次调用增加1次播放数，请求约 `1000` 次后会被抖音限制，需要等待一段时间（如：2小时后）后再继续调用。
    - 该限制是针对作品的，不是针对接口的，在未登录的情况下，使用不同IP的浏览器或在APP中浏览作品，该作品的播放数也不会增加。
    - 可以携带抖音网页端的Cookie来请求此接口，但是不保证一定有效，需要自行测试。
    - 上述的限制是根据测试结果得出的，具体限制可能会有所不同，仅供参考。
    ### 参数:
    - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。
    - item_id: 作品id，别名为aweme_id
    - cookie: 可选，默认使用游客Cookie
    ### 返回:
    - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。

    # [English]
    ### Purpose:
    - Increase the number of plays of the work according to the video ID
    - This interface uses guest Cookie by default. If you need to use the Cookie of the logged-in user,
    please pass it in the parameters.
    - Each call to a single work increases the number of plays by 1. After about `1000` calls, Douyin
    will restrict it. You need to wait for a period of time (such as 2 hours) before continuing to call.
    - This restriction is for the work, not for the interface. When browsing the work without logging
    in, using different IP browsers or browsing the work in the APP, the number of plays of the work
    will not increase.
    - You can carry the Cookie of the Douyin web page to request this interface, but it is not
    guaranteed to be effective and needs to be tested by yourself.
    - The above restrictions are based on test results, and the specific restrictions may vary, for
    reference only.
    ### Parameters:
    - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data
    interface.
    - item_id: Video id, alias aweme_id
    - cookie: Optional, use guest Cookie by default
    ### Return:
    - The current timestamp and status code. When the status code is 200, it means success, otherwise it
    is a failure. You can try to change another work id and call it again, or wait for a period of time
    and call it again.

    # [示例/Example]
    aweme_type = 0
    item_id = \"7197598285882789120\"
    cookie = None

    Args:
        aweme_type (int): 作品类型/Video type
        item_id (str): 作品id/Video id
        cookie (Union[Unset, str]): 可选，默认使用游客Cookie/Optional, use guest Cookie by default

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_type=aweme_type,
        item_id=item_id,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aweme_type: int,
    item_id: str,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID

     # [中文]
    ### 用途:
    - 根据视频ID来增加作品的播放数
    - 该接口默认使用游客Cookie，如果需要使用登录用户的Cookie，请在参数中传入。
    - 单一作品每次调用增加1次播放数，请求约 `1000` 次后会被抖音限制，需要等待一段时间（如：2小时后）后再继续调用。
    - 该限制是针对作品的，不是针对接口的，在未登录的情况下，使用不同IP的浏览器或在APP中浏览作品，该作品的播放数也不会增加。
    - 可以携带抖音网页端的Cookie来请求此接口，但是不保证一定有效，需要自行测试。
    - 上述的限制是根据测试结果得出的，具体限制可能会有所不同，仅供参考。
    ### 参数:
    - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。
    - item_id: 作品id，别名为aweme_id
    - cookie: 可选，默认使用游客Cookie
    ### 返回:
    - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。

    # [English]
    ### Purpose:
    - Increase the number of plays of the work according to the video ID
    - This interface uses guest Cookie by default. If you need to use the Cookie of the logged-in user,
    please pass it in the parameters.
    - Each call to a single work increases the number of plays by 1. After about `1000` calls, Douyin
    will restrict it. You need to wait for a period of time (such as 2 hours) before continuing to call.
    - This restriction is for the work, not for the interface. When browsing the work without logging
    in, using different IP browsers or browsing the work in the APP, the number of plays of the work
    will not increase.
    - You can carry the Cookie of the Douyin web page to request this interface, but it is not
    guaranteed to be effective and needs to be tested by yourself.
    - The above restrictions are based on test results, and the specific restrictions may vary, for
    reference only.
    ### Parameters:
    - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data
    interface.
    - item_id: Video id, alias aweme_id
    - cookie: Optional, use guest Cookie by default
    ### Return:
    - The current timestamp and status code. When the status code is 200, it means success, otherwise it
    is a failure. You can try to change another work id and call it again, or wait for a period of time
    and call it again.

    # [示例/Example]
    aweme_type = 0
    item_id = \"7197598285882789120\"
    cookie = None

    Args:
        aweme_type (int): 作品类型/Video type
        item_id (str): 作品id/Video id
        cookie (Union[Unset, str]): 可选，默认使用游客Cookie/Optional, use guest Cookie by default

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            aweme_type=aweme_type,
            item_id=item_id,
            cookie=cookie,
        )
    ).parsed
