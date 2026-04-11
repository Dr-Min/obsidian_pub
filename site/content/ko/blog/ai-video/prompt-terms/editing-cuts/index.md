---
title: "편집과 컷 구성"
description: "짧은 AI 영상 시퀀스를 컷, 비트, 전환으로 설계할 때 쓰는 용어를 실제 사진 레퍼런스로 정리한 페이지입니다."
publish: true
draft: false
lang: "ko"
translationKey: "ai-video-editing-cuts"
tags:
  - blog
  - ko
  - ai-video
  - editing-cuts
---

# 편집과 컷 구성

AI 영상은 한 장면으로 끝내는 것보다 여러 비트로 나누었을 때 훨씬 강해집니다. 컷 구조 용어는 짧은 시퀀스에 리듬과 상승 구조를 줍니다.

이 페이지는 더 이상 SVG 도식 이미지를 쓰지 않습니다. 지금 보이는 예시는 **실제 사진을 조합한 레퍼런스 보드**와, 한 장으로 충분한 경우의 실제 사진 레퍼런스로 구성되어 있습니다.

## Cut 1 / Cut 2

가장 기본적인 방식은 장면을 순서 있는 비트로 나누는 것입니다. 핵심은 각 컷이 예쁜지보다, 다음 컷이 무엇을 더 강조하는지입니다.

![[assets/ai-video/editing-cuts-photos/cut-1-cut-2.jpg|1400]]

- 프롬프트 조각: `Cut 1 wide establishing frame, Cut 2 close-up emotional emphasis`
- 실제 레퍼런스 보드: [Man standing in court (Unsplash)](https://commons.wikimedia.org/wiki/File%3AMan_standing_in_court_%28Unsplash%29.jpg) + [Face portrait (Unsplash)](https://commons.wikimedia.org/wiki/File%3AFace_portrait_%28Unsplash%29.jpg), 둘 다 `CC0`

## setup

세트업은 상황, 공간, 인물의 기본 규칙을 처음 소개하는 도입 비트입니다.

![[assets/ai-video/shot-composition-photos/wide-shot.jpg|1400]]

- 프롬프트 조각: `Cut 1 setup, wide establishing frame, subject small inside the environment`
- 실제 레퍼런스: [Man standing in court (Unsplash)](https://commons.wikimedia.org/wiki/File%3AMan_standing_in_court_%28Unsplash%29.jpg), `CC0`, 크롭

## escalation

에스컬레이션은 움직임, 긴장, 규모가 올라가기 시작하는 비트입니다. 소개에서 끝나지 않고 시퀀스가 가속되기 시작하는 지점입니다.

![escalation reference](https://commons.wikimedia.org/wiki/Special:FilePath/Woman_running.jpg?width=1200)

- 프롬프트 조각: `Cut 2 escalation, faster movement, rising urgency`
- 실제 레퍼런스: [Woman running](https://commons.wikimedia.org/wiki/File%3AWoman_running.jpg)

## climax

클라이맥스는 시퀀스에서 시각적이거나 감정적인 강도가 가장 높아지는 정점입니다.

![climax reference](<https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/New_York_City_night_skyline_by_500px_1.jpg/1280px-New_York_City_night_skyline_by_500px_1.jpg>)

- 프롬프트 조각: `Cut 3 climax, epic payoff, maximum visual scale`
- 실제 레퍼런스: [New York City night skyline by 500px 1.jpg](<https://commons.wikimedia.org/wiki/File%3ANew%20York%20City%20night%20skyline%20by%20500px%201.jpg>)

## ending beat

엔딩 비트는 마지막 여운이나 잔상을 남기는 마무리 이미지입니다.

![ending beat reference](https://commons.wikimedia.org/wiki/Special:FilePath/Golden_Hour_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `final ending beat, quieter landing image, lingering afterglow`
- 실제 레퍼런스: [Golden Hour (Unsplash)](https://commons.wikimedia.org/wiki/File%3AGolden_Hour_%28Unsplash%29.jpg)

## match cut

매치 컷은 형태, 선, 동작 방향이 비슷한 두 장면을 이어 붙이는 방식입니다. 컷이 갑자기 끊기기보다 의도적으로 이어지는 느낌을 줍니다.

![[assets/ai-video/editing-cuts-photos/match-cut.jpg|1400]]

- 프롬프트 조각: `match cut through circular shape continuity`
- 실제 레퍼런스 보드: [Comparison of softbox to direct flash.jpg](https://commons.wikimedia.org/wiki/File%3AComparison_of_softbox_to_direct_flash.jpg) + [Man standing in court (Unsplash)](https://commons.wikimedia.org/wiki/File%3AMan_standing_in_court_%28Unsplash%29.jpg)

## transition

`transition`은 한 샷에서 다음 샷으로 넘어가는 방식 전체를 가리키는 넓은 표현입니다. 단순 절단보다 설계된 연결을 뜻하는 경우가 많습니다.

![[assets/ai-video/editing-cuts-photos/transition.jpg|1400]]

- 프롬프트 조각: `transition beat, image change carried by blur and directional motion`
- 실제 레퍼런스 보드: [Golden Hour (Unsplash)](https://commons.wikimedia.org/wiki/File%3AGolden_Hour_%28Unsplash%29.jpg) + [Motion blur (1325070316).jpg](https://commons.wikimedia.org/wiki/File%3AMotion_blur_%281325070316%29.jpg) + [Red and blue open neon (Unsplash)](https://commons.wikimedia.org/wiki/File%3ARed_and_blue_open_neon_%28Unsplash%29.jpg)

## hard cut

하드 컷은 아무런 부드러운 블렌드 없이 다음 샷으로 바로 넘어가는 전환입니다. 대비가 분명할수록 잘 먹힙니다.

![[assets/ai-video/editing-cuts-photos/hard-cut.jpg|1400]]

- 프롬프트 조각: `hard cut from warm daylight to neon night`
- 실제 레퍼런스 보드: [Golden Hour (Unsplash)](https://commons.wikimedia.org/wiki/File%3AGolden_Hour_%28Unsplash%29.jpg) + [Red and blue open neon (Unsplash)](https://commons.wikimedia.org/wiki/File%3ARed_and_blue_open_neon_%28Unsplash%29.jpg)

## fade in / fade out

페이드 인과 페이드 아웃은 화면이 천천히 열리고 닫히는 방식입니다. 하드 컷보다 훨씬 부드럽고 여닫는 느낌이 강합니다.

![[assets/ai-video/editing-cuts-photos/fade-in-fade-out.jpg|1400]]

- 프롬프트 조각: `fade in from black, hold on the subject, fade out gently`
- 실제 레퍼런스 보드: [Elegant man with a laptop (Unsplash)](https://commons.wikimedia.org/wiki/File%3AElegant_man_with_a_laptop_%28Unsplash%29.jpg)

## 정리

이 카테고리는 한 줄 프롬프트보다 비트 단위로 생각할 때 훨씬 실전적입니다.

- 도입 규칙: `setup`
- 상승 구간: `escalation`
- 정점 이미지: `climax`
- 마지막 잔상: `ending beat`
- 컷의 연결 방식: `match cut`, `transition`, `hard cut`, `fade in / fade out`

AI 영상 프롬프트에서는 각 비트가 프레이밍, 정보량, 강도 중 하나라도 분명히 바뀌어야 컷 구조가 살아납니다.
