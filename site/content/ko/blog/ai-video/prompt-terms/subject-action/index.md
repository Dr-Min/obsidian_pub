---
title: "주체와 행동"
description: "주체, 행동, 표정, 제스처를 실제 사진 레퍼런스로 다시 정리한 AI 영상 프롬프트 용어집입니다."
publish: true
draft: false
lang: "ko"
translationKey: "ai-video-subject-action"
tags:
  - blog
  - ko
  - ai-video
  - subject-action
---

# 주체와 행동

이 페이지는 **실제 사진 레퍼런스**로 다시 정리했습니다.  
주체와 행동 계열은 프롬프트의 가장 첫 구조를 잡아줍니다. 즉, **누가 나오고**, **무엇을 하고**, **그 행동이 어떤 감정과 몸짓으로 보이는지**를 분리해서 쓰는 층입니다.

## subject

`subject`는 프레임 안의 중심 대상입니다. 렌즈, 구도, 조명을 정하기 전에 먼저 누가 화면의 주인공인지 고정해야 합니다.

![subject reference](https://commons.wikimedia.org/wiki/Special:FilePath/Elegant_man_with_a_laptop_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `an elegant man with a laptop, subject isolated, editorial portrait`
- 실제 레퍼런스: [Elegant man with a laptop (Unsplash)](https://commons.wikimedia.org/wiki/File%3AElegant_man_with_a_laptop_%28Unsplash%29.jpg)

## action

`action`은 피사체가 지금 실제로 하고 있는 동작입니다. 정지 자세인지, 걷는지, 달리는지에 따라 장면 에너지가 크게 달라집니다.

![action reference](https://commons.wikimedia.org/wiki/Special:FilePath/Woman_running.jpg?width=1200)

- 프롬프트 조각: `woman running along the waterfront, dynamic action, candid movement`
- 실제 레퍼런스: [Woman running](https://commons.wikimedia.org/wiki/File%3AWoman_running.jpg)

## expression

`expression`은 얼굴에서 읽히는 감정 신호입니다. 같은 인물과 같은 조명이어도 표정만 달라지면 장르와 톤이 달라집니다.

![expression reference](https://commons.wikimedia.org/wiki/Special:FilePath/Elegant_woman_by_storefront_(Unsplash).jpg?width=1100)

- 프롬프트 조각: `thoughtful expression, eyes looking off frame, calm mood`
- 실제 레퍼런스: [Elegant woman by storefront (Unsplash)](https://commons.wikimedia.org/wiki/File%3AElegant_woman_by_storefront_%28Unsplash%29.jpg)

## gesture

`gesture`는 손, 손목, 팔 방향처럼 더 작은 몸짓 레이어를 말합니다. 제품 컷이나 가까운 디테일 장면에서 특히 중요합니다.

![gesture reference](https://commons.wikimedia.org/wiki/Special:FilePath/Hands_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `delicate hand gesture holding a candle jar, intimate close detail`
- 실제 레퍼런스: [Hands (Unsplash)](https://commons.wikimedia.org/wiki/File%3AHands_%28Unsplash%29.jpg)

## interaction

`interaction`은 사람과 사람, 사람과 사물 사이의 관계가 화면에 드러나는 상태입니다. 혼자 있는 인물보다 훨씬 빨리 서사를 만듭니다.

![interaction reference](https://commons.wikimedia.org/wiki/Special:FilePath/Young_people_in_conversation_(Unsplash).jpg?width=1400)

- 프롬프트 조각: `young people in conversation, natural interaction, warm social energy`
- 실제 레퍼런스: [Young people in conversation (Unsplash)](https://commons.wikimedia.org/wiki/File%3AYoung_people_in_conversation_%28Unsplash%29.jpg)

## pose

`pose`는 체중 분배, 다리 각도, 어깨 방향, 전체 실루엣처럼 몸 전체 배열을 뜻합니다. 캐릭터 인상을 가장 빨리 바꾸는 요소 중 하나입니다.

![[assets/ai-video/shot-composition-photos/full-shot.jpg|1000]]

- 프롬프트 조각: `full-body pose, one leg forward, relaxed editorial stance`
- 실제 레퍼런스: [Man standing in court (Unsplash)](https://commons.wikimedia.org/wiki/File%3AMan_standing_in_court_%28Unsplash%29.jpg), `CC0`, 크롭

## 정리

실전에서는 이 단어들을 한 덩어리로 뭉개면 안 됩니다.

- `subject`: 누가 보이는가
- `action`: 무엇을 하는가
- `expression`: 얼굴이 어떤 감정을 띠는가
- `gesture`: 손과 팔이 어떻게 움직이는가
- `interaction`: 누구와 무엇이 관계를 맺는가
- `pose`: 몸 전체 실루엣이 어떤가

실제로는 `subject + action + expression`만 먼저 고정해도 장면 방향이 상당히 안정됩니다.
