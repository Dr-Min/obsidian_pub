---
title: "Hermes Agent 설치 스킬 카탈로그: 90개 작업 절차 한눈에 보기"
description: "Hermes Agent에 설치된 90개 스킬을 카테고리별로 정리한 공개 카탈로그입니다."
publish: true
draft: false
lang: "ko"
translationKey: "hermes-agent-skills"
date: 2026-04-30
tags:
  - blog
  - ko
  - ai
  - hermes-agent
  - skills
  - catalog
---

# Hermes Agent 설치 스킬 카탈로그: 90개 작업 절차 한눈에 보기

Skill은 Hermes가 특정 작업을 잘하기 위해 불러오는 **절차 기억**입니다. 도구가 손이라면, 스킬은 “이 일을 어떤 순서와 기준으로 처리할지” 알려주는 작업 매뉴얼에 가깝습니다.

> 기준 시점: 2026-04-29 22:14 KST
> 기준: `skills_list()` 결과. 총 **90개**.
> 설치/삭제/업데이트에 따라 목록은 바뀔 수 있다.

## 빠른 요약

| 카테고리                 |  개수 |
| -------------------- | --: |
| dogfood/QA           |   1 |
| autonomous-ai-agents |   4 |
| creative             |  18 |
| data-science         |   1 |
| devops               |   1 |
| email                |   1 |
| gaming               |   2 |
| github               |   7 |
| leisure              |   1 |
| mcp                  |   2 |
| media                |   5 |
| mlops                |  22 |
| note-taking          |   3 |
| productivity         |   9 |
| red-teaming          |   1 |
| research             |   5 |
| smart-home           |   1 |
| software-development |   6 |

## dogfood/QA

| 스킬 | 기능 |
| --- | --- |
| dogfood | 웹 애플리케이션을 사람처럼 탐색 테스트하고, 버그 증거와 구조화 리포트를 만든다. |

## autonomous-ai-agents

| 스킬 | 기능 |
| --- | --- |
| claude-code | Claude Code CLI 에이전트에 기능 구현, 리팩터링, PR 리뷰 같은 코딩 작업을 위임한다. |
| codex | OpenAI Codex CLI 에이전트에 기능 구현, 리팩터링, 배치 이슈 수정을 위임한다. |
| hermes-agent | Hermes Agent 자체의 CLI, 설정, 게이트웨이, 툴, 스킬, 개발 구조를 설명하고 문제 해결에 쓴다. |
| opencode | OpenCode CLI 에이전트에 기능 구현, 리팩터링, 장기 자율 코딩 세션을 맡긴다. |

## creative

| 스킬                                | 기능                                                                  |
| --------------------------------- | ------------------------------------------------------------------- |
| architecture-diagram              | 소프트웨어 시스템/클라우드 구조를 다크 테마 SVG 아키텍처 다이어그램으로 만든다.                      |
| ascii-art                         | 텍스트나 이미지를 figlet/cowsay/boxes/toilet 등으로 ASCII 아트로 만든다.             |
| ascii-video                       | 영상·오디오·이미지를 컬러 ASCII 영상, GIF, 이미지 시퀀스, 오디오 반응형 비주얼로 변환한다.           |
| baoyu-comic                       | 지식/교육 내용을 여러 컷 만화 패널 구성과 이미지 생성 프롬프트로 바꾼다.                          |
| baoyu-infographic                 | 복잡한 정보를 21개 레이아웃/스타일 중 적절한 인포그래픽으로 구성한다.                            |
| cinematic-video-prompt-debugging  | AI 영상 결과가 평면적이거나 시선·블로킹·스케일이 틀릴 때 프롬프트를 디버깅한다.                      |
| design-md                         | DESIGN.md 형식의 디자인 시스템 문서를 작성·검증·이식한다.                               |
| english-word-thread-writer        | 한국인 학습자용 영어 단어 설명 스레드/카드뉴스를 어원·핵심 이미지 중심으로 작성한다.                    |
| excalidraw                        | Excalidraw JSON으로 손그림 스타일 다이어그램, 플로우차트, 시퀀스 다이어그램을 만든다.             |
| ideation                          | 도구는 있는데 방향이 없을 때 만들 프로젝트/콘텐츠 아이디어를 제약 기반으로 발상한다.                    |
| live-action-actor-profile-sheet   | 캐릭터 콘셉트를 실사 캐스팅 보드/배우 프로필 시트 이미지 프롬프트로 바꾼다.                         |
| manim-video                       | Manim으로 수학·알고리즘·기술 설명 애니메이션을 제작하는 파이프라인을 제공한다.                      |
| p5js                              | p5.js 기반 인터랙티브/제너러티브 아트, 데이터 시각화, 웹 캔버스 애니메이션을 만든다.                 |
| pixel-art                         | 이미지를 NES/Game Boy/PICO-8 같은 레트로 팔레트 픽셀아트로 변환하고 애니메이션화한다.            |
| policy-safe-character-prompting   | 차단될 수 있는 이미지 프롬프트를 의도와 스타일을 보존하면서 안전한 캐릭터 디자인 프롬프트로 재작성한다.          |
| popular-web-designs               | Stripe/Linear/Vercel/Notion/Airbnb 등 실제 웹 디자인 시스템 템플릿을 참고해 UI를 만든다. |
| songwriting-and-ai-music          | 작사·작곡·Suno류 AI 음악 프롬프트와 패러디/발음 트릭을 다룬다.                             |
| viral-shortform-ai-video-ideation | 쇼츠/릴스 바이럴 패턴을 조사해 AI 영상 네이티브 콘셉트와 실행 프레임으로 바꾼다.                     |

