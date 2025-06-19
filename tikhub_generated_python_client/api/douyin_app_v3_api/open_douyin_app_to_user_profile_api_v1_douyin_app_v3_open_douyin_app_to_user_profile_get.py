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
    uid: str,
    sec_uid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["uid"] = uid

    params["sec_uid"] = sec_uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/open_douyin_app_to_user_profile",
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
    uid: str,
    sec_uid: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified
    user profile

     # [中文]
    ### 用途:
    - 生成抖音分享链接，唤起抖音APP，跳转指定用户主页。

    ### 参数:
    - uid: 用户id
    - sec_uid: 用户sec_uid
    - 注意: 请确保user_id和sec_uid都有值，否则无法跳转到指定用户主页。

    ### 返回:
    - 分享链接

    # [English]
    ### Purpose:
    - Generate Douyin share link, call Douyin APP, and jump to the specified user profile

    ### Parameters:
    - uid: User id
    - sec_uid: User sec_uid
    - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot jump to the
    specified user profile.

    ### Return:
    - Share link

    # [示例/Example]
    uid = \"96874812426\"
    sec_uid = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"

    Args:
        uid (str): 用户id/User id
        sec_uid (str): 用户sec_uid/User sec_uid

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        sec_uid=sec_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    uid: str,
    sec_uid: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified
    user profile

     # [中文]
    ### 用途:
    - 生成抖音分享链接，唤起抖音APP，跳转指定用户主页。

    ### 参数:
    - uid: 用户id
    - sec_uid: 用户sec_uid
    - 注意: 请确保user_id和sec_uid都有值，否则无法跳转到指定用户主页。

    ### 返回:
    - 分享链接

    # [English]
    ### Purpose:
    - Generate Douyin share link, call Douyin APP, and jump to the specified user profile

    ### Parameters:
    - uid: User id
    - sec_uid: User sec_uid
    - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot jump to the
    specified user profile.

    ### Return:
    - Share link

    # [示例/Example]
    uid = \"96874812426\"
    sec_uid = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"

    Args:
        uid (str): 用户id/User id
        sec_uid (str): 用户sec_uid/User sec_uid

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        uid=uid,
        sec_uid=sec_uid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    uid: str,
    sec_uid: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified
    user profile

     # [中文]
    ### 用途:
    - 生成抖音分享链接，唤起抖音APP，跳转指定用户主页。

    ### 参数:
    - uid: 用户id
    - sec_uid: 用户sec_uid
    - 注意: 请确保user_id和sec_uid都有值，否则无法跳转到指定用户主页。

    ### 返回:
    - 分享链接

    # [English]
    ### Purpose:
    - Generate Douyin share link, call Douyin APP, and jump to the specified user profile

    ### Parameters:
    - uid: User id
    - sec_uid: User sec_uid
    - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot jump to the
    specified user profile.

    ### Return:
    - Share link

    # [示例/Example]
    uid = \"96874812426\"
    sec_uid = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"

    Args:
        uid (str): 用户id/User id
        sec_uid (str): 用户sec_uid/User sec_uid

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        sec_uid=sec_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    uid: str,
    sec_uid: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified
    user profile

     # [中文]
    ### 用途:
    - 生成抖音分享链接，唤起抖音APP，跳转指定用户主页。

    ### 参数:
    - uid: 用户id
    - sec_uid: 用户sec_uid
    - 注意: 请确保user_id和sec_uid都有值，否则无法跳转到指定用户主页。

    ### 返回:
    - 分享链接

    # [English]
    ### Purpose:
    - Generate Douyin share link, call Douyin APP, and jump to the specified user profile

    ### Parameters:
    - uid: User id
    - sec_uid: User sec_uid
    - Note: Please make sure that both user_id and sec_uid have values, otherwise you cannot jump to the
    specified user profile.

    ### Return:
    - Share link

    # [示例/Example]
    uid = \"96874812426\"
    sec_uid = \"MS4wLjABAAAA9y04iBlVdeMQqTJbqsQZKb-tqWqWW29jPVJqideHT70\"

    Args:
        uid (str): 用户id/User id
        sec_uid (str): 用户sec_uid/User sec_uid

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            uid=uid,
            sec_uid=sec_uid,
        )
    ).parsed
