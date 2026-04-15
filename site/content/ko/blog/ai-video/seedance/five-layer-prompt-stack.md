---
title: "5층 프롬프트 스택"
description: "Subject, Action, Camera, Style, Constraints 순서로 Seedance 프롬프트를 짜는 법과 카메라 키워드, 조명 수정어, 제약 조건, 타임코드 멀티샷, @ 레퍼런스 시스템을 정리한 가이드."
date: 2026-04-16
modified: 2026-04-16
draft: false
publish: true
lang: "ko"
translationKey: "seedance-five-layer-prompt-stack"
tags:
  - blog
  - ko
  - ai-video
  - seedance
  - seedance-2
  - guide
  - shot-design
---

# 5층 프롬프트 스택

Seedance는 단순한 텍스트-to-비디오 상자보다 작은 멀티모달 영화 세트에 더 가깝습니다. 그래서 평범한 설명문만 넣으면 결과가 쉽게 퍼지고, 카메라와 모션이 따로 놀기 쉽습니다. 이 문서는 설정법보다 프롬프팅 구조에만 집중해, 실제로 결과 차이를 만드는 규칙만 빠르게 정리합니다.

## 먼저 알아둘 것

- 한 번의 생성에 텍스트와 함께 최대 `9`개 이미지, `3`개 비디오, `3`개 오디오 레퍼런스를 함께 넣을 수 있습니다.
- 텍스트만 쓰는 것보다 `@Image`, `@Video`, `@Audio`에 역할을 분명하게 주는 편이 훨씬 안정적입니다.
- 한 샷에는 주체 움직임 하나, 카메라 움직임 하나만 두는 편이 가장 안전합니다.

## 기본 구조

```text
Subject -> Action -> Camera -> Style -> Constraints
```

이 순서가 중요한 이유는 단순합니다.

- `Subject`가 먼저 있어야 모델이 누구를 붙잡아야 하는지 흔들리지 않습니다.
- `Action`이 둘째여야 정적인 사진이 아니라 움직이는 샷으로 해석됩니다.
- `Camera`는 그 다음에 두어 프레임과 시점을 잠급니다.
- `Style`은 마지막에 가까울수록 분위기를 더하되 모션을 덜 방해합니다.
- `Constraints`는 끝에 두어 남는 문제를 가드레일처럼 막습니다.

## 1. Subject

주체는 추상적일수록 쉽게 흐려집니다. 짧더라도 디테일이 있는 쪽이 훨씬 낫습니다.

```text
Bad: a woman
Good: a young woman with brown hair
Best: late 20s woman, tight dark curls at ear length, small silver hoop in left ear, fitted black turtleneck, neutral expression
```

- 한 생성당 한 명의 주체가 가장 안전합니다.
- 두 명 이상이 필요하면 공간을 분리하고 `@Character_A`, `@Character_B`처럼 역할을 분명히 나누는 편이 낫습니다.
- 캐릭터 일관성이 중요한 샷은 얼굴, 헤어, 의상, 표정 중 최소 두세 가지를 같이 적는 편이 좋습니다.

## 2. Action

Action은 감정 설명이 아니라 화면에 보이는 움직임으로 써야 합니다. 현재형으로 쓰고, 한 샷당 하나의 큰 움직임만 잡는 편이 좋습니다.

```text
Bad: she looks happy and is enjoying the sunset
Good: she slowly turns toward the camera, breeze lifting the hem of her skirt, eyes narrowing against the light
```

가장 중요한 규칙은 주체 움직임과 카메라 움직임을 섞지 않는 것입니다.

```text
Bad: spinning camera around a dancing person
Good: the dancer spins slowly, camera holds fixed framing
```

- 주체는 무엇을 하는지 적고
- 카메라는 어떻게 보는지 따로 적습니다.

이 분리만 지켜도 샷 해석이 훨씬 안정됩니다.

## 3. Camera

Seedance에서 가장 차이를 크게 만드는 층입니다. 한 생성당 하나의 주요 카메라 움직임만 두는 편이 좋고, 기술 스펙보다 리듬과 방향을 적는 편이 더 잘 먹힙니다.

### 자주 쓰는 카메라 키워드

- 정적 샷: `fixed`, `locked-off`, `static wide`, `locked tripod`
- 이동 샷: `push-in`, `dolly in`, `pull-out`, `dolly out`, `pan left`, `pan right`, `tracking shot`, `orbit`, `arc`, `360 orbit`, `aerial`, `drone shot`, `handheld`, `crane up`, `crane down`, `gimbal`, `steadicam walk`, `whip pan`, `dolly zoom`, `rack focus`

### 속도 수정어

- 매우 느리게: `imperceptible`, `barely`
- 가장 안전한 기본값: `slow`, `gentle`, `gradual`
- 안정적 무브: `smooth`, `controlled`
- 강한 무브: `dynamic`, `swift`

