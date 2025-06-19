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
    body: list[str],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/web/get_all_webcast_id",
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
    body: list[str],
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""提取列表直播间号/Extract list webcast id

     # [中文]
    ### 用途:
    - 提取列表直播间号
    ### 参数:
    - url: 直播间链接列表（最多支持20个链接）
    ### 返回:
    - 直播间号列表

    # [English]
    ### Purpose:
    - Extract list webcast id
    ### Parameters:
    - url: Room link list (supports up to 20 links)
    ### Return:
    - Room id list

    # [示例/Example]
    ```json
    {
      \"urls\": [
            \"https://live.douyin.com/775841227732\",
            \"https://live.douyin.com/775841227732?room_id=7318296342189919011&enter_from_merge=web_shar
    e_link&enter_method=web_share_link&previous_page=app_code_link\",
            'https://webcast.amemv.com/douyin/webcast/reflow/7318296342189919011?u_code=l1j9bkbd&did=MS4
    wLjABAAAAEs86TBQPNwAo-RGrcxWyCdwKhI66AK3Pqf3ieo6HaxI&iid=MS4wLjABAAAA0ptpM-zzoliLEeyvWOCUt-_dQza4uSj
    lIvbtIazXnCY&with_sec_did=1&use_link_command=1&ecom_share_track_params=&extra_params={\"from_request
    _id\":\"20231230162057EC005772A8EAA0199906\",\"im_channel_invite_id\":\"0\"}&user_id=364420789804220
    6&liveId=7318296342189919011&from=share&style=share&enter_method=click_share&roomId=7318296342189919
    011&activity_info={}',
            \"6i- Q@x.Sl 03/23 【醒子8ke的直播间】  点击打开👉https://v.douyin.com/i8tBR7hX/  或长按复制此条消息，打开抖音，看TA直播\",
            \"https://v.douyin.com/i8tBR7hX/\",
            ]
    }
    ```

    Args:
        body (list[str]): 直播间链接列表/Room link list

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
    body: list[str],
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""提取列表直播间号/Extract list webcast id

     # [中文]
    ### 用途:
    - 提取列表直播间号
    ### 参数:
    - url: 直播间链接列表（最多支持20个链接）
    ### 返回:
    - 直播间号列表

    # [English]
    ### Purpose:
    - Extract list webcast id
    ### Parameters:
    - url: Room link list (supports up to 20 links)
    ### Return:
    - Room id list

    # [示例/Example]
    ```json
    {
      \"urls\": [
            \"https://live.douyin.com/775841227732\",
            \"https://live.douyin.com/775841227732?room_id=7318296342189919011&enter_from_merge=web_shar
    e_link&enter_method=web_share_link&previous_page=app_code_link\",
            'https://webcast.amemv.com/douyin/webcast/reflow/7318296342189919011?u_code=l1j9bkbd&did=MS4
    wLjABAAAAEs86TBQPNwAo-RGrcxWyCdwKhI66AK3Pqf3ieo6HaxI&iid=MS4wLjABAAAA0ptpM-zzoliLEeyvWOCUt-_dQza4uSj
    lIvbtIazXnCY&with_sec_did=1&use_link_command=1&ecom_share_track_params=&extra_params={\"from_request
    _id\":\"20231230162057EC005772A8EAA0199906\",\"im_channel_invite_id\":\"0\"}&user_id=364420789804220
    6&liveId=7318296342189919011&from=share&style=share&enter_method=click_share&roomId=7318296342189919
    011&activity_info={}',
            \"6i- Q@x.Sl 03/23 【醒子8ke的直播间】  点击打开👉https://v.douyin.com/i8tBR7hX/  或长按复制此条消息，打开抖音，看TA直播\",
            \"https://v.douyin.com/i8tBR7hX/\",
            ]
    }
    ```

    Args:
        body (list[str]): 直播间链接列表/Room link list

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
    body: list[str],
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""提取列表直播间号/Extract list webcast id

     # [中文]
    ### 用途:
    - 提取列表直播间号
    ### 参数:
    - url: 直播间链接列表（最多支持20个链接）
    ### 返回:
    - 直播间号列表

    # [English]
    ### Purpose:
    - Extract list webcast id
    ### Parameters:
    - url: Room link list (supports up to 20 links)
    ### Return:
    - Room id list

    # [示例/Example]
    ```json
    {
      \"urls\": [
            \"https://live.douyin.com/775841227732\",
            \"https://live.douyin.com/775841227732?room_id=7318296342189919011&enter_from_merge=web_shar
    e_link&enter_method=web_share_link&previous_page=app_code_link\",
            'https://webcast.amemv.com/douyin/webcast/reflow/7318296342189919011?u_code=l1j9bkbd&did=MS4
    wLjABAAAAEs86TBQPNwAo-RGrcxWyCdwKhI66AK3Pqf3ieo6HaxI&iid=MS4wLjABAAAA0ptpM-zzoliLEeyvWOCUt-_dQza4uSj
    lIvbtIazXnCY&with_sec_did=1&use_link_command=1&ecom_share_track_params=&extra_params={\"from_request
    _id\":\"20231230162057EC005772A8EAA0199906\",\"im_channel_invite_id\":\"0\"}&user_id=364420789804220
    6&liveId=7318296342189919011&from=share&style=share&enter_method=click_share&roomId=7318296342189919
    011&activity_info={}',
            \"6i- Q@x.Sl 03/23 【醒子8ke的直播间】  点击打开👉https://v.douyin.com/i8tBR7hX/  或长按复制此条消息，打开抖音，看TA直播\",
            \"https://v.douyin.com/i8tBR7hX/\",
            ]
    }
    ```

    Args:
        body (list[str]): 直播间链接列表/Room link list

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
    body: list[str],
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""提取列表直播间号/Extract list webcast id

     # [中文]
    ### 用途:
    - 提取列表直播间号
    ### 参数:
    - url: 直播间链接列表（最多支持20个链接）
    ### 返回:
    - 直播间号列表

    # [English]
    ### Purpose:
    - Extract list webcast id
    ### Parameters:
    - url: Room link list (supports up to 20 links)
    ### Return:
    - Room id list

    # [示例/Example]
    ```json
    {
      \"urls\": [
            \"https://live.douyin.com/775841227732\",
            \"https://live.douyin.com/775841227732?room_id=7318296342189919011&enter_from_merge=web_shar
    e_link&enter_method=web_share_link&previous_page=app_code_link\",
            'https://webcast.amemv.com/douyin/webcast/reflow/7318296342189919011?u_code=l1j9bkbd&did=MS4
    wLjABAAAAEs86TBQPNwAo-RGrcxWyCdwKhI66AK3Pqf3ieo6HaxI&iid=MS4wLjABAAAA0ptpM-zzoliLEeyvWOCUt-_dQza4uSj
    lIvbtIazXnCY&with_sec_did=1&use_link_command=1&ecom_share_track_params=&extra_params={\"from_request
    _id\":\"20231230162057EC005772A8EAA0199906\",\"im_channel_invite_id\":\"0\"}&user_id=364420789804220
    6&liveId=7318296342189919011&from=share&style=share&enter_method=click_share&roomId=7318296342189919
    011&activity_info={}',
            \"6i- Q@x.Sl 03/23 【醒子8ke的直播间】  点击打开👉https://v.douyin.com/i8tBR7hX/  或长按复制此条消息，打开抖音，看TA直播\",
            \"https://v.douyin.com/i8tBR7hX/\",
            ]
    }
    ```

    Args:
        body (list[str]): 直播间链接列表/Room link list

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
