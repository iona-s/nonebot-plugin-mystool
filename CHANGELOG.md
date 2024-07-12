## Changelog

### 更新内容

#### 💡 新特性

- 新增绝区零微博超话兑换 - by @Joseandluue
- 增加微博超话相关参数设置错误提示 - by @Joseandluue
- 调整微博设置功能：补充删除账号 - by @Joseandluue
- 优化多个微博超话有兑换码的消息推送 - by @Joseandluue
- 优化微博签到出错推送 - by @Joseandluue

- 原神体力上限修改 (#308) - by @Joseandluue
- 增加绝区零游戏签到支持 (#332) - by @Yinhaoran1128

#### 🐛 修复
- 修复微博超话签到结果判断逻辑错误 - by @Joseandluue
- 因微博超话签到触发人机验证，每日签到改为检测到超话存在可兑换礼包时才会进行签到 - by @Joseandluue
- 修复微博超话自动签到开关功能缺失 (#327) - by @Joseandluue
- 微博超话签到验证对自动签到进行调整 - by @Joseandluue
- 对于 OneBot 协议，推送米游币任务结果时不再配上图片，以修复米游币任务中途出错导致提前结束的问题 (#323, #309)
- 修复添加兑换计划后的兑换时间错误 (#330)

#### 🔧 杂项
- 微博超话签到设置注释补充参数 `c` 为必填（找不到超话列表） (#318, #294) - by @Joseandluue

### 更新方式

如果使用的是镜像源，可能需要等待镜像源同步才能更新至最新版

- 使用 nb-cli 命令：
  ```
  nb plugin update nonebot-plugin-mystool
  ```

- 或 pip 命令（如果使用了虚拟环境，需要先进入虚拟环境）：
  ```
  pip install --upgrade nonebot-plugin-mystool
  ```

### 兼容性

- `>=v2.0.0` 为 `configV2.json`, `dataV2.json`, `.env` 文件，如果存在 V1 版本的文件，**会自动备份和升级**
- `>=v1.0.0, <v2.0.0` 插件配置/数据包含于 `plugin_data.json`
- `< v1.0.0` 插件配置文件为 `pluginConfig.json`

**Full Changelog**: https://github.com/Ljzd-PRO/nonebot-plugin-mystool/compare/v2.5.0…v2.6.0