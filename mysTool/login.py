from nonebot import on_command
from nonebot.adapters.onebot.v11 import PrivateMessageEvent
from nonebot.params import T_State, ArgPlainText
import requests.utils
import httpx
from .config import mysTool_config as conf
from .utils import *
from .data import UserData

URL_1 = "https://webapi.account.mihoyo.com/Api/login_by_mobilecaptcha"
URL_2 = "https://api-takumi.mihoyo.com/auth/api/getMultiTokenByLoginTicket?login_ticket={loginTicket}&token_types=3&uid={bbsUID}"
HEADERS_1 = {
    "Host": "webapi.account.mihoyo.com",
    "Connection": "keep-alive",
    "sec-ch-ua": conf.device.UA,
    "DNT": "1",
    "x-rpc-device_model": conf.device.X_RPC_DEVICE_MODEL_PC,
    "sec-ch-ua-mobile": "?0",
    "User-Agent": conf.device.USER_AGENT_PC,
    "x-rpc-device_id": None,
    "Accept": "application/json, text/plain, */*",
    "x-rpc-device_name": conf.device.X_RPC_DEVICE_NAME_PC,
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-rpc-client_type": "4",
    "sec-ch-ua-platform": conf.device.UA_PLATFORM,
    "Origin": "https://user.mihoyo.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://user.mihoyo.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}
HEADERS_2 = {
    "Host": "api-takumi.mihoyo.com",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": "https://bbs.mihoyo.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": conf.device.USER_AGENT_PC,
    "Referer": "https://bbs.mihoyo.com/",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9"
}


class GetCookie:
    def __init__(self, qq: int, phone: int) -> None:
        self.phone = phone
        self.bbsUID: str = None
        self.cookie: dict = None
        self.client = httpx.AsyncClient()
        account = UserData.read_account(qq, phone)
        if account is None:
            self.deviceID = generateDeviceID()
        else:
            self.deviceID = account.deviceID

    async def get_1(self, captcha: str):
        headers = HEADERS_1.copy()
        headers["x-rpc-device_id"] = self.deviceID
        res = await self.client.post(URL_1, headers=headers, data="mobile={0}&mobile_captcha={1}&source=user.mihoyo.com".format(self.phone, captcha))
        if "login_ticket" not in res.cookies:
            return 0

        for item in ("login_uid", "stuid", "ltuid", "account_id"):
            if item in res.cookies:
                self.bbsUID = res.cookies[item]
                break
        if not self.bbsUID:
            return -1

        return True

    async def get_2(self, captcha: str):
        res = await self.client.post(URL_2, headers=HEADERS_2, json={
            "is_bh2": False,
            "mobile": self.phone,
            "captcha": captcha,
            "action_type": "login",
            "token_type": 6
        })
        if "cookie_token" not in res.cookies:
            return False
        await self.client.aclose()
        self.cookie = requests.utils.dict_from_cookiejar(res.cookies.jar)
        return True

    async def __del__(self):
        await self.client.aclose()


get_cookie = on_command(
    'cookie', aliases={'cookie填写', 'cookie'}, priority=4, block=True)
get_cookie.__help__ = {
    "usage":     "get_cookie",
    "introduce": "通过电话获取验证码方式获取cookie"
}


@get_cookie.handle()
async def handle_first_receive(event: PrivateMessageEvent, state: T_State):
    await get_cookie.send('获取cookie过程分为三步：\n1.发送手机号\n2.登录https://user.mihoyo.com/#/login/captcha，输入手机号并获取验证码并发送\n3.刷新页面，再次获取验证码并发送\n过程中随时输入退出即可退出')


@get_cookie.got('手机号', prompt='请输入您的手机号')
async def _(event: PrivateMessageEvent, state: T_State, phone: str = ArgPlainText('手机号')):
    if phone == '退出':
        await get_cookie.finish("已成功退出")
    try:
        phone_num = int(phone)
    except:
        await get_cookie.reject("手机号应为11位数字，请重新输入")
    if len(phone) != 11:
        await get_cookie.reject("手机号应为11位数字，请重新输入")
    else:
        state['phone'] = phone_num
        state['getCookie'] = GetCookie(event.user_id, phone_num)


@get_cookie.handle()
async def _(event: PrivateMessageEvent, state: T_State):
    await get_cookie.send('登录https://user.mihoyo.com/#/login/captcha，输入手机号并获取验证码并发送（不要登录！）')


@get_cookie.got("验证码1", prompt='请输入验证码')
async def _(event: PrivateMessageEvent, state: T_State, captcha1: str = ArgPlainText('验证码1')):
    if captcha1 == '退出':
        await get_cookie.finish("已成功退出")
    try:
        int(captcha1)
    except:
        await get_cookie.reject("验证码应为6位数字，请重新输入")
    if len(captcha1) != 6:
        await get_cookie.reject("验证码应为6位数字，请重新输入")
    else:
        status: int = state['getCookie'].get_1(captcha1)
        if status == 0:
            await get_cookie.finish("由于Cookie缺少login_ticket，无法继续，请稍后再试")
        elif status == -1:
            await get_cookie.finish("由于Cookie缺少uid，无法继续，请稍后再试")


@get_cookie.handle()
async def _(event: PrivateMessageEvent, state: T_State):
    await get_cookie.send('请刷新浏览器，再次输入手机号，获取验证码并发送（不要登录！）')


@get_cookie.got('验证码2', prompt='请输入验证码')
async def _(event: PrivateMessageEvent, state: T_State, captcha2: str = ArgPlainText('验证码2')):
    if captcha2 == '退出':
        await get_cookie.finish("已成功退出")
    try:
        int(captcha2)
    except:
        await get_cookie.reject("验证码应为6位数字，请重新输入")
    if len(captcha2) != 6:
        await get_cookie.reject("验证码应为6位数字，请重新输入")
    else:
        status: bool = state["getCookie"].get_2(captcha2)
        if not status:
            await get_cookie.finish("获取stoken失败，一种可能是登录失效，请稍后再试")

    UserData.set_cookie(state['getCookie'].cookie,
                        event.user_id, state['phone'])
    await get_cookie.finish("Cookie获取成功")