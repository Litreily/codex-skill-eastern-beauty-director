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
