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
    ads_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ads_id"] = ads_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_ads_detail",
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
    ads_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个广告详情/Get single ad detail

     # [中文]
    ### 用途:
    - 获取TikTok单个广告的详细信息，包括广告素材、创作者信息、互动数据等
    - 分析广告的表现指标，如观看量、点赞数、评论数等核心数据
    - 帮助广告主和营销人员深入了解特定广告的效果和用户反馈

    ### 参数:
    - ads_id: 广告ID，必填参数，可从广告列表或TikTok Ads Creative Center获取

    ### 返回内容说明:
    - `ad_title`: 广告标题
    - `brand_name`: 品牌名称
    - `comment`: 评论数
    - `cost`: 花费等级(1-5)
    - `country_code`: 投放国家代码列表
    - `ctr`: 点击率（百分比）
    - `favorite`: 是否收藏
    - `has_summary`: 是否有摘要
    - `highlight_text`: 高亮文本
    - `id`: 广告ID
    - `industry_key`: 行业标签
    - `is_search`: 是否搜索结果
    - `keyword_list`: 关键词列表
    - `landing_page`: 落地页URL
    - `like`: 点赞数
    - `objective_key`: 广告目标键
    - `objectives`: 广告目标列表
      - `label`: 目标标签
      - `value`: 目标值
    - `pattern_label`: 模式标签列表
    - `share`: 分享数
    - `source`: 来源
    - `source_key`: 来源键值
    - `tag`: 标签
    - `video_info`: 视频信息
      - `vid`: 视频ID
      - `duration`: 时长（秒）
      - `cover`: 封面图URL
      - `video_url`: 视频播放地址
        - `720p`: 720p质量视频URL
      - `width`: 视频宽度
      - `height`: 视频高度
    - `voice_over`: 是否有配音

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",
      \"params\": {
        \"ads_id\": \"7131673574381518849\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",
          \"brand_name\": \"The Bamboo Breeze Shop\",
          \"comment\": 232,
          \"cost\": 2,
          \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],
          \"ctr\": 0.14,
          \"favorite\": false,
          \"has_summary\": true,
          \"highlight_text\": \"\",
          \"id\": \"7131673574381518849\",
          \"industry_key\": \"label_29100000000\",
          \"is_search\": false,
          \"keyword_list\": [
            \"adjustable back posture corrector\",
            \"poor posture\",
            \"eliminate unnecessary back pain\"
          ],
          \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-
    corrector\",
          \"like\": 61242,
          \"objective_key\": \"campaign_objective_conversion\",
          \"objectives\": [
            {
              \"label\": \"campaign_objective_conversion\",
              \"value\": 3
            },
            {
              \"label\": \"campaign_objective_product_sales\",
              \"value\": 15
            }
          ],
          \"pattern_label\": [],
          \"share\": 6486,
          \"source\": \"TikTok Ads Manager\",
          \"source_key\": 1,
          \"tag\": 3,
          \"video_info\": {
            \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",
            \"duration\": 17,
            \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",
            \"video_url\": {
              \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"
            },
            \"width\": 576,
            \"height\": 1024
          },
          \"voice_over\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed information about a single TikTok ad, including creative content, creator info,
    and engagement data
    - Analyze ad performance metrics such as views, likes, comments, and other core statistics
    - Help advertisers and marketers gain deep insights into specific ad effectiveness and user feedback

    ### Parameters:
    - ads_id: Ad ID, required parameter, can be obtained from ad lists or TikTok Ads Creative Center

    ### Return Description:
    - `ad_title`: Ad title
    - `brand_name`: Brand name
    - `comment`: Comment count
    - `cost`: Cost level (1-5)
    - `country_code`: List of target country codes
    - `ctr`: Click-through rate (percentage)
    - `favorite`: Whether favorited
    - `has_summary`: Whether has summary
    - `highlight_text`: Highlight text
    - `id`: Ad ID
    - `industry_key`: Industry label
    - `is_search`: Whether from search results
    - `keyword_list`: List of keywords
    - `landing_page`: Landing page URL
    - `like`: Like count
    - `objective_key`: Ad objective key
    - `objectives`: List of ad objectives
      - `label`: Objective label
      - `value`: Objective value
    - `pattern_label`: List of pattern labels
    - `share`: Share count
    - `source`: Source
    - `source_key`: Source key value
    - `tag`: Tag
    - `video_info`: Video information
      - `vid`: Video ID
      - `duration`: Duration (seconds)
      - `cover`: Cover image URL
      - `video_url`: Video playback URLs
        - `720p`: 720p quality video URL
      - `width`: Video width
      - `height`: Video height
    - `voice_over`: Whether has voice over

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",
      \"params\": {
        \"ads_id\": \"7131673574381518849\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",
          \"brand_name\": \"The Bamboo Breeze Shop\",
          \"comment\": 232,
          \"cost\": 2,
          \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],
          \"ctr\": 0.14,
          \"favorite\": false,
          \"has_summary\": true,
          \"highlight_text\": \"\",
          \"id\": \"7131673574381518849\",
          \"industry_key\": \"label_29100000000\",
          \"is_search\": false,
          \"keyword_list\": [
            \"adjustable back posture corrector\",
            \"poor posture\",
            \"eliminate unnecessary back pain\"
          ],
          \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-
    corrector\",
          \"like\": 61242,
          \"objective_key\": \"campaign_objective_conversion\",
          \"objectives\": [
            {
              \"label\": \"campaign_objective_conversion\",
              \"value\": 3
            },
            {
              \"label\": \"campaign_objective_product_sales\",
              \"value\": 15
            }
          ],
          \"pattern_label\": [],
          \"share\": 6486,
          \"source\": \"TikTok Ads Manager\",
          \"source_key\": 1,
          \"tag\": 3,
          \"video_info\": {
            \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",
            \"duration\": 17,
            \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",
            \"video_url\": {
              \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"
            },
            \"width\": 576,
            \"height\": 1024
          },
          \"voice_over\": true
        }
      }
    }
    ```

    Args:
        ads_id (str): 广告ID/Ad ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        ads_id=ads_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ads_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个广告详情/Get single ad detail

     # [中文]
    ### 用途:
    - 获取TikTok单个广告的详细信息，包括广告素材、创作者信息、互动数据等
    - 分析广告的表现指标，如观看量、点赞数、评论数等核心数据
    - 帮助广告主和营销人员深入了解特定广告的效果和用户反馈

    ### 参数:
    - ads_id: 广告ID，必填参数，可从广告列表或TikTok Ads Creative Center获取

    ### 返回内容说明:
    - `ad_title`: 广告标题
    - `brand_name`: 品牌名称
    - `comment`: 评论数
    - `cost`: 花费等级(1-5)
    - `country_code`: 投放国家代码列表
    - `ctr`: 点击率（百分比）
    - `favorite`: 是否收藏
    - `has_summary`: 是否有摘要
    - `highlight_text`: 高亮文本
    - `id`: 广告ID
    - `industry_key`: 行业标签
    - `is_search`: 是否搜索结果
    - `keyword_list`: 关键词列表
    - `landing_page`: 落地页URL
    - `like`: 点赞数
    - `objective_key`: 广告目标键
    - `objectives`: 广告目标列表
      - `label`: 目标标签
      - `value`: 目标值
    - `pattern_label`: 模式标签列表
    - `share`: 分享数
    - `source`: 来源
    - `source_key`: 来源键值
    - `tag`: 标签
    - `video_info`: 视频信息
      - `vid`: 视频ID
      - `duration`: 时长（秒）
      - `cover`: 封面图URL
      - `video_url`: 视频播放地址
        - `720p`: 720p质量视频URL
      - `width`: 视频宽度
      - `height`: 视频高度
    - `voice_over`: 是否有配音

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",
      \"params\": {
        \"ads_id\": \"7131673574381518849\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",
          \"brand_name\": \"The Bamboo Breeze Shop\",
          \"comment\": 232,
          \"cost\": 2,
          \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],
          \"ctr\": 0.14,
          \"favorite\": false,
          \"has_summary\": true,
          \"highlight_text\": \"\",
          \"id\": \"7131673574381518849\",
          \"industry_key\": \"label_29100000000\",
          \"is_search\": false,
          \"keyword_list\": [
            \"adjustable back posture corrector\",
            \"poor posture\",
            \"eliminate unnecessary back pain\"
          ],
          \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-
    corrector\",
          \"like\": 61242,
          \"objective_key\": \"campaign_objective_conversion\",
          \"objectives\": [
            {
              \"label\": \"campaign_objective_conversion\",
              \"value\": 3
            },
            {
              \"label\": \"campaign_objective_product_sales\",
              \"value\": 15
            }
          ],
          \"pattern_label\": [],
          \"share\": 6486,
          \"source\": \"TikTok Ads Manager\",
          \"source_key\": 1,
          \"tag\": 3,
          \"video_info\": {
            \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",
            \"duration\": 17,
            \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",
            \"video_url\": {
              \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"
            },
            \"width\": 576,
            \"height\": 1024
          },
          \"voice_over\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed information about a single TikTok ad, including creative content, creator info,
    and engagement data
    - Analyze ad performance metrics such as views, likes, comments, and other core statistics
    - Help advertisers and marketers gain deep insights into specific ad effectiveness and user feedback

    ### Parameters:
    - ads_id: Ad ID, required parameter, can be obtained from ad lists or TikTok Ads Creative Center

    ### Return Description:
    - `ad_title`: Ad title
    - `brand_name`: Brand name
    - `comment`: Comment count
    - `cost`: Cost level (1-5)
    - `country_code`: List of target country codes
    - `ctr`: Click-through rate (percentage)
    - `favorite`: Whether favorited
    - `has_summary`: Whether has summary
    - `highlight_text`: Highlight text
    - `id`: Ad ID
    - `industry_key`: Industry label
    - `is_search`: Whether from search results
    - `keyword_list`: List of keywords
    - `landing_page`: Landing page URL
    - `like`: Like count
    - `objective_key`: Ad objective key
    - `objectives`: List of ad objectives
      - `label`: Objective label
      - `value`: Objective value
    - `pattern_label`: List of pattern labels
    - `share`: Share count
    - `source`: Source
    - `source_key`: Source key value
    - `tag`: Tag
    - `video_info`: Video information
      - `vid`: Video ID
      - `duration`: Duration (seconds)
      - `cover`: Cover image URL
      - `video_url`: Video playback URLs
        - `720p`: 720p quality video URL
      - `width`: Video width
      - `height`: Video height
    - `voice_over`: Whether has voice over

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",
      \"params\": {
        \"ads_id\": \"7131673574381518849\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",
          \"brand_name\": \"The Bamboo Breeze Shop\",
          \"comment\": 232,
          \"cost\": 2,
          \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],
          \"ctr\": 0.14,
          \"favorite\": false,
          \"has_summary\": true,
          \"highlight_text\": \"\",
          \"id\": \"7131673574381518849\",
          \"industry_key\": \"label_29100000000\",
          \"is_search\": false,
          \"keyword_list\": [
            \"adjustable back posture corrector\",
            \"poor posture\",
            \"eliminate unnecessary back pain\"
          ],
          \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-
    corrector\",
          \"like\": 61242,
          \"objective_key\": \"campaign_objective_conversion\",
          \"objectives\": [
            {
              \"label\": \"campaign_objective_conversion\",
              \"value\": 3
            },
            {
              \"label\": \"campaign_objective_product_sales\",
              \"value\": 15
            }
          ],
          \"pattern_label\": [],
          \"share\": 6486,
          \"source\": \"TikTok Ads Manager\",
          \"source_key\": 1,
          \"tag\": 3,
          \"video_info\": {
            \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",
            \"duration\": 17,
            \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",
            \"video_url\": {
              \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"
            },
            \"width\": 576,
            \"height\": 1024
          },
          \"voice_over\": true
        }
      }
    }
    ```

    Args:
        ads_id (str): 广告ID/Ad ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        ads_id=ads_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ads_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个广告详情/Get single ad detail

     # [中文]
    ### 用途:
    - 获取TikTok单个广告的详细信息，包括广告素材、创作者信息、互动数据等
    - 分析广告的表现指标，如观看量、点赞数、评论数等核心数据
    - 帮助广告主和营销人员深入了解特定广告的效果和用户反馈

    ### 参数:
    - ads_id: 广告ID，必填参数，可从广告列表或TikTok Ads Creative Center获取

    ### 返回内容说明:
    - `ad_title`: 广告标题
    - `brand_name`: 品牌名称
    - `comment`: 评论数
    - `cost`: 花费等级(1-5)
    - `country_code`: 投放国家代码列表
    - `ctr`: 点击率（百分比）
    - `favorite`: 是否收藏
    - `has_summary`: 是否有摘要
    - `highlight_text`: 高亮文本
    - `id`: 广告ID
    - `industry_key`: 行业标签
    - `is_search`: 是否搜索结果
    - `keyword_list`: 关键词列表
    - `landing_page`: 落地页URL
    - `like`: 点赞数
    - `objective_key`: 广告目标键
    - `objectives`: 广告目标列表
      - `label`: 目标标签
      - `value`: 目标值
    - `pattern_label`: 模式标签列表
    - `share`: 分享数
    - `source`: 来源
    - `source_key`: 来源键值
    - `tag`: 标签
    - `video_info`: 视频信息
      - `vid`: 视频ID
      - `duration`: 时长（秒）
      - `cover`: 封面图URL
      - `video_url`: 视频播放地址
        - `720p`: 720p质量视频URL
      - `width`: 视频宽度
      - `height`: 视频高度
    - `voice_over`: 是否有配音

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",
      \"params\": {
        \"ads_id\": \"7131673574381518849\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",
          \"brand_name\": \"The Bamboo Breeze Shop\",
          \"comment\": 232,
          \"cost\": 2,
          \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],
          \"ctr\": 0.14,
          \"favorite\": false,
          \"has_summary\": true,
          \"highlight_text\": \"\",
          \"id\": \"7131673574381518849\",
          \"industry_key\": \"label_29100000000\",
          \"is_search\": false,
          \"keyword_list\": [
            \"adjustable back posture corrector\",
            \"poor posture\",
            \"eliminate unnecessary back pain\"
          ],
          \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-
    corrector\",
          \"like\": 61242,
          \"objective_key\": \"campaign_objective_conversion\",
          \"objectives\": [
            {
              \"label\": \"campaign_objective_conversion\",
              \"value\": 3
            },
            {
              \"label\": \"campaign_objective_product_sales\",
              \"value\": 15
            }
          ],
          \"pattern_label\": [],
          \"share\": 6486,
          \"source\": \"TikTok Ads Manager\",
          \"source_key\": 1,
          \"tag\": 3,
          \"video_info\": {
            \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",
            \"duration\": 17,
            \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",
            \"video_url\": {
              \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"
            },
            \"width\": 576,
            \"height\": 1024
          },
          \"voice_over\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed information about a single TikTok ad, including creative content, creator info,
    and engagement data
    - Analyze ad performance metrics such as views, likes, comments, and other core statistics
    - Help advertisers and marketers gain deep insights into specific ad effectiveness and user feedback

    ### Parameters:
    - ads_id: Ad ID, required parameter, can be obtained from ad lists or TikTok Ads Creative Center

    ### Return Description:
    - `ad_title`: Ad title
    - `brand_name`: Brand name
    - `comment`: Comment count
    - `cost`: Cost level (1-5)
    - `country_code`: List of target country codes
    - `ctr`: Click-through rate (percentage)
    - `favorite`: Whether favorited
    - `has_summary`: Whether has summary
    - `highlight_text`: Highlight text
    - `id`: Ad ID
    - `industry_key`: Industry label
    - `is_search`: Whether from search results
    - `keyword_list`: List of keywords
    - `landing_page`: Landing page URL
    - `like`: Like count
    - `objective_key`: Ad objective key
    - `objectives`: List of ad objectives
      - `label`: Objective label
      - `value`: Objective value
    - `pattern_label`: List of pattern labels
    - `share`: Share count
    - `source`: Source
    - `source_key`: Source key value
    - `tag`: Tag
    - `video_info`: Video information
      - `vid`: Video ID
      - `duration`: Duration (seconds)
      - `cover`: Cover image URL
      - `video_url`: Video playback URLs
        - `720p`: 720p quality video URL
      - `width`: Video width
      - `height`: Video height
    - `voice_over`: Whether has voice over

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",
      \"params\": {
        \"ads_id\": \"7131673574381518849\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",
          \"brand_name\": \"The Bamboo Breeze Shop\",
          \"comment\": 232,
          \"cost\": 2,
          \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],
          \"ctr\": 0.14,
          \"favorite\": false,
          \"has_summary\": true,
          \"highlight_text\": \"\",
          \"id\": \"7131673574381518849\",
          \"industry_key\": \"label_29100000000\",
          \"is_search\": false,
          \"keyword_list\": [
            \"adjustable back posture corrector\",
            \"poor posture\",
            \"eliminate unnecessary back pain\"
          ],
          \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-
    corrector\",
          \"like\": 61242,
          \"objective_key\": \"campaign_objective_conversion\",
          \"objectives\": [
            {
              \"label\": \"campaign_objective_conversion\",
              \"value\": 3
            },
            {
              \"label\": \"campaign_objective_product_sales\",
              \"value\": 15
            }
          ],
          \"pattern_label\": [],
          \"share\": 6486,
          \"source\": \"TikTok Ads Manager\",
          \"source_key\": 1,
          \"tag\": 3,
          \"video_info\": {
            \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",
            \"duration\": 17,
            \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",
            \"video_url\": {
              \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"
            },
            \"width\": 576,
            \"height\": 1024
          },
          \"voice_over\": true
        }
      }
    }
    ```

    Args:
        ads_id (str): 广告ID/Ad ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        ads_id=ads_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ads_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个广告详情/Get single ad detail

     # [中文]
    ### 用途:
    - 获取TikTok单个广告的详细信息，包括广告素材、创作者信息、互动数据等
    - 分析广告的表现指标，如观看量、点赞数、评论数等核心数据
    - 帮助广告主和营销人员深入了解特定广告的效果和用户反馈

    ### 参数:
    - ads_id: 广告ID，必填参数，可从广告列表或TikTok Ads Creative Center获取

    ### 返回内容说明:
    - `ad_title`: 广告标题
    - `brand_name`: 品牌名称
    - `comment`: 评论数
    - `cost`: 花费等级(1-5)
    - `country_code`: 投放国家代码列表
    - `ctr`: 点击率（百分比）
    - `favorite`: 是否收藏
    - `has_summary`: 是否有摘要
    - `highlight_text`: 高亮文本
    - `id`: 广告ID
    - `industry_key`: 行业标签
    - `is_search`: 是否搜索结果
    - `keyword_list`: 关键词列表
    - `landing_page`: 落地页URL
    - `like`: 点赞数
    - `objective_key`: 广告目标键
    - `objectives`: 广告目标列表
      - `label`: 目标标签
      - `value`: 目标值
    - `pattern_label`: 模式标签列表
    - `share`: 分享数
    - `source`: 来源
    - `source_key`: 来源键值
    - `tag`: 标签
    - `video_info`: 视频信息
      - `vid`: 视频ID
      - `duration`: 时长（秒）
      - `cover`: 封面图URL
      - `video_url`: 视频播放地址
        - `720p`: 720p质量视频URL
      - `width`: 视频宽度
      - `height`: 视频高度
    - `voice_over`: 是否有配音

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",
      \"params\": {
        \"ads_id\": \"7131673574381518849\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",
          \"brand_name\": \"The Bamboo Breeze Shop\",
          \"comment\": 232,
          \"cost\": 2,
          \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],
          \"ctr\": 0.14,
          \"favorite\": false,
          \"has_summary\": true,
          \"highlight_text\": \"\",
          \"id\": \"7131673574381518849\",
          \"industry_key\": \"label_29100000000\",
          \"is_search\": false,
          \"keyword_list\": [
            \"adjustable back posture corrector\",
            \"poor posture\",
            \"eliminate unnecessary back pain\"
          ],
          \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-
    corrector\",
          \"like\": 61242,
          \"objective_key\": \"campaign_objective_conversion\",
          \"objectives\": [
            {
              \"label\": \"campaign_objective_conversion\",
              \"value\": 3
            },
            {
              \"label\": \"campaign_objective_product_sales\",
              \"value\": 15
            }
          ],
          \"pattern_label\": [],
          \"share\": 6486,
          \"source\": \"TikTok Ads Manager\",
          \"source_key\": 1,
          \"tag\": 3,
          \"video_info\": {
            \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",
            \"duration\": 17,
            \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",
            \"video_url\": {
              \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"
            },
            \"width\": 576,
            \"height\": 1024
          },
          \"voice_over\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed information about a single TikTok ad, including creative content, creator info,
    and engagement data
    - Analyze ad performance metrics such as views, likes, comments, and other core statistics
    - Help advertisers and marketers gain deep insights into specific ad effectiveness and user feedback

    ### Parameters:
    - ads_id: Ad ID, required parameter, can be obtained from ad lists or TikTok Ads Creative Center

    ### Return Description:
    - `ad_title`: Ad title
    - `brand_name`: Brand name
    - `comment`: Comment count
    - `cost`: Cost level (1-5)
    - `country_code`: List of target country codes
    - `ctr`: Click-through rate (percentage)
    - `favorite`: Whether favorited
    - `has_summary`: Whether has summary
    - `highlight_text`: Highlight text
    - `id`: Ad ID
    - `industry_key`: Industry label
    - `is_search`: Whether from search results
    - `keyword_list`: List of keywords
    - `landing_page`: Landing page URL
    - `like`: Like count
    - `objective_key`: Ad objective key
    - `objectives`: List of ad objectives
      - `label`: Objective label
      - `value`: Objective value
    - `pattern_label`: List of pattern labels
    - `share`: Share count
    - `source`: Source
    - `source_key`: Source key value
    - `tag`: Tag
    - `video_info`: Video information
      - `vid`: Video ID
      - `duration`: Duration (seconds)
      - `cover`: Cover image URL
      - `video_url`: Video playback URLs
        - `720p`: 720p quality video URL
      - `width`: Video width
      - `height`: Video height
    - `voice_over`: Whether has voice over

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ads_detail\",
      \"params\": {
        \"ads_id\": \"7131673574381518849\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"ad_title\": \"BLACK FRIDAY SALE at 50% OFF + FREE SHIPPING\",
          \"brand_name\": \"The Bamboo Breeze Shop\",
          \"comment\": 232,
          \"cost\": 2,
          \"country_code\": [\"US\", \"CA\", \"PH\", \"SE\", \"FI\"],
          \"ctr\": 0.14,
          \"favorite\": false,
          \"has_summary\": true,
          \"highlight_text\": \"\",
          \"id\": \"7131673574381518849\",
          \"industry_key\": \"label_29100000000\",
          \"is_search\": false,
          \"keyword_list\": [
            \"adjustable back posture corrector\",
            \"poor posture\",
            \"eliminate unnecessary back pain\"
          ],
          \"landing_page\": \"https://thebamboobreezeshop.com/products/adjustable-back-shoulder-posture-
    corrector\",
          \"like\": 61242,
          \"objective_key\": \"campaign_objective_conversion\",
          \"objectives\": [
            {
              \"label\": \"campaign_objective_conversion\",
              \"value\": 3
            },
            {
              \"label\": \"campaign_objective_product_sales\",
              \"value\": 15
            }
          ],
          \"pattern_label\": [],
          \"share\": 6486,
          \"source\": \"TikTok Ads Manager\",
          \"source_key\": 1,
          \"tag\": 3,
          \"video_info\": {
            \"vid\": \"v12025gd0000cuavia7og65o5g7ucnb0\",
            \"duration\": 17,
            \"cover\": \"https://p16-sign-va.tiktokcdn.com/xxx\",
            \"video_url\": {
              \"720p\": \"https://v16m-default.tiktokcdn.com/xxx\"
            },
            \"width\": 576,
            \"height\": 1024
          },
          \"voice_over\": true
        }
      }
    }
    ```

    Args:
        ads_id (str): 广告ID/Ad ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            ads_id=ads_id,
        )
    ).parsed
