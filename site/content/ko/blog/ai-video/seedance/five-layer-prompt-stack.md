---
title: "5층 프롬프트 스택"
description: "Seedance에서 slop을 줄이는 5층 프롬프트 구조, 카메라·조명 키워드, 제약 조건, 타임코드 멀티샷, @ 레퍼런스 시스템을 정리한 실전 가이드."
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

아이디어가 아무리 좋아도 Seedance의 프롬프팅 언어를 모르면 결과가 쉽게 slop으로 갑니다. 특히 이 모델은 `카메라`, `조명`, `모션`, `제약 조건`을 평범한 설명문이 아니라 촬영 언어처럼 읽는 편에 가깝습니다. 프롬프트 박스에 자연어 설명만 길게 넣으면, 주체는 흔들리고 카메라는 엉뚱하게 움직이고, 스타일은 덧칠만 된 채 끝나는 경우가 많습니다.

이 글은 설정이나 접근 권한보다 **프롬프팅 시스템 자체**에 집중합니다. 목적은 단순합니다. Seedance가 어떤 순서로 프롬프트를 읽는지, 어떤 단어가 실제로 잘 먹히는지, 무엇을 마지막에 제약으로 걸어야 흔들림과 정체성 드리프트를 줄일 수 있는지 한 번에 정리하는 것입니다.

## 왜 slop이 반복되는가

Seedance에서 결과가 흐려지는 가장 흔한 이유는 아이디어 부족이 아니라 **프롬프트 구조 부족**입니다.

- 주체 묘사가 추상적이면 얼굴과 실루엣이 쉽게 흐려집니다.
- 동작이 감정 설명으로 끝나면 비디오가 아니라 정적인 이미지처럼 나옵니다.
- 카메라와 피사체 움직임을 한 문장에 섞으면 모델이 누구를 움직여야 하는지 헷갈립니다.
- `cinematic`, `beautiful`, `epic` 같은 큰 단어만 쌓으면 분위기는 생겨도 샷 설계는 생기지 않습니다.
- 제약 조건이 없으면 jitter, flicker, bent limbs, identity drift가 바로 튀어나옵니다.

한마디로 말해, Seedance는 검색창처럼 대답하는 모델이 아니라 **촬영 지시를 읽는 모델**에 더 가깝습니다.

## 이 글이 다루는 범위

Seedance는 텍스트-to-비디오 박스라기보다 작은 멀티모달 영화 세트에 가깝습니다. 한 번의 생성 안에서 아래를 함께 넣을 수 있습니다.

- 최대 `9`개 이미지 레퍼런스
- 최대 `3`개 비디오 레퍼런스
- 최대 `3`개 오디오 레퍼런스
- 텍스트 프롬프트

이미지 레퍼런스는 캐릭터 시트, 무드보드, 제품 사진, 스토리보드 패널처럼 역할을 나눠 쓰는 편이 좋습니다. 비디오 레퍼런스는 카메라 무브, 안무, 페이싱을 고정하는 데 강하고, 오디오 레퍼런스는 음악, 보이스오버, 효과음 방향을 같이 잡을 때 유용합니다.

실전에서는 텍스트만 넣는 것보다 `@Image`, `@Video`, `@Audio`에 역할을 분명하게 주는 편이 훨씬 안정적입니다. 텍스트만 쓰고 있다면 이 시스템의 일부만 쓰는 셈입니다.

## 기본 구조

```text
Subject -> Action -> Camera -> Style -> Constraints
```

공식 문서 쪽에서는 더 넓은 공식이 보이기도 하지만, 커뮤니티 테스트 기준으로는 위 5층 구조가 더 일관되게 잘 맞는 경우가 많습니다. 순서가 중요한 이유도 분명합니다.

- `Subject`가 먼저 있어야 모델이 누구를 붙잡아야 하는지 흔들리지 않습니다.
- `Action`이 둘째여야 정적인 사진이 아니라 움직이는 샷으로 해석됩니다.
- `Camera`는 그 다음에 두어 프레임과 시점을 잠급니다.
- `Style`은 마지막에 가까울수록 분위기를 더하되 모션을 덜 방해합니다.
- `Constraints`는 끝에 두어 남는 문제를 가드레일처럼 막습니다.

이 다섯 층을 섞지 않고 순서대로 쌓는 것만으로도 결과 편차가 크게 줄어듭니다.

## 1. Subject

주체는 추상적일수록 쉽게 흐려집니다. 짧더라도 디테일이 있는 쪽이 훨씬 낫습니다.

```text
Bad: a woman
Good: a young woman with brown hair
Best: late 20s woman, tight dark curls at ear length, small silver hoop in left ear, fitted black turtleneck, neutral expression
```

- 한 생성당 한 명의 주체가 가장 안전합니다.
- 두 명까지는 공간을 분리하고 `@Character_A`, `@Character_B`처럼 태그를 분명히 나누면 버틸 수 있습니다.
- 세 명 이상부터는 주체 간섭과 정체성 붕괴가 급격히 늘어나는 편입니다.
- 캐릭터 일관성이 중요한 샷은 얼굴, 헤어, 의상, 표정 중 최소 두세 가지를 같이 적는 편이 좋습니다.

