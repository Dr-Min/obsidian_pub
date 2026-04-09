---
title: "AI 영상 프롬프트 작성법: 실전 예시와 구조 완전 가이드"
description: "AI 영상 프롬프트를 어떻게 써야 결과가 좋아지는지, 샷 구성, 카메라 무브, 16:9와 9:16 차이, 실전 예시까지 한 번에 정리한 가이드."
date: 2026-04-10
modified: 2026-04-10
draft: false
publish: true
lang: "ko"
translationKey: "ai-video-prompts"
tags:
  - blog
  - ko
---

지금 많은 사람이 AI 영상 모델을 쓰기 시작했지만, 결과가 만족스럽지 않다고 느끼는 경우가 많습니다. 이유는 간단합니다. 대부분의 입력이 "멋진 영상", "영화 같은 분위기", "고퀄리티" 같은 추상적인 말에 머물기 때문입니다. AI 영상 프롬프트는 감상문이 아니라 촬영 지시서에 더 가깝습니다. 어떤 피사체가 어디에 있고, 카메라는 어떤 거리와 각도에서 바라보며, 어떤 빛과 움직임으로 장면을 해석해야 하는지를 분명하게 적어야 결과가 안정됩니다.

예를 들어 `a woman in a city`라고 쓰는 것과 `medium shot of a woman in a rainy city street, 50mm lens, soft neon reflections, slow push-in`이라고 쓰는 것은 완전히 다릅니다. 두 번째 문장은 모델이 무엇을 어떻게 보여줘야 하는지 훨씬 명확하게 이해할 수 있게 해줍니다. 이 차이가 결과물을 바꿉니다.

이 글에서는 AI 영상 프롬프트가 무엇인지, 왜 중요한지, 어떻게 구조화해야 하는지, 16:9와 9:16에서 무엇이 달라지는지, 그리고 바로 복붙해서 쓸 수 있는 예시까지 정리합니다. 이미 구도와 움직임 중심 가이드를 따로 정리해 두었기 때문에, 읽으면서 [[ko/blog/shot-composition-camera-movement|화면 구도와 카메라 움직임 가이드]]와 함께 보면 이해가 더 빨라집니다.

## AI 영상 프롬프트란?

AI 영상 프롬프트는 텍스트로 영상의 핵심 요소를 지정하는 입력 문장입니다. 하지만 단순한 설명문이 아니라, 실제로는 다음 요소를 묶어 전달하는 구조라고 보는 편이 정확합니다.

- 피사체: 누가, 무엇이 등장하는가
- 행동: 무엇을 하고 있는가
- 장면: 어디에서 벌어지는가
- 시각 언어: 샷 크기, 렌즈, 카메라 각도, 무빙
- 분위기: 조명, 색감, 질감, 감정 톤
- 시간 흐름: 한 컷인지, 여러 컷인지, 장면 전환이 있는지

즉 AI 영상 프롬프트는 "보이는 것"만 설명하는 게 아니라 "찍히는 방식"까지 지정해야 합니다. 여기서 많은 초보자가 놓치는 부분이 있습니다. 이미지 프롬프트는 정지된 한 장면에 집중해도 되지만, 영상 프롬프트는 시간과 움직임이 들어갑니다. 그래서 카메라가 어떻게 따라가는지, 피사체가 어떻게 이동하는지, 장면이 어느 지점에서 커지거나 닫히는지가 중요합니다.

가장 쉬운 비유는 이겁니다. 이미지 프롬프트가 포스터 설명에 가깝다면, AI 영상 프롬프트는 쇼트 리스트와 미니 스토리보드의 중간쯤에 가깝습니다. 한 문장으로 끝날 수도 있지만, 잘 만든 프롬프트는 이미 안에 카메라 언어와 장면 의도를 포함하고 있습니다.

그래서 "예쁜 영상"보다 "어떤 인물이, 어떤 환경에서, 어떤 카메라 동작과 조명 안에서, 어떤 순간을 보여주는가"를 생각하는 습관이 중요합니다. 그 순간 프롬프트는 추상적 표현에서 연출 언어로 바뀝니다.

## 왜 좋은 AI 영상 프롬프트가 중요한가

좋은 프롬프트는 단지 더 화려한 결과를 만드는 것이 아닙니다. 더 중요한 건 **일관성**과 **재현성**입니다. 비슷한 구조를 여러 번 반복해서 쓰더라도 원하는 결과 범위 안에 머무르게 만들어 줍니다.

