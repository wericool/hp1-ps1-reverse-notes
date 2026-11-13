# Game functions (EURO1.GAM 0x10000..0x5B2AF)

Status: `ported` = present in the native port, `todo` = not yet. Notes from the port comments and log.

## 0x10000 (ported)

- The SDK starts at 0x5B2B0 (LIBSN __main): game code = 0x10000..0x5B2AF.
- pos +0/+4/+8) loops [0x7C794] visible cells from list [0x7D30C] (+0x12 cell index * 24 into map [t4+0x3C] rows: x +8, z +0x10, |dx|,|dz| < 10000 and dx^2 + dz^2 < limit), then face records via map +0x4C / +0x54 (face byte 7 & 0x3F type 1/2, variant by [0x77A08] and +0x48 stride from [0x78AE8] records * 0x68), and rewrites vertex colour bytes in place (45 SB) logging each original word into the und
- the 1E368 cell culling ((r + 0xD00)^2 xz, |d| < 10000, visible cells only) is not reproduced (vertices outside r get nothing either way).
- ITEM 160 (build-190) NATIVE POLICY (audio backend only): scene spatial rows without 0x10000 (positional emitters, 4D490..4D64C: group-nearest pick, SPU voice query/alloc/start/release 4C14C/4CE6C/4BEEC, handle +36) are skipped = silent;
- hit window |angle_diff(L33<<7, L40<<7 or (L40+0x10000)<<7)| < L0<<7, a miss decrements L32.

## 0x10268 (ported)

- 26E54 frame: GP+1E5C countdown, L1/R1 dropped (10268 cheats not ported), 339F8, the 19F04 items 144 "Start Game" / 135 "Options" (78AF4 cursor) once the wait ends, 12660, 169A4 logo, 1A044 {68 copyright, 0xEC}, and the background world's frame LAST (27028).
- from 78E38 and feeds 10268 (cheat sequences: not ported);
- L1 / R1 belong to 10268's cheat sequences (not ported)
- input of 10268, not ported (native-front-end-title.h: 77620 debug word is 0 natively), so the word stays 0.

## 0x103F0 (todo)


## 0x104F8 (todo)

- sdk-hook-points.txt = which game function calls which SDK function (pad = 131CC/12D9C, display env = 11230/104F8, GTE, SPU, CD) = hook points for PC features (controls, resolution).

## 0x10604 (todo)


## 0x106CC (todo)


## 0x10710 (todo)


## 0x10750 (ported)

- 10750, actual word6FD04

## 0x10780 (ported)


## 0x10794 (ported)

- Exact scalar leaves10780/10794/107A0 and global wrappers107D4/10804/1082C/10854.

## 0x107A0 (ported)

- Exact scalar leaves10780/10794/107A0 and global wrappers107D4/10804/1082C/10854.

## 0x107D4 (ported)

- Item 191: visibility setup 0x1B5A0, scene flags [0x7915C] & 0x800 (not special): 107D4(4096) -> [0x7B5F0], 107D4(0x8000) -> [0x7D408] reciprocal table (word 0 = 0, word i = 0x1000000 / i, i < 8192), then a nonzero mode 107D4(8192) -> [0x7D30C].
- Levels without TROP descriptors never allocate [0x7B5FC] (0x19244 skips 107D4);
- r607 item 191: 0x1B5A0 (the setup): 107D4(4096) -> [0x7B5F0];
- scene flags [0x7915C] & 0x800: 107D4(0x8000) -> [0x7D408], word 0 = 0, word i = 0x1000000 / i (i 1..8191, divu).
- nonzero mode: 107D4(8192) -> [0x7D30C];

## 0x10804 (ported)

- Exact scalar leaves10780/10794/107A0 and global wrappers107D4/10804/1082C/10854.

## 0x1082C (ported)

- 0x78ADC = 5 (reload) is read only by 24790 and mode-3 enter 26588 (-> 1082C + 42B30);
- After ALL requested banks really returned, actual180A0->1082C(savedS5).
- Exact scalar leaves10780/10794/107A0 and global wrappers107D4/10804/1082C/10854.
- GPU/label/1082C.

## 0x10854 (ported)

- Exact scalar leaves10780/10794/107A0 and global wrappers107D4/10804/1082C/10854.

## 0x109A4 (todo)


## 0x10AF8 (ported)


## 0x10CAC (ported)


## 0x10CDC (ported)

- Does not execute107D4/10CDC, resource/header mutations, upload or1082C.

## 0x10F04 (ported)


## 0x10F18 (todo)


## 0x1108C (todo)


## 0x11094 (todo)


## 0x11178 (ported)

- Actual183D8..184C4 including111CC/11178 color copies and actor model pointer
- 111CC sets two flag bytes;11178 writes actual argument pointer and
- Exact nonnull111CC/11178 color copy for the same private selected record,

## 0x111CC (ported)

- 7B78 := 0, 111CC(77808), 11C44 loads
- 111CC sets two flag bytes;11178 writes actual argument pointer and

## 0x1120C (ported)

- 13/22/24 "Loading data...." (33C34, 1120C, 4C770 x3, 4C810);
- when the 2A2C8 fade 789CC ends: mode := 77600, 1120C).
- sliders 2B354), 5 -> 0xF screen offset 77814 (-24..24) / 77818 (-16..16) = primary 0x55 / 0x56 via 1120C, Triangle there restores GP+CB4/CB8, 6 done.
- 2B520 = load the working copies (7C6B8 := 1, 7C6BC := 6, 7D310/7D314, 7D300/7D2FC, 7C854/7C858, 77814/CB4, 77818/CB8, 2FF90), 2B5EC = commit them back (+30030, 1120C).
- row 3 Return), 5 Center Screen (77814 -24..24 / 77818 -16..16 = 0x55 / 0x56, 1120C), 6 Exit (Cross release -> keep).

## 0x11230 (todo)

- sdk-hook-points.txt = which game function calls which SDK function (pad = 131CC/12D9C, display env = 11230/104F8, GTE, SPU, CD) = hook points for PC features (controls, resolution).

## 0x1150C (todo)


## 0x11630 (todo)


## 0x11700 (todo)


## 0x11804 (todo)


## 0x1183C (ported)

- 25D18 (called by 26864 / 26764) stores 0 there (0x25D50) with 7B588 := 100, 7B58C/7C7DC := 0, 7C820/7C824 := rand, 16504 (two heap buffers 0x908/0xD8C), title images 1183C (7D36C != 0).
- 25D18 (when GP+1E50 == 0) loads SKY.IMG with 1183C(name, 0x100 CLUT, 0x200 x 0x100, VRAM 0x300,0, CLUT 0x200,0xFA, mode 2).
- r607-title-check + 1183C mode 2 (stubbed file/alloc/read/close/free/DrawSync, 59088 source pointers for h = 0x100 / 0x10 / 0x40): 1,767,470 / 0.
- The IMG layout is 1183C's: a 256-entry CLUT (512 bytes) then w x h 8-bit
- 1183C mode 2, which uploads the image again at y + 0x100 row by row from its last row = SKY.IMG flipped vertically);

## 0x11C44 (ported)

- 11C44 loads GAMEOVER.IMG (512x256 15-bit) to VRAM (512,256);
- 7B78 := 0, 111CC(77808), 11C44 loads

## 0x11D4C (ported)

