## 1. Original code (EURO1.GAM) named in the native port

"Named" = the function address appears in the port sources (ported, or replaced by a native backend). Not every named
function is complete. The game's own code is 0x10000..0x5B2AF; from 0x5B2B0 (LIBSN __main) on, the EXE is the Sony PSY-Q 4.x
SDK (identified with lab313ru/psx_psyq_signatures, list psyq-sdk-functions.txt). The SDK is REPLACED by Windows backends
(D3D11, XAudio2, files, XInput), not decoded. progress-todo.txt = game functions not yet named (the real remainder; some of
them are PS1-only: memory card UI, CD streaming, debug).

| Address range | Contents | Named in the port | Total called | % |
|---|---|---|---|---|
| 0x10000-0x20000 | main loop, modes, pad | 83 | 118 | 70% |
| 0x20000-0x30000 | front end, menus, camera, fades | 45 | 73 | 61% |
| 0x30000-0x40000 | actors, ASL VM core | 59 | 64 | 92% |
| 0x40000-0x50000 | ASL ops, sound managers, text | 143 | 177 | 80% |
| 0x50000-0x5b2b0 | text windows, render, misc | 54 | 125 | 43% |
| **game code total** | | **387** | **561** | **68%** |
| 0x5b2b0+ | Sony PSY-Q SDK (identified by signature: 174) | replaced natively | 259 | n/a |

Game functions not yet named in the port: 174 (list: progress-todo.txt)

ASL opcodes: SUMMARY levels=59 scripts=1253 words=620575 data_stops=1486 distinct_used=338 missing=0
Gate oracle: TOTAL refused pairs 14 of 5439 distinct (op,imm)
Level smoke (level-smoke31.txt): 46 / 54 story WADs run 300 frames from a save

