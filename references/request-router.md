# Request Router

Use this reference when the user gives a short Chinese request, asks for a rewrite, requests a prompt pack, or names a model/platform. Route first; then write the prompt with `prompt-framework.md`.

Before creating or implying a new route family, check `style-taxonomy.md`. If the request fits an existing canonical family, extend that family with a new route or scene rather than creating a duplicate template.

## Intent Routing

| User intent | Output mode | What to load |
|---|---|---|
| "写提示词", "优化提示词", "扩写", "改得高级" | single prompt | `prompt-framework.md`, route reference, quality control |
| Chinese parameter block with fields such as `技能 / 风格 / 气质 / 场景 / 服装 / 动作 / 构图 / 生成` | structured call | `structured-call-format.md`, route reference, quality control |
| "来一组", "10个", "批量", "关键词包" | prompt pack | route reference, `eastern-fantasy-series.md` |
| "做系列", "人物设定", "世界观", "IP" | series bible + lineup | `eastern-fantasy-series.md`, route reference |
| "太普通", "没亮点", "不够惊艳", "高级感不够" | rewrite with stronger wow device | `wow-factor-system.md`, `quality-control.md` |
| "脸不好看", "气质", "体态", "纯欲", "私房" | character-focused rewrite | `character-subject-system.md`, safety notes |
| "东方美人", "东方审美", "柔美", "妩媚", "成熟", "优雅", "高贵", "清冷", "温婉", "英气", "神性", "慵懒" | aesthetic-led Eastern beauty prompt | `styles/东方美人审美系统.md`, then route reference |
| "东方美学图鉴", "图鉴封面", "图鉴正文", "小红书图鉴", "四大美人", "四大才女", "十二花神", "二十四节气", "东方神女", "敦煌飞天", "朝代服饰", "历史人物", "东方器物", "东方神话", "东方文化专题" | Eastern aesthetic atlas cover/content system | `styles/东方美学图鉴.md`, `prompt-framework.md`, `quality-control.md` |
| "SweetHomeGirl", "甜系纯欲生活写真", "甜系纯欲", "甜美女友感", "真实女生", "自然抓拍", "故事感", "女友视角", "girlfriend portrait" | 甜系纯欲生活写真 realistic pure-desire lifestyle prompt | `styles/甜系纯欲生活写真.md`, `prompt-framework.md`, `quality-control.md` |
| "古风闺蜜", "闺阁夜话", "姐妹古风写真", "古代闺阁生活", "灯下梳发", "共读", "夏夜纳凉", "守夜", "双人古风真人摄影", "AncientFemaleCompanionship", "Ancient Female Companionship" | 古风闺蜜 / ancient Chinese female companionship photography | `styles/古风闺蜜.md`, `prompt-framework.md`, `quality-control.md` |
| "Cosplay展会摄影", "coser", "Coser", "漫展摄影", "展会摄影", "ChinaJoy", "Bilibili World", "BW", "Tokyo Game Show", "TGS", "游戏展台", "官方展会摄影", "AAA游戏角色Cosplay" | Cosplay convention photography / official game booth portrait | `styles/Cosplay展会摄影.md`, `prompt-framework.md`, `quality-control.md` |
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
| 闺阁, 夜话, 梳发, 共读, 纳凉, 守夜, 姐妹, 闺蜜, 同行, 知己, 江南同行, 湖亭共伞 | `ancient-female-companionship` | Keep ancient Chinese lifestyle photography, two distinct adult women, caring interaction, realistic silk fabric, no xianxia poster. |
| coser, 漫展, 展会, ChinaJoy, BW, Bilibili World, TGS, Tokyo Game Show, 游戏展台, 官方摄影 | `cosplay-convention-photography` | Use official convention photography, original AAA game-character cosplay, 85mm portrait lens, softly blurred booth background, no cheap costume or cluttered crowd. |

## Structured Chinese Calls

When the user provides fields such as `技能 / 风格 / 气质 / 场景 / 服装 / 动作 / 构图 / 生成`:

1. Load `references/structured-call-format.md`.
2. Treat the block as a complete user interface request, not as prose to rewrite.
3. Preserve user fields exactly in parameter lock.
4. Infer missing route, aesthetic, clothing, gesture, light, palette, lens, and negative prompt from the relevant style file.
5. If a field needs safety rewriting, apply intent-preserving safety rewrite: change only the risky wording, not the scene, temperament, costume class, story relation, or composition.
6. If `生成: 是`, `生图`, or `直接生成` is present, assemble a safe final prompt and generate the image. Otherwise return prompt first.
7. Never ask the user to read examples or style docs.

