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
    sogou_url: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sogou_url"] = sogou_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/wechat_mp/web/fetch_mp_article_url",
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
    sogou_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号文章永久链接/Get Wechat MP Article URL

     # [中文]
    ### 用途:
    - 获取微信公众号文章永久链接
    ### 参数:
    - sogou_url: 搜狗链接
    ### 返回:
    - 永久链接

    # [English]
    ### Purpose:
    - Get Wechat MP Article URL
    ### Parameters:
    - sogou_url: Sogou URL
    ### Returns:
    - Article URL

    # [示例/Example]
    sogou_url = \"https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVg
    S5mzcw64XRlRaPIdMgILsPEBI9djq3byAlqXa8Fplpd9bV3r44ewJj5IFttt-prmTSHShu8JtNlpDYR_z_1xvD2J_XrGTUriRYOO
    Y2mt9pZSIUQEepUVTybxAOW4P5fEPd23R0CgK6W3KEODtIkcv1U5w5VkZ8a7_lyyAqreiCgr1YH9mz_7mzFDl6rX6ZnkVYNsUHV_
    OmaXBUCqpZ1Pa6YO8fIRwtipOg..&type=2&query=deepseek&token=C2E90D2050EB6EA5C2C4EDB1541D855FC322013E67C
    5DC5A&k=4&h=k\"

    Args:
        sogou_url (str): 搜狗链接/Sogou URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sogou_url=sogou_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sogou_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号文章永久链接/Get Wechat MP Article URL

     # [中文]
    ### 用途:
    - 获取微信公众号文章永久链接
    ### 参数:
    - sogou_url: 搜狗链接
    ### 返回:
    - 永久链接

    # [English]
    ### Purpose:
    - Get Wechat MP Article URL
    ### Parameters:
    - sogou_url: Sogou URL
    ### Returns:
    - Article URL

    # [示例/Example]
    sogou_url = \"https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVg
    S5mzcw64XRlRaPIdMgILsPEBI9djq3byAlqXa8Fplpd9bV3r44ewJj5IFttt-prmTSHShu8JtNlpDYR_z_1xvD2J_XrGTUriRYOO
    Y2mt9pZSIUQEepUVTybxAOW4P5fEPd23R0CgK6W3KEODtIkcv1U5w5VkZ8a7_lyyAqreiCgr1YH9mz_7mzFDl6rX6ZnkVYNsUHV_
    OmaXBUCqpZ1Pa6YO8fIRwtipOg..&type=2&query=deepseek&token=C2E90D2050EB6EA5C2C4EDB1541D855FC322013E67C
    5DC5A&k=4&h=k\"

    Args:
        sogou_url (str): 搜狗链接/Sogou URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        sogou_url=sogou_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sogou_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号文章永久链接/Get Wechat MP Article URL

     # [中文]
    ### 用途:
    - 获取微信公众号文章永久链接
    ### 参数:
    - sogou_url: 搜狗链接
    ### 返回:
    - 永久链接

    # [English]
    ### Purpose:
    - Get Wechat MP Article URL
    ### Parameters:
    - sogou_url: Sogou URL
    ### Returns:
    - Article URL

    # [示例/Example]
    sogou_url = \"https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVg
    S5mzcw64XRlRaPIdMgILsPEBI9djq3byAlqXa8Fplpd9bV3r44ewJj5IFttt-prmTSHShu8JtNlpDYR_z_1xvD2J_XrGTUriRYOO
    Y2mt9pZSIUQEepUVTybxAOW4P5fEPd23R0CgK6W3KEODtIkcv1U5w5VkZ8a7_lyyAqreiCgr1YH9mz_7mzFDl6rX6ZnkVYNsUHV_
    OmaXBUCqpZ1Pa6YO8fIRwtipOg..&type=2&query=deepseek&token=C2E90D2050EB6EA5C2C4EDB1541D855FC322013E67C
    5DC5A&k=4&h=k\"

    Args:
        sogou_url (str): 搜狗链接/Sogou URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sogou_url=sogou_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sogou_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号文章永久链接/Get Wechat MP Article URL

     # [中文]
    ### 用途:
    - 获取微信公众号文章永久链接
    ### 参数:
    - sogou_url: 搜狗链接
    ### 返回:
    - 永久链接

    # [English]
    ### Purpose:
    - Get Wechat MP Article URL
    ### Parameters:
    - sogou_url: Sogou URL
    ### Returns:
    - Article URL

    # [示例/Example]
    sogou_url = \"https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVg
    S5mzcw64XRlRaPIdMgILsPEBI9djq3byAlqXa8Fplpd9bV3r44ewJj5IFttt-prmTSHShu8JtNlpDYR_z_1xvD2J_XrGTUriRYOO
    Y2mt9pZSIUQEepUVTybxAOW4P5fEPd23R0CgK6W3KEODtIkcv1U5w5VkZ8a7_lyyAqreiCgr1YH9mz_7mzFDl6rX6ZnkVYNsUHV_
    OmaXBUCqpZ1Pa6YO8fIRwtipOg..&type=2&query=deepseek&token=C2E90D2050EB6EA5C2C4EDB1541D855FC322013E67C
    5DC5A&k=4&h=k\"

    Args:
        sogou_url (str): 搜狗链接/Sogou URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            sogou_url=sogou_url,
        )
    ).parsed