`fast`는 가장 조심해야 할 단어입니다. 빠르게 움직이는 것이 필요하면 하나만 빠르게 하고 나머지는 고정하는 편이 낫습니다.

복합 움직임이 필요하면 한 줄에 몰아넣지 말고 시간 순서로 나눕니다.

```text
start: slow dolly-in, then: gentle pan right for the final 2 seconds
```

## 4. Style

Style은 분위기보다 먼저 조명을 잡는 게 핵심입니다. `cinematic` 하나만 쓰면 너무 넓어서 효과가 약합니다. 조명, 컬러, 필름 질감을 구체적으로 적는 편이 좋습니다.

### 자주 쓰는 조명과 스타일 키워드

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

이런 식으로 묶는 편이 낫습니다.

```text
cinematic film tone, 35mm, warm golden lighting
```

반대로 `glow`, `glimmer`, `glints` 같은 단어는 깜빡임 아티팩트를 만들기 쉬워서 조심하는 편이 좋습니다.

## 5. Constraints

Constraints는 AI 느낌을 줄이는 마지막 안전장치입니다. 특히 인물 샷에서는 거의 상시로 붙여 두는 편이 좋습니다.

### 기본 제약 세트

- `avoid jitter`
- `avoid bent limbs`
- `avoid identity drift`
- `avoid temporal flicker`
- `no distortion`
- `no stretching`
- `maintain face consistency`

### 자주 붙이는 품질 접미사

- `sharp clarity`
- `natural colors`
- `stable picture`
- `no blur`
- `no ghosting`
- `no flickering`

Constraints는 문장 중간보다 맨 끝에 두는 편이 깔끔합니다.

## 타임코드 멀티샷

15초 안에서 여러 샷을 지시할 때는 타임코드가 가장 깔끔합니다. 각 구간마다 주체, 동작, 카메라, 조명을 함께 적고 전환 방식도 같이 적습니다.

```text
(0-3s) late 20s woman, tight dark curls, black turtleneck. She stands still, then slowly turns toward camera. Fixed framing. Golden hour rim light. Avoid jitter, maintain face consistency.

hard cut to

(3-7s) she breaks into a sprint through shallow water, coat lifting behind her. Side tracking shot, slow then controlled acceleration. Overcast daylight, natural colors. Avoid temporal flicker, no distortion.

seamless morph into

(7-12s) she jumps onto a rooftop ledge and holds for one beat. Gentle push-in. Backlit sunset silhouette. Sharp clarity, stable picture.
```

- 샷마다 목적이 하나씩 보이게 쓰고
- 전환은 `hard cut to`, `seamless morph into`처럼 분명하게 적는 편이 좋습니다.

## @ 레퍼런스 시스템

AI 느낌이 덜 나는 결과는 대개 레퍼런스 역할을 명확하게 나눌 때 나옵니다. 파일이 많을수록 좋은 것이 아니라, 각 파일의 일이 분명할수록 좋습니다.

- `@Image1 = first frame`
- `@Image2 = last frame`
- `@Video1 = camera motion reference`
- `@Video2 = pacing reference`
- `@Audio1 = background music`
- `@Audio2 = voiceover`

레퍼런스를 여러 개 쓸 때는 파일마다 담당이 하나씩만 있게 두는 편이 안정적입니다.

## 바로 쓰는 템플릿

### 싱글샷

```text
[Subject]. [Action]. [Camera]. [Style]. [Constraints].
```

### 예시

```text
late 20s woman, tight dark curls at ear length, fitted black turtleneck, neutral expression. She slowly turns toward the camera, breeze lifting the edge of her coat. Gentle push-in, fixed eye-level framing. Golden hour rim light, cinematic film tone, 35mm. Avoid jitter, avoid identity drift, maintain face consistency, sharp clarity, natural colors.
```

### 멀티샷

```text
(0-3s) [Subject]. [Action]. [Camera]. [Style]. [Constraints].
hard cut to
(3-6s) [Subject]. [Action]. [Camera]. [Style]. [Constraints].
```

## 핵심만 남기면

- 주체와 카메라 움직임을 절대 한 문장 안에서 섞지 않습니다.
- 카메라 무브는 하나만 고르고, 속도는 `slow`, `gentle`, `controlled` 쪽에서 시작합니다.
- `cinematic` 같은 큰 단어보다 조명과 필름 질감을 먼저 구체화합니다.
- 제약 조건은 항상 마지막에 붙여 흔들림, 왜곡, 정체성 드리프트를 막습니다.
- 레퍼런스를 쓸 때는 파일마다 역할을 하나씩만 줍니다.

이 다섯 가지만 지켜도 같은 아이디어에서 나오는 결과 편차가 크게 줄어듭니다.
