# Motivation
Sometimes you want to watch other videos during an online meeting without totally muting the meeting or losing response time.

# Requirements
- OS: Linux
- DE: XORG
- AD: PulseAudio
- pip: `pulsectl==21.10.5`

# Installation
*Assuming `~/.local/bin` is in PATH.*
```bash
pip3 install pulsectl==21.10.5
URL_=https://raw.githubusercontent.com/m2-farzan/presence/main/presence.py
wget -O ~/.local/bin/presence ${URL_}
```

# CLI Args
```bash
usage: presence.py [-h]
                   [PERIOD ...] [ACTIVE_VOLUME ...]
                   [INACTIVE_VOLUME ...]

Automatically reduce volume of background applications

positional arguments:
  PERIOD           Period in seconds
  ACTIVE_VOLUME    The volume to set when the active window is
                   focused [default: 1.0]
  INACTIVE_VOLUME  The volume to set when the active window is not
                   focused [default: 0.5]

optional arguments:
  -h, --help       show this help message and exit
```

# Detached Usage
Start:
```bash
nohup ./presence.py
```
Stop:
```bash
¯\_(ツ)_/¯
```

# Contribution
Would be great if somebody could turn this into a gnome extension.