## data-science

| 스킬 | 기능 |
| --- | --- |
| jupyter-live-kernel | 라이브 Jupyter 커널을 써서 상태를 유지하며 데이터 분석/실험/중간 결과 확인을 반복한다. |

## devops

| 스킬 | 기능 |
| --- | --- |
| webhook-subscriptions | 외부 서비스가 Hermes를 호출하거나 알림을 보내도록 webhook 구독을 만들고 관리한다. |

## email

| 스킬 | 기능 |
| --- | --- |
| himalaya | himalaya CLI로 IMAP/SMTP 이메일 목록·읽기·작성·답장·검색·정리를 한다. |

## gaming

| 스킬 | 기능 |
| --- | --- |
| minecraft-modpack-server | CurseForge/Modrinth 모드팩 서버를 설치·튜닝·백업·방화벽 설정까지 진행한다. |
| pokemon-player | 헤드리스 에뮬레이션으로 포켓몬 게임 상태를 읽고 전략적으로 버튼 입력을 수행한다. |

## github

| 스킬 | 기능 |
| --- | --- |
| codebase-inspection | pygount로 코드베이스 LOC, 언어 비율, 주석 비율, 규모를 분석한다. |
| github-auth | git/gh CLI 기반 GitHub 인증, HTTPS 토큰, SSH 키, credential helper를 설정한다. |
| github-code-review | git diff와 PR 변경사항을 분석해 코드 리뷰와 인라인 코멘트를 수행한다. |
| github-issues | GitHub 이슈 검색·생성·라벨링·할당·PR 연결·종료를 관리한다. |
| github-pr-workflow | 브랜치 생성부터 커밋, PR 생성, CI 확인, 자동 수정, 병합까지 PR 생명주기를 관리한다. |
| github-repo-management | GitHub 저장소 clone/create/fork/remote/secrets/releases/workflows를 관리한다. |
| github-repo-quick-assessment | GitHub 저장소의 활동성, 문서, 릴리즈, 구현 신뢰도를 빠르게 평가한다. |

## leisure

| 스킬 | 기능 |
| --- | --- |
| find-nearby | OpenStreetMap 기반으로 주변 식당/카페/약국/장소를 좌표·주소·도시명에서 찾는다. |

## mcp

| 스킬 | 기능 |
| --- | --- |
| mcporter | mcporter CLI로 MCP 서버/툴을 나열, 설정, 인증, 호출하고 CLI/types를 만든다. |
| native-mcp | Hermes 내장 MCP 클라이언트로 외부 MCP 서버에 연결해 도구를 네이티브 툴처럼 등록한다. |

## media

