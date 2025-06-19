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
    material_id: str,
    industry: Union[Unset, str] = "25308000000",
    country_code: Union[Unset, str] = "US",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["material_id"] = material_id

    params["industry"] = industry

    params["country_code"] = country_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_recommended_ads",
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
    material_id: str,
    industry: Union[Unset, str] = "25308000000",
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取推荐广告/Get recommended ads

     # [中文]
    ### 用途:
    - 基于指定广告获取相似的推荐广告列表
    - 发现同行业或相似风格的优秀广告案例
    - 为广告创意提供更多参考和灵感

    ### 参数:
    - material_id: 参考广告素材ID，必填参数
    - industry: 行业ID，如游戏行业：25308000000
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `materials`: 推荐广告素材列表
      - `ad_title`: 广告标题
      - `brand_name`: 品牌名称
      - `cost`: 花费等级
      - `ctr`: 点击率
      - `favorite`: 是否收藏
      - `id`: 广告ID
      - `industry_key`: 行业键值
      - `is_search`: 是否搜索结果
      - `like`: 点赞数
      - `objective_key`: 广告目标键值
      - `tag`: 标签
      - `video_info`: 视频信息
        - `vid`: 视频ID
        - `duration`: 时长（秒）
        - `cover`: 封面图URL
        - `video_url`: 视频播放地址
          - `360p`: 360p画质
          - `480p`: 480p画质
          - `540p`: 540p画质
          - `720p`: 720p画质
        - `width`: 视频宽度
        - `height`: 视频高度

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"industry\": \"25308000000\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"ad_title\": \"What will you decide?\",
              \"brand_name\": \"Eatventure\",
              \"cost\": 2,
              \"ctr\": 0.07,
              \"favorite\": false,
              \"id\": \"7164756134804979714\",
              \"industry_key\": \"label_25308000000\",
              \"is_search\": false,
              \"like\": 1009024,
              \"objective_key\": \"campaign_objective_conversion\",
              \"tag\": 3,
              \"video_info\": {
                \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",
                \"duration\": 30.016,
                \"cover\": \"https://p16-sign-
    sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",
                \"video_url\": {
                  \"360p\": \"https://v16m-
    default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",
                  \"480p\": \"https://v16m-
    default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",
                  \"540p\": \"https://v16m-
    default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",
                  \"720p\": \"https://v16m-
    default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"
                },
                \"width\": 720,
                \"height\": 1280
              }
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get similar recommended ads based on a specified ad
    - Discover excellent ad cases in the same industry or with similar styles
    - Provide more references and inspiration for ad creativity

    ### Parameters:
    - material_id: Reference ad material ID, required parameter
    - industry: Industry ID, e.g., Games: 25308000000
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `materials`: Recommended ad materials list
      - `ad_title`: Ad title
      - `brand_name`: Brand name
      - `cost`: Cost level
      - `ctr`: Click-through rate
      - `favorite`: Whether favorited
      - `id`: Ad ID
      - `industry_key`: Industry key
      - `is_search`: Whether search result
      - `like`: Like count
      - `objective_key`: Ad objective key
      - `tag`: Tag
      - `video_info`: Video information
        - `vid`: Video ID
        - `duration`: Duration in seconds
        - `cover`: Cover image URL
        - `video_url`: Video playback URLs
          - `360p`: 360p quality
          - `480p`: 480p quality
          - `540p`: 540p quality
          - `720p`: 720p quality
        - `width`: Video width
        - `height`: Video height

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"industry\": \"25308000000\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"ad_title\": \"What will you decide?\",
              \"brand_name\": \"Eatventure\",
              \"cost\": 2,
              \"ctr\": 0.07,
              \"favorite\": false,
              \"id\": \"7164756134804979714\",
              \"industry_key\": \"label_25308000000\",
              \"is_search\": false,
              \"like\": 1009024,
              \"objective_key\": \"campaign_objective_conversion\",
              \"tag\": 3,
              \"video_info\": {
                \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",
                \"duration\": 30.016,
                \"cover\": \"https://p16-sign-
    sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",
                \"video_url\": {
                  \"360p\": \"https://v16m-
    default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",
                  \"480p\": \"https://v16m-
    default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",
                  \"540p\": \"https://v16m-
    default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",
                  \"720p\": \"https://v16m-
    default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"
                },
                \"width\": 720,
                \"height\": 1280
              }
            }
          ]
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        industry (Union[Unset, str]): 行业ID/Industry ID Default: '25308000000'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        material_id=material_id,
        industry=industry,
        country_code=country_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    material_id: str,
    industry: Union[Unset, str] = "25308000000",
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取推荐广告/Get recommended ads

     # [中文]
    ### 用途:
    - 基于指定广告获取相似的推荐广告列表
    - 发现同行业或相似风格的优秀广告案例
    - 为广告创意提供更多参考和灵感

    ### 参数:
    - material_id: 参考广告素材ID，必填参数
    - industry: 行业ID，如游戏行业：25308000000
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `materials`: 推荐广告素材列表
      - `ad_title`: 广告标题
      - `brand_name`: 品牌名称
      - `cost`: 花费等级
      - `ctr`: 点击率
      - `favorite`: 是否收藏
      - `id`: 广告ID
      - `industry_key`: 行业键值
      - `is_search`: 是否搜索结果
      - `like`: 点赞数
      - `objective_key`: 广告目标键值
      - `tag`: 标签
      - `video_info`: 视频信息
        - `vid`: 视频ID
        - `duration`: 时长（秒）
        - `cover`: 封面图URL
        - `video_url`: 视频播放地址
          - `360p`: 360p画质
          - `480p`: 480p画质
          - `540p`: 540p画质
          - `720p`: 720p画质
        - `width`: 视频宽度
        - `height`: 视频高度

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"industry\": \"25308000000\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"ad_title\": \"What will you decide?\",
              \"brand_name\": \"Eatventure\",
              \"cost\": 2,
              \"ctr\": 0.07,
              \"favorite\": false,
              \"id\": \"7164756134804979714\",
              \"industry_key\": \"label_25308000000\",
              \"is_search\": false,
              \"like\": 1009024,
              \"objective_key\": \"campaign_objective_conversion\",
              \"tag\": 3,
              \"video_info\": {
                \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",
                \"duration\": 30.016,
                \"cover\": \"https://p16-sign-
    sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",
                \"video_url\": {
                  \"360p\": \"https://v16m-
    default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",
                  \"480p\": \"https://v16m-
    default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",
                  \"540p\": \"https://v16m-
    default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",
                  \"720p\": \"https://v16m-
    default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"
                },
                \"width\": 720,
                \"height\": 1280
              }
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get similar recommended ads based on a specified ad
    - Discover excellent ad cases in the same industry or with similar styles
    - Provide more references and inspiration for ad creativity

    ### Parameters:
    - material_id: Reference ad material ID, required parameter
    - industry: Industry ID, e.g., Games: 25308000000
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `materials`: Recommended ad materials list
      - `ad_title`: Ad title
      - `brand_name`: Brand name
      - `cost`: Cost level
      - `ctr`: Click-through rate
      - `favorite`: Whether favorited
      - `id`: Ad ID
      - `industry_key`: Industry key
      - `is_search`: Whether search result
      - `like`: Like count
      - `objective_key`: Ad objective key
      - `tag`: Tag
      - `video_info`: Video information
        - `vid`: Video ID
        - `duration`: Duration in seconds
        - `cover`: Cover image URL
        - `video_url`: Video playback URLs
          - `360p`: 360p quality
          - `480p`: 480p quality
          - `540p`: 540p quality
          - `720p`: 720p quality
        - `width`: Video width
        - `height`: Video height

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"industry\": \"25308000000\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"ad_title\": \"What will you decide?\",
              \"brand_name\": \"Eatventure\",
              \"cost\": 2,
              \"ctr\": 0.07,
              \"favorite\": false,
              \"id\": \"7164756134804979714\",
              \"industry_key\": \"label_25308000000\",
              \"is_search\": false,
              \"like\": 1009024,
              \"objective_key\": \"campaign_objective_conversion\",
              \"tag\": 3,
              \"video_info\": {
                \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",
                \"duration\": 30.016,
                \"cover\": \"https://p16-sign-
    sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",
                \"video_url\": {
                  \"360p\": \"https://v16m-
    default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",
                  \"480p\": \"https://v16m-
    default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",
                  \"540p\": \"https://v16m-
    default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",
                  \"720p\": \"https://v16m-
    default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"
                },
                \"width\": 720,
                \"height\": 1280
              }
            }
          ]
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        industry (Union[Unset, str]): 行业ID/Industry ID Default: '25308000000'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        material_id=material_id,
        industry=industry,
        country_code=country_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    material_id: str,
    industry: Union[Unset, str] = "25308000000",
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取推荐广告/Get recommended ads

     # [中文]
    ### 用途:
    - 基于指定广告获取相似的推荐广告列表
    - 发现同行业或相似风格的优秀广告案例
    - 为广告创意提供更多参考和灵感

    ### 参数:
    - material_id: 参考广告素材ID，必填参数
    - industry: 行业ID，如游戏行业：25308000000
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `materials`: 推荐广告素材列表
      - `ad_title`: 广告标题
      - `brand_name`: 品牌名称
      - `cost`: 花费等级
      - `ctr`: 点击率
      - `favorite`: 是否收藏
      - `id`: 广告ID
      - `industry_key`: 行业键值
      - `is_search`: 是否搜索结果
      - `like`: 点赞数
      - `objective_key`: 广告目标键值
      - `tag`: 标签
      - `video_info`: 视频信息
        - `vid`: 视频ID
        - `duration`: 时长（秒）
        - `cover`: 封面图URL
        - `video_url`: 视频播放地址
          - `360p`: 360p画质
          - `480p`: 480p画质
          - `540p`: 540p画质
          - `720p`: 720p画质
        - `width`: 视频宽度
        - `height`: 视频高度

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"industry\": \"25308000000\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"ad_title\": \"What will you decide?\",
              \"brand_name\": \"Eatventure\",
              \"cost\": 2,
              \"ctr\": 0.07,
              \"favorite\": false,
              \"id\": \"7164756134804979714\",
              \"industry_key\": \"label_25308000000\",
              \"is_search\": false,
              \"like\": 1009024,
              \"objective_key\": \"campaign_objective_conversion\",
              \"tag\": 3,
              \"video_info\": {
                \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",
                \"duration\": 30.016,
                \"cover\": \"https://p16-sign-
    sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",
                \"video_url\": {
                  \"360p\": \"https://v16m-
    default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",
                  \"480p\": \"https://v16m-
    default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",
                  \"540p\": \"https://v16m-
    default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",
                  \"720p\": \"https://v16m-
    default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"
                },
                \"width\": 720,
                \"height\": 1280
              }
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get similar recommended ads based on a specified ad
    - Discover excellent ad cases in the same industry or with similar styles
    - Provide more references and inspiration for ad creativity

    ### Parameters:
    - material_id: Reference ad material ID, required parameter
    - industry: Industry ID, e.g., Games: 25308000000
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `materials`: Recommended ad materials list
      - `ad_title`: Ad title
      - `brand_name`: Brand name
      - `cost`: Cost level
      - `ctr`: Click-through rate
      - `favorite`: Whether favorited
      - `id`: Ad ID
      - `industry_key`: Industry key
      - `is_search`: Whether search result
      - `like`: Like count
      - `objective_key`: Ad objective key
      - `tag`: Tag
      - `video_info`: Video information
        - `vid`: Video ID
        - `duration`: Duration in seconds
        - `cover`: Cover image URL
        - `video_url`: Video playback URLs
          - `360p`: 360p quality
          - `480p`: 480p quality
          - `540p`: 540p quality
          - `720p`: 720p quality
        - `width`: Video width
        - `height`: Video height

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"industry\": \"25308000000\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"ad_title\": \"What will you decide?\",
              \"brand_name\": \"Eatventure\",
              \"cost\": 2,
              \"ctr\": 0.07,
              \"favorite\": false,
              \"id\": \"7164756134804979714\",
              \"industry_key\": \"label_25308000000\",
              \"is_search\": false,
              \"like\": 1009024,
              \"objective_key\": \"campaign_objective_conversion\",
              \"tag\": 3,
              \"video_info\": {
                \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",
                \"duration\": 30.016,
                \"cover\": \"https://p16-sign-
    sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",
                \"video_url\": {
                  \"360p\": \"https://v16m-
    default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",
                  \"480p\": \"https://v16m-
    default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",
                  \"540p\": \"https://v16m-
    default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",
                  \"720p\": \"https://v16m-
    default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"
                },
                \"width\": 720,
                \"height\": 1280
              }
            }
          ]
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        industry (Union[Unset, str]): 行业ID/Industry ID Default: '25308000000'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        material_id=material_id,
        industry=industry,
        country_code=country_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    material_id: str,
    industry: Union[Unset, str] = "25308000000",
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取推荐广告/Get recommended ads

     # [中文]
    ### 用途:
    - 基于指定广告获取相似的推荐广告列表
    - 发现同行业或相似风格的优秀广告案例
    - 为广告创意提供更多参考和灵感

    ### 参数:
    - material_id: 参考广告素材ID，必填参数
    - industry: 行业ID，如游戏行业：25308000000
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `materials`: 推荐广告素材列表
      - `ad_title`: 广告标题
      - `brand_name`: 品牌名称
      - `cost`: 花费等级
      - `ctr`: 点击率
      - `favorite`: 是否收藏
      - `id`: 广告ID
      - `industry_key`: 行业键值
      - `is_search`: 是否搜索结果
      - `like`: 点赞数
      - `objective_key`: 广告目标键值
      - `tag`: 标签
      - `video_info`: 视频信息
        - `vid`: 视频ID
        - `duration`: 时长（秒）
        - `cover`: 封面图URL
        - `video_url`: 视频播放地址
          - `360p`: 360p画质
          - `480p`: 480p画质
          - `540p`: 540p画质
          - `720p`: 720p画质
        - `width`: 视频宽度
        - `height`: 视频高度

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"industry\": \"25308000000\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"ad_title\": \"What will you decide?\",
              \"brand_name\": \"Eatventure\",
              \"cost\": 2,
              \"ctr\": 0.07,
              \"favorite\": false,
              \"id\": \"7164756134804979714\",
              \"industry_key\": \"label_25308000000\",
              \"is_search\": false,
              \"like\": 1009024,
              \"objective_key\": \"campaign_objective_conversion\",
              \"tag\": 3,
              \"video_info\": {
                \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",
                \"duration\": 30.016,
                \"cover\": \"https://p16-sign-
    sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",
                \"video_url\": {
                  \"360p\": \"https://v16m-
    default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",
                  \"480p\": \"https://v16m-
    default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",
                  \"540p\": \"https://v16m-
    default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",
                  \"720p\": \"https://v16m-
    default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"
                },
                \"width\": 720,
                \"height\": 1280
              }
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get similar recommended ads based on a specified ad
    - Discover excellent ad cases in the same industry or with similar styles
    - Provide more references and inspiration for ad creativity

    ### Parameters:
    - material_id: Reference ad material ID, required parameter
    - industry: Industry ID, e.g., Games: 25308000000
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `materials`: Recommended ad materials list
      - `ad_title`: Ad title
      - `brand_name`: Brand name
      - `cost`: Cost level
      - `ctr`: Click-through rate
      - `favorite`: Whether favorited
      - `id`: Ad ID
      - `industry_key`: Industry key
      - `is_search`: Whether search result
      - `like`: Like count
      - `objective_key`: Ad objective key
      - `tag`: Tag
      - `video_info`: Video information
        - `vid`: Video ID
        - `duration`: Duration in seconds
        - `cover`: Cover image URL
        - `video_url`: Video playback URLs
          - `360p`: 360p quality
          - `480p`: 480p quality
          - `540p`: 540p quality
          - `720p`: 720p quality
        - `width`: Video width
        - `height`: Video height

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_recommended_ads\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"industry\": \"25308000000\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"ad_title\": \"What will you decide?\",
              \"brand_name\": \"Eatventure\",
              \"cost\": 2,
              \"ctr\": 0.07,
              \"favorite\": false,
              \"id\": \"7164756134804979714\",
              \"industry_key\": \"label_25308000000\",
              \"is_search\": false,
              \"like\": 1009024,
              \"objective_key\": \"campaign_objective_conversion\",
              \"tag\": 3,
              \"video_info\": {
                \"vid\": \"v10033g50000ctgjtl7og65ivnpdo87g\",
                \"duration\": 30.016,
                \"cover\": \"https://p16-sign-
    sg.tiktokcdn.com/v0201/ogKcNlWrjIQwDVBDpBbeR7PDQXnAIeA9Dgbb4w~tplv-noop.image\",
                \"video_url\": {
                  \"360p\": \"https://v16m-
    default.tiktokcdn.com/9e086e91176219d756e9c875fb739dc4/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oIQcoRBNNpXbALnjIeLgbKfwWPDDDDIgQ9l6BF\",
                  \"480p\": \"https://v16m-
    default.tiktokcdn.com/2f304931bd351dad0e43e9771364bd78/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/o8lIsnPILWelBwDbDgDuwQj9UlNebAYdDUXBKS\",
                  \"540p\": \"https://v16m-
    default.tiktokcdn.com/351ae3acb3121d42db8a5091811b2340/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQwpeXyWjDBg7KXcBDeDgPnDDbANoISoQIb9Ql\",
                  \"720p\": \"https://v16m-
    default.tiktokcdn.com/a04bacceb906e5336a68158479f5eac5/684d7e29/video/tos/useast2a/tos-
    useast2a-ve-0051c799-euttp/oQQnWCmCDfpgIxegjrKAXZlbIPDNBDDbZQBHw9\"
                },
                \"width\": 720,
                \"height\": 1280
              }
            }
          ]
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        industry (Union[Unset, str]): 行业ID/Industry ID Default: '25308000000'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            material_id=material_id,
            industry=industry,
            country_code=country_code,
        )
    ).parsed