- 11D4C draws the image;
- then 11D4C draws the GAMEOVER image (16, 0, 512 x 256, 128).
- r607 item 84: the native title (native-front-end-title.h) vs the ORIGINAL code on random states: the backdrop 12660 (11D4C sprites

## 0x1205C (todo)


## 0x12394 (todo)


## 0x124A0 (ported)

- 124A0 mode0: upper pixels+own CLUT;

## 0x12660 (ported)

- 3000-frame idle -> attract mode 4), mode 6 = LOAD MENU: enter 26864, frame 2777C (27028, 12660, 318B8), check 25104 (24D34;
- 12660.
- TITLE SCREEN (MODE 2) + FRONT-END BACKDROP 12660 (2026-11-01).
- 26E54 frame: GP+1E5C countdown, L1/R1 dropped (10268 cheats not ported), 339F8, the 19F04 items 144 "Start Game" / 135 "Options" (78AF4 cursor) once the wait ends, 12660, 169A4 logo, 1A044 {68 copyright, 0xEC}, and the background world's frame LAST (27028).
- 12660 backdrop words (native_front_end_backdrop): 7BA54 scroll (+2 every front-end frame), and in mode 2 the lightning machine: 7B588 bolt timer (other buttons speed it), 7B58C thunder timer, 6AC1C flash sequence 7C7DC, bolt position 7C820/7C824 from rand.

## 0x12AB4 (ported)


## 0x12C50 (todo)


## 0x12D74 (ported)

- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- RISK: frame header clears the pad when 789CC != 0 (12D74, oracle-exact);
- 12D74, 2A898 pad repeat GP+D18/D19/D1C/D20, 2B354 sliders, 2B4D8, the list, sound screen 0xE, screen-position screen 0xF), native_options_check (24AFC + 2B5EC cancel + 30030), native_options_defaults (3418C), NativeAudioOptions (engine manager +5C volumes / system +A4 mode as 4C770 / 4C810 leave them;
- 6 -> 12D74 + 78E38 |= 8 (Continue: 27028 then sees Start);
- 12D74 at the top only in mode 5.

## 0x12D9C (ported)

- sdk-hook-points.txt = which game function calls which SDK function (pad = 131CC/12D9C, display env = 11230/104F8, GTE, SPU, CD) = hook points for PC features (controls, resolution).

## 0x12E44 (ported)

- stick calibration after the 0x12E44 range check fails (its reset branch): centre 128, max 255, min 0 for both sticks.

## 0x13128 (todo)


## 0x131CC (ported)

- sdk-hook-points.txt = which game function calls which SDK function (pad = 131CC/12D9C, display env = 11230/104F8, GTE, SPU, CD) = hook points for PC features (controls, resolution).
- else wait for Cross release (131CC loop) and 77610 := 0;
- Reader 131CC (pad poll, 133A0..13450): with primary 0x57 (Vibration) on, a vibration pad, mode 3 or 5, 77610 == 0 or cursor 7C6B8 == 1, 789CC == 0, first port: actuator byte 0x26 = (78E0C != 0), 0x27 = low byte 78DF8.
- NativePcSession::rumble() = {78DF8 low byte x257 -> XInput low-frequency, 78E0C != 0 -> high-frequency 0xFFFF} under the 131CC gate (front-end options, game, pause;
- d-pad bits: NATIVE POLICY, the PC has no 0x131CC stick poll here).

## 0x13A20 (ported)


## 0x13A64 (ported)

- 0x07 72 / 73 = second pad words 0x78E28 (poll sample, held) / 0x78DE0 (13A64 pressed edge) - on PC the second pad is known-absent (0);
- continue the process step, sample primary input (13A64), begin the next frame prefix, drain again.
- r607 item 112: 0x3D07C / 0x3D090 read the second pad words 0x78E28 (held, the poll sample) and 0x78DE0 (pressed edge of 13A64).

## 0x13AB8 (ported)

- 13AB8 writes both the full RAM word and the narrowed lens focal value.
- 13AB8 uses signed ASR of the LOW32 product;

## 0x13ADC (ported)


## 0x13B50 (todo)


## 0x13C1C (todo)


## 0x13C90 (ported)

- Original240D4 orbit eye +13C90/5DD04 view, optional roll5DF44/5E1D4.

## 0x13E0C (ported)

- 13E0C rotation becomes IR = clamp16(floor(M[r][c]*s_c/4096)) via MVMVA sf=1 with IR=(s,0,0)/(0,s,0)/(0,0,s);
- Original 0x3BFF0: build the object matrix from the actor angles (+0x24/+0x28/+0x2C via 0x13E0C), rotate the vector with
- 13E0C masks after>>12.
- 13E0C and34528 construct the row-major Q12 object MATRIX.
- r607: actor matrix builder 34528 (13E0C rotation + scale columns 34554..3463C + translation) against the ORIGINAL,

## 0x140F0 (ported)


## 0x141C4 (todo)


## 0x14208 (ported)

- source 0x14208 "STORY%d.IMG"
- Source 0x142C4 non-reset branch (chapter != multiple of 100): 78EB5=1, 78EA8=chapter, 14208(0) loads only the

## 0x142C4 (ported)

- Source 0x142C4 non-reset branch (chapter != multiple of 100): 78EB5=1, 78EA8=chapter, 14208(0) loads only the

## 0x1437C (ported)

- 0x203 (0x421B4 -> 0x1437C): close the story book (only while busy 78EAC == 0): native_story_close;
- r607: source 0x1437C (ASL 0x203, close the book on chapter n): only while busy 78EAC (signed half) == 0: n % 100 == 0 -> 78EB7 := 1;
- 0x203 (0x421B4 -> 0x1437C book close, 14450 MoveImage leaf) by the ORIGINAL interpreter vs the native VM + native helpers.
- r607: ASL 0x203 (0x421B4 -> 0x1437C) close the book on chapter n (appended ABI)

## 0x14400 (ported)


## 0x14450 (ported)

- then 14450 = DrawSync + MoveImage (768,0,256,256)->(768,256): lower slice := upper slice (mirrored on NativeStoryBookSnapshot).
- then 14450 (DrawSync + MoveImage lower := upper, mirrored on the slices;
- 14450 MoveImage (768,0,256,256)->(768,256): lower slice := upper (unknown stays unknown)
- 0x203 (0x421B4 -> 0x1437C book close, 14450 MoveImage leaf) by the ORIGINAL interpreter vs the native VM + native helpers.

## 0x144A0 (ported)

- 14544 initial reset amplitude0.144A0/5E2E4 only read LUT/math

## 0x14544 (ported)

- 14544 initial reset amplitude0.144A0/5E2E4 only read LUT/math

## 0x145F4 (ported)


## 0x14688 (ported)


## 0x14894 (ported)

- 15114 camera projection/14894 lighting are still separate recovery work.

## 0x14C10 (ported)


## 0x14CA8 (ported)


## 0x15114 (ported)

- 15114 camera projection/14894 lighting are still separate recovery work.

## 0x155F8 (todo)


## 0x15CBC (todo)


## 0x15CE8 (todo)


## 0x15DEC (todo)


## 0x160D4 (todo)


## 0x16254 (todo)


## 0x16504 (todo)

- 25D18 (called by 26864 / 26764) stores 0 there (0x25D50) with 7B588 := 100, 7B58C/7C7DC := 0, 7C820/7C824 := rand, 16504 (two heap buffers 0x908/0xD8C), title images 1183C (7D36C != 0).
- 16504's buffers are not modeled (the background world is cosmetic and thrown away);

## 0x16534 (ported)

- 16534 builds 17x17 SVECTORs (x = -0x780 + 0xF0*col, y = -0x3E8 + 0x7D*row, z 0);
- r607-title-check: 16534 vertices, 16588 TR + squash (x200), 169A4 quads (x2000 random sxy / clock): 1,767,467 / 0.
- 16534 builds 17 x 17 SVECTORs (x = -0x780 + 0xF0 * col, y = -0x3E8 + 0x7D * row, z = 0);
- 16534 + 16588 (the PC's RTPS: identity rotation, z = 0x800 so H / SZ = 1 / 8).
- 16534 (SVECTORs), 16588 (TR, the sy squash;

## 0x16588 (ported)

- 16588 loads the identity matrix 77908, TR = R*(78EDC = 0, -0x190, 0x800) (MVMVA sf=1 cv=TR 0x4A498012, added to r604-source-oracle.h) and RotTransPers 5E3A4 into the sxy table GP+18F4 (row stride 17), then sy := (sy>>1)+(sy>>3).
- r607-title-check: 16534 vertices, 16588 TR + squash (x200), 169A4 quads (x2000 random sxy / clock): 1,767,467 / 0.
- 16588 loads the identity matrix
- 16534 + 16588 (the PC's RTPS: identity rotation, z = 0x800 so H / SZ = 1 / 8).
- 16534 (SVECTORs), 16588 (TR, the sy squash;

## 0x16870 (ported)

- 16870's sine shade table (+0x908) has no reader.
- 16870's 0x908 table (sine shades) has no reader here.
- 169A4 (16534 / 16870 / 16588 / 5D218 stubbed: the primitives from a random sxy table and a random clock).

## 0x1697C (ported)

- 1697C shades a vertex 0xFF when col+row == (78AFC & 0xFF) else 0x80 = a diagonal glint 33 of every 256 frames.
- 1697C shades a vertex 0xFF when col + row == (78AFC & 0xFF), else

## 0x169A4 (ported)

- 26E54 frame: GP+1E5C countdown, L1/R1 dropped (10268 cheats not ported), 339F8, the 19F04 items 144 "Start Game" / 135 "Options" (78AF4 cursor) once the wait ends, 12660, 169A4 logo, 1A044 {68 copyright, 0xEC}, and the background world's frame LAST (27028).
- UK_TEXT logo flat at the top (169A4's wavy GTE grid not ported);
- TITLE LOGO 169A4 (not a wave).
- 169A4 = 16x16 POLY_GT4 of UK_TEXT (u 28*col with the 0x80 page fix, v 10*row, tpage ((14*col+0x200)&0x3FF)>>6 | 0x90, CLUT 5D218(0x200,0x1FF));
- the title step passes 78AFC in the 169A4 call.

## 0x16C44 (ported)


## 0x16D58 (ported)

- Mode 3 enter 264F4 = 77848/7784A, 16D58, 17754(primary[1],[2],[4..5],[3]) -- the same for a new game and a load;
- GP+330..338 (16D58 cursors): the EXE's initial data;
- 16D58's two episode reads use the same current immutable save snapshot.

## 0x16E48 (ported)

- 0x1B7 (0x37EF4 read) / 0x1B8 (0x37E2C store): progress SCALAR with the lazily allocated id at actor+0x152 (16E48 allocate_progress_scalar / 17054 signed byte << 12 / 16F34 byte := popped SRA 12).
- r607: ASL 0x1B7 (0x37EF4 read) / 0x1B8 (0x37E2C store) progress scalar with the lazily allocated id at actor+0x152 (16E48 / 17054 /
- r607: 0x37EF4 (read) / 0x37E2C (store): +0x152 == 0 -> 16E48 allocates a scalar id into it;
- Original3D5AC ->16E48: copy current scalar byte to previous,

## 0x16E88 (ported)

- Original16E48/16E88 read current (+334/+336), write previous (+330/+332)

## 0x16F34 (ported)

- 0x1B7 (0x37EF4 read) / 0x1B8 (0x37E2C store): progress SCALAR with the lazily allocated id at actor+0x152 (16E48 allocate_progress_scalar / 17054 signed byte << 12 / 16F34 byte := popped SRA 12).
- 19E4 actual source37D04/16F34, already-owned slot.
- 16F34) by the ORIGINAL interpreter vs the native VM: stack, pushed value, +0x152, both cursors and every scalar byte.
- byte << 12, or 16F34 stores (popped >> 12, SRA) as a byte.

## 0x16F48 (ported)

- arg: 16F48(0,0x37,0) = primary[0x27B] &= ~0x80, primary[0x572+i] := 0, word primary[0x544+4i] := 0 (i < 6).
- 16F48, whole 33C34 incl.
- No literal write, and no exe constant write (func 16F48 is called with a constant only for bit 55).
- 3407C(slot, 0) fresh new-game reset (0x100 = all slot images), 33AE0(arg) 33AE0 exactly (16F48(0,0x37,0) = clear flag bit
- arg != 0: 16F48(0,0x37,0), then

## 0x17054 (ported)

- 0x1B7 (0x37EF4 read) / 0x1B8 (0x37E2C store): progress SCALAR with the lazily allocated id at actor+0x152 (16E48 allocate_progress_scalar / 17054 signed byte << 12 / 16F34 byte := popped SRA 12).
- r607: ASL 0x1B7 (0x37EF4 read) / 0x1B8 (0x37E2C store) progress scalar with the lazily allocated id at actor+0x152 (16E48 / 17054 /
- then 17054 pushes the signed

## 0x1706C (ported)

- IDs200..255 use the current episode's bank (1706C/16F48), not the

## 0x171B8 (todo)


## 0x171F8 (todo)


## 0x172DC (ported)

- 16/27 "Saving data...." (28734, 172DC);
- 18 write (30B8C checksum -> 0x82F20, 5E7C8, 172DC, 79154 status 6/1/5 -> 30C14 = retry 27, else 79954 -= 2 ...
- state 16/17/18 save (172DC/173CC/17470/5E7C8 write) -> 16 keeps the original "Saving" countdown, 17 = native_save_prepare_slot

## 0x173CC (ported)

- 17 173CC/17470;
- state 16/17/18 save (172DC/173CC/17470/5E7C8 write) -> 16 keeps the original "Saving" countdown, 17 = native_save_prepare_slot

## 0x17470 (ported)

- 17 173CC/17470;
- slot[0] := 1) + 17470 checksum at +0x57C;
- state 16/17/18 save (172DC/173CC/17470/5E7C8 write) -> 16 keeps the original "Saving" countdown, 17 = native_save_prepare_slot
- (33D88 + 17470), 18 = write that one slot;
- 33D88 + 17470 save preparation: 25FB4 on the primary, slot := primary (0x580 bytes), slot[0] := 1 (slot used), then

## 0x175E4 (ported)


## 0x1764C (ported)

- Actual18258->1764C allocation/decode and18260/64 return;

## 0x17754 (ported)

- Mode 3 enter 264F4 = 77848/7784A, 16D58, 17754(primary[1],[2],[4..5],[3]) -- the same for a new game and a load;
- NativeColdSceneContext::load_front_end_game = 264F4/17754 cold load of the image's scene tuple on load_impl (new admission `savedGame`: mode 3 with the front end's raw known image;
- 17754(0,0,999,3) = T0I0M999;
- incoming_previous is the caller's FP (zero on a fresh 17754 entry).
- GAMEOVER.IMG (512 x 256, 15-bit) to VRAM (512, 256), 17754(0, 0, 999, 3) (T0I0M999: the mode-8 scene tuple), 78AE0 := result,

## 0x19418 (ported)

- The original 19418 loader consumes exactly204 sequential records:
- The language heap (19418/194AC, 0x7D350

## 0x1956C (ported)


## 0x19598 (ported)

- Actual17E54..17EB4 and195C8 with1956C/19598 scalar codeunit operations.

## 0x195C8 (ported)


## 0x196E4 (ported)

- 19780 glyph runs become the native slider's eight {glyph, y} pairs, 196E4 / 2B488 dropped.

## 0x19704 (ported)

- 0x19704 print/measure for drawing, 0x19F44/0x34450 prompt effects, 0x533A8 choice UI) are presentation
- 0x19704: sum of glyph advances

## 0x19780 (ported)

- the 19780 slider glyphs;
- sound {0, kind}, 2B10C corner {a0..a5}, 1120C display offset apply, slider {which, y, value, active} (2B354's eight 19780
- Presentation and audio leaves are stubbed in the original and compared call by call (2B354's eight 19780 glyphs against the
- 19780 glyph runs become the native slider's eight {glyph, y} pairs, 196E4 / 2B488 dropped.

## 0x19A14 (todo)


## 0x19CB4 (todo)


## 0x19D98 (ported)

- 19D98's a1 = y, sp+0x18 = x;
- 78DE4 == 2 -> 19D98 "Continue" (150) x 120 / "Quit Game" (147) x 300, y 205, shade 0xA0 chosen / 0x40;
- NATIVE: full-src/native-game-over.h (restore 269C4, step 2516C -> NativeSaveMenuResult calls, new call pc 0x19D98 = native_menu_option_xy {id, y, shade, x});
- otherwise 19D98 options
- 19D98's a1 is y, sp+0x18 x;

## 0x19E98 (ported)

- (2) port 0x318B8 + 30CBC + 31148 state machine exactly (draw via native text 1A044/19E98/19F44, pad 4CDD0/4CD3C);
- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 

## 0x19ECC (ported)

- 1A044 text {id, y}, 19F44 option {id, y, value, current, dim, x}, 19ECC option {id, y, value, current}, 4CDD0/4CD3C menu
- 19ECC = a centred row ("Back").

## 0x19F04 (ported)

- 26E54 frame: GP+1E5C countdown, L1/R1 dropped (10268 cheats not ported), 339F8, the 19F04 items 144 "Start Game" / 135 "Options" (78AF4 cursor) once the wait ends, 12660, 169A4 logo, 1A044 {68 copyright, 0xEC}, and the background world's frame LAST (27028).
- 19F04 items {144 Start Game, y 0xBA, 0} / {135 Options, y 0xCE, 1} with the cursor 78AF4;
- r607 item 84 (NATIVE PC VIEW, cosmetic): the front end's backdrop (12660) and the title's own picture (169A4 logo, 19F04 items,
- The title's calls (native_front_end_title_step): logo, the 19F04 items (cursor = gold), the copyright line.

## 0x19F44 (ported)

- (2) port 0x318B8 + 30CBC + 31148 state machine exactly (draw via native text 1A044/19E98/19F44, pad 4CDD0/4CD3C);
- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- Presentation omitted: the two option icons (0x19F44) and the menu-move sound 9 (0x4CDD0 / 0x4CD3C);
- 1A044 text {id, y}, 19F44 option {id, y, value, current, dim, x}, 19ECC option {id, y, value, current}, 4CDD0/4CD3C menu
- 19F44 with a[4] == 1 = a row label, right-aligned at x;

## 0x1A044 (ported)

- 0x1EC research (2026-11-01): after 41F88 sets 77610 := 2, the main frame driver 27028 (mode 75F8 == 3, control == 2) runs 0x318B8 every frame instead of the process step: a 35-state machine (state word 0x7C7F0, jump table 0x763EC, code 0x318B8..0x33694 ~7.5 KB) that draws strings (1A044, table *0x7D350, e.g.
- (2) port 0x318B8 + 30CBC + 31148 state machine exactly (draw via native text 1A044/19E98/19F44, pad 4CDD0/4CD3C);
- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- 26E54 frame: GP+1E5C countdown, L1/R1 dropped (10268 cheats not ported), 339F8, the 19F04 items 144 "Start Game" / 135 "Options" (78AF4 cursor) once the wait ends, 12660, 169A4 logo, 1A044 {68 copyright, 0xEC}, and the background world's frame LAST (27028).
- 1A044 {68 copyright, y 0xEC};

## 0x1A070 (ported)

- Rendering calls (0x1A070,

## 0x1A114 (ported)

- Recovered argument order and alignment from196E4..1A114/53CF8, expressed

## 0x1A7A4 (ported)


## 0x1AE60 (ported)

- 1AE60 never increments it.

## 0x1B5A0 (ported)

- Defaults (1B5A0 at load, s5 = map header [0x78AE0]): light matrix 0x79274 = header +0x58, colour matrix 0x79254 = header +0x78, FC = 0 (1B840;
- Item 191: visibility setup 0x1B5A0, scene flags [0x7915C] & 0x800 (not special): 107D4(4096) -> [0x7B5F0], 107D4(0x8000) -> [0x7D408] reciprocal table (word 0 = 0, word i = 0x1000000 / i, i < 8192), then a nonzero mode 107D4(8192) -> [0x7D30C].
- defaults (1B5A0, per level): light matrix 0x79274 = map header +0x58, colour matrix 0x79254 = map header +0x78
- r607 item 191: 0x1B5A0 (the setup): 107D4(4096) -> [0x7B5F0];

## 0x1BCBC (ported)


## 0x1BD38 (todo)


## 0x1CEA4 (todo)


## 0x1DF98 (todo)


## 0x1E048 (ported)


## 0x1E070 (todo)


## 0x1E0B4 (ported)

- 0x152 (0x420D4 -> 0x1E0E0): per-frame actor light table 0x7C6F4 (4 x 36 bytes) -> native-actor-light.h (add_native_actor_light / clear_native_actor_lights), stored in NativeActorFramePrefixSnapshot::actor_lights and carried to the next frame with active/owner cleared (= 0x1E0B4 after the render;
- 1DFFC (render) calls 1E368 then 1E0B4.
- NO GTE in 1E0B4..1F664: plain CPU.
- 1E0B4 clears the 4 x 36-byte table 0x7C6F4 (+0x18 owner, +0x1C active).
- r607: the previous frame's render ended with 0x1E0B4 (active/owner cleared);

## 0x1E0E0 (ported)

- 0x152 (0x420D4 -> 0x1E0E0): per-frame actor light table 0x7C6F4 (4 x 36 bytes) -> native-actor-light.h (add_native_actor_light / clear_native_actor_lights), stored in NativeActorFramePrefixSnapshot::actor_lights and carried to the next frame with active/owner cleared (= 0x1E0B4 after the render;
- 1E0E0 = add (item 55);
- ASL 0x152 (0x420D4 -> 0x1E0E0) adds one;
- 0x1E0E0: scan entries in order;
- r607: ASL 0x152 (0x420D4 -> 0x1E0E0 add a per-frame actor light to the 4-entry table 0x7C6F4) by the ORIGINAL interpreter vs the

## 0x1E2FC (ported)

- 1E2FC = UNDO LOG: count [0x7BA40], list [0x7B540] of (address, saved word) pairs walked backwards and restored, then the 4 entries' +0x18 cleared.
- Each frame it undoes its previous edits (1E2FC), then for every active entry of

## 0x1E368 (ported)

- The light RENDERER 0x1E368..0x1F664 (GTE) is NOT ported: no visible light yet.
- 1DFFC (render) calls 1E368 then 1E0B4.
- 1E368 (frame 0x78): undo, reset count, for light entry 0x7C6F4 (+0x1C active;
- Port plan: (1) native_actor_light_relight() that mutates a copy of the scene map bytes exactly (oracle over 1E368 with r604-source-oracle, random lights/cells);
- 0x152 LIGHTS DRAWN (1E368, hybrid map shader).

## 0x1F6AC (ported)

- Render 0x1F6AC

## 0x21FE0 (todo)


## 0x2202C (todo)


## 0x220E8 (todo)


## 0x2225C (todo)


## 0x22AE4 (todo)


## 0x22B28 (ported)


## 0x22C2C (ported)

- Renderer: masked PRIMARY layer of the original render pose 0x22C2C (evaluate_actor_layered_pose in player_pose.cpp): a group with its bit in ctx+0C takes the primary clip key + delta (final group-0 translation - primary group-0 translation);
- r607: masked primary layer of the original render pose 0x22C2C (evaluate_actor_layered_pose).
- Read-only 22C2C secondary full-body branch.
- r607: the masked PRIMARY context layer of the original render pose 0x22C2C.
- 22C2C full-body path: interpolate each clip first, then fixed quaternion /

## 0x2309C (ported)


## 0x23140 (ported)


## 0x231CC (todo)


## 0x2344C (todo)


## 0x2408C (ported)

- only writer besides ASL is the activation's 2408C (0 / 0x1000 / 0, next to the listener reset) -> Impl known_7b52c/words_7b52c set at scene activation, through misc_words, unknown (refused) before one.
- Faithful: the scene entry 264F4 (called from 2674C) runs 2408C for the mode-3 game entry too, so load_front_end_game now sets 0x7B52C / 30 / 34 := 0 / 0x1000 / 0 like the activation (item 119).
- 2408C also zeroes the camera yaw 0x7898E.
- NATIVE POLICY (pad, one frame): NativePcSession::Impl::cold_start_pad (set by start_game(front)) polls the live pad on the first frame through NativeColdSceneContext::snapshot_cold_start_pad_context: camera yaw from the live C6 pose if any (cold_camera_listener), else the root yaw, else 0 (= the 2408C reset value;
- Item 205: 0x2408C (scene setup from 0x266B0;

## 0x240D4 (ported)

- NATIVE POLICY (backend only): the first frame after a cold scene load with a live environment group and no retained 0x240D4 listener yet uses the unpanned runtime gain (RUNTIME_ENVIRONMENT_NO_LISTENER);
- NATIVE POLICY (audio backend, one pass): no 0x240D4 cache exists before the first pass.
- native = prepare_source_visibility: projection 160, eye y 4096) also stores the listener yaw [0x7898E] = 0, and 0x240D4 rewrites it only with a bound camera.
- original6C940, 240D4
- r607 item 136 NATIVE POLICY: a cold start (no pass has produced the 0x240D4 cache yet) treats every live sound as at the

## 0x24CA4 (ported)

- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- Finished = 24CA4 wrote
- 77600 once 24CA4 finished the screen;
- once 24CA4 chose mode 3 the session holds the started world.
- mode 3 enter once 24CA4 chose it.

## 0x24D34 (ported)

- (4) frame driver branch 27028 (75F8 == 3 && 77610 == 2 -> 318B8, 24D34, 28388) and the continue path (load -> scene reload).
- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- r607-save-menu-check 319,734/0 (original 318B8 on all 24 non-I/O states, 24D34 incl.
- 3000-frame idle -> attract mode 4), mode 6 = LOAD MENU: enter 26864, frame 2777C (27028, 12660, 318B8), check 25104 (24D34;
- NATIVE: full-src/native-front-end.h (NativeFrontEnd = one CRT-cleared image + slots + transition globals + menu state): native_front_end_open (26864 above), native_front_end_step (318B8 + 24D34 via native-save-menu.h with E84 = 1;

## 0x25D18 (ported)

- 26864: 25F04 (mode 6 keys [1]=1 [2]=0 [4..5]=0 [3]=3), 4C6AC, GP+584 := 1, E98/E94/E9C/78ADC := 0, 26734 (264F4 loads the front-end background scene 1,0,0,3 -- NOT ported, cosmetic), 267BC (E84 != 0: 3407C(0x100,0), 7D324 := -1, 7D358 := 0, 30C54), 25D18 (title images), fade.
- 25D18 (called by 26864 / 26764) stores 0 there (0x25D50) with 7B588 := 100, 7B58C/7C7DC := 0, 7C820/7C824 := rand, 16504 (two heap buffers 0x908/0xD8C), title images 1183C (7D36C != 0).
- The other 25D18 words have no native reader and stay unowned;
- 25D18 title images NOT drawn.
- OPTIONS MAP (research, NOT PORTED): title item 1 -> mode 5: enter 26764 = 25F04, 78ADC := 0, 26734 (mode 5 background scene), 2B520, 25D18, 2A2C8(2).

## 0x25F04 (ported)

- 26864: 25F04 (mode 6 keys [1]=1 [2]=0 [4..5]=0 [3]=3), 4C6AC, GP+584 := 1, E98/E94/E9C/78ADC := 0, 26734 (264F4 loads the front-end background scene 1,0,0,3 -- NOT ported, cosmetic), 267BC (E84 != 0: 3407C(0x100,0), 7D324 := -1, 7D358 := 0, 30C54), 25D18 (title images), fade.
- VERIFIED: r607-front-end-check 60,003/0 (original 25F04, 25F70, 33AE0(0/1) incl.
- OPTIONS MAP (research, NOT PORTED): title item 1 -> mode 5: enter 26764 = 25F04, 78ADC := 0, 26734 (mode 5 background scene), 2B520, 25D18, 2A2C8(2).
- PC WIRING: no native title (mode 2), so the load menu's PC key O = title item 1 (native_front_end_open_options: 25F04, 78ADC := 0, 2B520;
- 26458 enter: 3407C(0x100,0), 25F04, 78ADC := 0, 25D18 words, 79458 -> GP+1E5C := 0x50 (the 80-frame wait after boot, set by mode 1 26398 only), 26048.

## 0x25F70 (ported)

- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- only text/line/option/ sound/slot list/4C6F8 resume are admitted in game, any other game-data call (3407C new-game slot, 25F70, 33AE0/33BAC, 33C34 load apply, 2A2C8) REFUSES;
- 25F70 = default keys (1,1,7,0 into [1..5], [6..9], [A..D]).
- game-data calls 3407C / 33AE0 / 25F70 / 33C34(+339F8) applied to the image, 2A2C8 cosmetic;
- VERIFIED: r607-front-end-check 60,003/0 (original 25F04, 25F70, 33AE0(0/1) incl.

## 0x25FB4 (ported)

- native_save_prepare_slot = 33D88 (25FB4 remembers location [A..D] := [1],[2],[4],[3] unless episode 1 level 0/9;
- r607-save-storage-check 36,065/0 (original 30B44/30B8C/33D88+25FB4/33C34+26008 + host-file cases).
- T1L9M* (mode not saveable, rule 25FB4) and T1L1M000 are not save-load targets.
- 25FB4 (start of 33D88): remember the location: unless episode [1] == 1 with level [2] 0 or 9, [A]:=[1] [B]:=[2] [C]:=[4] [D]:=[3].
- 33D88 + 17470 save preparation: 25FB4 on the primary, slot := primary (0x580 bytes), slot[0] := 1 (slot used), then

## 0x26008 (ported)

- native_save_apply_slot = 33C34 (primary := slot, backup := primary) + 26008 (location back into [1..9], half [4]).
- r607-save-storage-check 36,065/0 (original 30B44/30B8C/33D88+25FB4/33C34+26008 + host-file cases).
- 33C34 = slot -> primary -> backup, 26008, 77814/77818 := primary[0x55]/[0x56], volumes 4C770(0,[0x52],0x80) (1,[0x52],0x80) (2,[0x53],0x80) 4C810([0x54]) (LB = signed), 77848/7784A, 33AE0(0) unless E8C, 339F8.
- 26008/E8C gate/ 339F8 + volume leaf args, on 5,000 random images;
- 33C34: slot (7D324) -> primary -> backup, 26008, 77814/77818 + volumes (options backend), 77848/7784A (rewritten by 264F4),

## 0x26048 (ported)

- 26458 enter: 3407C(0x100,0), 25F04, 78ADC := 0, 25D18 words, 79458 -> GP+1E5C := 0x50 (the 80-frame wait after boot, set by mode 1 26398 only), 26048.
- wait), 26048 (GP+584 := 0;
- 26048 (7D36C == 1: no 4C6F8)

## 0x26084 (ported)

- Original main loop 10000: mode handler returns nonzero -> 10230 26084 (returns 1 only for front-end 75F8 in {2,5,6,13}) -> gameplay: 5B2B0(0), 5B518(0), 4C63C -> 4A704 (stream close 47C5C/5B5F8/60CA8, GP+11A0 := 0) and the 3-manager table 0x78878 cleared -> j 10044 (next scene load, 4C54C re-creates managers).
- r607 item 214: 10230 -> 4C63C -> 4A704 closes the speech stream on EVERY gameplay scene change (26084 == 0), so the

## 0x26120 (todo)


## 0x26458 (ported)

- 26458 enter: 3407C(0x100,0), 25F04, 78ADC := 0, 25D18 words, 79458 -> GP+1E5C := 0x50 (the 80-frame wait after boot, set by mode 1 26398 only), 26048.
- Mode 2 enter 26458: 7D40C := 1, 3407C(0x100, 0), 25F04, 78ADC := 0, 26734 (background scene: the PC keeps the running one),
- 26458 (header of native-front-end-title.h) on the image.

## 0x264F4 (ported)

- Mode 3 enter 264F4 = 77848/7784A, 16D58, 17754(primary[1],[2],[4..5],[3]) -- the same for a new game and a load;
- 26864: 25F04 (mode 6 keys [1]=1 [2]=0 [4..5]=0 [3]=3), 4C6AC, GP+584 := 1, E98/E94/E9C/78ADC := 0, 26734 (264F4 loads the front-end background scene 1,0,0,3 -- NOT ported, cosmetic), 267BC (E84 != 0: 3407C(0x100,0), 7D324 := -1, 7D358 := 0, 30C54), 25D18 (title images), fade.
- NativeColdSceneContext::load_front_end_game = 264F4/17754 cold load of the image's scene tuple on load_impl (new admission `savedGame`: mode 3 with the front end's raw known image;
- 26864 -> 26734 -> 264F4 builds T1I0M000 (1,0,0,3) in mode 6;
- Faithful: the scene entry 264F4 (called from 2674C) runs 2408C for the mode-3 game entry too, so load_front_end_game now sets 0x7B52C / 30 / 34 := 0 / 0x1000 / 0 like the activation (item 119).

## 0x26734 (ported)

- 26864: 25F04 (mode 6 keys [1]=1 [2]=0 [4..5]=0 [3]=3), 4C6AC, GP+584 := 1, E98/E94/E9C/78ADC := 0, 26734 (264F4 loads the front-end background scene 1,0,0,3 -- NOT ported, cosmetic), 267BC (E84 != 0: 3407C(0x100,0), 7D324 := -1, 7D358 := 0, 30C54), 25D18 (title images), fade.
- 26864 -> 26734 -> 264F4 builds T1I0M000 (1,0,0,3) in mode 6;
- OPTIONS MAP (research, NOT PORTED): title item 1 -> mode 5: enter 26764 = 25F04, 78ADC := 0, 26734 (mode 5 background scene), 2B520, 25D18, 2A2C8(2).
- 26734 background kept, 25D18 / fade cosmetic).
- 12 ticks) on every front-end enter (26734: title, mode 5 options, mode 6 load menu).

## 0x267BC (ported)

- 0x7847C := 0, control 0x77610 := 2 (process step stops), 0x2FF90 (sound settings), 0x4C6AC (stop 3 streams), 0x267BC -> 0x30C54 (menu state).
- (3) 0x1EC effects (progress marks, 339F8, 7847C := 0, 77610 := 2, 2FF90, 4C6AC, 267BC/30C54);
- Save/load step 4: ASL 0x1EC (41F88) is PORTED (native-save-screen.h: 339F8 duplicate native_progress_summary_339f8, hub marks when primary[1..2] == 1/9, E84 := 0, 77610 := 2, 2FF90 hybrid = option bytes primary[0x52..0x54] copied into the backup, 267BC E8C, 30C54 resets).
- 26864: 25F04 (mode 6 keys [1]=1 [2]=0 [4..5]=0 [3]=3), 4C6AC, GP+584 := 1, E98/E94/E9C/78ADC := 0, 26734 (264F4 loads the front-end background scene 1,0,0,3 -- NOT ported, cosmetic), 267BC (E84 != 0: 3407C(0x100,0), 7D324 := -1, 7D358 := 0, 30C54), 25D18 (title images), fade.
- load_front_end_game takes the pre-267BC scene_image).

## 0x27028 (ported)

- 0x1EC research (2026-11-01): after 41F88 sets 77610 := 2, the main frame driver 27028 (mode 75F8 == 3, control == 2) runs 0x318B8 every frame instead of the process step: a 35-state machine (state word 0x7C7F0, jump table 0x763EC, code 0x318B8..0x33694 ~7.5 KB) that draws strings (1A044, table *0x7D350, e.g.
- (4) frame driver branch 27028 (75F8 == 3 && 77610 == 2 -> 318B8, 24D34, 28388) and the continue path (load -> scene reload).
- NativePcSession::advance: while the screen is open, 53FEC samples with control = 77610 (no catch-up), the process/world step is skipped (27028).
- 3000-frame idle -> attract mode 4), mode 6 = LOAD MENU: enter 26864, frame 2777C (27028, 12660, 318B8), check 25104 (24D34;
- 2777C runs its world frame (27028) before 318B8.

## 0x2834C (ported)

- Original: 27028 at 2743C, mode 3, Start (78E38 & 8) with 2834C != 0, 77610 != 2, 7C0E8 == 0, primary byte 3 (82423) != 3, 789B0 == 0: 4CDD0/4CD3C sound;
- 2834C / 7C0E8 / 82423 / 789B0 not modelled);
- Start opens the pause only if: 2834C (28734 = GP+BD8 != 0 and GP+BDC < 0, i.e.
- while 2A230 / 2879C run, 2834C decides exactly.
- r607-options-check + 2834C x40000 (28734 as original) + gate cases: 430,764 / 0.

## 0x28388 (ported)

- (4) frame driver branch 27028 (75F8 == 3 && 77610 == 2 -> 318B8, 24D34, 28388) and the continue path (load -> scene reload).

## 0x284F4 (ported)

- 284F4 draws the phase first: native-title-view.h draw_fade = black quad at min(phase,256)/256 drawn by main before the menu view.
- r607-title-check now also runs 2879C / 2A230 as original (284F4 / 28760 / 28740 stubbed) x20000 + fade_done random against 28734: 1,194,978 checks / 0 failures.
- 284F4 draws the phase before the step (native: black at min(phase,256)/256).
- (284F4 black, 29AE0, 2945C, the 29088 wipe) are all replaced by the same native black-alpha adapter (cosmetic hybrid policy).
- Whole2A230 callback, including28740's callback clear.284F4 draw and saved

## 0x28734 (ported)

- 16/27 "Saving data...." (28734, 172DC);
- check 24AFC: Triangle (78E08 & 0x1000) with cursor 7C6B8 < 0xB -> sound, 2B5EC (commit), GP+57C := 10 -> 2A2C8(1) fade -> 28734 -> mode 2 / 77600 = 2;
- 11 ticks): started on the title's Cross, the title check 24418 waits on 28734 (= BD8) before switching (Start Game -> mode 6, Options).
- r607-title-check now also runs 2879C / 2A230 as original (284F4 / 28760 / 28740 stubbed) x20000 + fade_done random against 28734: 1,194,978 checks / 0 failures.
- Start opens the pause only if: 2834C (28734 = GP+BD8 != 0 and GP+BDC < 0, i.e.

## 0x28740 (ported)

- Entry fade (native-scene-entry-fade.h, native_scene_fade_in_callback) now steps all four fade-in callbacks: identical BDC -= BE0 / 28740 scalar flow (source spans hashed);
- <= -2*step -> 28740 BD8 := 1, 789CC := 0;
- r607-title-check now also runs 2879C / 2A230 as original (284F4 / 28760 / 28740 stubbed) x20000 + fade_done random against 28734: 1,194,978 checks / 0 failures.
- !(-2*BE0 < BDC) -> 28740 BD8 1, 789CC 0, H := BE4).
- phase <= -2 * step -> 28740: BD8 := 1, 789CC := 0).

## 0x28760 (ported)

- > 2*step+0x100 -> 28760 BD8 := 1, 789CC stays;
- r607-title-check now also runs 2879C / 2A230 as original (284F4 / 28760 / 28740 stubbed) x20000 + fade_done random against 28734: 1,194,978 checks / 0 failures.
- 2*BE0+256 < BDC -> 28760 BD8 1, H := BE4, callback kept), 0x29088 open (BDC -= BE0;
- phase > 2 * step + 0x100 -> 28760: BD8 := 1, 789CC stays, black).
- Fade28740/28760 restores only the lens;

## 0x2945C (ported)

- their different draws (29AE0, 2945C, 29088 wipe) all use the native black-alpha adapter (cosmetic hybrid).
- r607: the other 2A2C8 fade-in callbacks (ASL 0xFA): same BDC -= BE0 / 28740 flow, only the draw differs (29AE0, 2945C, wipe).
- (284F4 black, 29AE0, 2945C, the 29088 wipe) are all replaced by the same native black-alpha adapter (cosmetic hybrid policy).

## 0x29AE0 (ported)

- their different draws (29AE0, 2945C, 29088 wipe) all use the native black-alpha adapter (cosmetic hybrid).
- r607: the other 2A2C8 fade-in callbacks (ASL 0xFA): same BDC -= BE0 / 28740 flow, only the draw differs (29AE0, 2945C, wipe).
- (284F4 black, 29AE0, 2945C, the 29088 wipe) are all replaced by the same native black-alpha adapter (cosmetic hybrid policy).
- door fade callback 789CC=0x2A0C0: same scalar flow as 2879C, draw 29AE0 instead of 284F4

## 0x2A280 (ported)

- 2A280 (per frame): the 789CC callback, then 2A594 while 789D0 != 0: two 512x256 TILEs (code 0x62) at (0,0) on the OT head: colour ~c with DR_MODE tpage 0x148 (semi-trans 2, B - F), then c with tpage 0x128 (mode 1, B + F);
- r607 item 90: the screen overlay 2A594 (drawn by 2A280 after the 789CC fade callback while 789D0 != 0;

## 0x2A2C8 (ported)

- 0xFA (0x37874): fade-in cases of 2A2C8 (idx 1->2, 3->10, 4->14, 5->16, else 4): plan_native_fade_request_fa (native-scene-transition.h;
- 0x172 (0x375FC): direct scene change (episode, level, map) without 201's 339F8 pass: plan_native_scene_transition_172 (primary[6..9] := old 1/2/4/3, new 1/2/4..5, [3] := 0, 78ADC := 7, 2A2C8(1) while 789CC == 0).
- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- only text/line/option/ sound/slot list/4C6F8 resume are admitted in game, any other game-data call (3407C new-game slot, 25F70, 33AE0/33BAC, 33C34 load apply, 2A2C8) REFUSES;
- when the 2A2C8 fade 789CC ends: mode := 77600, 1120C).

## 0x2A538 (ported)

- r607: 0x379C8: inline word != 0 -> 2A538 (789D0 := 1, BEC/BF0/BF4/BF8 := 0), else 2A55C (789D0 := 0).

## 0x2A55C (ported)

- r607: 0x379C8: inline word != 0 -> 2A538 (789D0 := 1, BEC/BF0/BF4/BF8 := 0), else 2A55C (789D0 := 0).

## 0x2A56C (ported)

- 0x150 (0x379C8, ONE inline word) / 0x151 (0x37A10 -> 2A56C): screen overlay state Globals::screen_overlay (789D0, GP+BEC..BF8).
- r607: 0x37A10 -> 2A56C: BF8 := top >> 12, BF4 := next, BF0 := next, BEC := bottom (all SRL).

## 0x2A594 (ported)

- Drawn by 2A594 each frame in the original;
- SCREEN OVERLAY 2A594 DRAWN (ASL 0x150 / 0x151) + PS1 BLENDS.
- 2A280 (per frame): the 789CC callback, then 2A594 while 789D0 != 0: two 512x256 TILEs (code 0x62) at (0,0) on the OT head: colour ~c with DR_MODE tpage 0x148 (semi-trans 2, B - F), then c with tpage 0x128 (mode 1, B + F);
- r607-screen-overlay-check (original 2A594 x100000: colours, codes, rects, both tpages): 400,000 / 0;
- r607 item 90: 2A594 screen overlay (ASL 0x150 / 0x151) on the OT head, over the world and its text windows.

## 0x2A898 (ported)

- 12D74, 2A898 pad repeat GP+D18/D19/D1C/D20, 2B354 sliders, 2B4D8, the list, sound screen 0xE, screen-position screen 0xF), native_options_check (24AFC + 2B5EC cancel + 30030), native_options_defaults (3418C), NativeAudioOptions (engine manager +5C volumes / system +A4 mode as 4C770 / 4C810 leave them;
- 2B698 (12D74, 2A898 pad repeat, the options list, the sound screen 0xE with the 2B354 sliders, the screen-position screen 0xF,
- GP+D18, D19 (2A898)
- 2A898: held-direction repeat counters, D18/D19 = counter >= 6 and odd, or a fresh left/right press.
- the 4C830 / 4C7CC getters stubbed), frame 2B698 (12D74, 2A898, 2B354, 2B4D8 run as original code) and check 24AFC (2B5EC, 30030).

## 0x2A984 (ported)


## 0x2A9A4 (todo)


## 0x2A9B0 (todo)


## 0x2A9C8 (todo)


## 0x2A9D4 (todo)


## 0x2A9F0 (todo)


## 0x2A9FC (todo)


## 0x2B044 (todo)


## 0x2B10C (ported)

- Drawing: NativeSaveScreenView::draw_options (labels right-aligned at x, values chained left-aligned, sliders as 8 blocks, 2B10C corners moved by the screen offset);
- draw_options no longer moves the 2B10C corners itself (the original passes fixed coordinates).
- sound {0, kind}, 2B10C corner {a0..a5}, 1120C display offset apply, slider {which, y, value, active} (2B354's eight 19780
- 2B10C corners stay at their fixed coordinates: the display offset (77814 / 77818) moves the whole frame (RendererD3D11::set_display_offset).

## 0x2B20C (todo)


## 0x2B258 (todo)


## 0x2B354 (ported)

- sliders 2B354), 5 -> 0xF screen offset 77814 (-24..24) / 77818 (-16..16) = primary 0x55 / 0x56 via 1120C, Triangle there restores GP+CB4/CB8, 6 done.
- 12D74, 2A898 pad repeat GP+D18/D19/D1C/D20, 2B354 sliders, 2B4D8, the list, sound screen 0xE, screen-position screen 0xF), native_options_check (24AFC + 2B5EC cancel + 30030), native_options_defaults (3418C), NativeAudioOptions (engine manager +5C volumes / system +A4 mode as 4C770 / 4C810 leave them;
- 2B698 (12D74, 2A898 pad repeat, the options list, the sound screen 0xE with the 2B354 sliders, the screen-position screen 0xF,
- sound {0, kind}, 2B10C corner {a0..a5}, 1120C display offset apply, slider {which, y, value, active} (2B354's eight 19780
- 2B354: a +-0x10 step per repeat, clamped 0..0x7F;

## 0x2B488 (ported)

- Not modeled: 2B488 string widths (x positions;
- 2B488 widths of strings 134, 153, 122, 189 (x positions only)
- 2B488 widths);
- 19780 glyph runs become the native slider's eight {glyph, y} pairs, 196E4 / 2B488 dropped.

## 0x2B4D8 (ported)

- 12D74, 2A898 pad repeat GP+D18/D19/D1C/D20, 2B354 sliders, 2B4D8, the list, sound screen 0xE, screen-position screen 0xF), native_options_check (24AFC + 2B5EC cancel + 30030), native_options_defaults (3418C), NativeAudioOptions (engine manager +5C volumes / system +A4 mode as 4C770 / 4C810 leave them;
- vibration_motor() = options 78DF8 (2B4D8: 0xFF fading by 4 per frame) drives the low-frequency motor (x257).
- 78DF8 += 78DFC with 78DFC > 0 forced to -0xFF, clamped 0..255) -- all already native in the process owner -- and the options (2B4D8 / 2B520 / 2B5EC / 2B698).
- 2B4D8 vibration), check 24AFC (Triangle = cancel 2B5EC + 30030;
- 2B4D8.

## 0x2B520 (ported)

- OPTIONS MAP (research, NOT PORTED): title item 1 -> mode 5: enter 26764 = 25F04, 78ADC := 0, 26734 (mode 5 background scene), 2B520, 25D18, 2A2C8(2).
- 2B520 = load the working copies (7C6B8 := 1, 7C6BC := 6, 7D310/7D314, 7D300/7D2FC, 7C854/7C858, 77814/CB4, 77818/CB8, 2FF90), 2B5EC = commit them back (+30030, 1120C).
- full-src/native-options-menu.h: native_options_open (2B520 + 2FF90), native_options_frame (2B698 mode-5 path incl.
- Triangle anywhere below 0xB = cancel (2B5EC restores everything 2B520 saved).
- PC WIRING: no native title (mode 2), so the load menu's PC key O = title item 1 (native_front_end_open_options: 25F04, 78ADC := 0, 2B520;

## 0x2B5EC (ported)

- check 24AFC: Triangle (78E08 & 0x1000) with cursor 7C6B8 < 0xB -> sound, 2B5EC (commit), GP+57C := 10 -> 2A2C8(1) fade -> 28734 -> mode 2 / 77600 = 2;
- 2B520 = load the working copies (7C6B8 := 1, 7C6BC := 6, 7D310/7D314, 7D300/7D2FC, 7C854/7C858, 77814/CB4, 77818/CB8, 2FF90), 2B5EC = commit them back (+30030, 1120C).
- 12D74, 2A898 pad repeat GP+D18/D19/D1C/D20, 2B354 sliders, 2B4D8, the list, sound screen 0xE, screen-position screen 0xF), native_options_check (24AFC + 2B5EC cancel + 30030), native_options_defaults (3418C), NativeAudioOptions (engine manager +5C volumes / system +A4 mode as 4C770 / 4C810 leave them;
- Triangle anywhere below 0xB = cancel (2B5EC restores everything 2B520 saved).
- Option pages in mode 3: top 0x14, title 140 at 0x36, Triangle = sound 2 + 2B5EC, Cross release on Exit -> 0x10 -> back to the list (7C83C := 0, cursor := first, D14 |= 0x100);

## 0x2B698 (ported)

- frame 2774C = 27028 + 2B698 +
- full-src/native-options-menu.h: native_options_open (2B520 + 2FF90), native_options_frame (2B698 mode-5 path incl.
- The in-game pause menu (same 2B698, 775F8 != 5) REFUSES (not ported).
- While 77610 != 0 the process step is skipped and 30394 calls 2B698 (775F8 = 3).
- each paused frame = 53FEC sample with control 1 + 2B698 + apply_option_bytes + audio / display update;

## 0x2D284 (todo)


## 0x2D310 (todo)


## 0x2D3A4 (ported)

- level-start values from 0x2D3A4: flags 0x1100, rest 0), apply_hud_panel_setting.
- 2B6A0..2D3A4 = ONE function shared with the in-game pause menu (775F8 != 5): cursor 7C6B8 items 1 vibration (7D314 = primary 0x57, shown only when 78D55 / 7D304 = pad with vibration), 2 toggle 7C858 = primary 0x571, 3 toggle 7D2FC = primary 0x570 (2FF90 / 30030 apply), 4 -> 0xE sound screen (789A4 row: 0 sound mode 7BA8C 0..2 = primary 0x54 -> 4C810, 1 music 7B5BC = primary 0x52 -> 4C770(0/1), 2 e
- 2D3A4 HUD words and 7D40C are not modelled.
- Deliberately NOT ported (documented owner, no native consumer): 0x40 / 0x07 160 = 0x7B554, a HUD module word (0x2E528 copies 0x7C874 into it every HUD frame while nonzero, 0x2D3A4 zeroes it;
- 0x40 161 / 162 = 0x7BA74 / 0x7C844 (zeroed by the HUD level setup 0x2D3A4 like 0x7B554).

## 0x2D4EC (todo)


## 0x2D550 (todo)


## 0x2D5CC (todo)


## 0x2D6E8 (todo)


## 0x2D858 (todo)


## 0x2DA74 (todo)


## 0x2DB14 (todo)


## 0x2DB90 (todo)


## 0x2DBB8 (todo)


## 0x2DBE0 (todo)


## 0x2E090 (todo)


## 0x2E104 (todo)


## 0x2E160 (todo)


## 0x2E300 (todo)


## 0x2E520 (ported)

- the HUD (0x2E520 -> 0x2F870) overwrites it only from a nonzero [0x7C874]

## 0x2FF90 (ported)

- 0x7847C := 0, control 0x77610 := 2 (process step stops), 0x2FF90 (sound settings), 0x4C6AC (stop 3 streams), 0x267BC -> 0x30C54 (menu state).
- (3) 0x1EC effects (progress marks, 339F8, 7847C := 0, 77610 := 2, 2FF90, 4C6AC, 267BC/30C54);
- Save/load step 4: ASL 0x1EC (41F88) is PORTED (native-save-screen.h: 339F8 duplicate native_progress_summary_339f8, hub marks when primary[1..2] == 1/9, E84 := 0, 77610 := 2, 2FF90 hybrid = option bytes primary[0x52..0x54] copied into the backup, 267BC E8C, 30C54 resets).
- 2B6A0..2D3A4 = ONE function shared with the in-game pause menu (775F8 != 5): cursor 7C6B8 items 1 vibration (7D314 = primary 0x57, shown only when 78D55 / 7D304 = pad with vibration), 2 toggle 7C858 = primary 0x571, 3 toggle 7D2FC = primary 0x570 (2FF90 / 30030 apply), 4 -> 0xE sound screen (789A4 row: 0 sound mode 7BA8C 0..2 = primary 0x54 -> 4C810, 1 music 7B5BC = primary 0x52 -> 4C770(0/1), 2 e
- 2B520 = load the working copies (7C6B8 := 1, 7C6BC := 6, 7D310/7D314, 7D300/7D2FC, 7C854/7C858, 77814/CB4, 77818/CB8, 2FF90), 2B5EC = commit them back (+30030, 1120C).

## 0x30030 (ported)

- 2B6A0..2D3A4 = ONE function shared with the in-game pause menu (775F8 != 5): cursor 7C6B8 items 1 vibration (7D314 = primary 0x57, shown only when 78D55 / 7D304 = pad with vibration), 2 toggle 7C858 = primary 0x571, 3 toggle 7D2FC = primary 0x570 (2FF90 / 30030 apply), 4 -> 0xE sound screen (789A4 row: 0 sound mode 7BA8C 0..2 = primary 0x54 -> 4C810, 1 music 7B5BC = primary 0x52 -> 4C770(0/1), 2 e
- 2B520 = load the working copies (7C6B8 := 1, 7C6BC := 6, 7D310/7D314, 7D300/7D2FC, 7C854/7C858, 77814/CB4, 77818/CB8, 2FF90), 2B5EC = commit them back (+30030, 1120C).
- 12D74, 2A898 pad repeat GP+D18/D19/D1C/D20, 2B354 sliders, 2B4D8, the list, sound screen 0xE, screen-position screen 0xF), native_options_check (24AFC + 2B5EC cancel + 30030), native_options_defaults (3418C), NativeAudioOptions (engine manager +5C volumes / system +A4 mode as 4C770 / 4C810 leave them;
- 2B4D8 vibration), check 24AFC (Triangle = cancel 2B5EC + 30030;
- 30030: the sound screen's saved values back (cancel).

## 0x300E4 (ported)


## 0x302B0 (todo)


## 0x30394 (ported)

- While 77610 != 0 the process step is skipped and 30394 calls 2B698 (775F8 = 3).
- 27028 with 77610 == 1: 53FEC samples (control != 0, no budget catch-up), 30394 runs 2B698, the process step is skipped.

## 0x30498 (ported)

- 0x30498 letterbox counter [0x789B0] (the dialogue window is frozen until it reaches 32).
- 0x30498 letterbox step;

## 0x30A98 (ported)


## 0x30B44 (ported)

- then byte-sum 30B44(slot) of 0x57C bytes == word at slot + 0x57C -> state 13 ("Loading", 81A8 = 45) else 24 ("Loading data....
- Exact game logic: 30B44 slot sum / 30B8C total;
- r607-save-storage-check 36,065/0 (original 30B44/30B8C/33D88+25FB4/33C34+26008 + host-file cases).
- 23 = re-read + 30B44 -> 13 / 24.
- level-smoke.sh fix: a patched save slot must get its 30B44 byte sum rewritten (slot +0x57C = file 0x58C = sum of file bytes 0x10..0x58B), else the load menu marks it damaged and stays in the front end (that was every "C7 owner not published").

## 0x30B8C (ported)

- 11/29/30 "Creating Harry Potter save block" (33FD8, 3407C, 30B8C, 5F71C create, 5F170, 30BCC, 337E0);
- 18 write (30B8C checksum -> 0x82F20, 5E7C8, 172DC, 79154 status 6/1/5 -> 30C14 = retry 27, else 79954 -= 2 ...
- 34 30B8C + 33BAC.
- 30B8C = byte sum of all three.
- Exact game logic: 30B44 slot sum / 30B8C total;

## 0x30BCC (ported)

- 11/29/30 "Creating Harry Potter save block" (33FD8, 3407C, 30B8C, 5F71C create, 5F170, 30BCC, 337E0);
- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- 30BCC
- non-I/O states), the pad step 24D34 (with 24CA4 / 33844 / 33910 / 33968 / 3129C / 336C4 / 30BE8 / 30BCC / 3424C), and the card

## 0x30BE8 (ported)

- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- 30BE8
- non-I/O states), the pad step 24D34 (with 24CA4 / 33844 / 33910 / 33968 / 3129C / 336C4 / 30BE8 / 30BCC / 3424C), and the card

## 0x30C14 (ported)

- 18 write (30B8C checksum -> 0x82F20, 5E7C8, 172DC, 79154 status 6/1/5 -> 30C14 = retry 27, else 79954 -= 2 ...
- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- success words, failure -> 30C14 (state 27).
- 30C14

## 0x30C34 (todo)


## 0x30C54 (ported)

- 0x7847C := 0, control 0x77610 := 2 (process step stops), 0x2FF90 (sound settings), 0x4C6AC (stop 3 streams), 0x267BC -> 0x30C54 (menu state).
- 30C54 resets its words (79934/38/3C/5C, 7C7F0, GP+E64/E74/E78/E80/E7C, GP+E90 := 1).
- (3) 0x1EC effects (progress marks, 339F8, 7847C := 0, 77610 := 2, 2FF90, 4C6AC, 267BC/30C54);
- Save/load step 4: ASL 0x1EC (41F88) is PORTED (native-save-screen.h: 339F8 duplicate native_progress_summary_339f8, hub marks when primary[1..2] == 1/9, E84 := 0, 77610 := 2, 2FF90 hybrid = option bytes primary[0x52..0x54] copied into the backup, 267BC E8C, 30C54 resets).
- 26864: 25F04 (mode 6 keys [1]=1 [2]=0 [4..5]=0 [3]=3), 4C6AC, GP+584 := 1, E98/E94/E9C/78ADC := 0, 26734 (264F4 loads the front-end background scene 1,0,0,3 -- NOT ported, cosmetic), 267BC (E84 != 0: 3407C(0x100,0), 7D324 := -1, 7D358 := 0, 30C54), 25D18 (title images), fade.

## 0x31224 (ported)

- +0x1FC/+0x200/+0x158) and reads the pad (4CDD0/4CD3C), and is mostly a MEMORY CARD flow: libcard/BIOS calls 0x5E444..0x5F818 via 31224 (5F600 event wait, jalr).
- 31224 polls Sync and calls the result callback at GP+E80 (0x31148 accept result: 0 -> Exist + callback 0x30CBC (result table 0x763D4), 1/2 -> state := result).
- Original leaf list as native calls (31224 = card poll, not part of the PC screen).

## 0x3129C (ported)

- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- 33968 / 3129C, slot cursor 336C4) as native code over the PC save file (native-save-storage.h).
- 3129C (cross pressed): returns 0 stay, 1 finished, 2 back (24CA4(1)), 3 leave (24CA4(0)).
- non-I/O states), the pad step 24D34 (with 24CA4 / 33844 / 33910 / 33968 / 3129C / 336C4 / 30BE8 / 30BCC / 3424C), and the card

## 0x318B8 (ported)

- 0x1EC research (2026-11-01): after 41F88 sets 77610 := 2, the main frame driver 27028 (mode 75F8 == 3, control == 2) runs 0x318B8 every frame instead of the process step: a 35-state machine (state word 0x7C7F0, jump table 0x763EC, code 0x318B8..0x33694 ~7.5 KB) that draws strings (1A044, table *0x7D350, e.g.
- 0x318B8 is the GENERAL memory card save/load UI (also used by the save-point path: 0x3F8D0 stores 77610 too), not a game-over-only screen.
- (2) port 0x318B8 + 30CBC + 31148 state machine exactly (draw via native text 1A044/19E98/19F44, pad 4CDD0/4CD3C);
- (4) frame driver branch 27028 (75F8 == 3 && 77610 == 2 -> 318B8, 24D34, 28388) and the continue path (load -> scene reload).
- Native UI code (the 0x318B8 port, step 3) must draw strings via decode_native_display_string / native_display_strings, never from the heap bytes.

## 0x336C4 (ported)

- 535A0, 336C4);
- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- 33968 / 3129C, slot cursor 336C4) as native code over the PC save file (native-save-storage.h).
- 336C4.
- non-I/O states), the pad step 24D34 (with 24CA4 / 33844 / 33910 / 33968 / 3129C / 336C4 / 30BE8 / 30BCC / 3424C), and the card

## 0x337E0 (ported)

- 11/29/30 "Creating Harry Potter save block" (33FD8, 3407C, 30B8C, 5F71C create, 5F170, 30BCC, 337E0);
- result -> 337E0 (30 ok / 27 failed).
- 337E0

## 0x33844 (ported)

- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- r607: the game's save/load screen (frame body 0x318B8, state word 0x7C7F0 / table 0x763EC, pad handlers 24D34 -> 33844 / 33910 /
- 33844 (circle): load menu on a used slot -> "Overwrite and start new game" question.
- non-I/O states), the pad step 24D34 (with 24CA4 / 33844 / 33910 / 33968 / 3129C / 336C4 / 30BE8 / 30BCC / 3424C), and the card

## 0x33910 (ported)

- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- r607: the game's save/load screen (frame body 0x318B8, state word 0x7C7F0 / table 0x763EC, pad handlers 24D34 -> 33844 / 33910 /
- 33910 (square): load menu -> "Begin new game without saving".
- non-I/O states), the pad step 24D34 (with 24CA4 / 33844 / 33910 / 33968 / 3129C / 336C4 / 30BE8 / 30BCC / 3424C), and the card

## 0x33968 (ported)

- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- 33968 / 3129C, slot cursor 336C4) as native code over the PC save file (native-save-storage.h).
- 33968 (triangle): may this state go back?
- non-I/O states), the pad step 24D34 (with 24CA4 / 33844 / 33910 / 33968 / 3129C / 336C4 / 30BE8 / 30BCC / 3424C), and the card

## 0x339E4 (todo)

- 15 339E4;
- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).

## 0x339F8 (ported)

- 0x1EC (0x41F88) is NOT a level exit: it is the shared "health ran out" script (word 199 of the same script in 15 levels) that opens the in-game menu in game-over mode: 0x82420 episode/level == 1/9 -> progression slot marks + 0x339F8;
- 0x172 (0x375FC): direct scene change (episode, level, map) without 201's 339F8 pass: plan_native_scene_transition_172 (primary[6..9] := old 1/2/4/3, new 1/2/4..5, [3] := 0, 78ADC := 7, 2A2C8(1) while 789CC == 0).
- (3) 0x1EC effects (progress marks, 339F8, 7847C := 0, 77610 := 2, 2FF90, 4C6AC, 267BC/30C54);
- Save/load step 4: ASL 0x1EC (41F88) is PORTED (native-save-screen.h: 339F8 duplicate native_progress_summary_339f8, hub marks when primary[1..2] == 1/9, E84 := 0, 77610 := 2, 2FF90 hybrid = option bytes primary[0x52..0x54] copied into the backup, 267BC E8C, 30C54 resets).
- 33C34 = slot -> primary -> backup, 26008, 77814/77818 := primary[0x55]/[0x56], volumes 4C770(0,[0x52],0x80) (1,[0x52],0x80) (2,[0x53],0x80) 4C810([0x54]) (LB = signed), 77848/7784A, 33AE0(0) unless E8C, 339F8.

## 0x33AE0 (ported)

- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- only text/line/option/ sound/slot list/4C6F8 resume are admitted in game, any other game-data call (3407C new-game slot, 25F70, 33AE0/33BAC, 33C34 load apply, 2A2C8) REFUSES;
- 33C34 = slot -> primary -> backup, 26008, 77814/77818 := primary[0x55]/[0x56], volumes 4C770(0,[0x52],0x80) (1,[0x52],0x80) (2,[0x53],0x80) 4C810([0x54]) (LB = signed), 77848/7784A, 33AE0(0) unless E8C, 339F8.
- 33AE0(arg): 7BA38 7D2E0 7C798 7B608 := 0, 7A4A4[6] 7D328/7C6C4/7C7B0[6] := 0;
- game-data calls 3407C / 33AE0 / 25F70 / 33C34(+339F8) applied to the image, 2A2C8 cosmetic;

## 0x33BAC (ported)

- 34 30B8C + 33BAC.
- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- only text/line/option/ sound/slot list/4C6F8 resume are admitted in game, any other game-data call (3407C new-game slot, 25F70, 33AE0/33BAC, 33C34 load apply, 2A2C8) REFUSES;
- 33BAC progress tables, 2A2C8, 4C6F8, 535A0 slot list, 33C34 load apply of state 13) are returned as typed calls, in the

## 0x33C34 (ported)

- 13/22/24 "Loading data...." (33C34, 1120C, 4C770 x3, 4C810);
- native_save_apply_slot = 33C34 (primary := slot, backup := primary) + 26008 (location back into [1..9], half [4]).
- r607-save-storage-check 36,065/0 (original 30B44/30B8C/33D88+25FB4/33C34+26008 + host-file cases).
- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- only text/line/option/ sound/slot list/4C6F8 resume are admitted in game, any other game-data call (3407C new-game slot, 25F70, 33AE0/33BAC, 33C34 load apply, 2A2C8) REFUSES;

## 0x33D88 (ported)

- native_save_prepare_slot = 33D88 (25FB4 remembers location [A..D] := [1],[2],[4],[3] unless episode 1 level 0/9;
- r607-save-storage-check 36,065/0 (original 30B44/30B8C/33D88+25FB4/33C34+26008 + host-file cases).
- (33D88 + 17470), 18 = write that one slot;
- 25FB4 (start of 33D88): remember the location: unless episode [1] == 1 with level [2] 0 or 9, [A]:=[1] [B]:=[2] [C]:=[4] [D]:=[3].
- 33D88 + 17470 save preparation: 25FB4 on the primary, slot := primary (0x580 bytes), slot[0] := 1 (slot used), then

## 0x33E38 (ported)


## 0x33FD8 (ported)

- 11/29/30 "Creating Harry Potter save block" (33FD8, 3407C, 30B8C, 5F71C create, 5F170, 30BCC, 337E0);
- state 11 create block (33FD8 + 30B8C + 5F71C/5F170) -> write a file of three zero slots;
- 33FD8 (+ 3407C(256,0) in the load menu) + 30B8C + create/write: a file of three zero slots.

## 0x34028 (todo)


## 0x3407C (ported)

- 11/29/30 "Creating Harry Potter save block" (33FD8, 3407C, 30B8C, 5F71C create, 5F170, 30BCC, 337E0);
- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- only text/line/option/ sound/slot list/4C6F8 resume are admitted in game, any other game-data call (3407C new-game slot, 25F70, 33AE0/33BAC, 33C34 load apply, 2A2C8) REFUSES;
- 26864: 25F04 (mode 6 keys [1]=1 [2]=0 [4..5]=0 [3]=3), 4C6AC, GP+584 := 1, E98/E94/E9C/78ADC := 0, 26734 (264F4 loads the front-end background scene 1,0,0,3 -- NOT ported, cosmetic), 267BC (E84 != 0: 3407C(0x100,0), 7D324 := -1, 7D358 := 0, 30C54), 25D18 (title images), fade.
- game-data calls 3407C / 33AE0 / 25F70 / 33C34(+339F8) applied to the image, 2A2C8 cosmetic;

## 0x3418C (ported)

- 12D74, 2A898 pad repeat GP+D18/D19/D1C/D20, 2B354 sliders, 2B4D8, the list, sound screen 0xE, screen-position screen 0xF), native_options_check (24AFC + 2B5EC cancel + 30030), native_options_defaults (3418C), NativeAudioOptions (engine manager +5C volumes / system +A4 mode as 4C770 / 4C810 leave them;
- FIXED BOOT GAP: 3418C (boot 106F0 + mode 1 enter 26398: primary 0x52/0x53 := 0x7F, 0x54 := 1, 0x55..0x57 / 0x570 / 0x571 := 0, volumes 0x7F, mode 1) now runs in native_front_end_open;
- KNOWN DIFFERENCE: start_new_game (smoke / regression path) still lacks 3418C, so its progress image differs from the front-end new game exactly at primary + backup 0x52/0x53/0x54 (0 vs 7F/7F/1);
- 500 x 3418C incl.
- NOT DONE (backends: see item 73): (pause menu + 3418C in start_new_game: item 74);

## 0x34224 (ported)

- 34224..34248: exact writes, including the conditional8000 default only

## 0x3424C (ported)

- Save/load screen (native-save-menu.h), step 3: the frame body 318B8, pad step 24D34 (+24CA4, 33844 circle = overwrite, 33910 square = new game without saving, 33968 triangle = back gate, 3129C cross), slot cursor 336C4, 30BE8/30BCC/30C14/ 3424C/339E4, and the card-read result branches 30F4C..31124, transliterated over NativeSaveMenuState (every screen word, named by address).
- 3424C
- non-I/O states), the pad step 24D34 (with 24CA4 / 33844 / 33910 / 33968 / 3129C / 336C4 / 30BE8 / 30BCC / 3424C), and the card

## 0x3426C (ported)

- 535A0 slot list = native "Game Save 1..3"/EMPTY with cursor (no 3426C details yet).
- Used slots show a dot only (3426C details: time/location not drawn yet).
- 3426C slot details still not drawn;
- 535A0 (slots 0x813A0, stride 0x580 = primary layout): used slot (byte 0) -> sprintf("%d%%", ((word +0x3E4 >> 12) * 100) / 47) a..."99'59'59", else h / m / s (108000 / 1800 / 30 ..."0%d" below 10, joined by "'";
- r607-slot-details-check (3426C x200000 with sprintf/strcat rebuilt from the executable's formats, 535A0 x20000 percents / time words / positions): 739,900 / 0.

## 0x34430 (ported)


## 0x34450 (ported)

- 0x19704 print/measure for drawing, 0x19F44/0x34450 prompt effects, 0x533A8 choice UI) are presentation
- 5DAF4 strcat, 34450 glyph conversion, 19D98 draw stubbed: the sprintf formats read from the executable are applied to the

## 0x344AC (ported)

- selector-gates.py synced with the VM (was stale): 10 refused pairs left - 0x07/160 (HUD 0x7B554), 0x07/173 (list length), 0x07/102 (0x7C040), 0x0B/37, 0x1C/140 (344AC anim), 0x40/8, 0x40/47, 0x40/55, 0x40/161..162.
- Remaining refused pairs (selector-gates.py): 0x07/160, 0x0B/37, 0x1C/140 (344AC animation then *(+144)), 0x07/173 (list length), 0x07/102 (0x7C040).
- Actual 1D1/0x41348: ensure context (0x344AC), primary layer pointer := NULL (context+0), actor 9C &= ~0x4000.
- r607: ASL 0x1D2 (0x41388), the primary twin of 0x1D9: after 344AC, ctx+8 (primary rate) := the popped value's low 16 bits.
- r607 item 178: 0x1C selector 140 (table 0x76750[140] = 0x3D74C with s0 = the ROOT [0x78A1C] actor): jal 344AC (ensure the

## 0x34528 (ported)

- C5 point with non-unit actor scale: actor matrix builder 0x34528 scale columns (test is (sx|sy|sz)==4096, an OR;
- r607: actor matrix builder 34528 (13E0C rotation + scale columns 34554..3463C + translation) against the ORIGINAL,

## 0x3466C (ported)

- 346B0 -> 3479C: [0x7C7EC] (normal used) >= capacity or free head [0x78A38] == 0 -> 3466C pops the parameter words and returns 0: no actor, D9 pushes nothing, the caller continues.
- r607 item 146: 346B0 -> 3479C: [0x7C7EC] (normal used) >= capacity or no free head [0x78A38] -> 3466C pops the
- r607 item 146: pool full, 3466C dropped the spawn

## 0x346B0 (ported)

- 0x93 / 0x1E8 = D9 spawn twins (same 0x3E230 + 0x346B0) with record flag +0x14 = 0 / 2 instead of 1: the constructor's other placement branches (0x346E4.., 0x34C34..) must be ported into the D9 path first (13 uses, 3 levels).
- In 346B0 the flag only matters at 34C34 (list insertion;
- 346B0 -> 3479C: [0x7C7EC] (normal used) >= capacity or free head [0x78A38] == 0 -> 3466C pops the parameter words and returns 0: no actor, D9 pushes nothing, the caller continues.
- 346B0 reads the parent header words (+4 cursor, +0x14..+0x1C, +0x24..
- flags&0x400, and calls the constructor 0x346B0 for every other one;

## 0x34D24 (ported)

- classification (36FA4/34D24) requires its own source-qualified service.
- Original36FA4/34D24 perform address arithmetic without a count guard.
- 34D24: signed wrapped XYZ box test;

## 0x34DE0 (ported)

- Source 0x4DAEC (called by 0x3515C through 0x34DE0's tail): walks the live particle/effect list from gp+0x12C0 (0x788B8) through
- 1) when 9C lacks 0x20000000: clear 9C bit 0x40000000 (+dirty 0x7BA68), 0x34DE0 clears every NORMAL actor's DC/D8/E0 reference to the
- r607 item 140: the delete paths (34DE0) clear a child's D8 when its parent dies (e.g.

## 0x34E64 (ported)

- 35D24/34E64 shared resource restoration precedes current actor visits.
- sees the 34E64 reverse restore already performed above, then
- The 34E64

## 0x34EB0 (ported)

- Item 204: post actor pair pass (0x34EB0): the subject's cell byte ([0x7B5FC] map) is read only when a pair needs the cell test (neither A4 has bits 0/1).

## 0x3515C (ported)

- actor deletion 0x3515C keeps an actor (0x20000000) while B8 != 0, and B8 (pass 0x369F0/3684C) = mask of its members with flags1C & 8.
- ITEM 171 (native-normal-delete.h + native_cold_scene.cpp special delete): source order 0x3515C - BC is read only after the B8 != 0 retain check;
- its 3515C deletion in the special pass refuses.
- Special deletion (3515C) unlinks through mixed-pool special-list neighbours (readL / writeL).
- Source 0x4DAEC (called by 0x3515C through 0x34DE0's tail): walks the live particle/effect list from gp+0x12C0 (0x788B8) through

## 0x3534C (ported)

- no 3534C, no category gate, no E0/130 clears);
- 3534C: same actor and owned context, no host or fabricated guest pointer.
- no 3534C, no category gate, no E0/130 clears).
- 3534C writes114;
- 3534C base+previous clocks and35868 fade: previous final holds while fading;

## 0x358BC (ported)

- Special-actor 0x358BC active trigger scan: the verified normal trigger block is now the lambda stageActorTriggers (native_cold_scene.cpp) shared by both pools;
- run_actor_quantum_impl separates the PASS (passSpecial) from the POOL (special): a hosted normal actor gets the special-pass sequence (35E68: A0 gates, 358BC with its normal region, 36EC4;
- 358BC pushes main3DC and consumes pending1;36EC4 clears yield;120/124
- 358BC pushes the current native typed source return, selects1564, then
- runs in the special pass (35E68: 3515C / A0 gates / 358BC / 36EC4;

## 0x35CD0 (ported)


## 0x35FA8 (ported)

- Its only per-frame writer is the actor pass 0x35FA8 (copy at 0x367F4: +34..+40 -> +54..+60;

## 0x364E8 (ported)

- (b) 364E8 moved-model light selection: T1I0M000's grid has empty cells (byte 255) and the original reads row 255 past the scene bytes (heap garbage).
- matrix cache.364E8 intentionally keeps that old cache when A0 skips
- 364E8 normal-list matrix/previous-pose update.
- 364E8 moved-model selection: grid36FA4 or ordered34D24 retention/scan fallback.

## 0x3684C (ported)

- Actor audio tail 0x3684C head: BC != 0 && A0 & 0x800000 releases the group (0x4CEAC -> 0x4B0D4 on manager AF 0 or 2) when 0x4CA0C (*[0x788A0], -1 -> 0, NULL global -> 0) differs from 1 << [0x7C6EC];
- Mono manager-2 streams (ambient loops, flags 6) are NOT played yet (need the 3684C distance / pan policy).
- ALL MANAGER-2 STREAMS (MONO AMBIENT LOOPS) + 3684C VOLUME / PAN (2026-11-01).
- Research: 3684C (per actor with a group, every frame) builds request 7C89C (flags 2, group BC, near B0 -> +20, far B4 -> +24);
- 3684C then stores the 4CEE0 active-channel mask to actor B8 (369B0);

## 0x369F0 (ported)

- actor deletion 0x3515C keeps an actor (0x20000000) while B8 != 0, and B8 (pass 0x369F0/3684C) = mask of its members with flags1C & 8.
- advance_native_sample_stops (start of finish_actor_audio_tail, before 0x369F0) steps the timers by 2*engine+AC per logic frame and executes them through a staged plan + prepare/publish commit.
- r607 item 123: the source manager queue's due sample stops (0x48538 / 0x98 -> 0x487AC) before this frame's 0x369F0 pass.

## 0x36A60 (ported)


## 0x36A90 (todo)


## 0x36AD0 (todo)


## 0x36B5C (ported)

- 0x36B5C the MAP-ACTOR loop constructs ONE ACTOR PER RECORD - it loops the
- EVERY carrier (0x36B5C constructs one actor per record;
- the 0x400 map-record skip loop is 0x36B5C),
- Atomically commits globals/context/phase and stops BEFORE36E90 ->36B5C.
- 36B5C's parent is its stack temporary (SP38).3480C reads unwritten

## 0x36CDC (ported)

- loops exactly those counts (0x36CDC;
- 36CDC, current79158
- 36CDC really cleared this private anchor word;

## 0x36EC4 (ported)

- r607-op153-check (original interpreter 0x36EC4) 20,001/0.
- KEY FACT: the interpreter 0x36EC4 has TWO tables: ops < 0x45 dispatch through 0x6B7FC + 4*op with a1 = high half (imm);
- Checks: r607-op101-check 5,143 / 0 (new: 0xD8 / 0x97 / 0x1D0 against the original interpreter 36EC4, 0x166 / 0xC3 VM paths);
- run_actor_quantum_impl separates the PASS (passSpecial) from the POOL (special): a hosted normal actor gets the special-pass sequence (35E68: A0 gates, 358BC with its normal region, 36EC4;
- actor+0x0C) and calls the ASL interpreter 0x36EC4 on EACH actor;

## 0x36FA4 (ported)

- classification (36FA4/34D24) requires its own source-qualified service.

## 0x374E0 (ported)

- 374E0 is an exact door-cell lookup, not a ground solver.

## 0x37B04 (ported)


## 0x38214 (ported)


## 0x3879C (ported)

- ASL 0x99 with an existing actor sound group (+BC != 0): 0x3879C/0x4CD3C path (channel -1 -> 0x4B2BC on the live group, B8 |= 1<<channel, result = channel).
- a NULL selection makes 3879C return 0 -> push -1 with NO audio/actor effect (read-only, so it composes with a staged effect).
- ASL 0x99 (38ED8 -> 3879C -> 4CD3C(2,...)) starts them;
- a new request of the same actor and manager replaces its voice (3879C existing-group restart);
- a later start on the actor takes the 3879C existing-group branch.

## 0x3A6A4 (ported)

- 1F5/3A81C -> 3A6A4: starting at the CURRENT waypoint (actor+0x1C), test the rectangle spanned by the waypoint and its link (NULL link wraps
- 0x3A81C pops z (top) then x, searches the waypoint rectangles (3A6A4) and pushes 4096 / 0.
- 1F5/3A6A4 search pairs for a rectangle holding (x,z) (appended ABI)

## 0x3B624 (ported)

- 3B624 copies six fields, no padding
- 0x3B624 only touches +0x24..+0x98, inside both the normal (364-byte) and the special (200-byte) actor record.

## 0x3BFF0 (ported)

- ASL 0x5D/0x5E (0x3C4B4/0x3C51C, move by (0,±v,0) in the actor frame via 0x3BFF0).
- Original 0x3BFF0: build the object matrix from the actor angles (+0x24/+0x28/+0x2C via 0x13E0C), rotate the vector with
- handlers 0x3C4B4/0x3C51C/0x3C074/0x3C0B4/0x3C24C/0x3C28C (all through 0x3BFF0 = matrix 13E0C + ApplyMatrixLV 5DBA4).
- is rotated by the actor's own angles and added to its position (0x3BFF0).
- ASL 0x5F (0x3C074 -> 0x3BFF0): move the actor along a vector rotated by its own 3D angles.

## 0x3C560 (ported)

- ITEM 155 (build-180): 0x40 through 3C560 (case table 0x76490): 8 -> actor+58 (pool bytes, previous position y), 47 -> *(actor+E4) (own embedded block +E8 only), 55 -> default case 0x3C8DC returns 0 = a store to address 0 (PS1 kernel low RAM, no gameplay owner): NATIVE POLICY no effect.
- Item 186: 0x37 / 0x3B selector 26 (3C560 [25] = 0x3C604: [0x7BA68] := 1, address target+0xA4) = store of the root's / bound actor's typed A4 word (store_shared_position;
- 3C560/137 returns this exact address.
- r607 item 187: 0x25 (3DEBC) = 3C560 on the iterator actor (+0xDC);
- r607 item 182: ASL 0x1D (0x3E0D8 -> 3C560 on [0x78A1C]): the same pose-word borrow on the ROOT actor.

## 0x3C8F0 (ported)

- 0x1E (0x3DDE4) = the 0x07 field reader 3C8F0 (table 0x76750) applied to the actor at [0x78A28];
- ORACLE: full-src/r607-selector112-check.cpp (`bash run-one-check.sh r607-selector112-check`): 0x454CC pitch (158) vs native_selector_pitch158, and the original read dispatcher 0x3C8F0 (a0 = executing, a1 = read actor, a2 = selector, as ops 0x07 / 0x1C call it) for 110 (vs native_selector_cell_index110 on a random width / zone table), 78 (self -> 0), 15, 169 (= 1 from the executable image): 300,002
- ITEM 130 (build-147): 0x28 selectors 163..166: 0x3DFF8 passes [0x78A2C] to 3C8F0 but bodies 0x3DA70..0x3DAAC read only save words +0x3E8..+0x3F4 -> same read as 0x07 163..166 (save_words.read).
- ITEM 163 (build-198): 0x1C (root actor) selector 138 = 3C8F0 jump table 0x76750[138] = 0x3D718: target+9C & 0x4000 (same as the self 0x07 138).
- Item 207: 0x1C / 0x6A / 0x6B root position readers (3C8F0 with s0 = [0x78A1C], 3A3AC / 3A258 4547C(root+0x34)) never test the root for NULL.

## 0x3E230 (ported)

- 0x93 / 0x1E8 = D9 spawn twins (same 0x3E230 + 0x346B0) with record flag +0x14 = 0 / 2 instead of 1: the constructor's other placement branches (0x346E4.., 0x34C34..) must be ported into the D9 path first (13 uses, 3 levels).
- Item 193: ASL 0xC4 collision sphere on a D9-born actor: locals / triggers / capacity from its 3E230 descriptor, storage from the birth binding (NativeDynamicActorMembershipAccess::collision_capacity) (T1L4M005 record 40, T1L4M006 record 35).
- 3E230 sets desc+0x18 = 0, so a D9 child is always NORMAL (364).
- 3E230 consumes these five inline words, in this order.
- Same 3E230 + 346B0 otherwise.

## 0x3E458 (ported)

- 3E458 with a non-null anchor publishes the unlink + insert-after
- NULL root global: 3E458 then rewinds the instruction cursor by one word and

## 0x3E4CC (ported)


## 0x3E8AC (ported)

- The actual36E88 ->3E8AC transition AFTER committed pools.
- Own selected episode comes from the original filename producer;3E8AC clears once before
- Explicit level-loader36E88 ->3E8AC producer: clear all256 Globals values
- Original level loader 36E88 calls 3E8AC before constructing any actor.
- 3E8AC clears exactly256 globals before static actors at36E88.

## 0x4009C (ported)

- Neither reaches a stopped actor: the 0x189 iterator (4009C) skips +9C & 4, and 457FC gates on & 4.
- 0x1E9/0x1EA (0x401E4/0x40210) are 0x189/0x18A with 0x4009C(1): the A0 0x18000 and 0x880 candidate filter.

## 0x406C0 (ported)

- r607: 0x40928: inline string index, 406D8 string, drawn at anchor x - width (not width/2), then anchor reset (406C0).

## 0x406D8 (ported)

- 0x1EE (0x40858 label at anchor x: NativeWorldLabel::left_aligned) and 0x208 (0x40A60 string empty: n <= 0 -> 4096, else string (n>>12)-1 after the 406D8 '#'/'$' prefixes, first glyph 0/10 -> 4096 else 0;
- r607: ASL 0x208 (0x40A60): after the 406D8 prefixes, a string whose first glyph is 0 or 10 counts as empty (4096), else 0.
- r607: ASL 0x208 (0x40A60 scene string emptiness, via 0x406D8 prefixes and 0x52580) — native_world_label_empty + the VM operand path
- 406D8 string, left / right aligned draw at the label anchor, anchor reset (T1L1M000 script 2 words 79..167).
- r607: 0x40928: inline string index, 406D8 string, drawn at anchor x - width (not width/2), then anchor reset (406C0).

## 0x421F0 (ported)


## 0x4275C (ported)

- 0x1AE (0x40304 -> 0x4275C free a 0x1AD buffer;
- ITEM 166 (native-normal-delete.h): 0x35204 frees a nonzero +144 animation context (0x4275C);
- r607 item 166: source 0x35204 frees a nonzero +144 animation context through 0x4275C.
- r607: ASL 0x1AE: release the buffer a base (offset 0) 0x1AD reference names through 0x4275C;
- r607: ASL 0x1AE (0x40304 -> 0x4275C release) VM path: pops a WordArenaBufferReference and hands (token, origin) to the release

## 0x42858 (ported)

- 42858 or42A00

## 0x429A0 (ported)

- 429A0 with caller-observed successful107D4 allocation.

## 0x42A00 (ported)


## 0x42A48 (ported)


## 0x42B30 (todo)

- 0x78ADC = 5 (reload) is read only by 24790 and mode-3 enter 26588 (-> 1082C + 42B30);

## 0x42B60 (ported)


## 0x42B78 (ported)

- The fog ranges come from the marker record [0x78AD4] (42B78: +0x3C -> [0x79524] near, +0x40 code -> [0x795FC] far = ((2 + (c & 1)) << (((c >> 1) + 8) & 31)) + near;
- 20408..204C8: fog range from the marker record (42B78: +0x3C near / +0x40 encoded far, or +0x34 / +0x38 with +0xA0 bit
- r607 item 99: map fog range = marker record +0x34 near / +0x38 code (42B78: [0x7C784] / [0x7C7E0], [0x7D2F8]).
- 42B78;

## 0x42CC8 (ported)

- contact buffer exactly like 0x42CC8 initialises sp58
- the main query never calls 0x43A78 with +9C bit 0x400 (0x42CC8: if(!(9C&0x400)));
- Original 0x43A78 (dynamic actor-model collision of the normal floor query 0x42CC8) and the merge of its three contact groups
- Full merge of 0x42CC8 (after the static 0x434D0 and dynamic 0x43A78 queries) for the caller 0x39934 (+9C bit 0x40000 cleared):
- Post-actor camera floor (flag 0x8000 with real 0x40000): native-post-static-floor.h with the actor-model contacts merged by the 0x42CC8

## 0x434D0 (ported)

- 434D0 guards43510..43540 return43A4C without contact writes outside the
- with the static 0x434D0 contacts (0x42E44..0x4349C).
- Full merge of 0x42CC8 (after the static 0x434D0 and dynamic 0x43A78 queries) for the caller 0x39934 (+9C bit 0x40000 cleared):

## 0x43A78 (ported)

- Differential check: native query_native_dynamic_floor_core against the ORIGINAL 0x43A78 executed on the research CPU.
- the main query never calls 0x43A78 with +9C bit 0x400 (0x42CC8: if(!(9C&0x400)));
- Original 0x43A78 (dynamic actor-model collision of the normal floor query 0x42CC8) and the merge of its three contact groups
- Plain-data candidate for the arithmetic core (testable against the original 0x43A78 without any level objects).
- Raw result of the three contact groups exactly as 0x43A78 leaves its 0x44-byte buffer (sp58).

## 0x44068 (ported)

- Original 0x44AB8: the actor-model branch of the wall query 0x44068 (the static terrain branch is 0x443A8/0x444E0).
- planes with the 5/4 slack rule) and each accepted face adds its pushout to the accumulator 0x44068 keeps at sp40.
- Original 0x44068 tail after BOTH branches (static accumulator sp10, actor-model accumulator sp40).
- same vector as world->states, for the 0x44068 cross-actor attach (+9C/+E0) alias update
- Original 0x44AB8 actor-model branch (plus the 0x44068 combined tail).

## 0x443A8 (ported)

- Original 0x44AB8: the actor-model branch of the wall query 0x44068 (the static terrain branch is 0x443A8/0x444E0).
- r606: end-to-end check of the actor-model wall branch through the ORIGINAL 0x44068 (static pass 0x443A8 made empty by a 0x0 grid,

## 0x444E0 (ported)

- Original 0x44AB8: the actor-model branch of the wall query 0x44068 (the static terrain branch is 0x443A8/0x444E0).
- Recovered443A8/444E0 static-terrain branch: motion direction, sphere/edge

## 0x44AB8 (ported)

- Original43A78/44AB8 traverse78A34 only, not the special pool.
- Original 0x44AB8: the actor-model branch of the wall query 0x44068 (the static terrain branch is 0x443A8/0x444E0).
- Original 0x44AB8 actor-model branch (plus the 0x44068 combined tail).
- 0x67, 0x81, 0x56..0x58, 0x10A, 0xE9, 0xF9(case 13) and the actor-model wall pass 0x44AB8 (native-dynamic-wall.h).
- ---- 0x44AB8 actor-model wall pass (native-dynamic-wall.h) against the original machine code

## 0x45208 (ported)


## 0x45250 (todo)


## 0x452CC (ported)

- ASL 0x28 selectors 75..78 (book actor distance: 452CC/453C4/4534C/45424).
- selector 75 = 0x452CC: sqrt (5DA54) of the sum of ((target+34/38/3C - executing+34/38/3C) >> 6)^2 via 5FD58 - the same as the already ported iterator-field selectors 75..78.
- op 0x07 selector 43 (0x3CCA8 -> 0x452CC) = 5DA54 sqrt of the 3D sum of ((actor - current waypoint) >> 6)^2 (5FD58), i.e.
- r607: read table 0x76750 [75..78] -> 452CC/453C4/4534C/45424(book+0x34, caller+0x34): 3D/XZ squared q12>>6 distance (77/78)
- Selectors 75 (0x452CC) and 76 (0x453C4) are the source square roots (5DA54) of the 3D / XZ squared sums of selectors 77 / 78.

## 0x4534C (ported)

- ASL 0x28 selectors 75..78 (book actor distance: 452CC/453C4/4534C/45424).
- 0x159 (0x3B22C -> 0x4534C squared distance to a stack point): r607-op159-check 40,000/0.
- record 0 only if type +19 == 2 AND 4534C(r0) < 4534C(r1) unsigned, else record 1 if type 2, else 0 (even if r0 is type 2).
- Item 194: 0x1C selectors 77 / 78 (3D0EC -> 4534C, root minus caller squared distance) from a SPECIAL actor: the caller may be in the 200-byte special pool (only its typed position is read) (T1L6M005 / T1L6M006 special actor word 250).
- 35BAC/35BF0: actor-minus-78A1C root, 4534C truncated GTE squares.

## 0x453C4 (ported)

- ASL 0x28 selectors 75..78 (book actor distance: 452CC/453C4/4534C/45424).
- r607: read table 0x76750 [75..78] -> 452CC/453C4/4534C/45424(book+0x34, caller+0x34): 3D/XZ squared q12>>6 distance (77/78)
- Selectors 75 (0x452CC) and 76 (0x453C4) are the source square roots (5DA54) of the 3D / XZ squared sums of selectors 77 / 78.
- 45424/453C4 never read Y.
- r607 item 105: selectors 75..78 (0x452CC / 0x453C4 / 0x4534C / 0x45424, as in native-iterator-field.h): squared q12>>6

## 0x45424 (ported)

- ASL 0x28 selectors 75..78 (book actor distance: 452CC/453C4/4534C/45424).
- Build-120 adds: 0x07 78 = 0 (0x3D104 -> 45424(s0+34, s1+34);
- op 0x07 (0x3DC60) passes the executing actor as both s0 and s1, 45424 / 5FD58 are pure, so it is the flat squared distance of the actor to itself);
- r607: read table 0x76750 [75..78] -> 452CC/453C4/4534C/45424(book+0x34, caller+0x34): 3D/XZ squared q12>>6 distance (77/78)
- Selectors 77 (0x4534C) and 78 (0x45424) are the squared q12>>6 distance between the caller's pending pose and the

## 0x4547C (ported)

- 0x24/0x1A selectors 74 (yaw toward target, 4547C) and 158 (pitch toward target, 454CC).
- Next barrier there (word 567): 0x1E selector 74 = 0x3D0A4 -> 0x4547C yaw: 5D734 ratan2(d.x, d.z) (full words), (& 0xFFF) << 12;
- ITEM 152 (build-178): 0x22 (E0 target, read table 0x76750) selectors 27 = raw +160 (3CB38), 147..149 = rotation +24/28/2C low 24 bits sign-extended (3D828..3D874), 74 = yaw toward the E0 target (3D0A4 -> 4547C, as 0x1A/0x24 74);
- Item 207: 0x1C / 0x6A / 0x6B root position readers (3C8F0 with s0 = [0x78A1C], 3A3AC / 3A258 4547C(root+0x34)) never test the root for NULL.
- Selector 74 (0x3D0A4 -> 0x4547C): yaw toward the [0x78A28] actor, 5D734 ratan2(d.x, d.z) (full words), (angle & 0xFFF) << 12.

## 0x454CC (ported)

- 0x24/0x1A selectors 74 (yaw toward target, 4547C) and 158 (pitch toward target, 454CC).
- Barrier there (record 40, word 560): 0x1E selector 158 = 0x3D9DC -> 0x454CC pitch toward the [0x78A28] actor: d = target - executing (+34/38/3C), 5FAB8 = GTE SQR sf=1 with IR = int16(d) (MAC = IR^2 >> 12), 5DA54 sqrt(MAC1 + MAC3), 5D734 ratan2(d.y, root), (angle & 0xFFF) << 12.
- Build-119 adds: 0x1C 158 / 0x20 158 = pitch from the executing actor to the root [0x78A1C] / [0x78A30] actor (0x3D9DC -> 454CC, same body as 0x1E 158);
- ORACLE: full-src/r607-selector112-check.cpp (`bash run-one-check.sh r607-selector112-check`): 0x454CC pitch (158) vs native_selector_pitch158, and the original read dispatcher 0x3C8F0 (a0 = executing, a1 = read actor, a2 = selector, as ops 0x07 / 0x1C call it) for 110 (vs native_selector_cell_index110 on a random width / zone table), 78 (self -> 0), 15, 169 (= 1 from the executable image): 300,002
- Read selector 158 (0x3D9DC -> 0x454CC(a0, a1)): d = *a0 - *a1 (full words);

## 0x45548 (ported)

- 0x6E (0x39D20 yaw AND pitch toward a point, 0x45548): r607-op6e-check 10,000/0 (original interpreter).
- r607: ASL 0x6B (0x3A258 turn yaw AND pitch toward the ROOT actor via 0x45548) run by the ORIGINAL interpreter 0x36EC4 against the native VM.
- r607: ASL 0x6E (0x39D20 turn yaw AND pitch toward a point via 0x45548) run by the ORIGINAL interpreter 0x36EC4 against the native VM.
- r607 item 101: 0x3A180 = the pitch half of 0x6B (45548(root+0x34, actor+0x34), only +0x24 turns);
- r607: 0x3A258 = 0x6E toward the ROOT actor (45548(root+0x34, actor+0x34));

## 0x45600 (ported)

- Pair spheres (0x45600) for animated actors: frame-table path (clip+1C frames[+13C], 24-byte entries +18) and bone path (0x5396C via the 0xC5 sampler sample_native_c5_compressed, bone = byte 0 of the +118 entry);
- r607: read-only sources of the animated 0x45600 sphere path: the current scene image (clip + frame tables) and the word arena
- 45600 sphere acquisition is the original separate service boundary.
- 45600 base sphere and unanimated fallback.
- r607: the ANIMATED 0x45600 sphere path (clip +138, frame table, +118 collision table radius) — native_pair_base_sphere with

## 0x457FC (ported)

- Neither reaches a stopped actor: the 0x189 iterator (4009C) skips +9C & 4, and 457FC gates on & 4.
- 457FC exact scalar/order layer.

## 0x45B64 (ported)

- 45B64 leaves7BA60/queue contents unchanged;

## 0x45BC8 (ported)

- 45BC8 globals in this order:7C790,7B53C,7BA78,7C868,7BA4C,7BA50.

## 0x45ED8 (ported)

- 45ED8: strict comparisons and the incremented loop's OLD index are significant.

## 0x45F84 (todo)

- the per-frame 45F84 (called from 27380 when the marker resource is set) that draws it is not ported either (no refusal;

## 0x467DC (ported)


## 0x46810 (ported)

- M001 -> T1L1M003 (door 134) + SCENE RESOURCE 46810.
- M003's door marker +36 names a resource model, so the load reaches 42CB0 jal 46810.
- New DPSX phase Resource46810 (dpsx_load_prefix.cpp, scene_marker_helper complete_scene_marker_resource_return): records 46810's word stores 46870..468A8 exactly (7D340 / 7D348 / 7C7A8 / 7D344 / 7D34C / 7C7AC := 0x7D000, 7D404 / 7C6F0 := 0) and returns 42CB8 -> 42CC0 -> 18A50 with v0 = 0 (46810's loop exit).
- r607 item 116: 46810(a0 = marker).
- r607 item 116: a nonzero marker resource is admitted only after the recorded 46810 return (its last store 468A8).

## 0x46B6C (ported)


## 0x46B88 (ported)

- 46B88 rounds with wrapped(a1+63)&~63, compares unsigned wrapped head+request
- First actual selected-map bank: genuine prewait ->46B88 reservation and

## 0x46BBC (ported)

- against head_limit, returns0 on exhaustion without changing head.46BBC moves

## 0x46C04 (ported)

- 46C04(7879C,1), wrapped subtraction and unsigned fallback.

## 0x46CA0 (ported)


## 0x46D08 (ported)


## 0x46DE0 (ported)

- then actual46D08 pump +46DE0 condition.

## 0x46E14 (ported)

- 46E14 enqueue.
- 46E14 call;

## 0x46FE8 (ported)


## 0x47134 (ported)


## 0x47148 (ported)


## 0x4724C (ported)

- then 4724C(service+0) (engine+9C == 1 and nonnull: row+4 = row+20 = 0), service+0 = service+8 = 0, member+18 = 0.
- Native: complete_audio_kind1_stream (audio_resource_manager.cpp, native-scene-sound-stop.h) = exact 479C4 / 48450 / 49778 / 4724C on the owned manager / queue / member / engine / service bytes;
- Then 4724C(service+0) (engine+9C == 1 and nonnull: row+4 = row+20 = 0), service+0 =
- r607 item 79: complete_audio_kind1_stream (native 49778 -> 48450 -> 479C4 / 4724C stream member cleanup) vs the ORIGINAL 49778 on

## 0x47358 (todo)


## 0x4744C (ported)

- 4744C (sector done): each 2048-byte sector carries 0x400 bytes per channel (L then R), the engine patches loop flags 6 / 3 into the SPU copy (the file has only the final END block per channel).
- Streamed data: looping mono streams (descriptor flags 6) carry block flag 2 on EVERY block and no END (the engine patches its SPU copy, 4744C);
- Stream completion (+1C & 8 clear) lives in the SPU-driver callbacks (4744C / 4989C tail) -> deferred.
- 4744C rewrites them in the SPU ring), so only filter/shift are validated here.
- interleave 0x400 per channel for stereo, 4744C), played to the end unless descriptor flags & 4 (4B56C +40 == 0: 4989C

## 0x47694 (todo)


## 0x4774C (ported)

- (+12 == root) gets +12 = 0, is unlinked (0x47774) and prepended to the manager free list +0x10 (0x4774C);
- Actual47ACC..47B60 plus24 complete60D28/4774C calls.

## 0x47774 (ported)

- (+12 == root) gets +12 = 0, is unlinked (0x47774) and prepended to the manager free list +0x10 (0x4774C);

## 0x477B4 (ported)


## 0x477DC (ported)

- 477DC writes links only;

## 0x47860 (ported)

- Embedded first-manager512-node478E4/47860 transport.

## 0x478E4 (ported)

- A member with an active voice (+0x3A != 0) would enqueue the 0x478E4 stop command: refused (not composed).
- original pushes volume/pan queue commands (0x478E4, opcode 9/10) every frame;
- Source 0x4C044 (stop channel): 0x4B448 member lookup, then 0x478E4 queues command code 1 with the member in the 0x79484 buffer.

## 0x479C4 (ported)

- else 48450: 479C4(manager+20, member) deletes the member's pending commands (delay moved into the following node, node to the free list, count - 1);
- Native: complete_audio_kind1_stream (audio_resource_manager.cpp, native-scene-sound-stop.h) = exact 479C4 / 48450 / 49778 / 4724C on the owned manager / queue / member / engine / service bytes;
- desc +44 and +40 -> opcode 4 after max(uint32(desc word0*1000)/member+24, m58), +24 0 -> m58), 3 = 0x48450 terminal cleanup (479C4 drop pending nodes, keyoff if 3A 2, 47FE8 unlink, flags&0x80 -> engine+90 &= ~4, 3A 0, flags &= 0x9FFFFE05), 4 = 0x487AC stop (group+10->+10 -> re-queue after m58;
- 479C4(manager+20, member)
- Otherwise 48450: 479C4 deletes the member's pending

## 0x47A78 (ported)


## 0x47A8C (todo)


## 0x47C5C (todo)

- Original main loop 10000: mode handler returns nonzero -> 10230 26084 (returns 1 only for front-end 75F8 in {2,5,6,13}) -> gameplay: 5B2B0(0), 5B518(0), 4C63C -> 4A704 (stream close 47C5C/5B5F8/60CA8, GP+11A0 := 0) and the 3-manager table 0x78878 cleared -> j 10044 (next scene load, 4C54C re-creates managers).

## 0x47D78 (ported)

- 47D78.
- Native owner-driven subsequent4A334+47D78 current idle-resource/clean

## 0x47F28 (ported)

- kind1: 3A -> opcode 3 at 0), 2 = 0x48538 start (key-on 47F28, 3A 2;
- 47F28 priorityFF/channel0.

## 0x47FE8 (ported)

- state3A != 0: 480D0 keyoff per channel (state 2) + 47FE8 channel unlink;
- the hardware part (480D0 / 47FE8) is the native voice's release (NATIVE POLICY: the native voice stands in for state3A 2, which the model never sets;
- desc +44 and +40 -> opcode 4 after max(uint32(desc word0*1000)/member+24, m58), +24 0 -> m58), 3 = 0x48450 terminal cleanup (479C4 drop pending nodes, keyoff if 3A 2, 47FE8 unlink, flags&0x80 -> engine+90 &= ~4, 3A 0, flags &= 0x9FFFFE05), 4 = 0x487AC stop (group+10->+10 -> re-queue after m58;
- part (state 2 keyoff 480D0 / 47FE8 channel unlink) is the native voice's release (NATIVE POLICY: the native voice stands in
- 48450: 479C4 drops the member's pending manager+20 commands, (3A 3: no 480D0 keyoff) 47FE8 channel unlink = the native voice

## 0x4808C (ported)


## 0x480D0 (ported)

- state3A != 0: 480D0 keyoff per channel (state 2) + 47FE8 channel unlink;
- the hardware part (480D0 / 47FE8) is the native voice's release (NATIVE POLICY: the native voice stands in for state3A 2, which the model never sets;
- part (state 2 keyoff 480D0 / 47FE8 channel unlink) is the native voice's release (NATIVE POLICY: the native voice stands in
- 48450: 479C4 drops the member's pending manager+20 commands, (3A 3: no 480D0 keyoff) 47FE8 channel unlink = the native voice
- r607 item 123: the release command (opcode 1, handler 0x48348) of a SAMPLE member: 3A != 0 -> 480D0 keyoff per voice and 3A = 3

## 0x48128 (todo)


## 0x48180 (todo)


## 0x481C8 (todo)


## 0x481F8 (todo)


## 0x48228 (todo)


## 0x4827C (ported)


## 0x482F0 (ported)

- Read-only current active47DF8/482F0/60888 adaptation after first keyon.

## 0x48348 (ported)

- Decoded handlers: 1 = 0x48348 release (3A -> keyoff + 3A 3;
- Port: audio_resource_manager stop_audio_sample_member (487AC+48450) / release_audio_sample_member (48348 flag write);
- r607 item 123: the release command (opcode 1, handler 0x48348) of a SAMPLE member: 3A != 0 -> 480D0 keyoff per voice and 3A = 3
- r607 item 123: the native model never runs the manager callbacks (0x496F8), so every newly queued node of opcode 1 (0x48348

## 0x48450 (ported)

- STREAM COMPLETION (49778 / 48450) + ACTOR B8 LIFECYCLE (369B0 / 369CC) (2026-11-01).
- else 48450: 479C4(manager+20, member) deletes the member's pending commands (delay moved into the following node, node to the free list, count - 1);
- Native: complete_audio_kind1_stream (audio_resource_manager.cpp, native-scene-sound-stop.h) = exact 479C4 / 48450 / 49778 / 4724C on the owned manager / queue / member / engine / service bytes;
- Original: a one-shot channel's end clears the member's active 8 (49778 / 48450);
- desc +44 and +40 -> opcode 4 after max(uint32(desc word0*1000)/member+24, m58), +24 0 -> m58), 3 = 0x48450 terminal cleanup (479C4 drop pending nodes, keyoff if 3A 2, 47FE8 unlink, flags&0x80 -> engine+90 &= ~4, 3A 0, flags &= 0x9FFFFE05), 4 = 0x487AC stop (group+10->+10 -> re-queue after m58;

## 0x48538 (ported)

- kind1: 3A -> opcode 3 at 0), 2 = 0x48538 start (key-on 47F28, 3A 2;
- start handler 0x48538 queues it after max(1000 * descriptor frames / member+24, manager+58) ticks, 0x98 queues it at once.
- release), 2 (0x48538 start) or 4 (0x487AC stop) on manager 0 / 2 is recorded here with its due tick (relative delays summed in
- start handler 0x48538 after max(1000 * descriptor word0 / member+24, manager+58) ticks (none when member+40 == 0 or no
- r607 item 123: the source manager queue's due sample stops (0x48538 / 0x98 -> 0x487AC) before this frame's 0x369F0 pass.

## 0x48820 (ported)

- else 3A 3 + 48450), 8 = 0x48820 pitch (member+24), 9 = 0x488C4 volume (+3B).

## 0x488C4 (ported)

- else 3A 3 + 48450), 8 = 0x48820 pitch (member+24), 9 = 0x488C4 volume (+3B).

## 0x48FAC (todo)


## 0x4907C (todo)


## 0x49158 (todo)


## 0x49294 (todo)


## 0x49778 (ported)

- STREAM COMPLETION (49778 / 48450) + ACTOR B8 LIFECYCLE (369B0 / 369CC) (2026-11-01).
- Source (audio-voice-completion-r1 + EURO1 disasm): the envelope poll 49E5C returning 0 -> 49FF0 -> 49778(manager, payload, payload+0C = member): NULL member+18 -> nothing;
- Native: complete_audio_kind1_stream (audio_resource_manager.cpp, native-scene-sound-stop.h) = exact 479C4 / 48450 / 49778 / 4724C on the owned manager / queue / member / engine / service bytes;
- VERIFIED: r607-stream-completion-check 20,000/0 vs the original 49778 (state3A 2, 3E 0 on the CPU side;
- Original: a one-shot channel's end clears the member's active 8 (49778 / 48450);

## 0x497D4 (ported)


## 0x49B78 (todo)


## 0x49E5C (ported)

- Source (audio-voice-completion-r1 + EURO1 disasm): the envelope poll 49E5C returning 0 -> 49FF0 -> 49778(manager, payload, payload+0C = member): NULL member+18 -> nothing;
- Active-group head is genuinely zero:49E5C/49778 are not skipped.
- Item 79 (NATIVE POLICY for the SPU envelope poll 49E5C -> 49FF0): the actual natural end of a one-shot stream voice

## 0x4A02C (todo)


## 0x4A148 (ported)


## 0x4A334 (ported)


## 0x4A468 (ported)

- Actual4C850->4A468 on the current loaded-scene manager.
- 4A468's NULL path does not read a descriptor.

## 0x4A4A0 (ported)


## 0x4A5D0 (todo)


## 0x4A704 (ported)

- Original main loop 10000: mode handler returns nonzero -> 10230 26084 (returns 1 only for front-end 75F8 in {2,5,6,13}) -> gameplay: 5B2B0(0), 5B518(0), 4C63C -> 4A704 (stream close 47C5C/5B5F8/60CA8, GP+11A0 := 0) and the 3-manager table 0x78878 cleared -> j 10044 (next scene load, 4C54C re-creates managers).
- r607 item 214: 10230 -> 4C63C -> 4A704 closes the speech stream on EVERY gameplay scene change (26084 == 0), so the
- r607 item 214: 4A704 stream close stops the voice model too

## 0x4A740 (ported)


## 0x4AB98 (todo)


## 0x4AD0C (ported)


## 0x4AF24 (todo)


## 0x4AFFC (todo)


## 0x4B0D4 (ported)

- Normal actor deletion with a sound group (B8==0, BC!=0): 0x4CEAC -> 0x4B0D4 group release (release_audio_group, plan_scene_sound_release), published with the deletion.
- Actor audio tail 0x3684C head: BC != 0 && A0 & 0x800000 releases the group (0x4CEAC -> 0x4B0D4 on manager AF 0 or 2) when 0x4CA0C (*[0x788A0], -1 -> 0, NULL global -> 0) differs from 1 << [0x7C6EC];
- ITEM 124 (build-142): deleted-actor group release 0x35238 -> 0x4CEAC(AF, BC): 0x4CEAC loads 0x78878[AF] and calls 0x4B0D4, so manager 0 is the same release;
- r607: source 0x4B0D4 (via 0x4CEAC, actor deletion with +BC): walk the group from its root through the +4 links;
- r607: 0x4CEAC(manager, root) -> 0x4B0D4 on manager 0 (first) or 2 (third);

## 0x4B1A8 (ported)


## 0x4B2BC (ported)

- ASL 0x99 with an existing actor sound group (+BC != 0): 0x3879C/0x4CD3C path (channel -1 -> 0x4B2BC on the live group, B8 |= 1<<channel, result = channel).
- 0x4CD3C(manager[AF]) resolves channel -1 through 0x4B2BC on that group, starts via 0x4BEEC and returns request+14 (else -1);
- continue with plan_scene_sound_channel (0x4B2BC).

## 0x4B448 (ported)

- Same source 0x4B448 walk for a group that is already live in the manager records
- 4B448 found no member: no source effects
- 4B448 lookup sees only our known channel0;4BB2C clamps volume128.
- single channel (request+14 != -1), no start tail: member lookup 0x4B448, early reuse
- Source 0x4C044 (stop channel): 0x4B448 member lookup, then 0x478E4 queues command code 1 with the member in the 0x79484 buffer.

## 0x4B4D8 (ported)


## 0x4B550 (todo)


## 0x4B56C (ported)

- 4B56C (kind1 bind): member +3E = (flags & 1) + 1 channels, +40 = !(flags & 4), +42 = (flags >> 1) & 1, +24 rate, stream start = begin + (+48 << 11).
- channels (4B56C: +3E = (flags & 1) + 1).
- interleave 0x400 per channel for stereo, 4744C), played to the end unless descriptor flags & 4 (4B56C +40 == 0: 4989C

## 0x4B784 (ported)

- the 0x4B784 whole-group walk and its returned active-channel mask (members with a

## 0x4BB2C (ported)

- QuantumAudioStage carries stream_group / stream_volume: 0x99 new group (plan root, min(request volume, 128)), 0x99 existing group (root, request volume), E1 (group, min(volumeWord >> 12, 128) like 386B4 / 4BB2C).
- (b) E5 pitch with known BC: 0x38620..0x38658 request flags 4 / +8 group / +14 channel / +28 = 4D7CC(P) via 4CEE0(AF) -> 4BB2C;
- prepare_audio_sound_early / admit_audio_sound_parameters / enqueue_audio_sound_parameters admit manager 0 (0x78878) as well (source 4BB2C/4BD44 is manager-agnostic: same 76-byte members, shared scratch 0x79484);
- r607 item 120: source 4BB2C/4BD44 is manager-agnostic;
- NATIVE POLICY (r604, backend-owned attenuation): the source 0x4BB2C tail toggles member+0x1C bit31 to the request's bit and, for

## 0x4BEEC (ported)

- ITEM 160 (build-190) NATIVE POLICY (audio backend only): scene spatial rows without 0x10000 (positional emitters, 4D490..4D64C: group-nearest pick, SPU voice query/alloc/start/release 4C14C/4CE6C/4BEEC, handle +36) are skipped = silent;
- the nonempty 0x121 query path refuses), 0x4BEEC engine gate for non-source
- 0x4CD3C(manager[AF]) resolves channel -1 through 0x4B2BC on that group, starts via 0x4BEEC and returns request+14 (else -1);
- nearest row of its group (+24), then queries / allocates / starts / releases an SPU voice (4C14C / 4CE6C / 4BEEC) and copies

## 0x4C044 (ported)

- scene-manager (AF=2) stop 0x98 -> 0x4C044
- Source 0x4C044 (stop channel): 0x4B448 member lookup, then 0x478E4 queues command code 1 with the member in the 0x79484 buffer.

## 0x4C0D8 (ported)

- 4CF48(AF, req flags 1, group BC) -> 4C14C on manager [0x78878+4*AF] (descriptor stride by manager kind +0x4C: 0 -> 20, 1 -> 16) -> 4C0D8 member walk (owner +12, descriptor +0x44, flags +0x1C & 8, channel half +0x38, count byte +0x3D).
- r607 item 106: same 4CF48 -> 4C14C -> 4C0D8 walk on manager [0x78878+4*AF] for AF 0 (first manager) or 2 (scene manager).
- Source 0x4CF48 -> 0x4C14C -> 0x4C0D8 (flags=1 query used by ASL 0x121): channel index

## 0x4C14C (ported)

- 4CF48(AF, req flags 1, group BC) -> 4C14C on manager [0x78878+4*AF] (descriptor stride by manager kind +0x4C: 0 -> 20, 1 -> 16) -> 4C0D8 member walk (owner +12, descriptor +0x44, flags +0x1C & 8, channel half +0x38, count byte +0x3D).
- ITEM 160 (build-190) NATIVE POLICY (audio backend only): scene spatial rows without 0x10000 (positional emitters, 4D490..4D64C: group-nearest pick, SPU voice query/alloc/start/release 4C14C/4CE6C/4BEEC, handle +36) are skipped = silent;
- nearest row of its group (+24), then queries / allocates / starts / releases an SPU voice (4C14C / 4CE6C / 4BEEC) and copies
- r607 item 106: same 4CF48 -> 4C14C -> 4C0D8 walk on manager [0x78878+4*AF] for AF 0 (first manager) or 2 (scene manager).
- The descriptor stride follows the manager kind (+0x4C: kind 0 -> 20, kind 1 -> 16), like 4C14C.

## 0x4C2CC (ported)

- ITEM 142 (build-165): scene fade-in commit takes the source target / slew: prepare_scene_fade_commit_values(engine, next, 0x1000, 0x200) (4C744 -> 4C2CC: B8 = a0 & 0x1FFF, BC = (int16)a1).
- r607 item 142: 4C744(a0, a1) -> 4C2CC stores engine +B8 = a0 & 0x1FFF and +BC = (int16)a1;

## 0x4C2FC (ported)


## 0x4C458 (ported)


## 0x4C4F0 (todo)


## 0x4C514 (todo)


## 0x4C530 (todo)


## 0x4C54C (todo)

- Original main loop 10000: mode handler returns nonzero -> 10230 26084 (returns 1 only for front-end 75F8 in {2,5,6,13}) -> gameplay: 5B2B0(0), 5B518(0), 4C63C -> 4A704 (stream close 47C5C/5B5F8/60CA8, GP+11A0 := 0) and the 3-manager table 0x78878 cleared -> j 10044 (next scene load, 4C54C re-creates managers).

## 0x4C63C (ported)

- Original main loop 10000: mode handler returns nonzero -> 10230 26084 (returns 1 only for front-end 75F8 in {2,5,6,13}) -> gameplay: 5B2B0(0), 5B518(0), 4C63C -> 4A704 (stream close 47C5C/5B5F8/60CA8, GP+11A0 := 0) and the 3-manager table 0x78878 cleared -> j 10044 (next scene load, 4C54C re-creates managers).
- r607 item 214: 10230 -> 4C63C -> 4A704 closes the speech stream on EVERY gameplay scene change (26084 == 0), so the

## 0x4C6AC (ported)

- 0x7847C := 0, control 0x77610 := 2 (process step stops), 0x2FF90 (sound settings), 0x4C6AC (stop 3 streams), 0x267BC -> 0x30C54 (menu state).
- (3) 0x1EC effects (progress marks, 339F8, 7847C := 0, 77610 := 2, 2FF90, 4C6AC, 267BC/30C54);
- NOT applied: 4C6AC/4C6F8 sound-manager pause/resume (audio backend, cosmetic).
- 26864: 25F04 (mode 6 keys [1]=1 [2]=0 [4..5]=0 [3]=3), 4C6AC, GP+584 := 1, E98/E94/E9C/78ADC := 0, 26734 (264F4 loads the front-end background scene 1,0,0,3 -- NOT ported, cosmetic), 267BC (E84 != 0: 3407C(0x100,0), 7D324 := -1, 7D358 := 0, 30C54), 25D18 (title images), fade.
- then 4C6AC + 77604 := 78E10 (pause) or 78E08/78E14 := 0, 78E10 := 77604, 4C6F8 (resume).

## 0x4C6F8 (ported)

- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- only text/line/option/ sound/slot list/4C6F8 resume are admitted in game, any other game-data call (3407C new-game slot, 25F70, 33AE0/33BAC, 33C34 load apply, 2A2C8) REFUSES;
- NOT applied: 4C6AC/4C6F8 sound-manager pause/resume (audio backend, cosmetic).
- then 4C6AC + 77604 := 78E10 (pause) or 78E08/78E14 := 0, 78E10 := 77604, 4C6F8 (resume).
- 7D36C is 1 after mode 1, so no 4C6F8), 7D40C := 0.

## 0x4C744 (ported)

- ITEM 142 (build-165): scene fade-in commit takes the source target / slew: prepare_scene_fade_commit_values(engine, next, 0x1000, 0x200) (4C744 -> 4C2CC: B8 = a0 & 0x1FFF, BC = (int16)a1).
- transition) is composed: 789CC=0x2A0C0, GP+1E64=11, fade BDC=0/BE0=32 (BD8 cleared on return), BE4=projection H, and 4C744(24576,-512)
- Every case: BE4 := 5FBB8 (projection H), 4C744(28672, 512) -> audio engine
- r607 item 142: 4C744(a0, a1) -> 4C2CC stores engine +B8 = a0 & 0x1FFF and +BC = (int16)a1;
- 4C744(28672, 512) audio fade: not modelled here

## 0x4C770 (ported)

- 13/22/24 "Loading data...." (33C34, 1120C, 4C770 x3, 4C810);
- 33C34 = slot -> primary -> backup, 26008, 77814/77818 := primary[0x55]/[0x56], volumes 4C770(0,[0x52],0x80) (1,[0x52],0x80) (2,[0x53],0x80) 4C810([0x54]) (LB = signed), 77848/7784A, 33AE0(0) unless E8C, 339F8.
- 2B6A0..2D3A4 = ONE function shared with the in-game pause menu (775F8 != 5): cursor 7C6B8 items 1 vibration (7D314 = primary 0x57, shown only when 78D55 / 7D304 = pad with vibration), 2 toggle 7C858 = primary 0x571, 3 toggle 7D2FC = primary 0x570 (2FF90 / 30030 apply), 4 -> 0xE sound screen (789A4 row: 0 sound mode 7BA8C 0..2 = primary 0x54 -> 4C810, 1 music 7B5BC = primary 0x52 -> 4C770(0/1), 2 e
- 12D74, 2A898 pad repeat GP+D18/D19/D1C/D20, 2B354 sliders, 2B4D8, the list, sound screen 0xE, screen-position screen 0xF), native_options_check (24AFC + 2B5EC cancel + 30030), native_options_defaults (3418C), NativeAudioOptions (engine manager +5C volumes / system +A4 mode as 4C770 / 4C810 leave them;
- sound engine volumes: boot 100CC / 33C34 / options (4C770, 4C810)

## 0x4C7CC (ported)

- 4C7CC / 4C830 read them).
- (the sound engine's manager volume +5C and system +A4, read back by 4C7CC / 4C830).
- 2FF90: 4C830 / 4C7CC(0, 0x80) / 4C7CC(2, 0x80), each stored as a signed byte into primary + backup and widened back.
- the 4C830 / 4C7CC getters stubbed), frame 2B698 (12D74, 2A898, 2B354, 2B4D8 run as original code) and check 24AFC (2B5EC, 30030).

## 0x4C810 (ported)

- 13/22/24 "Loading data...." (33C34, 1120C, 4C770 x3, 4C810);
- 33C34 = slot -> primary -> backup, 26008, 77814/77818 := primary[0x55]/[0x56], volumes 4C770(0,[0x52],0x80) (1,[0x52],0x80) (2,[0x53],0x80) 4C810([0x54]) (LB = signed), 77848/7784A, 33AE0(0) unless E8C, 339F8.
- 2B6A0..2D3A4 = ONE function shared with the in-game pause menu (775F8 != 5): cursor 7C6B8 items 1 vibration (7D314 = primary 0x57, shown only when 78D55 / 7D304 = pad with vibration), 2 toggle 7C858 = primary 0x571, 3 toggle 7D2FC = primary 0x570 (2FF90 / 30030 apply), 4 -> 0xE sound screen (789A4 row: 0 sound mode 7BA8C 0..2 = primary 0x54 -> 4C810, 1 music 7B5BC = primary 0x52 -> 4C770(0/1), 2 e
- 12D74, 2A898 pad repeat GP+D18/D19/D1C/D20, 2B354 sliders, 2B4D8, the list, sound screen 0xE, screen-position screen 0xF), native_options_check (24AFC + 2B5EC cancel + 30030), native_options_defaults (3418C), NativeAudioOptions (engine manager +5C volumes / system +A4 mode as 4C770 / 4C810 leave them;
- sound engine volumes: boot 100CC / 33C34 / options (4C770, 4C810)

## 0x4C830 (ported)

- 4C7CC / 4C830 read them).
- (the sound engine's manager volume +5C and system +A4, read back by 4C7CC / 4C830).
- 2FF90: 4C830 / 4C7CC(0, 0x80) / 4C7CC(2, 0x80), each stored as a signed byte into primary + backup and widened back.
- the 4C830 / 4C7CC getters stubbed), frame 2B698 (12D74, 2A898, 2B354, 2B4D8 run as original code) and check 24AFC (2B5EC, 30030).

## 0x4C850 (ported)

- It cannot skip111CC/4C850/46810 or admit42B60/fullboot/main.

## 0x4C87C (todo)


## 0x4C8A8 (todo)


## 0x4C8C8 (ported)


## 0x4C97C (ported)


## 0x4CA0C (ported)

- Actor audio tail 0x3684C head: BC != 0 && A0 & 0x800000 releases the group (0x4CEAC -> 0x4B0D4 on manager AF 0 or 2) when 0x4CA0C (*[0x788A0], -1 -> 0, NULL global -> 0) differs from 1 << [0x7C6EC];
- The 3684C actor audio mode release now uses it too: a nonzero 4CA0C mask equal to 1 << (7C6EC & 31) keeps the group (BEQ at 36898), otherwise releases.
- r607: source 0x4CA0C: the current remap global 0x788A0 NULL -> 0, else its first word, with -1 -> 0 (read from the SAME retained
- An actor with BC != 0 and A0 & 0x800000 compares 0x4CA0C (= *[0x788A0], 0 when that remap global is

## 0x4CA38 (todo)


## 0x4CAD8 (todo)


## 0x4CC7C (ported)

- XSPS size, copies declared bytes and executes4C97C/4CC7C metadata effects.

## 0x4CCA8 (ported)


## 0x4CD1C (todo)


## 0x4CD3C (ported)

- ASL 0x99 with an existing actor sound group (+BC != 0): 0x3879C/0x4CD3C path (channel -1 -> 0x4B2BC on the live group, B8 |= 1<<channel, result = channel).
- +0x1FC/+0x200/+0x158) and reads the pad (4CDD0/4CD3C), and is mostly a MEMORY CARD flow: libcard/BIOS calls 0x5E444..0x5F818 via 31224 (5F600 event wait, jalr).
- (2) port 0x318B8 + 30CBC + 31148 state machine exactly (draw via native text 1A044/19E98/19F44, pad 4CDD0/4CD3C);
- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- Menu sounds 4CDD0/4CD3C id 9.

## 0x4CDD0 (ported)

- 0xD1/0xDE existing group (+BC != 0): 0x3889C sets request group/channel -1 then 0x4CDD0;
- +0x1FC/+0x200/+0x158) and reads the pad (4CDD0/4CD3C), and is mostly a MEMORY CARD flow: libcard/BIOS calls 0x5E444..0x5F818 via 31224 (5F600 event wait, jalr).
- (2) port 0x318B8 + 30CBC + 31148 state machine exactly (draw via native text 1A044/19E98/19F44, pad 4CDD0/4CD3C);
- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- Menu sounds 4CDD0/4CD3C id 9.

## 0x4CE6C (ported)

- ITEM 160 (build-190) NATIVE POLICY (audio backend only): scene spatial rows without 0x10000 (positional emitters, 4D490..4D64C: group-nearest pick, SPU voice query/alloc/start/release 4C14C/4CE6C/4BEEC, handle +36) are skipped = silent;
- r607: a group receipt for a group that is ALREADY live in the manager records (actor +BC, created by an earlier 0x3879C/0x4CE6C).
- nearest row of its group (+24), then queries / allocates / starts / releases an SPU voice (4C14C / 4CE6C / 4BEEC) and copies

## 0x4CEAC (ported)

- Normal actor deletion with a sound group (B8==0, BC!=0): 0x4CEAC -> 0x4B0D4 group release (release_audio_group, plan_scene_sound_release), published with the deletion.
- Actor audio tail 0x3684C head: BC != 0 && A0 & 0x800000 releases the group (0x4CEAC -> 0x4B0D4 on manager AF 0 or 2) when 0x4CA0C (*[0x788A0], -1 -> 0, NULL global -> 0) differs from 1 << [0x7C6EC];
- a zero mask with A0 & 0x18000 == 0x18000 releases the group (4CEAC) and clears BC (369CC..369DC).
- ITEM 124 (build-142): deleted-actor group release 0x35238 -> 0x4CEAC(AF, BC): 0x4CEAC loads 0x78878[AF] and calls 0x4B0D4, so manager 0 is the same release;
- r607: source 0x4B0D4 (via 0x4CEAC, actor deletion with +BC): walk the group from its root through the +4 links;

## 0x4CEE0 (ported)

- then 4CEE0 queues it to the group's members.
- 3684C then stores the 4CEE0 active-channel mask to actor B8 (369B0);
- BC != 0 and C >= 0 -> command 4 with 0x4D7CC(P) through 0x4CEE0(AF)) on that channel 0.
- (b) E5 pitch with known BC: 0x38620..0x38658 request flags 4 / +8 group / +14 channel / +28 = 4D7CC(P) via 4CEE0(AF) -> 4BB2C;
- ITEM 149 (build-175): 0xE1 (386E4..38724) on a KNOWN BC group of manager 0: the source builds {8, BC, channel low16, volume>>12} and calls 4CEE0(AF) for any manager (same dispatcher as E5 / item 120).

## 0x4CF14 (ported)

- 0x98 on AF 0 now plans the real 0x4CF14 stop on manager 0 (NativeAudioStartupContext::plan_sound_stop) and ends the actor's recorded backend requests.
- Sound: the user's T1L1M001 barrier "second live audio effect in one quant..." (record 121: 0xDE starts a new manager-0 group 654756, then 0x98 stops its channel in the same quantum) -> QuantumAudioStage::deferred_stop: the stop is planned on the audio owner right after the staged start is published (source order start -> 0x4CF14 stop);
- r607 item 102: a 0x98 stop after the staged effect in the same quantum (source order: start, then 0x4CF14 stop).
- r607 item 198: further 0x98 stops after the first deferred one (no deferred update): each a sequential 4CF14 call, applied in
- r607 item 202: 0x98 stops AFTER the deferred update chain (source order: effect, E1/E5 update(s), then 4CF14 stops);

## 0x4CF48 (ported)

- 4CF48(AF, req flags 1, group BC) -> 4C14C on manager [0x78878+4*AF] (descriptor stride by manager kind +0x4C: 0 -> 20, 1 -> 16) -> 4C0D8 member walk (owner +12, descriptor +0x44, flags +0x1C & 8, channel half +0x38, count byte +0x3D).
- 0x07 136 = text window voice state (0x7C0E8 / 0x7BA98 + 526EC -> 4CF48 voice stream);
- 4CF48 voice query: playing 1 / ended +5B4:=-1, 0).
- r607 item 106: same 4CF48 -> 4C14C -> 4C0D8 walk on manager [0x78878+4*AF] for AF 0 (first manager) or 2 (scene manager).
- Source 0x4CF48 -> 0x4C14C -> 0x4C0D8 (flags=1 query used by ASL 0x121): channel index

## 0x4CF7C (ported)

- else 4CF7C (distance = sqrt-table of the >>6 / >>5 / >>6 deltas to the listener 78994.., angle = (ratan2(dx >> 6, dz >> 6) - listener yaw 7898E) & 0xFFF) and 4D0EC: v = 127 inside B0, (B4 - d) * 127 / (B4 - B0) up to B4;
- In the original every actor with a group (BC != 0, B8 != 0) gets the 3684C 4CF7C / 4D0EC volume pair each frame, the 0xD0 family's manager-0 groups included;
- Exactly recovered here: listener distance (0x4CF7C), near/far high-bit selection,
- 5D734 table for the 4CF7C angle
- its 4CF7C / 4D0EC pair

## 0x4D054 (ported)

- 4D054 with NULL optional angle output: CPU MULT/LO XZ squares, original5DA54*2.

## 0x4D0EC (ported)

- else 4CF7C (distance = sqrt-table of the >>6 / >>5 / >>6 deltas to the listener 78994.., angle = (ratan2(dx >> 6, dz >> 6) - listener yaw 7898E) & 0xFFF) and 4D0EC: v = 127 inside B0, (B4 - d) * 127 / (B4 - B0) up to B4;
- QuantumActorSoundFrame::stream_gain = 4D0EC port;
- VERIFIED: r607-stream-gain-check 200,000/0 (stream_gain vs ORIGINAL 4D0EC, random near / far / distance / angle);
- sync_native_streams scales every voice (stereo included) by volume / 128 on top of the mono 4D0EC pair (NATIVE POLICY: the engine queues command 9 per member;
- In the original every actor with a group (BC != 0, B8 != 0) gets the 3684C 4CF7C / 4D0EC volume pair each frame, the 0xD0 family's manager-0 groups included;

## 0x4D210 (ported)


## 0x4D69C (ported)


## 0x4D708 (todo)


## 0x4D7CC (ported)

- frequency ratio = native_sound_pitch_factor (4D7CC, Q12, 0x1000 = one octave) / 4096, capped at 2 (XAudio voice limit);
- BC != 0 and C >= 0 -> command 4 with 0x4D7CC(P) through 0x4CEE0(AF)) on that channel 0.
- (b) E5 pitch with known BC: 0x38620..0x38658 request flags 4 / +8 group / +14 channel / +28 = 4D7CC(P) via 4CEE0(AF) -> 4BB2C;
- r607 item 120: E5 pitch (request flags 4, +28 = 4D7CC factor) on manager 0 or 2;
- 0x4CDD0 bank, flags|0xD, 0x4D7CC volume;

## 0x4D970 (ported)

- builder snapshot after 0x4D970 normalization (from_builder only)
- 0x4D970
- 0x4F644 pops z, y, x (raw words) into a stack vector, normalizes the builder (0x4D970) and emits at that point (0x4E0E8)
- r607: 0x4F6D8 pops vz (top), vy, vx as LHU+sign halves, normalizes the builder (0x4D970) and emits from the actor position
- ASL 0x1A7 (0x4F600): normalize the builder (0x4D970) and emit it at the executing actor (0x4E430).

## 0x4D9D0 (ported)


## 0x4DA58 (ported)

- ResetPool covers 4DA58 alone, NOT the selected 4DAB4 bootstrap/live pool.

## 0x4DAB4 (ported)

- actual 4DAB4 entry
- ResetPool covers 4DA58 alone, NOT the selected 4DAB4 bootstrap/live pool.

## 0x4DAE4 (ported)


## 0x4DAEC (ported)

- Source 0x4DAEC (called by 0x3515C through 0x34DE0's tail): walks the live particle/effect list from gp+0x12C0 (0x788B8) through
- deleted actor, 0x4DAEC clears the owner of its live effects (project_native_particle_owner_clear, caller), then 9C |= 0x20000000;

## 0x4DB38 (ported)


## 0x4DBC8 (ported)

- 0x1A6 (0x4F544 -> bare 0x4DBC8 with a script vector): plan_particle_point_record `given` vector;
- 0x1AA (0x4F77C builder at a point with a vector -> 0x4DBC8): r607-op1aa-check (VM operand order;
- r607: ASL 0x1A6 (0x4F544 -> 0x4DBC8(actor, template+16, point, vx, vy, vz)): a template emitter whose vector halves come from the
- 0x4DBC8
- Actor+40 is copied by the original but not consumed by4E0E8/4DBC8's final

## 0x4E0E8 (ported)

- r607: ASL 0x1A7 (4F600 -> 4E430(actor, builder 788C0)) and 0x1A8 (4F644 -> 4E0E8(actor, builder, popped point)) use the SAME
- 0x4E0E8
- Research/native candidate for 4E0E8 -> 4DBC8 scalar record construction.
- r607: with `given`, this is the bare 0x4DBC8 constructor (ASL 0x1A6 passes the vector halves itself): the 4E0E8 template vector and
- 0x4F644 pops z, y, x (raw words) into a stack vector, normalizes the builder (0x4D970) and emits at that point (0x4E0E8)

## 0x4E248 (ported)

- 0x1A9 (0x4F6D8 -> 0x4E248 builder from the actor position with a vector): r607-op1a9-check 307,529/0 (oracle admit_4e248 flag added).
- 0x1A5 (0x4F4D0 template emitter from the actor position with a script vector, core 0x4E248) and 0x7A (0x39FFC pitch toward the current waypoint, = 0x6C with the +1C waypoint point): r607-op7a-check 10,001/0.
- 0x4E248
- r607: admit 0x4E248 (ASL 0x1A9 emitter) for its own check only
- r607: ASL 0x1A9 core — 0x4E248 (actor-position offset/spread, then 0x4DBC8 with an explicit vector): plan_particle_actor_point +

## 0x4E430 (ported)

- ASL opcode 0x1A3 (source 0x4F410 -> 0x4E430(actor, template+16)): spawn a particle effect from a
- r607: ASL 0x1A7 (4F600 -> 4E430(actor, builder 788C0)) and 0x1A8 (4F644 -> 4E0E8(actor, builder, popped point)) use the SAME
- 0x4E430
- ASL 0x1A7 (0x4F600): normalize the builder (0x4D970) and emit it at the executing actor (0x4E430).

## 0x4E5DC (ported)


## 0x4E624 (ported)

- ASL 0x18C (0x4E624), appended (ABI)

## 0x4E63C (ported)


## 0x4E684 (ported)

- ASL 0x18F (0x4ECDC): if the template's owner word (+8) is the executing actor it is cleared, then 0x4E684 releases the reference.

## 0x4E708 (ported)


## 0x4E748 (ported)


## 0x4E77C (ported)


## 0x4E868 (ported)


## 0x4E8BC (ported)


## 0x4E8F0 (ported)


## 0x4E9C8 (ported)


## 0x4EA18 (ported)


## 0x4EA28 (ported)


## 0x4EA5C (ported)


## 0x4EA68 (ported)


## 0x4EA78 (ported)


## 0x4EAAC (ported)


## 0x4EABC (ported)


## 0x4EAF8 (ported)


## 0x4EB08 (ported)


## 0x4EB3C (ported)


## 0x4EB54 (ported)


## 0x4F8FC (ported)

- Source 0x4F8FC: per-frame update of the live particle/effect list (gp+0x12C0 active, gp+0x12C4 free).
- 4F8FC incl.

## 0x4FD2C (ported)


## 0x4FD80 (todo)


## 0x51A24 (todo)


## 0x51D18 (ported)


## 0x51D44 (todo)


## 0x520B8 (todo)


## 0x52580 (ported)

- '#' prefix: 52580 counts from byte s+2, reading the LOW byte of each halfword (ctype 0x70665 & 0x44 = hex), count starts 1 and ++ per probe incl.
- '#' skips through 52580 started at BYTE 2 (glyph 1 low byte): count = 1 + every byte read while the
- 0x52580 from byte s+2: count starts 1, ++ per probe, reads the LOW byte of each halfword, stops on non-hex.
- Exact406D8 byte arithmetic: for LHU '#',52580 starts at byte+1 (zero),
- 0x52580: hex id (value = acc*16 + (c>=0x3A?c-0x37:c-0x30)), consumes '#', the digits and one terminator glyph

## 0x525EC (ported)

- NATIVE voice model (replaces the audio-manager voice of 0x525EC/0x526EC/0x5279C): +5B4 stays -1 when no voice plays,

## 0x526EC (ported)

- 0x07 136 = text window voice state (0x7C0E8 / 0x7BA98 + 526EC -> 4CF48 voice stream);
- +5B4 < 0 -> 0x1000, else 526EC (+5B8 != 0 -> -1;
- 526EC (+5B8 != 0 or voice playing) -> 5279C (+5B4 != -1: stop the voice, +5B4 := -1, +5B8 := 0).
- NATIVE voice model (replaces the audio-manager voice of 0x525EC/0x526EC/0x5279C): +5B4 stays -1 when no voice plays,
- 0x526EC result: query of the voice channel

## 0x52770 (todo)


## 0x5279C (ported)

- 526EC (+5B8 != 0 or voice playing) -> 5279C (+5B4 != -1: stop the voice, +5B4 := -1, +5B8 := 0).
- not the finish path), HELD pad word [0x78E10]: left 0x80 with +5C8 == 0 -> 1, right 0x20 with +5C8 != 0 -> 0, square 0x8000 with +5A8 == 0 -> +5A8 = +5C8 ? 8192 : 4096 (option 0 also stops the voice model 5279C).
- NATIVE voice model (replaces the audio-manager voice of 0x525EC/0x526EC/0x5279C): +5B4 stays -1 when no voice plays,
- the first option also stopping the voice (5279C: +5B4 != -1 -> stop;
- 5279C: +5B4 != -1 -> stop.

## 0x52804 (ported)

- The old header claim "+5C4 is never written" was wrong: every ASL dialogue starter writes +5C0 / +5C4 / +5C8 before 0x52804 - 0xF2 (0x52CA4) / 0x1E0 (0x52D54): +5C0 = 4096, +5C4 = 0;
- ITEM 170 (recovered_gameplay.cpp + native_cold_scene.cpp misc selector 0x1088): 0x07 selector 136 after an UNVOICED dialogue start in the same tick: 0x52804 writes +5B4/+5B8 only in the '#' branch (0x528B4..0x528C8), so 3D658 reads the dialogue window 0x7C0E8 with its carried voice state (s39 LessonTimerSprout lip sync after the 0x167 "try again?" prompt).
- 0x52F44 boot projection, 0x52804 start (line split via the existing recovered wrap_original),
- r607 item 157: +5C0 / +5C4 / +5C8 ARE written by the ASL starters before 0x52804 (0xF2 0x52CA4 / 0x1E0 0x52D54: +5C0 = 4096,
- The words each ASL starter writes before 0x52804 (see the header note).

## 0x52F44 (ported)

- Item 213: scene activation with an OPEN window (T1L4M007 frame 126): 10178 -> 52F70 -> 52F44 resets both window structs (+0 active, +1/+2 lines, +5A8 = 4096, +5B0/+5B4 = -1/+5B8 speech words, +5C6), which activate_requested_native_scene already mirrors;
- Source52F70/52F44 freshboot byte7C0E8 producer.
- 0x52F44 boot projection, 0x52804 start (line split via the existing recovered wrap_original),
- source 0x52F44 (plus BSS-zero policy for never-written fields)
- Projection of actual52F70/52F44 freshboot into EXISTING text-state type.

## 0x52F70 (ported)

- Item 213: scene activation with an OPEN window (T1L4M007 frame 126): 10178 -> 52F70 -> 52F44 resets both window structs (+0 active, +1/+2 lines, +5A8 = 4096, +5B0/+5B4 = -1/+5B8 speech words, +5C6), which activate_requested_native_scene already mirrors;
- r607 item 213: an OPEN window no longer refuses: 10178 -> 52F70 -> 52F44 resets both windows (active byte, lines, close flag
- Actual10178->52F70->52F44 resets only these source fields.

## 0x52FA8 (ported)

- NATIVE POLICY (audio backend timing): answered from the state the per-frame 52FA8 update last observed via the same query (voice_active / speech_id), so an end inside the frame is seen from the next update;
- Choice UI 0x533A8 ported (native_text_choice_ui): on every draw path of 0x52FA8 (counting, choice no-page, speech, page advance;
- 0x52FA8 per-frame update for the subset "no speech, no choice, no button page ...",
- 0x52FA8 update.
- state is the one the per-frame 52FA8 update last observed through the same 526EC query (native_text_update: voice_active

## 0x533A8 (ported)

- includes "Would you like to try again?" = probable choice UI, 0x533A8 not composed yet, and a later Glitterby moths task).
- Choice UI 0x533A8 ported (native_text_choice_ui): on every draw path of 0x52FA8 (counting, choice no-page, speech, page advance;
- 0x19704 print/measure for drawing, 0x19F44/0x34450 prompt effects, 0x533A8 choice UI) are presentation
- The choice UI 0x533A8 is ported in native_text_update (logic only;
- 0x533A8 choice UI (only when +5C4 != 0), reading the HELD pad word [0x78E10]: left (0x80) with +5C8 == 0 -> +5C8 = 1, right (0x20)

## 0x53568 (todo)


## 0x535A0 (ported)

- 535A0, 336C4);
- Leaves come back as NativeSaveMenuCall in original order: text 1A044 (id,y), line 19E98 (id,y,128,128,128), option 19F44 (id,y,value,selected,5/4,x 224/288), sound 4CDD0 kind 0 toggle / 1 confirm / 2 back (+4CD3C), and game-data calls for step 4: 3407C new-game slot init (slot|256, keep), 25F70 default options, 33AE0 / 33BAC progress tables, 2A2C8, 4C6F8 resume, 12D74, 535A0 slot list, 33C34 load 
- 535A0 slot list = native "Game Save 1..3"/EMPTY with cursor (no 3426C details yet).
- 535A0 (slots 0x813A0, stride 0x580 = primary layout): used slot (byte 0) -> sprintf("%d%%", ((word +0x3E4 >> 12) * 100) / 47) a..."99'59'59", else h / m / s (108000 / 1800 / 30 ..."0%d" below 10, joined by "'";
- r607-slot-details-check (3426C x200000 with sprintf/strcat rebuilt from the executable's formats, 535A0 x20000 percents / time words / positions): 739,900 / 0.

## 0x53750 (ported)

- Actual538D8/53750 selection, bound to current loader key pointers and the
- 53750 integer division truncates the Q12 weight;

## 0x537A0 (ported)

- 537A0: signed-half operands/weight, arithmetic right shift, then SH narrowing.

## 0x53820 (ported)

- 53820 preserves the complete original16-byte key.

## 0x538D8 (ported)

- 538D8 uses group0 time, not a separate timeline for each bone.

## 0x5396C (ported)

- Pair spheres (0x45600) for animated actors: frame-table path (clip+1C frames[+13C], 24-byte entries +18) and bone path (0x5396C via the 0xC5 sampler sample_native_c5_compressed, bone = byte 0 of the +118 entry);
- 5396C translations: primary is ROOT-relative replacement on a mask hit and
- bone: the 0x5396C local point of bone/group `bone` for the actor at `slot` (the same sampler as ASL 0xC5);
- A NULL f with A+20 != 0 is the 0x5396C bone path (refused);
- 0x45664: bone = byte 0 of the same table entry, local = 0x5396C(actor, bone).

## 0x53CF8 (ported)

- 53CF8 measures with19704 but draws raw.
- Recovered argument order and alignment from196E4..1A114/53CF8, expressed

## 0x53D70 (todo)


## 0x53E3C (todo)


## 0x53F24 (ported)


## 0x53F58 (todo)


## 0x540C8 (todo)


## 0x5410C (todo)


## 0x541BC (todo)


## 0x54498 (todo)


## 0x5456C (todo)


## 0x545FC (todo)


## 0x546B4 (todo)


## 0x54704 (todo)


## 0x54AC8 (todo)


## 0x54B14 (todo)


## 0x54C54 (todo)


## 0x54DD0 (todo)


## 0x5501C (ported)


## 0x5508C (ported)


## 0x55100 (ported)

- Original5508C/555C8/55100.

## 0x555C8 (ported)

- Original5508C/555C8/55100.

## 0x557D4 (todo)


## 0x55898 (ported)

- 55898's actual return address from17B80;

## 0x559E0 (todo)


## 0x55B84 (todo)


## 0x55F3C (ported)

- record+0x1C, map face byte 7 flags and 55F3C GTE vertex-colour relight are lighting presentation (unread natively): native admits only record addresses (index <= 255, as the original) and consumes the operands.
- intensity 0 -> 0x40, 0x1000 -> clear, else byte 3 == 3 -> 0x80) and builds frame 2 with 55F3C = GTE DPCS sf=1 (native_map_dpcs_55f3c: RGB frame 1, FC frame 0 << 4, IR0 intensity) instead of writing scene bytes.
- 55F3C saves/restores it), RGBC = word 0x77A70 = 255,255,255 (lwc2 $6 at 1F750).
- 0x13E relight (55F3C: frame 2 = lerp(frame 1, frame 0, intensity), byte 7 flag 0x80 / 0x40) and the type-1 animation select.
- 55F3C per channel: GTE DPCS sf=1 with RGB = frame 1 byte, FC = frame 0 byte << 4, IR0 = intensity -> lerp toward frame 0.

## 0x56000 (todo)


## 0x560E8 (ported)

- 560E8 squares/shifts each term BEFORE summing, then divides8192<<12.
- Native port of53820/56268/560E8 + the base-clip branch of22C2C.

## 0x56268 (ported)

- 56268: GPF(first) then GPL(second) for components0..2;
- Native port of53820/56268/560E8 + the base-clip branch of22C2C.

## 0x56390 (ported)

- Map (56390, called for every piece from 1C064): SZ3 per vertex, below [0x7C784] colour kept, at / beyond [0x7C7E0] black, between DPCS sf=1 toward FC = 0 with IR0 = ((SZ - near) << 3) >> s7, s7 = ([0x7D2F8] + 1) >> 1, odd s7 adds t >> 2, t >> 4, t >> 8.
- new r607-map-fog-render-check 381,032 / 0 (D3D vs integer 56390 over codes 0,1,2,3,4,5,8,9, +-2);
- r607 item 99: the D3D map shader depth cue (RendererD3D11::MapFog) against the integer 56390 reference: SZ below near keeps
- 56390: SZ below near keeps the colour, at / beyond far it is black, between: DPCS toward FC = 0 with
- 56390 map depth cue: SZ = dot(row, position) in source units;

## 0x565EC (todo)


## 0x57F28 (todo)


## 0x5804C (todo)


## 0x584FC (todo)


## 0x5852C (todo)


## 0x5855C (todo)


## 0x5858C (todo)


## 0x585C0 (todo)


## 0x585F0 (todo)


## 0x58620 (todo)


## 0x58630 (todo)


## 0x58720 (todo)


## 0x58B50 (todo)


## 0x58B74 (todo)


## 0x58CE8 (todo)


## 0x58D44 (todo)


## 0x58DDC (ported)


## 0x58E44 (todo)


## 0x58F60 (todo)


## 0x58FF0 (todo)


## 0x59088 (ported)

- Mode 2 = CLUT copied unchanged to 7B610, the image uploaded at (x, y), then once more at y + 0x100 + k from row h-1-k (one 59088 per row): VRAM 0x300,0x100 = SKY.IMG flipped vertically.
- r607-title-check + 1183C mode 2 (stubbed file/alloc/read/close/free/DrawSync, 59088 source pointers for h = 0x100 / 0x10 / 0x40): 1,767,470 / 0.
- Item 87: 1183C mode 2 (25D18's SKY.IMG, 512 x 256 at VRAM 0x300,0): after the CLUT and the image, one LoadImage 59088 per

## 0x590E8 (ported)


## 0x591A0 (todo)


## 0x5924C (todo)


## 0x592A8 (todo)


## 0x59318 (todo)


## 0x593D8 (todo)


## 0x598D0 (todo)


## 0x59950 (todo)


## 0x59B88 (todo)


## 0x59DF8 (todo)


## 0x59E18 (todo)


## 0x59EB0 (todo)


## 0x59F48 (todo)


## 0x59F64 (todo)


## 0x5A824 (todo)


## 0x5A86C (todo)


## 0x5A8C0 (todo)


## 0x5AB70 (todo)


## 0x5ADD0 (todo)


## 0x5B048 (todo)


## 0x5B07C (todo)


## 0x5B1C0 (todo)


## 0x5B288 (todo)


