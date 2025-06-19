from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.a_bogus_model import ABogusModel
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: ABogusModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/web/generate_a_bogus",
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
    body: ABogusModel,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""使用接口网址生成A-Bogus参数/Generate A-Bogus parameter using API URL

     # [中文]
    ### 用途:
    - 使用接口网址生成A-Bogus参数，提交的URL不能带有a_bogus参数，同时a_bogus参数与请求头中的User-Agent有关，需要一起提交和请求。
    ### 参数:
    - url: API链接，请去除url中的原本的a_boogus参数(如有)。
    - data: 请求载荷，只有在POST请求中才需要提交，GET请求中使用空字符串即可。
    - user_agent: user-agent，需要提交你请求头中的User-Agent，该值参与a_bogus参数的计算。
    - index_0: 加密明文列表的第一个值，无特殊要求，默认为0，不要随意修改。
    - index_1: 加密明文列表的第二个值，无特殊要求，默认为1，不要随意修改。
    - index_2: 加密明文列表的第三个值，无特殊要求，默认为14，不要随意修改。
    ### 返回:
    - A-Bogus参数

    # [English]
    ### Purpose:
    - Generate A-Bogus parameter using API URL, the submitted URL cannot contain the original a_boogus
    parameter, and the a_bogus parameter is related to the User-Agent in the request header, which needs
    to be submitted and requested together.
    ### Parameters:
    - url: API link, please remove the original a_boogus parameter from the url (if any).
    - data: Request payload, only need to submit in POST request, use an empty string in GET request.
    - user_agent: user-agent, you need to submit the User-Agent in your request header, which is
    involved in the calculation of the a_bogus parameter.
    - index_0: The first value of the encrypted plaintext list, no special requirements, the default is
    0, do not modify it at will.
    - index_1: The second value of the encrypted plaintext list, no special requirements, the default is
    1, do not modify it at will.
    - index_2: The third value of the encrypted plaintext list, no special requirements, the default is
    14, do not modify it at will.
    ### Return:
    - A-Bogus parameter

    # [示例/Example]
    ```json
    {
    \"url\": \"https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=638
    3&channel=channel_pc_web&search_channel=aweme_general&enable_history=1&keyword=%E4%B8%AD%E5%8D%8E%E5
    %A8%98&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=73469059025
    54844468&offset=0&count=15&need_filter_settings=1&pc_client_type=1&version_code=190600&version_name=
    19.6.0&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platfo
    rm=Win32&browser_name=Firefox&browser_version=124.0&browser_online=true&engine_name=Gecko&engine_ver
    sion=124.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=&platform=PC&webid=7348962975
    497324070&msToken=YCTVM6YGmjFdIpQAN9ykXLBXiSiuHdZkOkEQWTeqVOHBEPmOcM0lNwE0Kd9vgHPMPigSndZDHfAq9k-
    6lDmH3Jqz6mHHxmn-BzQjmLMIfLIPgirgnOixM9x4PwgcNQ%3D%3D\",
    \"data\": \"\",
    \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/104.0.0.0 Safari/537.36\",
    \"index_0\": 0,
    \"index_1\": 1,
    \"index_2\": 14
    }
    ```

    Args:
        body (ABogusModel):

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
    body: ABogusModel,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""使用接口网址生成A-Bogus参数/Generate A-Bogus parameter using API URL

     # [中文]
    ### 用途:
    - 使用接口网址生成A-Bogus参数，提交的URL不能带有a_bogus参数，同时a_bogus参数与请求头中的User-Agent有关，需要一起提交和请求。
    ### 参数:
    - url: API链接，请去除url中的原本的a_boogus参数(如有)。
    - data: 请求载荷，只有在POST请求中才需要提交，GET请求中使用空字符串即可。
    - user_agent: user-agent，需要提交你请求头中的User-Agent，该值参与a_bogus参数的计算。
    - index_0: 加密明文列表的第一个值，无特殊要求，默认为0，不要随意修改。
    - index_1: 加密明文列表的第二个值，无特殊要求，默认为1，不要随意修改。
    - index_2: 加密明文列表的第三个值，无特殊要求，默认为14，不要随意修改。
    ### 返回:
    - A-Bogus参数

    # [English]
    ### Purpose:
    - Generate A-Bogus parameter using API URL, the submitted URL cannot contain the original a_boogus
    parameter, and the a_bogus parameter is related to the User-Agent in the request header, which needs
    to be submitted and requested together.
    ### Parameters:
    - url: API link, please remove the original a_boogus parameter from the url (if any).
    - data: Request payload, only need to submit in POST request, use an empty string in GET request.
    - user_agent: user-agent, you need to submit the User-Agent in your request header, which is
    involved in the calculation of the a_bogus parameter.
    - index_0: The first value of the encrypted plaintext list, no special requirements, the default is
    0, do not modify it at will.
    - index_1: The second value of the encrypted plaintext list, no special requirements, the default is
    1, do not modify it at will.
    - index_2: The third value of the encrypted plaintext list, no special requirements, the default is
    14, do not modify it at will.
    ### Return:
    - A-Bogus parameter

    # [示例/Example]
    ```json
    {
    \"url\": \"https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=638
    3&channel=channel_pc_web&search_channel=aweme_general&enable_history=1&keyword=%E4%B8%AD%E5%8D%8E%E5
    %A8%98&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=73469059025
    54844468&offset=0&count=15&need_filter_settings=1&pc_client_type=1&version_code=190600&version_name=
    19.6.0&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platfo
    rm=Win32&browser_name=Firefox&browser_version=124.0&browser_online=true&engine_name=Gecko&engine_ver
    sion=124.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=&platform=PC&webid=7348962975
    497324070&msToken=YCTVM6YGmjFdIpQAN9ykXLBXiSiuHdZkOkEQWTeqVOHBEPmOcM0lNwE0Kd9vgHPMPigSndZDHfAq9k-
    6lDmH3Jqz6mHHxmn-BzQjmLMIfLIPgirgnOixM9x4PwgcNQ%3D%3D\",
    \"data\": \"\",
    \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/104.0.0.0 Safari/537.36\",
    \"index_0\": 0,
    \"index_1\": 1,
    \"index_2\": 14
    }
    ```

    Args:
        body (ABogusModel):

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
    body: ABogusModel,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""使用接口网址生成A-Bogus参数/Generate A-Bogus parameter using API URL

     # [中文]
    ### 用途:
    - 使用接口网址生成A-Bogus参数，提交的URL不能带有a_bogus参数，同时a_bogus参数与请求头中的User-Agent有关，需要一起提交和请求。
    ### 参数:
    - url: API链接，请去除url中的原本的a_boogus参数(如有)。
    - data: 请求载荷，只有在POST请求中才需要提交，GET请求中使用空字符串即可。
    - user_agent: user-agent，需要提交你请求头中的User-Agent，该值参与a_bogus参数的计算。
    - index_0: 加密明文列表的第一个值，无特殊要求，默认为0，不要随意修改。
    - index_1: 加密明文列表的第二个值，无特殊要求，默认为1，不要随意修改。
    - index_2: 加密明文列表的第三个值，无特殊要求，默认为14，不要随意修改。
    ### 返回:
    - A-Bogus参数

    # [English]
    ### Purpose:
    - Generate A-Bogus parameter using API URL, the submitted URL cannot contain the original a_boogus
    parameter, and the a_bogus parameter is related to the User-Agent in the request header, which needs
    to be submitted and requested together.
    ### Parameters:
    - url: API link, please remove the original a_boogus parameter from the url (if any).
    - data: Request payload, only need to submit in POST request, use an empty string in GET request.
    - user_agent: user-agent, you need to submit the User-Agent in your request header, which is
    involved in the calculation of the a_bogus parameter.
    - index_0: The first value of the encrypted plaintext list, no special requirements, the default is
    0, do not modify it at will.
    - index_1: The second value of the encrypted plaintext list, no special requirements, the default is
    1, do not modify it at will.
    - index_2: The third value of the encrypted plaintext list, no special requirements, the default is
    14, do not modify it at will.
    ### Return:
    - A-Bogus parameter

    # [示例/Example]
    ```json
    {
    \"url\": \"https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=638
    3&channel=channel_pc_web&search_channel=aweme_general&enable_history=1&keyword=%E4%B8%AD%E5%8D%8E%E5
    %A8%98&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=73469059025
    54844468&offset=0&count=15&need_filter_settings=1&pc_client_type=1&version_code=190600&version_name=
    19.6.0&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platfo
    rm=Win32&browser_name=Firefox&browser_version=124.0&browser_online=true&engine_name=Gecko&engine_ver
    sion=124.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=&platform=PC&webid=7348962975
    497324070&msToken=YCTVM6YGmjFdIpQAN9ykXLBXiSiuHdZkOkEQWTeqVOHBEPmOcM0lNwE0Kd9vgHPMPigSndZDHfAq9k-
    6lDmH3Jqz6mHHxmn-BzQjmLMIfLIPgirgnOixM9x4PwgcNQ%3D%3D\",
    \"data\": \"\",
    \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/104.0.0.0 Safari/537.36\",
    \"index_0\": 0,
    \"index_1\": 1,
    \"index_2\": 14
    }
    ```

    Args:
        body (ABogusModel):

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
    body: ABogusModel,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""使用接口网址生成A-Bogus参数/Generate A-Bogus parameter using API URL

     # [中文]
    ### 用途:
    - 使用接口网址生成A-Bogus参数，提交的URL不能带有a_bogus参数，同时a_bogus参数与请求头中的User-Agent有关，需要一起提交和请求。
    ### 参数:
    - url: API链接，请去除url中的原本的a_boogus参数(如有)。
    - data: 请求载荷，只有在POST请求中才需要提交，GET请求中使用空字符串即可。
    - user_agent: user-agent，需要提交你请求头中的User-Agent，该值参与a_bogus参数的计算。
    - index_0: 加密明文列表的第一个值，无特殊要求，默认为0，不要随意修改。
    - index_1: 加密明文列表的第二个值，无特殊要求，默认为1，不要随意修改。
    - index_2: 加密明文列表的第三个值，无特殊要求，默认为14，不要随意修改。
    ### 返回:
    - A-Bogus参数

    # [English]
    ### Purpose:
    - Generate A-Bogus parameter using API URL, the submitted URL cannot contain the original a_boogus
    parameter, and the a_bogus parameter is related to the User-Agent in the request header, which needs
    to be submitted and requested together.
    ### Parameters:
    - url: API link, please remove the original a_boogus parameter from the url (if any).
    - data: Request payload, only need to submit in POST request, use an empty string in GET request.
    - user_agent: user-agent, you need to submit the User-Agent in your request header, which is
    involved in the calculation of the a_bogus parameter.
    - index_0: The first value of the encrypted plaintext list, no special requirements, the default is
    0, do not modify it at will.
    - index_1: The second value of the encrypted plaintext list, no special requirements, the default is
    1, do not modify it at will.
    - index_2: The third value of the encrypted plaintext list, no special requirements, the default is
    14, do not modify it at will.
    ### Return:
    - A-Bogus parameter

    # [示例/Example]
    ```json
    {
    \"url\": \"https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=webapp&aid=638
    3&channel=channel_pc_web&search_channel=aweme_general&enable_history=1&keyword=%E4%B8%AD%E5%8D%8E%E5
    %A8%98&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=73469059025
    54844468&offset=0&count=15&need_filter_settings=1&pc_client_type=1&version_code=190600&version_name=
    19.6.0&cookie_enabled=true&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platfo
    rm=Win32&browser_name=Firefox&browser_version=124.0&browser_online=true&engine_name=Gecko&engine_ver
    sion=124.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=&platform=PC&webid=7348962975
    497324070&msToken=YCTVM6YGmjFdIpQAN9ykXLBXiSiuHdZkOkEQWTeqVOHBEPmOcM0lNwE0Kd9vgHPMPigSndZDHfAq9k-
    6lDmH3Jqz6mHHxmn-BzQjmLMIfLIPgirgnOixM9x4PwgcNQ%3D%3D\",
    \"data\": \"\",
    \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/104.0.0.0 Safari/537.36\",
    \"index_0\": 0,
    \"index_1\": 1,
    \"index_2\": 14
    }
    ```

    Args:
        body (ABogusModel):

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
