---
title: "렌즈와 심도"
description: "초점 거리와 심도 표현을 실제 사진 레퍼런스로 정리한 AI 영상 프롬프트 용어집입니다."
publish: true
draft: false
lang: "ko"
translationKey: "ai-video-lens-depth"
tags:
  - blog
  - ko
  - ai-video
  - lens-depth
---

# 렌즈와 심도

이 페이지는 **실제 사진 레퍼런스**로 다시 정리했습니다.  
초점 거리 비교가 중요한 24mm, 35mm, 50mm는 같은 테스트 장면 계열을 사용해 시야 차이를 보기 쉽게 맞췄고, `rack focus`처럼 시간에 따라 변하는 용어는 **정지 이미지에서 보여줄 수 있는 핵심인 초점면 분리**를 중심으로 설명합니다.

## 24mm wide lens

24mm는 넓은 공간을 한 번에 담기 좋고, 가까운 전경과 먼 배경의 거리감이 크게 느껴집니다.

![24mm reference](https://commons.wikimedia.org/wiki/Special:FilePath/Focal_length_f24mm.jpg?width=1100)

- 프롬프트 조각: `24mm wide lens, expanded environment, strong spatial depth`
- 실제 레퍼런스: [Focal length f24mm.jpg](https://commons.wikimedia.org/wiki/File:Focal_length_f24mm.jpg)

## 35mm lens

35mm는 공간감과 인물 비중의 균형이 좋아서 가장 영화적으로 느껴지는 범용 구간 중 하나입니다.

![35mm reference](https://commons.wikimedia.org/wiki/Special:FilePath/Focal_length_f35mm.jpg?width=1100)

- 프롬프트 조각: `35mm lens, natural cinematic perspective, balanced framing`
- 실제 레퍼런스: [Focal length f35mm.jpg](https://commons.wikimedia.org/wiki/File:Focal_length_f35mm.jpg)

## 50mm lens

50mm는 과장되지 않은 자연스러운 시야를 만들기 좋아서 인물과 사물을 무난하게 담을 때 자주 쓰입니다.

![50mm reference](https://commons.wikimedia.org/wiki/Special:FilePath/Focal_length_f50mm.jpg?width=1100)

- 프롬프트 조각: `50mm lens, natural perspective, neutral subject-to-background balance`
- 실제 레퍼런스: [Focal length f50mm.jpg](https://commons.wikimedia.org/wiki/File:Focal_length_f50mm.jpg)

## 85mm portrait lens

85mm 계열은 배경을 더 눌러 보이게 하고 인물 분리를 강하게 만드는 전형적인 포트레이트 구간입니다.

![85mm portrait reference](https://commons.wikimedia.org/wiki/Special:FilePath/Elegant_woman_by_storefront_(Unsplash).jpg?width=1100)

- 프롬프트 조각: `85mm portrait lens, compressed background, clean subject separation`
- 실제 레퍼런스: [Elegant woman by storefront (Unsplash)](https://commons.wikimedia.org/wiki/File:Elegant_woman_by_storefront_(Unsplash).jpg)

## shallow depth of field

얕은 심도는 피사체만 또렷하게 두고 배경을 흐리게 만들어 시선을 한 지점으로 밀어붙입니다.

![shallow depth of field reference](https://commons.wikimedia.org/wiki/Special:FilePath/Depth-of-field-comparison-side-by-side-small.png?width=1200)

- 프롬프트 조각: `shallow depth of field, creamy background blur, subject isolated`
- 실제 레퍼런스: [Depth-of-field-comparison-side-by-side-small.png](https://commons.wikimedia.org/wiki/File:Depth-of-field-comparison-side-by-side-small.png)

## deep focus

깊은 심도는 앞과 뒤를 함께 읽히게 만들어 공간 정보가 많은 장면, 동선이 중요한 장면에 유리합니다.

![deep focus reference](https://commons.wikimedia.org/wiki/Special:FilePath/Depth-of-field-comparison-side-by-side-small.png?width=1200)

- 프롬프트 조각: `deep focus, foreground and background both sharp, spatial clarity`
- 실제 레퍼런스: [Depth-of-field-comparison-side-by-side-small.png](https://commons.wikimedia.org/wiki/File:Depth-of-field-comparison-side-by-side-small.png)

## anamorphic lens look

아나모픽 룩은 수평 플레어, 넓은 화면감, 약간의 타원형 보케 같은 영화적 인상을 강조할 때 자주 언급됩니다.

![anamorphic lens look reference](https://commons.wikimedia.org/wiki/Special:FilePath/Lens_Flare_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `anamorphic lens look, horizontal flare, cinematic widescreen mood`
- 실제 레퍼런스: [Lens Flare (Unsplash)](https://commons.wikimedia.org/wiki/File:Lens_Flare_(Unsplash).jpg)

## rack focus

`rack focus`는 초점이 앞대상에서 뒤대상으로, 혹은 반대로 이동하는 연출입니다. 정지 이미지에서는 이동 자체보다 **어느 평면이 선명하고 어느 평면이 흐려지는지**를 먼저 보는 게 핵심입니다.

![rack focus reference](https://commons.wikimedia.org/wiki/Special:FilePath/Depth-of-field-comparison-side-by-side-small.png?width=1200)

- 프롬프트 조각: `rack focus from foreground object to background subject`
- 실제 레퍼런스: [Depth-of-field-comparison-side-by-side-small.png](https://commons.wikimedia.org/wiki/File:Depth-of-field-comparison-side-by-side-small.png)

## 정리

렌즈와 심도는 보통 같이 묶여야 효과가 납니다.

- 더 넓고 공간감 있는 장면: `24mm + deep focus`
- 균형 잡힌 영화 톤: `35mm + moderate background separation`
- 자연스러운 인물/사물 중심: `50mm + shallow depth of field`
- 인물 강조 포트레이트: `85mm + strong subject isolation`

프롬프트에서 렌즈와 심도를 같이 쓰면 결과가 훨씬 안정적입니다.