좋은 AI 영상 프롬프트가 중요한 이유는 크게 네 가지입니다.

첫째, 결과 해석의 폭을 줄여 줍니다. 모델은 입력이 추상적일수록 자기 식으로 장면을 해석합니다. 어떤 경우에는 그게 우연한 재미를 만들지만, 대부분은 의도와 다른 결과가 나옵니다. 반대로 샷 크기, 각도, 조명, 움직임을 명확히 넣으면 결과가 흔들릴 여지가 줄어듭니다.

둘째, 수정이 쉬워집니다. 좋은 프롬프트는 여러 층으로 나뉘어 있기 때문에, 문제가 생겼을 때 어느 부분을 고쳐야 하는지 보입니다. 예를 들어 인물은 좋은데 카메라가 이상하면 `camera movement` 구간만 바꾸면 됩니다. 도시 배경은 좋은데 감정이 약하면 조명과 무드 부분만 손보면 됩니다.

셋째, 플랫폼별 최적화가 쉬워집니다. 같은 아이디어라도 유튜브형 16:9 영상과 쇼츠형 9:16 영상은 프레이밍이 다릅니다. 좋은 프롬프트는 핵심 요소를 분리해 써두기 때문에, 구조는 유지하고 화면비에 맞는 부분만 바꾸기가 쉽습니다.

넷째, 여러 컷 구조로 확장하기 쉽습니다. 실제로 강한 AI 영상은 한 컷짜리 예쁜 장면보다, 짧아도 `도입 -> 상승 -> 클라이맥스 -> 종료` 흐름이 있는 경우가 많습니다. 최근 정리한 [[ko/blog/seedance-manhattan-wall-run-portal-prompt|Seedance 포털 액션 아카이브]]처럼 컷 단위로 구조를 만들면 훨씬 강한 결과가 나옵니다.

결국 좋은 프롬프트는 결과를 한 번 맞히는 기술이 아니라, 원하는 영상을 계속 비슷한 품질로 만들게 해주는 작업 방식입니다.

## AI 영상 프롬프트의 핵심 공식

가장 실용적인 공식은 아래 하나로 시작하면 됩니다.

```text
[피사체] + [행동] + [샷 크기] + [카메라 각도] + [렌즈 느낌] + [카메라 움직임] + [조명] + [배경/환경] + [질감/무드]
```

이 공식을 그대로 풀어 쓰면 이렇게 됩니다.

```text
A young director reviewing a storyboard wall, medium shot, eye-level angle, 50mm lens, slow lateral tracking shot, soft daylight from studio windows, industrial creative workspace, cinematic realism, subtle depth of field
```

이 공식의 좋은 점은 추상적인 형용사를 최소화하고, 프레임을 구성하는 실제 요소를 앞쪽에 배치한다는 데 있습니다. 대부분의 모델은 앞부분에서 피사체와 장면을 잡고, 뒤쪽에서 카메라 언어와 질감을 조정하는 식으로 반응합니다.

조금 더 확장하면 컷 구조형 공식도 만들 수 있습니다.

```text
Cut 1: setup
Cut 2: motion escalation
Cut 3: visual twist
Cut 4: climax
Cut 5: ending beat
```

이 구조는 액션, 광고, 캐릭터 소개, 제품 시네마틱, 게임풍 영상에 모두 응용할 수 있습니다. 중요한 건 장면을 예쁘게 만드는 수식어보다, **무엇이 어떻게 커지고 닫히는지**를 적는 것입니다.

또 하나 기억할 점은 프롬프트 안에 우선순위가 있다는 사실입니다. 피사체와 행동, 샷 크기와 움직임은 핵심층이고, `epic`, `beautiful`, `high quality` 같은 단어는 보조층입니다. 핵심층이 약한데 보조층만 많으면 결과는 멋져 보이는 잡음이 되기 쉽습니다.

## 샷 구성, 렌즈, 카메라 움직임은 어떻게 적어야 하나

많은 가이드가 프롬프트를 설명하면서도 카메라 언어는 대충 넘어갑니다. 하지만 영상 결과 품질을 가르는 핵심은 여기 있습니다.

샷 구성은 프롬프트의 첫 번째 시각적 골격입니다.

- 와이드샷: 공간, 규모감, 배경 설명
- 미디엄샷: 인물 행동, 제품 시연, 인터뷰, 설명 장면
- 클로즈업: 감정, 디테일, 텍스처 강조

