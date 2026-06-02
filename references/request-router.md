# Request Router

Use this reference when the user gives a short Chinese request, asks for a rewrite, requests a prompt pack, or names a model/platform. Route first; then write the prompt with `prompt-framework.md`.

## Intent Routing

| User intent | Output mode | What to load |
|---|---|---|
| "写提示词", "优化提示词", "扩写", "改得高级" | single prompt | `prompt-framework.md`, route reference, quality control |
| "来一组", "10个", "批量", "关键词包" | prompt pack | route reference, `eastern-fantasy-series.md` |
| "做系列", "人物设定", "世界观", "IP" | series bible + lineup | `eastern-fantasy-series.md`, route reference |
| "太普通", "没亮点", "不够惊艳", "高级感不够" | rewrite with stronger wow device | `wow-factor-system.md`, `quality-control.md` |
| "脸不好看", "气质", "体态", "纯欲", "私房" | character-focused rewrite | `character-subject-system.md`, safety notes |
| "小程序", "标签", "参数块", "表单字段" | modular fields | `prompt-framework.md`, relevant mini-program tags |
| "MJ", "Midjourney", "SD", "ComfyUI", "DALL-E", "GPT image", "Seedream" | model-specific prompt | `prompt-framework.md` model adaptation |

## Chinese Trigger Phrase Map

| Phrase | Likely route | Notes |
|---|---|---|
| 星象, 观星, 命盘, 天命, 神官 | `celestial-empire` | Add astronomical instruments, not just stars. |
| 雪山, 昆仑, 剑姬, 清冷, 守桥 | `kunlun-snow-sword` | Keep sword action functional and restrained. |
| 敦煌, 飞天, 壁画, 矿物色, 沙漠 | `dunhuang-mural-oracle` | Avoid belly-dance clichés; use mural and grotto logic. |
| 龙女, 海潮, 珍珠, 水下, 琉璃 | `tide-dragon-court` | Keep hanfu-derived silhouette; no mermaid tail unless requested. |
| 莲灯, 梦境, 镇邪, 符箓, 镜湖 | `lotus-dream-exorcist` | Lyrical supernatural tension, not gore horror. |
| 凤凰, 宫廷, 女王, 红金, 火焰 | `phoenix-palace-fire` | Control red/gold density; use one dominant phoenix shape. |
| 月宫, 桂树, 炼丹, 银炉, 月镜 | `moon-palace-alchemy` | Combine cold lunar divinity with warm alchemy light. |
| 青铜, 甲骨, 古城, 祭司, 预言 | `bronze-oracle-city` | Make it epic and archaeological; avoid steampunk. |
| 浴后, 湿发, 私房, 纯欲, 水汽 | `mist-bath-boudoir` | Keep adult, covered, opaque, and non-voyeuristic. |

If multiple phrases appear, choose the user's strongest noun as the primary route and treat the others as accents only when compatible.

## Rewrite Moves

When improving an existing prompt:

1. Preserve all explicit nouns, ratio, platform, and "must avoid" constraints.
2. Identify the current weak point: route ambiguity, bland role, idle pose, generic background, missing wow device, unsafe sensual framing, or model mismatch.
3. Rewrite around one stronger visual event before adding ornament.
4. Return a concise "改动重点" before the new prompt only when useful.

## Output Length Defaults

- Short user request: one strong complete prompt plus negative prompt.
- Professional prompt request: parameter lock, director setting, module analysis, Chinese prompt, English prompt, negative prompt, parameter suggestions.
- Prompt pack: compact table; keep each prompt copyable.
- Series: series bible, lineup table, shared negative prompt.
