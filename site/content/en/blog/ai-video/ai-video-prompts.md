---
title: "How to Write AI Video Prompts: Practical Examples and a Clear Structure"
description: "A practical guide to writing better AI video prompts with shot structure, framing, camera movement, 16:9 vs 9:16 strategy, and reusable prompt examples."
date: 2026-04-10
modified: 2026-04-10
draft: false
publish: true
lang: "en"
translationKey: "ai-video-prompts"
tags:
  - blog
  - en
  - ai-video
  - guide
---

If you have tried prompting an AI video model a few times, you have probably seen the pattern already. The idea sounds strong in your head, but the result comes back vague, unstable, or visually generic. In most cases, the issue is not the model alone. The issue is that the prompt is too abstract. An AI video prompt works better when it behaves less like a mood sentence and more like a shot instruction.

There is a major difference between writing `a woman in a city` and writing `medium shot of a woman in a rainy city street, 50mm lens, neon reflections, slow push-in, cinematic night mood`. The second prompt gives the model much clearer direction about framing, lens feel, motion, and atmosphere. That is what makes the output more consistent.

This guide explains what an AI video prompt really is, why structure matters, how to describe framing and motion, how 16:9 and 9:16 differ, and how to build prompts you can actually reuse. If you want a deeper breakdown of camera language on its own, pair this page with [[en/blog/ai-video/camera-techniques/shot-composition-camera-movement|How to Describe Shot Composition and Camera Movement in AI Video Prompts]].

## What Is an AI Video Prompt?

An AI video prompt is a text instruction that tells a model what kind of scene to generate over time. That last part matters. Unlike a still-image prompt, a video prompt has to account for movement, progression, and how the frame evolves.

A useful AI video prompt usually contains these layers:

- subject: who or what appears in frame
- action: what the subject is doing
- setting: where the scene happens
- framing: wide shot, medium shot, close-up, low angle, overhead, and so on
- lens feel: wide, normal, portrait, compressed
- camera movement: static, push-in, tracking, handheld, crane, orbit
- lighting and mood: daylight, rim light, neon spill, soft haze, dramatic contrast
- timing or cut logic: whether the moment is a single shot or a multi-cut sequence

That is why a strong AI video prompt is not just a list of adjectives. It is closer to a compact shot plan. You are not only describing what should exist. You are describing how the viewer should experience it.

## Why Good AI Video Prompts Matter

Better prompts matter for two reasons: control and repeatability.

First, they reduce interpretation drift. When the prompt is vague, the model fills the gaps with broad assumptions. Sometimes that produces something interesting, but just as often it creates an image-like clip with weak direction. Clear prompts reduce that randomness by setting stronger constraints.

Second, they make iteration easier. If a result is close but not quite right, a structured prompt lets you isolate one variable at a time. You can change the shot size without rewriting the whole scene. You can replace the movement while keeping the lighting. You can rewrite only the lens feel or the pacing.

Third, they make aspect-ratio adaptation much easier. A wide cinematic frame and a vertical short-form frame should not be prompted the same way. If your prompt already separates subject, framing, movement, and environment, it becomes much easier to adapt the same idea to a new format.

Finally, good prompts scale into multi-cut storytelling. Many strong AI videos are not just a single polished shot. They become stronger when they move through a short structure like setup, escalation, twist, and ending. That is exactly why prompt archives such as [[en/blog/ai-video/seedance/seedance-manhattan-wall-run-portal-prompt|Seedance 2.0 Prompt Archive: Manhattan Sprint, Wall Run, Portal Dive]] are useful. They show how a concept becomes more cinematic when it is broken into cuts.

## A Simple Formula for Writing AI Video Prompts

A practical baseline formula looks like this:

```text
[subject] + [action] + [shot size] + [camera angle] + [lens feel] + [camera movement] + [lighting] + [environment] + [mood/texture]
```

Here is a clean example:

```text
A young director reviewing a storyboard wall, medium shot, eye-level angle, 50mm lens, slow lateral tracking shot, soft daylight through studio windows, industrial creative workspace, cinematic realism, shallow depth of field
```

The point of this formula is not to make every prompt rigid. The point is to force the important visual variables into the sentence so the model has something concrete to follow.

You can also expand the same logic into a cut sequence:

```text
Cut 1: setup
Cut 2: motion escalation
Cut 3: visual twist
Cut 4: climax
Cut 5: ending beat
```

That format works especially well for action scenes, short ads, character reveals, music visuals, and dramatic social clips.

One more rule matters here: keep priority in mind. Subject, action, framing, and movement are usually more important than generic quality adjectives. Words like `epic`, `beautiful`, and `high quality` can help shape tone, but they are not a substitute for actual camera language.

## How to Describe Framing, Lens, and Camera Movement

This is where many AI video prompt guides stay too shallow. They explain style words, but they do not explain how to direct the camera.

Shot size controls how the subject is perceived:

- wide shot: environment, scale, geography
- medium shot: performance, body language, demonstrations
- close-up: emotion, texture, product detail

Lens language changes spatial feeling:

- `24mm wide lens`: expansive space, stronger perspective, more environmental energy
- `50mm lens`: balanced and natural, often the safest general-purpose choice
- `85mm portrait lens`: stronger subject isolation, compressed background, more intimate emotion