렌즈 느낌은 공간 왜곡과 피사체 분리를 조절합니다.

- `24mm wide lens`: 넓은 공간감, 역동적인 왜곡
- `50mm lens`: 가장 무난하고 안정적인 인물 프레이밍
- `85mm portrait lens`: 인물 강조, 배경 압축, 감정 집중

카메라 움직임은 속도와 몰입을 조절합니다.

- `locked-off tripod shot`: 차분하고 정확한 프레임
- `slow push-in`: 감정이나 집중도를 올릴 때 유리
- `side tracking shot`: 이동감, 속도감 표현
- `gentle handheld`: 브이로그, 현장감, 다큐 느낌

여기서 중요한 원칙은 **한 번에 하나의 핵심 움직임만 선택하는 것**입니다. `drone shot, handheld, dolly in, spinning camera`를 한 줄에 다 넣으면 모델은 장면을 안정적으로 해석하기 어렵습니다. 먼저 하나를 정하고, 그 움직임의 속도와 질감만 조절하는 편이 결과가 좋습니다.

이 부분은 이미 별도 글에서 더 길게 다뤘기 때문에, 구체적인 샷 예시가 필요하면 [[ko/blog/shot-composition-camera-movement|구도와 카메라 움직임 가이드]]를 같이 참고하는 편이 좋습니다.

## 16:9와 9:16 프롬프트는 왜 다르게 써야 하나

많은 사람이 여기서 실수합니다. 같은 프롬프트를 그대로 두고 9:16만 누르면 된다고 생각하지만, 실제로는 그렇지 않습니다. 세로 영상은 단순히 가로 영상을 잘라낸 버전이 아니라, **프레임의 우선순위 자체가 달라진 화면**입니다.

16:9는 환경과 좌우 이동을 보여주기 좋습니다. 도시 배경, 군중, 차량 흐름, 넓은 세트, 수평 추적 장면이 잘 먹힙니다. 반면 9:16은 인물 중심성, 세로 방향 움직임, 위아래 레이어, 얼굴과 몸의 비율이 더 중요해집니다.

예를 들어 16:9에서는 이렇게 쓸 수 있습니다.

```text
A creator running through a neon city alley, wide shot, side tracking shot, 35mm lens, cinematic night lighting
```

하지만 9:16에서는 같은 장면이라도 이렇게 바꾸는 편이 낫습니다.

```text
A creator centered in frame, vertical full-body shot, slight low angle, narrow neon alley rising behind the subject, upward motion emphasis, 35mm lens, handheld energy
```

차이는 명확합니다. 세로 화면에서는 좌우 환경을 설명하기보다, 인물과 배경의 높이 관계를 설명해야 합니다. 계단을 오르거나, 빌딩 벽을 타거나, 포털 위로 빨려 들어가거나, 점프가 위아래 축으로 커지는 장면은 9:16에서 훨씬 강하게 보일 수 있습니다.

정리하면:

- 16:9는 환경과 수평 이동을 키워라
- 9:16은 인물과 세로 축을 키워라
- 세로 화면에서는 얼굴, 몸, 상하 배경층을 더 분명하게 써라
- 같은 프롬프트를 단순 크롭하지 말고, 프레임 목적을 다시 써라

## 실전에서 바로 쓰는 AI 영상 프롬프트 예시 5개

### 1. 인터뷰형 브랜드 영상

```text
A founder speaking calmly in a creative studio, medium shot, eye-level angle, 50mm lens, locked-off tripod shot, soft key light from the left, subtle background depth, premium documentary feel
```

### 2. 제품 디테일 강조 영상

```text
Close-up of hands unfolding a compact drone controller, slight top-down angle, 85mm lens, slow push-in, crisp studio lighting, matte black tabletop, premium commercial texture
```

### 3. 영화풍 도심 러닝 샷

```text
A young woman running through a rain-soaked Seoul street at night, medium tracking shot, 35mm lens, reflections on wet asphalt, soft neon haze, cinematic urgency
```

### 4. 9:16 쇼츠형 인물 중심 영상

```text
Vertical full-body shot of a creator stepping into a glowing portal, slight low angle, centered framing, strong upward energy, blue rim light, dramatic smartphone-friendly composition
```

### 5. 컷 구조형 액션 프롬프트

