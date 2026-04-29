---
title: "Hermes Agent 명령어"
description: "Hermes Agent를 터미널과 대화 세션에서 조작하는 CLI 커맨드와 슬래시 명령어를 정리합니다."
publish: true
draft: false
lang: "ko"
translationKey: "hermes-agent-commands"
date: 2026-04-30
tags:
  - blog
  - ko
  - ai
  - hermes-agent
  - cli
  - commands
---

# Hermes Agent 명령어

Hermes에는 두 종류의 명령 계층이 있습니다.

- 터미널에서 쓰는 **CLI 커맨드**: 설치, 설정, gateway, profile, cron, skills 등을 관리합니다.
- 대화 중 쓰는 **슬래시 명령어**: 현재 세션의 모델, 도구, 스킬, 상태, 재시작 등을 빠르게 제어합니다.


## 가장 자주 쓰는 명령

| 목적 | 명령 |
| --- | --- |
| 환경 진단 | `hermes doctor`, `hermes status --all` |
| 모델 변경 | `hermes model`, `/model` |
| 도구 확인 | `hermes tools list`, `/toolsets` |
| 스킬 확인 | `hermes skills list`, `/skills` |
| 스킬 로드 | `/skill <name>` |
| gateway 재시작 | `hermes gateway restart`, `/restart` |
| cron 확인 | `hermes cron list`, `/cron` |
| 세션 새로 시작 | `/new`, `/reset` |

## CLI 커맨드

