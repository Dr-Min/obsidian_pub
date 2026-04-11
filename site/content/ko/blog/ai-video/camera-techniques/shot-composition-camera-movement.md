---
title: "AI 영상 프롬프트에서 화면 구도와 카메라 움직임을 설명하는 법"
description: "와이드샷, 미디엄샷, 클로즈업, 렌즈, 카메라 무브를 어떻게 문장으로 조합해야 AI 영상 결과가 더 안정적으로 나오는지 정리한 실전 가이드."
date: 2026-04-10
modified: 2026-04-10
draft: false
publish: true
lang: "ko"
translationKey: "shot-composition-camera-movement"
tags:
  - blog
  - ko
  - ai-video
  - camera-techniques
  - shot-design
aliases:
  - "AI 영상 프롬프트 구도 가이드"
---

# AI 영상 프롬프트에서 화면 구도와 카메라 움직임을 설명하는 법

AI 영상 모델은 "예쁜 영상"이라는 막연한 표현보다, **무엇을 어떤 거리에서 어떤 방식으로 찍는지**를 명확하게 적었을 때 훨씬 안정적으로 반응합니다. 특히 사람을 중심으로 한 장면에서는 `샷 크기`, `카메라 각도`, `렌즈 느낌`, `움직임`, `조명`, `장면 분위기`가 동시에 정리돼야 결과물이 덜 흔들립니다.

아래 다이어그램은 가장 기본적인 샷 스케일입니다.

![샷 스케일 레퍼런스](../../../../assets/shot-scale-reference.svg)

## 왜 구도 설명이 중요한가

같은 피사체라도 프롬프트가 다르면 결과 해석이 완전히 달라집니다.

- `a woman in a cafe`는 피사체와 장소만 전달합니다
- `medium shot of a woman in a cafe, 50mm lens, shallow depth of field`는 프레임 거리와 렌즈 감각까지 전달합니다
- `slow push-in close-up, warm window light, intimate cinematic mood`는 움직임과 감정선까지 전달합니다

즉, AI 영상 프롬프트는 단순 묘사가 아니라 **촬영 지시서처럼 써야** 합니다.

## 먼저 잡아야 할 5가지 요소

프롬프트를 만들 때는 아래 순서로 생각하면 편합니다.

1. **피사체**: 누가, 무엇을 하고 있는가
2. **샷 크기**: 와이드, 미디엄, 클로즈업 중 무엇인가
3. **시점과 렌즈**: eye-level, low angle, overhead / 24mm, 50mm, 85mm
4. **카메라 움직임**: static, pan, tilt, dolly in, tracking shot, handheld
5. **조명과 분위기**: soft morning light, neon backlight, foggy blue atmosphere

이 다섯 가지가 빠지면 결과가 예측 불가능해집니다.

## 샷 크기를 문장으로 바꾸는 법

### 1. 와이드 샷

와이드 샷은 환경 정보를 주는 데 유리합니다. 장소, 규모감, 인물과 배경의 관계를 보여주고 싶을 때 씁니다.

예시 표현:

- `wide shot of a lone director standing on a rain-soaked rooftop`
- `establishing shot of a small film crew in a narrow alley`
- `full-body wide frame with dramatic skyline in the background`

와이드 샷은 배경이 중요하므로, 장소 묘사를 한 줄 더 붙이는 편이 좋습니다.

### 2. 미디엄 샷

미디엄 샷은 가장 실용적입니다. 손동작, 표정, 몸의 제스처를 동시에 보여주기 좋습니다.

예시 표현:

- `medium shot of a creator adjusting a camera rig`
- `waist-up framing, confident posture, direct eye line`
- `medium tracking shot as the subject walks through a studio set`

제품 시연, 설명형 콘텐츠, 인터뷰형 장면은 대부분 미디엄 샷에서 안정적으로 나옵니다.

### 3. 클로즈업

감정, 질감, 디테일 강조에 좋습니다. 하지만 장면 정보가 부족하면 결과가 답답해질 수 있어 배경 분위기를 짧게라도 넣는 게 좋습니다.

예시 표현:

- `close-up of focused eyes reflecting monitor light`
- `tight close-up on hands turning the focus ring`
- `slow push-in close-up, subtle emotional tension`

## 카메라 움직임은 한 번에 하나만

초보자가 가장 많이 하는 실수는 움직임을 여러 개 섞는 것입니다.

나쁜 예:

`drone shot, dolly in, handheld, spinning camera, fast zoom, cinematic`

이렇게 쓰면 모델이 무엇을 우선해야 할지 모릅니다.

좋은 예:

