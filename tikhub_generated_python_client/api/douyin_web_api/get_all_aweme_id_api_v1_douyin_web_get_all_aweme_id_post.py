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
        "url": "/api/v1/douyin/web/get_all_aweme_id",
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
    r"""提取列表作品id/Extract list video id

     # [中文]
     ### 用途:
     - 提取列表作品id（最多支持20个链接）
     ### 参数:
     - url: 作品链接列表
     ### 返回:
     - 作品id列表

     # [English]
     ### Purpose:
     - Extract list video id (supports up to 20 links)
     ### Parameters:
     - url: Video link list
     ### Return:
     - Video id list

     # [示例/Example]
     ```json
     {
    \"urls\":[
        \"0.53 02/26 I@v.sE Fus:/ 你别太帅了郑润泽# 现场版live # 音乐节 # 郑润泽  https://v.douyin.com/iRNBho6u/
    复制此链接，打开Dou音搜索，直接观看视频!\",
        \"https://v.douyin.com/iRNBho6u/\",
        \"https://www.iesdouyin.com/share/video/7298145681699622182/?region=CN&mid=7298145762238565171&u
    _code=l1j9bkbd&did=MS4wLjABAAAAtqpCx0hpOERbdSzQdjRZw-wFPxaqdbAzsKDmbJMUI3KWlMGQHC-n6dXAqa-
    dM2EP&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&sha
    re_sign=05kGlqGmR4_IwCX.ZGk6xuL0osNA..5ur7b0jbOx6cc-
    &share_version=170400&ts=1699262937&from_aid=6383&from_ssr=1&from=web_code_link\",
        \"https://www.douyin.com/video/7298145681699622182?previous_page=web_code_link\",
        \"https://www.douyin.com/video/7298145681699622182\",
     ]
     }
     ```

    Args:
        body (list[str]): 作品链接列表/Video link list

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
    r"""提取列表作品id/Extract list video id

     # [中文]
     ### 用途:
     - 提取列表作品id（最多支持20个链接）
     ### 参数:
     - url: 作品链接列表
     ### 返回:
     - 作品id列表

     # [English]
     ### Purpose:
     - Extract list video id (supports up to 20 links)
     ### Parameters:
     - url: Video link list
     ### Return:
     - Video id list

     # [示例/Example]
     ```json
     {
    \"urls\":[
        \"0.53 02/26 I@v.sE Fus:/ 你别太帅了郑润泽# 现场版live # 音乐节 # 郑润泽  https://v.douyin.com/iRNBho6u/
    复制此链接，打开Dou音搜索，直接观看视频!\",
        \"https://v.douyin.com/iRNBho6u/\",
        \"https://www.iesdouyin.com/share/video/7298145681699622182/?region=CN&mid=7298145762238565171&u
    _code=l1j9bkbd&did=MS4wLjABAAAAtqpCx0hpOERbdSzQdjRZw-wFPxaqdbAzsKDmbJMUI3KWlMGQHC-n6dXAqa-
    dM2EP&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&sha
    re_sign=05kGlqGmR4_IwCX.ZGk6xuL0osNA..5ur7b0jbOx6cc-
    &share_version=170400&ts=1699262937&from_aid=6383&from_ssr=1&from=web_code_link\",
        \"https://www.douyin.com/video/7298145681699622182?previous_page=web_code_link\",
        \"https://www.douyin.com/video/7298145681699622182\",
     ]
     }
     ```

    Args:
        body (list[str]): 作品链接列表/Video link list

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
    r"""提取列表作品id/Extract list video id

     # [中文]
     ### 用途:
     - 提取列表作品id（最多支持20个链接）
     ### 参数:
     - url: 作品链接列表
     ### 返回:
     - 作品id列表

     # [English]
     ### Purpose:
     - Extract list video id (supports up to 20 links)
     ### Parameters:
     - url: Video link list
     ### Return:
     - Video id list

     # [示例/Example]
     ```json
     {
    \"urls\":[
        \"0.53 02/26 I@v.sE Fus:/ 你别太帅了郑润泽# 现场版live # 音乐节 # 郑润泽  https://v.douyin.com/iRNBho6u/
    复制此链接，打开Dou音搜索，直接观看视频!\",
        \"https://v.douyin.com/iRNBho6u/\",
        \"https://www.iesdouyin.com/share/video/7298145681699622182/?region=CN&mid=7298145762238565171&u
    _code=l1j9bkbd&did=MS4wLjABAAAAtqpCx0hpOERbdSzQdjRZw-wFPxaqdbAzsKDmbJMUI3KWlMGQHC-n6dXAqa-
    dM2EP&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&sha
    re_sign=05kGlqGmR4_IwCX.ZGk6xuL0osNA..5ur7b0jbOx6cc-
    &share_version=170400&ts=1699262937&from_aid=6383&from_ssr=1&from=web_code_link\",
        \"https://www.douyin.com/video/7298145681699622182?previous_page=web_code_link\",
        \"https://www.douyin.com/video/7298145681699622182\",
     ]
     }
     ```

    Args:
        body (list[str]): 作品链接列表/Video link list

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
    r"""提取列表作品id/Extract list video id

     # [中文]
     ### 用途:
     - 提取列表作品id（最多支持20个链接）
     ### 参数:
     - url: 作品链接列表
     ### 返回:
     - 作品id列表

     # [English]
     ### Purpose:
     - Extract list video id (supports up to 20 links)
     ### Parameters:
     - url: Video link list
     ### Return:
     - Video id list

     # [示例/Example]
     ```json
     {
    \"urls\":[
        \"0.53 02/26 I@v.sE Fus:/ 你别太帅了郑润泽# 现场版live # 音乐节 # 郑润泽  https://v.douyin.com/iRNBho6u/
    复制此链接，打开Dou音搜索，直接观看视频!\",
        \"https://v.douyin.com/iRNBho6u/\",
        \"https://www.iesdouyin.com/share/video/7298145681699622182/?region=CN&mid=7298145762238565171&u
    _code=l1j9bkbd&did=MS4wLjABAAAAtqpCx0hpOERbdSzQdjRZw-wFPxaqdbAzsKDmbJMUI3KWlMGQHC-n6dXAqa-
    dM2EP&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&sha
    re_sign=05kGlqGmR4_IwCX.ZGk6xuL0osNA..5ur7b0jbOx6cc-
    &share_version=170400&ts=1699262937&from_aid=6383&from_ssr=1&from=web_code_link\",
        \"https://www.douyin.com/video/7298145681699622182?previous_page=web_code_link\",
        \"https://www.douyin.com/video/7298145681699622182\",
     ]
     }
     ```

    Args:
        body (list[str]): 作品链接列表/Video link list

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