| 커맨드 | 기능 |
| --- | --- |
| hermes | 기본 대화형 채팅을 시작한다. 서브커맨드가 없으면 chat으로 동작한다. |
| hermes --version / -V | Hermes 버전을 출력한다. |
| hermes --resume / -r SESSION | 세션 ID 또는 제목으로 이전 세션을 이어간다. |
| hermes --continue / -c [NAME] | 이름 또는 가장 최근 세션을 이어간다. |
| hermes --worktree / -w | 병렬 코딩 에이전트용 격리 git worktree 모드를 사용한다. |
| hermes --skills / -s SKILL | 시작 시 특정 스킬을 미리 로드한다. 반복 또는 콤마 구분 가능. |
| hermes --profile / -p NAME | 지정한 프로필의 설정/메모리/세션/스킬을 사용한다. |
| hermes --yolo | 위험 명령 승인 절차를 건너뛴다. 매우 조심해서 쓴다. |
| hermes --pass-session-id | 세션 ID를 시스템 프롬프트에 포함한다. |
| hermes chat | 대화형 또는 단발 질의 채팅을 실행한다. |
| hermes chat -q / --query TEXT | 비대화형 단발 질문을 실행하고 종료한다. |
| hermes chat -m / --model MODEL | 사용할 모델을 지정한다. |
| hermes chat -t / --toolsets LIST | 사용할 toolset 목록을 콤마로 지정한다. |
| hermes chat --provider PROVIDER | openrouter/anthropic/nous 등 provider를 강제한다. |
| hermes chat -v / --verbose | 상세 출력 모드로 실행한다. |
| hermes chat -Q / --quiet | 배너, 스피너, 툴 미리보기를 숨긴다. |
| hermes chat --checkpoints | 파일시스템 체크포인트와 /rollback 기능을 켠다. |
| hermes chat --source TAG | 세션 source 태그를 지정한다. |
| hermes setup [section] | model/terminal/gateway/tools/agent 설정 wizard를 실행한다. |
| hermes model | 모델과 provider를 인터랙티브로 선택한다. |
| hermes config | 현재 config를 출력한다. |
| hermes config edit | config.yaml을 에디터로 연다. |
| hermes config set KEY VAL | 특정 config 값을 설정한다. |
| hermes config path | config.yaml 경로를 출력한다. |
| hermes config env-path | .env 경로를 출력한다. |
| hermes config check | 누락되거나 오래된 설정을 검사한다. |
| hermes config migrate | 새 옵션 기준으로 config를 마이그레이션한다. |
| hermes login [--provider P] | nous/openai-codex 등 OAuth 로그인을 수행한다. |
| hermes logout | 저장된 인증을 지운다. |
| hermes doctor [--fix] | 의존성/설정 상태를 진단하고 가능하면 고친다. |
| hermes status [--all] | 구성요소 상태를 보여준다. |
| hermes tools | 툴 enable/disable curses UI를 연다. |
| hermes tools list | 모든 toolset과 활성 상태를 나열한다. |
| hermes tools enable NAME | 특정 toolset을 켠다. |
| hermes tools disable NAME | 특정 toolset을 끈다. |
| hermes skills list | 설치된 스킬을 나열한다. |
| hermes skills search QUERY | 스킬 허브에서 검색한다. |
| hermes skills install ID | 스킬을 설치한다. |
| hermes skills inspect ID | 설치하지 않고 스킬 내용을 미리 본다. |
| hermes skills config | 플랫폼별 스킬 활성화를 설정한다. |
| hermes skills check | 스킬 업데이트 여부를 확인한다. |
| hermes skills update | 오래된 스킬을 업데이트한다. |
| hermes skills uninstall N | 허브 스킬을 삭제한다. |
| hermes skills publish PATH | 스킬을 registry에 publish한다. |
| hermes skills browse | 사용 가능한 스킬 전체 카탈로그를 탐색한다. |
| hermes skills tap add REPO | GitHub repo를 스킬 source로 추가한다. |
| hermes mcp serve | Hermes를 MCP server로 실행한다. |
| hermes mcp add NAME | MCP server를 --url 또는 --command로 추가한다. |
| hermes mcp remove NAME | 등록된 MCP server를 제거한다. |
| hermes mcp list | 설정된 MCP server를 나열한다. |
| hermes mcp test NAME | MCP 연결을 테스트한다. |
| hermes mcp configure NAME | MCP tool 선택을 토글/설정한다. |
| hermes gateway run | 메시징 gateway를 foreground로 실행한다. |
| hermes gateway install | gateway를 background service로 설치한다. |
| hermes gateway start / stop | gateway service를 시작/중지한다. |
| hermes gateway restart | gateway service를 재시작한다. |
| hermes gateway status | gateway 상태를 확인한다. |
| hermes gateway setup | Telegram/Discord/Slack 등 platform 설정 wizard를 연다. |
| hermes sessions list | 최근 세션 목록을 보여준다. |
| hermes sessions browse | 인터랙티브 세션 선택기를 연다. |
| hermes sessions export OUT | 세션을 JSONL로 export한다. |
| hermes sessions rename ID T | 세션 제목을 바꾼다. |
| hermes sessions delete ID | 세션을 삭제한다. |
| hermes sessions prune | 오래된 세션을 정리한다. |
| hermes sessions stats | 세션 저장소 통계를 보여준다. |
| hermes cron list | cron job 목록을 보여준다. |
| hermes cron create SCHED | '30m', 'every 2h', '0 9 * * *' 같은 스케줄로 job을 만든다. |
| hermes cron edit ID | 스케줄, 프롬프트, delivery를 수정한다. |
| hermes cron pause / resume ID | cron job을 일시정지/재개한다. |
| hermes cron run ID | 다음 tick에 job을 즉시 실행하도록 한다. |
| hermes cron remove ID | cron job을 삭제한다. |
| hermes cron status | scheduler 상태를 확인한다. |
| hermes webhook subscribe N | /webhooks/<name> route를 만들어 외부 POST를 받는다. |
| hermes webhook list | webhook 구독 목록을 보여준다. |
| hermes webhook remove NAME | webhook 구독을 삭제한다. |
| hermes webhook test NAME | 테스트 POST를 보낸다. |
| hermes profile list | 프로필 목록을 보여준다. |
| hermes profile create NAME | 새 프로필을 만든다. clone/clone-all/clone-from 옵션 가능. |
| hermes profile use NAME | sticky default 프로필로 설정한다. |
| hermes profile delete NAME | 프로필을 삭제한다. |
| hermes profile show NAME | 프로필 상세를 보여준다. |
| hermes profile alias NAME | 프로필 wrapper script alias를 관리한다. |
| hermes profile rename A B | 프로필 이름을 바꾼다. |
| hermes profile export NAME | 프로필을 tar.gz로 export한다. |
| hermes profile import FILE | 프로필 archive를 import한다. |
| hermes auth add | credential pool용 인증 정보를 인터랙티브로 추가한다. |
| hermes auth list [PROVIDER] | provider별 credential pool을 나열한다. |
| hermes auth remove P INDEX | provider와 index로 credential을 제거한다. |
| hermes auth reset PROVIDER | provider의 exhaustion 상태를 초기화한다. |
| hermes insights [--days N] | 사용량 analytics를 보여준다. |
| hermes update | Hermes를 최신 버전으로 업데이트한다. |
| hermes pairing list / approve / revoke | DM authorization pairing을 나열/승인/취소한다. |
| hermes plugins list / install / remove | 플러그인을 나열/설치/삭제한다. |
| hermes honcho setup / status | Honcho memory integration을 설정/확인한다. |
| hermes memory setup / status / off | memory provider를 설정/확인/비활성화한다. |
| hermes completion bash\|zsh | shell completion 스크립트를 생성한다. |
| hermes acp | IDE integration용 ACP server를 실행한다. |
| hermes claw migrate | OpenClaw에서 Hermes로 migration한다. |
| hermes uninstall | Hermes를 제거한다. |

