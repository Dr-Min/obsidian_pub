---
title: "Hermes Agent"
description: "A short guide to Hermes Agent commands, tools, and skills."
publish: true
draft: false
lang: "en"
translationKey: "hermes-agent-field-guide"
date: 2026-04-30
tags:
  - blog
  - en
  - ai
  - hermes-agent
  - automation
---

# Hermes Agent

Hermes Agent is a tool-using AI agent that can run in terminals, messaging platforms, IDEs, and automation workflows. It is not just a chatbot: it can read and write files, execute shell commands, automate browsers, schedule jobs, search prior sessions, and delegate work to subagents.


## The core vocabulary

| Term | Meaning | Examples |
| --- | --- | --- |
| CLI command | A terminal command that controls Hermes itself | `hermes doctor`, `hermes model`, `hermes skills list` |
| Slash command | A command typed inside a running session | `/model`, `/skill`, `/reset`, `/cron` |
| Toolset | A group of tools that can be enabled or disabled together | `terminal`, `file`, `browser`, `skills` |
| API tool | A callable function exposed to the agent in a session | `read_file`, `terminal`, `search_files`, `cronjob` |
| Skill | A reusable procedure document for a task | debugging, GitHub workflows, Obsidian publishing |
| Profile | An isolated Hermes runtime with separate config, sessions, skills, and memory | personal, work, experiment profiles |

## Why this matters

The words “command,” “tool,” and “skill” sound similar, but they operate at different layers.

- **Commands** control Hermes.
- **Tools** let Hermes act on the outside world.
- **Skills** teach Hermes how to perform a task reliably.

To use Hermes well, choose the model, the toolsets, and the relevant skills together.

## Start here

| Goal | Starting point |
| --- | --- |
| Check environment health | `hermes doctor`, `hermes status --all` |
| Change models | `hermes model` or `/model` |
| Inspect tools | `hermes tools list` or `/toolsets` |
| Inspect skills | `hermes skills list` or `/skills` |
| Check the messaging gateway | `hermes gateway status` or `/platforms` |
| Check scheduled jobs | `hermes cron list` or `/cron` |

## In this series

- [[en/blog/ai/hermes-agent/commands|Commands]] — terminal and in-session commands.
- [[en/blog/ai/hermes-agent/tools|Tools]] — how the agent acts outside chat.
- [[en/blog/ai/hermes-agent/skills|Skills]] — reusable workflows for specific tasks.
