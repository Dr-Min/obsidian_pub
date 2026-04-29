---
title: "Hermes Agent"
description: "Hermes Agent의 명령어, 도구, 스킬 구조를 짧게 정리합니다."
publish: true
draft: false
lang: "ko"
translationKey: "hermes-agent-field-guide"
date: 2026-04-30
tags:
  - blog
  - ko
  - ai
  - hermes-agent
  - automation
---

# Hermes Agent

Hermes Agent는 터미널, 메신저, IDE, 자동화 작업에서 동작하는 **도구 사용형 AI 에이전트**입니다. 단순 챗봇처럼 답만 하는 것이 아니라, 파일을 읽고 쓰고, 터미널 명령을 실행하고, 브라우저를 조작하고, 스케줄 작업을 등록하고, 필요하면 다른 하위 에이전트에게 일을 나눌 수 있습니다.


## 먼저 구분해야 할 것

| 구분 | 의미 | 예시 |
| --- | --- | --- |
| CLI 커맨드 | 터미널에서 `hermes ...`로 실행하는 명령 | `hermes doctor`, `hermes model`, `hermes skills list` |
| 슬래시 명령어 | 대화 중 바로 입력하는 명령 | `/model`, `/skill`, `/reset`, `/cron` |
| Toolset | 도구를 묶어서 켜고 끄는 단위 | `terminal`, `file`, `browser`, `skills` |
| API tool | 실제 세션 안에서 호출되는 함수형 도구 | `read_file`, `terminal`, `search_files`, `cronjob` |
| Skill | 특정 작업을 잘하기 위한 절차 문서 | GitHub 작업, Obsidian 정리, 디버깅 루프 등 |
| Profile | 설정, 세션, 스킬, 메모리를 분리한 실행 단위 | 개인용/업무용/실험용 프로필 |

## 왜 이 구조가 중요한가

Hermes를 이해할 때 제일 헷갈리는 부분은 “명령어”, “도구”, “스킬”이 전부 비슷해 보인다는 점입니다. 하지만 역할은 다릅니다.

- **명령어**는 Hermes 자체를 조작합니다.
- **도구**는 Hermes가 실제 세계에 손을 뻗는 방법입니다.
- **스킬**은 어떤 작업을 어떤 순서로 처리할지 알려주는 절차 기억입니다.

그래서 Hermes를 잘 쓰려면 모델만 고르는 것이 아니라, 현재 작업에 맞는 toolset과 skill을 함께 이해해야 합니다.

## 빠르게 쓰는 시작점

| 하고 싶은 일 | 시작 명령 |
| --- | --- |
| 설치/환경 상태 확인 | `hermes doctor`, `hermes status --all` |
| 모델 바꾸기 | `hermes model` 또는 `/model` |
| 도구 확인 | `hermes tools list` 또는 `/toolsets` |
| 스킬 확인 | `hermes skills list` 또는 `/skills` |
| 메신저 gateway 확인 | `hermes gateway status` 또는 `/platforms` |
| 스케줄 작업 확인 | `hermes cron list` 또는 `/cron` |

## 이 시리즈의 글

- [[ko/blog/ai/hermes-agent/commands|명령어]] — 터미널 명령과 세션 명령.
- [[ko/blog/ai/hermes-agent/tools|도구]] — 에이전트가 실제로 일하는 방식.
- [[ko/blog/ai/hermes-agent/skills|스킬]] — 작업 절차를 불러오는 방식.
