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
| "东方美人", "东方审美", "柔美", "妩媚", "成熟", "优雅", "高贵", "清冷", "温婉", "英气", "神性", "慵懒" | aesthetic-led Eastern beauty prompt | `styles/东方美人审美系统.md`, then route reference |
| "SweetHomeGirl", "甜系纯欲生活写真", "甜系纯欲", "甜美女友感", "真实女生", "自然抓拍", "故事感", "女友视角", "girlfriend portrait" | 甜系纯欲生活写真 realistic pure-desire lifestyle prompt | `styles/甜系纯欲生活写真.md`, `prompt-framework.md`, `quality-control.md` |
| "古典东方美人", "宋韵", "唐宫", "江南", "洛神", "青瓷", "昆曲", "仕女" | classical Eastern beauty prompt | `styles/东方美人审美系统.md`, `styles/古典东方美人.md`, `prompt-framework.md` |
| "写实", "现代", "摄影", "杂志", "新中式", "东方高级感", "旗袍电影感", "东方静奢", "珠宝大片", "茶室光影", "都市晚宴" | realistic / modern Eastern beauty prompt | `styles/东方美人审美系统.md`, `styles/现代东方美人.md`, `prompt-framework.md`, `character-subject-system.md` |
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
| 绮罗, 金帐, 红金寝殿, 纱幔, 珠饰, 香雾, 烛火秘仪 | `red-gold-luo-curtain` | Use ornate red-gold palace intimacy; avoid fetish framing, transparent revealing fabric, and extreme poses. |
| 月宫, 桂树, 炼丹, 银炉, 月镜 | `moon-palace-alchemy` | Combine cold lunar divinity with warm alchemy light. |
| 青铜, 甲骨, 古城, 祭司, 预言 | `bronze-oracle-city` | Make it epic and archaeological; avoid steampunk. |
| 浴后, 湿发, 私房, 纯欲, 水汽 | `mist-bath-boudoir` | Keep adult, covered, opaque, and non-voyeuristic. |

## Aesthetic-Led Eastern Beauty

When the user asks for 东方美人, 东方审美, 美人风格, 柔美, 妩媚, 成熟, 优雅, 高贵, 清冷, 温婉, 英气, 神性, or 慵懒:

1. Load `styles/东方美人审美系统.md`.
2. Choose one dominant aesthetic and at most one secondary accent.
3. Then choose the correct route family:
   - fantasy / mythic / 仙侠 / 神女 / 龙女 / 宫廷奇观 -> `styles/东方幻想古风.md`
   - classical / 宋韵 / 唐宫 / 江南 / 洛神 / 青瓷 / 昆曲 / 仕女 -> `styles/古典东方美人.md`
   - realistic / modern / magazine / new-Chinese / qipao / jewelry / tea room / city evening -> `styles/现代东方美人.md`
   - girlfriend / lifestyle / SweetHomeGirl / 真实女生 / 故事感 -> `styles/甜系纯欲生活写真.md`
4. Let the aesthetic system shape gaze, posture, hand gesture, fabric behavior, light, and composition before adding route-specific props.
5. If the user says 妩媚, mature allure must come from gaze, posture, fabric, candlelight, jewelry, and controlled expression, not exposure.

## Classical Eastern Beauty

When the user asks for 古典东方美人, 古典美人, 宋韵, 唐宫, 江南, 洛神, 青瓷, 昆曲, 仕女, 闺阁, or a classical but non-fantasy beauty image:

1. Load `styles/东方美人审美系统.md` and `styles/古典东方美人.md`.
2. Choose one classical route and one dominant aesthetic.
3. Do not force mythic artifacts, impossible scale, or battle spectacle unless the user asks for fantasy.
4. Focus on line, gesture, fabric, light, face temperament, and spatial poetry.

## SweetHomeGirl Routing

When the user asks for SweetHomeGirl, 甜系纯欲生活写真, 甜系纯欲, 甜美女友感, 真实女生, 自然抓拍, 故事感, 女友视角, lifestyle girlfriend portrait, private-room portrait, or home fashion shoot:

1. Load `styles/甜系纯欲生活写真.md`.
2. Apply the 甜系纯欲生活写真 priority exactly: body system, story moment, pure-desire, face, outfit, composition, scene.
3. Treat the core formula as realism + feminine charm + romantic feeling + story moment + natural pure-desire.
4. Build story first, action second, expression last.
5. Do not lock one fixed face. Vary face style while preserving body system, realism, natural attraction, adult age impression, high attractiveness, and approachability.
6. Never let face style, clothing, action, scene, props, camera, or composition override the body system hard lock.
7. If the user provides the Chinese structured format (`技能 / 人脸风格 / 场景 / 穿搭 / 故事瞬间 / 构图 / 天气 / 时间 / 镜头要求`), preserve those field names in the parameter lock.
8. Prefer one-line `穿搭` input. Preserve structured outfit subfields only when the user explicitly provides `穿搭细节 / 上装 / 下装 / 鞋袜 / 配饰`.
9. Use the user's selected face style, scene, outfit direction, story moment, composition, weather, time, and camera requirements when provided.
10. If composition is only an aspect ratio such as `9比16`, choose a real framing mode from the composition system and label it as a supplement.
11. If weather, time, light, palette, atmosphere, or lens is missing, infer a tasteful default from scene plus story and label it as a supplement.
12. Return a complete prompt and checklist first; generate an image only when the user explicitly asks to generate directly or confirms.

## Realistic and Modern Eastern Beauty

When the user asks for 写实, 现代, 摄影, 杂志, 新中式, 东方高级感, fashion editorial, beauty campaign, or realistic portrait:

1. Do not force hanfu, mythology, magical artifacts, or wonder-scale environments.
2. Load `styles/现代东方美人.md` and choose one modern style route from that file.
3. Prioritize facial temperament, styling, garment silhouette, fabric, posture, lens, light, background, and tasteful Eastern aesthetic cues.
4. Keep the subject adult, dignified, and non-sexualized.
5. Use gu feng or Eastern fantasy routes only when the user also asks for 古风, 仙侠, 神话, 国风角色, or a fantasy setting.
6. Add a brief note that current skill coverage is strongest for gu feng / Eastern fantasy only if the user expects a fully developed modern-realistic system.

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
