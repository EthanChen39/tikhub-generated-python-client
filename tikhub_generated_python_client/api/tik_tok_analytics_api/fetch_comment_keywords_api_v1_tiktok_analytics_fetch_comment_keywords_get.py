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
    item_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["item_id"] = item_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/analytics/fetch_comment_keywords",
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
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频评论关键词分析/Get comment keywords analysis

     # [中文]
    ### 用途:
    - 分析视频评论中出现的热门关键词和话题，挖掘用户反馈
    - 提取观众评论中的主要内容和观点，帮助理解受众关注点
    - 支持创作者优化内容策略，增强与观众的互动和连接

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频分享链接或TikTok Studio获取

    ### 返回内容说明:
    - `item_id`: 请求的视频ID
    - `key_words`: 评论中提取的关键词列表，包含以下字段:
      - `key_word`: 关键词文本
      - `comments`: 包含该关键词的评论列表，每条评论包含:
        - `cid`: 评论ID
        - `text`: 评论内容
        - `create_date`: 评论创建时间戳
        - `digg_count`: 评论获赞数量
        - `comment_type`: 评论类型
        - `comment_author`: 评论作者信息
          - `uid`: 用户ID
          - `nick_name`: 用户昵称
          - `cover`: 用户头像信息
            - `url_list`: 头像URL列表

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_comment_keywords\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"key_words\": [
          {
            \"key_word\": \"tik tok\",
            \"comments\": [
              {
                \"cid\": \"7502621950457463574\",
                \"comment_author\": {
                  \"nick_name\": \"ollie_russell05\",
                  \"uid\": \"7332627012203414560\"
                },
                \"create_date\": 1746840350,
                \"digg_count\": 17,
                \"text\": \"Imagine been tik tok and only getting 700 likes 🥀🙏😭\"
              }
            ]
          },
          {
            \"key_word\": \"go viral\",
            \"comments\": [
              {
                \"cid\": \"7502743477604680465\",
                \"comment_author\": {
                  \"nick_name\": \"★ 🇦🇫\",
                  \"uid\": \"7274239704915149829\"
                },
                \"create_date\": 1746868614,
                \"digg_count\": 13,
                \"text\": \"I want to go viral\"
              }
            ]
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Analyze popular keywords and topics in video comments to uncover user feedback
    - Extract main content and opinions from audience comments to understand viewer focus points
    - Support creators in optimizing content strategy and enhancing audience engagement and connection

    ### Parameters:
    - item_id: Video ID, required parameter, can be obtained from video sharing links or TikTok Studio

    ### Return Description:
    - `item_id`: The requested video ID
    - `key_words`: List of keywords extracted from comments, including:
      - `key_word`: Keyword text
      - `comments`: List of comments containing this keyword, each comment includes:
        - `cid`: Comment ID
        - `text`: Comment content
        - `create_date`: Comment creation timestamp
        - `digg_count`: Number of likes on the comment
        - `comment_type`: Comment type
        - `comment_author`: Comment author information
          - `uid`: User ID
          - `nick_name`: User nickname
          - `cover`: User avatar information
            - `url_list`: List of avatar URLs

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_comment_keywords\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"key_words\": [
          {
            \"key_word\": \"tik tok\",
            \"comments\": [
              {
                \"cid\": \"7502621950457463574\",
                \"comment_author\": {
                  \"nick_name\": \"ollie_russell05\",
                  \"uid\": \"7332627012203414560\"
                },
                \"create_date\": 1746840350,
                \"digg_count\": 17,
                \"text\": \"Imagine been tik tok and only getting 700 likes 🥀🙏😭\"
              }
            ]
          },
          {
            \"key_word\": \"go viral\",
            \"comments\": [
              {
                \"cid\": \"7502743477604680465\",
                \"comment_author\": {
                  \"nick_name\": \"★ 🇦🇫\",
                  \"uid\": \"7274239704915149829\"
                },
                \"create_date\": 1746868614,
                \"digg_count\": 13,
                \"text\": \"I want to go viral\"
              }
            ]
          }
        ]
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频评论关键词分析/Get comment keywords analysis

     # [中文]
    ### 用途:
    - 分析视频评论中出现的热门关键词和话题，挖掘用户反馈
    - 提取观众评论中的主要内容和观点，帮助理解受众关注点
    - 支持创作者优化内容策略，增强与观众的互动和连接

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频分享链接或TikTok Studio获取

    ### 返回内容说明:
    - `item_id`: 请求的视频ID
    - `key_words`: 评论中提取的关键词列表，包含以下字段:
      - `key_word`: 关键词文本
      - `comments`: 包含该关键词的评论列表，每条评论包含:
        - `cid`: 评论ID
        - `text`: 评论内容
        - `create_date`: 评论创建时间戳
        - `digg_count`: 评论获赞数量
        - `comment_type`: 评论类型
        - `comment_author`: 评论作者信息
          - `uid`: 用户ID
          - `nick_name`: 用户昵称
          - `cover`: 用户头像信息
            - `url_list`: 头像URL列表

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_comment_keywords\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"key_words\": [
          {
            \"key_word\": \"tik tok\",
            \"comments\": [
              {
                \"cid\": \"7502621950457463574\",
                \"comment_author\": {
                  \"nick_name\": \"ollie_russell05\",
                  \"uid\": \"7332627012203414560\"
                },
                \"create_date\": 1746840350,
                \"digg_count\": 17,
                \"text\": \"Imagine been tik tok and only getting 700 likes 🥀🙏😭\"
              }
            ]
          },
          {
            \"key_word\": \"go viral\",
            \"comments\": [
              {
                \"cid\": \"7502743477604680465\",
                \"comment_author\": {
                  \"nick_name\": \"★ 🇦🇫\",
                  \"uid\": \"7274239704915149829\"
                },
                \"create_date\": 1746868614,
                \"digg_count\": 13,
                \"text\": \"I want to go viral\"
              }
            ]
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Analyze popular keywords and topics in video comments to uncover user feedback
    - Extract main content and opinions from audience comments to understand viewer focus points
    - Support creators in optimizing content strategy and enhancing audience engagement and connection

    ### Parameters:
    - item_id: Video ID, required parameter, can be obtained from video sharing links or TikTok Studio

    ### Return Description:
    - `item_id`: The requested video ID
    - `key_words`: List of keywords extracted from comments, including:
      - `key_word`: Keyword text
      - `comments`: List of comments containing this keyword, each comment includes:
        - `cid`: Comment ID
        - `text`: Comment content
        - `create_date`: Comment creation timestamp
        - `digg_count`: Number of likes on the comment
        - `comment_type`: Comment type
        - `comment_author`: Comment author information
          - `uid`: User ID
          - `nick_name`: User nickname
          - `cover`: User avatar information
            - `url_list`: List of avatar URLs

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_comment_keywords\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"key_words\": [
          {
            \"key_word\": \"tik tok\",
            \"comments\": [
              {
                \"cid\": \"7502621950457463574\",
                \"comment_author\": {
                  \"nick_name\": \"ollie_russell05\",
                  \"uid\": \"7332627012203414560\"
                },
                \"create_date\": 1746840350,
                \"digg_count\": 17,
                \"text\": \"Imagine been tik tok and only getting 700 likes 🥀🙏😭\"
              }
            ]
          },
          {
            \"key_word\": \"go viral\",
            \"comments\": [
              {
                \"cid\": \"7502743477604680465\",
                \"comment_author\": {
                  \"nick_name\": \"★ 🇦🇫\",
                  \"uid\": \"7274239704915149829\"
                },
                \"create_date\": 1746868614,
                \"digg_count\": 13,
                \"text\": \"I want to go viral\"
              }
            ]
          }
        ]
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        item_id=item_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频评论关键词分析/Get comment keywords analysis

     # [中文]
    ### 用途:
    - 分析视频评论中出现的热门关键词和话题，挖掘用户反馈
    - 提取观众评论中的主要内容和观点，帮助理解受众关注点
    - 支持创作者优化内容策略，增强与观众的互动和连接

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频分享链接或TikTok Studio获取

    ### 返回内容说明:
    - `item_id`: 请求的视频ID
    - `key_words`: 评论中提取的关键词列表，包含以下字段:
      - `key_word`: 关键词文本
      - `comments`: 包含该关键词的评论列表，每条评论包含:
        - `cid`: 评论ID
        - `text`: 评论内容
        - `create_date`: 评论创建时间戳
        - `digg_count`: 评论获赞数量
        - `comment_type`: 评论类型
        - `comment_author`: 评论作者信息
          - `uid`: 用户ID
          - `nick_name`: 用户昵称
          - `cover`: 用户头像信息
            - `url_list`: 头像URL列表

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_comment_keywords\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"key_words\": [
          {
            \"key_word\": \"tik tok\",
            \"comments\": [
              {
                \"cid\": \"7502621950457463574\",
                \"comment_author\": {
                  \"nick_name\": \"ollie_russell05\",
                  \"uid\": \"7332627012203414560\"
                },
                \"create_date\": 1746840350,
                \"digg_count\": 17,
                \"text\": \"Imagine been tik tok and only getting 700 likes 🥀🙏😭\"
              }
            ]
          },
          {
            \"key_word\": \"go viral\",
            \"comments\": [
              {
                \"cid\": \"7502743477604680465\",
                \"comment_author\": {
                  \"nick_name\": \"★ 🇦🇫\",
                  \"uid\": \"7274239704915149829\"
                },
                \"create_date\": 1746868614,
                \"digg_count\": 13,
                \"text\": \"I want to go viral\"
              }
            ]
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Analyze popular keywords and topics in video comments to uncover user feedback
    - Extract main content and opinions from audience comments to understand viewer focus points
    - Support creators in optimizing content strategy and enhancing audience engagement and connection

    ### Parameters:
    - item_id: Video ID, required parameter, can be obtained from video sharing links or TikTok Studio

    ### Return Description:
    - `item_id`: The requested video ID
    - `key_words`: List of keywords extracted from comments, including:
      - `key_word`: Keyword text
      - `comments`: List of comments containing this keyword, each comment includes:
        - `cid`: Comment ID
        - `text`: Comment content
        - `create_date`: Comment creation timestamp
        - `digg_count`: Number of likes on the comment
        - `comment_type`: Comment type
        - `comment_author`: Comment author information
          - `uid`: User ID
          - `nick_name`: User nickname
          - `cover`: User avatar information
            - `url_list`: List of avatar URLs

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_comment_keywords\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"key_words\": [
          {
            \"key_word\": \"tik tok\",
            \"comments\": [
              {
                \"cid\": \"7502621950457463574\",
                \"comment_author\": {
                  \"nick_name\": \"ollie_russell05\",
                  \"uid\": \"7332627012203414560\"
                },
                \"create_date\": 1746840350,
                \"digg_count\": 17,
                \"text\": \"Imagine been tik tok and only getting 700 likes 🥀🙏😭\"
              }
            ]
          },
          {
            \"key_word\": \"go viral\",
            \"comments\": [
              {
                \"cid\": \"7502743477604680465\",
                \"comment_author\": {
                  \"nick_name\": \"★ 🇦🇫\",
                  \"uid\": \"7274239704915149829\"
                },
                \"create_date\": 1746868614,
                \"digg_count\": 13,
                \"text\": \"I want to go viral\"
              }
            ]
          }
        ]
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频评论关键词分析/Get comment keywords analysis

     # [中文]
    ### 用途:
    - 分析视频评论中出现的热门关键词和话题，挖掘用户反馈
    - 提取观众评论中的主要内容和观点，帮助理解受众关注点
    - 支持创作者优化内容策略，增强与观众的互动和连接

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频分享链接或TikTok Studio获取

    ### 返回内容说明:
    - `item_id`: 请求的视频ID
    - `key_words`: 评论中提取的关键词列表，包含以下字段:
      - `key_word`: 关键词文本
      - `comments`: 包含该关键词的评论列表，每条评论包含:
        - `cid`: 评论ID
        - `text`: 评论内容
        - `create_date`: 评论创建时间戳
        - `digg_count`: 评论获赞数量
        - `comment_type`: 评论类型
        - `comment_author`: 评论作者信息
          - `uid`: 用户ID
          - `nick_name`: 用户昵称
          - `cover`: 用户头像信息
            - `url_list`: 头像URL列表

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_comment_keywords\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"key_words\": [
          {
            \"key_word\": \"tik tok\",
            \"comments\": [
              {
                \"cid\": \"7502621950457463574\",
                \"comment_author\": {
                  \"nick_name\": \"ollie_russell05\",
                  \"uid\": \"7332627012203414560\"
                },
                \"create_date\": 1746840350,
                \"digg_count\": 17,
                \"text\": \"Imagine been tik tok and only getting 700 likes 🥀🙏😭\"
              }
            ]
          },
          {
            \"key_word\": \"go viral\",
            \"comments\": [
              {
                \"cid\": \"7502743477604680465\",
                \"comment_author\": {
                  \"nick_name\": \"★ 🇦🇫\",
                  \"uid\": \"7274239704915149829\"
                },
                \"create_date\": 1746868614,
                \"digg_count\": 13,
                \"text\": \"I want to go viral\"
              }
            ]
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Analyze popular keywords and topics in video comments to uncover user feedback
    - Extract main content and opinions from audience comments to understand viewer focus points
    - Support creators in optimizing content strategy and enhancing audience engagement and connection

    ### Parameters:
    - item_id: Video ID, required parameter, can be obtained from video sharing links or TikTok Studio

    ### Return Description:
    - `item_id`: The requested video ID
    - `key_words`: List of keywords extracted from comments, including:
      - `key_word`: Keyword text
      - `comments`: List of comments containing this keyword, each comment includes:
        - `cid`: Comment ID
        - `text`: Comment content
        - `create_date`: Comment creation timestamp
        - `digg_count`: Number of likes on the comment
        - `comment_type`: Comment type
        - `comment_author`: Comment author information
          - `uid`: User ID
          - `nick_name`: User nickname
          - `cover`: User avatar information
            - `url_list`: List of avatar URLs

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_comment_keywords\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"key_words\": [
          {
            \"key_word\": \"tik tok\",
            \"comments\": [
              {
                \"cid\": \"7502621950457463574\",
                \"comment_author\": {
                  \"nick_name\": \"ollie_russell05\",
                  \"uid\": \"7332627012203414560\"
                },
                \"create_date\": 1746840350,
                \"digg_count\": 17,
                \"text\": \"Imagine been tik tok and only getting 700 likes 🥀🙏😭\"
              }
            ]
          },
          {
            \"key_word\": \"go viral\",
            \"comments\": [
              {
                \"cid\": \"7502743477604680465\",
                \"comment_author\": {
                  \"nick_name\": \"★ 🇦🇫\",
                  \"uid\": \"7274239704915149829\"
                },
                \"create_date\": 1746868614,
                \"digg_count\": 13,
                \"text\": \"I want to go viral\"
              }
            ]
          }
        ]
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id

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
        )
    ).parsed