Subject의 핵심은 시적인 표현이 아니라 **시각적으로 다시 잡을 수 있는 앵커**를 남기는 것입니다.

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
- 한 샷에는 주요 움직임 하나만 두는 편이 좋습니다.
- `turns`, `walks`, `sprints`, `leans`, `reaches`, `jumps`처럼 화면에서 보이는 동사를 우선합니다.

이 분리만 지켜도 샷 해석이 훨씬 안정됩니다.

## 3. Camera

Seedance에서 가장 차이를 크게 만드는 층입니다. 한 생성당 하나의 주요 카메라 움직임만 두는 편이 좋고, 기술 스펙보다 **리듬, 방향, 안정성**을 적는 편이 더 잘 먹힙니다.

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

추가로 기억할 점은 단순합니다.

- `f-stop`, `ISO`, `mm` 같은 카메라 스펙보다 `slow`, `controlled`, `fixed framing` 같은 촬영 감각이 더 잘 먹힙니다.
- `handheld`는 긴장감은 좋지만 흔들림도 같이 올라오므로 제약 조건을 같이 두는 편이 안전합니다.
- `whip pan`, `dynamic`, `swift`는 강한 맛이 있지만 실패하면 바로 어수선해집니다.

## 4. Style

Style은 분위기보다 먼저 조명을 잡는 게 핵심입니다. Seedance에서는 조명이 프레임 전체 품질에 미치는 영향이 큽니다. `cinematic` 하나만 쓰면 너무 넓어서 효과가 약하고, 조명, 컬러, 필름 질감을 같이 적는 편이 훨씬 낫습니다.

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

Style의 핵심은 장식이 아니라 **빛의 방향과 질감**입니다.

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

Constraints는 문장 중간보다 맨 끝에 두는 편이 깔끔합니다. 인물 프롬프트라면 `avoid bent limbs`와 `maintain face consistency`는 거의 기본값처럼 붙이는 편이 안전합니다.

## 타임코드 멀티샷

15초 안에서 여러 샷을 지시할 때는 타임코드가 가장 깔끔합니다. 이것이 Seedance의 강점이기도 합니다. 각 구간마다 주체, 동작, 카메라, 조명을 함께 적고 전환 방식도 같이 적습니다.

```text
(0-3s) late 20s woman, tight dark curls, black turtleneck. She stands still, then slowly turns toward camera. Fixed framing. Golden hour rim light. Avoid jitter, maintain face consistency.

hard cut to

(3-7s) she breaks into a sprint through shallow water, coat lifting behind her. Side tracking shot, slow then controlled acceleration. Overcast daylight, natural colors. Avoid temporal flicker, no distortion.

seamless morph into

(7-12s) she jumps onto a rooftop ledge and holds for one beat. Gentle push-in. Backlit sunset silhouette. Sharp clarity, stable picture.
```

- 샷마다 목적이 하나씩 보이게 쓰고
- 전환은 `hard cut to`, `seamless morph into`처럼 분명하게 적는 편이 좋습니다.
- 각 샷마다 카메라 상태와 조명 상태를 다시 적는 편이 안정적입니다.
- 여러 움직임을 한 샷에 우겨 넣기보다 2~4초 단위로 역할을 쪼개는 편이 낫습니다.

## @ 레퍼런스 시스템

AI 느낌이 덜 나는 결과는 대개 레퍼런스 역할을 명확하게 나눌 때 나옵니다. 파일이 많을수록 좋은 것이 아니라, 각 파일의 일이 분명할수록 좋습니다. 실전에서는 6~12개 레퍼런스를 쓰되, 각 파일이 담당하는 역할을 겹치지 않게 두는 편이 안정적입니다.

- `@Image1 = first frame`
- `@Image2 = last frame`
- `@Video1 = camera motion reference`
- `@Video2 = pacing reference`
- `@Audio1 = background music`
- `@Audio2 = voiceover`

레퍼런스를 여러 개 쓸 때는 파일마다 담당이 하나씩만 있게 두는 편이 좋습니다.

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

## 빠르게 점검하는 체크리스트

- 주체가 한 문장 안에서 충분히 구체적인가
- 동작이 감정이 아니라 실제 움직임으로 쓰였는가
- 카메라 움직임이 하나만 남아 있는가
- 스타일이 `cinematic` 같은 큰 단어가 아니라 조명과 질감으로 적혔는가
- 제약 조건이 마지막에 붙어 있는가
- 레퍼런스가 있다면 각 파일의 역할이 하나씩만 정해져 있는가

## 핵심만 남기면

- 주체와 카메라 움직임을 절대 한 문장 안에서 섞지 않습니다.
- 카메라 무브는 하나만 고르고, 속도는 `slow`, `gentle`, `controlled` 쪽에서 시작합니다.
- `cinematic` 같은 큰 단어보다 조명과 필름 질감을 먼저 구체화합니다.
- 제약 조건은 항상 마지막에 붙여 흔들림, 왜곡, 정체성 드리프트를 막습니다.
- 레퍼런스를 쓸 때는 파일마다 역할을 하나씩만 줍니다.

이 다섯 가지만 지켜도 같은 아이디어에서 나오는 결과 편차가 크게 줄어듭니다. Seedance는 마법 문장을 찾는 모델이 아니라, **촬영 구조를 얼마나 명확하게 지시하느냐**에 반응하는 모델입니다. 그래서 이 글의 핵심은 복잡한 수사보다도, `Subject -> Action -> Camera -> Style -> Constraints` 순서를 끝까지 지키는 데 있습니다.
