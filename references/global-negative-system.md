# Global Negative System

Use this file as the shared safety and quality base for every Eastern Beauty
route before adding style-specific negatives. The goal is to prevent the most
basic model failures first, then control taste and style.

## Priority

1. Human anatomy integrity
2. Face and eye integrity
3. Hand and foot integrity
4. Prop semantic integrity
5. Multi-subject boundary integrity
6. Image quality and style cleanliness

## Global Human Anatomy Negative

```text
bad anatomy, malformed anatomy, wrong limb count, extra limbs,
extra arms, missing arms, extra legs, missing legs, broken limbs,
twisted limbs, twisted joints, dislocated shoulders, broken wrists,
deformed elbows, deformed knees, unnatural torso twist, broken neck,
neck too long, body out of frame accidentally, duplicated body parts
```

## Global Hand And Foot Negative

```text
bad hands, deformed hands, malformed hands, extra hands, missing hands,
floating hands, extra fingers, missing fingers, wrong finger count,
fused fingers, melted fingers, broken fingers, fingers fused with objects,
hand fused with fabric, hand penetrating hair, hand penetrating sleeve,
bad feet, deformed feet, missing feet, extra feet, mutated toes,
wrong toe count, foot fused with fabric, feet cut off unnaturally
```

## Global Face Integrity Negative

```text
distorted face, broken face, melted facial features, duplicated face parts,
asymmetrical eyes, misaligned eyes, extra eyes, deformed mouth,
scenery inside face, landscape on face, object fused with face,
flowers fused into skin, fabric pattern on skin, jewelry entering eyes,
water reflection inside face, background texture on face
```

## Global Prop Semantic Negative

```text
prop morphing, object mutation, deformed prop, melted object,
cup turning into chain, jewelry replacing prop, lantern becoming jewelry,
book becoming fabric, fan becoming background texture,
umbrella turning into ribbon, bouquet becoming hair,
random chain objects, floating random objects
```

## Multi-Subject Negative

Use this section whenever there are two or more people.

```text
merged bodies, fused torsos, fused shoulders, unclear body boundary,
one body with two heads, duplicate face, same face on multiple people,
clone face, unwanted third person, extra person, extra arms between people,
intertwined extra hands, deformed embrace, body parts crossing unnaturally
```

## Global Quality Negative

```text
low quality, low resolution, blurry, jpeg artifacts, watermark, text, logo,
plastic skin, wax skin, over-smoothed skin, over-sharpened, overexposed,
oversaturated, messy background, background stealing focus,
multiple focal points, visual clutter
```

## Style-Specific Layering

After applying the global base, append only the relevant style-specific
negative layer:

- Fantasy / gu feng: excessive particles, chaotic ribbons, ornament overload,
  AI fantasy poster style, mobile game splash art.
- Classical beauty: cheap hanfu studio photo, tourist costume photo, heavy
  stage makeup, dynasty mismatch, transparent revealing fabric.
- Modern beauty: influencer selfie, heavy beauty filter, cheap cosplay,
  commercial hard-sell advertising, neon cyberpunk.
- Gu Feng Girlfriends: duplicate face, merged bodies, unclear body boundary,
  xianxia poster, sexual posing, body display posing.
- SweetHomeGirl: underage, childish, student-girl styling, AI-sexy feeling,
  static model posing, influencer cover pose, excessive exposure.
- Eastern Aesthetic Atlas: garbled text, fake letters, random Chinese
  characters, text over face, PPT layout, knowledge-card clutter.

## Positive Repair Prompts

When a generated image fails, simplify the prompt and add positive controls:

```text
clear full body structure, correct limb count, natural hand anatomy,
five fingers on each visible hand, realistic feet, clean face area,
sharp eyes, separate subject silhouette, clear prop identity,
background does not enter the face, subject-first composition
```
