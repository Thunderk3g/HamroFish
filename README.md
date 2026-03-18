<div align="center">

<img src="./static/image/ShibaSwarm_logo_compressed.jpeg" alt="ShibaSwarm Logo" width="75%"/>

<a href="https://trendshift.io/repositories/16144" target="_blank"><img src="https://trendshift.io/api/badge/repositories/16144" alt="666ghj%2FShibaSwarm | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

A simple and universal swarm intelligence engine, predicting anything
</br>
<em>A simple and universal swarm intelligence engine, predicting anything</em>

<a href="https://www.shanda.com/" target="_blank"><img src="./static/image/shanda_logo.png" alt="ShibaSwarm | Shanda" height="40"/></a>

[![GitHub Stars](https://img.shields.io/github/stars/666ghj/ShibaSwarm?style=flat-square&color=DAA520)](https://github.com/666ghj/ShibaSwarm/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/666ghj/ShibaSwarm?style=flat-square)](https://github.com/666ghj/ShibaSwarm/watchers)
[![GitHub Forks](https://img.shields.io/github/forks/666ghj/ShibaSwarm?style=flat-square)](https://github.com/666ghj/ShibaSwarm/network)
[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/666ghj/ShibaSwarm)

[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.com/channels/1469200078932545606/1469201282077163739)
[![X](https://img.shields.io/badge/X-Follow-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/ShibaSwarm_ai)
[![Instagram](https://img.shields.io/badge/Instagram-Follow-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/ShibaSwarm_ai/)

</div>

## Overview

**ShibaSwarm** is a next-generation AI prediction engine powered by multi-agent technology. By extracting seed information from the real world (such as breaking news, policy drafts, or financial signals), it automatically constructs a high-fidelity parallel digital world. Within this space, thousands of intelligent agents with independent personalities, long-term memory, and behavioral logic freely interact and undergo social evolution. You can inject variables dynamically from a "God's-eye view" to precisely deduce future trajectories — rehearse the future in a digital sandbox, and win decisions after countless simulations.

> You only need to: upload seed materials (data analysis reports or interesting novel stories) and describe your prediction requirements in natural language</br>
> ShibaSwarm will return: a detailed prediction report and a deeply interactive high-fidelity digital world

### Our Vision

ShibaSwarm is dedicated to creating a swarm intelligence mirror that maps reality. By capturing the collective emergence triggered by individual interactions, we break through the limitations of traditional prediction:

- **At the macro level**: we are a rehearsal laboratory for decision-makers, allowing policies and public relations to be tested at zero risk
- **At the micro level**: we are a creative sandbox for individual users — whether deducing novel endings or exploring imaginative scenarios, everything can be fun, playful, and accessible

From serious predictions to playful simulations, we let every "what if" see its outcome, making it possible to predict anything.

## Live Demo

Welcome to visit our online demo environment and experience a prediction simulation on trending public opinion events we've prepared for you: [ShibaSwarm-live-demo](https://666ghj.github.io/ShibaSwarm-demo/)

## Screenshots

<div align="center">
<table>
<tr>
<td><img src="./static/image/Screenshot/screenshot-1.png" alt="Screenshot 1" width="100%"/></td>
<td><img src="./static/image/Screenshot/screenshot-2.png" alt="Screenshot 2" width="100%"/></td>
</tr>
<tr>
<td><img src="./static/image/Screenshot/screenshot-3.png" alt="Screenshot 3" width="100%"/></td>
<td><img src="./static/image/Screenshot/screenshot-4.png" alt="Screenshot 4" width="100%"/></td>
</tr>
<tr>
<td><img src="./static/image/Screenshot/screenshot-5.png" alt="Screenshot 5" width="100%"/></td>
<td><img src="./static/image/Screenshot/screenshot-6.png" alt="Screenshot 6" width="100%"/></td>
</tr>
</table>
</div>

## Demo Videos

### 1. Wuhan University Public Opinion Simulation + ShibaSwarm Project Introduction

<div align="center">
<a href="https://www.bilibili.com/video/BV1VYBsBHEMY/" target="_blank"><img src="./static/image/wuhan-university-demo-cover.png" alt="ShibaSwarm Demo Video" width="75%"/></a>

Click the image to watch the complete demo video for prediction using a BettaFish-generated "Wuhan University Public Opinion Report"
</div>

### 2. Dream of the Red Chamber Lost Ending Simulation

<div align="center">
<a href="https://www.bilibili.com/video/BV1cPk3BBExq" target="_blank"><img src="./static/image/dream-of-red-chamber-demo-cover.jpg" alt="ShibaSwarm Demo Video" width="75%"/></a>

Click the image to watch ShibaSwarm's deep prediction of the lost ending based on hundreds of thousands of words from the first 80 chapters of "Dream of the Red Chamber"
</div>

> **Financial prediction**, **political news prediction** and more examples coming soon...

## Workflow

1. **Graph Building**: seed extraction, individual/collective memory injection, GraphRAG construction
2. **Environment Setup**: entity relationship extraction, persona generation, agent configuration injection
3. **Simulation**: dual-platform parallel simulation, auto-parse prediction requirements, dynamic temporal memory updates
4. **Report Generation**: ReportAgent with a rich toolset for deep interaction with the post-simulation environment
5. **Deep Interaction**: chat with any agent in the simulated world and interact with ReportAgent

## Quick Start

### Option 1: Source Code Deployment (Recommended)

#### Prerequisites

| Tool | Version | Description | Check Installation |
|------|---------|-------------|-------------------|
| **Node.js** | 18+ | Frontend runtime, includes npm | `node -v` |
| **Python** | >=3.11, <=3.12 | Backend runtime | `python --version` |
| **uv** | Latest | Python package manager | `uv --version` |

#### 1. Configure Environment Variables

```bash
# Copy the example configuration file
cp .env.example .env

# Edit the .env file and fill in the required API keys
```

**Required Environment Variables:**

```env
# LLM API configuration (supports any LLM API with OpenAI SDK format)
# Recommended: Alibaba Qwen-plus model via Bailian Platform: https://bailian.console.aliyun.com/
# High consumption, try simulations with fewer than 40 rounds first
LLM_API_KEY=your_api_key
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

# Zep Cloud configuration
# Free monthly quota is sufficient for simple usage: https://app.getzep.com/
ZEP_API_KEY=your_zep_api_key
```

#### 2. Install Dependencies

```bash
# One-click installation of all dependencies (root + frontend + backend)
npm run setup:all
```

Or install step by step:

```bash
# Install Node dependencies (root + frontend)
npm run setup

# Install Python dependencies (backend, auto-creates virtual environment)
npm run setup:backend
```

#### 3. Start Services

```bash
# Start both frontend and backend (run from project root)
npm run dev
```

**Service URLs:**
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5001`

**Start Individually:**

```bash
npm run backend   # Start backend only
npm run frontend  # Start frontend only
```

### Option 2: Docker Deployment

```bash
# 1. Configure environment variables (same as source deployment)
cp .env.example .env

# 2. Pull image and start
docker compose up -d
```

Reads `.env` from the root directory by default, maps ports `3000 (frontend) / 5001 (backend)`.

> A mirror address for faster pulling is provided as comments in `docker-compose.yml`. Replace if needed.

## Join the Conversation

<div align="center">
<img src="./static/image/qq-group.png" alt="QQ Group" width="60%"/>
</div>

&nbsp;

The ShibaSwarm team is recruiting full-time/internship positions. If you're interested in multi-agent simulation and LLM applications, feel free to send your resume to: **ShibaSwarm@shanda.com**

## Acknowledgments

**ShibaSwarm has received strategic support and incubation from Shanda Group.**

ShibaSwarm's simulation engine is powered by **[OASIS (Open Agent Social Interaction Simulations)](https://github.com/camel-ai/oasis)**. We sincerely thank the CAMEL-AI team for their open-source contributions.

## Project Statistics

<a href="https://www.star-history.com/#666ghj/ShibaSwarm&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=666ghj/ShibaSwarm&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=666ghj/ShibaSwarm&type=date&theme=light&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=666ghj/ShibaSwarm&type=date" />
 </picture>
</a>
