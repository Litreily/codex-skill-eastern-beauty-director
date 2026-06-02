# Prompt Framework

## Director Brief

Use a brief before the prompt when the user needs quality, not just a one-line prompt:

- Route: the single primary Eastern fantasy route.
- Concept: the image's central idea.
- Role: the heroine's mythic profession, duty, or destiny.
- Story moment: what has just happened or is about to happen.
- Worldbuilding hook: the object, place, or phenomenon that makes the image belong to an Eastern fantasy world.
- Wow device: the first-glance attraction point, such as giant halo, impossible transformation, scale contrast, dangerous action, or unusual viewpoint.
- Visual priority: face, clothing, environment, gesture, or atmosphere.
- Avoid: anything that would weaken the image.

Example:

```text
导演设定：
一位身着宋制灵感长衫的成年女子在雨后水榭回身，画面重点是克制的情绪、湿润木纹、薄雾与织物层次，而不是夸张仙气。
```

## Universal Prompt Grammar

Use this order unless the target model benefits from another structure:

```text
[adult subject], [mythic role/subgenre], [story moment], [face and expression],
[body language, gaze target, hand action], [hair and makeup], [costume silhouette and materials],
[iconic prop/artifact], [wonder-scale setting], [primary wow device], [supernatural phenomenon],
[lighting], [camera/lens/composition], [color palette], [texture/detail],
[art style / render style], [quality constraints]
```

## Parameter Lock

Before expansion, list explicit inputs without rewriting them away:

```text
Subject:
Face temperament:
Body language:
Route/style:
Mood:
Costume:
Scene:
Prop/artifact:
Wow device:
Palette:
Aspect ratio:
Model/platform:
Output mode:
Must keep:
Must avoid:
Supplements:
```

Only fill fields that exist or matter. Put inferred defaults under `Supplements`.

## Director Module Expansion

For high-quality prompt requests, include a public-facing module analysis. Keep reasoning private; show only final visible decisions:

- Character and temperament: adult boundary, role, face temperament, facial structure, body language, gaze, hand action.
- Costume and artifact: silhouette, materials, embroidery, ornaments, prop function.
- Scene and spectacle: territory, depth layers, primary wow device, supernatural phenomenon, story tension.
- Camera and lighting: framing, angle, depth of field, light source, color and texture.

This analysis should read like art direction, not a field recap.

## Chinese Prompt Template

```text
生成一张[画幅比例]东方幻想古风美女主视觉。成年东方幻想女子，[神话职业/身份]，[情绪与故事瞬间]，
[脸部气质/脸型/眼神/神态]，[身形剪影/身体语言/视线目标/手部动作]，
[发髻/发饰/妆容]，身着[幻想化服装形制/材质/纹样/颜色]，
手持/操控[标志性法器或道具]，置身[奇观场景/季节/天气/空间层次]，
[超自然异象或世界观符号]，
[主光源/辅光/轮廓光]，[镜头/景别/构图]，
[色彩方案]，[材质细节]，
东方幻想系列主视觉，电影级光影，细腻皮肤质感，真实布料纹理，强剪影，高级国风审美，画面干净，无文字
```

## English Prompt Template

```text
adult Eastern fantasy Chinese heroine, [mythic role], [story moment and mood],
[facial temperament, face structure, expression], [body language, gaze target, meaningful hand action],
[hair ornament and makeup],
wearing [fantasy hanfu silhouette, fabric, embroidery, color],
[gesture/action], controlling [iconic artifact], in [wonder-scale setting, season, weather, depth],
[supernatural phenomenon], [lighting], [camera/lens/composition],
[color palette], detailed fabric texture, natural skin texture,
premium Eastern fantasy key visual, refined art direction, strong silhouette, high detail, no text
```

## Model Adaptation

Midjourney:

- Use concise English with strong visual nouns.
- Put the most important subject and scene early.
- Add parameters at the end: `--ar 2:3 --style raw --s 150` when suitable.

Stable Diffusion / ComfyUI:

- Provide positive and negative prompts separately.
- Use comma-separated tags, avoid extremely long poetic sentences.
- Add hand/anatomy negatives and optional weighting only if the user asks.

DALL-E / GPT image tools:

- Use natural language instructions.
- Mention composition and exact exclusions clearly.
- Avoid tag soup and unsupported sampler parameters.

Chinese prompt generator apps:

- Keep fields structured: subject, style, scene, lighting, camera, negative.
- Make prompts copyable and avoid hidden assumptions.
