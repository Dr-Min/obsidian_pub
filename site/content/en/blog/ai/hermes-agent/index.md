---
title: "Hermes Agent Field Guide: Commands, Tools, and Skills"
description: "A public field guide to Hermes Agent's CLI, slash commands, tools, toolsets, and installed skills."
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

# Hermes Agent Field Guide: Commands, Tools, and Skills

Hermes Agent is a tool-using AI agent that can run in terminals, messaging platforms, IDEs, and automation workflows. It is not just a chatbot: it can read and write files, execute shell commands, automate browsers, schedule jobs, search prior sessions, and delegate work to subagents.

This page is a public-facing field guide distilled from a private working reference. Private paths, credentials, message-routing details, and operational logs are intentionally excluded.

> Snapshot: 2026-04-29 22:14 KST
> Inventory covered here: 99 CLI commands, 48 slash commands, 20 toolsets, 30 API tools, and 90 installed skills.

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

- [[en/blog/ai/hermes-agent/commands|Hermes Agent Command Reference]] — CLI and slash commands.
- [[en/blog/ai/hermes-agent/tools|Hermes Agent Tools and Toolsets]] — the tool surface available to an agent session.
- [[en/blog/ai/hermes-agent/skills|Hermes Agent Installed Skills Catalog]] — the installed skill catalog grouped by category.
