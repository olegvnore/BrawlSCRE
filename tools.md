# 🧰 RE toolbox (Brawl Stars / SCRE)

## APK teardown

| Tool | Use |
|------|-----|
| [APKTool](https://ibotpeaches.github.io/Apktool/) | Decode APK → smali + resources + csv |
| [JADX](https://github.com/skylot/jadx) | DEX → readable Java, fast |
| [Ghidra](https://ghidra-sre.org/) | Native lib (libg.so) reversing |
| [IDA Free](https://hex-rays.com/ida-free/) | Alternative for native |

## Runtime

| Tool | Use |
|------|-----|
| [Frida](https://frida.re/) | Hook crypto, dump keys, bypass pinning |
| [Objection](https://github.com/sensepost/objection) | Frida without writing scripts |
| [mitmproxy](https://mitmproxy.org/) | Traffic sniffing after pinning bypass |
| [Wireshark](https://www.wireshark.org/) + tcpdump | Raw packet capture |

## .sc / assets

| Tool | Use |
|------|-----|
| [sc-compressor](https://github.com/Vorono4ka/scc) | Decompress .sc files |
| [BrawlBox](https://github.com/Daniil-256) / Metzliits tools | View/export .sc textures |
| This repo's `sc_parser.py` | Quick header inspection |

## CSV / gamedata

- `csv_dump.py` (this repo) — pretty-print csv_logic
- Any spreadsheet app for diffing versions

## Workflow (TL;DR)

1. Pull APK (same version as your notes!)
2. APKTool decode → grab `csv_logic/` + `.sc`
3. JADX on classes.dex → find crypto + packet handlers
4. Frida on device → dump session keys at runtime
5. mitmproxy → capture → decrypt offline with dumped keys
6. Document packet IDs in `protocol_notes.md`

## ⚠️

Emulator + private server for experiments. Official servers = instant ban.