- `slow dolly in`
- `smooth left-to-right tracking shot`
- `locked-off tripod shot`
- `gentle handheld sway`

먼저 **하나의 핵심 움직임**을 정하고, 필요하면 속도나 질감만 추가하세요.

## 렌즈 표현을 함께 쓰면 결과가 안정적이다

렌즈는 꼭 숫자를 써야 하는 건 아니지만, 쓰면 결과가 더 일관적입니다.

| 목적 | 추천 표현 | 느낌 |
| --- | --- | --- |
| 장소를 넓게 보여주기 | `24mm wide lens` | 공간감, 왜곡, 역동성 |
| 자연스러운 인물 컷 | `50mm lens` | 밸런스 좋고 무난함 |
| 감정 강조 인물 클로즈업 | `85mm portrait lens` | 배경 압축, 피사체 분리 |

실전에서는 아래처럼 조합하면 됩니다.

`medium close-up, 85mm portrait lens, soft backlight, slow push-in`

## 가장 실전적인 프롬프트 공식

아래 공식 하나만 익혀도 초안 품질이 많이 올라갑니다.

```text
[피사체] + [행동] + [샷 크기] + [카메라 각도] + [렌즈] + [카메라 움직임] + [조명] + [배경 분위기] + [텍스처/품질]
```

예시:

```text
A fashion director reviewing a storyboard wall, medium shot, eye-level angle, 50mm lens, slow lateral tracking shot, soft daylight from large studio windows, minimal industrial set, cinematic realism, fine fabric detail, subtle depth of field
```

## 바로 써먹는 프롬프트 5개

### 인터뷰 스타일

```text
A founder speaking calmly in a creative studio, medium shot, eye-level angle, 50mm lens, locked-off tripod shot, soft key light with gentle shadow falloff, modern workspace in the background, clean documentary look
```

### 제품 시연 스타일

```text
Hands demonstrating a compact cinema camera, close-up, slight top-down angle, 85mm macro feel, slow push-in, crisp controlled studio lighting, matte black tabletop, premium commercial texture
```

### 영화 예고편 스타일

```text
A lone character stepping into a foggy warehouse, wide shot, low angle, 24mm lens, slow forward dolly, cold blue backlight, floating dust, dramatic cinematic scale
```

### 브이로그 스타일

```text
A creator entering a neon-lit editing room, medium handheld shot, eye-level, 35mm lens, gentle natural handheld motion, practical monitor light and magenta accent glow, energetic but grounded mood
```

### 감정 강조 컷

```text
Close-up of a director pausing before the shoot begins, eye-level, 85mm lens, subtle push-in, soft side light, shallow depth of field, quiet tension, cinematic realism
```

## 자주 망하는 패턴

- **형용사만 많고 촬영 정보가 없음**
  `beautiful cinematic masterpiece`는 거의 도움이 안 됩니다.
- **샷 크기와 움직임이 충돌함**
  `extreme close-up drone shot`처럼 물리적으로 어색한 조합은 피하세요.
- **조명이 너무 추상적임**
  `nice lighting`보다 `warm sunset rim light`가 훨씬 낫습니다.
- **장면 목적이 없음**
  감정 강조 컷인지, 장소 소개 컷인지, 제품 디테일 컷인지 먼저 정해야 합니다.

## 이미지와 영상 레퍼런스도 넣을 수 있다

이 사이트 구조에서는 글 안에 이미지와 영상 레퍼런스를 같이 넣을 수 있습니다.

이미지 파일:

```md
![[ko/blog/media/reference-board.jpg|1200]]
```

로컬 영상 파일:

```md
![[ko/blog/media/camera-move-demo.mp4]]
```

유튜브 임베드:

```md
![](https://www.youtube.com/watch?v=VIDEO_ID)
```

즉, 글을 단순 텍스트로만 쓰는 게 아니라 **레퍼런스 보드 + 예시 프롬프트 + 영상 데모**가 한 페이지 안에 함께 들어갈 수 있습니다.

## 결론

AI 영상 프롬프트에서 구도 설명은 옵션이 아니라 핵심입니다. 모델은 결국 장면을 카메라 언어로 해석하기 때문에, 피사체 설명만으로는 안정적인 결과를 기대하기 어렵습니다.

가장 먼저 해야 할 일은 복잡한 문장을 늘리는 게 아니라, 아래 네 줄을 습관처럼 붙이는 것입니다.

- 샷 크기
- 카메라 각도
- 렌즈 느낌
- 움직임

이 네 가지가 들어가면 결과물의 일관성이 눈에 띄게 올라갑니다.