| 스킬 | 기능 |
| --- | --- |
| gif-search | Tenor에서 GIF를 검색·다운로드해 채팅 반응이나 시각 자료로 쓴다. |
| heartmula | HeartMuLa 오픈소스 음악 생성 모델을 설치·실행해 가사와 태그로 곡을 만든다. |
| songsee | 오디오 파일에서 스펙트로그램, mel/chroma/MFCC/tempogram 같은 음악 특징 시각화를 만든다. |
| spotify | Spotify 재생/일시정지/검색/큐/플레이리스트/라이브러리/디바이스 상태를 제어한다. |
| youtube-content | YouTube 링크에서 자막을 가져와 요약, 챕터, 글, 스레드 등으로 변환한다. |

## mlops

| 스킬 | 기능 |
| --- | --- |
| audiocraft-audio-generation | AudioCraft/MusicGen/AudioGen으로 텍스트 기반 음악·효과음·멜로디 조건 생성 작업을 한다. |
| axolotl | Axolotl로 LLM 파인튜닝 YAML, LoRA/QLoRA, DPO/KTO/ORPO/GRPO 설정을 돕는다. |
| clip | CLIP으로 이미지-텍스트 매칭, 제로샷 이미지 분류, 크로스모달 검색을 수행한다. |
| dspy | DSPy로 프롬프트/모듈/RAG/에이전트 프로그램을 선언적으로 만들고 최적화한다. |
| evaluating-llms-harness | lm-evaluation-harness로 MMLU/HumanEval/GSM8K 등 벤치마크 평가를 수행한다. |
| fine-tuning-with-trl | TRL로 SFT, DPO, PPO, GRPO, reward model 등 RLHF/선호정렬 파인튜닝을 한다. |
| gguf-quantization | llama.cpp용 GGUF 변환과 2~8비트 양자화로 로컬 추론용 모델을 만든다. |
| grpo-rl-training | TRL 기반 GRPO/RL 파인튜닝으로 추론형·과제 특화 모델 학습을 설계한다. |
| guidance | Guidance로 정규식/문법 기반 구조화 생성, JSON/XML/code 형식 보장을 수행한다. |
| huggingface-hub | hf CLI로 Hugging Face 모델/데이터셋 검색·다운로드·업로드·Repo/Space 관리를 한다. |
| llama-cpp | llama.cpp와 GGUF 모델로 로컬 CPU/GPU 추론, HF 모델 탐색을 수행한다. |
| modal-serverless-gpu | Modal 서버리스 GPU로 ML 배치 작업, 모델 API, 온디맨드 GPU 실행을 만든다. |
| obliteratus | 오픈웨이트 모델의 거부/가드레일 특성을 해석·완화하는 연구형 모델 수술 도구를 다룬다. |
| outlines | Outlines로 Pydantic/문법 기반 JSON/XML/code 구조화 생성을 보장한다. |
| peft-fine-tuning | PEFT/LoRA/QLoRA 등 파라미터 효율 파인튜닝과 어댑터 운영을 다룬다. |
| pytorch-fsdp | PyTorch FSDP/FSDP2로 대규모 모델 분산 학습, sharding, mixed precision을 설정한다. |
| segment-anything-model | SAM으로 포인트/박스/마스크 프롬프트 기반 이미지 객체 분할을 수행한다. |
| serving-llms-vllm | vLLM으로 OpenAI 호환 LLM API를 고처리량/저지연으로 서빙한다. |
| stable-diffusion-image-generation | Diffusers 기반 Stable Diffusion 이미지 생성, img2img, inpainting, pipeline 구축을 한다. |
| unsloth | Unsloth로 LoRA/QLoRA 파인튜닝을 더 빠르고 적은 메모리로 수행한다. |
| weights-and-biases | W&B로 실험 로그, 대시보드, sweeps, 모델 레지스트리, 협업 추적을 한다. |
| whisper | Whisper로 음성 인식, 번역, 언어 감지, 다국어 전사를 수행한다. |

## note-taking

