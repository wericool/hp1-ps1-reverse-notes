# Engine notes (EURO1.GAM, PAL)

All addresses are RAM addresses without the 0x80000000 bit. Collected while porting; verified against the original code.

## Main loop (0x10000)
- Boot, then per scene: 0x26084 (front-end check) -> level load (0x1082C, 0x19418, 0x467DC), sound managers 0x4C54C,
  mode init table, 0x13128, **0x52F70 -> 0x52F44** (reset both text windows), 0x231CC, 0x4DAB4 (particles), 0x13C1C.
- Frame loop 0x101B8: 0x10710, mode update table, mode "done" table; 0x2344C (draw), 0x53F58 (end of frame).
- Scene end 0x10230: when 0x26084 returns 0 (gameplay; it returns 1 only for front-end modes 2/5/6/13):
  0x5B2B0(0), 0x5B518(0), **0x4C63C** (sound shutdown: 0x4A704 closes the speech/XA stream, clears the 3-manager table
  0x78878), 0x5B3E8(3), then the next scene load. So a playing dialogue voice is always cut at a scene change.

## Actors
- Two pools: normal and special. Root actor pointer 0x78A1C (published by 0x3BF60, cleared at level init 0x36D20).
- Special list head 0x78A3C. A normal actor spawned by a special parent (0xD9 spawn, placement 0x34C44) is linked into
  the SPECIAL list after its parent, so the special pass (0x35E48 / 0x35E68) updates it.
- Normal pass 0x35D4C; special-list walkers: render 0x21DDC, audio 0x36A24 -> 0x3684C, broadcast 0x41BB4 / 0x41D8C.
- Some opcodes read the root without a null check (0x1C at 0x3C8F0, 0x6A at 0x3A3AC, 0x6B): with no root they read low RAM
  0x30..0x5F, which is always zero on real hardware.
- Health = actor field 111 = word 0x82980 (save +0x560), max 0x8000.

## Script VM (ASL / "strat")
- One 32-bit word per instruction: low 16 bits opcode, high 16 bits signed immediate; see `data/asl-opcodes.tsv`.
- Field read table 0x76750 (selector -> handler). Globals base 0x7C8C8.
- Script header = trigger descriptors (type, raw, continuation). Op 0x0C register_trigger makes one live:
  continuation = (register word + 2) + descriptor word 2 (in words). Type 4 = damage/contact, type 8 = event with a code
  in `raw` (e.g. 0x579000 Flipendo hit on the Fire Seed plant, 0x456000 pick-up).
- Progress bits: ops 0x174 read / 0x176 write / 0x1B9-0x1BA per-actor "auto" bit; bit id = value / 4096.

## Text windows
- Two window structs (dialogue 0x7C0E8, narration 0x7BA98): +0 active, +5A8 close flag, +5B0 speech group, +5B4 voice id,
  +5B8 countdown. 0x5279C stops the voice (0x4CF14 -> manager 0x4C044); 0x526EC queries it (0x4CF48 -> 0x4C14C).

## Pad / display (hook points for PC features)
- Pad: 0x12D9C (PadInitDirect), 0x131CC (PadGetState, actuators). Display env: 0x11230 / 0x104F8. See `data/sdk-hook-points.txt`.
