---
title: "주체와 행동"
description: "주체, 행동, 표정, 제스처를 실제 사진 레퍼런스로 정리한 AI 영상 프롬프트 용어집입니다."
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

이 페이지는 다이어그램이 아니라 **실제 사진 레퍼런스**로 다시 정리했습니다.  
주체와 행동 계열 용어는 프롬프트의 첫 줄을 결정하는 핵심이라서, 화면에 **누가 있는지**, **무슨 동작을 하는지**, **어떤 감정과 몸짓인지**를 분리해서 잡는 게 중요합니다.

## subject

`subject`는 프레임 안의 중심 대상을 뜻합니다. 사람인지, 동물인지, 물건인지부터 먼저 고정해야 이후 구도와 조명이 흔들리지 않습니다.

![subject reference](https://commons.wikimedia.org/wiki/Special:FilePath/Elegant_man_with_a_laptop_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `an elegant man with a laptop, subject isolated, editorial portrait`
- 실제 레퍼런스: [Elegant man with a laptop (Unsplash)](https://commons.wikimedia.org/wiki/File:Elegant_man_with_a_laptop_(Unsplash).jpg)

## action

`action`은 주체가 지금 실제로 하고 있는 동작입니다. 정지 상태인지, 달리는지, 손을 뻗는지에 따라 장면의 에너지가 달라집니다.

![action reference](https://commons.wikimedia.org/wiki/Special:FilePath/Woman_running.jpg?width=1200)

- 프롬프트 조각: `woman running along the waterfront, dynamic action, candid movement`
- 실제 레퍼런스: [Woman running](https://commons.wikimedia.org/wiki/File:Woman_running.jpg)

## expression

`expression`은 얼굴에서 읽히는 감정입니다. 같은 인물이라도 표정이 달라지면 장면의 장르와 긴장감이 완전히 달라집니다.

![expression reference](https://commons.wikimedia.org/wiki/Special:FilePath/Elegant_woman_by_storefront_(Unsplash).jpg?width=1100)

- 프롬프트 조각: `thoughtful expression, eyes looking off frame, calm mood`
- 실제 레퍼런스: [Elegant woman by storefront (Unsplash)](https://commons.wikimedia.org/wiki/File:Elegant_woman_by_storefront_(Unsplash).jpg)

## gesture

`gesture`는 손동작, 손끝 방향, 팔의 위치처럼 작은 몸짓을 말합니다. 특히 제품을 들거나 무언가를 가리키는 장면에서 정보 전달력이 큽니다.

![gesture reference](https://commons.wikimedia.org/wiki/Special:FilePath/Hands_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `delicate hand gesture holding a candle jar, intimate close detail`
- 실제 레퍼런스: [Hands (Unsplash)](https://commons.wikimedia.org/wiki/File:Hands_(Unsplash).jpg)

## interaction

`interaction`은 사람과 사람, 사람과 사물 사이의 반응입니다. 단독 인물보다 서사감과 관계성이 빨리 생깁니다.

![interaction reference](https://commons.wikimedia.org/wiki/Special:FilePath/Young_people_in_conversation_(Unsplash).jpg?width=1400)

- 프롬프트 조각: `young people in conversation, natural interaction, warm social energy`
- 실제 레퍼런스: [Young people in conversation (Unsplash)](https://commons.wikimedia.org/wiki/File:Young_people_in_conversation_(Unsplash).jpg)

## pose

`pose`는 몸의 방향, 체중 분배, 다리 각도, 어깨 정렬처럼 전신 자세를 말합니다. 인물의 분위기와 캐릭터성을 빠르게 정리할 때 유용합니다.

![pose reference](https://commons.wikimedia.org/wiki/Special:FilePath/Elegant_woman_by_storefront_(Unsplash).jpg?width=1200)

- 프롬프트 조각: `full-body pose, one leg forward, relaxed editorial stance`
- 실제 레퍼런스: [Elegant woman by storefront (Unsplash)](https://commons.wikimedia.org/wiki/File:Elegant_woman_by_storefront_(Unsplash).jpg)

## 정리

이 카테고리에서 제일 중요한 건 용어를 섞어 쓰지 않는 것입니다.

- `subject`: 누가 보이는가
- `action`: 무엇을 하고 있는가
- `expression`: 얼굴에 어떤 감정이 보이는가
- `gesture`: 손과 팔이 어떻게 움직이는가
- `interaction`: 누구와 무엇이 반응하는가
- `pose`: 몸 전체가 어떤 실루엣을 만드는가

실전 프롬프트에서는 보통 `subject + action + expression`까지만 먼저 고정해도 장면 방향이 많이 안정됩니다.
