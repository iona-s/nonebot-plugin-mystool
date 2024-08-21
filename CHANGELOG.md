## Changelog

### 更新内容

#### 💡 新特性
- 米游币任务 — 讨论区签到 的人机验证增加更多的日志输出
- 群聊中使用时构建合并的消息/聊天记录再进行推送 (#353) - by @dontdot
- 实时便笺根据可签到的游戏进行自动推送 (#352) - by @dontdot

#### 🐛 修复
- 修复二维码登录提示已过期的问题 (#357) - by @tym2008
- 修复二维码登录相关的部分反馈文本没有发送的问题 (#357)
- 修复QQ频道私聊不响应的问题 (#356) - by @dontdot
- 修复手动触发米游社任务时，消息列表为空导致任务中断的问题 (#354) - by @dontdot
- 修复截取微博超话id的正则公式错误 (#352) - by @dontdot
- 修复当用户不填写偏好设置 `geetest_params` 时报错的问题 (#352) - by @dontdot

[//]: # (#### 🔧 杂项)

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

- V2 (`>=v2.0.0`) 的相关文件为 _`configV2.json`, `dataV2.json`, `.env`_，如果存在 V1 版本的文件，**会自动备份和升级**
- V1 (`>=v1.0.0, <v2.0.0`) 插件配置/数据文件为 _`plugin_data.json`_
- `<v1.0.0` 插件配置文件为 _`pluginConfig.json`_

**Full Changelog**: https://github.com/Ljzd-PRO/nonebot-plugin-mystool/compare/v2.7.0…v2.8.0