## 주요 설정 파일과 디렉터리

| 경로 | 기능 |
|---|---|
| `~/.hermes/config.yaml` 또는 `HERMES_HOME/config.yaml` | 모델, provider, agent, tool, gateway 등 메인 설정 |
| `~/.hermes/.env` 또는 `HERMES_HOME/.env` | API key, token 같은 비밀값. 공개 글이나 노트에 값 복사 금지 |
| `$HERMES_HOME/skills/` | 설치된 스킬 문서 |
| `$HERMES_HOME/sessions/` | 세션 transcript와 session index |
| `$HERMES_HOME/logs/` | gateway/error log |
| `$HERMES_HOME/auth.json` | OAuth token과 credential pool |
| `$HERMES_HOME/hermes-agent/` | git 설치된 Hermes source code |

## Config section 요약

| section | 주로 조정하는 것 |
|---|---|
| `model` | default model, provider, base_url, api_key, context_length |
| `agent` | max_turns, tool_use_enforcement |
| `terminal` | backend, cwd, timeout |
| `compression` | context compression threshold/ratio |
| `display` | skin, tool_progress, reasoning/cost 표시 |
| `stt` | voice-to-text provider/model |
| `tts` | text-to-speech provider |
| `memory` | memory/profile backend와 활성화 |
| `security` | Tirith, website blocklist |
| `delegation` | subagent 모델/provider/max_iterations/reasoning |
| `checkpoints` | filesystem snapshot/rollback 설정 |

## Provider 목록

아래 표는 **환경변수 이름과 인증 방식만** 정리합니다. 실제 API key 값은 절대 공개 글이나 노트에 복사하면 안 됩니다.

| Provider | 인증/환경변수 |
| --- | --- |
| OpenRouter | OPENROUTER_API_KEY |
| Anthropic | ANTHROPIC_API_KEY |
| Nous Portal | hermes auth |
| OpenAI Codex | hermes auth |
| GitHub Copilot | COPILOT_GITHUB_TOKEN |
| Google Gemini | GOOGLE_API_KEY 또는 GEMINI_API_KEY |
| DeepSeek | DEEPSEEK_API_KEY |
| xAI / Grok | XAI_API_KEY |
| Hugging Face | HF_TOKEN |
| Z.AI / GLM | GLM_API_KEY |
| MiniMax | MINIMAX_API_KEY |
| MiniMax CN | MINIMAX_CN_API_KEY |
| Kimi / Moonshot | KIMI_API_KEY |
| Alibaba / DashScope | DASHSCOPE_API_KEY |
| Xiaomi MiMo | XIAOMI_API_KEY |
| Kilo Code | KILOCODE_API_KEY |
| AI Gateway / Vercel | AI_GATEWAY_API_KEY |
| OpenCode Zen | OPENCODE_ZEN_API_KEY |
| OpenCode Go | OPENCODE_GO_API_KEY |
| Qwen OAuth | hermes login --provider qwen-oauth |
| Custom endpoint | model.base_url + model.api_key |
| GitHub Copilot ACP | COPILOT_CLI_PATH 또는 Copilot CLI |

