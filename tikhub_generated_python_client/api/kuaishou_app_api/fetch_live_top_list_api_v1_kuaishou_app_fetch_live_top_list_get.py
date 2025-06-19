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
    sub_tab_id: Union[Unset, int] = 0,
    sub_tab_name: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["subTabId"] = sub_tab_id

    params["subTabName"] = sub_tab_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/kuaishou/app/fetch_live_top_list",
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
    sub_tab_id: Union[Unset, int] = 0,
    sub_tab_name: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""快手直播榜单/Kuaishou live top list

     # [中文]
    ### 用途:
    - 快手直播榜单
    ### 参数:
    获取快手直播榜单，支持多个子榜单，具体参数如下：

    - 直播总榜对应参数：
        - subTabId = 0
        - subTabName = None
    - 直播音乐榜对应参数：
        - subTabId = 102
        - subTabName = \"音乐\"
    - 直播舞蹈榜对应参数：
        - subTabId = 107
        - subTabName = \"舞蹈\"
    - 直播颜值榜对应参数：
        - subTabId = 101
        - subTabName = \"颜值\"
    - 直播国艺榜对应参数：
        - subTabId = 105
        - subTabName = \"国艺\"
    - 直播相亲榜对应参数：
        - subTabId = 111
        - subTabName = \"相亲\"
    - 直播游戏榜对应参数：
        - subTabId = 106
        - subTabName = \"游戏\"
    - 直播二次元榜对应参数：
        - subTabId = 110
        - subTabName = \"二次元\"
    - 直播故事榜对应参数：
        - subTabId = 104
        - subTabName = \"故事\"
    - 直播团播榜对应参数：
        - subTabId = 113
        - subTabName = \"团播\"
    - 直播九宫格榜对应参数：
        - subTabId = 114
        - subTabName = \"九宫格\"

    ### 返回:
    - 榜单数据

    # [English]
    ### Purpose:
    - Kuaishou live top list
    ### Parameters:
    Get the Kuaishou live top list, support multiple sub-top lists, specific parameters are as follows:

    - Corresponding parameters for the live total list:
        - subTabId = 0
        - subTabName = None
    - Corresponding parameters for the live music list:
        - subTabId = 102
        - subTabName = \"Music\"
    - Corresponding parameters for the live dance list:
        - subTabId = 107
        - subTabName = \"Dance\"
    - Corresponding parameters for the live beauty list:
        - subTabId = 101
        - subTabName = \"Beauty\"
    - Corresponding parameters for the live national art list:
        - subTabId = 105
        - subTabName = \"National Art\"
    - Corresponding parameters for the live blind date list:
        - subTabId = 111
        - subTabName = \"Blind Date\"
    - Corresponding parameters for the live game list:
        - subTabId = 106
        - subTabName = \"Game\"
    - Corresponding parameters for the live second element list:
        - subTabId = 110
        - subTabName = \"Second Element\"
    - Corresponding parameters for the live story list:
        - subTabId = 104
        - subTabName = \"Story\"
    - Corresponding parameters for the live group broadcast list:
        - subTabId = 113
        - subTabName = \"Group Broadcast\"
    - Corresponding parameters for the live nine-grid list:
        - subTabId = 114
        - subTabName = \"Nine Grid\"

    ### Returns:
    - List data

    # [示例/Example]
    subTabId = 0
    subTabName = None

    Args:
        sub_tab_id (Union[Unset, int]):  Default: 0.
        sub_tab_name (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sub_tab_id=sub_tab_id,
        sub_tab_name=sub_tab_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sub_tab_id: Union[Unset, int] = 0,
    sub_tab_name: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""快手直播榜单/Kuaishou live top list

     # [中文]
    ### 用途:
    - 快手直播榜单
    ### 参数:
    获取快手直播榜单，支持多个子榜单，具体参数如下：

    - 直播总榜对应参数：
        - subTabId = 0
        - subTabName = None
    - 直播音乐榜对应参数：
        - subTabId = 102
        - subTabName = \"音乐\"
    - 直播舞蹈榜对应参数：
        - subTabId = 107
        - subTabName = \"舞蹈\"
    - 直播颜值榜对应参数：
        - subTabId = 101
        - subTabName = \"颜值\"
    - 直播国艺榜对应参数：
        - subTabId = 105
        - subTabName = \"国艺\"
    - 直播相亲榜对应参数：
        - subTabId = 111
        - subTabName = \"相亲\"
    - 直播游戏榜对应参数：
        - subTabId = 106
        - subTabName = \"游戏\"
    - 直播二次元榜对应参数：
        - subTabId = 110
        - subTabName = \"二次元\"
    - 直播故事榜对应参数：
        - subTabId = 104
        - subTabName = \"故事\"
    - 直播团播榜对应参数：
        - subTabId = 113
        - subTabName = \"团播\"
    - 直播九宫格榜对应参数：
        - subTabId = 114
        - subTabName = \"九宫格\"

    ### 返回:
    - 榜单数据

    # [English]
    ### Purpose:
    - Kuaishou live top list
    ### Parameters:
    Get the Kuaishou live top list, support multiple sub-top lists, specific parameters are as follows:

    - Corresponding parameters for the live total list:
        - subTabId = 0
        - subTabName = None
    - Corresponding parameters for the live music list:
        - subTabId = 102
        - subTabName = \"Music\"
    - Corresponding parameters for the live dance list:
        - subTabId = 107
        - subTabName = \"Dance\"
    - Corresponding parameters for the live beauty list:
        - subTabId = 101
        - subTabName = \"Beauty\"
    - Corresponding parameters for the live national art list:
        - subTabId = 105
        - subTabName = \"National Art\"
    - Corresponding parameters for the live blind date list:
        - subTabId = 111
        - subTabName = \"Blind Date\"
    - Corresponding parameters for the live game list:
        - subTabId = 106
        - subTabName = \"Game\"
    - Corresponding parameters for the live second element list:
        - subTabId = 110
        - subTabName = \"Second Element\"
    - Corresponding parameters for the live story list:
        - subTabId = 104
        - subTabName = \"Story\"
    - Corresponding parameters for the live group broadcast list:
        - subTabId = 113
        - subTabName = \"Group Broadcast\"
    - Corresponding parameters for the live nine-grid list:
        - subTabId = 114
        - subTabName = \"Nine Grid\"

    ### Returns:
    - List data

    # [示例/Example]
    subTabId = 0
    subTabName = None

    Args:
        sub_tab_id (Union[Unset, int]):  Default: 0.
        sub_tab_name (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        sub_tab_id=sub_tab_id,
        sub_tab_name=sub_tab_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sub_tab_id: Union[Unset, int] = 0,
    sub_tab_name: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""快手直播榜单/Kuaishou live top list

     # [中文]
    ### 用途:
    - 快手直播榜单
    ### 参数:
    获取快手直播榜单，支持多个子榜单，具体参数如下：

    - 直播总榜对应参数：
        - subTabId = 0
        - subTabName = None
    - 直播音乐榜对应参数：
        - subTabId = 102
        - subTabName = \"音乐\"
    - 直播舞蹈榜对应参数：
        - subTabId = 107
        - subTabName = \"舞蹈\"
    - 直播颜值榜对应参数：
        - subTabId = 101
        - subTabName = \"颜值\"
    - 直播国艺榜对应参数：
        - subTabId = 105
        - subTabName = \"国艺\"
    - 直播相亲榜对应参数：
        - subTabId = 111
        - subTabName = \"相亲\"
    - 直播游戏榜对应参数：
        - subTabId = 106
        - subTabName = \"游戏\"
    - 直播二次元榜对应参数：
        - subTabId = 110
        - subTabName = \"二次元\"
    - 直播故事榜对应参数：
        - subTabId = 104
        - subTabName = \"故事\"
    - 直播团播榜对应参数：
        - subTabId = 113
        - subTabName = \"团播\"
    - 直播九宫格榜对应参数：
        - subTabId = 114
        - subTabName = \"九宫格\"

    ### 返回:
    - 榜单数据

    # [English]
    ### Purpose:
    - Kuaishou live top list
    ### Parameters:
    Get the Kuaishou live top list, support multiple sub-top lists, specific parameters are as follows:

    - Corresponding parameters for the live total list:
        - subTabId = 0
        - subTabName = None
    - Corresponding parameters for the live music list:
        - subTabId = 102
        - subTabName = \"Music\"
    - Corresponding parameters for the live dance list:
        - subTabId = 107
        - subTabName = \"Dance\"
    - Corresponding parameters for the live beauty list:
        - subTabId = 101
        - subTabName = \"Beauty\"
    - Corresponding parameters for the live national art list:
        - subTabId = 105
        - subTabName = \"National Art\"
    - Corresponding parameters for the live blind date list:
        - subTabId = 111
        - subTabName = \"Blind Date\"
    - Corresponding parameters for the live game list:
        - subTabId = 106
        - subTabName = \"Game\"
    - Corresponding parameters for the live second element list:
        - subTabId = 110
        - subTabName = \"Second Element\"
    - Corresponding parameters for the live story list:
        - subTabId = 104
        - subTabName = \"Story\"
    - Corresponding parameters for the live group broadcast list:
        - subTabId = 113
        - subTabName = \"Group Broadcast\"
    - Corresponding parameters for the live nine-grid list:
        - subTabId = 114
        - subTabName = \"Nine Grid\"

    ### Returns:
    - List data

    # [示例/Example]
    subTabId = 0
    subTabName = None

    Args:
        sub_tab_id (Union[Unset, int]):  Default: 0.
        sub_tab_name (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sub_tab_id=sub_tab_id,
        sub_tab_name=sub_tab_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sub_tab_id: Union[Unset, int] = 0,
    sub_tab_name: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""快手直播榜单/Kuaishou live top list

     # [中文]
    ### 用途:
    - 快手直播榜单
    ### 参数:
    获取快手直播榜单，支持多个子榜单，具体参数如下：

    - 直播总榜对应参数：
        - subTabId = 0
        - subTabName = None
    - 直播音乐榜对应参数：
        - subTabId = 102
        - subTabName = \"音乐\"
    - 直播舞蹈榜对应参数：
        - subTabId = 107
        - subTabName = \"舞蹈\"
    - 直播颜值榜对应参数：
        - subTabId = 101
        - subTabName = \"颜值\"
    - 直播国艺榜对应参数：
        - subTabId = 105
        - subTabName = \"国艺\"
    - 直播相亲榜对应参数：
        - subTabId = 111
        - subTabName = \"相亲\"
    - 直播游戏榜对应参数：
        - subTabId = 106
        - subTabName = \"游戏\"
    - 直播二次元榜对应参数：
        - subTabId = 110
        - subTabName = \"二次元\"
    - 直播故事榜对应参数：
        - subTabId = 104
        - subTabName = \"故事\"
    - 直播团播榜对应参数：
        - subTabId = 113
        - subTabName = \"团播\"
    - 直播九宫格榜对应参数：
        - subTabId = 114
        - subTabName = \"九宫格\"

    ### 返回:
    - 榜单数据

    # [English]
    ### Purpose:
    - Kuaishou live top list
    ### Parameters:
    Get the Kuaishou live top list, support multiple sub-top lists, specific parameters are as follows:

    - Corresponding parameters for the live total list:
        - subTabId = 0
        - subTabName = None
    - Corresponding parameters for the live music list:
        - subTabId = 102
        - subTabName = \"Music\"
    - Corresponding parameters for the live dance list:
        - subTabId = 107
        - subTabName = \"Dance\"
    - Corresponding parameters for the live beauty list:
        - subTabId = 101
        - subTabName = \"Beauty\"
    - Corresponding parameters for the live national art list:
        - subTabId = 105
        - subTabName = \"National Art\"
    - Corresponding parameters for the live blind date list:
        - subTabId = 111
        - subTabName = \"Blind Date\"
    - Corresponding parameters for the live game list:
        - subTabId = 106
        - subTabName = \"Game\"
    - Corresponding parameters for the live second element list:
        - subTabId = 110
        - subTabName = \"Second Element\"
    - Corresponding parameters for the live story list:
        - subTabId = 104
        - subTabName = \"Story\"
    - Corresponding parameters for the live group broadcast list:
        - subTabId = 113
        - subTabName = \"Group Broadcast\"
    - Corresponding parameters for the live nine-grid list:
        - subTabId = 114
        - subTabName = \"Nine Grid\"

    ### Returns:
    - List data

    # [示例/Example]
    subTabId = 0
    subTabName = None

    Args:
        sub_tab_id (Union[Unset, int]):  Default: 0.
        sub_tab_name (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            sub_tab_id=sub_tab_id,
            sub_tab_name=sub_tab_name,
        )
    ).parsed
