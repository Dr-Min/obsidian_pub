---
title: "5-Layer Prompt Stack"
description: "A practical Seedance guide to building prompts in the order Subject, Action, Camera, Style, Constraints, plus camera keywords, lighting modifiers, constraint sets, time-coded multi-shot structure, and @ reference roles."
date: 2026-04-16
modified: 2026-04-16
draft: false
publish: true
lang: "en"
translationKey: "seedance-five-layer-prompt-stack"
tags:
  - blog
  - en
  - ai-video
  - seedance
  - seedance-2
  - guide
  - shot-design
---

# 5-Layer Prompt Stack

Seedance behaves less like a plain text-to-video box and more like a small multimodal film set. That is why generic prose often turns into mushy results with unstable framing or motion. This page skips setup details and focuses only on the prompt structure that most directly changes output quality.

## What to know first

- A single generation can combine text with up to `9` image references, `3` video references, and `3` audio references.
- Results are usually more stable when `@Image`, `@Video`, and `@Audio` each have a clear job.
- The safest default is one subject move and one camera move per shot.

## Core structure

```text
Subject -> Action -> Camera -> Style -> Constraints
```

This order matters for a reason.

- `Subject` locks identity first.
- `Action` tells the model that the shot should move instead of sit like a still.
- `Camera` fixes framing and point of view.
- `Style` adds flavor later so it interferes less with motion.
- `Constraints` close the gaps with guardrails.

## 1. Subject

Subjects get weak fast when they stay abstract. Even a short line works better when it contains specific visual anchors.

```text
Bad: a woman
Good: a young woman with brown hair
Best: late 20s woman, tight dark curls at ear length, small silver hoop in left ear, fitted black turtleneck, neutral expression
```

- One subject per generation is the safest default.
- If you need more than one, separate them spatially and label them clearly, such as `@Character_A` and `@Character_B`.
- If face consistency matters, define at least a few stable features such as hair, clothing, age range, expression, or accessories.

## 2. Action

Action should describe visible movement, not mood. Use present tense and keep each shot focused on one major motion.

```text
Bad: she looks happy and is enjoying the sunset
Good: she slowly turns toward the camera, breeze lifting the hem of her skirt, eyes narrowing against the light
```

The most important rule is to separate subject motion from camera motion.

```text
Bad: spinning camera around a dancing person
Good: the dancer spins slowly, camera holds fixed framing
```

- The subject line says what the person or object does.
- The camera line says how the shot observes that action.

That separation alone usually makes shot interpretation more stable.

## 3. Camera

This is one of the biggest quality levers in Seedance. Use one primary camera move per generation, and describe rhythm and direction rather than technical camera-sheet details.

### Common camera keywords

- Static shots: `fixed`, `locked-off`, `static wide`, `locked tripod`
- Moving shots: `push-in`, `dolly in`, `pull-out`, `dolly out`, `pan left`, `pan right`, `tracking shot`, `orbit`, `arc`, `360 orbit`, `aerial`, `drone shot`, `handheld`, `crane up`, `crane down`, `gimbal`, `steadicam walk`, `whip pan`, `dolly zoom`, `rack focus`

### Speed modifiers

- Very slow: `imperceptible`, `barely`
- Safe defaults: `slow`, `gentle`, `gradual`
- Stable motion: `smooth`, `controlled`
- Stronger motion: `dynamic`, `swift`

`fast` is one of the riskiest words in the box. If something needs to move fast, let one element move fast and keep the rest stable.

When you need a compound move, write it in time order instead of stacking everything together.

```text
start: slow dolly-in, then: gentle pan right for the final 2 seconds
```

## 4. Style

Style works best when lighting comes first. A word like `cinematic` is usually too vague on its own. Specific lighting, color, and film texture cues land more reliably.

### Useful lighting and style modifiers

- `golden hour`
- `rim light`
- `dramatic rim light`
- `soft key from 45 degrees`
- `overcast daylight`
- `backlit silhouette at sunset`
- `volumetric fog`
- `chiaroscuro`
- `35mm`
- `16mm`
- `anamorphic lens flare`

This kind of bundle tends to work better:

```text
cinematic film tone, 35mm, warm golden lighting
```

By contrast, words like `glow`, `glimmer`, and `glints` can introduce flicker artifacts, so they are worth using carefully.

## 5. Constraints

Constraints are the last safety layer. They matter most when you want a shot to feel less synthetic or when character consistency is critical.

### Base constraint set

- `avoid jitter`
- `avoid bent limbs`
- `avoid identity drift`
- `avoid temporal flicker`
- `no distortion`
- `no stretching`
- `maintain face consistency`

### Common quality suffix

- `sharp clarity`
- `natural colors`
- `stable picture`
- `no blur`
- `no ghosting`
- `no flickering`

Constraints are usually cleanest at the very end of the prompt.

## Time-coded multi-shot prompts

When you want several beats inside a short clip, time coding is the clearest structure. Give each segment its own subject, action, camera, and lighting state, then specify transitions explicitly.

```text
(0-3s) late 20s woman, tight dark curls, black turtleneck. She stands still, then slowly turns toward camera. Fixed framing. Golden hour rim light. Avoid jitter, maintain face consistency.

hard cut to

(3-7s) she breaks into a sprint through shallow water, coat lifting behind her. Side tracking shot, slow then controlled acceleration. Overcast daylight, natural colors. Avoid temporal flicker, no distortion.

seamless morph into

(7-12s) she jumps onto a rooftop ledge and holds for one beat. Gentle push-in. Backlit sunset silhouette. Sharp clarity, stable picture.
```

- Give each shot one clear job.
- Use transitions like `hard cut to` or `seamless morph into` instead of leaving the handoff ambiguous.

## @ reference system

The most believable results usually come from clearer reference roles, not just more files. Each file should have one job.

- `@Image1 = first frame`
- `@Image2 = last frame`
- `@Video1 = camera motion reference`
- `@Video2 = pacing reference`
- `@Audio1 = background music`
- `@Audio2 = voiceover`

If you use many references, stability usually improves when each one owns a single responsibility.

## Reusable template

### Single shot

```text
[Subject]. [Action]. [Camera]. [Style]. [Constraints].
```

### Example

```text
late 20s woman, tight dark curls at ear length, fitted black turtleneck, neutral expression. She slowly turns toward the camera, breeze lifting the edge of her coat. Gentle push-in, fixed eye-level framing. Golden hour rim light, cinematic film tone, 35mm. Avoid jitter, avoid identity drift, maintain face consistency, sharp clarity, natural colors.
```

### Multi-shot

```text
(0-3s) [Subject]. [Action]. [Camera]. [Style]. [Constraints].
hard cut to
(3-6s) [Subject]. [Action]. [Camera]. [Style]. [Constraints].
```

## Keep these rules

- Never mix subject motion and camera motion in the same instruction.
- Pick one camera move and start from `slow`, `gentle`, or `controlled`.
- Replace vague mood words with specific lighting and film texture.
- Put constraints last so they can catch jitter, distortion, and identity drift.
- If you use references, give each file exactly one role.

Those five habits alone reduce a large amount of output variance from the same idea.