```text
Cut 1: a lone character stands in an empty rooftop garden at dusk, low-angle cinematic shot, wind in coat and hair
Cut 2: the character sprints forward with impossible speed, side tracking shot, shockwaves and dust
Cut 3: the run transitions into a leap across connected rooftops, brief slow motion, orange city glow
Cut 4: the character lands near a bright portal doorway, camera push-in, tension spike
Cut 5: the character enters the portal as the frame fills with light
```

이 예시들의 공통점은 장르가 아니라 구조입니다. 피사체, 샷 크기, 카메라 언어, 조명, 무드가 최소 단위로 들어가 있습니다. 여기에 배경만 바꾸면 여행 영상도 되고, 게임풍 티저도 되고, 광고형 영상도 됩니다.

## AI 영상 프롬프트에서 자주 하는 실수

첫째, 형용사만 많고 연출 정보가 없습니다. `stunning, epic, beautiful, ultra quality`만으로는 프레임이 만들어지지 않습니다.

둘째, 물리적으로 충돌하는 조합을 씁니다. 예를 들어 `extreme close-up drone shot`처럼 동시에 성립하기 어려운 조합은 결과를 흔듭니다.

셋째, 움직임을 너무 많이 섞습니다. 한 프롬프트에 추적, 드론, 핸드헬드, 스핀, 줌까지 다 넣으면 모델은 우선순위를 잃습니다.

넷째, 조명을 너무 추상적으로 씁니다. `nice lighting`보다 `warm sunset rim light`, `soft daylight through curtains`, `cold blue backlight`가 훨씬 낫습니다.

다섯째, 화면비를 고려하지 않습니다. 특히 세로 영상은 인물 중심성과 상하 구성이 중요한데, 가로형 사고방식 그대로 쓰는 경우가 많습니다.

여섯째, 스토리의 상승 구조가 없습니다. 영상은 시간이 있는 매체라서, 한 장면만 예쁘게 만드는 것보다 장면이 어떻게 커지고 닫히는지를 적는 편이 결과가 좋습니다.

## 자주 묻는 질문

### AI 영상 프롬프트는 길수록 좋은가요?

무조건 그렇지는 않습니다. 길이보다 구조가 중요합니다. 짧아도 피사체, 행동, 샷 크기, 카메라 움직임, 조명이 분명하면 강한 결과가 나옵니다. 반대로 길어도 추상 형용사만 늘어놓으면 품질은 오르지 않습니다.

### 영어로 쓰는 게 더 좋은가요?

많은 모델이 영어 프롬프트에서 더 안정적으로 반응하는 편이지만, 중요한 건 언어 자체보다 구조입니다. 한국어로도 명확하게 잘 쓰면 괜찮습니다. 다만 모델 반응을 비교해 보고 싶다면, 핵심 구조는 유지한 채 영어 버전을 같이 테스트하는 방법이 좋습니다.

### 9:16용 프롬프트는 따로 만들어야 하나요?

가능하면 따로 만드는 것이 좋습니다. 최소한 인물 중심성, 상하 구도, 세로 방향 움직임을 다시 써주는 편이 결과가 낫습니다.

### 컷 구조형 프롬프트는 언제 유리한가요?

액션, 캐릭터 소개, 짧은 스토리형 광고, 영화 예고편 느낌 영상처럼 장면 전환이 중요한 작업에서 특히 유리합니다. 한 컷짜리 미장센보다 몰입감 있는 결과가 나올 가능성이 높습니다.

## 결론

AI 영상 프롬프트를 잘 쓴다는 건 멋진 형용사를 많이 아는 것이 아닙니다. 피사체와 환경, 샷 크기와 렌즈, 카메라 움직임과 조명을 **촬영 언어로 정리하는 능력**에 가깝습니다.

가장 먼저 익혀야 할 핵심은 네 가지입니다.

- 무엇을 찍는가
- 어느 거리에서 보는가
- 카메라는 어떻게 움직이는가
- 빛과 분위기는 무엇인가

이 네 가지만 분명해져도 결과 품질은 눈에 띄게 좋아집니다. 그다음에는 16:9와 9:16을 구분하고, 단일 장면에서 컷 구조형 프롬프트로 확장해 가면 됩니다. 일반 방식으로 글을 만드는 흐름도 결국 같습니다. 먼저 리서치 브리프를 잡고, 플랜으로 구조를 만들고, 그 위에 초안을 쓰면 내용이 훨씬 덜 흔들립니다.
