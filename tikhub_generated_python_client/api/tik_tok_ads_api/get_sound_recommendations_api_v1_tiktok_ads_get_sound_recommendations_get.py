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
    clip_id: str,
    limit: Union[Unset, int] = 6,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["clip_id"] = clip_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_sound_recommendations",
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
    clip_id: str,
    limit: Union[Unset, int] = 6,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐推荐/Get sound recommendations

     # [中文]
    ### 用途:
    - 基于指定音乐获取相似的推荐音乐
    - 发现风格相近或使用场景类似的音乐
    - 扩展音乐选择范围，找到更多合适的配乐

    ### 参数:
    - clip_id: 参考音乐ID，必填参数
    - limit: 推荐数量，默认6

    ### 返回内容说明:
    - `musics`: 推荐音乐列表
      - `author`: 音乐作者
      - `cover`: 封面图URL
      - `music_id`: 音乐ID
      - `music_url`: 音乐播放URL
      - `title`: 音乐标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",
      \"params\": {
        \"clip_id\": \"7156826385225353217\",
        \"limit\": \"6\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"musics\": [
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949146013727653889\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/d0d0dca4400886718099898494b7e31b.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(810161)\"
            },
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949294080044843010\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/451acbadd83a76748a99878ccfef2df5.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(816672)\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get similar music recommendations based on specified music
    - Discover music with similar styles or usage scenarios
    - Expand music selection range to find more suitable soundtracks

    ### Parameters:
    - clip_id: Reference sound clip ID, required parameter
    - limit: Number of recommendations, default 6

    ### Return Description:
    - `musics`: Recommended music list
      - `author`: Music author
      - `cover`: Cover image URL
      - `music_id`: Music ID
      - `music_url`: Music playback URL
      - `title`: Music title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",
      \"params\": {
        \"clip_id\": \"7156826385225353217\",
        \"limit\": 6
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"musics\": [
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949146013727653889\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/d0d0dca4400886718099898494b7e31b.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(810161)\"
            },
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949294080044843010\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/451acbadd83a76748a99878ccfef2df5.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(816672)\"
            }
          ]
        }
      }
    }
    ```

    Args:
        clip_id (str): 参考音乐ID/Reference sound clip ID
        limit (Union[Unset, int]): 推荐数量/Number of recommendations Default: 6.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        clip_id=clip_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    clip_id: str,
    limit: Union[Unset, int] = 6,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐推荐/Get sound recommendations

     # [中文]
    ### 用途:
    - 基于指定音乐获取相似的推荐音乐
    - 发现风格相近或使用场景类似的音乐
    - 扩展音乐选择范围，找到更多合适的配乐

    ### 参数:
    - clip_id: 参考音乐ID，必填参数
    - limit: 推荐数量，默认6

    ### 返回内容说明:
    - `musics`: 推荐音乐列表
      - `author`: 音乐作者
      - `cover`: 封面图URL
      - `music_id`: 音乐ID
      - `music_url`: 音乐播放URL
      - `title`: 音乐标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",
      \"params\": {
        \"clip_id\": \"7156826385225353217\",
        \"limit\": \"6\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"musics\": [
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949146013727653889\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/d0d0dca4400886718099898494b7e31b.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(810161)\"
            },
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949294080044843010\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/451acbadd83a76748a99878ccfef2df5.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(816672)\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get similar music recommendations based on specified music
    - Discover music with similar styles or usage scenarios
    - Expand music selection range to find more suitable soundtracks

    ### Parameters:
    - clip_id: Reference sound clip ID, required parameter
    - limit: Number of recommendations, default 6

    ### Return Description:
    - `musics`: Recommended music list
      - `author`: Music author
      - `cover`: Cover image URL
      - `music_id`: Music ID
      - `music_url`: Music playback URL
      - `title`: Music title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",
      \"params\": {
        \"clip_id\": \"7156826385225353217\",
        \"limit\": 6
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"musics\": [
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949146013727653889\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/d0d0dca4400886718099898494b7e31b.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(810161)\"
            },
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949294080044843010\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/451acbadd83a76748a99878ccfef2df5.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(816672)\"
            }
          ]
        }
      }
    }
    ```

    Args:
        clip_id (str): 参考音乐ID/Reference sound clip ID
        limit (Union[Unset, int]): 推荐数量/Number of recommendations Default: 6.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        clip_id=clip_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    clip_id: str,
    limit: Union[Unset, int] = 6,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐推荐/Get sound recommendations

     # [中文]
    ### 用途:
    - 基于指定音乐获取相似的推荐音乐
    - 发现风格相近或使用场景类似的音乐
    - 扩展音乐选择范围，找到更多合适的配乐

    ### 参数:
    - clip_id: 参考音乐ID，必填参数
    - limit: 推荐数量，默认6

    ### 返回内容说明:
    - `musics`: 推荐音乐列表
      - `author`: 音乐作者
      - `cover`: 封面图URL
      - `music_id`: 音乐ID
      - `music_url`: 音乐播放URL
      - `title`: 音乐标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",
      \"params\": {
        \"clip_id\": \"7156826385225353217\",
        \"limit\": \"6\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"musics\": [
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949146013727653889\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/d0d0dca4400886718099898494b7e31b.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(810161)\"
            },
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949294080044843010\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/451acbadd83a76748a99878ccfef2df5.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(816672)\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get similar music recommendations based on specified music
    - Discover music with similar styles or usage scenarios
    - Expand music selection range to find more suitable soundtracks

    ### Parameters:
    - clip_id: Reference sound clip ID, required parameter
    - limit: Number of recommendations, default 6

    ### Return Description:
    - `musics`: Recommended music list
      - `author`: Music author
      - `cover`: Cover image URL
      - `music_id`: Music ID
      - `music_url`: Music playback URL
      - `title`: Music title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",
      \"params\": {
        \"clip_id\": \"7156826385225353217\",
        \"limit\": 6
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"musics\": [
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949146013727653889\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/d0d0dca4400886718099898494b7e31b.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(810161)\"
            },
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949294080044843010\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/451acbadd83a76748a99878ccfef2df5.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(816672)\"
            }
          ]
        }
      }
    }
    ```

    Args:
        clip_id (str): 参考音乐ID/Reference sound clip ID
        limit (Union[Unset, int]): 推荐数量/Number of recommendations Default: 6.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        clip_id=clip_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    clip_id: str,
    limit: Union[Unset, int] = 6,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐推荐/Get sound recommendations

     # [中文]
    ### 用途:
    - 基于指定音乐获取相似的推荐音乐
    - 发现风格相近或使用场景类似的音乐
    - 扩展音乐选择范围，找到更多合适的配乐

    ### 参数:
    - clip_id: 参考音乐ID，必填参数
    - limit: 推荐数量，默认6

    ### 返回内容说明:
    - `musics`: 推荐音乐列表
      - `author`: 音乐作者
      - `cover`: 封面图URL
      - `music_id`: 音乐ID
      - `music_url`: 音乐播放URL
      - `title`: 音乐标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",
      \"params\": {
        \"clip_id\": \"7156826385225353217\",
        \"limit\": \"6\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"musics\": [
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949146013727653889\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/d0d0dca4400886718099898494b7e31b.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(810161)\"
            },
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949294080044843010\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/451acbadd83a76748a99878ccfef2df5.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(816672)\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get similar music recommendations based on specified music
    - Discover music with similar styles or usage scenarios
    - Expand music selection range to find more suitable soundtracks

    ### Parameters:
    - clip_id: Reference sound clip ID, required parameter
    - limit: Number of recommendations, default 6

    ### Return Description:
    - `musics`: Recommended music list
      - `author`: Music author
      - `cover`: Cover image URL
      - `music_id`: Music ID
      - `music_url`: Music playback URL
      - `title`: Music title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_recommendations\",
      \"params\": {
        \"clip_id\": \"7156826385225353217\",
        \"limit\": 6
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"musics\": [
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949146013727653889\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/d0d0dca4400886718099898494b7e31b.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(810161)\"
            },
            {
              \"author\": \"zomap\",
              \"cover\": \"https://p16-sg-default.akamaized.net/aweme/720x720/tiktok-
    obj/6f9903752958820d144fa90d54cb5f3a.png.jpeg\",
              \"music_id\": \"6949294080044843010\",
              \"music_url\": \"https://sf16-sg-default.akamaized.net/obj/tiktok-
    obj/451acbadd83a76748a99878ccfef2df5.mp3\",
              \"title\": \"Relaxed and gentle fashionable chillout(816672)\"
            }
          ]
        }
      }
    }
    ```

    Args:
        clip_id (str): 参考音乐ID/Reference sound clip ID
        limit (Union[Unset, int]): 推荐数量/Number of recommendations Default: 6.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            clip_id=clip_id,
            limit=limit,
        )
    ).parsed
