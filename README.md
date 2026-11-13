# Harry Potter and the Philosopher's Stone (PS1) — reverse-engineering notes

Notes collected while writing a native Windows port of the PS1 game (PAL, `EURO1.GAM`).
They are meant to help other people who study the game or the Argonaut PS1 engine.

**No game data is included.** No executable, no disassembly listing, no WAD/DAT files, no assets, no saves.
You need your own copy of the game. Everything here is our own description: addresses, names we gave, and notes.

## What is inside

| Path | Contents |
|---|---|
| `data/game-functions.tsv` | 561 game functions (0x10000..0x5B2AF) called in `EURO1.GAM`; `ported` / `todo` status and short notes |
| `data/asl-opcodes.tsv` | ASL (strat script) opcodes: number, extra words, handler address in `EURO1.GAM`, our name |
| `data/psyq-sdk-functions.txt` | Sony PSY-Q SDK functions identified by signature (the SDK starts at 0x5B2B0) |
| `data/sdk-hook-points.txt` | which game function calls which SDK function (pad, GPU, GTE, SPU, CD) |
| `docs/asl-opcodes.md` | every opcode: name, handler, extra words, behaviour notes (228 of 359 with notes) |
| `docs/functions.md` | every game function: status and behaviour notes (301 of 561 with notes) |
| `docs/engine.md` | engine overview: memory layout, actor lists, frame loop, script VM, scene change |
| `docs/progress.md` | coverage numbers |
| `tools/psyq_match.py`, `tools/psyq_union.py` | match PSY-Q OBJ signatures against a PS1 executable |

## Address mapping

`EURO1.GAM` is a PS-X EXE: header 0x800 bytes, loaded at 0x80010000, so file offset = 0x800 + (addr - 0x10000).
Addresses here are written without the 0x80000000 KSEG0 bit (0x10000 = 0x80010000). `SLES_036.62` is only a small loader.

## Credits / related work

- PSY-Q signatures: [lab313ru/psx_psyq_signatures](https://github.com/lab313ru/psx_psyq_signatures)
- File formats: [OverSurge/PS1-Argonaut-Reverse](https://github.com/OverSurge/PS1-Argonaut-Reverse),
  [mateusfavarin/HP1-PS1-Tools](https://github.com/mateusfavarin/HP1-PS1-Tools), [joshbarrass/hptools](https://github.com/joshbarrass/hptools)
- Early decompilation: [Argonaut-PS1-Reverse/hp1](https://github.com/Argonaut-PS1-Reverse/hp1)

Harry Potter is a trademark of Warner Bros. Entertainment Inc. This project is not affiliated with Warner Bros.,
Electronic Arts, Argonaut Games or Sony. Notes are provided for research and interoperability.
