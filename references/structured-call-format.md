# Structured Call Format

Use this reference when the user provides a short Chinese parameter block or when the user wants simple fields instead of reading examples.

The user should be able to call the skill with a small form. Codex must infer the route, aesthetic system, lighting, lens, atmosphere, prompt, negative prompt, and image-generation prompt.

## Universal Minimal Format

Recommended for all Eastern beauty routes:

```text
技能: 东方美人

风格:
气质:
场景:
服装:
动作:
构图:

生成:
```

Field meanings:

- `技能`: 东方美人, 古典东方美人, 东方幻想古风, 现代东方美人, 甜系纯欲生活写真, or SweetHomeGirl.
- `风格`: route or broad style, such as 宋韵茶影, 唐宫夜宴, 绮罗金帐, 东方珠宝大片.
- `气质`: one or two aesthetics, such as 温婉优雅, 成熟妩媚, 高贵成熟, 清冷高贵.
- `场景`: user-facing scene phrase. If broad, refine it internally.
- `服装`: one simple line. If missing, infer from style and scene.
- `动作`: story moment or visible gesture. If missing, infer one.
- `构图`: framing such as 上半身, 大腿以上, 全身, 特写. Ratio still follows global default `9:16` unless specified.
- `生成`: yes/no. If yes, generate image after assembling the final prompt. If missing, return prompt first.

## Route-Specific Lightweight Calls

### Classical Eastern Beauty

```text
技能: 古典东方美人

风格: 宋韵茶影
气质: 温婉优雅
场景: 雨天茶室
服装: 宋式浅色交领长衫
动作: 端起茶杯前抬眼
构图: 大腿以上
生成: 是
```

Supported `风格`:

- 洛神水镜
- 宋韵茶影
- 唐宫夜宴
- 江南烟雨
- 青瓷月影
- 昆曲花影
- 竹林清谈
- 胭脂雪
- 玉楼春睡

### Modern Eastern Beauty

```text
技能: 现代东方美人

风格: 东方珠宝大片
气质: 高贵成熟
场景: 黑色丝绒背景
服装: 黑色新中式高领丝质上衣
动作: 手指轻触翡翠耳坠
构图: 上半身
生成: 是
```

Supported `风格`:

- 新中式杂志
- 东方静奢
- 旗袍电影感
- 东方珠宝大片
- 茶室光影
- 都市晚宴东方
- 江南现代诗意

### Eastern Fantasy / Gu Feng

```text
技能: 东方幻想古风

风格: 绮罗金帐
气质: 妩媚高贵
场景: 红金宫廷秘仪空间
服装: 朱砂古金色层叠礼服
动作: 一手扶纱幔，一手提宫灯
构图: 全身
生成: 是
```

Supported `风格`:

- 天象神朝
- 昆仑雪剑
- 敦煌壁画
- 沧海龙庭
- 莲梦镇邪
- 凤阙宫火
- 绮罗金帐
- 月宫炼华
- 青铜神谕城
- 雾浴私语

### SweetHomeGirl / 甜系纯欲生活写真

Keep the existing lightweight SweetHomeGirl format:

```text
技能: SweetHomeGirl

人脸风格:
场景:
穿搭:
故事瞬间:
构图:

天气:
时间:
镜头要求:
生成:
```

## Inference Rules

When fields are missing:

1. If `技能` is missing but style is known, infer skill family from `风格`.
2. If `气质` is missing, choose the route default:
   - 宋韵茶影 -> 温婉优雅
   - 唐宫夜宴 -> 成熟妩媚
   - 东方珠宝大片 -> 高贵成熟
   - 绮罗金帐 -> 妩媚高贵
3. If `动作` is missing, add one visible gesture using `东方美人审美系统.md`.
4. If `服装` is missing, infer route-appropriate opaque clothing.
5. If `构图` is missing, default to 大腿以上 for beauty portraits, 全身 for key visuals.
6. If `生成: 是`, produce the image after prompt assembly unless the request is unsafe or ambiguous.

## Intent-Preserving Safety Rewrite

When a user field contains sensitive wording, do the smallest possible rewrite. The goal is to make the prompt accepted by image models while preserving the user's scene, temperament, story, costume direction, and composition.

Hard rules:

- Preserve the user's core nouns in `参数锁定`: style, temperament, scene type, clothing intent, action relation, composition, ratio, and generation choice.
- Do not replace the user's concept with a different scene, different mood, different costume class, or unrelated action.
- Rewrite only the risky expression layer: camera angle, exposure implication, voyeuristic wording, transparent/revealing fabric, direct bath/body wording, or fetish framing.
- If the original request is intimate or bath-related, keep it adult, dignified, covered, ceremonial, and non-voyeuristic.
- Prefer `安全改写` labels so the user can see what was changed and why.

Examples:

| User wording | Safe rewrite while preserving intent |
|---|---|
| 泡花浴池 | 唐代宫廷花浴池 / 香汤池畔 / 花瓣倒影池 |
| 浴裙 | 覆身式唐风浴裙 / 轻薄但不透的丝绸浴裙 / 典礼感浴袍 |
| 洗浴，柔美 | 花浴仪式中的柔美瞬间 / 扶池沿拨动花瓣 / 整理被水汽润湿的衣袖 |
| 私房、浴后、水汽 | 私密内室的仪式感人像 / 香雾与烛光 / 覆身丝绸层次 |
| 透、微透 | 轻薄层叠、光泽丝绸、不透明覆身 |

For example, this user request:

```text
技能: 古典东方美人
风格: 唐代宫廷
气质: 高贵大气
场景: 泡花浴池
服装: 浴裙
动作: 洗浴 柔美
构图: 全身
生成: 否
```

should stay close to the original concept:

```text
参数锁定:
风格: 唐代宫廷
气质: 高贵大气
场景: 宫廷花浴池 / 香汤池畔
服装: 覆身式唐风浴裙，轻薄但不透
动作: 花浴仪式中的柔美瞬间
构图: 9:16，全身

安全改写:
将“洗浴”改为“花浴仪式”，将“浴裙”限定为覆身、不透明、典礼感；保留花浴池、柔美、高贵大气和全身构图。
```

## Output Behavior

For structured calls:

- Preserve user fields as `参数锁定`.
- Add inferred values as `自动补全`.
- Generate the full prompt internally.
- If `生成: 是`, call image generation after assembling a safe prompt.
- If `生成` is missing or no, return the complete prompt and checklist first.
