# 🔬 BrawlSCRE

<div align="center">

**Brawl Stars Reverse Engineering lab**

*.sc files • CSV configs • protocol notes • tools*

![bs](https://img.shields.io/badge/Brawl_Stars-RE-yellow?style=for-the-badge)
![scre](https://img.shields.io/badge/SCRE-lab-blue?style=for-the-badge)
![python](https://img.shields.io/badge/Python-tools-green?style=for-the-badge)

</div>

---

## 🗺️ Карта репозитория

| Файл | Что это |
|------|---------|
| `sc_parser.py` | Парсер заголовка .sc файлов (Supercell format) |
| `csv_dump.py` | Дамп и разбор CSV конфигов из APK |
| `protocol_notes.md` | Заметки по протоколу (packets, crypto) |
| `tools.md` | Чем ковырять: полный список инструментов |

## 📦 .sc формат (кратко)

```
offset  size  field
0x00    2     magic ("SC" = 0x53 0x43)
0x02    4     file size (big-endian)
0x06    4     header size
0x0A    ...   sections: shapes, textures, animations
```

Файлы сжаты **LZMA**. Декомпрессия:

```python
import lzma
with open("player.sc", "rb") as f:
    data = f.read()
assert data[:2] == b"SC"
body = lzma.decompress(data[6:])  # skip magic + sizes
```

Полный парсер — в [sc_parser.py](sc_parser.py).

## 📄 CSV конфиги

Лежат в APK: `assets/csv_logic/` — персонажи, скины, карты, баланс.
Скрипт [csv_dump.py](csv_dump.py) вытаскивает и складывает в читаемый вид.

## 🔌 Протокол

Клиент ↔ сервер: TCP + NaCl crypto (см. [protocol_notes.md](protocol_notes.md)).
Для сниффинга: mitmproxy + патч cert-pinning (frida).

## 🧰 Инструменты

См. [tools.md](tools.md) — от APKTool до Ghidra.

## ⚠️ Дисклеймер

Только в образовательных целях и для моддинга своей игры.
Не используйте для читов на официальных серверах — бан прилетит быстрее,
чем вы скажете «Supercell».

---

<div align="center">

*Reverse it till it makes sense.* 🔬

</div>
