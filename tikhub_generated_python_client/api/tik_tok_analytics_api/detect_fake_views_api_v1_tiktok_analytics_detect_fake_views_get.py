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
    item_id: str,
    content_category: Union[Unset, str] = "default",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["item_id"] = item_id

    params["content_category"] = content_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/analytics/detect_fake_views",
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
    item_id: str,
    content_category: Union[Unset, str] = "default",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""检测视频虚假流量分析/Detect fake views in video

     # [中文]
    ### 用途:
    - 通过高级算法分析TikTok视频流量数据，精确检测可能存在的虚假观看量和不自然互动
    - 基于TikTok赛马机制(Traffic Pool)流量池理论，评估内容真实性和流量质量
    - 提供全面的欺诈风险分析，包含8种维度、20+指标的深度评估
    - 为创作者、MCN机构和内容管理者提供专业的流量质量报告和优化建议

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频URL中提取(例如: https://www.tiktok.com/@tiktok/video/7460937381265411370
    中的7460937381265411370)
    - content_category: 内容分类，可选参数，影响互动率基准值，选项包括:
      - default: 默认类别，通用内容
      - entertainment: 娱乐内容，预期有较高互动率
      - education: 教育内容，预期有适中互动和较高收藏率
      - product: 产品内容，预期有较低互动但较高转化
      - verified_large: 大型认证账号，预期互动率适当降低

    ### 返回内容详解:
    - `video_metrics`: 视频核心指标
      - `total_views`: 总观看量，视频被观看的总次数
      - `total_likes`: 总点赞数，用户点赞互动次数
      - `total_comments`: 总评论数，用户评论互动次数
      - `total_favorites`: 总收藏数，用户收藏次数
      - `total_shares`: 总分享数，用户分享次数
      - `engagement_rates`: 互动率指标，值越高越好
        - `like_ratio`: 点赞率，正常值 1-10%，大账号可能较低
        - `comment_ratio`: 评论率，正常值 0.1-0.5%，高于1%极佳
        - `favorite_ratio`: 收藏率，正常值 0.05-0.8%
        - `share_ratio`: 分享率，正常值 0.05-0.5%，高于1%极佳

    - `creator_metrics`: 创作者账号健康指标
      - `account_age_days`: 账号存在天数，越长越可信
      - `follower_count`: 粉丝数量，影响预期观看量
      - `verified`: 是否验证账号，认证账号可信度更高
      - `trust_score`: 账号信任度评分(0-100)，越高越可信

    - `content_metrics`: 内容质量指标
      - `content_type`: 内容类型(video, image等)
      - `created_by_ai`: 是否AI生成，AI生成内容可能有特定流量模式
      - `high_quality_upload`: 是否高质量上传，高质量上传更可信

    - `fake_view_analysis`: 虚假流量综合分析
      - `fake_score`: 虚假流量评分(0-100)，评分越低越好:
        - 0-20: 极低风险，自然流量模式
        - 20-40: 低风险，可能有少量异常但不构成问题
        - 40-60: 中等风险，存在值得关注的异常
        - 60-80: 高风险，明显的虚假流量特征
        - 80-100: 极高风险，几乎确定存在虚假流量
      - `confidence_level`: 风险等级，分为\"Minimal\", \"Low\", \"Medium\", \"High\"
      - `estimated_fake_views`: 估计虚假观看量，基于虚假流量模型推算
      - `fake_view_percentage`: 虚假观看百分比，虚假占总量的比例
      - `is_suspicious`: 是否可疑，综合判断是否需要关注
      - `main_detection_reason`: 主要检测原因，最显著的异常特征
      - `component_scores`: 各维度异常评分，各项都是0-100，越低越好:
        - `engagement_score`: 互动异常评分
        - `distribution_score`: 分布异常评分
        - `consistency_score`: 一致性异常评分
        - `creator_credibility_score`: 创作者可信度异常评分
        - `content_authenticity_score`: 内容真实性异常评分
        - `follower_correlation_score`: 粉丝相关性异常评分
        - `racing_mechanism_score`: 赛马机制异常评分
        - `fan_growth_score`: 粉丝增长异常评分

    - `traffic_pool`: 流量池分析(TikTok赛马机制)
      - `current_tier`: 当前流量池级别(1-8)，越高代表流量越大
      - `current_tier_name`: 当前流量池名称
      - `expected_tier`: 预期流量池级别，基于有机流量预测
      - `expected_tier_name`: 预期流量池名称
      - `current_views_range`: 当前流量池预期观看范围
      - `expected_views_range`: 预期流量池观看范围
      - `estimated_organic_views`: 估计有机观看量，扣除虚假后的真实观看

    - `suspicious_features`: 可疑特征列表，检测到的具体异常现象

    - `recommendations`: 建议操作
      - `action`: 建议操作类型，可能值包括:
        - `no_action`: 无需操作，健康内容
        - `monitor`: 持续监控，存在轻微异常
        - `scheduled_review`: 安排审核，存在值得关注的异常
        - `immediate_review`: 立即审核，存在严重异常
      - `risk_level`: 风险等级(\"low\", \"medium\", \"high\", \"critical\")
      - `potential_revenue_impact`: 潜在收益影响
      - `suggested_steps`: 建议步骤，具体操作建议

    - `mcn_report`: (可选)MCN商业影响分析报告，适用于商业账号
      - `summary`: 摘要信息
      - `business_impact`: 商业影响评估
        - `revenue_impact`: 收益影响评估
        - `brand_safety_impact`: 品牌安全影响
        - `platform_relationship`: 平台关系影响
        - `contract_impact`: 合约影响评估
      - `recommended_actions`: 建议操作清单
      - `historical_context`: 历史背景数据

    ### 特性与优势:
    - 基于TikTok原生流量池(Traffic Pool)理论构建的精确评估系统
    - 8个维度、20+指标的全面分析，覆盖流量、互动、创作者、内容等全方位评估
    - 自适应算法，根据账号规模、认证状态、内容类型自动调整阈值
    - 基于大数据统计模型的异常检测，准确识别不自然流量模式
    - 为不同规模账号(微型、小型、中型、大型、超大型)提供定制化评估标准
    - 提供详细的商业影响分析和具体可行的建议步骤

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/detect_fake_views\",
      \"params\": {
        \"item_id\": \"7460937381265411370\",
        \"content_category\": \"verified_large\"
      },
      \"data\": {
        \"video_metrics\": {
          \"total_views\": 159414915,
          \"total_likes\": 15817234,
          \"total_comments\": 392493,
          \"total_favorites\": 1051470,
          \"total_shares\": 1312741,
          \"engagement_rates\": {
            \"like_ratio\": 0.09922,
            \"comment_ratio\": 0.00246,
            \"favorite_ratio\": 0.0066,
            \"share_ratio\": 0.00823
          }
        },
        \"creator_metrics\": {
          \"account_age_days\": 3733.94,
          \"follower_count\": 89827771,
          \"verified\": true,
          \"trust_score\": 100
        },
        \"content_metrics\": {
          \"content_type\": \"video\",
          \"created_by_ai\": false,
          \"high_quality_upload\": true
        },
        \"fake_view_analysis\": {
          \"fake_score\": 7.16,
          \"confidence_level\": \"Minimal\",
          \"estimated_fake_views\": 7970745,
          \"fake_view_percentage\": 5.0,
          \"is_suspicious\": false,
          \"main_detection_reason\": \"Statistical View Anomalies\",
          \"component_scores\": {
            \"engagement_score\": 0.0,
            \"distribution_score\": 10.0,
            \"consistency_score\": 0,
            \"creator_credibility_score\": 0,
            \"content_authenticity_score\": 34.0,
            \"follower_correlation_score\": 35.0,
            \"racing_mechanism_score\": 0,
            \"fan_growth_score\": 45
          }
        },
        \"traffic_pool\": {
          \"current_tier\": 8,
          \"current_tier_name\": \"8th-Level Traffic Pool\",
          \"expected_tier\": 8,
          \"expected_tier_name\": \"8th-Level Traffic Pool\",
          \"current_views_range\": \"30M+\",
          \"expected_views_range\": \"30M+\",
          \"estimated_organic_views\": 148000807
        },
        \"suspicious_features\": [
          \"Suspicious: Reached 100000 followers from 10000 in only 31 days\",
          \"Suspicious: Account gaining 24063 followers per day on average\"
        ],
        \"recommendations\": {
          \"action\": \"no_action\",
          \"risk_level\": \"low\",
          \"potential_revenue_impact\": \"minimal\",
          \"suggested_steps\": [
            \"No immediate action required\",
            \"Include in routine monitoring\"
          ]
        },
        \"mcn_report\": {
          \"summary\": {
            \"estimated_revenue_impact\": 7970.745,
            \"recommended_actions\": \"No immediate action required\"
          },
          \"business_impact\": {
            \"revenue_impact\": {
              \"level\": \"low\",
              \"estimated_amount\": 7970.745
            },
            \"brand_safety_impact\": {
              \"level\": \"minimal\"
            },
            \"platform_relationship\": {
              \"status\": \"good\"
            }
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Analyze TikTok video traffic data using advanced algorithms to precisely detect potential fake
    views and unnatural engagement
    - Evaluate content authenticity and traffic quality based on TikTok's Traffic Pool theory
    - Provide comprehensive fraud risk analysis with in-depth assessment across 8 dimensions and 20+
    metrics
    - Deliver professional traffic quality reports and optimization recommendations for creators, MCN
    agencies, and content managers

    ### Parameters:
    - item_id: Video ID, required parameter, can be extracted from video URL (e.g., 7460937381265411370
    from https://www.tiktok.com/@tiktok/video/7460937381265411370)
    - content_category: Content category, optional parameter, affects engagement rate benchmarks,
    options include:
      - default: Default category for general content
      - entertainment: Entertainment content, expected to have higher engagement
      - education: Educational content, expected to have moderate engagement and higher save rates
      - product: Product content, expected to have lower engagement but higher conversion
      - verified_large: Large verified accounts, expected to have appropriately lower engagement rates

    ### Return Description:
    - `video_metrics`: Core video metrics
      - `total_views`: Total number of views
      - `total_likes`: Total number of likes
      - `total_comments`: Total number of comments
      - `total_favorites`: Total number of saves
      - `total_shares`: Total number of shares
      - `engagement_rates`: Engagement rate metrics, higher is better
        - `like_ratio`: Like rate, normal range 1-10%, may be lower for large accounts
        - `comment_ratio`: Comment rate, normal range 0.1-0.5%, excellent if above 1%
        - `favorite_ratio`: Save rate, normal range 0.05-0.8%
        - `share_ratio`: Share rate, normal range 0.05-0.5%, excellent if above 1%

    - `creator_metrics`: Creator account health indicators
      - `account_age_days`: Account age in days, longer is more credible
      - `follower_count`: Number of followers, affects expected view count
      - `verified`: Whether account is verified, verified accounts have higher credibility
      - `trust_score`: Account trust score (0-100), higher is more trustworthy

    - `content_metrics`: Content quality indicators
      - `content_type`: Content type (video, image, etc.)
      - `created_by_ai`: Whether AI-generated, AI-generated content may have specific traffic patterns
      - `high_quality_upload`: Whether high-quality upload, high-quality uploads are more credible

    - `fake_view_analysis`: Comprehensive fake traffic analysis
      - `fake_score`: Fake view score (0-100), lower is better:
        - 0-20: Very low risk, natural traffic patterns
        - 20-40: Low risk, may have minor anomalies but not problematic
        - 40-60: Medium risk, anomalies worth attention
        - 60-80: High risk, obvious fake traffic characteristics
        - 80-100: Very high risk, almost certainly fake traffic
      - `confidence_level`: Risk level, categorized as \"Minimal\", \"Low\", \"Medium\", \"High\"
      - `estimated_fake_views`: Estimated fake views, calculated based on fake traffic model
      - `fake_view_percentage`: Fake view percentage, proportion of fake views to total views
      - `is_suspicious`: Whether suspicious, comprehensive judgment if attention is needed
      - `main_detection_reason`: Main detection reason, most significant anomaly feature
      - `component_scores`: Dimensional anomaly scores, each 0-100, lower is better:
        - `engagement_score`: Engagement anomaly score
        - `distribution_score`: Distribution anomaly score
        - `consistency_score`: Consistency anomaly score
        - `creator_credibility_score`: Creator credibility anomaly score
        - `content_authenticity_score`: Content authenticity anomaly score
        - `follower_correlation_score`: Follower correlation anomaly score
        - `racing_mechanism_score`: Racing mechanism anomaly score
        - `fan_growth_score`: Fan growth anomaly score

    - `traffic_pool`: Traffic pool analysis (TikTok racing mechanism)
      - `current_tier`: Current traffic pool level (1-8), higher means more traffic
      - `current_tier_name`: Current traffic pool name
      - `expected_tier`: Expected traffic pool level, based on organic traffic prediction
      - `expected_tier_name`: Expected traffic pool name
      - `current_views_range`: Current traffic pool expected view range
      - `expected_views_range`: Expected traffic pool view range
      - `estimated_organic_views`: Estimated organic views, real views after deducting fake ones

    - `suspicious_features`: List of suspicious features, specific detected anomalies

    - `recommendations`: Recommended actions
      - `action`: Recommended action type, possible values include:
        - `no_action`: No action needed, healthy content
        - `monitor`: Continuous monitoring, minor anomalies present
        - `scheduled_review`: Schedule review, anomalies worth attention
        - `immediate_review`: Immediate review, serious anomalies present
      - `risk_level`: Risk level (\"low\", \"medium\", \"high\", \"critical\")
      - `potential_revenue_impact`: Potential revenue impact
      - `suggested_steps`: Suggested steps, specific action recommendations

    - `mcn_report`: (Optional) MCN business impact analysis report, applicable for business accounts
      - `summary`: Summary information
      - `business_impact`: Business impact assessment
        - `revenue_impact`: Revenue impact assessment
        - `brand_safety_impact`: Brand safety impact
        - `platform_relationship`: Platform relationship impact
        - `contract_impact`: Contract impact assessment
      - `recommended_actions`: Recommended action list
      - `historical_context`: Historical background data

    ### Features and Advantages:
    - Precise evaluation system built on TikTok's native Traffic Pool theory
    - Comprehensive analysis across 8 dimensions and 20+ metrics, covering traffic, engagement, creator,
    content, etc.
    - Adaptive algorithm automatically adjusts thresholds based on account size, verification status,
    content type
    - Anomaly detection based on big data statistical models, accurately identifies unnatural traffic
    patterns
    - Provides customized evaluation standards for different account sizes (micro, small, medium, large,
    extra-large)
    - Delivers detailed business impact analysis and specific, actionable recommendations

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/detect_fake_views\",
      \"params\": {
        \"item_id\": \"7460937381265411370\",
        \"content_category\": \"verified_large\"
      },
      \"data\": {
        \"video_metrics\": {
          \"total_views\": 159414915,
          \"total_likes\": 15817234,
          \"total_comments\": 392493,
          \"total_favorites\": 1051470,
          \"total_shares\": 1312741,
          \"engagement_rates\": {
            \"like_ratio\": 0.09922,
            \"comment_ratio\": 0.00246,
            \"favorite_ratio\": 0.0066,
            \"share_ratio\": 0.00823
          }
        },
        \"creator_metrics\": {
          \"account_age_days\": 3733.94,
          \"follower_count\": 89827771,
          \"verified\": true,
          \"trust_score\": 100
        },
        \"content_metrics\": {
          \"content_type\": \"video\",
          \"created_by_ai\": false,
          \"high_quality_upload\": true
        },
        \"fake_view_analysis\": {
          \"fake_score\": 7.16,
          \"confidence_level\": \"Minimal\",
          \"estimated_fake_views\": 7970745,
          \"fake_view_percentage\": 5.0,
          \"is_suspicious\": false,
          \"main_detection_reason\": \"Statistical View Anomalies\",
          \"component_scores\": {
            \"engagement_score\": 0.0,
            \"distribution_score\": 10.0,
            \"consistency_score\": 0,
            \"creator_credibility_score\": 0,
            \"content_authenticity_score\": 34.0,
            \"follower_correlation_score\": 35.0,
            \"racing_mechanism_score\": 0,
            \"fan_growth_score\": 45
          }
        },
        \"traffic_pool\": {
          \"current_tier\": 8,
          \"current_tier_name\": \"8th-Level Traffic Pool\",
          \"expected_tier\": 8,
          \"expected_tier_name\": \"8th-Level Traffic Pool\",
          \"current_views_range\": \"30M+\",
          \"expected_views_range\": \"30M+\",
          \"estimated_organic_views\": 148000807
        },
        \"suspicious_features\": [
          \"Suspicious: Reached 100000 followers from 10000 in only 31 days\",
          \"Suspicious: Account gaining 24063 followers per day on average\"
        ],
        \"recommendations\": {
          \"action\": \"no_action\",
          \"risk_level\": \"low\",
          \"potential_revenue_impact\": \"minimal\",
          \"suggested_steps\": [
            \"No immediate action required\",
            \"Include in routine monitoring\"
          ]
        },
        \"mcn_report\": {
          \"summary\": {
            \"estimated_revenue_impact\": 7970.745,
            \"recommended_actions\": \"No immediate action required\"
          },
          \"business_impact\": {
            \"revenue_impact\": {
              \"level\": \"low\",
              \"estimated_amount\": 7970.745
            },
            \"brand_safety_impact\": {
              \"level\": \"minimal\"
            },
            \"platform_relationship\": {
              \"status\": \"good\"
            }
          }
        }
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id
        content_category (Union[Unset, str]): 内容分类/Content category, options: default,
            entertainment, education, product, verified_large Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        content_category=content_category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    item_id: str,
    content_category: Union[Unset, str] = "default",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""检测视频虚假流量分析/Detect fake views in video

     # [中文]
    ### 用途:
    - 通过高级算法分析TikTok视频流量数据，精确检测可能存在的虚假观看量和不自然互动
    - 基于TikTok赛马机制(Traffic Pool)流量池理论，评估内容真实性和流量质量
    - 提供全面的欺诈风险分析，包含8种维度、20+指标的深度评估
    - 为创作者、MCN机构和内容管理者提供专业的流量质量报告和优化建议

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频URL中提取(例如: https://www.tiktok.com/@tiktok/video/7460937381265411370
    中的7460937381265411370)
    - content_category: 内容分类，可选参数，影响互动率基准值，选项包括:
      - default: 默认类别，通用内容
      - entertainment: 娱乐内容，预期有较高互动率
      - education: 教育内容，预期有适中互动和较高收藏率
      - product: 产品内容，预期有较低互动但较高转化
      - verified_large: 大型认证账号，预期互动率适当降低

    ### 返回内容详解:
    - `video_metrics`: 视频核心指标
      - `total_views`: 总观看量，视频被观看的总次数
      - `total_likes`: 总点赞数，用户点赞互动次数
      - `total_comments`: 总评论数，用户评论互动次数
      - `total_favorites`: 总收藏数，用户收藏次数
      - `total_shares`: 总分享数，用户分享次数
      - `engagement_rates`: 互动率指标，值越高越好
        - `like_ratio`: 点赞率，正常值 1-10%，大账号可能较低
        - `comment_ratio`: 评论率，正常值 0.1-0.5%，高于1%极佳
        - `favorite_ratio`: 收藏率，正常值 0.05-0.8%
        - `share_ratio`: 分享率，正常值 0.05-0.5%，高于1%极佳

    - `creator_metrics`: 创作者账号健康指标
      - `account_age_days`: 账号存在天数，越长越可信
      - `follower_count`: 粉丝数量，影响预期观看量
      - `verified`: 是否验证账号，认证账号可信度更高
      - `trust_score`: 账号信任度评分(0-100)，越高越可信

    - `content_metrics`: 内容质量指标
      - `content_type`: 内容类型(video, image等)
      - `created_by_ai`: 是否AI生成，AI生成内容可能有特定流量模式
      - `high_quality_upload`: 是否高质量上传，高质量上传更可信

    - `fake_view_analysis`: 虚假流量综合分析
      - `fake_score`: 虚假流量评分(0-100)，评分越低越好:
        - 0-20: 极低风险，自然流量模式
        - 20-40: 低风险，可能有少量异常但不构成问题
        - 40-60: 中等风险，存在值得关注的异常
        - 60-80: 高风险，明显的虚假流量特征
        - 80-100: 极高风险，几乎确定存在虚假流量
      - `confidence_level`: 风险等级，分为\"Minimal\", \"Low\", \"Medium\", \"High\"
      - `estimated_fake_views`: 估计虚假观看量，基于虚假流量模型推算
      - `fake_view_percentage`: 虚假观看百分比，虚假占总量的比例
      - `is_suspicious`: 是否可疑，综合判断是否需要关注
      - `main_detection_reason`: 主要检测原因，最显著的异常特征
      - `component_scores`: 各维度异常评分，各项都是0-100，越低越好:
        - `engagement_score`: 互动异常评分
        - `distribution_score`: 分布异常评分
        - `consistency_score`: 一致性异常评分
        - `creator_credibility_score`: 创作者可信度异常评分
        - `content_authenticity_score`: 内容真实性异常评分
        - `follower_correlation_score`: 粉丝相关性异常评分
        - `racing_mechanism_score`: 赛马机制异常评分
        - `fan_growth_score`: 粉丝增长异常评分

    - `traffic_pool`: 流量池分析(TikTok赛马机制)
      - `current_tier`: 当前流量池级别(1-8)，越高代表流量越大
      - `current_tier_name`: 当前流量池名称
      - `expected_tier`: 预期流量池级别，基于有机流量预测
      - `expected_tier_name`: 预期流量池名称
      - `current_views_range`: 当前流量池预期观看范围
      - `expected_views_range`: 预期流量池观看范围
      - `estimated_organic_views`: 估计有机观看量，扣除虚假后的真实观看

    - `suspicious_features`: 可疑特征列表，检测到的具体异常现象

    - `recommendations`: 建议操作
      - `action`: 建议操作类型，可能值包括:
        - `no_action`: 无需操作，健康内容
        - `monitor`: 持续监控，存在轻微异常
        - `scheduled_review`: 安排审核，存在值得关注的异常
        - `immediate_review`: 立即审核，存在严重异常
      - `risk_level`: 风险等级(\"low\", \"medium\", \"high\", \"critical\")
      - `potential_revenue_impact`: 潜在收益影响
      - `suggested_steps`: 建议步骤，具体操作建议

    - `mcn_report`: (可选)MCN商业影响分析报告，适用于商业账号
      - `summary`: 摘要信息
      - `business_impact`: 商业影响评估
        - `revenue_impact`: 收益影响评估
        - `brand_safety_impact`: 品牌安全影响
        - `platform_relationship`: 平台关系影响
        - `contract_impact`: 合约影响评估
      - `recommended_actions`: 建议操作清单
      - `historical_context`: 历史背景数据

    ### 特性与优势:
    - 基于TikTok原生流量池(Traffic Pool)理论构建的精确评估系统
    - 8个维度、20+指标的全面分析，覆盖流量、互动、创作者、内容等全方位评估
    - 自适应算法，根据账号规模、认证状态、内容类型自动调整阈值
    - 基于大数据统计模型的异常检测，准确识别不自然流量模式
    - 为不同规模账号(微型、小型、中型、大型、超大型)提供定制化评估标准
    - 提供详细的商业影响分析和具体可行的建议步骤

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/detect_fake_views\",
      \"params\": {
        \"item_id\": \"7460937381265411370\",
        \"content_category\": \"verified_large\"
      },
      \"data\": {
        \"video_metrics\": {
          \"total_views\": 159414915,
          \"total_likes\": 15817234,
          \"total_comments\": 392493,
          \"total_favorites\": 1051470,
          \"total_shares\": 1312741,
          \"engagement_rates\": {
            \"like_ratio\": 0.09922,
            \"comment_ratio\": 0.00246,
            \"favorite_ratio\": 0.0066,
            \"share_ratio\": 0.00823
          }
        },
        \"creator_metrics\": {
          \"account_age_days\": 3733.94,
          \"follower_count\": 89827771,
          \"verified\": true,
          \"trust_score\": 100
        },
        \"content_metrics\": {
          \"content_type\": \"video\",
          \"created_by_ai\": false,
          \"high_quality_upload\": true
        },
        \"fake_view_analysis\": {
          \"fake_score\": 7.16,
          \"confidence_level\": \"Minimal\",
          \"estimated_fake_views\": 7970745,
          \"fake_view_percentage\": 5.0,
          \"is_suspicious\": false,
          \"main_detection_reason\": \"Statistical View Anomalies\",
          \"component_scores\": {
            \"engagement_score\": 0.0,
            \"distribution_score\": 10.0,
            \"consistency_score\": 0,
            \"creator_credibility_score\": 0,
            \"content_authenticity_score\": 34.0,
            \"follower_correlation_score\": 35.0,
            \"racing_mechanism_score\": 0,
            \"fan_growth_score\": 45
          }
        },
        \"traffic_pool\": {
          \"current_tier\": 8,
          \"current_tier_name\": \"8th-Level Traffic Pool\",
          \"expected_tier\": 8,
          \"expected_tier_name\": \"8th-Level Traffic Pool\",
          \"current_views_range\": \"30M+\",
          \"expected_views_range\": \"30M+\",
          \"estimated_organic_views\": 148000807
        },
        \"suspicious_features\": [
          \"Suspicious: Reached 100000 followers from 10000 in only 31 days\",
          \"Suspicious: Account gaining 24063 followers per day on average\"
        ],
        \"recommendations\": {
          \"action\": \"no_action\",
          \"risk_level\": \"low\",
          \"potential_revenue_impact\": \"minimal\",
          \"suggested_steps\": [
            \"No immediate action required\",
            \"Include in routine monitoring\"
          ]
        },
        \"mcn_report\": {
          \"summary\": {
            \"estimated_revenue_impact\": 7970.745,
            \"recommended_actions\": \"No immediate action required\"
          },
          \"business_impact\": {
            \"revenue_impact\": {
              \"level\": \"low\",
              \"estimated_amount\": 7970.745
            },
            \"brand_safety_impact\": {
              \"level\": \"minimal\"
            },
            \"platform_relationship\": {
              \"status\": \"good\"
            }
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Analyze TikTok video traffic data using advanced algorithms to precisely detect potential fake
    views and unnatural engagement
    - Evaluate content authenticity and traffic quality based on TikTok's Traffic Pool theory
    - Provide comprehensive fraud risk analysis with in-depth assessment across 8 dimensions and 20+
    metrics
    - Deliver professional traffic quality reports and optimization recommendations for creators, MCN
    agencies, and content managers

    ### Parameters:
    - item_id: Video ID, required parameter, can be extracted from video URL (e.g., 7460937381265411370
    from https://www.tiktok.com/@tiktok/video/7460937381265411370)
    - content_category: Content category, optional parameter, affects engagement rate benchmarks,
    options include:
      - default: Default category for general content
      - entertainment: Entertainment content, expected to have higher engagement
      - education: Educational content, expected to have moderate engagement and higher save rates
      - product: Product content, expected to have lower engagement but higher conversion
      - verified_large: Large verified accounts, expected to have appropriately lower engagement rates

    ### Return Description:
    - `video_metrics`: Core video metrics
      - `total_views`: Total number of views
      - `total_likes`: Total number of likes
      - `total_comments`: Total number of comments
      - `total_favorites`: Total number of saves
      - `total_shares`: Total number of shares
      - `engagement_rates`: Engagement rate metrics, higher is better
        - `like_ratio`: Like rate, normal range 1-10%, may be lower for large accounts
        - `comment_ratio`: Comment rate, normal range 0.1-0.5%, excellent if above 1%
        - `favorite_ratio`: Save rate, normal range 0.05-0.8%
        - `share_ratio`: Share rate, normal range 0.05-0.5%, excellent if above 1%

    - `creator_metrics`: Creator account health indicators
      - `account_age_days`: Account age in days, longer is more credible
      - `follower_count`: Number of followers, affects expected view count
      - `verified`: Whether account is verified, verified accounts have higher credibility
      - `trust_score`: Account trust score (0-100), higher is more trustworthy

    - `content_metrics`: Content quality indicators
      - `content_type`: Content type (video, image, etc.)
      - `created_by_ai`: Whether AI-generated, AI-generated content may have specific traffic patterns
      - `high_quality_upload`: Whether high-quality upload, high-quality uploads are more credible

    - `fake_view_analysis`: Comprehensive fake traffic analysis
      - `fake_score`: Fake view score (0-100), lower is better:
        - 0-20: Very low risk, natural traffic patterns
        - 20-40: Low risk, may have minor anomalies but not problematic
        - 40-60: Medium risk, anomalies worth attention
        - 60-80: High risk, obvious fake traffic characteristics
        - 80-100: Very high risk, almost certainly fake traffic
      - `confidence_level`: Risk level, categorized as \"Minimal\", \"Low\", \"Medium\", \"High\"
      - `estimated_fake_views`: Estimated fake views, calculated based on fake traffic model
      - `fake_view_percentage`: Fake view percentage, proportion of fake views to total views
      - `is_suspicious`: Whether suspicious, comprehensive judgment if attention is needed
      - `main_detection_reason`: Main detection reason, most significant anomaly feature
      - `component_scores`: Dimensional anomaly scores, each 0-100, lower is better:
        - `engagement_score`: Engagement anomaly score
        - `distribution_score`: Distribution anomaly score
        - `consistency_score`: Consistency anomaly score
        - `creator_credibility_score`: Creator credibility anomaly score
        - `content_authenticity_score`: Content authenticity anomaly score
        - `follower_correlation_score`: Follower correlation anomaly score
        - `racing_mechanism_score`: Racing mechanism anomaly score
        - `fan_growth_score`: Fan growth anomaly score

    - `traffic_pool`: Traffic pool analysis (TikTok racing mechanism)
      - `current_tier`: Current traffic pool level (1-8), higher means more traffic
      - `current_tier_name`: Current traffic pool name
      - `expected_tier`: Expected traffic pool level, based on organic traffic prediction
      - `expected_tier_name`: Expected traffic pool name
      - `current_views_range`: Current traffic pool expected view range
      - `expected_views_range`: Expected traffic pool view range
      - `estimated_organic_views`: Estimated organic views, real views after deducting fake ones

    - `suspicious_features`: List of suspicious features, specific detected anomalies

    - `recommendations`: Recommended actions
      - `action`: Recommended action type, possible values include:
        - `no_action`: No action needed, healthy content
        - `monitor`: Continuous monitoring, minor anomalies present
        - `scheduled_review`: Schedule review, anomalies worth attention
        - `immediate_review`: Immediate review, serious anomalies present
      - `risk_level`: Risk level (\"low\", \"medium\", \"high\", \"critical\")
      - `potential_revenue_impact`: Potential revenue impact
      - `suggested_steps`: Suggested steps, specific action recommendations

    - `mcn_report`: (Optional) MCN business impact analysis report, applicable for business accounts
      - `summary`: Summary information
      - `business_impact`: Business impact assessment
        - `revenue_impact`: Revenue impact assessment
        - `brand_safety_impact`: Brand safety impact
        - `platform_relationship`: Platform relationship impact
        - `contract_impact`: Contract impact assessment
      - `recommended_actions`: Recommended action list
      - `historical_context`: Historical background data

    ### Features and Advantages:
    - Precise evaluation system built on TikTok's native Traffic Pool theory
    - Comprehensive analysis across 8 dimensions and 20+ metrics, covering traffic, engagement, creator,
    content, etc.
    - Adaptive algorithm automatically adjusts thresholds based on account size, verification status,
    content type
    - Anomaly detection based on big data statistical models, accurately identifies unnatural traffic
    patterns
    - Provides customized evaluation standards for different account sizes (micro, small, medium, large,
    extra-large)
    - Delivers detailed business impact analysis and specific, actionable recommendations

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/detect_fake_views\",
      \"params\": {
        \"item_id\": \"7460937381265411370\",
        \"content_category\": \"verified_large\"
      },
      \"data\": {
        \"video_metrics\": {
          \"total_views\": 159414915,
          \"total_likes\": 15817234,
          \"total_comments\": 392493,
          \"total_favorites\": 1051470,
          \"total_shares\": 1312741,
          \"engagement_rates\": {
            \"like_ratio\": 0.09922,
            \"comment_ratio\": 0.00246,
            \"favorite_ratio\": 0.0066,
            \"share_ratio\": 0.00823
          }
        },
        \"creator_metrics\": {
          \"account_age_days\": 3733.94,
          \"follower_count\": 89827771,
          \"verified\": true,
          \"trust_score\": 100
        },
        \"content_metrics\": {
          \"content_type\": \"video\",
          \"created_by_ai\": false,
          \"high_quality_upload\": true
        },
        \"fake_view_analysis\": {
          \"fake_score\": 7.16,
          \"confidence_level\": \"Minimal\",
          \"estimated_fake_views\": 7970745,
          \"fake_view_percentage\": 5.0,
          \"is_suspicious\": false,
          \"main_detection_reason\": \"Statistical View Anomalies\",
          \"component_scores\": {
            \"engagement_score\": 0.0,
            \"distribution_score\": 10.0,
            \"consistency_score\": 0,
            \"creator_credibility_score\": 0,
            \"content_authenticity_score\": 34.0,
            \"follower_correlation_score\": 35.0,
            \"racing_mechanism_score\": 0,
            \"fan_growth_score\": 45
          }
        },
        \"traffic_pool\": {
          \"current_tier\": 8,
          \"current_tier_name\": \"8th-Level Traffic Pool\",
          \"expected_tier\": 8,
          \"expected_tier_name\": \"8th-Level Traffic Pool\",
          \"current_views_range\": \"30M+\",
          \"expected_views_range\": \"30M+\",
          \"estimated_organic_views\": 148000807
        },
        \"suspicious_features\": [
          \"Suspicious: Reached 100000 followers from 10000 in only 31 days\",
          \"Suspicious: Account gaining 24063 followers per day on average\"
        ],
        \"recommendations\": {
          \"action\": \"no_action\",
          \"risk_level\": \"low\",
          \"potential_revenue_impact\": \"minimal\",
          \"suggested_steps\": [
            \"No immediate action required\",
            \"Include in routine monitoring\"
          ]
        },
        \"mcn_report\": {
          \"summary\": {
            \"estimated_revenue_impact\": 7970.745,
            \"recommended_actions\": \"No immediate action required\"
          },
          \"business_impact\": {
            \"revenue_impact\": {
              \"level\": \"low\",
              \"estimated_amount\": 7970.745
            },
            \"brand_safety_impact\": {
              \"level\": \"minimal\"
            },
            \"platform_relationship\": {
              \"status\": \"good\"
            }
          }
        }
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id
        content_category (Union[Unset, str]): 内容分类/Content category, options: default,
            entertainment, education, product, verified_large Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        item_id=item_id,
        content_category=content_category,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    item_id: str,
    content_category: Union[Unset, str] = "default",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""检测视频虚假流量分析/Detect fake views in video

     # [中文]
    ### 用途:
    - 通过高级算法分析TikTok视频流量数据，精确检测可能存在的虚假观看量和不自然互动
    - 基于TikTok赛马机制(Traffic Pool)流量池理论，评估内容真实性和流量质量
    - 提供全面的欺诈风险分析，包含8种维度、20+指标的深度评估
    - 为创作者、MCN机构和内容管理者提供专业的流量质量报告和优化建议

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频URL中提取(例如: https://www.tiktok.com/@tiktok/video/7460937381265411370
    中的7460937381265411370)
    - content_category: 内容分类，可选参数，影响互动率基准值，选项包括:
      - default: 默认类别，通用内容
      - entertainment: 娱乐内容，预期有较高互动率
      - education: 教育内容，预期有适中互动和较高收藏率
      - product: 产品内容，预期有较低互动但较高转化
      - verified_large: 大型认证账号，预期互动率适当降低

    ### 返回内容详解:
    - `video_metrics`: 视频核心指标
      - `total_views`: 总观看量，视频被观看的总次数
      - `total_likes`: 总点赞数，用户点赞互动次数
      - `total_comments`: 总评论数，用户评论互动次数
      - `total_favorites`: 总收藏数，用户收藏次数
      - `total_shares`: 总分享数，用户分享次数
      - `engagement_rates`: 互动率指标，值越高越好
        - `like_ratio`: 点赞率，正常值 1-10%，大账号可能较低
        - `comment_ratio`: 评论率，正常值 0.1-0.5%，高于1%极佳
        - `favorite_ratio`: 收藏率，正常值 0.05-0.8%
        - `share_ratio`: 分享率，正常值 0.05-0.5%，高于1%极佳

    - `creator_metrics`: 创作者账号健康指标
      - `account_age_days`: 账号存在天数，越长越可信
      - `follower_count`: 粉丝数量，影响预期观看量
      - `verified`: 是否验证账号，认证账号可信度更高
      - `trust_score`: 账号信任度评分(0-100)，越高越可信

    - `content_metrics`: 内容质量指标
      - `content_type`: 内容类型(video, image等)
      - `created_by_ai`: 是否AI生成，AI生成内容可能有特定流量模式
      - `high_quality_upload`: 是否高质量上传，高质量上传更可信

    - `fake_view_analysis`: 虚假流量综合分析
      - `fake_score`: 虚假流量评分(0-100)，评分越低越好:
        - 0-20: 极低风险，自然流量模式
        - 20-40: 低风险，可能有少量异常但不构成问题
        - 40-60: 中等风险，存在值得关注的异常
        - 60-80: 高风险，明显的虚假流量特征
        - 80-100: 极高风险，几乎确定存在虚假流量
      - `confidence_level`: 风险等级，分为\"Minimal\", \"Low\", \"Medium\", \"High\"
      - `estimated_fake_views`: 估计虚假观看量，基于虚假流量模型推算
      - `fake_view_percentage`: 虚假观看百分比，虚假占总量的比例
      - `is_suspicious`: 是否可疑，综合判断是否需要关注
      - `main_detection_reason`: 主要检测原因，最显著的异常特征
      - `component_scores`: 各维度异常评分，各项都是0-100，越低越好:
        - `engagement_score`: 互动异常评分
        - `distribution_score`: 分布异常评分
        - `consistency_score`: 一致性异常评分
        - `creator_credibility_score`: 创作者可信度异常评分
        - `content_authenticity_score`: 内容真实性异常评分
        - `follower_correlation_score`: 粉丝相关性异常评分
        - `racing_mechanism_score`: 赛马机制异常评分
        - `fan_growth_score`: 粉丝增长异常评分

    - `traffic_pool`: 流量池分析(TikTok赛马机制)
      - `current_tier`: 当前流量池级别(1-8)，越高代表流量越大
      - `current_tier_name`: 当前流量池名称
      - `expected_tier`: 预期流量池级别，基于有机流量预测
      - `expected_tier_name`: 预期流量池名称
      - `current_views_range`: 当前流量池预期观看范围
      - `expected_views_range`: 预期流量池观看范围
      - `estimated_organic_views`: 估计有机观看量，扣除虚假后的真实观看

    - `suspicious_features`: 可疑特征列表，检测到的具体异常现象

    - `recommendations`: 建议操作
      - `action`: 建议操作类型，可能值包括:
        - `no_action`: 无需操作，健康内容
        - `monitor`: 持续监控，存在轻微异常
        - `scheduled_review`: 安排审核，存在值得关注的异常
        - `immediate_review`: 立即审核，存在严重异常
      - `risk_level`: 风险等级(\"low\", \"medium\", \"high\", \"critical\")
      - `potential_revenue_impact`: 潜在收益影响
      - `suggested_steps`: 建议步骤，具体操作建议

    - `mcn_report`: (可选)MCN商业影响分析报告，适用于商业账号
      - `summary`: 摘要信息
      - `business_impact`: 商业影响评估
        - `revenue_impact`: 收益影响评估
        - `brand_safety_impact`: 品牌安全影响
        - `platform_relationship`: 平台关系影响
        - `contract_impact`: 合约影响评估
      - `recommended_actions`: 建议操作清单
      - `historical_context`: 历史背景数据

    ### 特性与优势:
    - 基于TikTok原生流量池(Traffic Pool)理论构建的精确评估系统
    - 8个维度、20+指标的全面分析，覆盖流量、互动、创作者、内容等全方位评估
    - 自适应算法，根据账号规模、认证状态、内容类型自动调整阈值
    - 基于大数据统计模型的异常检测，准确识别不自然流量模式
    - 为不同规模账号(微型、小型、中型、大型、超大型)提供定制化评估标准
    - 提供详细的商业影响分析和具体可行的建议步骤

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/detect_fake_views\",
      \"params\": {
        \"item_id\": \"7460937381265411370\",
        \"content_category\": \"verified_large\"
      },
      \"data\": {
        \"video_metrics\": {
          \"total_views\": 159414915,
          \"total_likes\": 15817234,
          \"total_comments\": 392493,
          \"total_favorites\": 1051470,
          \"total_shares\": 1312741,
          \"engagement_rates\": {
            \"like_ratio\": 0.09922,
            \"comment_ratio\": 0.00246,
            \"favorite_ratio\": 0.0066,
            \"share_ratio\": 0.00823
          }
        },
        \"creator_metrics\": {
          \"account_age_days\": 3733.94,
          \"follower_count\": 89827771,
          \"verified\": true,
          \"trust_score\": 100
        },
        \"content_metrics\": {
          \"content_type\": \"video\",
          \"created_by_ai\": false,
          \"high_quality_upload\": true
        },
        \"fake_view_analysis\": {
          \"fake_score\": 7.16,
          \"confidence_level\": \"Minimal\",
          \"estimated_fake_views\": 7970745,
          \"fake_view_percentage\": 5.0,
          \"is_suspicious\": false,
          \"main_detection_reason\": \"Statistical View Anomalies\",
          \"component_scores\": {
            \"engagement_score\": 0.0,
            \"distribution_score\": 10.0,
            \"consistency_score\": 0,
            \"creator_credibility_score\": 0,
            \"content_authenticity_score\": 34.0,
            \"follower_correlation_score\": 35.0,
            \"racing_mechanism_score\": 0,
            \"fan_growth_score\": 45
          }
        },
        \"traffic_pool\": {
          \"current_tier\": 8,
          \"current_tier_name\": \"8th-Level Traffic Pool\",
          \"expected_tier\": 8,
          \"expected_tier_name\": \"8th-Level Traffic Pool\",
          \"current_views_range\": \"30M+\",
          \"expected_views_range\": \"30M+\",
          \"estimated_organic_views\": 148000807
        },
        \"suspicious_features\": [
          \"Suspicious: Reached 100000 followers from 10000 in only 31 days\",
          \"Suspicious: Account gaining 24063 followers per day on average\"
        ],
        \"recommendations\": {
          \"action\": \"no_action\",
          \"risk_level\": \"low\",
          \"potential_revenue_impact\": \"minimal\",
          \"suggested_steps\": [
            \"No immediate action required\",
            \"Include in routine monitoring\"
          ]
        },
        \"mcn_report\": {
          \"summary\": {
            \"estimated_revenue_impact\": 7970.745,
            \"recommended_actions\": \"No immediate action required\"
          },
          \"business_impact\": {
            \"revenue_impact\": {
              \"level\": \"low\",
              \"estimated_amount\": 7970.745
            },
            \"brand_safety_impact\": {
              \"level\": \"minimal\"
            },
            \"platform_relationship\": {
              \"status\": \"good\"
            }
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Analyze TikTok video traffic data using advanced algorithms to precisely detect potential fake
    views and unnatural engagement
    - Evaluate content authenticity and traffic quality based on TikTok's Traffic Pool theory
    - Provide comprehensive fraud risk analysis with in-depth assessment across 8 dimensions and 20+
    metrics
    - Deliver professional traffic quality reports and optimization recommendations for creators, MCN
    agencies, and content managers

    ### Parameters:
    - item_id: Video ID, required parameter, can be extracted from video URL (e.g., 7460937381265411370
    from https://www.tiktok.com/@tiktok/video/7460937381265411370)
    - content_category: Content category, optional parameter, affects engagement rate benchmarks,
    options include:
      - default: Default category for general content
      - entertainment: Entertainment content, expected to have higher engagement
      - education: Educational content, expected to have moderate engagement and higher save rates
      - product: Product content, expected to have lower engagement but higher conversion
      - verified_large: Large verified accounts, expected to have appropriately lower engagement rates

    ### Return Description:
    - `video_metrics`: Core video metrics
      - `total_views`: Total number of views
      - `total_likes`: Total number of likes
      - `total_comments`: Total number of comments
      - `total_favorites`: Total number of saves
      - `total_shares`: Total number of shares
      - `engagement_rates`: Engagement rate metrics, higher is better
        - `like_ratio`: Like rate, normal range 1-10%, may be lower for large accounts
        - `comment_ratio`: Comment rate, normal range 0.1-0.5%, excellent if above 1%
        - `favorite_ratio`: Save rate, normal range 0.05-0.8%
        - `share_ratio`: Share rate, normal range 0.05-0.5%, excellent if above 1%

    - `creator_metrics`: Creator account health indicators
      - `account_age_days`: Account age in days, longer is more credible
      - `follower_count`: Number of followers, affects expected view count
      - `verified`: Whether account is verified, verified accounts have higher credibility
      - `trust_score`: Account trust score (0-100), higher is more trustworthy

    - `content_metrics`: Content quality indicators
      - `content_type`: Content type (video, image, etc.)
      - `created_by_ai`: Whether AI-generated, AI-generated content may have specific traffic patterns
      - `high_quality_upload`: Whether high-quality upload, high-quality uploads are more credible

    - `fake_view_analysis`: Comprehensive fake traffic analysis
      - `fake_score`: Fake view score (0-100), lower is better:
        - 0-20: Very low risk, natural traffic patterns
        - 20-40: Low risk, may have minor anomalies but not problematic
        - 40-60: Medium risk, anomalies worth attention
        - 60-80: High risk, obvious fake traffic characteristics
        - 80-100: Very high risk, almost certainly fake traffic
      - `confidence_level`: Risk level, categorized as \"Minimal\", \"Low\", \"Medium\", \"High\"
      - `estimated_fake_views`: Estimated fake views, calculated based on fake traffic model
      - `fake_view_percentage`: Fake view percentage, proportion of fake views to total views
      - `is_suspicious`: Whether suspicious, comprehensive judgment if attention is needed
      - `main_detection_reason`: Main detection reason, most significant anomaly feature
      - `component_scores`: Dimensional anomaly scores, each 0-100, lower is better:
        - `engagement_score`: Engagement anomaly score
        - `distribution_score`: Distribution anomaly score
        - `consistency_score`: Consistency anomaly score
        - `creator_credibility_score`: Creator credibility anomaly score
        - `content_authenticity_score`: Content authenticity anomaly score
        - `follower_correlation_score`: Follower correlation anomaly score
        - `racing_mechanism_score`: Racing mechanism anomaly score
        - `fan_growth_score`: Fan growth anomaly score

    - `traffic_pool`: Traffic pool analysis (TikTok racing mechanism)
      - `current_tier`: Current traffic pool level (1-8), higher means more traffic
      - `current_tier_name`: Current traffic pool name
      - `expected_tier`: Expected traffic pool level, based on organic traffic prediction
      - `expected_tier_name`: Expected traffic pool name
      - `current_views_range`: Current traffic pool expected view range
      - `expected_views_range`: Expected traffic pool view range
      - `estimated_organic_views`: Estimated organic views, real views after deducting fake ones

    - `suspicious_features`: List of suspicious features, specific detected anomalies

    - `recommendations`: Recommended actions
      - `action`: Recommended action type, possible values include:
        - `no_action`: No action needed, healthy content
        - `monitor`: Continuous monitoring, minor anomalies present
        - `scheduled_review`: Schedule review, anomalies worth attention
        - `immediate_review`: Immediate review, serious anomalies present
      - `risk_level`: Risk level (\"low\", \"medium\", \"high\", \"critical\")
      - `potential_revenue_impact`: Potential revenue impact
      - `suggested_steps`: Suggested steps, specific action recommendations

    - `mcn_report`: (Optional) MCN business impact analysis report, applicable for business accounts
      - `summary`: Summary information
      - `business_impact`: Business impact assessment
        - `revenue_impact`: Revenue impact assessment
        - `brand_safety_impact`: Brand safety impact
        - `platform_relationship`: Platform relationship impact
        - `contract_impact`: Contract impact assessment
      - `recommended_actions`: Recommended action list
      - `historical_context`: Historical background data

    ### Features and Advantages:
    - Precise evaluation system built on TikTok's native Traffic Pool theory
    - Comprehensive analysis across 8 dimensions and 20+ metrics, covering traffic, engagement, creator,
    content, etc.
    - Adaptive algorithm automatically adjusts thresholds based on account size, verification status,
    content type
    - Anomaly detection based on big data statistical models, accurately identifies unnatural traffic
    patterns
    - Provides customized evaluation standards for different account sizes (micro, small, medium, large,
    extra-large)
    - Delivers detailed business impact analysis and specific, actionable recommendations

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/detect_fake_views\",
      \"params\": {
        \"item_id\": \"7460937381265411370\",
        \"content_category\": \"verified_large\"
      },
      \"data\": {
        \"video_metrics\": {
          \"total_views\": 159414915,
          \"total_likes\": 15817234,
          \"total_comments\": 392493,
          \"total_favorites\": 1051470,
          \"total_shares\": 1312741,
          \"engagement_rates\": {
            \"like_ratio\": 0.09922,
            \"comment_ratio\": 0.00246,
            \"favorite_ratio\": 0.0066,
            \"share_ratio\": 0.00823
          }
        },
        \"creator_metrics\": {
          \"account_age_days\": 3733.94,
          \"follower_count\": 89827771,
          \"verified\": true,
          \"trust_score\": 100
        },
        \"content_metrics\": {
          \"content_type\": \"video\",
          \"created_by_ai\": false,
          \"high_quality_upload\": true
        },
        \"fake_view_analysis\": {
          \"fake_score\": 7.16,
          \"confidence_level\": \"Minimal\",
          \"estimated_fake_views\": 7970745,
          \"fake_view_percentage\": 5.0,
          \"is_suspicious\": false,
          \"main_detection_reason\": \"Statistical View Anomalies\",
          \"component_scores\": {
            \"engagement_score\": 0.0,
            \"distribution_score\": 10.0,
            \"consistency_score\": 0,
            \"creator_credibility_score\": 0,
            \"content_authenticity_score\": 34.0,
            \"follower_correlation_score\": 35.0,
            \"racing_mechanism_score\": 0,
            \"fan_growth_score\": 45
          }
        },
        \"traffic_pool\": {
          \"current_tier\": 8,
          \"current_tier_name\": \"8th-Level Traffic Pool\",
          \"expected_tier\": 8,
          \"expected_tier_name\": \"8th-Level Traffic Pool\",
          \"current_views_range\": \"30M+\",
          \"expected_views_range\": \"30M+\",
          \"estimated_organic_views\": 148000807
        },
        \"suspicious_features\": [
          \"Suspicious: Reached 100000 followers from 10000 in only 31 days\",
          \"Suspicious: Account gaining 24063 followers per day on average\"
        ],
        \"recommendations\": {
          \"action\": \"no_action\",
          \"risk_level\": \"low\",
          \"potential_revenue_impact\": \"minimal\",
          \"suggested_steps\": [
            \"No immediate action required\",
            \"Include in routine monitoring\"
          ]
        },
        \"mcn_report\": {
          \"summary\": {
            \"estimated_revenue_impact\": 7970.745,
            \"recommended_actions\": \"No immediate action required\"
          },
          \"business_impact\": {
            \"revenue_impact\": {
              \"level\": \"low\",
              \"estimated_amount\": 7970.745
            },
            \"brand_safety_impact\": {
              \"level\": \"minimal\"
            },
            \"platform_relationship\": {
              \"status\": \"good\"
            }
          }
        }
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id
        content_category (Union[Unset, str]): 内容分类/Content category, options: default,
            entertainment, education, product, verified_large Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        content_category=content_category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    item_id: str,
    content_category: Union[Unset, str] = "default",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""检测视频虚假流量分析/Detect fake views in video

     # [中文]
    ### 用途:
    - 通过高级算法分析TikTok视频流量数据，精确检测可能存在的虚假观看量和不自然互动
    - 基于TikTok赛马机制(Traffic Pool)流量池理论，评估内容真实性和流量质量
    - 提供全面的欺诈风险分析，包含8种维度、20+指标的深度评估
    - 为创作者、MCN机构和内容管理者提供专业的流量质量报告和优化建议

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频URL中提取(例如: https://www.tiktok.com/@tiktok/video/7460937381265411370
    中的7460937381265411370)
    - content_category: 内容分类，可选参数，影响互动率基准值，选项包括:
      - default: 默认类别，通用内容
      - entertainment: 娱乐内容，预期有较高互动率
      - education: 教育内容，预期有适中互动和较高收藏率
      - product: 产品内容，预期有较低互动但较高转化
      - verified_large: 大型认证账号，预期互动率适当降低

    ### 返回内容详解:
    - `video_metrics`: 视频核心指标
      - `total_views`: 总观看量，视频被观看的总次数
      - `total_likes`: 总点赞数，用户点赞互动次数
      - `total_comments`: 总评论数，用户评论互动次数
      - `total_favorites`: 总收藏数，用户收藏次数
      - `total_shares`: 总分享数，用户分享次数
      - `engagement_rates`: 互动率指标，值越高越好
        - `like_ratio`: 点赞率，正常值 1-10%，大账号可能较低
        - `comment_ratio`: 评论率，正常值 0.1-0.5%，高于1%极佳
        - `favorite_ratio`: 收藏率，正常值 0.05-0.8%
        - `share_ratio`: 分享率，正常值 0.05-0.5%，高于1%极佳

    - `creator_metrics`: 创作者账号健康指标
      - `account_age_days`: 账号存在天数，越长越可信
      - `follower_count`: 粉丝数量，影响预期观看量
      - `verified`: 是否验证账号，认证账号可信度更高
      - `trust_score`: 账号信任度评分(0-100)，越高越可信

    - `content_metrics`: 内容质量指标
      - `content_type`: 内容类型(video, image等)
      - `created_by_ai`: 是否AI生成，AI生成内容可能有特定流量模式
      - `high_quality_upload`: 是否高质量上传，高质量上传更可信

    - `fake_view_analysis`: 虚假流量综合分析
      - `fake_score`: 虚假流量评分(0-100)，评分越低越好:
        - 0-20: 极低风险，自然流量模式
        - 20-40: 低风险，可能有少量异常但不构成问题
        - 40-60: 中等风险，存在值得关注的异常
        - 60-80: 高风险，明显的虚假流量特征
        - 80-100: 极高风险，几乎确定存在虚假流量
      - `confidence_level`: 风险等级，分为\"Minimal\", \"Low\", \"Medium\", \"High\"
      - `estimated_fake_views`: 估计虚假观看量，基于虚假流量模型推算
      - `fake_view_percentage`: 虚假观看百分比，虚假占总量的比例
      - `is_suspicious`: 是否可疑，综合判断是否需要关注
      - `main_detection_reason`: 主要检测原因，最显著的异常特征
      - `component_scores`: 各维度异常评分，各项都是0-100，越低越好:
        - `engagement_score`: 互动异常评分
        - `distribution_score`: 分布异常评分
        - `consistency_score`: 一致性异常评分
        - `creator_credibility_score`: 创作者可信度异常评分
        - `content_authenticity_score`: 内容真实性异常评分
        - `follower_correlation_score`: 粉丝相关性异常评分
        - `racing_mechanism_score`: 赛马机制异常评分
        - `fan_growth_score`: 粉丝增长异常评分

    - `traffic_pool`: 流量池分析(TikTok赛马机制)
      - `current_tier`: 当前流量池级别(1-8)，越高代表流量越大
      - `current_tier_name`: 当前流量池名称
      - `expected_tier`: 预期流量池级别，基于有机流量预测
      - `expected_tier_name`: 预期流量池名称
      - `current_views_range`: 当前流量池预期观看范围
      - `expected_views_range`: 预期流量池观看范围
      - `estimated_organic_views`: 估计有机观看量，扣除虚假后的真实观看

    - `suspicious_features`: 可疑特征列表，检测到的具体异常现象

    - `recommendations`: 建议操作
      - `action`: 建议操作类型，可能值包括:
        - `no_action`: 无需操作，健康内容
        - `monitor`: 持续监控，存在轻微异常
        - `scheduled_review`: 安排审核，存在值得关注的异常
        - `immediate_review`: 立即审核，存在严重异常
      - `risk_level`: 风险等级(\"low\", \"medium\", \"high\", \"critical\")
      - `potential_revenue_impact`: 潜在收益影响
      - `suggested_steps`: 建议步骤，具体操作建议

    - `mcn_report`: (可选)MCN商业影响分析报告，适用于商业账号
      - `summary`: 摘要信息
      - `business_impact`: 商业影响评估
        - `revenue_impact`: 收益影响评估
        - `brand_safety_impact`: 品牌安全影响
        - `platform_relationship`: 平台关系影响
        - `contract_impact`: 合约影响评估
      - `recommended_actions`: 建议操作清单
      - `historical_context`: 历史背景数据

    ### 特性与优势:
    - 基于TikTok原生流量池(Traffic Pool)理论构建的精确评估系统
    - 8个维度、20+指标的全面分析，覆盖流量、互动、创作者、内容等全方位评估
    - 自适应算法，根据账号规模、认证状态、内容类型自动调整阈值
    - 基于大数据统计模型的异常检测，准确识别不自然流量模式
    - 为不同规模账号(微型、小型、中型、大型、超大型)提供定制化评估标准
    - 提供详细的商业影响分析和具体可行的建议步骤

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/detect_fake_views\",
      \"params\": {
        \"item_id\": \"7460937381265411370\",
        \"content_category\": \"verified_large\"
      },
      \"data\": {
        \"video_metrics\": {
          \"total_views\": 159414915,
          \"total_likes\": 15817234,
          \"total_comments\": 392493,
          \"total_favorites\": 1051470,
          \"total_shares\": 1312741,
          \"engagement_rates\": {
            \"like_ratio\": 0.09922,
            \"comment_ratio\": 0.00246,
            \"favorite_ratio\": 0.0066,
            \"share_ratio\": 0.00823
          }
        },
        \"creator_metrics\": {
          \"account_age_days\": 3733.94,
          \"follower_count\": 89827771,
          \"verified\": true,
          \"trust_score\": 100
        },
        \"content_metrics\": {
          \"content_type\": \"video\",
          \"created_by_ai\": false,
          \"high_quality_upload\": true
        },
        \"fake_view_analysis\": {
          \"fake_score\": 7.16,
          \"confidence_level\": \"Minimal\",
          \"estimated_fake_views\": 7970745,
          \"fake_view_percentage\": 5.0,
          \"is_suspicious\": false,
          \"main_detection_reason\": \"Statistical View Anomalies\",
          \"component_scores\": {
            \"engagement_score\": 0.0,
            \"distribution_score\": 10.0,
            \"consistency_score\": 0,
            \"creator_credibility_score\": 0,
            \"content_authenticity_score\": 34.0,
            \"follower_correlation_score\": 35.0,
            \"racing_mechanism_score\": 0,
            \"fan_growth_score\": 45
          }
        },
        \"traffic_pool\": {
          \"current_tier\": 8,
          \"current_tier_name\": \"8th-Level Traffic Pool\",
          \"expected_tier\": 8,
          \"expected_tier_name\": \"8th-Level Traffic Pool\",
          \"current_views_range\": \"30M+\",
          \"expected_views_range\": \"30M+\",
          \"estimated_organic_views\": 148000807
        },
        \"suspicious_features\": [
          \"Suspicious: Reached 100000 followers from 10000 in only 31 days\",
          \"Suspicious: Account gaining 24063 followers per day on average\"
        ],
        \"recommendations\": {
          \"action\": \"no_action\",
          \"risk_level\": \"low\",
          \"potential_revenue_impact\": \"minimal\",
          \"suggested_steps\": [
            \"No immediate action required\",
            \"Include in routine monitoring\"
          ]
        },
        \"mcn_report\": {
          \"summary\": {
            \"estimated_revenue_impact\": 7970.745,
            \"recommended_actions\": \"No immediate action required\"
          },
          \"business_impact\": {
            \"revenue_impact\": {
              \"level\": \"low\",
              \"estimated_amount\": 7970.745
            },
            \"brand_safety_impact\": {
              \"level\": \"minimal\"
            },
            \"platform_relationship\": {
              \"status\": \"good\"
            }
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Analyze TikTok video traffic data using advanced algorithms to precisely detect potential fake
    views and unnatural engagement
    - Evaluate content authenticity and traffic quality based on TikTok's Traffic Pool theory
    - Provide comprehensive fraud risk analysis with in-depth assessment across 8 dimensions and 20+
    metrics
    - Deliver professional traffic quality reports and optimization recommendations for creators, MCN
    agencies, and content managers

    ### Parameters:
    - item_id: Video ID, required parameter, can be extracted from video URL (e.g., 7460937381265411370
    from https://www.tiktok.com/@tiktok/video/7460937381265411370)
    - content_category: Content category, optional parameter, affects engagement rate benchmarks,
    options include:
      - default: Default category for general content
      - entertainment: Entertainment content, expected to have higher engagement
      - education: Educational content, expected to have moderate engagement and higher save rates
      - product: Product content, expected to have lower engagement but higher conversion
      - verified_large: Large verified accounts, expected to have appropriately lower engagement rates

    ### Return Description:
    - `video_metrics`: Core video metrics
      - `total_views`: Total number of views
      - `total_likes`: Total number of likes
      - `total_comments`: Total number of comments
      - `total_favorites`: Total number of saves
      - `total_shares`: Total number of shares
      - `engagement_rates`: Engagement rate metrics, higher is better
        - `like_ratio`: Like rate, normal range 1-10%, may be lower for large accounts
        - `comment_ratio`: Comment rate, normal range 0.1-0.5%, excellent if above 1%
        - `favorite_ratio`: Save rate, normal range 0.05-0.8%
        - `share_ratio`: Share rate, normal range 0.05-0.5%, excellent if above 1%

    - `creator_metrics`: Creator account health indicators
      - `account_age_days`: Account age in days, longer is more credible
      - `follower_count`: Number of followers, affects expected view count
      - `verified`: Whether account is verified, verified accounts have higher credibility
      - `trust_score`: Account trust score (0-100), higher is more trustworthy

    - `content_metrics`: Content quality indicators
      - `content_type`: Content type (video, image, etc.)
      - `created_by_ai`: Whether AI-generated, AI-generated content may have specific traffic patterns
      - `high_quality_upload`: Whether high-quality upload, high-quality uploads are more credible

    - `fake_view_analysis`: Comprehensive fake traffic analysis
      - `fake_score`: Fake view score (0-100), lower is better:
        - 0-20: Very low risk, natural traffic patterns
        - 20-40: Low risk, may have minor anomalies but not problematic
        - 40-60: Medium risk, anomalies worth attention
        - 60-80: High risk, obvious fake traffic characteristics
        - 80-100: Very high risk, almost certainly fake traffic
      - `confidence_level`: Risk level, categorized as \"Minimal\", \"Low\", \"Medium\", \"High\"
      - `estimated_fake_views`: Estimated fake views, calculated based on fake traffic model
      - `fake_view_percentage`: Fake view percentage, proportion of fake views to total views
      - `is_suspicious`: Whether suspicious, comprehensive judgment if attention is needed
      - `main_detection_reason`: Main detection reason, most significant anomaly feature
      - `component_scores`: Dimensional anomaly scores, each 0-100, lower is better:
        - `engagement_score`: Engagement anomaly score
        - `distribution_score`: Distribution anomaly score
        - `consistency_score`: Consistency anomaly score
        - `creator_credibility_score`: Creator credibility anomaly score
        - `content_authenticity_score`: Content authenticity anomaly score
        - `follower_correlation_score`: Follower correlation anomaly score
        - `racing_mechanism_score`: Racing mechanism anomaly score
        - `fan_growth_score`: Fan growth anomaly score

    - `traffic_pool`: Traffic pool analysis (TikTok racing mechanism)
      - `current_tier`: Current traffic pool level (1-8), higher means more traffic
      - `current_tier_name`: Current traffic pool name
      - `expected_tier`: Expected traffic pool level, based on organic traffic prediction
      - `expected_tier_name`: Expected traffic pool name
      - `current_views_range`: Current traffic pool expected view range
      - `expected_views_range`: Expected traffic pool view range
      - `estimated_organic_views`: Estimated organic views, real views after deducting fake ones

    - `suspicious_features`: List of suspicious features, specific detected anomalies

    - `recommendations`: Recommended actions
      - `action`: Recommended action type, possible values include:
        - `no_action`: No action needed, healthy content
        - `monitor`: Continuous monitoring, minor anomalies present
        - `scheduled_review`: Schedule review, anomalies worth attention
        - `immediate_review`: Immediate review, serious anomalies present
      - `risk_level`: Risk level (\"low\", \"medium\", \"high\", \"critical\")
      - `potential_revenue_impact`: Potential revenue impact
      - `suggested_steps`: Suggested steps, specific action recommendations

    - `mcn_report`: (Optional) MCN business impact analysis report, applicable for business accounts
      - `summary`: Summary information
      - `business_impact`: Business impact assessment
        - `revenue_impact`: Revenue impact assessment
        - `brand_safety_impact`: Brand safety impact
        - `platform_relationship`: Platform relationship impact
        - `contract_impact`: Contract impact assessment
      - `recommended_actions`: Recommended action list
      - `historical_context`: Historical background data

    ### Features and Advantages:
    - Precise evaluation system built on TikTok's native Traffic Pool theory
    - Comprehensive analysis across 8 dimensions and 20+ metrics, covering traffic, engagement, creator,
    content, etc.
    - Adaptive algorithm automatically adjusts thresholds based on account size, verification status,
    content type
    - Anomaly detection based on big data statistical models, accurately identifies unnatural traffic
    patterns
    - Provides customized evaluation standards for different account sizes (micro, small, medium, large,
    extra-large)
    - Delivers detailed business impact analysis and specific, actionable recommendations

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/detect_fake_views\",
      \"params\": {
        \"item_id\": \"7460937381265411370\",
        \"content_category\": \"verified_large\"
      },
      \"data\": {
        \"video_metrics\": {
          \"total_views\": 159414915,
          \"total_likes\": 15817234,
          \"total_comments\": 392493,
          \"total_favorites\": 1051470,
          \"total_shares\": 1312741,
          \"engagement_rates\": {
            \"like_ratio\": 0.09922,
            \"comment_ratio\": 0.00246,
            \"favorite_ratio\": 0.0066,
            \"share_ratio\": 0.00823
          }
        },
        \"creator_metrics\": {
          \"account_age_days\": 3733.94,
          \"follower_count\": 89827771,
          \"verified\": true,
          \"trust_score\": 100
        },
        \"content_metrics\": {
          \"content_type\": \"video\",
          \"created_by_ai\": false,
          \"high_quality_upload\": true
        },
        \"fake_view_analysis\": {
          \"fake_score\": 7.16,
          \"confidence_level\": \"Minimal\",
          \"estimated_fake_views\": 7970745,
          \"fake_view_percentage\": 5.0,
          \"is_suspicious\": false,
          \"main_detection_reason\": \"Statistical View Anomalies\",
          \"component_scores\": {
            \"engagement_score\": 0.0,
            \"distribution_score\": 10.0,
            \"consistency_score\": 0,
            \"creator_credibility_score\": 0,
            \"content_authenticity_score\": 34.0,
            \"follower_correlation_score\": 35.0,
            \"racing_mechanism_score\": 0,
            \"fan_growth_score\": 45
          }
        },
        \"traffic_pool\": {
          \"current_tier\": 8,
          \"current_tier_name\": \"8th-Level Traffic Pool\",
          \"expected_tier\": 8,
          \"expected_tier_name\": \"8th-Level Traffic Pool\",
          \"current_views_range\": \"30M+\",
          \"expected_views_range\": \"30M+\",
          \"estimated_organic_views\": 148000807
        },
        \"suspicious_features\": [
          \"Suspicious: Reached 100000 followers from 10000 in only 31 days\",
          \"Suspicious: Account gaining 24063 followers per day on average\"
        ],
        \"recommendations\": {
          \"action\": \"no_action\",
          \"risk_level\": \"low\",
          \"potential_revenue_impact\": \"minimal\",
          \"suggested_steps\": [
            \"No immediate action required\",
            \"Include in routine monitoring\"
          ]
        },
        \"mcn_report\": {
          \"summary\": {
            \"estimated_revenue_impact\": 7970.745,
            \"recommended_actions\": \"No immediate action required\"
          },
          \"business_impact\": {
            \"revenue_impact\": {
              \"level\": \"low\",
              \"estimated_amount\": 7970.745
            },
            \"brand_safety_impact\": {
              \"level\": \"minimal\"
            },
            \"platform_relationship\": {
              \"status\": \"good\"
            }
          }
        }
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id
        content_category (Union[Unset, str]): 内容分类/Content category, options: default,
            entertainment, education, product, verified_large Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            item_id=item_id,
            content_category=content_category,
        )
    ).parsed
