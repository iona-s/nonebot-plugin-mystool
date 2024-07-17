## Changelog

### 更新内容

#### 💡 新特性
- 支持指定要进行签到的游戏（游戏签到）(#291) - by @Joseandluue
  - 通过 `/账号设置` 命令更改游戏签到限定范围

#### 🐛 修复
- 修复体力阈值设置需要发送两次的问题 (#342) - by @Joseandluue
- 修复米游币任务讨论区签到在人机验证成功后签到失败的问题 (#323, #309)
- 撤销上个版本兑换时间的相关变更，以修复错误的兑换时间 (#341, #342)

#### 🔧 杂项
- 撤销上个版本 OneBot 协议推送米游币任务结果时不配上图片的变更

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

**Full Changelog**: https://github.com/Ljzd-PRO/nonebot-plugin-mystool/compare/v2.6.0…v2.7.0