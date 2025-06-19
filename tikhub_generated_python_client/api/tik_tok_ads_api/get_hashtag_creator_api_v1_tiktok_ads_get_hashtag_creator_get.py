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
    hashtag: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["hashtag"] = hashtag

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_hashtag_creator",
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
    hashtag: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取标签创作者信息/Get hashtag creator info

     # [中文]
    ### 用途:
    - 获取特定标签的创作者信息和相关数据
    - 了解标签的来源、创建者和使用情况
    - 分析标签的影响力和传播路径

    ### 参数:
    - hashtag_name: 标签名称，不需要包含#号

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: TCM ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 获赞总数
      - `tt_link`: TikTok链接
      - `tcm_link`: TCM链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: TikTok链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",
      \"params\": {
        \"hashtag_name\": \"blowup\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7153957957875531782\",
              \"user_id\": \"7137978712880088065\",
              \"nick_name\": \"Ben🎧\",
              \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",
              \"follower_cnt\": 1123490,
              \"liked_cnt\": 45506383,
              \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",
              \"items\": [
                {
                  \"item_id\": \"7484029831462522119\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",
                  \"vv\": 1068946,
                  \"liked_cnt\": 124292,
                  \"create_time\": 1742511489
                },
                {
                  \"item_id\": \"7483385475252751623\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oUew2qzADECItXAWFYGeoPQftQEZYPjUKLyIuM~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7483385475252751623\",
                  \"vv\": 239239,
                  \"liked_cnt\": 16919,
                  \"create_time\": 1742361463
                }
              ]
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get creator information and related data for specific hashtags
    - Understand hashtag origin, creator and usage
    - Analyze hashtag influence and spread path

    ### Parameters:
    - hashtag_name: Hashtag name without # symbol

    ### Return Description:
    - `creators`: Creator list
      - `tcm_id`: TCM ID
      - `user_id`: User ID
      - `nick_name`: Nickname
      - `avatar_url`: Avatar URL
      - `follower_cnt`: Follower count
      - `liked_cnt`: Total likes received
      - `tt_link`: TikTok link
      - `tcm_link`: TCM link
      - `items`: Items list
        - `item_id`: Item ID
        - `cover_url`: Cover URL
        - `tt_link`: TikTok link
        - `vv`: View count
        - `liked_cnt`: Like count
        - `create_time`: Creation time

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",
      \"params\": {
        \"hashtag_name\": \"blowup\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7153957957875531782\",
              \"user_id\": \"7137978712880088065\",
              \"nick_name\": \"Ben🎧\",
              \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",
              \"follower_cnt\": 1123490,
              \"liked_cnt\": 45506383,
              \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",
              \"items\": [
                {
                  \"item_id\": \"7484029831462522119\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",
                  \"vv\": 1068946,
                  \"liked_cnt\": 124292,
                  \"create_time\": 1742511489
                }
              ]
            }
          ]
        }
      }
    }
    ```

    Args:
        hashtag (str): 标签名称，不包含#符号/Hashtag name (without # symbol)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        hashtag=hashtag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    hashtag: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取标签创作者信息/Get hashtag creator info

     # [中文]
    ### 用途:
    - 获取特定标签的创作者信息和相关数据
    - 了解标签的来源、创建者和使用情况
    - 分析标签的影响力和传播路径

    ### 参数:
    - hashtag_name: 标签名称，不需要包含#号

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: TCM ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 获赞总数
      - `tt_link`: TikTok链接
      - `tcm_link`: TCM链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: TikTok链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",
      \"params\": {
        \"hashtag_name\": \"blowup\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7153957957875531782\",
              \"user_id\": \"7137978712880088065\",
              \"nick_name\": \"Ben🎧\",
              \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",
              \"follower_cnt\": 1123490,
              \"liked_cnt\": 45506383,
              \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",
              \"items\": [
                {
                  \"item_id\": \"7484029831462522119\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",
                  \"vv\": 1068946,
                  \"liked_cnt\": 124292,
                  \"create_time\": 1742511489
                },
                {
                  \"item_id\": \"7483385475252751623\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oUew2qzADECItXAWFYGeoPQftQEZYPjUKLyIuM~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7483385475252751623\",
                  \"vv\": 239239,
                  \"liked_cnt\": 16919,
                  \"create_time\": 1742361463
                }
              ]
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get creator information and related data for specific hashtags
    - Understand hashtag origin, creator and usage
    - Analyze hashtag influence and spread path

    ### Parameters:
    - hashtag_name: Hashtag name without # symbol

    ### Return Description:
    - `creators`: Creator list
      - `tcm_id`: TCM ID
      - `user_id`: User ID
      - `nick_name`: Nickname
      - `avatar_url`: Avatar URL
      - `follower_cnt`: Follower count
      - `liked_cnt`: Total likes received
      - `tt_link`: TikTok link
      - `tcm_link`: TCM link
      - `items`: Items list
        - `item_id`: Item ID
        - `cover_url`: Cover URL
        - `tt_link`: TikTok link
        - `vv`: View count
        - `liked_cnt`: Like count
        - `create_time`: Creation time

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",
      \"params\": {
        \"hashtag_name\": \"blowup\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7153957957875531782\",
              \"user_id\": \"7137978712880088065\",
              \"nick_name\": \"Ben🎧\",
              \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",
              \"follower_cnt\": 1123490,
              \"liked_cnt\": 45506383,
              \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",
              \"items\": [
                {
                  \"item_id\": \"7484029831462522119\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",
                  \"vv\": 1068946,
                  \"liked_cnt\": 124292,
                  \"create_time\": 1742511489
                }
              ]
            }
          ]
        }
      }
    }
    ```

    Args:
        hashtag (str): 标签名称，不包含#符号/Hashtag name (without # symbol)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        hashtag=hashtag,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    hashtag: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取标签创作者信息/Get hashtag creator info

     # [中文]
    ### 用途:
    - 获取特定标签的创作者信息和相关数据
    - 了解标签的来源、创建者和使用情况
    - 分析标签的影响力和传播路径

    ### 参数:
    - hashtag_name: 标签名称，不需要包含#号

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: TCM ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 获赞总数
      - `tt_link`: TikTok链接
      - `tcm_link`: TCM链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: TikTok链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",
      \"params\": {
        \"hashtag_name\": \"blowup\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7153957957875531782\",
              \"user_id\": \"7137978712880088065\",
              \"nick_name\": \"Ben🎧\",
              \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",
              \"follower_cnt\": 1123490,
              \"liked_cnt\": 45506383,
              \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",
              \"items\": [
                {
                  \"item_id\": \"7484029831462522119\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",
                  \"vv\": 1068946,
                  \"liked_cnt\": 124292,
                  \"create_time\": 1742511489
                },
                {
                  \"item_id\": \"7483385475252751623\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oUew2qzADECItXAWFYGeoPQftQEZYPjUKLyIuM~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7483385475252751623\",
                  \"vv\": 239239,
                  \"liked_cnt\": 16919,
                  \"create_time\": 1742361463
                }
              ]
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get creator information and related data for specific hashtags
    - Understand hashtag origin, creator and usage
    - Analyze hashtag influence and spread path

    ### Parameters:
    - hashtag_name: Hashtag name without # symbol

    ### Return Description:
    - `creators`: Creator list
      - `tcm_id`: TCM ID
      - `user_id`: User ID
      - `nick_name`: Nickname
      - `avatar_url`: Avatar URL
      - `follower_cnt`: Follower count
      - `liked_cnt`: Total likes received
      - `tt_link`: TikTok link
      - `tcm_link`: TCM link
      - `items`: Items list
        - `item_id`: Item ID
        - `cover_url`: Cover URL
        - `tt_link`: TikTok link
        - `vv`: View count
        - `liked_cnt`: Like count
        - `create_time`: Creation time

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",
      \"params\": {
        \"hashtag_name\": \"blowup\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7153957957875531782\",
              \"user_id\": \"7137978712880088065\",
              \"nick_name\": \"Ben🎧\",
              \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",
              \"follower_cnt\": 1123490,
              \"liked_cnt\": 45506383,
              \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",
              \"items\": [
                {
                  \"item_id\": \"7484029831462522119\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",
                  \"vv\": 1068946,
                  \"liked_cnt\": 124292,
                  \"create_time\": 1742511489
                }
              ]
            }
          ]
        }
      }
    }
    ```

    Args:
        hashtag (str): 标签名称，不包含#符号/Hashtag name (without # symbol)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        hashtag=hashtag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    hashtag: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取标签创作者信息/Get hashtag creator info

     # [中文]
    ### 用途:
    - 获取特定标签的创作者信息和相关数据
    - 了解标签的来源、创建者和使用情况
    - 分析标签的影响力和传播路径

    ### 参数:
    - hashtag_name: 标签名称，不需要包含#号

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: TCM ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 获赞总数
      - `tt_link`: TikTok链接
      - `tcm_link`: TCM链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: TikTok链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",
      \"params\": {
        \"hashtag_name\": \"blowup\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7153957957875531782\",
              \"user_id\": \"7137978712880088065\",
              \"nick_name\": \"Ben🎧\",
              \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",
              \"follower_cnt\": 1123490,
              \"liked_cnt\": 45506383,
              \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",
              \"items\": [
                {
                  \"item_id\": \"7484029831462522119\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",
                  \"vv\": 1068946,
                  \"liked_cnt\": 124292,
                  \"create_time\": 1742511489
                },
                {
                  \"item_id\": \"7483385475252751623\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oUew2qzADECItXAWFYGeoPQftQEZYPjUKLyIuM~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7483385475252751623\",
                  \"vv\": 239239,
                  \"liked_cnt\": 16919,
                  \"create_time\": 1742361463
                }
              ]
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get creator information and related data for specific hashtags
    - Understand hashtag origin, creator and usage
    - Analyze hashtag influence and spread path

    ### Parameters:
    - hashtag_name: Hashtag name without # symbol

    ### Return Description:
    - `creators`: Creator list
      - `tcm_id`: TCM ID
      - `user_id`: User ID
      - `nick_name`: Nickname
      - `avatar_url`: Avatar URL
      - `follower_cnt`: Follower count
      - `liked_cnt`: Total likes received
      - `tt_link`: TikTok link
      - `tcm_link`: TCM link
      - `items`: Items list
        - `item_id`: Item ID
        - `cover_url`: Cover URL
        - `tt_link`: TikTok link
        - `vv`: View count
        - `liked_cnt`: Like count
        - `create_time`: Creation time

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_creator\",
      \"params\": {
        \"hashtag_name\": \"blowup\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7153957957875531782\",
              \"user_id\": \"7137978712880088065\",
              \"nick_name\": \"Ben🎧\",
              \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/dee2b881a7833ba36ed8811f3116abb2~tplv-tiktokx-cropcenter:100:100.png\",
              \"follower_cnt\": 1123490,
              \"liked_cnt\": 45506383,
              \"tt_link\": \"https://www.tiktok.com/@ur_localnpcs\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7153957957875531782\",
              \"items\": [
                {
                  \"item_id\": \"7484029831462522119\",
                  \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-
    alisg-p-0037/oY1c0nzeEOyJAF47RDUI4gBnysS3BVDiEIYfRk~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7484029831462522119\",
                  \"vv\": 1068946,
                  \"liked_cnt\": 124292,
                  \"create_time\": 1742511489
                }
              ]
            }
          ]
        }
      }
    }
    ```

    Args:
        hashtag (str): 标签名称，不包含#符号/Hashtag name (without # symbol)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            hashtag=hashtag,
        )
    ).parsed