| 스킬 | 기능 |
| --- | --- |
| obsidian | Obsidian vault의 노트를 찾고, 읽고, 만들고, wikilink로 연결한다. |
| obsidian-personal-docs-human-guides | 원본 아카이브/지식베이스 근거를 바탕으로 사람이 실제로 쓰는 개인 작업 문서 문서를 만들고 검증한다. |
| toeic-vocab-study-system | 토익 단어 사진/메시지를 Day별 단어장, JSON 진도, 오답 누적, 복습 리마인더로 관리한다. |

## productivity

| 스킬 | 기능 |
| --- | --- |
| google-workspace | Gmail/Calendar/Drive/Contacts/Sheets/Docs를 Hermes OAuth/CLI/Python fallback으로 조작한다. |
| linear | Linear GraphQL API로 이슈, 프로젝트, 팀을 검색·생성·수정·정리한다. |
| maps | OSM/Overpass/OSRM 기반 지오코딩, 주변 장소, 길찾기, 거리/시간, 시간대를 조회한다. |
| nano-pdf | nano-pdf CLI로 PDF 텍스트 수정, 제목 변경, 페이지별 자연어 편집을 수행한다. |
| notion | Notion API를 curl로 호출해 페이지/DB/block을 검색·생성·업데이트한다. |
| ocr-and-documents | PDF/스캔 문서/DOCX/PPTX에서 텍스트를 추출하고 OCR 경로를 선택한다. |
| old-man-voca-threads-publishing | old_man_voca Threads 영어 단어 스레드를 로컬 helper로 발행하고 중복 단어를 피한다. |
| powerpoint | PPTX 읽기·생성·수정·병합·분할·템플릿·발표자료 작업 전체를 다룬다. |
| threads-api-troubleshooting | Meta Threads API/OAuth/429 Too Many Requests 문제를 진단하고 복구한다. |

## red-teaming

| 스킬 | 기능 |
| --- | --- |
| godmode | API 모델의 안전성/필터 취약성을 레드팀 관점에서 시험하는 기법을 다룬다. |

## research

| 스킬 | 기능 |
| --- | --- |
| arxiv | arXiv REST API로 논문을 검색하고 메타데이터/초록/원문 접근 흐름을 만든다. |
| blogwatcher | 블로그/RSS/Atom 피드 업데이트를 추적하고 새 글/읽음 상태를 관리한다. |
| insane-search-adaptive-web-access | 차단·JS·rate limit 사이트를 검색/API/브라우저/대체 접근으로 적응형 조사한다. |
| llm-wiki | Karpathy식 LLM Wiki 지식베이스를 ingest/query/lint하며 interlinked markdown으로 유지한다. |
| polymarket | Polymarket 예측시장 검색, 가격, orderbook, 가격 히스토리를 공개 API로 조회한다. |

## smart-home

| 스킬 | 기능 |
| --- | --- |
| openhue | OpenHue CLI로 Philips Hue 조명, 방, 장면, 밝기, 색, 색온도를 제어한다. |

## software-development

| 스킬 | 기능 |
| --- | --- |
| plan | 코드를 바로 수정하지 않고 .hermes/plans/에 구현 계획을 작성하는 계획 모드다. |
| requesting-code-review | 코드 변경 후 커밋/푸시/PR 전 정적 검사, 독립 리뷰, auto-fix loop를 수행한다. |
| subagent-driven-development | 독립 구현 작업을 delegate_task로 나누고 spec compliance/code quality 2단계 리뷰를 돌린다. |
| systematic-debugging | 버그/테스트 실패를 4단계로 원인 조사하고 이해 없이 수정하지 않도록 한다. |
| test-driven-development | 기능/버그 수정 전 RED-GREEN-REFACTOR 테스트 우선 개발을 강제한다. |
| writing-plans | 요구사항을 bite-sized task, 파일 경로, 코드 예시가 있는 구현 계획으로 바꾼다. |

## 읽는 법

- 같은 도구라도 어떤 skill이 로드되느냐에 따라 작업 방식이 달라집니다.
- 예를 들어 GitHub 작업은 `github-pr-workflow`, Obsidian 공개/비공개 정리는 `obsidian-personal-docs-human-guides`, 버그 조사는 `systematic-debugging`이 기준 절차를 제공합니다.
- 스킬 목록은 설치/업데이트에 따라 변하므로, 이 글은 기준 시점의 공개 스냅샷입니다.
