from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.tik_tok_appv3_content_translate import TikTokAPPV3ContentTranslate
from ...types import Response


def _get_kwargs(
    *,
    body: TikTokAPPV3ContentTranslate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/app/v3/fetch_content_translate",
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
    body: TikTokAPPV3ContentTranslate,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取内容翻译数据/Get content translation data

     # [中文]
    ### 用途:
    - 获取内容翻译数据
    ### 参数:
    - trg_lang: 目标语言
        - zh-Hans: 简体中文
        - zh-Hant: 繁体中文
        - en: 英语
        - ja: 日语
        - ko: 韩语
        - fr: 法语
        - de: 德语
        - ru: 俄语
        - es: 西班牙语
        - pt: 葡萄牙语
        - vi: 越南语
        - th: 泰语
        - id: 印尼语
        - ar: 阿拉伯语
        - it: 意大利语
        - tr: 土耳其语
        - he: 希伯来语
        - pl: 波兰语
        - nl: 荷兰语
        - sv: 瑞典语
        - da: 丹麦语
        - fi: 芬兰语
        - no: 挪威语
        - cs: 捷克语
        - hu: 匈牙利语
    - src_content: 源内容，也就是需要翻译的内容，长度不超过5000个字符，如果超过5000个字符，只会翻译前5000个字符。
    ### 返回:
    - 内容翻译数据

    # [English]
    ### Purpose:
    - Get content translation data
    ### Parameters:
    - trg_lang: Target language
        - zh-Hans: Simplified Chinese
        - zh-Hant: Traditional Chinese
        - en: English
        - ja: Japanese
        - ko: Korean
        - fr: French
        - de: German
        - ru: Russian
        - es: Spanish
        - pt: Portuguese
        - vi: Vietnamese
        - th: Thai
        - id: Indonesian
        - ar: Arabic
        - it: Italian
        - tr: Turkish
        - he: Hebrew
        - pl: Polish
        - nl: Dutch
        - sv: Swedish
        - da: Danish
        - fi: Finnish
        - no: Norwegian
        - cs: Czech
        - hu: Hungarian
    - src_content: Source content, that is, the content that needs to be translated, the length does not
    exceed 5000 characters, if it exceeds 5000 characters, only the first 5000 characters will be
    translated.
    ### Return:
    - Content translation data

    # [示例/Example]
    trg_lang = \"zh-Hans\"
    src_content = \"Hello, welcome to TikHub!\"

    Args:
        body (TikTokAPPV3ContentTranslate):

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
    body: TikTokAPPV3ContentTranslate,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取内容翻译数据/Get content translation data

     # [中文]
    ### 用途:
    - 获取内容翻译数据
    ### 参数:
    - trg_lang: 目标语言
        - zh-Hans: 简体中文
        - zh-Hant: 繁体中文
        - en: 英语
        - ja: 日语
        - ko: 韩语
        - fr: 法语
        - de: 德语
        - ru: 俄语
        - es: 西班牙语
        - pt: 葡萄牙语
        - vi: 越南语
        - th: 泰语
        - id: 印尼语
        - ar: 阿拉伯语
        - it: 意大利语
        - tr: 土耳其语
        - he: 希伯来语
        - pl: 波兰语
        - nl: 荷兰语
        - sv: 瑞典语
        - da: 丹麦语
        - fi: 芬兰语
        - no: 挪威语
        - cs: 捷克语
        - hu: 匈牙利语
    - src_content: 源内容，也就是需要翻译的内容，长度不超过5000个字符，如果超过5000个字符，只会翻译前5000个字符。
    ### 返回:
    - 内容翻译数据

    # [English]
    ### Purpose:
    - Get content translation data
    ### Parameters:
    - trg_lang: Target language
        - zh-Hans: Simplified Chinese
        - zh-Hant: Traditional Chinese
        - en: English
        - ja: Japanese
        - ko: Korean
        - fr: French
        - de: German
        - ru: Russian
        - es: Spanish
        - pt: Portuguese
        - vi: Vietnamese
        - th: Thai
        - id: Indonesian
        - ar: Arabic
        - it: Italian
        - tr: Turkish
        - he: Hebrew
        - pl: Polish
        - nl: Dutch
        - sv: Swedish
        - da: Danish
        - fi: Finnish
        - no: Norwegian
        - cs: Czech
        - hu: Hungarian
    - src_content: Source content, that is, the content that needs to be translated, the length does not
    exceed 5000 characters, if it exceeds 5000 characters, only the first 5000 characters will be
    translated.
    ### Return:
    - Content translation data

    # [示例/Example]
    trg_lang = \"zh-Hans\"
    src_content = \"Hello, welcome to TikHub!\"

    Args:
        body (TikTokAPPV3ContentTranslate):

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
    body: TikTokAPPV3ContentTranslate,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取内容翻译数据/Get content translation data

     # [中文]
    ### 用途:
    - 获取内容翻译数据
    ### 参数:
    - trg_lang: 目标语言
        - zh-Hans: 简体中文
        - zh-Hant: 繁体中文
        - en: 英语
        - ja: 日语
        - ko: 韩语
        - fr: 法语
        - de: 德语
        - ru: 俄语
        - es: 西班牙语
        - pt: 葡萄牙语
        - vi: 越南语
        - th: 泰语
        - id: 印尼语
        - ar: 阿拉伯语
        - it: 意大利语
        - tr: 土耳其语
        - he: 希伯来语
        - pl: 波兰语
        - nl: 荷兰语
        - sv: 瑞典语
        - da: 丹麦语
        - fi: 芬兰语
        - no: 挪威语
        - cs: 捷克语
        - hu: 匈牙利语
    - src_content: 源内容，也就是需要翻译的内容，长度不超过5000个字符，如果超过5000个字符，只会翻译前5000个字符。
    ### 返回:
    - 内容翻译数据

    # [English]
    ### Purpose:
    - Get content translation data
    ### Parameters:
    - trg_lang: Target language
        - zh-Hans: Simplified Chinese
        - zh-Hant: Traditional Chinese
        - en: English
        - ja: Japanese
        - ko: Korean
        - fr: French
        - de: German
        - ru: Russian
        - es: Spanish
        - pt: Portuguese
        - vi: Vietnamese
        - th: Thai
        - id: Indonesian
        - ar: Arabic
        - it: Italian
        - tr: Turkish
        - he: Hebrew
        - pl: Polish
        - nl: Dutch
        - sv: Swedish
        - da: Danish
        - fi: Finnish
        - no: Norwegian
        - cs: Czech
        - hu: Hungarian
    - src_content: Source content, that is, the content that needs to be translated, the length does not
    exceed 5000 characters, if it exceeds 5000 characters, only the first 5000 characters will be
    translated.
    ### Return:
    - Content translation data

    # [示例/Example]
    trg_lang = \"zh-Hans\"
    src_content = \"Hello, welcome to TikHub!\"

    Args:
        body (TikTokAPPV3ContentTranslate):

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
    body: TikTokAPPV3ContentTranslate,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取内容翻译数据/Get content translation data

     # [中文]
    ### 用途:
    - 获取内容翻译数据
    ### 参数:
    - trg_lang: 目标语言
        - zh-Hans: 简体中文
        - zh-Hant: 繁体中文
        - en: 英语
        - ja: 日语
        - ko: 韩语
        - fr: 法语
        - de: 德语
        - ru: 俄语
        - es: 西班牙语
        - pt: 葡萄牙语
        - vi: 越南语
        - th: 泰语
        - id: 印尼语
        - ar: 阿拉伯语
        - it: 意大利语
        - tr: 土耳其语
        - he: 希伯来语
        - pl: 波兰语
        - nl: 荷兰语
        - sv: 瑞典语
        - da: 丹麦语
        - fi: 芬兰语
        - no: 挪威语
        - cs: 捷克语
        - hu: 匈牙利语
    - src_content: 源内容，也就是需要翻译的内容，长度不超过5000个字符，如果超过5000个字符，只会翻译前5000个字符。
    ### 返回:
    - 内容翻译数据

    # [English]
    ### Purpose:
    - Get content translation data
    ### Parameters:
    - trg_lang: Target language
        - zh-Hans: Simplified Chinese
        - zh-Hant: Traditional Chinese
        - en: English
        - ja: Japanese
        - ko: Korean
        - fr: French
        - de: German
        - ru: Russian
        - es: Spanish
        - pt: Portuguese
        - vi: Vietnamese
        - th: Thai
        - id: Indonesian
        - ar: Arabic
        - it: Italian
        - tr: Turkish
        - he: Hebrew
        - pl: Polish
        - nl: Dutch
        - sv: Swedish
        - da: Danish
        - fi: Finnish
        - no: Norwegian
        - cs: Czech
        - hu: Hungarian
    - src_content: Source content, that is, the content that needs to be translated, the length does not
    exceed 5000 characters, if it exceeds 5000 characters, only the first 5000 characters will be
    translated.
    ### Return:
    - Content translation data

    # [示例/Example]
    trg_lang = \"zh-Hans\"
    src_content = \"Hello, welcome to TikHub!\"

    Args:
        body (TikTokAPPV3ContentTranslate):

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
