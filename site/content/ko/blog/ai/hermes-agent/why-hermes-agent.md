---
title: "그냥 Codex 쓰면 되는데 왜 Hermes Agent를 쓸까?"
description: "Codex와 Hermes Agent의 역할을 구분하고, Hermes Agent를 Telegram에 연결해 개인 AI 비서처럼 쓰는 흐름을 정리합니다."
publish: true
draft: false
lang: "ko"
translationKey: "why-hermes-agent"
date: 2026-05-11
tags:
  - blog
  - ko
  - ai
  - hermes-agent
  - codex
  - telegram
  - automation
---

# 그냥 Codex 쓰면 되는데 왜 Hermes Agent를 쓸까?

Hermes Agent를 처음 설명할 때 가장 먼저 나오는 질문이 있다.

“그냥 Codex 쓰면 되는 거 아닌가?”

맞다. **코딩만 할 거면 Codex를 쓰면 된다.** GitHub repo를 읽고, 코드를 고치고, 테스트를 돌리고, 리팩터링하고, PR 리뷰를 하는 일에는 Codex가 훨씬 단순하고 직접적이다.

그런데 Hermes Agent를 쓰는 이유는 “Codex보다 코딩을 더 잘해서”가 아니다.

핵심은 범위가 다르다는 점이다.

Codex가 코딩 작업자에 가깝다면, Hermes Agent는 메신저, 파일, 웹, 터미널, 스케줄, 메모리, 스킬을 묶어 쓰는 **개인 AI 비서이자 자동화 레이어**에 가깝다.

## Codex와 Hermes Agent는 경쟁 관계가 아니다

Codex는 개발 작업에 강하다.

예를 들면 이런 일에 잘 맞는다.

- repo 구조 읽기
- 코드 수정
- 테스트 실행
- 버그 수정
- 리팩터링
- PR 리뷰
- 설치 스크립트 점검

반면 Hermes Agent는 조금 다른 위치에 있다.

Hermes Agent는 단순히 대답만 하는 챗봇이 아니라, 필요한 도구를 호출해서 실제 작업을 수행하는 에이전트다. 파일을 읽고 쓸 수 있고, 터미널 명령을 실행할 수 있고, 웹을 확인할 수 있고, 예약 작업을 만들 수 있고, Telegram이나 Discord 같은 메신저에 붙어서 동작할 수 있다.

그래서 Hermes Agent를 Codex의 대체재로 보면 애매하다.

더 정확히는 이렇게 보는 편이 좋다.

- Codex는 개발할 때 켜는 코딩 에이전트다.
- Hermes Agent는 평소에 메신저에서 부르는 개인 작업 에이전트다.

코딩만 할 거면 Codex가 맞다. 하지만 링크 정리, 노트 저장, 리마인더, 웹 조사, 파일 정리, 반복 자동화까지 맡기고 싶다면 Hermes Agent 쪽이 더 자연스럽다.

## Hermes Agent를 쓰는 이유

### 1. Telegram에서 바로 부를 수 있다

Hermes Agent의 가장 큰 장점 중 하나는 메신저 연결이다.

gateway를 켜두면 Telegram에서 그냥 메시지를 보내듯이 AI에게 일을 시킬 수 있다. 컴퓨터 앞에서 터미널을 열 필요가 없다.

예를 들면 이런 식이다.

```text
이 링크 읽고 핵심만 정리해줘.
이 이미지 보고 마감일을 리마인더에 넣어줘.
오늘 작업한 내용을 노트로 저장해줘.
이 에러 로그 보고 원인 후보부터 정리해줘.
내일 오전 9시에 이 일 다시 알려줘.
```

이건 단순 코딩 에이전트의 영역이라기보다, 개인 비서형 자동화에 가깝다.

### 2. 파일과 노트 작업을 이어서 맡길 수 있다

Hermes Agent는 파일을 읽고 쓰는 도구를 사용할 수 있다.

그래서 단순히 “설명해줘”에서 끝나는 게 아니라, 정리한 내용을 실제 Markdown 파일로 저장하거나, 기존 문서를 수정하거나, 처리 로그를 남기는 식으로 이어갈 수 있다.

예를 들어 Obsidian을 쓰고 있다면, 웹에서 찾은 자료를 요약해서 노트로 만들고, 관련 허브에 링크를 추가하고, 나중에 다시 찾을 수 있게 색인까지 정리하는 흐름을 만들 수 있다.

