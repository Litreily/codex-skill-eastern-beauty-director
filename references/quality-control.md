# Quality Control

## Avoid Generic Gufeng

Before finalizing, check:

- Is exactly one primary route driving the visual direction?
- Have explicit user parameters been preserved rather than replaced?
- Is the output more than a beauty portrait?
- Does the heroine have a readable fantasy role?
- Does the character have a clear face temperament and body language?
- Is the hand action meaningful rather than idle?
- Is there a memorable visual hook or artifact?
- Is there one dominant first-glance wow device?
- Can the image be summarized as one striking thumbnail shape?
- Does the environment imply a larger Eastern fantasy world?
- Is there a clear story moment?
- Is the clothing specific enough to visualize?
- Are the hands doing something plausible?
- Does the scene have spatial depth?
- Is the lighting named and motivated?
- Is the color palette restrained?
- Are modern/cosplay cues excluded?

If fewer than three of role, artifact, wonder setting, supernatural phenomenon, strict color system, story conflict, or wow device are present, upgrade the prompt before returning it.

If the prompt has many decorative details but no dominant shape or event, remove secondary ornaments and add a single oversized or impossible visual device.

## Avoid Generic Eastern Beauty

For 东方美人, 东方审美, 柔美, 妩媚, 成熟, 优雅, 高贵, 清冷, 温婉, 英气, 神性, or 慵懒, check:

- Is one dominant beauty temperament driving the image?
- Does the prompt express beauty through gaze, posture, hand gesture, shoulder-neck line, hair rhythm, fabric behavior, light, and emotion?
- Is the woman still the visual subject rather than being swallowed by costume, props, or background?
- Does 妩媚 come from mature gaze, controlled posture, fabric, jewelry, candlelight, and atmosphere rather than exposure?
- Does 高贵 come from identity, ritual, symmetry, posture, and composition rather than random gold clutter?
- Does 成熟 come from composure, material weight, deep palette, and controlled expression rather than age exaggeration?
- Does 清冷 still have emotion in the eyes rather than a blank mannequin face?

If the result reads like "pretty woman + Eastern clothes + vague elegance," add a concrete gesture, a precise material, a motivated light source, and a specific emotional moment.

## Avoid Generic Classical Beauty

For 古典东方美人, 宋韵, 唐宫, 江南, 洛神, 青瓷, 昆曲, 仕女, or 闺阁, check:

- Is one classical route driving the image?
- Is the image classical without automatically becoming mythic fantasy?
- Are line, fabric, gesture, face temperament, light, and atmosphere doing the beauty work?
- Does the scene have cultural taste without turning into costume cosplay or tourist photography?
- Is gauze used as atmosphere or layering, not revealing fabric?

If the prompt is too plain, add one poetic visual device: rain reflection, water mirror, tea steam, porcelain moonlight, flower-window shadow, bamboo shadow, lantern in snow, or spring curtain light.

## Avoid Generic Modern Beauty

For 写实, 现代, 摄影, 杂志, 新中式, 东方高级感, check:

- Is one modern style route driving the prompt?
- Does the face have a temperament, structure, gaze, and natural skin texture?
- Is the clothing a specific modern or new-Chinese silhouette, not a vague "Chinese dress"?
- Does the posture or hand action reveal character without sexualized framing?
- Is the background tasteful and spatially clear?
- Are lens, light source, and palette named?
- Are cheap cosplay, heavy filters, plastic skin, transparent revealing fabric, and clutter excluded?

If the result reads like "pretty woman in Chinese clothes," upgrade styling, posture, light, and location before returning.

## SweetHomeGirl Consistency

For SweetHomeGirl prompts, check:

- Is 甜系纯欲生活写真 / SweetHomeGirl using the correct priority: body, story moment, pure-desire, face, outfit, composition, scene?
- Does the prompt follow the core formula: realism + feminine charm + romantic feeling + story moment + natural pure-desire?
- Is the body system hard lock placed first and protected from all other parameters?
- Does the prompt preserve young mature feminine body, healthy fullness, rounded natural curves, full natural bust, natural waist-hip transition, soft S-curve, full healthy legs, and no supermodel/fitness/bony/anime drift?
- Is there a real story moment, with story first, action second, expression last?
- Is pure-desire built from gaze, expression, action, outfit, atmosphere, and feminine curves rather than exposure, erotic suggestion, exaggerated pose, or deliberate seduction?
- Does the subject read as 20-26 adult young urban woman, not underage, childish, or student-girl?
- Is the face style varied without becoming a different universe or a fixed-face clone?
- Does the outfit feel like something a real woman would wear, not lingerie/swimsuit/gown/professional/stage/overexposed styling?
- Is composition treated as framing, not just aspect ratio: upper-body close-up, thigh-up, full body, or face close-up?
- Does the person occupy more than 60% of the frame, with expression/gaze first and background only supporting?
- Does the image avoid influencer photoshoot, fashion editorial, edge-bait, AI-sexy, static model display, and background-dominant feeling?
- Does the prompt keep realistic anatomy, natural proportions, correct hands, and natural body posture?
- Is the negative prompt protecting against body drift, age drift, story loss, static posing, influencer/fashion/AI-sexy feeling, excessive exposure, background dominance, deformed hands, plastic skin, and low-quality artifacts?

## Prompt Copy Blocks

When returning a final prompt for copy/paste, keep the final prompt and negative prompt in separate Markdown `text` code blocks. Do not mix notes, route labels, or analysis inside the copyable prompt block.

## Common Negative Prompt

```text
low quality, low resolution, blurry, jpeg artifacts, watermark, text, logo,
bad anatomy, bad hands, extra fingers, missing fingers, fused fingers,
distorted face, asymmetrical eyes, plastic skin, over-smoothed skin,
modern clothing, cheap cosplay, zipper, sneakers, phone, microphone,
generic hanfu photoshoot, plain beauty portrait, western medieval armor,
japanese shrine, korean hanbok, random cyberpunk neon,
overexposed, oversaturated, messy background, duplicate person
```

## Safety and Taste

- Keep the character adult and avoid sexualized framing.
- Avoid transparent clothing used to reveal the body.
- Avoid "young girl", "schoolgirl", or age-ambiguous sensual language.
- For beauty-focused prompts, emphasize dignity, expression, styling, and cinematic craft.
- For red-gold palace boudoir or ornate pure-desire gu feng prompts, use candlelight, incense haze, silk layers, jewelry, carved screens, and dignified gaze; avoid foot-sole foreground, fetish framing, extreme contortion, exposed chest, lingerie, or transparent revealing fabric.
- For pure-desire or private-chamber prompts, build attraction through gaze, shoulder-neck line, wet hair, opaque silk folds, candlelight, steam, and composition. Do not use nudity, exposed chest, lingerie, voyeuristic framing, or transparent revealing clothing.

## Mini-Program Prompt Generator Fit

When the output will be used in a prompt app, provide modular fields:

```text
主题：
人物：
服饰：
场景：
光影：
镜头：
风格：
负面词：
```

Keep each field independently reusable.
