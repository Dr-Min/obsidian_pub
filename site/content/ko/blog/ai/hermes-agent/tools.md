---
title: "Hermes Agent 도구와 Toolset: 에이전트가 실제로 일하는 방법"
description: "Hermes Agent의 Toolset 20개와 현재 공개 스냅샷 기준 API tool 30개를 정리합니다."
publish: true
draft: false
lang: "ko"
translationKey: "hermes-agent-tools"
date: 2026-04-30
tags:
  - blog
  - ko
  - ai
  - hermes-agent
  - tools
  - toolsets
---

# Hermes Agent 도구와 Toolset: 에이전트가 실제로 일하는 방법

Toolset은 Hermes에게 “어떤 종류의 손을 쥐여 줄지” 정하는 단위입니다. 예를 들어 파일을 다루려면 `file`, 셸 명령을 실행하려면 `terminal`, 브라우저 UI를 확인하려면 `browser`가 필요합니다.

> 기준 시점: 2026-04-29 22:14 KST

## Toolset 전체

| Toolset | 기능 |
| --- | --- |
| web | 웹 검색과 콘텐츠 추출. |
| browser | Browserbase/Camofox/local Chromium 기반 브라우저 자동화. |
| terminal | 셸 명령 실행과 process 관리. |
| file | 파일 읽기/쓰기/검색/patch. |
| code_execution | 샌드박스 Python 실행. |
| vision | 이미지 분석. |
| image_gen | AI 이미지 생성. |
| tts | 텍스트 음성 변환. |
| skills | 스킬 조회/로드/생성/수정. |
| memory | 세션을 넘어 유지되는 장기 memory/profile. |
| session_search | 과거 대화 검색. |
| delegation | subagent에게 독립 작업 위임. |
| cronjob | 스케줄 작업 생성/관리. |
| clarify | 사용자에게 선택지/질문을 보낸다. |
| messaging | 연결된 플랫폼으로 메시지 전송. |
| search | 웹 검색 전용 subset. |
| todo | 현재 세션 작업 목록 관리. |
| rl | 강화학습 도구. 기본 off. |
| moa | Mixture of Agents. 기본 off. |
| homeassistant | 스마트홈/Home Assistant 제어. 기본 off. |

## API tool 전체

아래는 이 글 작성 시점에 공개 가능한 세션 도구 표면입니다. 실제 환경에서는 profile, platform, toolset 설정에 따라 달라질 수 있습니다.

| API tool | 기능 |
| --- | --- |
| browser_navigate | URL로 이동하고 페이지 snapshot을 받는다. |
| browser_snapshot | 현재 페이지 접근성 tree/snapshot을 본다. |
| browser_click | snapshot ref ID의 요소를 클릭한다. |
| browser_type | snapshot ref ID input에 텍스트를 입력한다. |
| browser_press | Enter/Tab/Escape 등 키를 누른다. |
| browser_scroll | 페이지를 위/아래로 스크롤한다. |
| browser_back | 브라우저 history 뒤로 간다. |
| browser_console | 콘솔 로그/JS 오류를 읽거나 JS expression을 실행한다. |
| browser_get_images | 현재 페이지 이미지 URL과 alt를 수집한다. |
| browser_vision | 스크린샷을 찍고 시각적으로 분석한다. |
| clarify | 선택지 또는 자유응답 질문을 사용자에게 보낸다. |
| cronjob | 스케줄 작업 create/list/update/pause/resume/remove/run을 한다. |
| delegate_task | 격리된 subagent에게 단일/병렬 작업을 위임한다. |
| image_generate | 텍스트 prompt로 이미지를 생성한다. |
| memory | 장기 memory/user profile을 add/replace/remove한다. |
| patch | 파일에 fuzzy find/replace 또는 V4A patch를 적용한다. |
| process | background terminal process를 list/poll/log/wait/kill/write/submit/close한다. |
| read_file | 텍스트 파일을 line number와 함께 페이지 단위로 읽는다. |
| search_files | 파일 이름 glob 검색 또는 파일 내용 regex 검색을 한다. |
| send_message | 연결된 메시징 플랫폼의 대상 목록을 보거나 메시지를 보낸다. |
| session_search | 과거 세션을 최근순/키워드로 검색한다. |
| skills_list | 설치된 스킬 목록과 설명을 가져온다. |
| skill_view | 스킬 본문이나 linked file을 읽는다. |
| skill_manage | 스킬 create/patch/edit/delete 및 supporting file 관리를 한다. |
| terminal | 셸 명령을 foreground/background/PTY로 실행한다. |
| text_to_speech | 텍스트를 음성 파일/voice message로 변환한다. |
| todo | 현재 세션의 작업 목록을 만들고 상태를 갱신한다. |
| vision_analyze | 이미지 URL/파일을 AI vision으로 분석한다. |
| write_file | 파일 전체 내용을 새로 쓰거나 생성한다. |
| multi_tool_use.parallel | 서로 독립적인 여러 developer tool 호출을 병렬 실행한다. |

## 실사용 판단 기준

| 상황 | 먼저 볼 도구 |
| --- | --- |
| 파일을 읽어야 함 | `read_file` |
| 파일 이름이나 내용을 찾아야 함 | `search_files` |
| 파일을 새로 쓰거나 고쳐야 함 | `write_file`, `patch` |
| 빌드/테스트/배포가 필요함 | `terminal`, `process` |
| 웹 UI를 직접 확인해야 함 | `browser_*` |
| 이미지나 스크린샷 판단이 필요함 | `vision_analyze`, `browser_vision` |
| 반복 일정이 필요함 | `cronjob` |
| 독립 조사/구현이 필요함 | `delegate_task` |
| 이전 대화 기억이 필요함 | `session_search` |

## 핵심 원칙

도구는 많을수록 무조건 좋은 것이 아닙니다. 필요한 toolset만 켜면 프롬프트가 가벼워지고, 보안 면에서도 예측하기 쉽습니다. 반대로 배포, 파일 수정, 외부 메시지 전송처럼 부작용이 있는 작업은 도구가 있어도 검증 단계를 거쳐야 합니다.
