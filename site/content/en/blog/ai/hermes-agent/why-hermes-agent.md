---
title: "Why Use Hermes Agent If You Already Have Codex?"
description: "A practical comparison between Codex and Hermes Agent, plus the basic flow for connecting Hermes Agent to Telegram."
publish: true
draft: false
lang: "en"
translationKey: "why-hermes-agent"
date: 2026-05-11
tags:
  - blog
  - en
  - ai
  - hermes-agent
  - codex
  - telegram
  - automation
---

# Why Use Hermes Agent If You Already Have Codex?

One of the first questions people ask about Hermes Agent is simple:

“Why not just use Codex?”

That is a fair question. If all you want to do is code, Codex is probably the simpler choice. It is good at reading a repository, editing code, running tests, refactoring, and reviewing changes.

But Hermes Agent is not interesting because it is “a better Codex.” The point is different.

Codex is closer to a coding worker. Hermes Agent is closer to a personal AI assistant and automation layer that can connect messaging platforms, files, the web, shell commands, schedules, memory, and reusable skills.

## Codex and Hermes Agent are not the same kind of tool

Codex is strong for software development work:

- reading a repo
- editing code
- running tests
- fixing bugs
- refactoring
- reviewing PRs
- inspecting install scripts

Hermes Agent sits at a broader layer.

It is a tool-using agent that can read and write files, run terminal commands, browse the web, create scheduled jobs, remember preferences, load reusable workflows, and connect to messaging platforms such as Telegram or Discord.

So Hermes Agent is not best understood as a Codex replacement.

A better distinction is this:

- Codex is a coding agent you open when you are developing software.
- Hermes Agent is a personal work agent you can call from your messaging app.

If you only need coding, use Codex. If you want link summaries, note taking, reminders, web research, file organization, and recurring automation, Hermes Agent becomes more interesting.

## Why use Hermes Agent?

### 1. You can call it from Telegram

One of the most useful parts of Hermes Agent is messaging integration.

When the gateway is running, you can send work to Hermes from Telegram without opening a terminal.

For example:

```text
Read this link and summarize the key points.
Look at this image and add the deadline to my reminders.
Save today's work as a note.
Read this error log and list likely causes.
Remind me about this tomorrow at 9 AM.
```

That is not just coding assistance. That is personal workflow automation.

### 2. It can work with files and notes

Hermes Agent can use tools that read and write files.

That means it can do more than answer a question. It can save the result into Markdown, update an existing document, add links to an index, or leave a processing log.

If you use Obsidian, for example, Hermes can turn a web source into a structured note and place it in the right folder.

### 3. It can accumulate memory and skills

Repeating the same instructions is tedious.

Where should notes go? What style do you prefer? Which verification steps matter? Which workflow should be used for a recurring task?

Hermes Agent can store stable preferences and reusable procedures. In Hermes terms, tools are the hands; skills are the operating manuals.

Over time, the agent becomes less like a blank chatbot and more like an assistant that knows your working style.

### 4. It can run scheduled and recurring work

Hermes Agent can create cron jobs for scheduled tasks.

That means it can send reminders, check sources periodically, or run recurring workflows.

This moves it beyond a “reply right now” assistant. It can become a background work assistant.

### 5. It connects work outside the code editor

A lot of useful AI work is not code:

- organizing documents
- researching web sources
- analyzing images
- checking email
- managing reminders
- saving notes
- drafting blog posts
- automating repeated tasks

For these workflows, an agent that connects messaging, files, browsers, and schedules is often more useful than a tool that lives only inside a coding context.

## Installing Hermes Agent

The official GitHub repository is:

```text
https://github.com/NousResearch/hermes-agent
```

On Linux, macOS, WSL2, and Termux, you can use the install script:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

On Windows PowerShell, use:

```powershell
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

After installation, check the environment:

```bash
hermes --version
hermes setup
hermes model
hermes tools
hermes doctor
```

You can also ask Codex to help with the install:

```text
Read this GitHub repo and help me install Hermes Agent for my environment.
Repo: https://github.com/NousResearch/hermes-agent
Check the README.md and the install script for my OS first.
Do not print API keys, bot tokens, .env contents, or auth files.
Ask before running destructive commands, permission changes, or global config changes.
After installation, verify with hermes --version, hermes doctor, and hermes setup.
```

Here Codex is useful as an installation helper. After Hermes is installed, the real point is connecting it to Telegram and using it as a long-running assistant.

## Connecting Hermes Agent to Telegram

The basic Telegram flow is:

1. Create a Telegram bot with BotFather.
2. Find your numeric Telegram user ID.
3. Run `hermes gateway setup` and enter the Telegram settings.
4. Test with `hermes gateway`.
5. If it works, install and start the gateway service.
6. Use `/sethome` in Telegram to set the default channel.

### Create a bot with BotFather

In Telegram, search for `@BotFather`.

Send `/newbot`, then choose a bot name and username. The username usually needs to end in `bot`.

BotFather will give you a token. Do not expose this token in a video, screenshot, blog post, or public repository.

### Find your Telegram user ID

Hermes can restrict who is allowed to use the bot.

For this, you need your numeric Telegram user ID, not just your username. Bots such as `@userinfobot` can show it to you.

### Configure the Hermes gateway

Run:

```bash
hermes gateway setup
```

Choose Telegram, then enter the bot token and allowed user ID.

Conceptually, the environment values look like this:

```bash
TELEGRAM_BOT_TOKEN=***
TELEGRAM_ALLOWED_USERS=123456789
```

Never publish the real token.

### Run the gateway

Test it in the foreground first:

```bash
hermes gateway
```

Send a message to the Telegram bot. If Hermes replies, the connection works.

For long-running use, install and start the gateway service:

```bash
hermes gateway install
hermes gateway start
hermes gateway status
```

Common Telegram commands include:

```text
/sethome
/status
/help
```

`/sethome` marks the current chat as the default delivery channel for scheduled jobs and automation output.

## Group chat note: privacy mode

If you use the bot in a Telegram group, understand privacy mode.

By default, a Telegram bot may not receive every group message. It may only see slash commands, direct replies, and messages that mention it.

If you want the bot to read all group messages, disable Group Privacy in BotFather or make the bot an admin. After changing privacy mode, you may need to remove and re-add the bot to the group.

## Security basics

Hermes Agent is powerful, so it deserves some caution.

At minimum:

- Do not expose bot tokens.
- Do not expose API keys or `.env` files.
- Restrict allowed Telegram user IDs.
- Ask before destructive shell commands or permission changes.
- Understand what the bot can read in group chats.
- Remove local paths, secrets, tokens, and personal data before publishing blog posts or videos.

An AI agent that can act on your computer is useful precisely because it has access. Treat that access carefully.

## Summary

Codex and Hermes Agent solve different problems.

Codex is a coding worker. It is great for repositories, code changes, tests, and reviews.

Hermes Agent is a personal AI assistant and automation layer. It can be called from Telegram, work with files, read the web, save notes, create reminders, and run scheduled workflows.

So the practical rule is simple:

If you only need coding, use Codex.

If you want an AI assistant connected to your broader working environment, try Hermes Agent.

In one sentence:

**Codex is a coding worker. Hermes Agent is a personal AI assistant you can call from Telegram.**