Movement changes intensity:

- `locked-off tripod shot`: calm, clear, deliberate
- `slow push-in`: emotional emphasis, growing tension
- `side tracking shot`: speed, travel, lateral momentum
- `gentle handheld`: immediacy, documentary feel, human energy

If you stack too many conflicting movement instructions, the model gets muddy fast. A prompt that says `drone shot, handheld, spinning orbit, dolly in` at the same time usually loses clarity. Pick the one movement that matters most and let the rest of the shot support it.

## How 16:9 and 9:16 Prompts Should Differ

This is one of the most common mistakes in AI video work. A vertical clip is not just a cropped wide clip. The composition priorities change.

In 16:9, you can lean more on horizontal travel, city width, side tracking, and environmental spread. Wide alleys, traffic flow, group blocking, and panoramic backgrounds read well there.

In 9:16, the subject usually needs stronger central framing and more vertical logic. Upward movement, full-body framing, headroom control, and the relation between subject and background height become more important.

Compare these two prompt styles:

```text
A creator running through a neon city alley, wide shot, side tracking shot, 35mm lens, cinematic night lighting
```

```text
A creator centered in frame, vertical full-body shot, slight low angle, narrow neon alley rising behind the subject, upward motion emphasis, 35mm lens, handheld energy
```

The core idea is similar, but the framing logic is different. In vertical video, you often want to emphasize body length, stairs, walls, towers, jumps, portals, vertical light columns, or strong top-to-bottom movement. That is much more effective than copying a wide-frame prompt and hoping the crop will solve it.

## Five Practical AI Video Prompt Examples

### 1. Interview-style brand video

```text
A founder speaking calmly in a creative studio, medium shot, eye-level angle, 50mm lens, locked-off tripod shot, soft key light from the left, subtle background depth, premium documentary feel
```

### 2. Product detail sequence

```text
Close-up of hands unfolding a compact drone controller, slight top-down angle, 85mm lens, slow push-in, crisp studio lighting, matte black tabletop, premium commercial texture
```

### 3. Cinematic street action

```text
A young woman running through a rain-soaked Seoul street at night, medium tracking shot, 35mm lens, reflections on wet asphalt, soft neon haze, cinematic urgency
```

### 4. Vertical short-form portal scene

```text
Vertical full-body shot of a creator stepping into a glowing portal, slight low angle, centered framing, strong upward energy, blue rim light, dramatic smartphone-friendly composition
```

### 5. Multi-cut action build

```text
Cut 1: a lone character stands in an empty rooftop garden at dusk, low-angle cinematic shot, wind in coat and hair
Cut 2: the character sprints forward with impossible speed, side tracking shot, shockwaves and dust
Cut 3: the run transitions into a leap across connected rooftops, brief slow motion, orange city glow
Cut 4: the character lands near a bright portal doorway, camera push-in, tension spike
Cut 5: the character enters the portal as the frame fills with light
```

These examples work because they are not only stylish. They are structurally readable. Each one gives the model enough information about subject, perspective, motion, and environment to produce a stronger interpretation.

## Common Mistakes to Avoid

The first mistake is using only taste words. `Beautiful`, `epic`, and `ultra quality` are not enough on their own.

The second mistake is combining incompatible instructions. A prompt like `extreme close-up drone shot` creates conflicting spatial expectations.

The third mistake is overloading movement. One dominant camera action is usually more reliable than four competing ones.

The fourth mistake is writing lighting too vaguely. `Nice lighting` is weak. `warm sunset rim light`, `soft daylight through curtains`, or `cold blue backlight` are much stronger.

The fifth mistake is ignoring aspect ratio. Vertical video should usually be composed as vertical video from the start.

The sixth mistake is forgetting story progression. Even short AI clips feel stronger when they have a sense of setup and escalation instead of a static visual idea.

## Frequently Asked Questions

### Do longer AI video prompts always work better?

No. Better structure is more important than more words. A short prompt with a clear subject, action, shot size, movement, and lighting often outperforms a long prompt full of vague style language.

### Should I always prompt in English?

Many models respond well to English, but structure matters more than language alone. If you can describe the scene clearly, either language can work. In practice, many creators test both when they want maximum consistency.

### Should 9:16 prompts be written separately?

Usually yes. At minimum, the framing logic, body placement, and vertical movement emphasis should be reconsidered rather than copied from a 16:9 version.

### When should I use multi-cut prompts?

Use them when transitions, escalation, or narrative flow matter. Action clips, dramatic reveals, ads, and stylized short-form videos often benefit from a cut-based structure.

## Conclusion

Writing better AI video prompts is not about collecting more impressive adjectives. It is about describing the scene in camera language. Once you clearly define the subject, the framing distance, the lens feel, the movement, and the light, the output usually becomes more stable and much easier to improve.

The fastest checklist is simple:

- what is in frame
- from what distance you see it
- how the camera moves
- what kind of light and mood define the scene

Get those four layers right first. Then adapt the framing for 16:9 or 9:16, and expand into a multi-cut structure when the idea needs more momentum. That is the real difference between a vague prompt and a reusable AI video prompt system.
