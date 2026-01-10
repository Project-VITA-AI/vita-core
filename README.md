<h1 align="center">Project VITA</h1>

<img src="docs/assets/banner.png" alt="Project J.A.I.son" width="1920">

<h4 align="center">Core server for building AI Companion applications.</h4>

<p align="center">
  <img alt="Project JAIson badge" src="https://img.shields.io/badge/Project-VITA-blue">
  <img alt="Github Release" src="https://img.shields.io/github/v/release/Project-VITA-AI/vita-core" />
  <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/Project-VITA-AI/vita-core" />
  <img alt="Issues" src="https://img.shields.io/github/issues/Project-VITA-AI/vita-core" />
  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/Project-VITA-AI/vita-core" />
</p>

<p align="center" >
  <a href="#about-this-project">About This Project</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#applications">Applications</a> •
  <a href="#install-from-scratch">Install From Scratch</a> •
  <a href="#operations">Operations</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#developer-guide">Developer Guide</a> •
  <a href="#Community">Community</a> •
  <a href="#thank-you-to-all-the-contributors">Credits</a> •
  <a href="#license">License</a>
</p>

## About This Project

This project is for a fully customizable AI persona usable for streaming or private companionship. Feel free to download and use how you wish. 

This software uses libraries from the FFmpeg project under the LGPLv2.1

## Key Features

- Realtime promptable AI personality with text and speech input
- Support for MCP
- REST API and websocket server for building applications on top of this server
- Options to run fully local

## Official Applications

- [Discord bot integration](https://github.com/limitcantcode/app-jaison-discord-lcc)
- [VTube Studio with emotions](https://github.com/limitcantcode/app-jaison-vts-hotkeys-lcc)
- [Twitch Chat and Events content provider](https://github.com/limitcantcode/app-jaison-twitch-lcc)

Feel free to build and share your own! See the [Developer Guide](#developer-guide) for more info.

## Install From Scratch

### Setup and install dependencies

Create and enter a virtual environment with Python 3.10. I suggest using [uv](https://docs.astral.sh/uv/getting-started/installation/) and this documentation will use uv

For example, using uv:
```bash
uv pip venv --python="3.10"

# Use this environment
.venv/Scripts/activate # Windows
source .venv/bin/activate # Linux
```

<hr />

Install dependencies according to your system.

**NOTE**: Only tested for windows on NVidia hardware. Use on Linux is possible but requires removal of windows specific dependencies. Use with AMD GPU may be possible with ROCm version of pytorch. Install v2.5.1 from [here](https://pytorch.org/get-started/locally/) after installing CPU version. There's no guaruntee this will work as some systems are NVidia specific.

```bash
# Inside project root where this README is located
uv pip install --no-deps -r requirements.win_cpu.lock # Example for CPU on windows
python install.py
```

> If on Windows, please enable [Developer Mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development)

> For NVidia cards, ensure you have the latest drivers and [CUDA toolkit](https://developer.nvidia.com/cuda-toolkit)

> Dealing with duplicate `libiomp5md.dll`.
> 
> It might not be necessary, but in case you encounter this error when running:
> 
> 1. Go to `torch` package in environment directory (`.venv/Lib/sit-packages/torch` for `uv`)
> 2. Search and delete `libiomp5md.dll`

<hr />

Install FFmpeg
#### For Ubuntu/Debian users
```bash
sudo apt install ffmpeg
```
#### For MacOS users
```bash
brew install ffmpeg
```
#### For Windows users
Download executables and place them in the root folder:
- [Download latest `ffmpeg-git-essentials.7z`](https://www.gyan.dev/ffmpeg/builds/)
- Extract and copy all contents from `bin/` to root of this project.

<hr />

Configuration

**FOR A FREE, 3RD PARTY T2T INTEGRATION**: Use `openai` type but configure for use with [Groq](https://console.groq.com/home).

Add keys and other sensitive information for services you intend to use in `.env` (make a new file and copy the contents of [`.env-template`](.env-template)).

For immediate setup using the example configuration, just provide the OpenAI API key.

Overall configuration can be done in `configs/` and an example with all configurable options is located in `configs/example.yaml`. See [Development guide](DEVELOPER.md) for details on configuration.


## How To Use

While using the virtual environment with the installation.

```bash
python ./src/main.py --help
```

Example usage: `python ./src/main.py --config=example`

## Developer Guide

See the specification for building applciations for Project VITA, creating custom integrations, and configuration tips below:

- [REST API spec](api.yaml)
- [Development guide](DEVELOPER.md)
- [Contributing guidelines](CONTRIBUTING.md)

## Community

Join the community!

- [Discord](https://discord.gg/Z8yyEzHsYM)
- [Youtube](https://www.youtube.com/@LimitCantCode)
- [Twitch](https://www.twitch.tv/atmylimit_)

## Thank you to all the contributors!

[Become a contributor as well](CONTRIBUTING.md)

<a href="https://github.com/Project-VITA-AI/vita-core/graphs/contributors" target="_blank">
  <img src="https://contrib.rocks/image?repo=Project-VITA-AI/vita-core" />
</a>

## License

[MIT](LICENSE)