즉 Hermes Agent는 답변을 생성하는 데서 멈추지 않고, 작업 결과를 내 파일 시스템에 남기는 쪽으로 확장된다.

### 3. 기억과 스킬이 쌓인다

매번 같은 작업 방식을 설명하는 건 피곤하다.

예를 들어 노트를 어디에 저장해야 하는지, 어떤 형식을 좋아하는지, 처리 로그를 남겨야 하는지, 특정 작업에서 어떤 검증을 해야 하는지를 매번 다시 말해야 한다면 자동화의 의미가 줄어든다.

Hermes Agent는 이런 반복 절차를 스킬로 만들고, 사용자 선호나 환경 정보를 기억하는 구조를 갖는다.

도구가 “손”이라면, 스킬은 “작업 매뉴얼”에 가깝다.

덕분에 시간이 지날수록 단순한 챗봇이 아니라, 내 작업 방식을 아는 실행형 도우미에 가까워진다.

### 4. 예약 작업과 반복 작업을 맡길 수 있다

Hermes Agent는 cron job 같은 예약 작업을 만들 수 있다.

예를 들어 특정 시간에 알림을 보내거나, 주기적으로 웹페이지를 확인하거나, 정해진 시간에 자료를 수집해 요약하도록 만들 수 있다.

이 지점에서 Hermes Agent는 “지금 당장 대답하는 AI”를 넘어선다.

계속 켜두고, 필요할 때 알아서 실행되는 작업 비서가 된다.

### 5. 코딩 밖의 작업까지 연결된다

실제로 AI에게 맡기고 싶은 일은 코드만이 아니다.

- 문서 정리
- 웹 자료 조사
- 이미지 분석
- 이메일 확인
- 일정/리마인더 관리
- 노트 저장
- 블로그 초안 작성
- 반복 작업 자동화

이런 일들은 개발 IDE 안에만 갇힌 도구보다, 메신저와 파일 시스템, 브라우저, 스케줄러를 함께 다룰 수 있는 에이전트가 더 잘 맞는다.

Hermes Agent가 의미 있는 지점은 바로 여기다.

## Hermes Agent 설치 방법

공식 GitHub repo는 여기다.

```text
https://github.com/NousResearch/hermes-agent
```

Linux, macOS, WSL2, Termux에서는 공식 설치 스크립트를 사용할 수 있다.

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Windows PowerShell에서는 다음 명령을 사용할 수 있다.

