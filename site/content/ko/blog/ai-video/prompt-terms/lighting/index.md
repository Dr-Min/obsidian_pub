---
title: "조명"
description: "AI 영상 프롬프트용 조명 용어를 실제 사진 레퍼런스로 다시 정리한 페이지입니다."
publish: true
draft: false
lang: "ko"
translationKey: "ai-video-lighting"
tags:
  - blog
  - ko
  - ai-video
  - lighting
---

# 조명

이 페이지는 **실제 사진 레퍼런스**로 다시 정리했습니다.  
조명 용어는 이름 자체보다도 **빛이 어디서 들어오는지**, **얼마나 부드럽거나 거친지**, **피사체와 배경을 어떻게 분리하는지**를 보는 것이 중요합니다.

## soft light

소프트 라이트는 하이라이트와 그림자 사이의 경계가 부드럽게 이어집니다. 피부와 표면 질감이 더 매끈하고 온화하게 보입니다.

![[assets/ai-video/lighting-crops/soft-light.jpg|1200]]

- 프롬프트 조각: `soft light, gentle shadow falloff, flattering skin texture`
- 실제 레퍼런스: [Comparison of softbox to direct flash.jpg](https://commons.wikimedia.org/wiki/File%3AComparison_of_softbox_to_direct_flash.jpg), 소프트 라이트 쪽 크롭

## hard light

하드 라이트는 그림자 경계가 또렷하고 명암 대비가 강합니다. 드라마, 질감, 날카로운 분위기를 만들 때 효과적입니다.

![[assets/ai-video/lighting-crops/hard-light.jpg|1200]]

- 프롬프트 조각: `hard light, crisp shadow edge, high-contrast texture`
- 실제 레퍼런스: [Comparison of softbox to direct flash.jpg](https://commons.wikimedia.org/wiki/File%3AComparison_of_softbox_to_direct_flash.jpg), 직접광 쪽 크롭

## rim light

림 라이트는 피사체 가장자리에 빛이 걸리면서 실루엣 테두리를 만들어주는 방식입니다. 머리카락과 어깨 분리에 특히 좋습니다.

![rim light reference](https://commons.wikimedia.org/wiki/Special:FilePath/Backlight_(50709183452).jpg?width=1100)

- 프롬프트 조각: `rim light catching the hairline, subject edge glow`
- 실제 레퍼런스: [Backlight (50709183452).jpg](https://commons.wikimedia.org/wiki/File%3ABacklight_%2850709183452%29.jpg)

## backlight

백라이트는 빛이 피사체 뒤에서 들어오는 구도입니다. 실루엣, 분리감, 분위기를 강하게 만들 수 있습니다.

![backlight reference](https://commons.wikimedia.org/wiki/Special:FilePath/Backlight-wedding.jpg?width=1100)

- 프롬프트 조각: `strong backlight, semi-silhouette portrait, luminous edge separation`
- 실제 레퍼런스: [Backlight-wedding.jpg](https://commons.wikimedia.org/wiki/File%3ABacklight-wedding.jpg)

## key light

키 라이트는 얼굴이나 피사체 형태를 가장 강하게 결정하는 메인 광원입니다. 어느 방향이 주광인지가 여기서 정해집니다.

![key light reference](https://commons.wikimedia.org/wiki/Special:FilePath/Emma%20%288640086553%29.jpg?width=1200)

- 프롬프트 조각: `key light from camera right, portrait light defining the face`
- 실제 레퍼런스: [Emma (8640086553).jpg](https://commons.wikimedia.org/wiki/File%3AEmma%20%288640086553%29.jpg)

## fill light

필 라이트는 키 라이트를 대신하는 빛이 아니라, 너무 깊어진 그림자를 적당히 열어주는 보조광입니다.

![fill light reference](https://commons.wikimedia.org/wiki/Special:FilePath/Juliet%20in%20the%20studio%20-%20Flickr%20-%20Jay%20DeFehr.jpg?width=1200)

- 프롬프트 조각: `subtle fill light, controlled shadow recovery, balanced contrast`
- 실제 레퍼런스: [Juliet in the studio - Flickr - Jay DeFehr.jpg](https://commons.wikimedia.org/wiki/File%3AJuliet%20in%20the%20studio%20-%20Flickr%20-%20Jay%20DeFehr.jpg)

## practical lighting

프랙티컬 라이팅은 램프, 전구, 화면 안 소품처럼 장면 안에 실제 광원이 보이는 조명 방식입니다.

![practical lighting reference](https://commons.wikimedia.org/wiki/Special:FilePath/Floor_lamp_near_a_wall_(Unsplash).jpg?width=1000)

- 프롬프트 조각: `practical lighting from a floor lamp, cozy interior glow`
- 실제 레퍼런스: [Floor lamp near a wall (Unsplash)](https://commons.wikimedia.org/wiki/File%3AFloor_lamp_near_a_wall_%28Unsplash%29.jpg)

## neon glow

네온 글로우는 색광 반사와 인공적인 야간 분위기를 빠르게 만들어줍니다. 도시 밤 장면에서 특히 자주 씁니다.

![neon glow reference](https://commons.wikimedia.org/wiki/Special:FilePath/Red_and_blue_open_neon_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `red and blue neon glow, reflective surfaces, cyberpunk night mood`
- 실제 레퍼런스: [Red and blue open neon (Unsplash)](https://commons.wikimedia.org/wiki/File%3ARed_and_blue_open_neon_%28Unsplash%29.jpg)

## golden hour

골든아워는 해 질 무렵의 따뜻하고 낮은 각도의 빛입니다. 피부 표현이 부드럽고 로맨틱한 분위기를 만들기 좋습니다.

![golden hour reference](https://commons.wikimedia.org/wiki/Special:FilePath/Golden_Hour_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `golden hour sunlight, warm rim highlights, soft sunset atmosphere`
- 실제 레퍼런스: [Golden Hour (Unsplash)](https://commons.wikimedia.org/wiki/File%3AGolden_Hour_%28Unsplash%29.jpg)

## blue hour

블루아워는 해가 진 직후의 차갑고 푸른 주변광입니다. 도시 스카이라인, 물가, 반사 많은 야경과 잘 맞습니다.

![blue hour reference](https://commons.wikimedia.org/wiki/Special:FilePath/Blue_Hour_(196206709).jpeg?width=1200)

- 프롬프트 조각: `blue hour skyline, cool ambient light, calm evening tone`
- 실제 레퍼런스: [Blue Hour (196206709).jpeg](https://commons.wikimedia.org/wiki/File%3ABlue_Hour_%28196206709%29.jpeg)

## volumetric light

볼류메트릭 라이트는 빛줄기가 공기 중에 보이는 상태를 말합니다. 안개, 먼지, 습기가 있을수록 더 뚜렷합니다.

![volumetric light reference](https://commons.wikimedia.org/wiki/Special:FilePath/Sunrays_through_the_trees_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `volumetric light beams, visible sun rays through haze`
- 실제 레퍼런스: [Sunrays through the trees (Unsplash)](https://commons.wikimedia.org/wiki/File%3ASunrays_through_the_trees_%28Unsplash%29.jpg)

## 정리

조명 용어는 하나씩보다 조합으로 쓸 때 훨씬 강합니다.

- 예쁜 상업 인물 톤: `soft light + key light + subtle fill`
- 실루엣과 분리감: `backlight + rim light`
- 도시형 인공 야간 톤: `neon glow + hard light`
- 시간대 기반 자연광 분위기: `golden hour` 또는 `blue hour`

AI 영상 프롬프트에서는 조명이 분위기와 색감을 동시에 바꾸는 가장 빠른 레버입니다.