## Eastern Aesthetic Atlas Routing

When the user asks for 东方美学图鉴, 图鉴封面, 图鉴正文, 小红书图鉴, 四大美人, 四大才女, 十二花神, 二十四节气, 东方神女, 敦煌飞天, 朝代服饰, 历史人物, 东方器物, 东方神话, 东方文化专题:

1. Load `styles/东方美学图鉴.md`.
2. Treat the request as a visual content system. Decide the page type: cover, overview page, character page, timeline page, compare page, or knowledge page.
3. Default ratio is `3:4` / `1080x1440` for atlas pages, overriding the global 9:16 default only for this route.
4. For cover pages, preserve Cover Template V1.0: series identity, issue number, theme title, subtitle, visual zone, restrained paper background.
5. For content pages, do not include 东方美学图鉴, DONGFANG MEIXUE TUJIAN, Vol.xx, logo, issue number, column frame, or cover-style brand header. Focus on the content layout.
6. Keep the design collectible, restrained, museum-catalog-like, and Xiaohongshu-friendly; avoid commercial poster noise.
7. Accept both `Type: Cover / Overview / Character` and Chinese `页面类型: 封面 / 总览页 / 人物页`.
8. If `Type` / `页面类型` is missing and the user gives `Issue` / `期数`, infer `Cover`; if the user gives multiple figures, infer `Overview`; if the user gives one named figure or fields such as `Name / Dynasty / Identity / Tags / Quote / Biography`, infer `Character`.
9. If `生成: 是`, assemble the final prompt and generate the image. If missing, return a complete prompt and layout checklist first.
10. If the user asks for 小红书标题 or 文案, use the Xiaohongshu Title Template and Xiaohongshu Copy Template from `styles/东方美学图鉴.md`.
11. Atlas prompts must follow this order: Global Style, Canvas & Layout, Background System, Typography System, Page Template, Character Parameters, Color System, Decoration Rules, Negative Rules.
12. If a reference image is approved, use reference inheritance mode and only change the requested target area.

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

## Gu Feng Girlfriends

When the user asks for 古风闺蜜, 闺阁夜话, 姐妹古风写真, 古代闺阁生活, 灯下梳发, 共读, 夏夜纳凉, 守夜, 双人古风真人摄影, AncientFemaleCompanionship, or Ancient Female Companionship:

1. Load `styles/古风闺蜜.md`.
2. Treat the result as realistic ancient Chinese lifestyle photography, not illustration, xianxia, fantasy poster, game art, goddess wallpaper, fashion catalog, or studio portrait.
3. Lock the relationship first: sister, close friend, childhood friend, travel companion, disciple sister, confidante, scholar companion, or tea companion.
4. Make the two faces visibly different. Avoid duplicate face, twin-face, doll-face, or copy-paste AI face.
5. Build the image around an interaction: chatting, combing hair, reading together, arranging hair, tea, umbrella sharing, boat travel, farewell, reunion, watching moon, listening rain, or night watch.
6. Use realistic silk/cotton/linen material, separated fabric layers, clear prop semantics, visible body boundaries, and soft natural emotional lighting.
7. Keep both subjects adult, tasteful, non-erotic, and non-voyeuristic.

## Cosplay Convention Photography

When the user asks for Cosplay展会摄影, coser, Coser, 漫展摄影, 展会摄影, ChinaJoy, Bilibili World, BW, Tokyo Game Show, TGS, 游戏展台, 官方展会摄影, or AAA游戏角色Cosplay:

1. Load `styles/Cosplay展会摄影.md`.
2. Treat the image as official convention photography, not ordinary convention snapshots.
3. Keep the character original. Do not reproduce a specific copyrighted game/anime character; use original role directions and AAA game character design quality.
4. Preserve the fixed photo system: 9:16, RAW photo, 85mm portrait lens, f/1.8, shallow depth of field, Kodak Portra-like color, natural skin texture, subject about 70% of frame.
5. Use a large anime/game convention hall with softly blurred official booth, game poster, LED light, few photographers, and few audience members.
6. Lock one role direction, one color system, one costume silhouette, one visible action, one prop or role symbol, and one framing mode.
7. Avoid cheap Lolita, excessive lace, plastic fabric, eroticized costume, cluttered convention background, booth logo stealing focus, all subjects looking at camera, and wide-angle distortion.

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
