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
    industry: Union[Unset, str] = "25000000000",
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["industry"] = industry

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_top_ads_spotlight",
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
    industry: Union[Unset, str] = "25000000000",
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门广告聚光灯/Get top ads spotlight

     # [中文]
    ### 用途:
    - 获取特定行业的热门广告聚光灯，展示行业内最受关注的广告案例
    - 分析行业内的广告创意趋势和优秀案例
    - 为广告创意制作提供灵感和参考

    ### 参数:
    - industry: 行业ID，必填参数，如教育行业：25000000000
    - page: 页码，默认1
    - limit: 每页数量，默认20

    ### 返回内容说明:
    - `materials`: 广告素材列表
      - `cost`: 花费等级
      - `ctr`: 点击率
      - `highlight`: 亮点描述
      - `id`: 广告ID
      - `like`: 点赞数
      - `video_info`: 视频信息
        - `vid`: 视频ID
        - `duration`: 时长（秒）
        - `cover`: 封面图片URL
        - `video_url`: 多种画质的视频播放URL
          - `360p`: 360p画质视频URL
          - `480p`: 480p画质视频URL
          - `540p`: 540p画质视频URL
          - `720p`: 720p画质视频URL
        - `width`: 视频宽度
        - `height`: 视频高度
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",
      \"params\": {
        \"industry\": \"25000000000\",
        \"page\": \"1\",
        \"limit\": \"20\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"cost\": 2,
              \"ctr\": 0.14,
              \"highlight\": \"Through the lens of a real person talking his way through the game, the
    video appears credible with commentary that sounds trustworthy.\",
              \"id\": \"7165768841499066370\",
              \"like\": 377333,
              \"video_info\": {
                \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",
                \"duration\": 19.156,
                \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",
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
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get top ads spotlight for specific industries, showcasing the most popular ad cases
    - Analyze creative trends and excellent cases within the industry
    - Provide inspiration and reference for ad creative production

    ### Parameters:
    - industry: Industry ID, required parameter, e.g., Education: 25000000000
    - page: Page number, default 1
    - limit: Items per page, default 20

    ### Return Description:
    - `materials`: Ad materials list
      - `cost`: Cost level
      - `ctr`: Click-through rate
      - `highlight`: Highlight description
      - `id`: Ad ID
      - `like`: Like count
      - `video_info`: Video information
        - `vid`: Video ID
        - `duration`: Duration in seconds
        - `cover`: Cover image URL
        - `video_url`: Video playback URLs in multiple qualities
          - `360p`: 360p quality video URL
          - `480p`: 480p quality video URL
          - `540p`: 540p quality video URL
          - `720p`: 720p quality video URL
        - `width`: Video width
        - `height`: Video height
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",
      \"params\": {
        \"industry\": \"25000000000\",
        \"page\": \"1\",
        \"limit\": \"20\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"cost\": 2,
              \"ctr\": 0.14,
              \"highlight\": \"Through the lens of a real person talking his way through the game, the
    video appears credible with commentary that sounds trustworthy.\",
              \"id\": \"7165768841499066370\",
              \"like\": 377333,
              \"video_info\": {
                \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",
                \"duration\": 19.156,
                \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",
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
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        industry (Union[Unset, str]): 行业ID/Industry ID Default: '25000000000'.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        industry=industry,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    industry: Union[Unset, str] = "25000000000",
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门广告聚光灯/Get top ads spotlight

     # [中文]
    ### 用途:
    - 获取特定行业的热门广告聚光灯，展示行业内最受关注的广告案例
    - 分析行业内的广告创意趋势和优秀案例
    - 为广告创意制作提供灵感和参考

    ### 参数:
    - industry: 行业ID，必填参数，如教育行业：25000000000
    - page: 页码，默认1
    - limit: 每页数量，默认20

    ### 返回内容说明:
    - `materials`: 广告素材列表
      - `cost`: 花费等级
      - `ctr`: 点击率
      - `highlight`: 亮点描述
      - `id`: 广告ID
      - `like`: 点赞数
      - `video_info`: 视频信息
        - `vid`: 视频ID
        - `duration`: 时长（秒）
        - `cover`: 封面图片URL
        - `video_url`: 多种画质的视频播放URL
          - `360p`: 360p画质视频URL
          - `480p`: 480p画质视频URL
          - `540p`: 540p画质视频URL
          - `720p`: 720p画质视频URL
        - `width`: 视频宽度
        - `height`: 视频高度
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",
      \"params\": {
        \"industry\": \"25000000000\",
        \"page\": \"1\",
        \"limit\": \"20\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"cost\": 2,
              \"ctr\": 0.14,
              \"highlight\": \"Through the lens of a real person talking his way through the game, the
    video appears credible with commentary that sounds trustworthy.\",
              \"id\": \"7165768841499066370\",
              \"like\": 377333,
              \"video_info\": {
                \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",
                \"duration\": 19.156,
                \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",
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
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get top ads spotlight for specific industries, showcasing the most popular ad cases
    - Analyze creative trends and excellent cases within the industry
    - Provide inspiration and reference for ad creative production

    ### Parameters:
    - industry: Industry ID, required parameter, e.g., Education: 25000000000
    - page: Page number, default 1
    - limit: Items per page, default 20

    ### Return Description:
    - `materials`: Ad materials list
      - `cost`: Cost level
      - `ctr`: Click-through rate
      - `highlight`: Highlight description
      - `id`: Ad ID
      - `like`: Like count
      - `video_info`: Video information
        - `vid`: Video ID
        - `duration`: Duration in seconds
        - `cover`: Cover image URL
        - `video_url`: Video playback URLs in multiple qualities
          - `360p`: 360p quality video URL
          - `480p`: 480p quality video URL
          - `540p`: 540p quality video URL
          - `720p`: 720p quality video URL
        - `width`: Video width
        - `height`: Video height
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",
      \"params\": {
        \"industry\": \"25000000000\",
        \"page\": \"1\",
        \"limit\": \"20\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"cost\": 2,
              \"ctr\": 0.14,
              \"highlight\": \"Through the lens of a real person talking his way through the game, the
    video appears credible with commentary that sounds trustworthy.\",
              \"id\": \"7165768841499066370\",
              \"like\": 377333,
              \"video_info\": {
                \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",
                \"duration\": 19.156,
                \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",
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
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        industry (Union[Unset, str]): 行业ID/Industry ID Default: '25000000000'.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        industry=industry,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    industry: Union[Unset, str] = "25000000000",
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门广告聚光灯/Get top ads spotlight

     # [中文]
    ### 用途:
    - 获取特定行业的热门广告聚光灯，展示行业内最受关注的广告案例
    - 分析行业内的广告创意趋势和优秀案例
    - 为广告创意制作提供灵感和参考

    ### 参数:
    - industry: 行业ID，必填参数，如教育行业：25000000000
    - page: 页码，默认1
    - limit: 每页数量，默认20

    ### 返回内容说明:
    - `materials`: 广告素材列表
      - `cost`: 花费等级
      - `ctr`: 点击率
      - `highlight`: 亮点描述
      - `id`: 广告ID
      - `like`: 点赞数
      - `video_info`: 视频信息
        - `vid`: 视频ID
        - `duration`: 时长（秒）
        - `cover`: 封面图片URL
        - `video_url`: 多种画质的视频播放URL
          - `360p`: 360p画质视频URL
          - `480p`: 480p画质视频URL
          - `540p`: 540p画质视频URL
          - `720p`: 720p画质视频URL
        - `width`: 视频宽度
        - `height`: 视频高度
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",
      \"params\": {
        \"industry\": \"25000000000\",
        \"page\": \"1\",
        \"limit\": \"20\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"cost\": 2,
              \"ctr\": 0.14,
              \"highlight\": \"Through the lens of a real person talking his way through the game, the
    video appears credible with commentary that sounds trustworthy.\",
              \"id\": \"7165768841499066370\",
              \"like\": 377333,
              \"video_info\": {
                \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",
                \"duration\": 19.156,
                \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",
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
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get top ads spotlight for specific industries, showcasing the most popular ad cases
    - Analyze creative trends and excellent cases within the industry
    - Provide inspiration and reference for ad creative production

    ### Parameters:
    - industry: Industry ID, required parameter, e.g., Education: 25000000000
    - page: Page number, default 1
    - limit: Items per page, default 20

    ### Return Description:
    - `materials`: Ad materials list
      - `cost`: Cost level
      - `ctr`: Click-through rate
      - `highlight`: Highlight description
      - `id`: Ad ID
      - `like`: Like count
      - `video_info`: Video information
        - `vid`: Video ID
        - `duration`: Duration in seconds
        - `cover`: Cover image URL
        - `video_url`: Video playback URLs in multiple qualities
          - `360p`: 360p quality video URL
          - `480p`: 480p quality video URL
          - `540p`: 540p quality video URL
          - `720p`: 720p quality video URL
        - `width`: Video width
        - `height`: Video height
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",
      \"params\": {
        \"industry\": \"25000000000\",
        \"page\": \"1\",
        \"limit\": \"20\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"cost\": 2,
              \"ctr\": 0.14,
              \"highlight\": \"Through the lens of a real person talking his way through the game, the
    video appears credible with commentary that sounds trustworthy.\",
              \"id\": \"7165768841499066370\",
              \"like\": 377333,
              \"video_info\": {
                \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",
                \"duration\": 19.156,
                \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",
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
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        industry (Union[Unset, str]): 行业ID/Industry ID Default: '25000000000'.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        industry=industry,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    industry: Union[Unset, str] = "25000000000",
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门广告聚光灯/Get top ads spotlight

     # [中文]
    ### 用途:
    - 获取特定行业的热门广告聚光灯，展示行业内最受关注的广告案例
    - 分析行业内的广告创意趋势和优秀案例
    - 为广告创意制作提供灵感和参考

    ### 参数:
    - industry: 行业ID，必填参数，如教育行业：25000000000
    - page: 页码，默认1
    - limit: 每页数量，默认20

    ### 返回内容说明:
    - `materials`: 广告素材列表
      - `cost`: 花费等级
      - `ctr`: 点击率
      - `highlight`: 亮点描述
      - `id`: 广告ID
      - `like`: 点赞数
      - `video_info`: 视频信息
        - `vid`: 视频ID
        - `duration`: 时长（秒）
        - `cover`: 封面图片URL
        - `video_url`: 多种画质的视频播放URL
          - `360p`: 360p画质视频URL
          - `480p`: 480p画质视频URL
          - `540p`: 540p画质视频URL
          - `720p`: 720p画质视频URL
        - `width`: 视频宽度
        - `height`: 视频高度
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",
      \"params\": {
        \"industry\": \"25000000000\",
        \"page\": \"1\",
        \"limit\": \"20\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"cost\": 2,
              \"ctr\": 0.14,
              \"highlight\": \"Through the lens of a real person talking his way through the game, the
    video appears credible with commentary that sounds trustworthy.\",
              \"id\": \"7165768841499066370\",
              \"like\": 377333,
              \"video_info\": {
                \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",
                \"duration\": 19.156,
                \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",
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
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get top ads spotlight for specific industries, showcasing the most popular ad cases
    - Analyze creative trends and excellent cases within the industry
    - Provide inspiration and reference for ad creative production

    ### Parameters:
    - industry: Industry ID, required parameter, e.g., Education: 25000000000
    - page: Page number, default 1
    - limit: Items per page, default 20

    ### Return Description:
    - `materials`: Ad materials list
      - `cost`: Cost level
      - `ctr`: Click-through rate
      - `highlight`: Highlight description
      - `id`: Ad ID
      - `like`: Like count
      - `video_info`: Video information
        - `vid`: Video ID
        - `duration`: Duration in seconds
        - `cover`: Cover image URL
        - `video_url`: Video playback URLs in multiple qualities
          - `360p`: 360p quality video URL
          - `480p`: 480p quality video URL
          - `540p`: 540p quality video URL
          - `720p`: 720p quality video URL
        - `width`: Video width
        - `height`: Video height
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_ads_spotlight\",
      \"params\": {
        \"industry\": \"25000000000\",
        \"page\": \"1\",
        \"limit\": \"20\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"materials\": [
            {
              \"cost\": 2,
              \"ctr\": 0.14,
              \"highlight\": \"Through the lens of a real person talking his way through the game, the
    video appears credible with commentary that sounds trustworthy.\",
              \"id\": \"7165768841499066370\",
              \"like\": 377333,
              \"video_info\": {
                \"vid\": \"v0911dg40001cdo7ukjc77ua0r66rqqg\",
                \"duration\": 19.156,
                \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-v-2c3654-us/1c87385bed544878bb94b61816a653a1~tplv-noop.image\",
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
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        industry (Union[Unset, str]): 行业ID/Industry ID Default: '25000000000'.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            industry=industry,
            page=page,
            limit=limit,
        )
    ).parsed
