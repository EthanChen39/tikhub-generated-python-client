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
    bv_id: str,
    pn: Union[Unset, int] = 1,
    rpid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["bv_id"] = bv_id

    params["pn"] = pn

    params["rpid"] = rpid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/bilibili/web/fetch_comment_reply",
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
    bv_id: str,
    pn: Union[Unset, int] = 1,
    rpid: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频下指定评论的回复/Get reply to the specified comment

     # [中文]
    ### 用途:
    - 获取视频下指定评论的回复
    ### 参数:
    - bv_id: 作品id
    - pn: 页码
    - rpid: 回复id
    ### 返回:
    - 指定评论的回复数据

    # [English]
    ### Purpose:
    - Get reply to the specified comment
    ### Parameters:
    - bv_id: Video id
    - pn: Page number
    - rpid: Reply id
    ### Return:
    - Reply of the specified comment

    # [示例/Example]
    bv_id = \"BV1M1421t7hT\"
    pn = 1
    rpid = \"237109455120\"

    Args:
        bv_id (str): 作品id/Video id
        pn (Union[Unset, int]): 页码/Page number Default: 1.
        rpid (str): 回复id/Reply id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        bv_id=bv_id,
        pn=pn,
        rpid=rpid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    bv_id: str,
    pn: Union[Unset, int] = 1,
    rpid: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频下指定评论的回复/Get reply to the specified comment

     # [中文]
    ### 用途:
    - 获取视频下指定评论的回复
    ### 参数:
    - bv_id: 作品id
    - pn: 页码
    - rpid: 回复id
    ### 返回:
    - 指定评论的回复数据

    # [English]
    ### Purpose:
    - Get reply to the specified comment
    ### Parameters:
    - bv_id: Video id
    - pn: Page number
    - rpid: Reply id
    ### Return:
    - Reply of the specified comment

    # [示例/Example]
    bv_id = \"BV1M1421t7hT\"
    pn = 1
    rpid = \"237109455120\"

    Args:
        bv_id (str): 作品id/Video id
        pn (Union[Unset, int]): 页码/Page number Default: 1.
        rpid (str): 回复id/Reply id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        bv_id=bv_id,
        pn=pn,
        rpid=rpid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    bv_id: str,
    pn: Union[Unset, int] = 1,
    rpid: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频下指定评论的回复/Get reply to the specified comment

     # [中文]
    ### 用途:
    - 获取视频下指定评论的回复
    ### 参数:
    - bv_id: 作品id
    - pn: 页码
    - rpid: 回复id
    ### 返回:
    - 指定评论的回复数据

    # [English]
    ### Purpose:
    - Get reply to the specified comment
    ### Parameters:
    - bv_id: Video id
    - pn: Page number
    - rpid: Reply id
    ### Return:
    - Reply of the specified comment

    # [示例/Example]
    bv_id = \"BV1M1421t7hT\"
    pn = 1
    rpid = \"237109455120\"

    Args:
        bv_id (str): 作品id/Video id
        pn (Union[Unset, int]): 页码/Page number Default: 1.
        rpid (str): 回复id/Reply id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        bv_id=bv_id,
        pn=pn,
        rpid=rpid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    bv_id: str,
    pn: Union[Unset, int] = 1,
    rpid: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频下指定评论的回复/Get reply to the specified comment

     # [中文]
    ### 用途:
    - 获取视频下指定评论的回复
    ### 参数:
    - bv_id: 作品id
    - pn: 页码
    - rpid: 回复id
    ### 返回:
    - 指定评论的回复数据

    # [English]
    ### Purpose:
    - Get reply to the specified comment
    ### Parameters:
    - bv_id: Video id
    - pn: Page number
    - rpid: Reply id
    ### Return:
    - Reply of the specified comment

    # [示例/Example]
    bv_id = \"BV1M1421t7hT\"
    pn = 1
    rpid = \"237109455120\"

    Args:
        bv_id (str): 作品id/Video id
        pn (Union[Unset, int]): 页码/Page number Default: 1.
        rpid (str): 回复id/Reply id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            bv_id=bv_id,
            pn=pn,
            rpid=rpid,
        )
    ).parsed
