---
title: "렌즈와 심도"
description: "초점 거리와 심도 표현을 실제 사진 레퍼런스로 다시 정리한 AI 영상 프롬프트 용어집입니다."
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
24mm, 35mm, 50mm 예시는 화각 차이를 비교하기 쉽도록 비슷한 테스트 장면을 유지했고, 심도와 초점 용어는 다른 레퍼런스로 분리해서 같은 표시 이미지를 반복하지 않도록 정리했습니다.

## 24mm wide lens

24mm는 넓은 화각을 담고, 앞과 뒤의 공간 거리를 더 크게 느끼게 합니다. 장소와 환경이 중요할 때 좋습니다.

![24mm reference](https://commons.wikimedia.org/wiki/Special:FilePath/Focal_length_f24mm.jpg?width=1100)

- 프롬프트 조각: `24mm wide lens, expanded environment, strong spatial depth`
- 실제 레퍼런스: [Focal length f24mm.jpg](https://commons.wikimedia.org/wiki/File%3AFocal_length_f24mm.jpg)

## 35mm lens

35mm는 환경 정보와 피사체 강조 사이의 균형이 좋아서 가장 영화적으로 무난한 기본값 중 하나입니다.

![35mm reference](https://commons.wikimedia.org/wiki/Special:FilePath/Focal_length_f35mm.jpg?width=1100)

- 프롬프트 조각: `35mm lens, natural cinematic perspective, balanced framing`
- 실제 레퍼런스: [Focal length f35mm.jpg](https://commons.wikimedia.org/wiki/File%3AFocal_length_f35mm.jpg)

## 50mm lens

50mm는 과장되지 않고 자연스러운 시야를 만들기 좋습니다. 피사체를 강조하면서도 너무 넓거나 너무 압축되지 않습니다.

![50mm reference](https://commons.wikimedia.org/wiki/Special:FilePath/Focal_length_f50mm.jpg?width=1100)

- 프롬프트 조각: `50mm lens, natural perspective, neutral subject-to-background balance`
- 실제 레퍼런스: [Focal length f50mm.jpg](https://commons.wikimedia.org/wiki/File%3AFocal_length_f50mm.jpg)

## 85mm portrait lens

85mm 영역은 배경 압축이 더 강하고 얼굴과 상반신 분리가 깔끔하게 나와서 인물 중심 장면에 좋습니다.

![85mm portrait reference](https://commons.wikimedia.org/wiki/Special:FilePath/Elegant_woman_by_storefront_(Unsplash).jpg?width=1100)

- 프롬프트 조각: `85mm portrait lens, compressed background, clean subject separation`
- 실제 레퍼런스: [Elegant woman by storefront (Unsplash)](https://commons.wikimedia.org/wiki/File%3AElegant_woman_by_storefront_%28Unsplash%29.jpg)

## shallow depth of field

얕은 심도는 피사체만 선명하게 두고 배경을 흐리게 밀어내는 방식입니다. 시선을 한 지점에 고정하는 데 매우 빠르게 먹힙니다.

![[assets/ai-video/shot-composition-photos/close-up.jpg|1200]]

- 프롬프트 조각: `shallow depth of field, creamy background blur, subject isolated`
- 실제 레퍼런스: [Face portrait (Unsplash)](https://commons.wikimedia.org/wiki/File%3AFace_portrait_%28Unsplash%29.jpg), `CC0`, 크롭

## deep focus

깊은 심도는 앞과 뒤를 동시에 읽히게 만듭니다. 공간 구조, 동선, 레이어가 중요한 장면에 잘 맞습니다.

![deep focus reference](https://commons.wikimedia.org/wiki/Special:FilePath/Vilnius%20Modern%20Skyline%20At%20Dusk%2C%20Lithuania%20-%20Diliff.jpg?width=1200)

- 프롬프트 조각: `deep focus, foreground and background both sharp, spatial clarity`
- 실제 레퍼런스: [Vilnius Modern Skyline At Dusk, Lithuania - Diliff.jpg](https://commons.wikimedia.org/wiki/File%3AVilnius%20Modern%20Skyline%20At%20Dusk%2C%20Lithuania%20-%20Diliff.jpg)

## anamorphic lens look

아나모픽 룩은 수평 플레어, 넓은 영화 화면 느낌, 스타일화된 스크린 존재감을 함께 떠올리게 합니다.

![anamorphic lens look reference](https://commons.wikimedia.org/wiki/Special:FilePath/Lens_Flare_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `anamorphic lens look, horizontal flare, cinematic widescreen mood`
- 실제 레퍼런스: [Lens Flare (Unsplash)](https://commons.wikimedia.org/wiki/File%3ALens_Flare_%28Unsplash%29.jpg)

## rack focus

`rack focus`는 선명한 초점을 한 피사체 평면에서 다른 평면으로 옮기는 연출입니다. 정지 이미지는 시간 변화 자체를 보여주진 못하지만, 이 무브가 의존하는 앞쪽과 뒤쪽의 초점 분리를 잘 보여줍니다.

![rack focus reference](https://commons.wikimedia.org/wiki/Special:FilePath/Depth-of-field-comparison-side-by-side-small.png?width=1200)

- 프롬프트 조각: `rack focus from foreground object to background subject`
- 실제 레퍼런스: [Depth-of-field-comparison-side-by-side-small.png](https://commons.wikimedia.org/wiki/File%3ADepth-of-field-comparison-side-by-side-small.png)

## 정리

렌즈와 심도는 같이 묶어 써야 결과가 안정적입니다.

- 넓은 공간과 장소감: `24mm + deep focus`
- 영화적인 기본 밸런스: `35mm + moderate background separation`
- 자연스러운 피사체 강조: `50mm + shallow depth of field`
- 인물 중심 초상 느낌: `85mm + strong subject isolation`

프롬프트에서 렌즈만 말하는 것보다 심도까지 같이 적는 편이 훨씬 예측 가능하게 나옵니다.
