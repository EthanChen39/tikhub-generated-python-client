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
    live_room_url: str,
    danmaku_type: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["live_room_url"] = live_room_url

    params["danmaku_type"] = danmaku_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/douyin_live_room",
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
    live_room_url: str,
    danmaku_type: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """提取直播间弹幕/Extract live room danmaku

     # [中文]
    ### 用途:
    - 提取直播间弹幕
    #### 价格:
    - 每10条数据消耗0.001$，支持阶梯式计费折扣。
    ### 参数:
    - live_room_url: 直播间链接
    - danmaku_type: 消息类型
        - WebcastRoomMessage：直播间消息
        - WebcastLikeMessage：点赞消息
        - WebcastMemberMessage：成员消息
        - WebcastChatMessage：聊天消息
        - WebcastGiftMessage：礼物消息
        - WebcastSocialMessage：社交消息
        - WebcastRoomUserSeqMessage：用户序列消息
        - WebcastUpdateFanTicketMessage：更新粉丝消息
        - WebcastCommonTextMessage：常规文本消息
        - WebcastMatchAgainstScoreMessage：比赛得分消息
        - WebcastFansclubMessage：粉丝俱乐部消息
        - WebcastRanklistHourEntranceMessage：排行榜小时入口消息
        - WebcastRoomStatsMessage：直播间统计消息
        - WebcastLiveShoppingMessage: 直播购物消息
        - WebcastLiveEcomGeneralMessage: 直播电商通用消息
        - WebcastProductChangeMessage: 直播商品变更消息
        - WebcastRoomStreamAdaptationMessage: 直播间流适配消息
        - WebcastNotifyEffectMessage: 通知效果消息
        - WebcastLightGiftMessage: 亮礼物消息
        - WebcastProfitInteractionScoreMessage: 收益互动分消息
        - WebcastRoomRankMessage: 直播间排行消息
    ### 返回:
    - 弹幕数据的WebSocket连接信息，需要使用WebSocket连接获取弹幕数据，此接口不返回弹幕数据。

    # [English]
    ### Purpose:
    - Extract live room danmaku
    #### Price:
    - 0.001$ per 10 data, support tiered billing discounts.
    ### Parameters:
    - live_room_url: Live room link
    - danmaku_type: Message type
        - WebcastRoomMessage: Live room message
        - WebcastLikeMessage: Like message
        - WebcastMemberMessage: Member message
        - WebcastChatMessage: Chat message
        - WebcastGiftMessage: Gift message
        - WebcastSocialMessage: Social message
        - WebcastRoomUserSeqMessage: User sequence message
        - WebcastUpdateFanTicketMessage: Update fan message
        - WebcastCommonTextMessage: Common text message
        - WebcastMatchAgainstScoreMessage: Match score message
        - WebcastFansclubMessage: Fans club message
        - WebcastRanklistHourEntranceMessage: Ranking list hour entrance message
        - WebcastRoomStatsMessage: Live room statistics message
        - WebcastLiveShoppingMessage: Live shopping message
        - WebcastLiveEcomGeneralMessage: Live e-commerce general message
        - WebcastProductChangeMessage: Live product change message
        - WebcastRoomStreamAdaptationMessage: Live room stream adaptation message
        - WebcastNotifyEffectMessage: Notification effect message
        - WebcastLightGiftMessage: Light gift message
        - WebcastProfitInteractionScoreMessage: Profit interaction score message
        - WebcastRoomRankMessage: Live room ranking message
    ### Return:
    - WebSocket connection information of the danmaku data, you need to use WebSocket connection to get
    the danmaku data, this interface does not return the danmaku data.

    Args:
        live_room_url (str): 直播间链接/Live room link
        danmaku_type (str): 消息类型/Message type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        live_room_url=live_room_url,
        danmaku_type=danmaku_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    live_room_url: str,
    danmaku_type: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """提取直播间弹幕/Extract live room danmaku

     # [中文]
    ### 用途:
    - 提取直播间弹幕
    #### 价格:
    - 每10条数据消耗0.001$，支持阶梯式计费折扣。
    ### 参数:
    - live_room_url: 直播间链接
    - danmaku_type: 消息类型
        - WebcastRoomMessage：直播间消息
        - WebcastLikeMessage：点赞消息
        - WebcastMemberMessage：成员消息
        - WebcastChatMessage：聊天消息
        - WebcastGiftMessage：礼物消息
        - WebcastSocialMessage：社交消息
        - WebcastRoomUserSeqMessage：用户序列消息
        - WebcastUpdateFanTicketMessage：更新粉丝消息
        - WebcastCommonTextMessage：常规文本消息
        - WebcastMatchAgainstScoreMessage：比赛得分消息
        - WebcastFansclubMessage：粉丝俱乐部消息
        - WebcastRanklistHourEntranceMessage：排行榜小时入口消息
        - WebcastRoomStatsMessage：直播间统计消息
        - WebcastLiveShoppingMessage: 直播购物消息
        - WebcastLiveEcomGeneralMessage: 直播电商通用消息
        - WebcastProductChangeMessage: 直播商品变更消息
        - WebcastRoomStreamAdaptationMessage: 直播间流适配消息
        - WebcastNotifyEffectMessage: 通知效果消息
        - WebcastLightGiftMessage: 亮礼物消息
        - WebcastProfitInteractionScoreMessage: 收益互动分消息
        - WebcastRoomRankMessage: 直播间排行消息
    ### 返回:
    - 弹幕数据的WebSocket连接信息，需要使用WebSocket连接获取弹幕数据，此接口不返回弹幕数据。

    # [English]
    ### Purpose:
    - Extract live room danmaku
    #### Price:
    - 0.001$ per 10 data, support tiered billing discounts.
    ### Parameters:
    - live_room_url: Live room link
    - danmaku_type: Message type
        - WebcastRoomMessage: Live room message
        - WebcastLikeMessage: Like message
        - WebcastMemberMessage: Member message
        - WebcastChatMessage: Chat message
        - WebcastGiftMessage: Gift message
        - WebcastSocialMessage: Social message
        - WebcastRoomUserSeqMessage: User sequence message
        - WebcastUpdateFanTicketMessage: Update fan message
        - WebcastCommonTextMessage: Common text message
        - WebcastMatchAgainstScoreMessage: Match score message
        - WebcastFansclubMessage: Fans club message
        - WebcastRanklistHourEntranceMessage: Ranking list hour entrance message
        - WebcastRoomStatsMessage: Live room statistics message
        - WebcastLiveShoppingMessage: Live shopping message
        - WebcastLiveEcomGeneralMessage: Live e-commerce general message
        - WebcastProductChangeMessage: Live product change message
        - WebcastRoomStreamAdaptationMessage: Live room stream adaptation message
        - WebcastNotifyEffectMessage: Notification effect message
        - WebcastLightGiftMessage: Light gift message
        - WebcastProfitInteractionScoreMessage: Profit interaction score message
        - WebcastRoomRankMessage: Live room ranking message
    ### Return:
    - WebSocket connection information of the danmaku data, you need to use WebSocket connection to get
    the danmaku data, this interface does not return the danmaku data.

    Args:
        live_room_url (str): 直播间链接/Live room link
        danmaku_type (str): 消息类型/Message type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        live_room_url=live_room_url,
        danmaku_type=danmaku_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    live_room_url: str,
    danmaku_type: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """提取直播间弹幕/Extract live room danmaku

     # [中文]
    ### 用途:
    - 提取直播间弹幕
    #### 价格:
    - 每10条数据消耗0.001$，支持阶梯式计费折扣。
    ### 参数:
    - live_room_url: 直播间链接
    - danmaku_type: 消息类型
        - WebcastRoomMessage：直播间消息
        - WebcastLikeMessage：点赞消息
        - WebcastMemberMessage：成员消息
        - WebcastChatMessage：聊天消息
        - WebcastGiftMessage：礼物消息
        - WebcastSocialMessage：社交消息
        - WebcastRoomUserSeqMessage：用户序列消息
        - WebcastUpdateFanTicketMessage：更新粉丝消息
        - WebcastCommonTextMessage：常规文本消息
        - WebcastMatchAgainstScoreMessage：比赛得分消息
        - WebcastFansclubMessage：粉丝俱乐部消息
        - WebcastRanklistHourEntranceMessage：排行榜小时入口消息
        - WebcastRoomStatsMessage：直播间统计消息
        - WebcastLiveShoppingMessage: 直播购物消息
        - WebcastLiveEcomGeneralMessage: 直播电商通用消息
        - WebcastProductChangeMessage: 直播商品变更消息
        - WebcastRoomStreamAdaptationMessage: 直播间流适配消息
        - WebcastNotifyEffectMessage: 通知效果消息
        - WebcastLightGiftMessage: 亮礼物消息
        - WebcastProfitInteractionScoreMessage: 收益互动分消息
        - WebcastRoomRankMessage: 直播间排行消息
    ### 返回:
    - 弹幕数据的WebSocket连接信息，需要使用WebSocket连接获取弹幕数据，此接口不返回弹幕数据。

    # [English]
    ### Purpose:
    - Extract live room danmaku
    #### Price:
    - 0.001$ per 10 data, support tiered billing discounts.
    ### Parameters:
    - live_room_url: Live room link
    - danmaku_type: Message type
        - WebcastRoomMessage: Live room message
        - WebcastLikeMessage: Like message
        - WebcastMemberMessage: Member message
        - WebcastChatMessage: Chat message
        - WebcastGiftMessage: Gift message
        - WebcastSocialMessage: Social message
        - WebcastRoomUserSeqMessage: User sequence message
        - WebcastUpdateFanTicketMessage: Update fan message
        - WebcastCommonTextMessage: Common text message
        - WebcastMatchAgainstScoreMessage: Match score message
        - WebcastFansclubMessage: Fans club message
        - WebcastRanklistHourEntranceMessage: Ranking list hour entrance message
        - WebcastRoomStatsMessage: Live room statistics message
        - WebcastLiveShoppingMessage: Live shopping message
        - WebcastLiveEcomGeneralMessage: Live e-commerce general message
        - WebcastProductChangeMessage: Live product change message
        - WebcastRoomStreamAdaptationMessage: Live room stream adaptation message
        - WebcastNotifyEffectMessage: Notification effect message
        - WebcastLightGiftMessage: Light gift message
        - WebcastProfitInteractionScoreMessage: Profit interaction score message
        - WebcastRoomRankMessage: Live room ranking message
    ### Return:
    - WebSocket connection information of the danmaku data, you need to use WebSocket connection to get
    the danmaku data, this interface does not return the danmaku data.

    Args:
        live_room_url (str): 直播间链接/Live room link
        danmaku_type (str): 消息类型/Message type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        live_room_url=live_room_url,
        danmaku_type=danmaku_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    live_room_url: str,
    danmaku_type: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """提取直播间弹幕/Extract live room danmaku

     # [中文]
    ### 用途:
    - 提取直播间弹幕
    #### 价格:
    - 每10条数据消耗0.001$，支持阶梯式计费折扣。
    ### 参数:
    - live_room_url: 直播间链接
    - danmaku_type: 消息类型
        - WebcastRoomMessage：直播间消息
        - WebcastLikeMessage：点赞消息
        - WebcastMemberMessage：成员消息
        - WebcastChatMessage：聊天消息
        - WebcastGiftMessage：礼物消息
        - WebcastSocialMessage：社交消息
        - WebcastRoomUserSeqMessage：用户序列消息
        - WebcastUpdateFanTicketMessage：更新粉丝消息
        - WebcastCommonTextMessage：常规文本消息
        - WebcastMatchAgainstScoreMessage：比赛得分消息
        - WebcastFansclubMessage：粉丝俱乐部消息
        - WebcastRanklistHourEntranceMessage：排行榜小时入口消息
        - WebcastRoomStatsMessage：直播间统计消息
        - WebcastLiveShoppingMessage: 直播购物消息
        - WebcastLiveEcomGeneralMessage: 直播电商通用消息
        - WebcastProductChangeMessage: 直播商品变更消息
        - WebcastRoomStreamAdaptationMessage: 直播间流适配消息
        - WebcastNotifyEffectMessage: 通知效果消息
        - WebcastLightGiftMessage: 亮礼物消息
        - WebcastProfitInteractionScoreMessage: 收益互动分消息
        - WebcastRoomRankMessage: 直播间排行消息
    ### 返回:
    - 弹幕数据的WebSocket连接信息，需要使用WebSocket连接获取弹幕数据，此接口不返回弹幕数据。

    # [English]
    ### Purpose:
    - Extract live room danmaku
    #### Price:
    - 0.001$ per 10 data, support tiered billing discounts.
    ### Parameters:
    - live_room_url: Live room link
    - danmaku_type: Message type
        - WebcastRoomMessage: Live room message
        - WebcastLikeMessage: Like message
        - WebcastMemberMessage: Member message
        - WebcastChatMessage: Chat message
        - WebcastGiftMessage: Gift message
        - WebcastSocialMessage: Social message
        - WebcastRoomUserSeqMessage: User sequence message
        - WebcastUpdateFanTicketMessage: Update fan message
        - WebcastCommonTextMessage: Common text message
        - WebcastMatchAgainstScoreMessage: Match score message
        - WebcastFansclubMessage: Fans club message
        - WebcastRanklistHourEntranceMessage: Ranking list hour entrance message
        - WebcastRoomStatsMessage: Live room statistics message
        - WebcastLiveShoppingMessage: Live shopping message
        - WebcastLiveEcomGeneralMessage: Live e-commerce general message
        - WebcastProductChangeMessage: Live product change message
        - WebcastRoomStreamAdaptationMessage: Live room stream adaptation message
        - WebcastNotifyEffectMessage: Notification effect message
        - WebcastLightGiftMessage: Light gift message
        - WebcastProfitInteractionScoreMessage: Profit interaction score message
        - WebcastRoomRankMessage: Live room ranking message
    ### Return:
    - WebSocket connection information of the danmaku data, you need to use WebSocket connection to get
    the danmaku data, this interface does not return the danmaku data.

    Args:
        live_room_url (str): 直播间链接/Live room link
        danmaku_type (str): 消息类型/Message type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            live_room_url=live_room_url,
            danmaku_type=danmaku_type,
        )
    ).parsed
