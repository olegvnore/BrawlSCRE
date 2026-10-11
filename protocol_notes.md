# 🔌 Protocol notes (Brawl Stars / SCRE)

> Living document. Tested against recent client versions.
> Packet IDs shift between updates — always verify.

## Transport

- TCP, usually port 9339
- Client hello → server hello → session key exchange
- After handshake all traffic is encrypted (NaCl box / custom stream cipher depending on version)

## Packet framing

```
+--------+--------+--------+-------------+
|  ID    | LEN (3B big-endian) | PAYLOAD   |
| 2B BE  | 3B              | LEN bytes |
+--------+--------+--------+-------------+
```

- ID `10100` — ClientHello (version, device info)
- ID `10101` — Login (account id + token)
- ID `20100+` — server responses
- Keepalive: ID `10108` every ~30s

## Crypto notes

- Old versions: RC4-like stream + nonce per packet
- Newer: libsodium sealed boxes, session keys derived from ECDH
- Keys live in memory — dump with frida after login packet

## Sniffing setup

1. Rooted device or emulator (NO cert validation bypass = NO traffic)
2. Patch cert pinning with frida script (see SCRE community scripts)
3. mitmproxy in transparent mode, or raw TCP dump via `tcpdump`
4. Parse with framing above, decrypt with dumped session key

## Useful message IDs (verify per version!)

| ID | Direction | Meaning |
|----|-----------|---------|
| 10100 | C→S | ClientHello |
| 10101 | C→S | Login |
| 10108 | C→S | KeepAlive |
| 14101 | C→S | GoHome / EndClientTurn |
| 20100 | S→C | ServerHello |
| 20104 | S→C | LoginOk |
| 20105 | S→C | LoginFailed |
| 23457 | S→C | ExtendedLoginOk (own home data) |

## ⚠️ Rules

- OFFICIAL servers = read-only recon. Don't send crafted packets there.
- Want to experiment? Run a private server (see Brawl server emulators on GitHub).
- Bans are permanent and HWID-based. You've been warned.