```powershell
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

설치 후에는 기본 상태를 확인한다.

```bash
hermes --version
hermes setup
hermes model
hermes tools
hermes doctor
```

만약 직접 설치가 부담스럽다면 Codex에게 설치를 도와달라고 할 수도 있다.

예를 들면 이런 프롬프트를 사용할 수 있다.

```text
이 GitHub 레포를 읽고 내 환경에 맞게 Hermes Agent 설치를 도와줘.
Repo: https://github.com/NousResearch/hermes-agent
README.md와 내 OS에 맞는 설치 스크립트를 먼저 확인해줘.
API key, bot token, .env, auth 파일 내용은 절대 화면에 출력하지 마.
위험한 삭제, 권한 변경, 전역 설정 변경은 실행 전에 물어봐.
설치 후 hermes --version, hermes doctor, hermes setup까지 검증해줘.
```

여기서 Codex는 설치를 돕는 작업자 역할을 한다. 설치가 끝난 뒤 Hermes Agent를 Telegram에 붙여서 계속 사용하는 흐름이 이 글의 핵심이다.

## Telegram에 연결하는 흐름

Hermes Agent를 개인 비서처럼 쓰려면 Telegram 연결이 중요하다.

전체 흐름은 대략 이렇다.

1. BotFather로 Telegram bot을 만든다.
2. 내 Telegram user ID를 확인한다.
3. `hermes gateway setup`으로 Telegram 설정을 입력한다.
4. `hermes gateway`로 테스트 실행한다.
5. 계속 쓸 거면 gateway를 서비스로 등록한다.
6. Telegram에서 `/sethome`으로 기본 채널을 정한다.

### BotFather로 bot 만들기

Telegram에서 `@BotFather`를 검색한다.

`/newbot`을 보내고, bot 이름과 username을 정한다. username은 보통 `bot`으로 끝나야 한다.

BotFather가 token을 발급해준다. 이 token은 절대 공개하면 안 된다. 영상이나 블로그 스크린샷에 token이 보이면 바로 폐기하고 새로 발급해야 한다.

### Telegram user ID 확인하기

Hermes Agent는 아무나 bot을 쓰지 못하게 접근 허용 사용자를 제한할 수 있다.

이때 필요한 값은 Telegram username이 아니라 숫자로 된 user ID다.

`@userinfobot` 같은 봇에게 메시지를 보내면 내 숫자 ID를 확인할 수 있다.

### Hermes gateway 설정하기

터미널에서 다음 명령을 실행한다.

```bash
hermes gateway setup
```

설정 과정에서 Telegram을 선택하고, BotFather에서 받은 bot token과 내 Telegram user ID를 입력한다.

수동 설정을 한다면 개념적으로는 이런 값들이 들어간다.

```bash
TELEGRAM_BOT_TOKEN=***
TELEGRAM_ALLOWED_USERS=123456789
```

실제 token은 절대 공개 문서나 영상에 노출하지 않는다.

### gateway 실행하기

먼저 foreground에서 테스트한다.

```bash
hermes gateway
```

이 상태에서 Telegram bot에게 메시지를 보내고 답장이 오는지 확인한다.

정상적으로 동작하면 계속 켜두기 위해 서비스로 등록할 수 있다.

```bash
hermes gateway install
hermes gateway start
hermes gateway status
```

Telegram에서는 다음 명령도 자주 쓴다.

```text
/sethome
/status
/help
```

`/sethome`은 현재 채팅을 기본 전달 채널로 지정하는 명령이다. 예약 작업이나 자동화 결과를 어디로 보낼지 정할 때 중요하다.

## 그룹에서 쓸 때 주의할 점

Telegram group에서 Hermes Agent bot을 쓰려면 privacy mode를 이해해야 한다.

Telegram bot은 기본적으로 모든 그룹 메시지를 읽지 못할 수 있다. privacy mode가 켜져 있으면 slash command나 bot에게 직접 답장한 메시지 위주로만 볼 수 있다.

모든 그룹 메시지를 읽게 하려면 BotFather에서 해당 bot의 설정으로 들어가 Group Privacy를 끄거나, bot을 그룹 admin으로 올려야 한다.

privacy mode를 바꾼 뒤에는 bot을 그룹에서 제거했다가 다시 초대해야 적용되는 경우가 있다.

## 보안상 꼭 조심할 것

Hermes Agent는 강력하다.

강력하다는 건 그만큼 조심해야 한다는 뜻이기도 하다. 파일을 읽고, 터미널을 실행하고, 메신저에 붙고, 외부 API를 사용할 수 있기 때문이다.

최소한 아래는 지키는 편이 좋다.

- bot token을 절대 공개하지 않는다.
- API key와 `.env` 파일을 화면에 노출하지 않는다.
- 허용 사용자 ID를 제한한다.
- 위험한 삭제 명령이나 권한 변경은 실행 전에 확인한다.
- 그룹에 붙일 때는 어떤 메시지를 읽을 수 있는지 이해한다.
- 공개 블로그나 영상에는 로컬 경로, token, key, 개인 정보가 들어가지 않게 확인한다.

AI 에이전트는 편리하지만, 내 컴퓨터에 손을 뻗는 도구이기도 하다. 그래서 편의성과 보안 감각을 같이 가져가야 한다.

## 정리

Codex와 Hermes Agent는 같은 문제를 푸는 도구가 아니다.

Codex는 코딩 작업자에 가깝다. repo를 읽고, 코드를 고치고, 테스트를 돌리는 개발 작업에 잘 맞는다.

Hermes Agent는 개인 AI 비서와 자동화 레이어에 가깝다. Telegram에서 부르고, 파일을 정리하고, 웹을 확인하고, 노트를 저장하고, 리마인더와 cron 작업까지 이어갈 수 있다.

그래서 결론은 단순하다.

코딩만 할 거면 Codex를 쓰면 된다.

하지만 AI를 내 작업 환경 전체에 붙여서, 메신저에서 부르고, 반복 작업을 맡기고, 노트와 파일까지 관리하게 만들고 싶다면 Hermes Agent를 써볼 이유가 충분하다.

한 문장으로 정리하면 이렇다.

**Codex는 코딩 작업자이고, Hermes Agent는 Telegram에서 부르는 개인 AI 비서다.**
