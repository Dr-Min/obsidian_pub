---
title: "Hermes Agent Tools"
description: "A public reference for Hermes Agent toolsets and callable API tools."
publish: true
draft: false
lang: "en"
translationKey: "hermes-agent-tools"
date: 2026-04-30
tags:
  - blog
  - en
  - ai
  - hermes-agent
  - tools
  - toolsets
---

# Hermes Agent Tools

A toolset is the unit that gives Hermes a class of capabilities. If the agent needs to edit files, it needs file tools. If it needs to run builds, it needs terminal tools. If it needs to inspect a web UI, it needs browser tools.


### Toolsets

Enable/disable via `hermes tools` (interactive) or `hermes tools enable/disable NAME`.

| Toolset | What it provides |
|---------|-----------------|
| `web` | Web search and content extraction |
| `browser` | Browser automation (Browserbase, Camofox, or local Chromium) |
| `terminal` | Shell commands and process management |
| `file` | File read/write/search/patch |
| `code_execution` | Sandboxed Python execution |
| `vision` | Image analysis |
| `image_gen` | AI image generation |
| `tts` | Text-to-speech |
| `skills` | Skill browsing and management |
| `memory` | Persistent cross-session memory |
| `session_search` | Search past conversations |
| `delegation` | Subagent task delegation |
| `cronjob` | Scheduled task management |
| `clarify` | Ask user clarifying questions |
| `messaging` | Cross-platform message sending |
| `search` | Web search only (subset of `web`) |
| `todo` | In-session task planning and tracking |
| `rl` | Reinforcement learning tools (off by default) |
| `moa` | Mixture of Agents (off by default) |
| `homeassistant` | Smart home control (off by default) |

Tool changes take effect on `/reset` (new session). They do NOT apply mid-conversation to preserve prompt caching.

---

## Callable API Tools

The exact callable tool surface depends on profile, platform, and enabled toolsets.

| API tool | What it does |
| --- | --- |
| `browser_navigate` | Open a URL and return a compact page snapshot. |
| `browser_snapshot` | Read the current page's accessibility tree. |
| `browser_click` | Click an element from a browser snapshot. |
| `browser_type` | Type text into a browser input. |
| `browser_press` | Press a keyboard key in the browser. |
| `browser_scroll` | Scroll the page up or down. |
| `browser_back` | Navigate back in browser history. |
| `browser_console` | Read console logs or evaluate JavaScript in the page. |
| `browser_get_images` | Collect images on the current page. |
| `browser_vision` | Screenshot and visually analyze the current page. |
| `clarify` | Ask the user a structured clarification question. |
| `cronjob` | Create, list, update, pause, resume, remove, or run scheduled jobs. |
| `delegate_task` | Spawn isolated subagents for independent work. |
| `image_generate` | Generate images from text prompts. |
| `memory` | Add, replace, or remove durable user/profile memory. |
| `patch` | Apply targeted fuzzy replacements or multi-file patches. |
| `process` | Manage background terminal processes. |
| `read_file` | Read text files with line numbers and pagination. |
| `search_files` | Search file names or file contents. |
| `send_message` | Send messages to connected platforms. |
| `session_search` | Search or browse prior conversation sessions. |
| `skills_list` | List installed skills. |
| `skill_view` | Read skill instructions and linked files. |
| `skill_manage` | Create, patch, edit, or delete skills. |
| `terminal` | Execute shell commands and builds. |
| `text_to_speech` | Convert text into audio. |
| `todo` | Track the current session's task list. |
| `vision_analyze` | Analyze images from URLs or local files. |
| `write_file` | Create or overwrite text files. |
| `multi_tool_use.parallel` | Run independent developer tool calls in parallel. |

## Practical routing

| Situation | Start with |
| --- | --- |
| Read a file | `read_file` |
| Search file names or contents | `search_files` |
| Create or edit files | `write_file`, `patch` |
| Run builds, tests, or deployment commands | `terminal`, `process` |
| Inspect a web UI | `browser_*` |
| Analyze images or screenshots | `vision_analyze`, `browser_vision` |
| Schedule repeated work | `cronjob` |
| Split independent workstreams | `delegate_task` |
| Recall prior conversations | `session_search` |

## Operating principle

More tools are not always better. Enable the capabilities required by the task, verify side effects, and treat deployment, file writes, external messages, and public posts as actions that deserve explicit checks.
