---
title: "5-Layer Prompt Stack"
description: "A practical Seedance guide to reducing slop with a 5-layer prompt structure, camera and lighting language, constraints, time-coded multi-shot prompts, and @ reference roles."
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

No matter how creative the idea is, Seedance will still drift into slop if the prompt does not match the way the model reads camera, lighting, motion, and constraints. In practice, it behaves less like a generic text box and more like a compact film set that expects directed shot language. If you only give it plain prose, the subject gets soft, the camera starts guessing, and style words sit on top without really controlling the shot.

This page focuses on the **prompting system itself**, not account setup or access. The goal is simple: make it clear how Seedance reads a shot, which words tend to stabilize output, and how to structure prompts so subject identity, motion, framing, and quality constraints reinforce each other instead of fighting each other.

## Why slop keeps happening

Most weak Seedance generations come from **prompt architecture problems**, not idea problems.

- If the subject is abstract, identity and silhouette drift quickly.
- If the action is really just mood description, the result behaves like a still image.
- If subject motion and camera motion are mixed together, the model has to guess what is supposed to move.
- If the prompt stacks vague words like `cinematic`, `beautiful`, or `epic`, it adds flavor without really directing the shot.
- If the prompt has no constraints, jitter, flicker, bent limbs, stretching, and identity drift show up fast.

The core point is that Seedance reacts more like a model reading **shooting instructions** than a model answering a search query.

## What this framework is for

Seedance works better when you think of it as a multimodal production setup rather than a plain text-to-video box. In one generation, you can combine:

- Up to `9` image references
- Up to `3` video references
- Up to `3` audio references
- A text prompt

Image references are useful for character sheets, moodboards, product shots, or storyboard panels. Video references are strong for camera motion, choreography, and pacing. Audio references help lock direction for music, voiceover, or sound effects.

Results are usually more stable when `@Image`, `@Video`, and `@Audio` each have a clear job. If you are typing text only, you are using only part of what makes the system strong.

## Core structure

```text
Subject -> Action -> Camera -> Style -> Constraints
```

Official material may present a broader formula, but in practice this 5-layer structure is one of the most reliable ways to keep Seedance outputs coherent. The order matters for a reason.

- `Subject` locks identity first.
- `Action` tells the model that the shot should move instead of sit like a still.
- `Camera` fixes framing and point of view.
- `Style` adds flavor later so it interferes less with motion.
- `Constraints` close the gaps with guardrails.

Even before you tune anything else, just keeping these layers separate usually improves consistency.

## 1. Subject

Subjects get weak fast when they stay abstract. Even a short line works better when it contains specific visual anchors.

```text
Bad: a woman
Good: a young woman with brown hair
Best: late 20s woman, tight dark curls at ear length, small silver hoop in left ear, fitted black turtleneck, neutral expression
```

- One subject per generation is the safest default.
- Two can work when they are separated spatially and labeled clearly, such as `@Character_A` and `@Character_B`.
- Three or more often increases identity confusion sharply.
- If face consistency matters, define at least a few stable features such as hair, clothing, age range, expression, or accessories.

The job of the subject layer is not poetic writing. Its job is to leave the model with **reusable visual anchors**.

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
- One major action per shot is the safest default.
- Verbs like `turns`, `walks`, `sprints`, `leans`, `reaches`, and `jumps` usually land better than mood-heavy phrasing.

That separation alone usually makes shot interpretation more stable.

## 3. Camera

This is one of the biggest quality levers in Seedance. Use one primary camera move per generation, and describe rhythm, direction, and control rather than technical camera-sheet details.

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

Additional practical rules:

- Prefer shot rhythm over camera specs like `f-stop`, `ISO`, or lens math.
- `handheld` adds energy, but it also raises the chance of visible instability, so pair it with constraints.
- `whip pan`, `dynamic`, and `swift` can work, but they fail loudly when the rest of the shot is not controlled.

## 4. Style

Style works best when lighting comes first. In Seedance, lighting has outsized influence on perceived quality. A word like `cinematic` is usually too vague on its own. Specific lighting, color, and film texture cues land more reliably.

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

The real job of the style layer is not decoration. It is to define **light direction, tone, and surface texture**.

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

Constraints are usually cleanest at the very end of the prompt. For character shots, `avoid bent limbs` and `maintain face consistency` are close to default safety settings.

## Time-coded multi-shot prompts

When you want several beats inside a short clip, time coding is the clearest structure. This is also one of the areas where Seedance can feel noticeably stronger. Give each segment its own subject, action, camera, and lighting state, then specify transitions explicitly.

```text
(0-3s) late 20s woman, tight dark curls, black turtleneck. She stands still, then slowly turns toward camera. Fixed framing. Golden hour rim light. Avoid jitter, maintain face consistency.

hard cut to

(3-7s) she breaks into a sprint through shallow water, coat lifting behind her. Side tracking shot, slow then controlled acceleration. Overcast daylight, natural colors. Avoid temporal flicker, no distortion.

seamless morph into

(7-12s) she jumps onto a rooftop ledge and holds for one beat. Gentle push-in. Backlit sunset silhouette. Sharp clarity, stable picture.
```

- Give each shot one clear job.
- Use transitions like `hard cut to` or `seamless morph into` instead of leaving the handoff ambiguous.
- Re-state camera and lighting state in each segment rather than assuming the model will carry them perfectly.
- It is usually better to split motion into 2-4 second chunks than to overload a single segment.

## @ reference system

The most believable results usually come from clearer reference roles, not just more files. In practice, 6-12 references can work well when every file has one job.

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

## Quick checklist

- Is the subject visually specific enough to stay stable
- Is the action written as visible motion instead of mood
- Is there only one main camera move
- Is style defined through lighting and texture rather than vague praise words
- Are the constraints placed at the end
- If references exist, does each file own one role

## Keep these rules

- Never mix subject motion and camera motion in the same instruction.
- Pick one camera move and start from `slow`, `gentle`, or `controlled`.
- Replace vague mood words with specific lighting and film texture.
- Put constraints last so they can catch jitter, distortion, and identity drift.
- If you use references, give each file exactly one role.

Those five habits alone reduce a large amount of output variance from the same idea. Seedance does not reward magic wording nearly as much as it rewards **clear shot architecture**. In practice, that means the real skill is keeping `Subject -> Action -> Camera -> Style -> Constraints` intact from start to finish.
