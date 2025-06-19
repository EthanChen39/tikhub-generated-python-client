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
    endpoint: str,
    request_per_day: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["endpoint"] = endpoint

    params["request_per_day"] = request_per_day

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tikhub/user/calculate_price",
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
    endpoint: str,
    request_per_day: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """计算价格/Calculate price

     # [中文]
    ### 用途:
    - 根据用户输入的每日请求次数以及端点信息计算最终价格。
    ### 参数:
    - endpoint: 请求的端点，用于查询端点的原始请求单价
    - request_per_day: 每日请求次数，用于计算价格，将自动根据阶梯式计费的折扣百分比计算最终价格
    ### 计算公式:
    - 总成本 = ∑ (阶梯内请求次数 * 阶梯折后单价)
    - 其中，阶梯折后单价 = 基础价格 * (1 - 折扣)
    ### 详细计算步骤:
    1. **初始化总成本**：
       总成本=0
    2. **遍历每个阶梯**：
       * 对于每个阶梯，计算该阶梯内的请求次数。
       * 计算该阶梯内的折后单价。
       * 计算该阶梯内的总费用，并累加到总成本中。
       * 更新剩余的请求次数。
    ### 数学表示:
    > 设有 𝑛 个阶梯，每个阶梯的参数为：
    * min_rpd𝑖: 第 𝑖 个阶梯的最小请求次数
    * max_rpd𝑖: 第 𝑖 个阶梯的最大请求次数
    * discount𝑖: 第 𝑖 个阶梯的折扣（百分比形式）
    * base_price：基础价格
    * request_per_day：每日请求次数
    > 那么，总成本的计算公式如下：
    - 总成本 = Σ𝑖=1𝑛（阶梯𝑖中的请求数量 * 阶梯𝑖中的折扣单价）
    - 其中，阶梯折扣单价 𝑖 = base_price * (1 - 折扣𝑖/100)
    - 该阶梯中的请求数 𝑖 = min(request_per_day - 累计付费请求数, max_rpd𝑖 - min_rpd𝑖)
    ### 示例
    > 假设有以下定价阶梯：
    * 第 1 阶梯：0 ≤ rpd < 1000，折扣 0%
    * 第 2 阶梯：1000 ≤ rpd < 5000，折扣 10%
    * 第 3 阶梯：5000 ≤ rpd < 10000，折扣 20%
    * 第 4 阶梯：10000 ≤ rpd < 20000，折扣 30%
    * 第 5 阶梯：20000 ≤ rpd < 30000，折扣 40%
    * 第 6 阶梯：30000 ≤ rpd，折扣 50%
    > 假设基础价格为 0.001 USD，每日请求次数为 12000，则计算过程如下：
    1. **第 1 阶梯**（0 ≤ rpd < 1000）：
       * 阶梯内请求次数=1000−0=1000
       * 阶梯折后单价=0.001×(1−0/100)=0.001
       * 总成本=1000×0.001=1
    2. **第 2 阶梯**（1000 ≤ rpd < 5000）：
       * 阶梯内请求次数=5000−1000=4000
       * 阶梯折后单价=0.001×(1−10/100)=0.0009
       * 总成本=4000×0.0009=3.6
    3. **第 3 阶梯**（5000 ≤ rpd < 10000）：
       * 阶梯内请求次数=10000−5000=5000
       * 阶梯折后单价=0.001×(1−20/100)=0.0008
       * 总成本=5000×0.0008=4
    4. **第 4 阶梯**（10000 ≤ rpd < 20000）：
       * 阶梯内请求次数=12000−10000=2000
       * 阶梯折后单价=0.001×(1−30/100)=0.0007
       * 总成本=2000×0.0007=1.4
    5. **累加总成本**：
       * 总成本=1+3.6+4+1.4=10
    ### 返回:
    - 端点uri
    - 每日请求次数
    - 端点原始请求单价
    - 总价格
    - 货币单位
    - 阶梯式计费的折扣百分比信息

    # [English]
    ### Purpose:
    - Calculate the final price based on the user's input of the number of daily requests and endpoint
    information.
    - Price calculation formula: Price = Number of daily requests * (Original request unit price of the
    endpoint * (1 - discount percentage of tiered billing))
    ### Parameters:
    - endpoint: Requested endpoint, used to query the original request unit price of the endpoint
    - request_per_day: Number of daily requests, used to calculate the price, the final price will be
    calculated automatically based on the discount percentage of the tiered billing
    ### Calculation formula:
    - Total cost = ∑ (Number of requests in the tier * Discounted unit price in the tier)
    - Where, Discounted unit price in the tier = Base price * (1 - Discount)
    ### Detailed calculation steps:
    1. **Initialize the total cost**:
         Total cost = 0
    2. **Traverse each tier**:
            * For each tier, calculate the number of requests in the tier.
            * Calculate the discounted unit price in the tier.
            * Calculate the total cost in the tier and add it to the total cost.
            * Update the remaining number of requests.
    ### Mathematical representation:
    Suppose there are 𝑛 tiers, and the parameters of each tier are:
    * min_rpd𝑖: The minimum number of requests in the 𝑖-th tier
    * max_rpd𝑖: The maximum number of requests in the 𝑖-th tier
    * discount𝑖: The discount of the 𝑖-th tier (in percentage form)
    * base_price: Base price
    * request_per_day: Number of daily requests
    > Then, the formula for calculating the total cost is as follows:
    - Total cost = ∑𝑖=1𝑛(Number of requests in the tier 𝑖 * Discounted unit price in the tier 𝑖)
    - Where, Discounted unit price in the tier 𝑖 = base_price * (1 - discount𝑖/100)
    - Number of requests in the tier 𝑖 = min(request_per_day - accumulated number of paid requests,
    max_rpd𝑖 - min_rpd𝑖)
    ### Example
    Suppose there are the following pricing tiers:
    * Tier 1: 0 ≤ rpd < 1000, discount 0%
    * Tier 2: 1000 ≤ rpd < 5000, discount 10%
    * Tier 3: 5000 ≤ rpd < 10000, discount 20%
    * Tier 4: 10000 ≤ rpd < 20000, discount 30%
    * Tier 5: 20000 ≤ rpd < 30000, discount 40%
    * Tier 6: 30000 ≤ rpd, discount 50%
    > Suppose the base price is 0.001 USD and the number of daily requests is 12000, the calculation
    process is as follows:
    1. **Tier 1** (0 ≤ rpd < 1000):
         - Number of requests in the tier 1 = 1000 - 0 = 1000
         - Discounted unit price in the tier 1 = 0.001 * (1 - 0/100) = 0.001
         - Total cost 1 = 1000 * 0.001 = 1
    2. **Tier 2** (1000 ≤ rpd < 5000):
        - Number of requests in the tier 2 = 5000 - 1000 = 4000
        - Discounted unit price in the tier 2 = 0.001 * (1 - 10/100) = 0.0009
        - Total cost 2 = 4000 * 0.0009 = 3.6
    3. **Tier 3** (5000 ≤ rpd < 10000):
        - Number of requests in the tier 3 = 10000 - 5000 = 5000
        - Discounted unit price in the tier 3 = 0.001 * (1 - 20/100) = 0.0008
        - Total cost 3 = 5000 * 0.0008 = 4
    4. **Tier 4** (10000 ≤ rpd < 20000):
        - Number of requests in the tier 4 = 12000 - 10000 = 2000
        - Discounted unit price in the tier 4 = 0.001 * (1 - 30/100) = 0.0007
        - Total cost 4 = 2000 * 0.0007 = 1.4
    5. **Accumulated total cost**:
        - Total cost = 1 + 3.6 + 4 + 1.4 = 10
    ### Return:
    - Endpoint uri
    - Number of daily requests
    - Original request unit price of the endpoint
    - Total price
    - Currency unit
    - Discount percentage information of tiered billing

    Args:
        endpoint (str): 请求的端点/Requested endpoint
        request_per_day (Union[Unset, int]): 每日请求次数/Request per day Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
        request_per_day=request_per_day,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    endpoint: str,
    request_per_day: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """计算价格/Calculate price

     # [中文]
    ### 用途:
    - 根据用户输入的每日请求次数以及端点信息计算最终价格。
    ### 参数:
    - endpoint: 请求的端点，用于查询端点的原始请求单价
    - request_per_day: 每日请求次数，用于计算价格，将自动根据阶梯式计费的折扣百分比计算最终价格
    ### 计算公式:
    - 总成本 = ∑ (阶梯内请求次数 * 阶梯折后单价)
    - 其中，阶梯折后单价 = 基础价格 * (1 - 折扣)
    ### 详细计算步骤:
    1. **初始化总成本**：
       总成本=0
    2. **遍历每个阶梯**：
       * 对于每个阶梯，计算该阶梯内的请求次数。
       * 计算该阶梯内的折后单价。
       * 计算该阶梯内的总费用，并累加到总成本中。
       * 更新剩余的请求次数。
    ### 数学表示:
    > 设有 𝑛 个阶梯，每个阶梯的参数为：
    * min_rpd𝑖: 第 𝑖 个阶梯的最小请求次数
    * max_rpd𝑖: 第 𝑖 个阶梯的最大请求次数
    * discount𝑖: 第 𝑖 个阶梯的折扣（百分比形式）
    * base_price：基础价格
    * request_per_day：每日请求次数
    > 那么，总成本的计算公式如下：
    - 总成本 = Σ𝑖=1𝑛（阶梯𝑖中的请求数量 * 阶梯𝑖中的折扣单价）
    - 其中，阶梯折扣单价 𝑖 = base_price * (1 - 折扣𝑖/100)
    - 该阶梯中的请求数 𝑖 = min(request_per_day - 累计付费请求数, max_rpd𝑖 - min_rpd𝑖)
    ### 示例
    > 假设有以下定价阶梯：
    * 第 1 阶梯：0 ≤ rpd < 1000，折扣 0%
    * 第 2 阶梯：1000 ≤ rpd < 5000，折扣 10%
    * 第 3 阶梯：5000 ≤ rpd < 10000，折扣 20%
    * 第 4 阶梯：10000 ≤ rpd < 20000，折扣 30%
    * 第 5 阶梯：20000 ≤ rpd < 30000，折扣 40%
    * 第 6 阶梯：30000 ≤ rpd，折扣 50%
    > 假设基础价格为 0.001 USD，每日请求次数为 12000，则计算过程如下：
    1. **第 1 阶梯**（0 ≤ rpd < 1000）：
       * 阶梯内请求次数=1000−0=1000
       * 阶梯折后单价=0.001×(1−0/100)=0.001
       * 总成本=1000×0.001=1
    2. **第 2 阶梯**（1000 ≤ rpd < 5000）：
       * 阶梯内请求次数=5000−1000=4000
       * 阶梯折后单价=0.001×(1−10/100)=0.0009
       * 总成本=4000×0.0009=3.6
    3. **第 3 阶梯**（5000 ≤ rpd < 10000）：
       * 阶梯内请求次数=10000−5000=5000
       * 阶梯折后单价=0.001×(1−20/100)=0.0008
       * 总成本=5000×0.0008=4
    4. **第 4 阶梯**（10000 ≤ rpd < 20000）：
       * 阶梯内请求次数=12000−10000=2000
       * 阶梯折后单价=0.001×(1−30/100)=0.0007
       * 总成本=2000×0.0007=1.4
    5. **累加总成本**：
       * 总成本=1+3.6+4+1.4=10
    ### 返回:
    - 端点uri
    - 每日请求次数
    - 端点原始请求单价
    - 总价格
    - 货币单位
    - 阶梯式计费的折扣百分比信息

    # [English]
    ### Purpose:
    - Calculate the final price based on the user's input of the number of daily requests and endpoint
    information.
    - Price calculation formula: Price = Number of daily requests * (Original request unit price of the
    endpoint * (1 - discount percentage of tiered billing))
    ### Parameters:
    - endpoint: Requested endpoint, used to query the original request unit price of the endpoint
    - request_per_day: Number of daily requests, used to calculate the price, the final price will be
    calculated automatically based on the discount percentage of the tiered billing
    ### Calculation formula:
    - Total cost = ∑ (Number of requests in the tier * Discounted unit price in the tier)
    - Where, Discounted unit price in the tier = Base price * (1 - Discount)
    ### Detailed calculation steps:
    1. **Initialize the total cost**:
         Total cost = 0
    2. **Traverse each tier**:
            * For each tier, calculate the number of requests in the tier.
            * Calculate the discounted unit price in the tier.
            * Calculate the total cost in the tier and add it to the total cost.
            * Update the remaining number of requests.
    ### Mathematical representation:
    Suppose there are 𝑛 tiers, and the parameters of each tier are:
    * min_rpd𝑖: The minimum number of requests in the 𝑖-th tier
    * max_rpd𝑖: The maximum number of requests in the 𝑖-th tier
    * discount𝑖: The discount of the 𝑖-th tier (in percentage form)
    * base_price: Base price
    * request_per_day: Number of daily requests
    > Then, the formula for calculating the total cost is as follows:
    - Total cost = ∑𝑖=1𝑛(Number of requests in the tier 𝑖 * Discounted unit price in the tier 𝑖)
    - Where, Discounted unit price in the tier 𝑖 = base_price * (1 - discount𝑖/100)
    - Number of requests in the tier 𝑖 = min(request_per_day - accumulated number of paid requests,
    max_rpd𝑖 - min_rpd𝑖)
    ### Example
    Suppose there are the following pricing tiers:
    * Tier 1: 0 ≤ rpd < 1000, discount 0%
    * Tier 2: 1000 ≤ rpd < 5000, discount 10%
    * Tier 3: 5000 ≤ rpd < 10000, discount 20%
    * Tier 4: 10000 ≤ rpd < 20000, discount 30%
    * Tier 5: 20000 ≤ rpd < 30000, discount 40%
    * Tier 6: 30000 ≤ rpd, discount 50%
    > Suppose the base price is 0.001 USD and the number of daily requests is 12000, the calculation
    process is as follows:
    1. **Tier 1** (0 ≤ rpd < 1000):
         - Number of requests in the tier 1 = 1000 - 0 = 1000
         - Discounted unit price in the tier 1 = 0.001 * (1 - 0/100) = 0.001
         - Total cost 1 = 1000 * 0.001 = 1
    2. **Tier 2** (1000 ≤ rpd < 5000):
        - Number of requests in the tier 2 = 5000 - 1000 = 4000
        - Discounted unit price in the tier 2 = 0.001 * (1 - 10/100) = 0.0009
        - Total cost 2 = 4000 * 0.0009 = 3.6
    3. **Tier 3** (5000 ≤ rpd < 10000):
        - Number of requests in the tier 3 = 10000 - 5000 = 5000
        - Discounted unit price in the tier 3 = 0.001 * (1 - 20/100) = 0.0008
        - Total cost 3 = 5000 * 0.0008 = 4
    4. **Tier 4** (10000 ≤ rpd < 20000):
        - Number of requests in the tier 4 = 12000 - 10000 = 2000
        - Discounted unit price in the tier 4 = 0.001 * (1 - 30/100) = 0.0007
        - Total cost 4 = 2000 * 0.0007 = 1.4
    5. **Accumulated total cost**:
        - Total cost = 1 + 3.6 + 4 + 1.4 = 10
    ### Return:
    - Endpoint uri
    - Number of daily requests
    - Original request unit price of the endpoint
    - Total price
    - Currency unit
    - Discount percentage information of tiered billing

    Args:
        endpoint (str): 请求的端点/Requested endpoint
        request_per_day (Union[Unset, int]): 每日请求次数/Request per day Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        endpoint=endpoint,
        request_per_day=request_per_day,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    endpoint: str,
    request_per_day: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """计算价格/Calculate price

     # [中文]
    ### 用途:
    - 根据用户输入的每日请求次数以及端点信息计算最终价格。
    ### 参数:
    - endpoint: 请求的端点，用于查询端点的原始请求单价
    - request_per_day: 每日请求次数，用于计算价格，将自动根据阶梯式计费的折扣百分比计算最终价格
    ### 计算公式:
    - 总成本 = ∑ (阶梯内请求次数 * 阶梯折后单价)
    - 其中，阶梯折后单价 = 基础价格 * (1 - 折扣)
    ### 详细计算步骤:
    1. **初始化总成本**：
       总成本=0
    2. **遍历每个阶梯**：
       * 对于每个阶梯，计算该阶梯内的请求次数。
       * 计算该阶梯内的折后单价。
       * 计算该阶梯内的总费用，并累加到总成本中。
       * 更新剩余的请求次数。
    ### 数学表示:
    > 设有 𝑛 个阶梯，每个阶梯的参数为：
    * min_rpd𝑖: 第 𝑖 个阶梯的最小请求次数
    * max_rpd𝑖: 第 𝑖 个阶梯的最大请求次数
    * discount𝑖: 第 𝑖 个阶梯的折扣（百分比形式）
    * base_price：基础价格
    * request_per_day：每日请求次数
    > 那么，总成本的计算公式如下：
    - 总成本 = Σ𝑖=1𝑛（阶梯𝑖中的请求数量 * 阶梯𝑖中的折扣单价）
    - 其中，阶梯折扣单价 𝑖 = base_price * (1 - 折扣𝑖/100)
    - 该阶梯中的请求数 𝑖 = min(request_per_day - 累计付费请求数, max_rpd𝑖 - min_rpd𝑖)
    ### 示例
    > 假设有以下定价阶梯：
    * 第 1 阶梯：0 ≤ rpd < 1000，折扣 0%
    * 第 2 阶梯：1000 ≤ rpd < 5000，折扣 10%
    * 第 3 阶梯：5000 ≤ rpd < 10000，折扣 20%
    * 第 4 阶梯：10000 ≤ rpd < 20000，折扣 30%
    * 第 5 阶梯：20000 ≤ rpd < 30000，折扣 40%
    * 第 6 阶梯：30000 ≤ rpd，折扣 50%
    > 假设基础价格为 0.001 USD，每日请求次数为 12000，则计算过程如下：
    1. **第 1 阶梯**（0 ≤ rpd < 1000）：
       * 阶梯内请求次数=1000−0=1000
       * 阶梯折后单价=0.001×(1−0/100)=0.001
       * 总成本=1000×0.001=1
    2. **第 2 阶梯**（1000 ≤ rpd < 5000）：
       * 阶梯内请求次数=5000−1000=4000
       * 阶梯折后单价=0.001×(1−10/100)=0.0009
       * 总成本=4000×0.0009=3.6
    3. **第 3 阶梯**（5000 ≤ rpd < 10000）：
       * 阶梯内请求次数=10000−5000=5000
       * 阶梯折后单价=0.001×(1−20/100)=0.0008
       * 总成本=5000×0.0008=4
    4. **第 4 阶梯**（10000 ≤ rpd < 20000）：
       * 阶梯内请求次数=12000−10000=2000
       * 阶梯折后单价=0.001×(1−30/100)=0.0007
       * 总成本=2000×0.0007=1.4
    5. **累加总成本**：
       * 总成本=1+3.6+4+1.4=10
    ### 返回:
    - 端点uri
    - 每日请求次数
    - 端点原始请求单价
    - 总价格
    - 货币单位
    - 阶梯式计费的折扣百分比信息

    # [English]
    ### Purpose:
    - Calculate the final price based on the user's input of the number of daily requests and endpoint
    information.
    - Price calculation formula: Price = Number of daily requests * (Original request unit price of the
    endpoint * (1 - discount percentage of tiered billing))
    ### Parameters:
    - endpoint: Requested endpoint, used to query the original request unit price of the endpoint
    - request_per_day: Number of daily requests, used to calculate the price, the final price will be
    calculated automatically based on the discount percentage of the tiered billing
    ### Calculation formula:
    - Total cost = ∑ (Number of requests in the tier * Discounted unit price in the tier)
    - Where, Discounted unit price in the tier = Base price * (1 - Discount)
    ### Detailed calculation steps:
    1. **Initialize the total cost**:
         Total cost = 0
    2. **Traverse each tier**:
            * For each tier, calculate the number of requests in the tier.
            * Calculate the discounted unit price in the tier.
            * Calculate the total cost in the tier and add it to the total cost.
            * Update the remaining number of requests.
    ### Mathematical representation:
    Suppose there are 𝑛 tiers, and the parameters of each tier are:
    * min_rpd𝑖: The minimum number of requests in the 𝑖-th tier
    * max_rpd𝑖: The maximum number of requests in the 𝑖-th tier
    * discount𝑖: The discount of the 𝑖-th tier (in percentage form)
    * base_price: Base price
    * request_per_day: Number of daily requests
    > Then, the formula for calculating the total cost is as follows:
    - Total cost = ∑𝑖=1𝑛(Number of requests in the tier 𝑖 * Discounted unit price in the tier 𝑖)
    - Where, Discounted unit price in the tier 𝑖 = base_price * (1 - discount𝑖/100)
    - Number of requests in the tier 𝑖 = min(request_per_day - accumulated number of paid requests,
    max_rpd𝑖 - min_rpd𝑖)
    ### Example
    Suppose there are the following pricing tiers:
    * Tier 1: 0 ≤ rpd < 1000, discount 0%
    * Tier 2: 1000 ≤ rpd < 5000, discount 10%
    * Tier 3: 5000 ≤ rpd < 10000, discount 20%
    * Tier 4: 10000 ≤ rpd < 20000, discount 30%
    * Tier 5: 20000 ≤ rpd < 30000, discount 40%
    * Tier 6: 30000 ≤ rpd, discount 50%
    > Suppose the base price is 0.001 USD and the number of daily requests is 12000, the calculation
    process is as follows:
    1. **Tier 1** (0 ≤ rpd < 1000):
         - Number of requests in the tier 1 = 1000 - 0 = 1000
         - Discounted unit price in the tier 1 = 0.001 * (1 - 0/100) = 0.001
         - Total cost 1 = 1000 * 0.001 = 1
    2. **Tier 2** (1000 ≤ rpd < 5000):
        - Number of requests in the tier 2 = 5000 - 1000 = 4000
        - Discounted unit price in the tier 2 = 0.001 * (1 - 10/100) = 0.0009
        - Total cost 2 = 4000 * 0.0009 = 3.6
    3. **Tier 3** (5000 ≤ rpd < 10000):
        - Number of requests in the tier 3 = 10000 - 5000 = 5000
        - Discounted unit price in the tier 3 = 0.001 * (1 - 20/100) = 0.0008
        - Total cost 3 = 5000 * 0.0008 = 4
    4. **Tier 4** (10000 ≤ rpd < 20000):
        - Number of requests in the tier 4 = 12000 - 10000 = 2000
        - Discounted unit price in the tier 4 = 0.001 * (1 - 30/100) = 0.0007
        - Total cost 4 = 2000 * 0.0007 = 1.4
    5. **Accumulated total cost**:
        - Total cost = 1 + 3.6 + 4 + 1.4 = 10
    ### Return:
    - Endpoint uri
    - Number of daily requests
    - Original request unit price of the endpoint
    - Total price
    - Currency unit
    - Discount percentage information of tiered billing

    Args:
        endpoint (str): 请求的端点/Requested endpoint
        request_per_day (Union[Unset, int]): 每日请求次数/Request per day Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
        request_per_day=request_per_day,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    endpoint: str,
    request_per_day: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """计算价格/Calculate price

     # [中文]
    ### 用途:
    - 根据用户输入的每日请求次数以及端点信息计算最终价格。
    ### 参数:
    - endpoint: 请求的端点，用于查询端点的原始请求单价
    - request_per_day: 每日请求次数，用于计算价格，将自动根据阶梯式计费的折扣百分比计算最终价格
    ### 计算公式:
    - 总成本 = ∑ (阶梯内请求次数 * 阶梯折后单价)
    - 其中，阶梯折后单价 = 基础价格 * (1 - 折扣)
    ### 详细计算步骤:
    1. **初始化总成本**：
       总成本=0
    2. **遍历每个阶梯**：
       * 对于每个阶梯，计算该阶梯内的请求次数。
       * 计算该阶梯内的折后单价。
       * 计算该阶梯内的总费用，并累加到总成本中。
       * 更新剩余的请求次数。
    ### 数学表示:
    > 设有 𝑛 个阶梯，每个阶梯的参数为：
    * min_rpd𝑖: 第 𝑖 个阶梯的最小请求次数
    * max_rpd𝑖: 第 𝑖 个阶梯的最大请求次数
    * discount𝑖: 第 𝑖 个阶梯的折扣（百分比形式）
    * base_price：基础价格
    * request_per_day：每日请求次数
    > 那么，总成本的计算公式如下：
    - 总成本 = Σ𝑖=1𝑛（阶梯𝑖中的请求数量 * 阶梯𝑖中的折扣单价）
    - 其中，阶梯折扣单价 𝑖 = base_price * (1 - 折扣𝑖/100)
    - 该阶梯中的请求数 𝑖 = min(request_per_day - 累计付费请求数, max_rpd𝑖 - min_rpd𝑖)
    ### 示例
    > 假设有以下定价阶梯：
    * 第 1 阶梯：0 ≤ rpd < 1000，折扣 0%
    * 第 2 阶梯：1000 ≤ rpd < 5000，折扣 10%
    * 第 3 阶梯：5000 ≤ rpd < 10000，折扣 20%
    * 第 4 阶梯：10000 ≤ rpd < 20000，折扣 30%
    * 第 5 阶梯：20000 ≤ rpd < 30000，折扣 40%
    * 第 6 阶梯：30000 ≤ rpd，折扣 50%
    > 假设基础价格为 0.001 USD，每日请求次数为 12000，则计算过程如下：
    1. **第 1 阶梯**（0 ≤ rpd < 1000）：
       * 阶梯内请求次数=1000−0=1000
       * 阶梯折后单价=0.001×(1−0/100)=0.001
       * 总成本=1000×0.001=1
    2. **第 2 阶梯**（1000 ≤ rpd < 5000）：
       * 阶梯内请求次数=5000−1000=4000
       * 阶梯折后单价=0.001×(1−10/100)=0.0009
       * 总成本=4000×0.0009=3.6
    3. **第 3 阶梯**（5000 ≤ rpd < 10000）：
       * 阶梯内请求次数=10000−5000=5000
       * 阶梯折后单价=0.001×(1−20/100)=0.0008
       * 总成本=5000×0.0008=4
    4. **第 4 阶梯**（10000 ≤ rpd < 20000）：
       * 阶梯内请求次数=12000−10000=2000
       * 阶梯折后单价=0.001×(1−30/100)=0.0007
       * 总成本=2000×0.0007=1.4
    5. **累加总成本**：
       * 总成本=1+3.6+4+1.4=10
    ### 返回:
    - 端点uri
    - 每日请求次数
    - 端点原始请求单价
    - 总价格
    - 货币单位
    - 阶梯式计费的折扣百分比信息

    # [English]
    ### Purpose:
    - Calculate the final price based on the user's input of the number of daily requests and endpoint
    information.
    - Price calculation formula: Price = Number of daily requests * (Original request unit price of the
    endpoint * (1 - discount percentage of tiered billing))
    ### Parameters:
    - endpoint: Requested endpoint, used to query the original request unit price of the endpoint
    - request_per_day: Number of daily requests, used to calculate the price, the final price will be
    calculated automatically based on the discount percentage of the tiered billing
    ### Calculation formula:
    - Total cost = ∑ (Number of requests in the tier * Discounted unit price in the tier)
    - Where, Discounted unit price in the tier = Base price * (1 - Discount)
    ### Detailed calculation steps:
    1. **Initialize the total cost**:
         Total cost = 0
    2. **Traverse each tier**:
            * For each tier, calculate the number of requests in the tier.
            * Calculate the discounted unit price in the tier.
            * Calculate the total cost in the tier and add it to the total cost.
            * Update the remaining number of requests.
    ### Mathematical representation:
    Suppose there are 𝑛 tiers, and the parameters of each tier are:
    * min_rpd𝑖: The minimum number of requests in the 𝑖-th tier
    * max_rpd𝑖: The maximum number of requests in the 𝑖-th tier
    * discount𝑖: The discount of the 𝑖-th tier (in percentage form)
    * base_price: Base price
    * request_per_day: Number of daily requests
    > Then, the formula for calculating the total cost is as follows:
    - Total cost = ∑𝑖=1𝑛(Number of requests in the tier 𝑖 * Discounted unit price in the tier 𝑖)
    - Where, Discounted unit price in the tier 𝑖 = base_price * (1 - discount𝑖/100)
    - Number of requests in the tier 𝑖 = min(request_per_day - accumulated number of paid requests,
    max_rpd𝑖 - min_rpd𝑖)
    ### Example
    Suppose there are the following pricing tiers:
    * Tier 1: 0 ≤ rpd < 1000, discount 0%
    * Tier 2: 1000 ≤ rpd < 5000, discount 10%
    * Tier 3: 5000 ≤ rpd < 10000, discount 20%
    * Tier 4: 10000 ≤ rpd < 20000, discount 30%
    * Tier 5: 20000 ≤ rpd < 30000, discount 40%
    * Tier 6: 30000 ≤ rpd, discount 50%
    > Suppose the base price is 0.001 USD and the number of daily requests is 12000, the calculation
    process is as follows:
    1. **Tier 1** (0 ≤ rpd < 1000):
         - Number of requests in the tier 1 = 1000 - 0 = 1000
         - Discounted unit price in the tier 1 = 0.001 * (1 - 0/100) = 0.001
         - Total cost 1 = 1000 * 0.001 = 1
    2. **Tier 2** (1000 ≤ rpd < 5000):
        - Number of requests in the tier 2 = 5000 - 1000 = 4000
        - Discounted unit price in the tier 2 = 0.001 * (1 - 10/100) = 0.0009
        - Total cost 2 = 4000 * 0.0009 = 3.6
    3. **Tier 3** (5000 ≤ rpd < 10000):
        - Number of requests in the tier 3 = 10000 - 5000 = 5000
        - Discounted unit price in the tier 3 = 0.001 * (1 - 20/100) = 0.0008
        - Total cost 3 = 5000 * 0.0008 = 4
    4. **Tier 4** (10000 ≤ rpd < 20000):
        - Number of requests in the tier 4 = 12000 - 10000 = 2000
        - Discounted unit price in the tier 4 = 0.001 * (1 - 30/100) = 0.0007
        - Total cost 4 = 2000 * 0.0007 = 1.4
    5. **Accumulated total cost**:
        - Total cost = 1 + 3.6 + 4 + 1.4 = 10
    ### Return:
    - Endpoint uri
    - Number of daily requests
    - Original request unit price of the endpoint
    - Total price
    - Currency unit
    - Discount percentage information of tiered billing

    Args:
        endpoint (str): 请求的端点/Requested endpoint
        request_per_day (Union[Unset, int]): 每日请求次数/Request per day Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            endpoint=endpoint,
            request_per_day=request_per_day,
        )
    ).parsed
