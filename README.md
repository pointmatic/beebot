# BeeZeeBot 
AI Desktop Configurator
- v.0.1.0

This application helps users install and configure utilities, applications, and dependencies that are commonly used for AI, data science, and software development. 


# HOW TO USE

Currently, only CLI commands are implemented as stubs and only MacOS is supported. 

Using the terminal...
1. Checkout the repo 
2. Run this command to compile: `pyinstaller --onefile beezeebot_cli.py`
3. Run this command to see the help file: beezeebot_cli


# BACKGROUND

Personally, there have been so many times that I have gone through an initial software development setup process on my Mac, Windows PC, or Linux computer, and each time there are a series of little gotchas, undocumented workarounds, and idiosyncracies or incompatibilities that make it annoying. After wasting an hour here and a few hours there with interruptions to do other things, I always get to the same question: "Why someone hasn't solved this problem?" 

Of course, after everything is working, I go on my merry way, gradually forgetting all the little details that I learned to make it work. Unfortunately changes over time in operating system, security, and software also confound or complexify the process when I need to do it all over again in a few months. Finally, after a couple decades of dealing with this problem, and seeing there is a similar problem across MacOS, Windows, and Linux, I've finally decided to do something about it. In March 2025, BeeZeeBot was born. 

Most recently, I've noticed that people get excited about AI and want to try out using AI models locally and also try other open source software, only to be slowed down and discouraged by the installation and configuration process. While an AI or a YouTube video might be able to walk through the installation of each tool, inevitably, there is some combination of tools, or some hidden detail that breaks down, turning it into a technical troubleshooting problem for a software engineer or IT technician. 


# SUPPORTED PLATFORMS

- MacOS (v. 15+)
- Windows (TBD)
- Linux (TBD)

While I anticipate expanding support for Windows and Linux, my first priority is for MacOS. Once I have end-to-end completion, I'll turn attention to the other platforms. 


# SUPPORTED UTILITIES & APPLICATIONS

## Utilities
- OS detection (prototype)
- Xcode command-line tools (prototype)
- MacOS Sofware updates (prototype)
- Homebrew (WIP)
- ~~asdf~~ TBD
    - ~~Python~~ TBD
    - ~~Ruby~~ TBD
- ~~direnv~~ TBD
## Applications
- ~~VS Code~~ TBD
  - ~~VS Code Extensions~~ TBD
- ~~Ollama~~ TBD
  - ~~AI models (various)~~ TBD
- ~~Open WebUI Chat~~ TBD
- ~~LangChain~~ TBD
- ~~Pydantic AI~~ TBD
- ~~CrewAI~~ TBD