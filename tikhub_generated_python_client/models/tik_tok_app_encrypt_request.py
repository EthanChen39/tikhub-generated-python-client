from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tik_tok_app_encrypt_request_device_info import TikTokAPPEncryptRequestDeviceInfo


T = TypeVar("T", bound="TikTokAPPEncryptRequest")


@_attrs_define
class TikTokAPPEncryptRequest:
    """
    Attributes:
        url (Union[Unset, str]): 需要加密的URL/URL to be encrypted Default: 'https://api16-normal-useast5.tiktokv.us/tiktok/v
            1/upvote/item/list?user_id=6726034365602628610&offset=0&count=21&scene=0&iid=7425045478163400491&device_id=73497
            21034012280362&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360704&version_name=36.7.4&d
            evice_platform=android&os=android&ab_version=36.7.4&ssmix=a&device_type=Pixel+6+Pro&device_brand=google&language
            =zh&os_api=33&os_version=13&openudid=711192517a8bbf03&manifest_version_code=2023607040&resolution=1440*2891&dpi=
            560&update_version_code=2023607040&_rticket=1728977220468&is_pad=0&app_type=normal&sys_region=CN&last_install_ti
            me=1728977141&timezone_name=America%2FLos_Angeles&app_language=zh-
            Hans&ac2=wifi5g&uoo=0&op_region=CN&timezone_offset=-28800&build_number=36.7.4&host_abi=arm64-v8a&locale=zh-
            Hans&region=CN&content_language=en%2C&ts=1728977220&cdid=aa21524b-8633-49ca-8e6e-3275fe1672db'.
        data (Union[Unset, str]): 如果有POST请求，请填写POST请求的数据参与加密计算/If there is a POST request, please fill in the data of
            the POST request to participate in the encryption calculation Default: ''.
        device_info (Union[Unset, TikTokAPPEncryptRequestDeviceInfo]): 设备信息，可选参数，如果不填写则使用默认设备信息/Device information,
            optional parameter, if not filled in, the default device information is used
    """

    url: Union[Unset, str] = (
        "https://api16-normal-useast5.tiktokv.us/tiktok/v1/upvote/item/list?user_id=6726034365602628610&offset=0&count=21&scene=0&iid=7425045478163400491&device_id=7349721034012280362&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=360704&version_name=36.7.4&device_platform=android&os=android&ab_version=36.7.4&ssmix=a&device_type=Pixel+6+Pro&device_brand=google&language=zh&os_api=33&os_version=13&openudid=711192517a8bbf03&manifest_version_code=2023607040&resolution=1440*2891&dpi=560&update_version_code=2023607040&_rticket=1728977220468&is_pad=0&app_type=normal&sys_region=CN&last_install_time=1728977141&timezone_name=America%2FLos_Angeles&app_language=zh-Hans&ac2=wifi5g&uoo=0&op_region=CN&timezone_offset=-28800&build_number=36.7.4&host_abi=arm64-v8a&locale=zh-Hans&region=CN&content_language=en%2C&ts=1728977220&cdid=aa21524b-8633-49ca-8e6e-3275fe1672db"
    )
    data: Union[Unset, str] = ""
    device_info: Union[Unset, "TikTokAPPEncryptRequestDeviceInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        data = self.data

        device_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.device_info, Unset):
            device_info = self.device_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if data is not UNSET:
            field_dict["data"] = data
        if device_info is not UNSET:
            field_dict["device_info"] = device_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tik_tok_app_encrypt_request_device_info import TikTokAPPEncryptRequestDeviceInfo

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        data = d.pop("data", UNSET)

        _device_info = d.pop("device_info", UNSET)
        device_info: Union[Unset, TikTokAPPEncryptRequestDeviceInfo]
        if isinstance(_device_info, Unset):
            device_info = UNSET
        else:
            device_info = TikTokAPPEncryptRequestDeviceInfo.from_dict(_device_info)

        tik_tok_app_encrypt_request = cls(
            url=url,
            data=data,
            device_info=device_info,
        )

        tik_tok_app_encrypt_request.additional_properties = d
        return tik_tok_app_encrypt_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