## 세션 슬래시 명령어 전체 목록

| 슬래시 명령어 | 기능 |
| --- | --- |
| /new 또는 /reset | 새 세션을 시작한다. |
| /clear | CLI 화면을 지우고 새 세션을 시작한다. |
| /retry | 마지막 사용자 메시지를 다시 보낸다. |
| /undo | 마지막 exchange를 제거한다. |
| /title [name] | 현재 세션 제목을 붙인다. |
| /compress | 현재 context를 수동 압축한다. |
| /stop | background process를 종료한다. |
| /rollback [N] | filesystem checkpoint로 되돌린다. |
| /background <prompt> | 프롬프트를 백그라운드 작업으로 실행한다. |
| /queue <prompt> | 다음 turn에 실행할 요청을 큐에 넣는다. |
| /resume [name] | 이름 있는 세션을 이어간다. |
| /config | CLI에서 config를 보여준다. |
| /model [name] | 모델을 보여주거나 변경한다. |
| /personality [name] | personality를 설정한다. |
| /reasoning [level] | reasoning level을 none/minimal/low/medium/high/xhigh/show/hide로 설정한다. |
| /verbose | off → new → all → verbose 순서로 상세 출력을 순환한다. |
| /voice [on\|off\|tts] | voice mode, always-TTS, off를 전환한다. |
| /yolo | approval bypass를 토글한다. |
| /skin [name] | CLI 테마를 바꾼다. |
| /statusbar | CLI status bar를 토글한다. |
| /tools | CLI tool 관리 화면을 연다. |
| /toolsets | toolset 목록을 보여준다. |
| /skills | 스킬 검색/설치 UI를 연다. |
| /skill <name> | 현재 세션에 특정 스킬을 로드한다. |
| /cron | cron job 관리 UI를 연다. |
| /reload-mcp | MCP server를 다시 로드한다. |
| /plugins | 플러그인 목록을 보여준다. |
| /approve | gateway에서 pending command를 승인한다. |
| /deny | gateway에서 pending command를 거절한다. |
| /restart | gateway를 재시작한다. |
| /sethome | 현재 채팅을 home channel로 설정한다. |
| /update | gateway에서 Hermes 업데이트를 실행한다. |
| /platforms 또는 /gateway | 플랫폼 연결 상태를 보여준다. |
| /branch 또는 /fork | 현재 세션을 branch/fork한다. |
| /btw | 메인 작업을 끊지 않는 임시 사이드 질문을 한다. |
| /fast | priority/fast processing을 토글한다. |
| /browser | CDP browser connection을 연다. |
| /history | CLI 대화 기록을 보여준다. |
| /save | 대화를 파일로 저장한다. |
| /paste | clipboard 이미지를 첨부한다. |
| /image | local image file을 첨부한다. |
| /help | 도움말/명령어 목록을 보여준다. |
| /commands [page] | gateway에서 모든 명령어를 페이지별로 탐색한다. |
| /usage | token usage를 보여준다. |
| /insights [days] | 사용량 analytics를 보여준다. |
| /status | gateway에서 현재 세션 정보를 보여준다. |
| /profile | active profile 정보를 보여준다. |
| /quit / /exit / /q | CLI를 종료한다. |

## 주의할 점

- `--yolo`와 `/yolo`는 위험 명령 승인 절차를 줄이므로 신뢰하는 로컬 환경에서만 조심해서 사용합니다.
- `.env`, `auth.json`, OAuth token, API key 값은 공개 문서에 넣지 않습니다.
- toolset과 skill 변경은 보통 새 세션 또는 `/reset` 이후 안정적으로 반영됩니다.
