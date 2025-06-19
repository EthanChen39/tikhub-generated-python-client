from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.xhs_web_sign_request_model import XhsWebSignRequestModel
from ...types import Response


def _get_kwargs(
    *,
    body: XhsWebSignRequestModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/xiaohongshu/web/sign",
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
    body: XhsWebSignRequestModel,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""小红书Web签名/Xiaohongshu Web sign

     # [中文]
    ### 用途:
    - 小红书Web签名，用于获取小红书的一些数据。
    - 生成 `X-s`, `X-t`, `X-s-common` 等签名参数。
    - 价格：0.001$/次
    ### 参数:
    - sign_request: 签名请求模型
        - path: 请求接口的路径，例如: `/api/sns/web/v1/homefeed`
        - data: 请求API的荷载数据
        - cookie: 请求接口的Cookie
    ### 返回:
    - 签名参数(X-s, X-t, X-s-common等)

    # [English]
    ### Purpose:
    - Xiaohongshu Web sign, used to get some data of Xiaohongshu.
    - Generate `X-s`, `X-t`, `X-s-common` and other signature parameters.
    - Price: 0.001$/time
    ### Parameters:
    - sign_request: Sign request model
        - path: Request API path, e.g. `/api/sns/web/v1/homefeed`
        - data: Payload data of request API
        - cookie: Request API cookie
    ### Return:
    - Signature parameters(X-s, X-t, X-s-common, etc.)

    # [示例/Example]
    {
        \"path\": \"/api/sns/web/v1/homefeed\",
        \"data\": {
            \"cursor_score\": \"\",
            \"num\": 35,
            \"refresh_type\": 1,
            \"note_index\": 35,
            \"unread_begin_note_id\": \"\",
            \"unread_end_note_id\": \"\",
            \"unread_note_count\": 0,
            \"category\": \"homefeed_recommend\",
            \"search_key\": \"\",
            \"need_num\": 10,
            \"image_formats\": [
                \"jpg\",
                \"webp\",
                \"avif\"
            ],
            \"need_filter_image\": False
        },
        \"cookie\": \"web_session=030037a04eafd37791e6e4bd05204a8cf2af05;acw_tc=0a00d79f1736309667934583
    8efb77751cc087fb039dd1691dc954824410f6;abRequestId=384480ae-5196-5818-a835-
    42e6278de9f0;webBuild=4.47.1;xsecappid=xhs-pc-web;a1=194441ef694PayUbdUvgp0dSHfIcACsNsLud0Lgru500003
    54513;webId=6cf10a564b9b07d129729b65e0d1785a;sec_poison_id=32964532-d414-4beb-914f-98811853b75f\"
    }

    Args:
        body (XhsWebSignRequestModel):

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
    body: XhsWebSignRequestModel,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""小红书Web签名/Xiaohongshu Web sign

     # [中文]
    ### 用途:
    - 小红书Web签名，用于获取小红书的一些数据。
    - 生成 `X-s`, `X-t`, `X-s-common` 等签名参数。
    - 价格：0.001$/次
    ### 参数:
    - sign_request: 签名请求模型
        - path: 请求接口的路径，例如: `/api/sns/web/v1/homefeed`
        - data: 请求API的荷载数据
        - cookie: 请求接口的Cookie
    ### 返回:
    - 签名参数(X-s, X-t, X-s-common等)

    # [English]
    ### Purpose:
    - Xiaohongshu Web sign, used to get some data of Xiaohongshu.
    - Generate `X-s`, `X-t`, `X-s-common` and other signature parameters.
    - Price: 0.001$/time
    ### Parameters:
    - sign_request: Sign request model
        - path: Request API path, e.g. `/api/sns/web/v1/homefeed`
        - data: Payload data of request API
        - cookie: Request API cookie
    ### Return:
    - Signature parameters(X-s, X-t, X-s-common, etc.)

    # [示例/Example]
    {
        \"path\": \"/api/sns/web/v1/homefeed\",
        \"data\": {
            \"cursor_score\": \"\",
            \"num\": 35,
            \"refresh_type\": 1,
            \"note_index\": 35,
            \"unread_begin_note_id\": \"\",
            \"unread_end_note_id\": \"\",
            \"unread_note_count\": 0,
            \"category\": \"homefeed_recommend\",
            \"search_key\": \"\",
            \"need_num\": 10,
            \"image_formats\": [
                \"jpg\",
                \"webp\",
                \"avif\"
            ],
            \"need_filter_image\": False
        },
        \"cookie\": \"web_session=030037a04eafd37791e6e4bd05204a8cf2af05;acw_tc=0a00d79f1736309667934583
    8efb77751cc087fb039dd1691dc954824410f6;abRequestId=384480ae-5196-5818-a835-
    42e6278de9f0;webBuild=4.47.1;xsecappid=xhs-pc-web;a1=194441ef694PayUbdUvgp0dSHfIcACsNsLud0Lgru500003
    54513;webId=6cf10a564b9b07d129729b65e0d1785a;sec_poison_id=32964532-d414-4beb-914f-98811853b75f\"
    }

    Args:
        body (XhsWebSignRequestModel):

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
    body: XhsWebSignRequestModel,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""小红书Web签名/Xiaohongshu Web sign

     # [中文]
    ### 用途:
    - 小红书Web签名，用于获取小红书的一些数据。
    - 生成 `X-s`, `X-t`, `X-s-common` 等签名参数。
    - 价格：0.001$/次
    ### 参数:
    - sign_request: 签名请求模型
        - path: 请求接口的路径，例如: `/api/sns/web/v1/homefeed`
        - data: 请求API的荷载数据
        - cookie: 请求接口的Cookie
    ### 返回:
    - 签名参数(X-s, X-t, X-s-common等)

    # [English]
    ### Purpose:
    - Xiaohongshu Web sign, used to get some data of Xiaohongshu.
    - Generate `X-s`, `X-t`, `X-s-common` and other signature parameters.
    - Price: 0.001$/time
    ### Parameters:
    - sign_request: Sign request model
        - path: Request API path, e.g. `/api/sns/web/v1/homefeed`
        - data: Payload data of request API
        - cookie: Request API cookie
    ### Return:
    - Signature parameters(X-s, X-t, X-s-common, etc.)

    # [示例/Example]
    {
        \"path\": \"/api/sns/web/v1/homefeed\",
        \"data\": {
            \"cursor_score\": \"\",
            \"num\": 35,
            \"refresh_type\": 1,
            \"note_index\": 35,
            \"unread_begin_note_id\": \"\",
            \"unread_end_note_id\": \"\",
            \"unread_note_count\": 0,
            \"category\": \"homefeed_recommend\",
            \"search_key\": \"\",
            \"need_num\": 10,
            \"image_formats\": [
                \"jpg\",
                \"webp\",
                \"avif\"
            ],
            \"need_filter_image\": False
        },
        \"cookie\": \"web_session=030037a04eafd37791e6e4bd05204a8cf2af05;acw_tc=0a00d79f1736309667934583
    8efb77751cc087fb039dd1691dc954824410f6;abRequestId=384480ae-5196-5818-a835-
    42e6278de9f0;webBuild=4.47.1;xsecappid=xhs-pc-web;a1=194441ef694PayUbdUvgp0dSHfIcACsNsLud0Lgru500003
    54513;webId=6cf10a564b9b07d129729b65e0d1785a;sec_poison_id=32964532-d414-4beb-914f-98811853b75f\"
    }

    Args:
        body (XhsWebSignRequestModel):

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
    body: XhsWebSignRequestModel,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""小红书Web签名/Xiaohongshu Web sign

     # [中文]
    ### 用途:
    - 小红书Web签名，用于获取小红书的一些数据。
    - 生成 `X-s`, `X-t`, `X-s-common` 等签名参数。
    - 价格：0.001$/次
    ### 参数:
    - sign_request: 签名请求模型
        - path: 请求接口的路径，例如: `/api/sns/web/v1/homefeed`
        - data: 请求API的荷载数据
        - cookie: 请求接口的Cookie
    ### 返回:
    - 签名参数(X-s, X-t, X-s-common等)

    # [English]
    ### Purpose:
    - Xiaohongshu Web sign, used to get some data of Xiaohongshu.
    - Generate `X-s`, `X-t`, `X-s-common` and other signature parameters.
    - Price: 0.001$/time
    ### Parameters:
    - sign_request: Sign request model
        - path: Request API path, e.g. `/api/sns/web/v1/homefeed`
        - data: Payload data of request API
        - cookie: Request API cookie
    ### Return:
    - Signature parameters(X-s, X-t, X-s-common, etc.)

    # [示例/Example]
    {
        \"path\": \"/api/sns/web/v1/homefeed\",
        \"data\": {
            \"cursor_score\": \"\",
            \"num\": 35,
            \"refresh_type\": 1,
            \"note_index\": 35,
            \"unread_begin_note_id\": \"\",
            \"unread_end_note_id\": \"\",
            \"unread_note_count\": 0,
            \"category\": \"homefeed_recommend\",
            \"search_key\": \"\",
            \"need_num\": 10,
            \"image_formats\": [
                \"jpg\",
                \"webp\",
                \"avif\"
            ],
            \"need_filter_image\": False
        },
        \"cookie\": \"web_session=030037a04eafd37791e6e4bd05204a8cf2af05;acw_tc=0a00d79f1736309667934583
    8efb77751cc087fb039dd1691dc954824410f6;abRequestId=384480ae-5196-5818-a835-
    42e6278de9f0;webBuild=4.47.1;xsecappid=xhs-pc-web;a1=194441ef694PayUbdUvgp0dSHfIcACsNsLud0Lgru500003
    54513;webId=6cf10a564b9b07d129729b65e0d1785a;sec_poison_id=32964532-d414-4beb-914f-98811853b75f\"
    }

    Args:
        body (XhsWebSignRequestModel):

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
