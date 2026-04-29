---
title: "Hermes Agent Skills"
description: "A category guide to Hermes Agent skills."
publish: true
draft: false
lang: "en"
translationKey: "hermes-agent-skills"
date: 2026-04-30
tags:
  - blog
  - en
  - ai
  - hermes-agent
  - skills
  - catalog
---

# Hermes Agent Skills

A skill is a reusable procedure that tells Hermes how to perform a class of work. If tools are the agent's hands, skills are the operating manuals it loads for specific tasks.


## dogfood/QA

| Skill | What it is for |
| --- | --- |
| `dogfood` | Systematic exploratory QA testing of web applications — find bugs, capture evidence, and generate structured reports |

## autonomous-ai-agents

| Skill | What it is for |
| --- | --- |
| `claude-code` | Delegate coding tasks to Claude Code (Anthropic's CLI agent). Use for building features, refactoring, PR reviews, and iterative coding. Requires the claude CLI installed. |
| `codex` | Delegate coding tasks to OpenAI Codex CLI agent. Use for building features, refactoring, PR reviews, and batch issue fixing. Requires the codex CLI and a git repository. |
| `hermes-agent` | Complete guide to using and extending Hermes Agent — CLI usage, setup, configuration, spawning additional agents, gateway platforms, skills, voice, tools, profiles, and a concise contributor reference. Load this skill when helping users configure Hermes, troubleshoot issues, spawn agent instances, or make code contributions. |
| `opencode` | Delegate coding tasks to OpenCode CLI agent for feature implementation, refactoring, PR review, and long-running autonomous sessions. Requires the opencode CLI installed and authenticated. |

## creative

| Skill | What it is for |
| --- | --- |
| `architecture-diagram` | Generate dark-themed SVG diagrams of software systems and cloud infrastructure as standalone HTML files with inline SVG graphics. Semantic component colors (cyan=frontend, emerald=backend, violet=database, amber=cloud/AWS, rose=security, orange=message bus), JetBrains Mono font, grid background. Best suited for software architecture, cloud/VPC topology, microservice maps, service-mesh diagrams, database + API layer diagrams, security groups, message buses — anything that fits a tech-infra deck with a dark aesthetic. If a more specialized diagramming skill exists for the subject (scientific, educational, hand-drawn, animated, etc.), prefer that — otherwise this skill can also serve as a general-purpose SVG diagram fallback. Based on Cocoon AI's architecture-diagram-generator (MIT). |
| `ascii-art` | Generate ASCII art using pyfiglet (571 fonts), cowsay, boxes, toilet, image-to-ascii, remote APIs (asciified, ascii.co.uk), and LLM fallback. No API keys required. |
| `ascii-video` | Production pipeline for ASCII art video — any format. Converts video/audio/images/generative input into colored ASCII character video output (MP4, GIF, image sequence). Covers: video-to-ASCII conversion, audio-reactive music visualizers, generative ASCII art animations, hybrid video+audio reactive, text/lyrics overlays, real-time terminal rendering. Use when users request: ASCII video, text art video, terminal-style video, character art animation, retro text visualization, audio visualizer in ASCII, converting video to ASCII art, matrix-style effects, or any animated ASCII output. |
| `baoyu-comic` | Knowledge comic creator supporting multiple art styles and tones. Creates original educational comics with detailed panel layouts and sequential image generation. Use when user asks to create "知识漫画", "教育漫画", "biography comic", "tutorial comic", or "Logicomix-style comic". |
| `baoyu-infographic` | Generate professional infographics with 21 layout types and 21 visual styles. Analyzes content, recommends layout×style combinations, and generates publication-ready infographics. Use when user asks to create "infographic", "visual summary", "信息图", "可视化", or "高密度信息大图". |
| `cinematic-video-prompt-debugging` | Refine scene-generation prompts when video models produce flat TV-drama lighting, wrong eyelines, incorrect blocking, or confused character scale/placement. |
| `design-md` | Author, validate, diff, and export DESIGN.md files — Google's open-source format spec that gives coding agents a persistent, structured understanding of a design system (tokens + rationale in one file). Use when building a design system, porting style rules between projects, generating UI with consistent brand, or auditing accessibility/contrast. |
| `english-word-thread-writer` | Writes Korean learner-friendly English word threads and card-style explanations that connect multiple meanings through one core image. |
| `excalidraw` | Create hand-drawn style diagrams using Excalidraw JSON format. Generate .excalidraw files for architecture diagrams, flowcharts, sequence diagrams, concept maps, and more. Files can be opened at excalidraw.com or uploaded for shareable links. |
| `ideation` | Generate project ideas through creative constraints. Use when the user says 'I want to build something', 'give me a project idea', 'I'm bored', 'what should I make', 'inspire me', or any variant of 'I have tools but no direction'. Works for code, art, hardware, writing, tools, and anything that can be made. |
| `live-action-actor-profile-sheet` | Turns a character concept into a final image prompt for a live-action casting board and actor profile sheet. |
| `manim-video` | Production pipeline for mathematical and technical animations using Manim Community Edition. Creates 3Blue1Brown-style explainer videos, algorithm visualizations, equation derivations, architecture diagrams, and data stories. Use when users request: animated explanations, math animations, concept visualizations, algorithm walkthroughs, technical explainers, 3Blue1Brown style videos, or any programmatic animation with geometric/mathematical content. |
| `p5js` | Production pipeline for interactive and generative visual art using p5.js. Creates browser-based sketches, generative art, data visualizations, interactive experiences, 3D scenes, audio-reactive visuals, and motion graphics — exported as HTML, PNG, GIF, MP4, or SVG. Covers: 2D/3D rendering, noise and particle systems, flow fields, shaders (GLSL), pixel manipulation, kinetic typography, WebGL scenes, audio analysis, mouse/keyboard interaction, and headless high-res export. Use when users request: p5.js sketches, creative coding, generative art, interactive visualizations, canvas animations, browser-based visual art, data viz, shader effects, or any p5.js project. |
| `pixel-art` | Convert images into retro pixel art with hardware-accurate palettes (NES, Game Boy, PICO-8, C64, etc.), and animate them into short videos. Presets cover arcade, SNES, and 10+ era-correct looks. Use `clarify` to let the user pick a style before generating. |
| `policy-safe-character-prompting` | Rewrite blocked image prompts into safer character-design prompts while preserving the user's intended visual style, layout, and annotation requirements. |
| `popular-web-designs` | 54 production-quality design systems extracted from real websites. Load a template to generate HTML/CSS that matches the visual identity of sites like Stripe, Linear, Vercel, Notion, Airbnb, and more. Each template includes colors, typography, components, layout rules, and ready-to-use CSS values. |
| `songwriting-and-ai-music` | Songwriting craft, AI music generation prompts (Suno focus), parody/adaptation techniques, phonetic tricks, and lessons learned. These are tools and ideas, not rules. Break any of them when the art calls for it. |
| `viral-shortform-ai-video-ideation` | Research and synthesize viral short-form video patterns for YouTube Shorts and Instagram Reels, then translate them into AI-video-native concepts and prompt/execution frameworks. |

## data-science

| Skill | What it is for |
| --- | --- |
| `jupyter-live-kernel` | Use a live Jupyter kernel for stateful, iterative Python execution via hamelnb. Load this skill when the task involves exploration, iteration, or inspecting intermediate results — data science, ML experimentation, API exploration, or building up complex code step-by-step. Uses terminal to run CLI commands against a live Jupyter kernel. No new tools required. |

## devops

| Skill | What it is for |
| --- | --- |
| `webhook-subscriptions` | Create and manage webhook subscriptions for event-driven agent activation, or for direct push notifications (zero LLM cost). Use when the user wants external services to trigger agent runs OR push notifications to chats. |

## email

| Skill | What it is for |
| --- | --- |
| `himalaya` | CLI to manage emails via IMAP/SMTP. Use himalaya to list, read, write, reply, forward, search, and organize emails from the terminal. Supports multiple accounts and message composition with MML (MIME Meta Language). |

## gaming

| Skill | What it is for |
| --- | --- |
| `minecraft-modpack-server` | Set up a modded Minecraft server from a CurseForge/Modrinth server pack zip. Covers NeoForge/Forge install, Java version, JVM tuning, firewall, LAN config, backups, and launch scripts. |
| `pokemon-player` | Play Pokemon games autonomously via headless emulation. Starts a game server, reads structured game state from RAM, makes strategic decisions, and sends button inputs — all from the terminal. |

## github

| Skill | What it is for |
| --- | --- |
| `codebase-inspection` | Inspect and analyze codebases using pygount for LOC counting, language breakdown, and code-vs-comment ratios. Use when asked to check lines of code, repo size, language composition, or codebase stats. |
| `github-auth` | Set up GitHub authentication for the agent using git (universally available) or the gh CLI. Covers HTTPS tokens, SSH keys, credential helpers, and gh auth — with a detection flow to pick the right method automatically. |
| `github-code-review` | Review code changes by analyzing git diffs, leaving inline comments on PRs, and performing thorough pre-push review. Works with gh CLI or falls back to git + GitHub REST API via curl. |
| `github-issues` | Create, manage, triage, and close GitHub issues. Search existing issues, add labels, assign people, and link to PRs. Works with gh CLI or falls back to git + GitHub REST API via curl. |
| `github-pr-workflow` | Full pull request lifecycle — create branches, commit changes, open PRs, monitor CI status, auto-fix failures, and merge. Works with gh CLI or falls back to git + GitHub REST API via curl. |
| `github-repo-management` | Clone, create, fork, configure, and manage GitHub repositories. Manage remotes, secrets, releases, and workflows. Works with gh CLI or falls back to git + GitHub REST API via curl. |
| `github-repo-quick-assessment` | Quickly assess whether a GitHub repo is worth using by checking metadata, activity, docs, changelog, and implementation signals. |

## leisure

| Skill | What it is for |
| --- | --- |
| `find-nearby` | Find nearby places (restaurants, cafes, bars, pharmacies, etc.) using OpenStreetMap. Works with coordinates, addresses, cities, zip codes, or Telegram location pins. No API keys needed. |

## mcp

| Skill | What it is for |
| --- | --- |
| `mcporter` | Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation. |
| `native-mcp` | Built-in MCP (Model Context Protocol) client that connects to external MCP servers, discovers their tools, and registers them as native Hermes Agent tools. Supports stdio and HTTP transports with automatic reconnection, security filtering, and zero-config tool injection. |

## media

| Skill | What it is for |
| --- | --- |
| `gif-search` | Search and download GIFs from Tenor using curl. No dependencies beyond curl and jq. Useful for finding reaction GIFs, creating visual content, and sending GIFs in chat. |
| `heartmula` | Set up and run HeartMuLa, the open-source music generation model family (Suno-like). Generates full songs from lyrics + tags with multilingual support. |
| `songsee` | Generate spectrograms and audio feature visualizations (mel, chroma, MFCC, tempogram, etc.) from audio files via CLI. Useful for audio analysis, music production debugging, and visual documentation. |
| `spotify` | Control Spotify — play music, search the catalog, manage playlists and library, inspect devices and playback state. Loads when the user asks to play/pause/queue music, search tracks/albums/artists, manage playlists, or check what's playing. Assumes the Hermes Spotify toolset is enabled and `hermes auth spotify` has been run. |
| `youtube-content` | Fetch YouTube video transcripts and transform them into structured content (chapters, summaries, threads, blog posts). Use when the user shares a YouTube URL or video link, asks to summarize a video, requests a transcript, or wants to extract and reformat content from any YouTube video. |

## mlops

| Skill | What it is for |
| --- | --- |
| `audiocraft-audio-generation` | PyTorch library for audio generation including text-to-music (MusicGen) and text-to-sound (AudioGen). Use when you need to generate music from text descriptions, create sound effects, or perform melody-conditioned music generation. |
| `axolotl` | Expert guidance for fine-tuning LLMs with Axolotl - YAML configs, 100+ models, LoRA/QLoRA, DPO/KTO/ORPO/GRPO, multimodal support |
| `clip` | OpenAI's model connecting vision and language. Enables zero-shot image classification, image-text matching, and cross-modal retrieval. Trained on 400M image-text pairs. Use for image search, content moderation, or vision-language tasks without fine-tuning. Best for general-purpose image understanding. |
| `dspy` | Build complex AI systems with declarative programming, optimize prompts automatically, create modular RAG systems and agents with DSPy - Stanford NLP's framework for systematic LM programming |
| `evaluating-llms-harness` | Evaluates LLMs across 60+ academic benchmarks (MMLU, HumanEval, GSM8K, TruthfulQA, HellaSwag). Use when benchmarking model quality, comparing models, reporting academic results, or tracking training progress. Industry standard used by EleutherAI, HuggingFace, and major labs. Supports HuggingFace, vLLM, APIs. |
| `fine-tuning-with-trl` | Fine-tune LLMs using reinforcement learning with TRL - SFT for instruction tuning, DPO for preference alignment, PPO/GRPO for reward optimization, and reward model training. Use when need RLHF, align model with preferences, or train from human feedback. Works with HuggingFace Transformers. |
| `gguf-quantization` | GGUF format and llama.cpp quantization for efficient CPU/GPU inference. Use when deploying models on consumer hardware, Apple Silicon, or when needing flexible quantization from 2-8 bit without GPU requirements. |
| `grpo-rl-training` | Expert guidance for GRPO/RL fine-tuning with TRL for reasoning and task-specific model training |
| `guidance` | Control LLM output with regex and grammars, guarantee valid JSON/XML/code generation, enforce structured formats, and build multi-step workflows with Guidance - Microsoft Research's constrained generation framework |
| `huggingface-hub` | Hugging Face Hub CLI (hf) — search, download, and upload models and datasets, manage repos, query datasets with SQL, deploy inference endpoints, manage Spaces and buckets. |
| `llama-cpp` | llama.cpp local GGUF inference + HF Hub model discovery. |
| `modal-serverless-gpu` | Serverless GPU cloud platform for running ML workloads. Use when you need on-demand GPU access without infrastructure management, deploying ML models as APIs, or running batch jobs with automatic scaling. |
| `obliteratus` | Remove refusal behaviors from open-weight LLMs using OBLITERATUS — mechanistic interpretability techniques (diff-in-means, SVD, whitened SVD, LEACE, SAE decomposition, etc.) to excise guardrails while preserving reasoning. 9 CLI methods, 28 analysis modules, 116 model presets across 5 compute tiers, tournament evaluation, and telemetry-driven recommendations. Use when a user wants to uncensor, abliterate, or remove refusal from an LLM. |
| `outlines` | Guarantee valid JSON/XML/code structure during generation, use Pydantic models for type-safe outputs, support local models (Transformers, vLLM), and maximize inference speed with Outlines - dottxt.ai's structured generation library |
| `peft-fine-tuning` | Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. Use when fine-tuning large models (7B-70B) with limited GPU memory, when you need to train <1% of parameters with minimal accuracy loss, or for multi-adapter serving. HuggingFace's official library integrated with transformers ecosystem. |
| `pytorch-fsdp` | Expert guidance for Fully Sharded Data Parallel training with PyTorch FSDP - parameter sharding, mixed precision, CPU offloading, FSDP2 |
| `segment-anything-model` | Foundation model for image segmentation with zero-shot transfer. Use when you need to segment any object in images using points, boxes, or masks as prompts, or automatically generate all object masks in an image. |
| `serving-llms-vllm` | Serves LLMs with high throughput using vLLM's PagedAttention and continuous batching. Use when deploying production LLM APIs, optimizing inference latency/throughput, or serving models with limited GPU memory. Supports OpenAI-compatible endpoints, quantization (GPTQ/AWQ/FP8), and tensor parallelism. |
| `stable-diffusion-image-generation` | State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. Use when generating images from text prompts, performing image-to-image translation, inpainting, or building custom diffusion pipelines. |
| `unsloth` | Expert guidance for fast fine-tuning with Unsloth - 2-5x faster training, 50-80% less memory, LoRA/QLoRA optimization |
| `weights-and-biases` | Track ML experiments with automatic logging, visualize training in real-time, optimize hyperparameters with sweeps, and manage model registry with W&B - collaborative MLOps platform |
| `whisper` | OpenAI's general-purpose speech recognition model. Supports 99 languages, transcription, translation to English, and language identification. Six model sizes from tiny (39M params) to large (1550M params). Use for speech-to-text, podcast transcription, or multilingual audio processing. Best for robust, multilingual ASR. |

## note-taking

| Skill | What it is for |
| --- | --- |
| `obsidian` | Read, search, and create notes in the Obsidian vault. |
| `obsidian-personal-docs-human-guides` | Audit and improve Obsidian document sets so they become practical human-facing guides with source links, logs, and verifier checks. |
| `toeic-vocab-study-system` | Build and maintain a TOEIC vocabulary study system from photographed textbook pages, with Obsidian notes, machine-readable JSON, cumulative error tracking, and Ebbinghaus-style review reminders. |

## productivity

| Skill | What it is for |
| --- | --- |
| `google-workspace` | Gmail, Calendar, Drive, Contacts, Sheets, and Docs integration for Hermes. Uses Hermes-managed OAuth2 setup, prefers the Google Workspace CLI (`gws`) when available for broader API coverage, and falls back to the Python client libraries otherwise. |
| `linear` | Manage Linear issues, projects, and teams via the GraphQL API. Create, update, search, and organize issues. Uses API key auth (no OAuth needed). All operations via curl — no dependencies. |
| `maps` | Location intelligence — geocode a place, reverse-geocode coordinates, find nearby places (46 POI categories), driving/walking/cycling distance + time, turn-by-turn directions, timezone lookup, bounding box + area for a named place, and POI search within a rectangle. Uses OpenStreetMap + Overpass + OSRM. Free, no API key. |
| `nano-pdf` | Edit PDFs with natural-language instructions using the nano-pdf CLI. Modify text, fix typos, update titles, and make content changes to specific pages without manual editing. |
| `notion` | Notion API for creating and managing pages, databases, and blocks via curl. Search, create, update, and query Notion workspaces directly from the terminal. |
| `ocr-and-documents` | Extract text from PDFs and scanned documents. Use web_extract for remote URLs, pymupdf for local text-based PDFs, marker-pdf for OCR/scanned docs. For DOCX use python-docx, for PPTX see the powerpoint skill. |
| `old-man-voca-threads-publishing` | Publish one old_man_voca English vocabulary thread via the local Threads helper script, with spoiler core-image validation and no repeated words. |
| `powerpoint` | Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill. |
| `threads-api-troubleshooting` | Troubleshoot Meta Threads API/OAuth setup and 429 Too Many Requests problems, especially when Threads web/OAuth fails on one PC while API endpoints or other devices still work. |

## red-teaming

| Skill | What it is for |
| --- | --- |
| `godmode` | Jailbreak API-served LLMs using G0DM0D3 techniques — Parseltongue input obfuscation (33 techniques), GODMODE CLASSIC system prompt templates, ULTRAPLINIAN multi-model racing, encoding escalation, and Hermes-native prefill/system prompt integration. Use when a user wants to bypass safety filters, jailbreak a model, or red-team model robustness. |

## research

| Skill | What it is for |
| --- | --- |
| `arxiv` | Search and retrieve academic papers from arXiv using their free REST API. No API key needed. Search by keyword, author, category, or ID. Combine with web_extract or the ocr-and-documents skill to read full paper content. |
| `blogwatcher` | Monitor blogs and RSS/Atom feeds for updates using the blogwatcher-cli tool. Add blogs, scan for new articles, track read status, and filter by category. |
| `insane-search-adaptive-web-access` | Adaptive web-access workflow for Hermes when a site is blocked, JS-rendered, rate-limited, or better served by public APIs. Inspired by fivetaku/insane-search, but adapted to Hermes tools. |
| `llm-wiki` | Karpathy's LLM Wiki — build and maintain a persistent, interlinked markdown knowledge base. Ingest sources, query compiled knowledge, and lint for consistency. |
| `polymarket` | Query Polymarket prediction market data — search markets, get prices, orderbooks, and price history. Read-only via public REST APIs, no API key needed. |

## smart-home

| Skill | What it is for |
| --- | --- |
| `openhue` | Control Philips Hue lights, rooms, and scenes via the OpenHue CLI. Turn lights on/off, adjust brightness, color, color temperature, and activate scenes. |

## software-development

| Skill | What it is for |
| --- | --- |
| `plan` | Plan mode for Hermes — inspect context, write a markdown plan into the active workspace's `.hermes/plans/` directory, and do not execute the work. |
| `requesting-code-review` | Pre-commit verification pipeline — static security scan, baseline-aware quality gates, independent reviewer subagent, and auto-fix loop. Use after code changes and before committing, pushing, or opening a PR. |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks. Dispatches fresh delegate_task per task with two-stage review (spec compliance then code quality). |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior. 4-phase root cause investigation — NO fixes without understanding the problem first. |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code. Enforces RED-GREEN-REFACTOR cycle with test-first approach. |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task. Creates comprehensive implementation plans with bite-sized tasks, exact file paths, and complete code examples. |

## How to read this catalog

- Skills define workflow standards, pitfalls, and verification steps.
- The same tools can behave very differently depending on the skill loaded for the task.
- This is a snapshot. Installed skills can change as the agent is updated.
