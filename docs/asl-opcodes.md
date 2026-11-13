# ASL (strat script) opcodes

For each opcode: our name, handler address in EURO1.GAM, extra instruction words, and notes
collected from the port (comments and the porting log). Notes describe behaviour in our own words; "selector" = the
immediate that picks an actor field. Opcodes without notes are simple (push/branch/arith) or self-explanatory.

## 0x000 `empty_handler_00`

Handler `0x42754`, extra words: 0.

- 0x00 (0x42754 empty), 0x0D/0x0E/0x0F (trigger slot type := 0 / |= 0x80000000 / &= 0x7FFFFFFF;
- 0x09 script-relative reference (0x3E9D8) and 0x00 (0x42754 empty), run by the ORIGINAL interpreter 0x36EC4 against the native VM.

## 0x001 `property_9c_bit1000000`

Handler `0x3B6A8`, extra words: 0.

- 0x3B6A8: imm!=0 -> +9C |= 0x01000000, else &= 0xFEFFFFFF

## 0x002 `skip_encoded_records`

Handler `0x3EAE4`, extra words: 1.

- 3EAE4 consumes an unsigned count, then that many encoded records.

## 0x003 `skip_debug_block`

Handler `0x3EA3C`, extra words: 1.

- 0x136 (0x39688 remove a collision sphere entry, partner of 0xC4) and 0x03 (0x3EA3C skip N instructions, 0x45/0xE2 carry one inline word, then the debug text line 0x7C7E4 = frame_prefix.raw_7c7e4 += 12): r607-op136-3-check 23,000/0.
- ASL 0x3 (0x3EA3C debug block skip) run by the ORIGINAL interpreter against the native VM (cursor and 0x7C7E4 += 12).
- r607: 0x3EA3C: skip `count` (inline word) instructions;
- r607: ASL 0x3 (0x3EA3C) debug block skip side effect: the debug text line word 0x7C7E4 (frame prefix raw_7c7e4) += 12 (appended ABI)

## 0x004 `load_local`

Handler `0x3E8F4`, extra words: 0.

- Later packed04/3E8F4 reads67;54/3EDB8 stores model pointer at actor+C8.

## 0x005 `push_script_word`

Handler `0x3E9F8`, extra words: 0.

- Build-159: 0x05 now pushes the CURRENT word through ScriptWordStoreService::kind(..., value) (a 0x42 store staged earlier in the same quantum included - 0x3E9F8 reads the self-modified image);
- r607 item 135: a word a 0x42 typed store wrote pushes back with that handle kind (0x3E9F8 copies the raw pointer).
- value = the CURRENT word (a store staged earlier in this quantum included: 0x3E9F8 reads the self-modified image).

## 0x006 `load_global`

Handler `0x3E880`, extra words: 0.

- Engine globals base = 0x7C8C8 (load_global 0x3E880).

## 0x007 `load_actor_field`

Handler `0x3DC60`, extra words: 0.

- op 0x07 selector 43 (0x3CCA8 -> 0x452CC) = 5DA54 sqrt of the 3D sum of ((actor - current waypoint) >> 6)^2 (5FD58), i.e.
- Static selector coverage (research aid): selector-coverage.cpp/.exe sweeps every scene WAD (same reachable walk as opcode-coverage, item 101) and prints "SEL op imm count level script word" for the field ops 0x07 0x0B 0x1C 0x1E 0x20 0x22 0x24 0x40 0x3C -> selector-coverage.txt;
- op 0x07 (0x3DC60) passes the executing actor as both s0 and s1, 45424 / 5FD58 are pure, so it is the flat squared distance of the actor to itself);
- ORACLE: full-src/r607-selector112-check.cpp (`bash run-one-check.sh r607-selector112-check`): 0x454CC pitch (158) vs native_selector_pitch158, and the original read dispatcher 0x3C8F0 (a0 = executing, a1 = read actor, a2 = selector, as ops 0x07 / 0x1C call it) for 110 (vs native_selector_cell_index110 on a random width / zone table), 78 (self -> 0), 15, 169 (= 1 from the executable image): 300,002
- Actual ASL op 0x07 selector 51 (read table 0x7681C -> 0x3CD78..0x3CD90): lw v0,0xE4(actor) primary pointer;
- op 0x07 (0x3DC60, a1 = a0) and op 0x1C (0x3E0AC, a1 = [0x78A1C]) make;

## 0x008 `reference_actor_local`

Handler `0x3E8D4`, extra words: 0.


## 0x009 `push_script_relative_reference`

Handler `0x3E9D8`, extra words: 0.

- 0x09 script-relative reference (0x3E9D8) and 0x00 (0x42754 empty), run by the ORIGINAL interpreter 0x36EC4 against the native VM.
- r607: 0x3E9D8 pushes actor cursor (already past this word) + 4*imm: a reference into the current script image.

## 0x00A `global_word_reference`

Handler `0x3E85C`, extra words: 0.


## 0x00B `owned_field_reference`

Handler `0x3DC84`, extra words: 0.


## 0x00C `register_trigger`

Handler `0x3B8B4`, extra words: 2.

- They are live only after ASL 0x0C register_trigger: continuation word = (register word + 2) + descriptor word 2 (signed, in words).
- startup prefix committed (original ASL 0x0C handler 0x3B8B4 applied to THIS
- ONCE by the accessor from the original ASL 0x0C handler's own instructions.
- r70 module pinned: 0x0C is EURO1.GAM 0x3B8B4 (dispatch word 0x6B82C),
- accessor derivation (original ASL 0x0C handler 0x3B8B4).
- through the ONE accessor derivation of the original ASL 0x0C handler

## 0x00D `disable_trigger_slot`

Handler `0x37C94`, extra words: 0.

- r607: ASL 0xD/0xE/0xF on the executing actor's trigger slot word (arena word locals+20+4*slot, the same binding QuantumTriggerStorage
- r607: low ASL opcodes dispatched through table 0x6B7FC (imm = high half): 0x0D/0x0E/0x0F trigger slot word (0x37C94/0x37CCC/0x37CA8),
- r607: ASL 0xD (0x37C94: type := 0), 0xE (0x37CCC: type |= 0x80000000), 0xF (0x37CA8: type &= 0x7FFFFFFF) on trigger slot `slot`
- r607: ASL 0xD/0xE/0xF (appended ABI)

## 0x00E `suspend_trigger_slot`

Handler `0x37CCC`, extra words: 0.

- r607: low ASL opcodes dispatched through table 0x6B7FC (imm = high half): 0x0D/0x0E/0x0F trigger slot word (0x37C94/0x37CCC/0x37CA8),
- r607: ASL 0xD (0x37C94: type := 0), 0xE (0x37CCC: type |= 0x80000000), 0xF (0x37CA8: type &= 0x7FFFFFFF) on trigger slot `slot`

## 0x00F `resume_trigger_slot`

Handler `0x37CA8`, extra words: 0.

- r607: low ASL opcodes dispatched through table 0x6B7FC (imm = high half): 0x0D/0x0E/0x0F trigger slot word (0x37C94/0x37CCC/0x37CA8),
- r607: ASL 0xD (0x37C94: type := 0), 0xE (0x37CCC: type |= 0x80000000), 0xF (0x37CA8: type &= 0x7FFFFFFF) on trigger slot `slot`

## 0x010 `call_yield`

Handler `0x3EF60`, extra words: 0.


## 0x011 `call`

Handler `0x3EF34`, extra words: 0.


## 0x012 `branch_zero_yield`

Handler `0x3F014`, extra words: 0.


## 0x013 `branch_nonzero_yield`

Handler `0x3F0C8`, extra words: 0.


## 0x014 `branch_zero`

Handler `0x3F058`, extra words: 0.


## 0x015 `branch_nonzero`

Handler `0x3F090`, extra words: 0.


## 0x016 `jump`

Handler `0x3EF94`, extra words: 0.


## 0x017 `switch_value_table`

Handler `0x3BE5C`, extra words: 0.


## 0x018 `load_parent_local`

Handler `0x3E960`, extra words: 0.

- r607: ASL 0x18 (0x3E960 push parent local), 0x3E (0x3EBCC pop into parent local) and 0x19 (0x3E98C parent local reference) run by
- r607: the parent actor's locals (parent = actor+D8, locals at parent+8): ASL 0x18 (0x3E960 read), 0x19 (0x3E98C reference),
- r607: ASL 0x18/0x19/0x3E (appended ABI)

## 0x019 `reference_parent_local`

Handler `0x3E98C`, extra words: 0.

- r607: ASL 0x18 (0x3E960 push parent local), 0x3E (0x3EBCC pop into parent local) and 0x19 (0x3E98C parent local reference) run by
- r607: the parent actor's locals (parent = actor+D8, locals at parent+8): ASL 0x18 (0x3E960 read), 0x19 (0x3E98C reference),

## 0x01A `parent_actor_field`

Handler `0x3DCC4`, extra words: 0.

- 24/3DE94 selects callerDC;1A/3DCC4 selects callerD8.

## 0x01C `read_bound_root_field`

Handler `0x3E0AC`, extra words: 0.

- op 0x07 (0x3DC60, a1 = a0) and op 0x1C (0x3E0AC, a1 = [0x78A1C]) make;

## 0x01D `reference_bound_root_field`

Handler `0x3E0D8`, extra words: 0.

- 0x1D (0x3E0D8 root-actor field reference, T1L2M007-9 / T1L9 only) stays unported.
- Item 182: op 0x1D (0x3E0D8) = reference to a ROOT actor field word (selectors 1..6, shared word 0x78A1C): ActorFieldWordService.root_reference (recovered_gameplay.h, native-actor-field-word.h).
- r607 item 182: ASL 0x1D (0x3E0D8 -> 3C560 on [0x78A1C]): the same pose-word borrow on the ROOT actor.
- r607 item 182: 0x3E0D8 pushes 3C560([0x78A1C], imm) = &root pose word (T1L2M007..
- r607 item 182: ASL 0x1D (0x3E0D8): &field of the ROOT actor [0x78A1C] (write table 0x3C560), selectors 1..6 (appended ABI)

## 0x01E `read_current_camera_direction`

Handler `0x3DDE4`, extra words: 0.

- M008 DOOR-48 ROOM SOLVED + DOOR 11 USED (route lib-wp-z26.txt, research tags dz18..dz26) + op 0x1E selectors 75..78.
- Barrier (frame 19431, record 93 = ActualDoor script 34 word 775): op 0x1E selector 75.
- 0x1E (0x3DDE4) = the 0x07 field reader 3C8F0 (table 0x76750) applied to the actor at [0x78A28];

## 0x01F `borrow_current_camera_pose_field`

Handler `0x3DE10`, extra words: 0.


## 0x020 `read_player_field`

Handler `0x3DF44`, extra words: 0.


## 0x022 `read_transient_actor_field`

Handler `0x3E15C`, extra words: 0.

- 22/3E15C reads via executing actor+E0, not shared ROOT/iterator/book.

## 0x024 `read_iterator_actor_field`

Handler `0x3DE94`, extra words: 0.

- 24/3DE94 selects callerDC;1A/3DCC4 selects callerD8.

## 0x025 `borrow_iterator_actor_field_word`

Handler `0x3DEBC`, extra words: 0.

- Item 187: 0x25 (3DEBC) selector 26 = word reference to the ITERATOR actor's +0xA4 (T1L3M005 s7 word 861, then 0x1DC and): QuantumActorFieldWords::reference accepts 26 (dirty 0x7BA68 at borrow, refuses the executing actor itself), encode_field maps 26 -> +0xA4, mutate/add keep the target's typed field_a4 in sync.
- r607 item 187: 0x25 (3DEBC) = 3C560 on the iterator actor (+0xDC);

## 0x028 `read_bound_book_actor_position`

Handler `0x3DFF8`, extra words: 0.

- ASL 0x28 selectors 75..78 (book actor distance: 452CC/453C4/4534C/45424).
- ITEM 130 (build-147): 0x28 selectors 163..166: 0x3DFF8 passes [0x78A2C] to 3C8F0 but bodies 0x3DA70..0x3DAAC read only save words +0x3E8..+0x3F4 -> same read as 0x07 163..166 (save_words.read).
- r607 item 130: 0x28 163..166: 0x3DFF8 passes [0x78A2C] to 3C8F0 but the 163..166 bodies (0x3DA70..0x3DAAC) never read it

## 0x029 `reference_bound_actor_pose_word`

Handler `0x3E024`, extra words: 0.

- Appended ABI:3E024/3C560 reference through current78A2C.

## 0x02A `property_9c_bit20`

Handler `0x398A8`, extra words: 0.


## 0x02B `jump_yield`

Handler `0x3EFA8`, extra words: 0.


## 0x02C `nop_2c`

Handler `0x380D4`, extra words: 0.


## 0x02D `nop_2d`

Handler `0x3AF64`, extra words: 0.


## 0x02E `property_9c_bit10000000`

Handler `0x3AF6C`, extra words: 0.

- 0x3AF6C: +9C |= 0x10000000

## 0x02F `property_a0_bit10000`

Handler `0x3AF9C`, extra words: 0.


## 0x031 `property_a0_bit2`

Handler `0x38598`, extra words: 0.

- Static script11+3158 /38598 enables the distinct actor+A0 bit2.

## 0x032 `property_9c_bit80000000`

Handler `0x3813C`, extra words: 0.

- 0x3813C: +9C |= 0x80000000

## 0x033 `property_a0_bit100`

Handler `0x380DC`, extra words: 0.

- 0x380DC: +A0 |= 0x100

## 0x034 `property_a0_bit200000`

Handler `0x3810C`, extra words: 0.

- 0x3810C: +A0 |= 0x200000

## 0x035 `nop_35`

Handler `0x398A0`, extra words: 0.


## 0x036 `nop_36`

Handler `0x39884`, extra words: 0.


## 0x037 `store_current_root_pose_word`

Handler `0x3E068`, extra words: 0.

- Real barriers already found: T1L3M005 post frame 1: ASL admission status 19 op 0x37 (store_current_root_pose_word) selector 26 at instruction 861;
- 37/3E068 stores a raw word through3C560 into current ROOT78A1C.

## 0x038 `store_current_camera_position`

Handler `0x3DDA0`, extra words: 0.


## 0x039 `store_player_pose_word`

Handler `0x3DF00`, extra words: 0.

- r607 item 175: 0x39 (3DF00) = 3C560 on the player actor [0x78A30] (C7 binding), raw sw of the popped word.
- r607 item 175: 3DF00, 3C560 selectors 1..6 on the player actor [0x78A30]
- r607 item 175: 39/3DF00 writes a raw word through 3C560 into the PLAYER actor [0x78A30] (as 37 does for ROOT) (appended ABI).

## 0x03A `store_iterator_pose_word`

Handler `0x3DE54`, extra words: 0.

- 0x3A (0x3DE54): exactly 0x37 but through the caller's iterator word +0xDC (QuantumActorReferences::iterator_store_position, read_caller_word;
- ITEM 158 (build-187/188): ASL 0x3A selectors 27 / 28.
- r607: the caller's own link word (0x3A/3DE54 reads caller+0xDC, the iterator actor written by store_cursor);
- 3A/3DE54 writes through3C560 into the caller's iterator actor (+0xDC), exactly as 37 does for ROOT.
- r607: ASL 0x3A (0x3DE54: pop, 3C560 through the caller's iterator actor word +0xDC, raw store) by the ORIGINAL handler vs the native
- 3A/3DE54 writes through3C560 into the caller's iterator actor (+0xDC), as 37 does for ROOT (appended ABI).

## 0x03B `store_current_bound_pose_word`

Handler `0x3DFB4`, extra words: 0.

- 3B/3DFB4 writes through the distinct shared bound actor78A2C.

## 0x03C `store_e0_actor_field`

Handler `0x3E11C`, extra words: 0.

- 0x3E11C: base = caller+0xE0 (pool word), then the write table 0x76490 selector 34..38 on THAT actor's current waypoint (+0x1C).
- 0x3E11C: *(3C560(caller+0xE0, selector)) = popped.
- ASL 0x3C selectors 34..38 (0x3E11C): the same waypoint word stores on the CURRENT waypoint of the actor at caller+0xE0 (appended ABI)

## 0x03E `store_parent_local`

Handler `0x3EBCC`, extra words: 0.

- r607: ASL 0x18 (0x3E960 push parent local), 0x3E (0x3EBCC pop into parent local) and 0x19 (0x3E98C parent local reference) run by
- 0x3E (0x3EBCC write).

## 0x040 `store_actor_field`

Handler `0x3EC38`, extra words: 0.

- ASL op 0x40 selectors 36..38
- staged waypoint word patches (op 0x40 selectors 36..38), scene byte offset -> raw word
- ASL 0xE9 (0x38504): copy pose words +0x24..+0x43 from the actor pointed to by the caller's +0xD8 (written by ASL 0x40/130).
- ASL 0x40/111 (0x3C6A8 -> save image +0x560), appended ABI
- op 0x40 selectors 36..38 (current waypoint +0x10/+0x14/+0x18), appended (ABI)
- ASL 0x40/130 (write table 0x76490[129] -> actor+0xD8), appended ABI

## 0x041 `store_local`

Handler `0x3EC80`, extra words: 0.

- packed41/3EC80 stores local67.

## 0x042 `store_script_relative_word`

Handler `0x3ECA4`, extra words: 0.

- ASL 0x42 script stores now also update every VM state copy of that script (shared original script image;
- 0x42 (0x3ECA4, raw sw) of a 0x18E particle template or a 0x1AD word buffer handle (M004 script 31 init: templates -> words 243..252, buffers -> 253..257) keeps the handle kind: LevelScriptRecord::word_kinds (byte ValueKind + origin, absent = Integer) on the shared actor_source script image, staged per quantum (scriptKinds) and committed with the words;
- ITEM 162 (build-197): ASL 0x42 of an ActorReference (origin 129) = 0x3ECA4 raw pointer store.
- r607 item 135: an ASL 0x42 store of a typed handle (gameplay::ValueKind as byte, origin) into a script word;
- ASL 0x42 stores into the executing actor's (shared) script image
- r607: an ASL 0x42 store lands in the ONE shared script image (source), so every actor VM copy of that script sees it too.

## 0x043 `store_global`

Handler `0x3ECC8`, extra words: 0.


## 0x044 `push_signed16`

Handler `0x3E7D4`, extra words: 0.

- pushes its signed high half unchanged (36F50/3E7D4).

## 0x045 `push32`

Handler `0x3E7B0`, extra words: 1.


## 0x046 `negate_wrapping`

Handler `0x3C434`, extra words: 0.


## 0x047 `increment_owned_word_q12`

Handler `0x3EB74`, extra words: 0.

- (a) 0x47 / 0x48 on a 0x09 reference (cursor + 4*imm) into the EXECUTING script image = self-modifying counter (0x3EB74 / 0x3EBA0), through script_word_store42 + new read (same-quantum staged stores first).
- 0x47/0x48 on it (0x3EB74/0x3EBA0 lw/addiu/sw at the raw word)
- r607 item 120: source 0x3EB74 / 0x3EBA0: lw (ref);

## 0x048 `decrement_owned_word_q12`

Handler `0x3EBA0`, extra words: 0.

- (a) 0x47 / 0x48 on a 0x09 reference (cursor + 4*imm) into the EXECUTING script image = self-modifying counter (0x3EB74 / 0x3EBA0), through script_word_store42 + new read (same-quantum staged stores first).
- ITEM 169 (native-save-decrement.h): 0x48 on save +0x3D8 (0x0B/114, house points) = 3EBA0 lw/addiu -4096/sw (T1L2M001 s64 HousePointDeductor word 26, "late for Herbology").
- 0x47/0x48 on it (0x3EB74/0x3EBA0 lw/addiu/sw at the raw word)
- Opcode48/3EBA0 on the canonical address issued for field156 (primary+3E4).
- r607 item 169: + 0x3D8 (0x0B selector 114 = 0x827F8, house points): T1L2M001 PointDeductor (script 64 word 26) 0x48 = 3EBA0 lw/addiu -4096/sw.
- r607 item 120: source 0x3EB74 / 0x3EBA0: lw (ref);

## 0x049 `add_wrapping`

Handler `0x55D44`, extra words: 0.


## 0x04A `subtract_wrapping`

Handler `0x55D6C`, extra words: 0.


## 0x04B `multiply_q12`

Handler `0x55E04`, extra words: 0.


## 0x04C `divide_q12_wrapped_shifts`

Handler `0x3E1C8`, extra words: 0.

- Opcode4C/3E1C8 intentionally shifts8 BEFORE signed division and4 after.

## 0x04E `equal`

Handler `0x55DB4`, extra words: 0.


## 0x04F `signed_less`

Handler `0x3ED88`, extra words: 0.


## 0x050 `shift_left_q12`

Handler `0x3B824`, extra words: 0.


## 0x051 `shift_right_q12`

Handler `0x3B858`, extra words: 0.


## 0x052 `seek_base_animation_frame`

Handler `0x3B738`, extra words: 0.

- 3B738..3B7F4: no per-frame22B28 call only when vertex stream is absent,

## 0x053 `signed_greater`

Handler `0x3ECF0`, extra words: 0.


## 0x054 `bind_model_reference`

Handler `0x3EDB8`, extra words: 0.

- Later packed04/3E8F4 reads67;54/3EDB8 stores model pointer at actor+C8.

## 0x055 `store_actor_scale_halves`

Handler `0x3BDE0`, extra words: 0.

- Source 0x3BDE0: the popped word's low half is stored to all three scale halfwords actor+0xD0/0xD2/0xD4.

## 0x056 `store_actor_scale_x`

Handler `0x3BE08`, extra words: 0.

- Sources 0x3BE08/0x3BE24/0x3BE40: the popped word's low half is stored to ONE scale halfword actor+0xD0/0xD2/0xD4.

## 0x057 `store_actor_scale_y`

Handler `0x3BE24`, extra words: 0.

- Sources 0x3BE08/0x3BE24/0x3BE40: the popped word's low half is stored to ONE scale halfword actor+0xD0/0xD2/0xD4.

## 0x058 `store_actor_scale_z`

Handler `0x3BE40`, extra words: 0.

- Sources 0x3BE08/0x3BE24/0x3BE40: the popped word's low half is stored to ONE scale halfword actor+0xD0/0xD2/0xD4.

## 0x059 `store_actor_physical_word14c`

Handler `0x39834`, extra words: 0.


## 0x05A `store_actor_physical_half150`

Handler `0x39850`, extra words: 0.

- Original39834 SW actor14C,39850 LHU/SH actor150 and37858 LHU/SH rate140.

## 0x05D `move_up_facing_3d`

Handler `0x3C4B4`, extra words: 0.

- ASL 0x5D/0x5E (0x3C4B4/0x3C51C, move by (0,±v,0) in the actor frame via 0x3BFF0).
- r607: ASL ops 0x5D/0x5E (vertical move in the actor's own frame) and 0x5F..0x62 (until now unchecked) against the ORIGINAL
- handlers 0x3C4B4/0x3C51C/0x3C074/0x3C0B4/0x3C24C/0x3C28C (all through 0x3BFF0 = matrix 13E0C + ApplyMatrixLV 5DBA4).
- 0x3C074 (0,0,v), 0x3C0B4 (0,0,-v), 0x3C24C (v,0,0), 0x3C28C (-v,0,0), r607: 0x3C4B4 (0,v,0), 0x3C51C (0,-v,0): the popped vector

## 0x05E `move_down_facing_3d`

Handler `0x3C51C`, extra words: 0.

- ASL 0x5D/0x5E (0x3C4B4/0x3C51C, move by (0,±v,0) in the actor frame via 0x3BFF0).
- handlers 0x3C4B4/0x3C51C/0x3C074/0x3C0B4/0x3C24C/0x3C28C (all through 0x3BFF0 = matrix 13E0C + ApplyMatrixLV 5DBA4).
- 0x3C074 (0,0,v), 0x3C0B4 (0,0,-v), 0x3C24C (v,0,0), 0x3C28C (-v,0,0), r607: 0x3C4B4 (0,v,0), 0x3C51C (0,-v,0): the popped vector

## 0x05F `move_along_facing_3d`

Handler `0x3C074`, extra words: 0.

- handlers 0x3C4B4/0x3C51C/0x3C074/0x3C0B4/0x3C24C/0x3C28C (all through 0x3BFF0 = matrix 13E0C + ApplyMatrixLV 5DBA4).
- 0x3C074 (0,0,v), 0x3C0B4 (0,0,-v), 0x3C24C (v,0,0), 0x3C28C (-v,0,0), r607: 0x3C4B4 (0,v,0), 0x3C51C (0,-v,0): the popped vector
- ASL 0x5F (0x3C074 -> 0x3BFF0): move the actor along a vector rotated by its own 3D angles.

## 0x060 `move_backward_facing_3d`

Handler `0x3C0B4`, extra words: 0.

- handlers 0x3C4B4/0x3C51C/0x3C074/0x3C0B4/0x3C24C/0x3C28C (all through 0x3BFF0 = matrix 13E0C + ApplyMatrixLV 5DBA4).
- 0x3C074 (0,0,v), 0x3C0B4 (0,0,-v), 0x3C24C (v,0,0), 0x3C28C (-v,0,0), r607: 0x3C4B4 (0,v,0), 0x3C51C (0,-v,0): the popped vector

## 0x061 `move_sideways_3d`

Handler `0x3C24C`, extra words: 0.

- handlers 0x3C4B4/0x3C51C/0x3C074/0x3C0B4/0x3C24C/0x3C28C (all through 0x3BFF0 = matrix 13E0C + ApplyMatrixLV 5DBA4).
- 0x3C074 (0,0,v), 0x3C0B4 (0,0,-v), 0x3C24C (v,0,0), 0x3C28C (-v,0,0), r607: 0x3C4B4 (0,v,0), 0x3C51C (0,-v,0): the popped vector

## 0x062 `move_sideways_negative_3d`

Handler `0x3C28C`, extra words: 0.

- handlers 0x3C4B4/0x3C51C/0x3C074/0x3C0B4/0x3C24C/0x3C28C (all through 0x3BFF0 = matrix 13E0C + ApplyMatrixLV 5DBA4).
- 0x3C074 (0,0,v), 0x3C0B4 (0,0,-v), 0x3C24C (v,0,0), 0x3C28C (-v,0,0), r607: 0x3C4B4 (0,v,0), 0x3C51C (0,-v,0): the popped vector

## 0x063 `sub_actor_yaw_masked24`

Handler `0x3EE84`, extra words: 0.

- 0x3EE84/0x3EEB0 (+0x28), 0x39A20/0x39A4C (+0x2C), 0x3EEDC/0x3EF08 (+0x24): word = (word -/+ popped) & 0xFFFFFF.

## 0x064 `add_actor_yaw_masked24`

Handler `0x3EEB0`, extra words: 0.

- 0x3EE84/0x3EEB0 (+0x28), 0x39A20/0x39A4C (+0x2C), 0x3EEDC/0x3EF08 (+0x24): word = (word -/+ popped) & 0xFFFFFF.

## 0x065 `sub_actor_roll_masked24`

Handler `0x39A20`, extra words: 0.

- 0x3EE84/0x3EEB0 (+0x28), 0x39A20/0x39A4C (+0x2C), 0x3EEDC/0x3EF08 (+0x24): word = (word -/+ popped) & 0xFFFFFF.

## 0x066 `add_actor_roll_masked24`

Handler `0x39A4C`, extra words: 0.

- 0x3EE84/0x3EEB0 (+0x28), 0x39A20/0x39A4C (+0x2C), 0x3EEDC/0x3EF08 (+0x24): word = (word -/+ popped) & 0xFFFFFF.

## 0x067 `add_actor_angle24_masked`

Handler `0x3EEDC`, extra words: 0.

- 0x3EE84/0x3EEB0 (+0x28), 0x39A20/0x39A4C (+0x2C), 0x3EEDC/0x3EF08 (+0x24): word = (word -/+ popped) & 0xFFFFFF.

## 0x068 `sub_actor_angle24_masked`

Handler `0x3EF08`, extra words: 0.

- 0x3EE84/0x3EEB0 (+0x28), 0x39A20/0x39A4C (+0x2C), 0x3EEDC/0x3EF08 (+0x24): word = (word -/+ popped) & 0xFFFFFF.

## 0x069 `turn_pitch_toward_root`

Handler `0x3A180`, extra words: 0.

- Ported: 0x1D2 (0x41388 primary rate, PrimaryRate1D2 call kind), 0x1D0 (0x41334: 9C &= ~0x4000), 0x166 (0x3FDD8 base frame seek: frame = v >> 12, 0 when >= total, +13C / +140, flags |= 8), 0x69 (0x3A180 pitch toward root), 0xC3 (0x39740 timer max via set_process_timer_c3), 0x97 (0x385C8 drop two), 0xD8 (0x55EFC sign q12), 0x107 (0x52DB4 literal prompt, as 0xF2 with the 0x167 prompt misc words).
- r607 item 101: 0x3A180 = the pitch half of 0x6B (45548(root+0x34, actor+0x34), only +0x24 turns);

## 0x06A `turn_yaw_toward_root`

Handler `0x3A3AC`, extra words: 0.

- Item 207: 0x1C / 0x6A / 0x6B root position readers (3C8F0 with s0 = [0x78A1C], 3A3AC / 3A258 4547C(root+0x34)) never test the root for NULL.
- r607 item 207: the original 0x1C/0x6A/0x6B readers (3C8F0 with s0 = [0x78A1C], 3A3AC/3A258 4547C(root+0x34)) never test the root
- branches 0x12/0x13/0x14/0x15, rotation add/sub 0x63..0x68, script-relative store 0x42, turn ops 0x6A/0x6C/0x6D and the map piece swap 0x10F
- 0x3A3AC: like 0x6D toward the ROOT actor's +0x34/+0x3C (4547C(root+0x34, actor+0x34));

## 0x06B `turn_yaw_and_pitch_toward_root`

Handler `0x3A258`, extra words: 0.

- 0x6B (0x3A258 = 0x6E toward the ROOT actor): r607-op6b-check 10,000/0.
- Item 207: 0x1C / 0x6A / 0x6B root position readers (3C8F0 with s0 = [0x78A1C], 3A3AC / 3A258 4547C(root+0x34)) never test the root for NULL.
- r607 item 207: the original 0x1C/0x6A/0x6B readers (3C8F0 with s0 = [0x78A1C], 3A3AC/3A258 4547C(root+0x34)) never test the root
- r607: ASL 0x6B (0x3A258 turn yaw AND pitch toward the ROOT actor via 0x45548) run by the ORIGINAL interpreter 0x36EC4 against the native VM.
- r607: 0x3A258 = 0x6E toward the ROOT actor (45548(root+0x34, actor+0x34));
- 0x6B (0x3A258) takes the point from the ROOT actor's position and pops only the step.

## 0x06C `turn_pitch_toward_point`

Handler `0x39B14`, extra words: 0.

- 0x39B14 / 0x39C1C: pop step (top), then the point (x,y,z);

## 0x06D `turn_yaw_toward_point`

Handler `0x39C1C`, extra words: 0.

- 0x39B14 / 0x39C1C: pop step (top), then the point (x,y,z);

## 0x06E `turn_yaw_and_pitch_toward_point`

Handler `0x39D20`, extra words: 0.

- 0x6E (0x39D20 yaw AND pitch toward a point, 0x45548): r607-op6e-check 10,000/0 (original interpreter).
- r607: ASL 0x6E (0x39D20 turn yaw AND pitch toward a point via 0x45548) run by the ORIGINAL interpreter 0x36EC4 against the native VM.
- r607: 0x39D20: pop step (top) then the point (x,y,z);

## 0x070 `restore_backup_pose`

Handler `0x3B658`, extra words: 0.

- 0x3B658 only touches +0x24..+0x98: inside both the normal (364-byte) and the special (200-byte) record.

## 0x071 `copy_current_pose_to_backup`

Handler `0x3B624`, extra words: 0.

- 3B624 copies six fields, no padding
- 0x3B624 only touches +0x24..+0x98, inside both the normal (364-byte) and the special (200-byte) actor record.

## 0x072 `copy_link_field`

Handler `0x39A90`, extra words: 0.


## 0x073 `link_field_to_last_waypoint`

Handler `0x3A5D0`, extra words: 0.

- 0x73 (0x3A5D0: +1C := +18 last waypoint): to_last service, r607-op73-check 10,000/0.
- Item 195: ASL 0x73 (0x3A5D0: +1C := +18) and the reverse waypoint step read +0x18 of a SPECIAL actor too (read_native_actor_last_waypoint18: normal 364 or special 200 pool, common header) (T1L7M002 / T1L7M003 special word 217).
- r607 item 195: actor +0x18 (last waypoint) of a NORMAL (364) or SPECIAL (200) pool actor: 0x3A5D0 (ASL 0x73) and the reverse
- r607: source 0x3A5D0 (ASL 0x73): actor+1C := actor+18.
- r607: ASL 0x73 (0x3A5D0: actor+1C := actor+18) through the native VM tick against the ORIGINAL handler.
- r607: op 0x73 (source 0x3A5D0): actor+1C := actor+18 (last waypoint), appended (ABI)

## 0x074 `loop_next_waypoint`

Handler `0x3A5DC`, extra words: 0.

- r607: the caller may be a normal OR special actor (0x3A5DC only touches actor+1C and scene waypoint records).

## 0x075 `loop_previous_waypoint`

Handler `0x3AD88`, extra words: 0.

- 75/3AD88, previous+4 or actor18(last)

## 0x078 `link_field_to_nearest_waypoint`

Handler `0x3ABA8`, extra words: 0.

- 0x78 (0x3ABA8 nearest waypoint of the +14 chain, unsigned strict min) + 0xFE (0x374D8 empty handler): r607-op78-check 20,001/0.
- r607: source 0x3ABA8 (ASL 0x78): walk actor+14 through NULL;
- r607: ASL 0x78 (0x3ABA8: actor+1C := nearest waypoint of the +14 chain) — native nearest_native_waypoint over a synthetic scene
- r607: ASL 0x78 (0x3ABA8): actor+1C := the waypoint of the +14 chain nearest to the actor (4534C, UNSIGNED strict minimum) (appended ABI)

## 0x07A `turn_pitch_toward_current_waypoint`

Handler `0x39FFC`, extra words: 0.

- 0x1A5 (0x4F4D0 template emitter from the actor position with a script vector, core 0x4E248) and 0x7A (0x39FFC pitch toward the current waypoint, = 0x6C with the +1C waypoint point): r607-op7a-check 10,001/0.
- r607: ASL 0x7A (0x39FFC turn PITCH toward the current waypoint +0x10 via 0x454CC) run by the ORIGINAL interpreter 0x36EC4 against the native VM;
- r607: 0x39FFC = 0x6C toward the CURRENT waypoint (454CC(link+0x10, actor+0x34));

## 0x07B `turn_yaw_to_waypoint`

Handler `0x3A0C0`, extra words: 0.

- 7B/3A0C0 turns yaw via4547C.

## 0x07C `turn_toward_current_waypoint`

Handler `0x39EAC`, extra words: 0.

- 7C/39EAC also turns pitch via45548;

## 0x07D `bind_base_animation`

Handler `0x3BF78`, extra words: 0.

- 7D/3BF78 only replaces the base clock.

## 0x07E `stop_base_animation_play_flag`

Handler `0x3B094`, extra words: 0.


## 0x07F `clear_base_animation`

Handler `0x3B0A8`, extra words: 0.

- r607: ASL 0x7F (0x3B0A8): the base clip word +138 becomes 0 and 9C loses bit 8 (common writeback publishes the typed flags).
- r607: ASL 0x8B (0x3BA2C 9C |= 0x12), 0xA6 (0x3BA60 9C &= 0xFFFB5FFF) and 0x7F (0x3B0A8 +138 := 0, 9C &= ~8) run by the ORIGINAL
- r607: ASL 0x7F (0x3B0A8): +138 := 0 and 9C &= ~8 (appended ABI)

## 0x081 `set_actor_a0_mode`

Handler `0x3BAA0`, extra words: 0.

- r607: ASL 0x81 (0x3BAA0 A0 mode) for ALL modes through the native VM tick against the ORIGINAL handler, including the
- 0x3BAA0: +A0 &= ~0x42C, then 1->|8, 2->|0x400, 3->|0x20, 4->nothing;
- r607: the progress dirty word 0x7BA68 := 1 (ASL 0x81 modes outside 1..4);
- r607: ASL 0x81 other modes (appended ABI)

## 0x082 `store_actor_halfword122_and_dirty`

Handler `0x398D8`, extra words: 0.


## 0x086 `save_primary_to_backup`

Handler `0x42030`, extra words: 0.

- 42030 copies 82420..
- 86 ->42030, data effect;

## 0x088 `mark_actor_flag40`

Handler `0x394A0`, extra words: 0.


## 0x089 `clear_actor_flags_40_and_4000000`

Handler `0x39480`, extra words: 0.

- 0x39480: 9C &= ~0x40 & 0xFBFFFFFF

## 0x08A `wait_q12`

Handler `0x3B7F8`, extra words: 0.


## 0x08B `disable_script_and_yield`

Handler `0x3BA2C`, extra words: 0.

- r607: ASL 0x8B (0x3BA2C 9C |= 0x12), 0xA6 (0x3BA60 9C &= 0xFFFB5FFF) and 0x7F (0x3B0A8 +138 := 0, 9C &= ~8) run by the ORIGINAL
- r607: 0x3BA2C: bit 0x10 disables the script (0x36F00) from the next frame;

## 0x08D `stop`

Handler `0x3E788`, extra words: 0.


## 0x093 `spawn_actor_at_list_head`

Handler `0x3E2AC`, extra words: 5.

- 0x93 / 0x1E8 (3E2AC / 3E380): the D9 spawn with record flag +0x14 = 0 / 2.
- r607: the spawn opcode and the constructor record flag +0x14 it passes (0x3E2AC/0x93: 0 = insert at the list head;
- r607: ASL 0x93 / 0x1E8 (3E2AC / 3E380 = the D9 spawn with constructor record flag +0x14 = 0 / 2): the list insertion of 346B0
- Wrappers: 3E2AC stores half 0, 3E314 half 1, 3E380 half 2 at sp+44 (= record+0x14);
- r607: 0x93 / 0x1E8 (3E2AC / 3E380) are the same spawn with record flag 0 / 2 (list head / tail);

## 0x097 `discard_two`

Handler `0x385C8`, extra words: 0.

- Ported: 0x1D2 (0x41388 primary rate, PrimaryRate1D2 call kind), 0x1D0 (0x41334: 9C &= ~0x4000), 0x166 (0x3FDD8 base frame seek: frame = v >> 12, 0 when >= total, +13C / +140, flags |= 8), 0x69 (0x3A180 pitch toward root), 0xC3 (0x39740 timer max via set_process_timer_c3), 0x97 (0x385C8 drop two), 0xD8 (0x55EFC sign q12), 0x107 (0x52DB4 literal prompt, as 0xF2 with the 0x167 prompt misc words).
- r607 item 101: self-field oracle + the 0x1D0 (41334), 0x97 (385C8), 0xD8 (55EFC) handlers.
- r607 item 101: ASL 0x1D0 (41334, 9C &= ~0x4000), 0x97 (385C8, drop two words), 0xD8 (55EFC, sign as q12) through the full
- r607 item 101: 0x385C8 drops two words, nothing else

## 0x098 `stop_actor_sound_channel`

Handler `0x3873C`, extra words: 0.

- ASL 0x98 (0x3873C): pops a channel;
- descriptor), ASL 0x98 at once.
- Opcode 0x98 (source 0x3873C): pops one channel word;
- ASL 0x98 (appended ABI)

## 0x099 `start_actor_sound`

Handler `0x38ED8`, extra words: 0.

- ASL 0x99 with an existing actor sound group (+BC != 0): 0x3879C/0x4CD3C path (channel -1 -> 0x4B2BC on the live group, B8 |= 1<<channel, result = channel).
- ASL 0x99 (38ED8 -> 3879C -> 4CD3C(2,...)) starts them;
- Item 210: 0x99 (38ED8 -> 3879C) on a SPECIAL actor: the sound request reads +AF/+B4/+B8/+BC/+C0/+C1 in the special pool;
- Source 0x38ED8 (ASL opcode 0x99): pop raw sound id, skip to result -1 when
- Actor effects of 0x3879C/0x38ED8 in the staged pool: AF=2, BC=group, B8|=1<<channel on success.
- 0x38ED8 then sets +B8 |= 1 << channel.

## 0x09A `start_actor_sound_manager1_no_result`

Handler `0x39120`, extra words: 0.

- ITEM 129 (build-146): ASL 0x9A (table 0x6AFD8 -> 0x39120) = 0x9D (0x391C4) WITHOUT the result push: pop id;
- r607 item 129: 0x39120 = 0x391C4 (0x9D) without the result push: pop the id;

## 0x09D `start_actor_sound_manager1`

Handler `0x391C4`, extra words: 0.

- ITEM 129 (build-146): ASL 0x9A (table 0x6AFD8 -> 0x39120) = 0x9D (0x391C4) WITHOUT the result push: pop id;
- Audio manager of the request (3879C arg a1 -> actor AF): 0 for ASL 0xD0/0xDD (0x389EC), 1 for ASL 0x9D (0x391C4, bank 4 = a2).
- ASL 0x9D (0x391C4) shape: -1 skips (mode 6 or id -1, pushed -1);
- ASL 0x9D (manager 1): a scene-WAD (bank 4) descriptor, decoded like speech;
- 0x391C4: same as 0x99 but on audio manager 1 (a1=1);
- r607 item 129: 0x39120 = 0x391C4 (0x9D) without the result push: pop the id;

## 0x0A4 `or_actor_flags_immediate`

Handler `0x3BA40`, extra words: 1.

- 3BA40,3BB84,3C67C,3C670.

## 0x0A5 `clear_actor_flags_immediate`

Handler `0x3BA78`, extra words: 1.


## 0x0A6 `clear_actor_flags_4a000`

Handler `0x3BA60`, extra words: 0.

- r607: ASL 0x8B (0x3BA2C 9C |= 0x12), 0xA6 (0x3BA60 9C &= 0xFFFB5FFF) and 0x7F (0x3B0A8 +138 := 0, 9C &= ~8) run by the ORIGINAL
- r607: 0x3BA60

## 0x0A7 `start_actor_sound_front_end_pitch`

Handler `0x38D08`, extra words: 0.

- ASL 0xA7 (0x38D08): the D0 request with the volume AND a pitch word taken from the script (3879C arg6, added to C1<<6, clamped).
- 0x38D08: id, volume word (>>12 logical), pitch word (top);
- Opcode 0xA7 (source 0x38D08): pops pitch word (top), volume word (>>12 logical) and sound id;
- ASL 0xA7 (appended ABI)

## 0x0AB `clear_low_q12`

Handler `0x55E5C`, extra words: 0.


## 0x0AC `source_table_sine`

Handler `0x397BC`, extra words: 0.


## 0x0AD `source_table_cosine`

Handler `0x397F4`, extra words: 0.

- Exact397BC/397F4 index bits: source SRA/mask, cosine phase+1024.

## 0x0AE `logical_not`

Handler `0x55E40`, extra words: 0.

- r607: 0xAE (55E40 sltiu 1) on a scene reference: 0xB1 (3E810) pushes scene base 0x7B528 + operand, a non-NULL address -> 0

## 0x0B1 `push_scene_offset`

Handler `0x3E810`, extra words: 1.

- B1/3E810 resolves a DPSX reference;
- TYPED ABSENCE, measured: ASL 0xB1 (handler0x3E810;
- only relaxed word is the operand after ASL0xB1, which 0x3E810 rewrites to
- only the word that follows a 0xB1 is scene-relative, because 0x3E810 rewrites
- ASL 0xB1 (handler0x3E810;
- (B1 0x3E810 pushes base + offset, 0x7D / 0x1ED store it as is).

## 0x0B2 `return`

Handler `0x3EA20`, extra words: 0.


## 0x0B3 `stop`

Handler `0x3E79C`, extra words: 0.


## 0x0B4 `bind_current_root`

Handler `0x3BF60`, extra words: 0.


## 0x0B5 `logical_and`

Handler `0x55EA4`, extra words: 0.


## 0x0B6 `bit_or`

Handler `0x55E7C`, extra words: 0.

- r607 item 134: 0xB6 (55E7C, raw OR) of an Integer and an ActorReference whose ONLY consumer is the next instruction, a

## 0x0B7 `bit_and`

Handler `0x55ED4`, extra words: 0.


## 0x0BA `not_equal`

Handler `0x55DDC`, extra words: 0.


## 0x0BB `signed_greater_equal`

Handler `0x3ED54`, extra words: 0.


## 0x0BC `signed_less_equal`

Handler `0x3ED20`, extra words: 0.


## 0x0BD `random_range`

Handler `0x3B328`, extra words: 0.


## 0x0BE `save_word_560_step`

Handler `0x3ADE0`, extra words: 0.

- ASL 0xBE with save word 0x560 == 0 now stages 0x78ADC := 2 (QuantumLivesStepBE.game_over, committed with the quantum into transition_globals) instead of refusing.
- Door 53 (206848, 34816 -> door 48 at 47104, 16384, 108544) did NOT open with presses (z15 / z16) and the patrol actor 57 (script 23, wp152..157, passes the door spot) knocks Harry out: global 55 -> script 25 words 4973..4994 (anim 4CB28, 60-frame wait, ASL 0xBE).
- DEATH FLOW (open, same as the ck-l2herb issue): s2 4973..4997: global 55 (health <= 0) -> anim 350E0, 60-tick wait (L46), ASL 0xBE (0x3ADE0: lives word 0x82980 -= 4096, or 0x78ADC := 2 = game over when 0), then an endless loop that calls 247 (camera;
- field 111 = HEALTH, and 0xBE (0x3ADE0) tests the SAME word.
- LAVA MECHANICS (s17 word 751, original): floor surface (actor field 48) == 0xA000 (10) -> G87 |= 0x800 (no spells) and, when g83 == 0 && !g60 && !(g4|g12) && health > 0: ASL 0xBE (health -= 4096), burnt-hop animation 213CC, g83 := 0x40000 (cooldown);
- Request: ASL 0xBE (3ADE0) with save word 0x560 == 0 sets 0x78ADC := 2;

## 0x0C0 `query_actor_floor_c0`

Handler `0x39934`, extra words: 0.

- Differential check: native plan_native_floor_contacts (static + dynamic contact groups merged for the caller 0x39934) against
- Full merge of 0x42CC8 (after the static 0x434D0 and dynamic 0x43A78 queries) for the caller 0x39934 (+9C bit 0x40000 cleared):

## 0x0C2 `set_process_effect_words`

Handler `0x3977C`, extra words: 0.

- Writers: script opcodes 3973C (78E0C := max(78E0C, arg >> 12), small-motor timer) and 3977C (78DF8 := arg1 >> 12, 78DFC := arg2 >> 12), the actor tail 35EDC (78E0C capped 90 and counted down;
- Gameplay script rumble (3973C / 3977C) and the Select+Start reset not exercised live (no scene trigger in the probe;
- The game's motor words (script opcodes 3977C / 3973C, actor-tail decay, pause options) drive the first connected pad.

## 0x0C3 `rumble_timer_max`

Handler `0x39740`, extra words: 0.

- Ported: 0x1D2 (0x41388 primary rate, PrimaryRate1D2 call kind), 0x1D0 (0x41334: 9C &= ~0x4000), 0x166 (0x3FDD8 base frame seek: frame = v >> 12, 0 when >= total, +13C / +140, flags |= 8), 0x69 (0x3A180 pitch toward root), 0xC3 (0x39740 timer max via set_process_timer_c3), 0x97 (0x385C8 drop two), 0xD8 (0x55EFC sign q12), 0x107 (0x52DB4 literal prompt, as 0xF2 with the 0x167 prompt misc words).
- r607 item 101: ASL 0xC3 (0x39740): n = pop >> 12 (logical);
- r607 item 101: ASL 0xC3 (0x39740) rumble timer max (appended ABI)

## 0x0C4 `set_collision_sphere_radius`

Handler `0x3960C`, extra words: 0.

- 0xC4 (0x3960C collision sphere radius set/append in +118 table, count +116;
- Item 193: ASL 0xC4 collision sphere on a D9-born actor: locals / triggers / capacity from its 3E230 descriptor, storage from the birth binding (NativeDynamicActorMembershipAccess::collision_capacity) (T1L4M005 record 40, T1L4M006 record 35).
- r607: source 0x3960C (ASL 0xC4).
- (the actor's +0x118 collision table entries written by ASL 0xC4).
- r607: ASL 0xC4 (0x3960C) on the executing NORMAL static actor: +0x118 must be bound to its own allocation word
- r607: ASL 0xC4 (0x3960C collision sphere table set/append) — native plan_native_collision_c4 against the ORIGINAL handler over a

## 0x0C5 `update_animation_group_world_point`

Handler `0x394B4`, extra words: 0.

- 394B4 compressed-key lane with source5396C supplemental translations.
- bone: the 0x5396C local point of bone/group `bone` for the actor at `slot` (the same sampler as ASL 0xC5);
- r607: the 0x5396C bone point for the pair sphere, through the same sampler/context route as ASL 0xC5.

## 0x0C6 `bind_current_camera`

Handler `0x3BF08`, extra words: 0.


## 0x0C7 `bind_current_player`

Handler `0x3BEF0`, extra words: 0.


## 0x0CC `save_word560_saturating_increment`

Handler `0x3AE9C`, extra words: 0.

- ASL 0xCC (0x3AE9C: lives save word 0x560 saturating +0x1000): r607-opcc-check 10,000/0.
- r607: ASL 0xCC (0x3AE9C: saturating +0x1000 on save word 0x82980 = save +0x560) through the native VM against the ORIGINAL handler.
- r607: 0x3AE9C: save word 0x82980 (= save base + 0x560, the lives counter read by selector 111):

## 0x0CF `debug_header`

Handler `0x3F10C`, extra words: 2.


## 0x0D0 `start_actor_sound_front_end`

Handler `0x389EC`, extra words: 0.

- SOUND EFFECTS: NATIVE PLAYBACK OF THE ASL 0xD0 FAMILY (2026-11-01, NATIVE PC POLICY, backend only).
- committed ASL 0xD0 requests
- NATIVE POLICY: an actor whose BC is unknown because ASL 0xD0 started a manager-0 sound keeps AF=0, B8 bit 0 and
- Source 0x389EC (ASL opcode 0xD0): pop sound id, skip when mode word 0x775F8==6, else 0x3879C(actor, manager 0,
- Audio manager of the request (3879C arg a1 -> actor AF): 0 for ASL 0xD0/0xDD (0x389EC), 1 for ASL 0x9D (0x391C4, bank 4 = a2).
- NATIVE POLICY queue of ASL 0xD0/0xA7/0x9D requests (see native-actor-sound-start99.h).

## 0x0D1 `start_actor_sound_front_end_result`

Handler `0x38924`, extra words: 0.

- Barrier 1 (frame 5906): ASL 0xD1 (DE path, manager 0) on actor record 57 whose group was created by the 0xD0 policy (AF 0, BC deliberately unknown) -> "Sound request consumed actor fields u...".

## 0x0D2 `push32_alt`

Handler `0x3E7EC`, extra words: 1.


## 0x0D3 `store_actor_halfwords_11c`

Handler `0x38554`, extra words: 0.


## 0x0D4 `absolute_wrapping`

Handler `0x3C45C`, extra words: 0.


## 0x0D6 `signed_minimum`

Handler `0x37FF4`, extra words: 0.

- 0x37FF4: blt top,second -> top else second (pair of 0xD7)

## 0x0D7 `signed_maximum`

Handler `0x37FAC`, extra words: 0.


## 0x0D8 `sign_q12`

Handler `0x55EFC`, extra words: 0.

- Ported: 0x1D2 (0x41388 primary rate, PrimaryRate1D2 call kind), 0x1D0 (0x41334: 9C &= ~0x4000), 0x166 (0x3FDD8 base frame seek: frame = v >> 12, 0 when >= total, +13C / +140, flags |= 8), 0x69 (0x3A180 pitch toward root), 0xC3 (0x39740 timer max via set_process_timer_c3), 0x97 (0x385C8 drop two), 0xD8 (0x55EFC sign q12), 0x107 (0x52DB4 literal prompt, as 0xF2 with the 0x167 prompt misc words).
- r607 item 101: self-field oracle + the 0x1D0 (41334), 0x97 (385C8), 0xD8 (55EFC) handlers.
- r607 item 101: ASL 0x1D0 (41334, 9C &= ~0x4000), 0x97 (385C8, drop two words), 0xD8 (55EFC, sign as q12) through the full
- r607 item 101: 0x55EFC top := 0x1000 / -0x1000 / 0 by sign, in place

## 0x0D9 `spawn_actor`

Handler `0x3E314`, extra words: 5.

- decode_actor_d9 = opcode 0xd9), NativeD9PrefixReceipt placement/cursor_mode, finish_native_d9_constructor branches, bind accepts return pc 0x3e300 / 0x3e3d8;
- Recovered SLES03662 D9 -> 3E314/346B0 normal-pool data initialization.
- 0x3E314/0xD9: 1 = insert after the parent;
- Wrappers: 3E2AC stores half 0, 3E314 half 1, 3E380 half 2 at sp+44 (= record+0x14);

## 0x0DB `move_along_facing`

Handler `0x3C1A4`, extra words: 0.

- 3C0F8/3C1A4 use only yaw bits12..23;

## 0x0DC `move_against_facing`

Handler `0x3C0F8`, extra words: 0.

- 3C0F8/3C1A4 use only yaw bits12..23;

## 0x0DD `start_actor_sound_front_end_volume`

Handler `0x38B6C`, extra words: 0.

- 0x38B6C: top = volume word (>>12 logical), second = sound id;

## 0x0DE `start_actor_sound_with_volume_result`

Handler `0x38A94`, extra words: 0.

- Source DE/38A94, manager0 fresh-group/resident-bank1 path.

## 0x0DF `backup_waypoint_link`

Handler `0x39A78`, extra words: 0.


## 0x0E0 `restore_waypoint_link`

Handler `0x39A84`, extra words: 0.


## 0x0E1 `set_actor_sound_volume`

Handler `0x386B4`, extra words: 0.

- QuantumAudioStage carries stream_group / stream_volume: 0x99 new group (plan root, min(request volume, 128)), 0x99 existing group (root, request volume), E1 (group, min(volumeWord >> 12, 128) like 386B4 / 4BB2C).
- Source 0x386B4 (ASL opcode 0xE1): pops volume word (top) and channel;
- Opcode 0xE1 (source 0x386B4): pops volume word (top) and channel;

## 0x0E2 `debug_noop`

Handler `0x374D0`, extra words: 0.


## 0x0E3 `store_scene_word_e3`

Handler `0x3ADB4`, extra words: 0.

- writer than 3ADB4).
- Original E3/3ADB4 consumes one raw word and overwrites7C874, independently of40/137.

## 0x0E5 `set_actor_channel_pitch`

Handler `0x385DC`, extra words: 0.

- 0xE5 (0x385DC channel pitch): a negative channel is a pure pop (r607-ope5-check 20,001/0);
- Barrier 2 (frame 6032): ASL 0xE5 (0x385DC: pops P, channel C;
- Source 0x385DC (ASL opcode 0xE5): pops pitch P (top) and channel C;
- r607 item 100: E5 (0x385DC command 4) replaces the pitch word of the playing channel;
- r607: ASL 0xE5 (0x385DC channel pitch) — the negative-channel branch through the native VM tick against the ORIGINAL handler: the
- r607 item 100: ASL 0xE5 (0x385DC) channel pitch.

## 0x0E6 `clamp_magnitude`

Handler `0x3803C`, extra words: 0.

- 0xE6 (0x3803C clamp magnitude, signed compare): r607-ope6-check 40,000/0.
- r607: ASL 0xE6 (0x3803C clamp magnitude) through the native VM tick against the ORIGINAL handler.
- r607: 0x3803C pops limit L then value V;

## 0x0E8 `narration_literal`

Handler `0x52C58`, extra words: 1.

- 0 if a narration start (0x52C58/0x52CF4) is emitted in the same tick.
- r607 item 180: a narration start emitted in THIS tick (0xE8 0x52C58 / 0x1DF 0x52CF4 -> 0x52804 clears +5A8)

## 0x0E9 `copy_parent_full_pose`

Handler `0x38504`, extra words: 0.

- ASL 0xE9 (0x38504): copy pose words +0x24..+0x43 from the actor pointed to by the caller's +0xD8 (written by ASL 0x40/130).
- ASL 0xE9 (0x38504): pose words +0x24..+0x43 copied from the actor stored at +0xD8 (appended ABI)

## 0x0EC `list_insert_after_root`

Handler `0x3E5A8`, extra words: 0.


## 0x0ED `list_move_before_current`

Handler `0x3E5D0`, extra words: 0.


## 0x0F2 `dialogue_literal`

Handler `0x52CA4`, extra words: 1.

- The old header claim "+5C4 is never written" was wrong: every ASL dialogue starter writes +5C0 / +5C4 / +5C8 before 0x52804 - 0xF2 (0x52CA4) / 0x1E0 (0x52D54): +5C0 = 4096, +5C4 = 0;
- Also: selector 103 read (close flag +5A8) in the same tick as a dialogue start now sees 0 for 0x52CA4 (0xF2) and 0x52DB4 (0x107) too (only 0x52D54 / 0x52E0C before) - the original starts the window synchronously.
- r607 item 157: +5C0 / +5C4 / +5C8 ARE written by the ASL starters before 0x52804 (0xF2 0x52CA4 / 0x1E0 0x52D54: +5C0 = 4096,
- 0x52D54 / 0x52CA4 (ASL 0xF2): [0x7C6A8]=4096, [0x7C6AC]=0
- r607 item 157: 0x52CA4 (0xF2) / 0x52DB4 (0x107) start the dialogue window the same way.

## 0x0F5 `copy_root_full_pose`

Handler `0x381C0`, extra words: 0.

- 381C0: full ROOT78A1C pose, not camera78A28.

## 0x0F6 `load_pose_from_waypoint`

Handler `0x384A4`, extra words: 0.

- Source 0x384A4 (ASL 0xF6): executing actor pose := waypoint at actor+0x1C.
- opcode 0xF6 (source 0x384A4)

## 0x0F9 `request_scene_fade`

Handler `0x37910`, extra words: 0.

- 0xF9 (37910) sets 0x78ADC := 6, which 24790 ignores at fade end.
- ASL 0xF9 (source 0x37910): pop raw, idx=raw>>12 selects the 2A2C8 case (1->1,2->5,3->11,4->13,5->15,6->7, otherwise 3), call 2A2C8(case)
- ASL 0xF9 (appended ABI)

## 0x0FA `request_scene_fade_in`

Handler `0x37874`, extra words: 0.

- 0xFA (0x37874): fade-in cases of 2A2C8 (idx 1->2, 3->10, 4->14, 5->16, else 4): plan_native_fade_request_fa (native-scene-transition.h;
- r607: the other 2A2C8 fade-in callbacks (ASL 0xFA): same BDC -= BE0 / 28740 flow, only the draw differs (29AE0, 2945C, wipe).
- r607: the fade-in bodies of 2A2C8 reached by ASL 0xFA (source 0x37874): idx = raw >> 12 selects 1 -> case 2, 3 -> 10, 4 -> 14,
- the ASL 0xFA fade-in cases pass
- r607: ASL 0xFA (0x37874 fade-in cases of 2A2C8), 0x172 (0x375FC direct scene change) and 0x150/0x151 (0x379C8/0x37A10 screen
- r607: ASL 0xFA (0x37874) fade-in cases of 2A2C8 (appended ABI)

## 0x0FB `add_actor_height`

Handler `0x3C48C`, extra words: 0.


## 0x0FC `subtract_actor_height`

Handler `0x3C4F4`, extra words: 0.


## 0x0FE `empty_handler_fe`

Handler `0x374D8`, extra words: 0.

- 0x78 (0x3ABA8 nearest waypoint of the +14 chain, unsigned strict min) + 0xFE (0x374D8 empty handler): r607-op78-check 20,001/0.
- plus 0xFE (0x374D8, empty handler) through the VM.

## 0x0FF `store_base_animation_rate140`

Handler `0x37858`, extra words: 0.


## 0x107 `dialogue_literal_prompt`

Handler `0x52DB4`, extra words: 1.

- Ported: 0x1D2 (0x41388 primary rate, PrimaryRate1D2 call kind), 0x1D0 (0x41334: 9C &= ~0x4000), 0x166 (0x3FDD8 base frame seek: frame = v >> 12, 0 when >= total, +13C / +140, flags |= 8), 0x69 (0x3A180 pitch toward root), 0xC3 (0x39740 timer max via set_process_timer_c3), 0x97 (0x385C8 drop two), 0xD8 (0x55EFC sign q12), 0x107 (0x52DB4 literal prompt, as 0xF2 with the 0x167 prompt misc words).
- 0x107 (0x52DB4) / 0x167 (0x52E0C): +5C0 = 0, +5C4 = 1, +5C8 = 0;
- Also: selector 103 read (close flag +5A8) in the same tick as a dialogue start now sees 0 for 0x52CA4 (0xF2) and 0x52DB4 (0x107) too (only 0x52D54 / 0x52E0C before) - the original starts the window synchronously.
- 0x107 0x52DB4 / 0x167 0x52E0C: +5C0 = 0, +5C4 = 1, +5C8 = 0;
- 0x52DB4 (ASL 0x107): the same words as 0x167
- r607 item 157: 0x52CA4 (0xF2) / 0x52DB4 (0x107) start the dialogue window the same way.

## 0x109 `assign_dialogue_owner`

Handler `0x3BF24`, extra words: 0.


## 0x10A `distance3d_sqrt_to_point`

Handler `0x3B130`, extra words: 0.

- 0x3B130 -> 0x452CC: pop z (top), y, x;

## 0x10D `close_dialogue_window`

Handler `0x52EF0`, extra words: 0.

- ITEM 131 (build-148): ASL 0x10D (0x52EF0) close dialogue window: 0x7C0E8 byte +0 := 0;
- Emitted as a dialogue event (handler 0x52EF0), applied to the staged dialogue window;
- a 0x52EF0 close or an unvoiced start falls back to misc_words (no blanket refusal any more).
- r607 item 131: ASL 0x10D close of the dialogue window
- r607 item 131: 0x52EF0: dialogue struct 0x7C0E8 byte +0 := 0;
- start (voice state carried over) or a close (0x52EF0) in this tick is still refused.

## 0x10E `revert_map_pieces_at_actor_cell`

Handler `0x3F134`, extra words: 0.

- Exact 0x3F2B8 (0x10F, record value +0xC) / 0x3F134 (0x10E, record value +0x10) loop for the actor's cell (x>>12, z>>12).
- ASL 0x10E (0x3F134): the same loop with record value +0x10, appended ABI

## 0x10F `swap_map_pieces_at_actor_cell`

Handler `0x3F2B8`, extra words: 0.

- Item 114 made ASL 0x10F/0x10E piece swaps change the collision;
- swapped by ASL 0x10F / 0x10E (item 114 already updates the collision) also changes on screen.
- ASL 0x10F (source 0x3F2B8): per-map "other piece records" (map+0x50, other_piece_records of 24 bytes each) bind a map cell (+0 = cell X,
- Exact 0x3F2B8 (0x10F, record value +0xC) / 0x3F134 (0x10E, record value +0x10) loop for the actor's cell (x>>12, z>>12).
- ASL 0x10F owner (initial values from the level file)
- r607 item 184: live ASL 0x10F/0x10E piece-model array (map+0x4C, level-file values) and, for the piece table map+0x54

## 0x115 `move_across_facing`

Handler `0x3C2D0`, extra words: 0.


## 0x116 `move_across_facing_reverse`

Handler `0x3C380`, extra words: 0.


## 0x117 `bitwise_not`

Handler `0x3B88C`, extra words: 0.


## 0x118 `script_frame_enter`

Handler `0x37AC0`, extra words: 0.


## 0x119 `script_frame_leave`

Handler `0x37AE0`, extra words: 0.

- Original37AC0/37AE0 are the only two handlers in the whole0x69000-byte

## 0x11B `store_fields_b0_b4`

Handler `0x38684`, extra words: 0.


## 0x11D `set_actor_bytes_158_15b`

Handler `0x3BC30`, extra words: 0.

- 0x3BC30: top -> +0x15A, second -> +0x159, third -> +0x158, then +0x15B := 1;
- ASL 0x11D (0x3BC30): bytes +0x158,+0x159,+0x15A := low bytes of the popped words >> 12 (logical) and +0x15B := 1 (appended ABI).

## 0x11E `clear_actor_byte_15b`

Handler `0x3BC88`, extra words: 0.

- ASL 0x11E: *(u8*)(actor+0x15B)=0 on the staged pool of this quantum (normal 364-byte actors only).
- ASL 0x11E (source 0x3BC88): stores the byte 0 at executing-actor +0x15B (normal actors only;
- ASL 0x11E (appended ABI)

## 0x121 `query_actor_audio_resource`

Handler `0x38DF4`, extra words: 0.

- a listed policy actor with B8 0 answers -1 (38DF4: BC nonzero, then B8 == 0);
- ASL 0x121 on manager 0 (LibrarySecretDoor, M008 actor 26 script 14 words 194..227).
- Source 0x38DF4: bank = key>>16 ? 3 : (AF ? 4 : 1);
- Item 82: a listed policy group whose one-shot completed keeps its (nonzero) group with B8 0: 38DF4 reads BC, then B8 == 0 -> -1.
- Source 0x4CF48 -> 0x4C14C -> 0x4C0D8 (flags=1 query used by ASL 0x121): channel index
- Native arithmetic of121/38DF4 + bank4 query path.

## 0x12C `horizontal_distance_table_sqrt`

Handler `0x3B1BC`, extra words: 0.


## 0x135 `increment_process_frame_budget`

Handler `0x4255C`, extra words: 0.

- Original135/4255C adds100hex to the SAME process budget, within an admitted

## 0x136 `remove_collision_sphere`

Handler `0x39688`, extra words: 0.

- 0x136 (0x39688 remove a collision sphere entry, partner of 0xC4) and 0x03 (0x3EA3C skip N instructions, 0x45/0xE2 carry one inline word, then the debug text line 0x7C7E4 = frame_prefix.raw_7c7e4 += 12): r607-op136-3-check 23,000/0.
- The oracle (r604-source-oracle.h) gained unaligned LWL/LWR/SWL/SWR (used by 0x39688);
- r607: source 0x39688 (ASL 0x136): pop K;
- by 0x39688 (ASL 0x136) entry moves.
- r607: ASL 0x136 (0x39688 collision sphere removal) — native plan_native_collision_136 against the ORIGINAL handler over a synthetic
- r607: ASL 0x136 (0x39688) (appended ABI)

## 0x137 `set_actor_context_flag400000`

Handler `0x3B00C`, extra words: 1.


## 0x138 `table_atan2_masked_q12`

Handler `0x3B0C8`, extra words: 0.


## 0x13A `set_actor_a0_bit40000000`

Handler `0x3B050`, extra words: 1.


## 0x13D `find_scene_light_record`

Handler `0x3F45C`, extra words: 0.

- 0x13D (0x3F45C): scene light record nearest the popped (x,y,z): cell (x>>12)+(z>>12)*columns of grid 0x79174 -> two indices;
- r607: ASL 0x13D (0x3F45C).
- r607: ASL 0x13D (0x3F45C scene light record nearest the popped point: grid 0x79174 cell pair, type byte +19 == 2, 4534C distance)
- 3F45C pops z (top), y, x and pushes the record address or 0 (a raw word;
- r607: ASL 0x13D (0x3F45C) scene light record (records 0x79438, grid 0x79174) nearest the popped (x,y,z): the exact original

## 0x13E `set_scene_light_intensity`

Handler `0x3F5B4`, extra words: 0.

- 0x13E (0x3F5B4): pops intensity + record;
- NATIVE POLICY (presentation only: nothing but the renderer reads those bytes) the world renderer replays 3F5B4 exactly (native_map_relight_3f5b4: radius ((2 + (b & 1)) << (((b >> 1) + 8) & 31)) + a, n = ((r + 0x800) >> 12) + 1, unsigned row stop ends the call, column stop ends the row, cell lists [h+0x40];
- r607-map-colour-check 196,617 / 0 (DPCS end points + lerp +-1, frame select, synthetic 3F5B4 grid: reach, byte 3, dark/clear, radius encoding, negative row ends the call);
- apply_piece_swaps (each synchronize) rebuilds the map mesh only when the live models/origins differ from what is drawn: OBJ triangles of changed pieces dropped, DPSX mesh of the live model appended, its vertex colours bound to the live table entry's stream (same 1E368 frame / 3F5B4 relight path).
- 3F5B4 replay over the current scene: per piece -1 untouched, else the byte 7 high bits it leaves (0, 0x40 or 0x80) and, for
- r607: ASL 0x13E (0x3F5B4) operand check: only a record address 0x13D can produce (records base + 32 * grid byte, so index <= 255

## 0x14C `store_bound_collision_halfword26`

Handler `0x3BB84`, extra words: 0.

- 3BA40,3BB84,3C67C,3C670.

## 0x14D `angle_difference_q12`

Handler `0x3F8DC`, extra words: 0.


## 0x150 `screen_overlay_enable`

Handler `0x379C8`, extra words: 1.

- 0x150 (0x379C8, ONE inline word) / 0x151 (0x37A10 -> 2A56C): screen overlay state Globals::screen_overlay (789D0, GP+BEC..BF8).
- SCREEN OVERLAY 2A594 DRAWN (ASL 0x150 / 0x151) + PS1 BLENDS.
- r607 item 90: 2A594 screen overlay (ASL 0x150 / 0x151) on the OT head, over the world and its text windows.
- ASL 0x150 switches it,
- r607: ASL 0xFA (0x37874 fade-in cases of 2A2C8), 0x172 (0x375FC direct scene change) and 0x150/0x151 (0x379C8/0x37A10 screen
- r607: 0x379C8: inline word != 0 -> 2A538 (789D0 := 1, BEC/BF0/BF4/BF8 := 0), else 2A55C (789D0 := 0).

## 0x151 `screen_overlay_colour`

Handler `0x37A10`, extra words: 0.

- 0x150 (0x379C8, ONE inline word) / 0x151 (0x37A10 -> 2A56C): screen overlay state Globals::screen_overlay (789D0, GP+BEC..BF8).
- r607: ASL 0xFA (0x37874 fade-in cases of 2A2C8), 0x172 (0x375FC direct scene change) and 0x150/0x151 (0x379C8/0x37A10 screen
- r607: 0x37A10 -> 2A56C: BF8 := top >> 12, BF4 := next, BF0 := next, BEC := bottom (all SRL).
- r607: ASL 0x150 (0x379C8) / 0x151 (0x37A10) screen colour overlay drawn each frame by 0x2A594 while 789D0 != 0: enabled = 789D0,

## 0x152 `add_actor_light`

Handler `0x420D4`, extra words: 0.

- 0x152 (0x420D4 -> 0x1E0E0): per-frame actor light table 0x7C6F4 (4 x 36 bytes) -> native-actor-light.h (add_native_actor_light / clear_native_actor_lights), stored in NativeActorFramePrefixSnapshot::actor_lights and carried to the next frame with active/owner cleared (= 0x1E0B4 after the render;
- r607: 0x7C6F4 per-frame actor lights (ASL 0x152);
- ASL 0x152 (0x420D4 -> 0x1E0E0) adds one;
- r607: ASL 0x152 (0x420D4 -> 0x1E0E0 add a per-frame actor light to the 4-entry table 0x7C6F4) by the ORIGINAL interpreter vs the
- r607: ASL 0x152 (0x420D4 -> 0x1E0E0): add a per-frame light owned by the executing actor at its position: (type = popped >> 12,

## 0x153 `turn_yaw_toward_actor`

Handler `0x3FD0C`, extra words: 0.

- 0x153 (0x3FD0C: turn yaw toward a POPPED actor, = 0x6A with an actor ref): new ActorReferenceService::position_xz;
- r607: 0x3FD0C reads other+0x34/+0x3C.
- r607: ASL 0x153 (0x3FD0C: turn the yaw toward a POPPED actor by at most `step`) and 0x159 run by the ORIGINAL interpreter
- r607: 0x3FD0C: pop step (top) and an actor;
- r607: ASL 0x153 (0x3FD0C): read the referenced actor's position words +0x34 (x) and +0x3C (z) (appended ABI)

## 0x154 `current_actor_reference`

Handler `0x3FCF4`, extra words: 0.

- 154/3FCF4 pushes the executing actor, independently of selected actorDC.

## 0x157 `interpolate_wrapping_q12`

Handler `0x3F938`, extra words: 0.


## 0x158 `signed_select_three_words`

Handler `0x3FA18`, extra words: 0.


## 0x159 `squared_distance_q12_point`

Handler `0x3B22C`, extra words: 0.

- 0x159 (0x3B22C -> 0x4534C squared distance to a stack point): r607-op159-check 40,000/0.
- r607: ASL 0x159 (0x3B22C -> 0x4534C squared distance to a stack point) through the native VM tick against the ORIGINAL handler.
- r607: 0x3B22C -> 0x4534C: pop z (top), y, x;

## 0x15A `squared_distance_to_xz`

Handler `0x3B2B8`, extra words: 0.

- 3B2B8 ->45424: pop targetZ,targetX,source SUBU/SRA6/IR16/SQR

## 0x15B `approach_value_by_step`

Handler `0x3FA7C`, extra words: 0.

- 0x3FA7C: pops step (top), target, current;

## 0x15C `squared_distance_xz_q12_four_words`

Handler `0x3FAF8`, extra words: 0.

- 0x3FAF8: pops four words;

## 0x15D `step_yaw_wrapping`

Handler `0x3A470`, extra words: 0.


## 0x15E `set_flag_a0_bit80`

Handler `0x3AFCC`, extra words: 1.


## 0x15F `point_in_rectangle_xz`

Handler `0x3FB80`, extra words: 0.

- 0x3FB80: stack (deep -> top) X, Z, x0, z0, x1, z1 -> 1 when x0<=X<=x1 and z0<=Z<=z1 (signed), else 0;

## 0x160 `advance_waypoint_by_count`

Handler `0x3A608`, extra words: 0.

- Source 0x3A608: steps = value>>12 (SRA).

## 0x161 `inside_current_waypoint_rectangle`

Handler `0x3A774`, extra words: 0.


## 0x164 `release_actor_particles`

Handler `0x4F86C`, extra words: 0.

- Source 0x4F86C (ASL 0x164): walk the live particle list (gp+0x12C0) and, for every record whose owner word (+8) is the calling actor,
- ASL 0x164: stage the owner release on the quantum's particle pool copy (published with the quantum).
- ASL 0x164 (source 0x4F86C): release every live particle/effect record owned by the executing actor.
- ASL 0x164 (appended ABI)

## 0x166 `set_base_animation_frame`

Handler `0x3FDD8`, extra words: 0.

- Ported: 0x1D2 (0x41388 primary rate, PrimaryRate1D2 call kind), 0x1D0 (0x41334: 9C &= ~0x4000), 0x166 (0x3FDD8 base frame seek: frame = v >> 12, 0 when >= total, +13C / +140, flags |= 8), 0x69 (0x3A180 pitch toward root), 0xC3 (0x39740 timer max via set_process_timer_c3), 0x97 (0x385C8 drop two), 0xD8 (0x55EFC sign q12), 0x107 (0x52DB4 literal prompt, as 0xF2 with the 0x167 prompt misc words).
- r607 item 101: ASL 0x166 (0x3FDD8): pop V;
- r607 item 101: ASL 0x166 (0x3FDD8) direct base frame set (appended ABI)

## 0x167 `dialogue_q12_prompt`

Handler `0x52E0C`, extra words: 0.

- 0x167 (0x52E0C): dialogue start like 0x1E0 but [7C6A8]=0, [7C6AC]=1, [7C6B0]=0 (index = sra(v,12)-1 only for v > 0;
- ITEM 141 (build-164): 0x0B selector 136 = 1 when a VOICED dialogue start (0x52D54 / 0x52E0C with a string voice >= 0) is the last window event this frame;
- 0x107 (0x52DB4) / 0x167 (0x52E0C): +5C0 = 0, +5C4 = 1, +5C8 = 0;
- Also: selector 103 read (close flag +5A8) in the same tick as a dialogue start now sees 0 for 0x52CA4 (0xF2) and 0x52DB4 (0x107) too (only 0x52D54 / 0x52E0C before) - the original starts the window synchronously.
- 0x107 0x52DB4 / 0x167 0x52E0C: +5C0 = 0, +5C4 = 1, +5C8 = 0;
- r607: 0x52E0C (ASL 0x167): [0x7C6A8]=0, [0x7C6AC]=1, [0x7C6B0]=0.

## 0x16C `random_signed_remainder`

Handler `0x3B52C`, extra words: 0.

- 0x3B52C: n==0 -> 0 (no draw);

## 0x16F `clamp_to_current_waypoint_segment`

Handler `0x3A928`, extra words: 0.

- 0x16F (0x3A928 clamp X/Z into the current waypoint segment box): r607-op16f-check 40,001/0.
- r607: source 0x3A928 (ASL 0x16F).
- r607: ASL 0x16F (0x3A928 clamp X/Z into the current waypoint segment box) — native clamp_native_waypoint_segment over a synthetic
- r607: ASL 0x16F (0x3A928): clamp actor X/Z into the box of the current waypoint (+1C) and its next (or +14 when last) (appended ABI)

## 0x170 `list_insert_before_camera_170`

Handler `0x3FF88`, extra words: 0.


## 0x171 `list_insert_after_anchor_171`

Handler `0x3FFB0`, extra words: 0.


## 0x172 `scene_transition_direct`

Handler `0x375FC`, extra words: 0.

- 0x172 (0x375FC): direct scene change (episode, level, map) without 201's 339F8 pass: plan_native_scene_transition_172 (primary[6..9] := old 1/2/4/3, new 1/2/4..5, [3] := 0, 78ADC := 7, 2A2C8(1) while 789CC == 0).
- r607: ASL 0x172 (source 0x375FC): direct scene change to (episode, level, map) without 201's 339F8 summary pass.
- r607: ASL 0xFA (0x37874 fade-in cases of 2A2C8), 0x172 (0x375FC direct scene change) and 0x150/0x151 (0x379C8/0x37A10 screen
- r607: ASL 0x172 (0x375FC) direct scene change (episode, level, map raw words, bottom to top) (appended ABI)

## 0x173 `progress_scalar_read`

Handler `0x37D8C`, extra words: 0.


## 0x174 `progress_bit_read`

Handler `0x37DDC`, extra words: 0.


## 0x175 `progress_scalar_write`

Handler `0x37D04`, extra words: 0.


## 0x176 `progress_bit_write`

Handler `0x37D4C`, extra words: 0.


## 0x177 `raw_table_square_root`

Handler `0x3AE3C`, extra words: 0.

- 177/3AE3C uses the same immutable5DA54 table as12C, with a raw word input.

## 0x17A `store_waypoint_half08`

Handler `0x39A9C`, extra words: 0.

- 39A9C/39AC4/39AEC: current waypoint [actor+1C] +8/+A/+C.

## 0x17B `store_waypoint_half0a`

Handler `0x39AC4`, extra words: 0.

- 39A9C/39AC4/39AEC: current waypoint [actor+1C] +8/+A/+C.
- op 0x17B: current waypoint halfword (ABI)

## 0x17C `store_waypoint_half0c`

Handler `0x39AEC`, extra words: 0.

- 39A9C/39AC4/39AEC: current waypoint [actor+1C] +8/+A/+C.

## 0x181 `list_move_to_head`

Handler `0x3FECC`, extra words: 0.

- 0x181 (0x3FECC move the executing actor to the normal list HEAD;
- r607: admit 0x3FECC (ASL 0x181) for its own check only
- r607: source 0x3FECC (ASL 0x181): a member with prev (+10) == 0 stays;
- r607: ASL 0x181: no anchor, move the executing actor to the normal list head
- r607: ASL 0x181 (0x3FECC move the executing actor to the normal list head) — native_actor_move_to_head vs the ORIGINAL routine.
- r607: ASL 0x181 (0x3FECC): move the executing actor to the normal list head (appended ABI)

## 0x188 `set_particle_half3e`

Handler `0x4F384`, extra words: 0.

- ASL 0x188: builder halfword at +62 (= gp+0x1306 = 0x788FE) := low16 of the popped word
- 0x4F384: gp+0x1306 (builder halfword +62) := (u16) popped word, no Q12 conversion.

## 0x189 `begin_normal_actor_iterator`

Handler `0x40168`, extra words: 0.


## 0x18A `advance_normal_actor_iterator`

Handler `0x40194`, extra words: 0.


## 0x18B `initialize_startup_block`

Handler `0x4EB6C`, extra words: 0.


## 0x18C `clear_particle_textures`

Handler `0x4EB8C`, extra words: 0.

- ASL 0x18C (0x4E624), appended (ABI)

## 0x18D `copy_particle_template`

Handler `0x4EBAC`, extra words: 0.


## 0x18E `intern_template_reference`

Handler `0x4EBE0`, extra words: 0.


## 0x18F `release_particle_template_reference`

Handler `0x4ECDC`, extra words: 0.

- ASL 0x18F (0x4ECDC): if the template's owner word (+8) is the executing actor it is cleared, then 0x4E684 releases the reference.
- ASL 0x18F (0x4ECDC): clear record+8 first when it equals the executing actor
- ASL 0x18F (appended ABI)

## 0x190 `append_startup_block`

Handler `0x4ED28`, extra words: 0.


## 0x191 `set_particle_vector_signed16`

Handler `0x4EEE4`, extra words: 0.


## 0x192 `set_particle_vector_range_signed16`

Handler `0x4EF3C`, extra words: 0.


## 0x193 `set_particle_color_offset`

Handler `0x4EF94`, extra words: 0.


## 0x194 `set_particle_color`

Handler `0x4EFEC`, extra words: 0.


## 0x195 `set_particle_color_range`

Handler `0x4F04C`, extra words: 0.


## 0x196 `set_startup_triple`

Handler `0x4F0AC`, extra words: 0.


## 0x197 `set_particle_scale`

Handler `0x4F10C`, extra words: 0.


## 0x198 `set_particle_scale_range`

Handler `0x4F140`, extra words: 0.


## 0x199 `set_particle_scalar_signed16`

Handler `0x4F174`, extra words: 0.


## 0x19A `set_particle_spread34`

Handler `0x4F1A8`, extra words: 0.

- ASL 0x19A: builder b[53]=0, b[52]=(u8)(popped>>12)
- raw popped word (0x4F3A8/0x4F3DC/0x4F1A8/0x4F1D0 pass it through unconverted)

## 0x19B `set_particle_spread34_range`

Handler `0x4F1D0`, extra words: 0.

- ASL 0x19B: builder b[52]/b[53] range pair from the popped word
- raw popped word (0x4F3A8/0x4F3DC/0x4F1A8/0x4F1D0 pass it through unconverted)

## 0x19C `initialize_startup_unsigned_half`

Handler `0x4F21C`, extra words: 0.


## 0x19D `update_startup_unsigned_half`

Handler `0x4F258`, extra words: 0.


## 0x19E `initialize_startup_signed_half`

Handler `0x4F294`, extra words: 0.


## 0x19F `update_startup_signed_half`

Handler `0x4F2D0`, extra words: 0.


## 0x1A0 `set_startup_byte44`

Handler `0x4F30C`, extra words: 0.


## 0x1A1 `set_particle_count_range`

Handler `0x4F348`, extra words: 0.


## 0x1A2 `set_particle_flags`

Handler `0x4F3A8`, extra words: 0.

- raw popped word (0x4F3A8/0x4F3DC/0x4F1A8/0x4F1D0 pass it through unconverted)
- ASL 0x1A2 FlagsSet, 0x1AC FlagsClear, 0x19A/0x19B spread bytes (raw popped word), appended (ABI)

## 0x1A3 `emit_particle_template`

Handler `0x4F410`, extra words: 0.

- ASL opcode 0x1A3 (source 0x4F410 -> 0x4E430(actor, template+16)): spawn a particle effect from a
- ASL 0x1A3 requests (native policy, see native-particle-emit.h)
- The native backend consumes the recorded ASL 0x1A3/0x1A7 emit requests;
- Opcode 0x1A3 (source 0x4F410): pops a particle template reference and requests the effect.

## 0x1A4 `emit_particle_at_world_point`

Handler `0x4F444`, extra words: 0.


## 0x1A5 `emit_template_particle_from_actor_with_vector`

Handler `0x4F4D0`, extra words: 0.

- 0x1A5 (0x4F4D0 template emitter from the actor position with a script vector, core 0x4E248) and 0x7A (0x39FFC pitch toward the current waypoint, = 0x6C with the +1C waypoint point): r607-op7a-check 10,001/0.
- plus the ASL 0x1A5 operand order (template + vector, core = 0x4E248 checked by r607-op1a9-check).
- r607: 0x4F4D0 pops vz (top), vy, vx (LHU+sign) and the template (+16 payload);
- r607: ASL 0x1A5 (0x4F4D0 -> 0x4E248): template from the actor position with an explicit vector (appended ABI)

## 0x1A6 `emit_template_particle_with_vector`

Handler `0x4F544`, extra words: 0.

- 0x1A6 (0x4F544 -> bare 0x4DBC8 with a script vector): plan_particle_point_record `given` vector;
- r607: ASL 0x1A6 (0x4F544 -> 0x4DBC8(actor, template+16, point, vx, vy, vz)): a template emitter whose vector halves come from the
- r607: with `given`, this is the bare 0x4DBC8 constructor (ASL 0x1A6 passes the vector halves itself): the 4E0E8 template vector and
- r607: ASL 0x1A6 core — the bare 0x4DBC8 particle constructor with an explicit vector (plan_native_particle_point_pool `vector`)
- r607: 0x4F544 pops vz (top), vy, vx as LHU+sign halves, then z, y, x words, then the template (+16 payload).
- r607: ASL 0x1A6 (0x4F544): template, point and an explicit vector (appended ABI)

## 0x1A7 `emit_particle_builder`

Handler `0x4F600`, extra words: 0.

- ASL 0x1A7: emitted from the live builder block (0x788C0), not from a template reference
- r607: ASL 0x1A7 (4F600 -> 4E430(actor, builder 788C0)) and 0x1A8 (4F644 -> 4E0E8(actor, builder, popped point)) use the SAME
- ASL 0x1A7 (0x4F600): normalize the builder (0x4D970) and emit it at the executing actor (0x4E430).

## 0x1A8 `emit_particle_builder_at_point`

Handler `0x4F644`, extra words: 0.

- ASL 0x1A8 (0x4F644): builder particle at an explicit point — same native particle policy as 0x1A7 (request recorded, pool not written).
- r607: ASL 0x1A8 explicit emission point
- r607: ASL 0x1A7 (4F600 -> 4E430(actor, builder 788C0)) and 0x1A8 (4F644 -> 4E0E8(actor, builder, popped point)) use the SAME
- 0x4F644 pops z, y, x (raw words) into a stack vector, normalizes the builder (0x4D970) and emits at that point (0x4E0E8)
- r607: ASL 0x1A8 (0x4F644): same normalized builder, emitted at an explicit point (x,y,z popped) through 0x4E0E8

## 0x1A9 `emit_builder_particle_with_vector`

Handler `0x4F6D8`, extra words: 0.

- 0x1A9 (0x4F6D8 -> 0x4E248 builder from the actor position with a vector): r607-op1a9-check 307,529/0 (oracle admit_4e248 flag added).
- r607: admit 0x4E248 (ASL 0x1A9 emitter) for its own check only
- r607: ASL 0x1A9 core — 0x4E248 (actor-position offset/spread, then 0x4DBC8 with an explicit vector): plan_particle_actor_point +
- r607: 0x4F6D8 pops vz (top), vy, vx as LHU+sign halves, normalizes the builder (0x4D970) and emits from the actor position
- r607: ASL 0x1A9 (0x4F6D8 -> 0x4E248): same normalized builder from the actor position with an explicit vector (appended ABI)

## 0x1AA `emit_builder_particle_at_point_with_vector`

Handler `0x4F77C`, extra words: 0.

- 0x1AA (0x4F77C builder at a point with a vector -> 0x4DBC8): r607-op1aa-check (VM operand order;
- r607: ASL 0x1AA (0x4F77C) operand order through the native VM: pops vz (top), vy, vx (LHU+sign halves) and z, y, x words, then
- r607: 0x4F77C pops vz (top), vy, vx (LHU+sign) then z, y, x words;
- r607: ASL 0x1AA (0x4F77C -> 0x4DBC8): same normalized builder at an explicit point with an explicit vector (appended ABI)

## 0x1AB `copy_current_camera_pose`

Handler `0x40260`, extra words: 0.


## 0x1AC `clear_particle_flags`

Handler `0x4F3DC`, extra words: 0.

- raw popped word (0x4F3A8/0x4F3DC/0x4F1A8/0x4F1D0 pass it through unconverted)

## 0x1AD `allocate_word_buffer_reference`

Handler `0x402B4`, extra words: 0.


## 0x1AE `release_word_arena_buffer`

Handler `0x40304`, extra words: 0.

- 0x1AE (0x40304 -> 0x4275C free a 0x1AD buffer;
- r607: ASL 0x1AE: release the buffer a base (offset 0) 0x1AD reference names through 0x4275C;
- r607: ASL 0x1AE (0x40304 -> 0x4275C release) VM path: pops a WordArenaBufferReference and hands (token, origin) to the release
- r607: ASL 0x1AE (0x40304 -> 0x4275C) free a 0x1AD buffer (appended ABI)
- r607 item 172: ASL 0x1AE (0x40304 -> 0x4275C) frees the buffer, but the source local / stack cell keeps the raw pointer word.

## 0x1AF `read_word_buffer_reference`

Handler `0x40338`, extra words: 0.


## 0x1B0 `store_word_buffer_reference`

Handler `0x40368`, extra words: 0.

- Item 176 (build-216): op 0x1B0 (0x40368) may store an ACTOR REFERENCE into a word-arena buffer element (M006 s8 vent parent stores its spawned child).
- 0x1B0 (0x40368) of an actor reference stores the raw actor pointer word;
- 40368 store,40418 copy

## 0x1B2 `string_number`

Handler `0x405EC`, extra words: 0.

- 0x1B2 (0x405EC): string number.
- r607: ASL 0x1B2 (0x405EC).
- r607: ASL 0x167 (0x52E0C dialogue start, words 7C6A8/7C6AC/7C6B0), 0x1B2 (0x405EC '#hex' skip via 0x52580 + '$NN' number) and
- r607: ASL 0x1B2 (0x405EC) '$NN' string number (appended ABI)

## 0x1B3 `draw_centered_inline_scene_text`

Handler `0x40750`, extra words: 1.

- (0x40928 = 0x40750 with x - width instead of x - width/2.)

## 0x1B4 `set_label_anchor`

Handler `0x40A18`, extra words: 0.

- 0x40A18: pop y-source (top) then x-source;
- ASL 0x1B4 (0x40A18): label anchor words 0x78728/0x7872C, appended ABI

## 0x1B5 `set_hud_panel`

Handler `0x305B4`, extra words: 0.

- 0x1B5 (0x305B4 "setpanel" = HUD panel settings): Globals::hud_panel (GP+D14 flags, +D7C/D7E/D80 modes, +D82/D83/D84 bytes;
- r607: ASL 0x1B5 (0x305B4 "setpanel": HUD panel flags GP+D14, modes GP+D7C/D7E/D80, bytes GP+D82/D83/D84) by the ORIGINAL
- r607: ASL 0x1B5 (0x305B4 "setpanel") HUD panel settings at GP 0x775F8: flags +D14, modes +D7C/+D7E/+D80, bytes +D82/+D83/+D84.
- r607: 0x305B4 body.

## 0x1B6 `query_actor_walls`

Handler `0x399C4`, extra words: 0.

- The original 0x399C4 call is a general NORMAL-actor query (not only the camera-bound startup actor): inside the frame body every

## 0x1B7 `progress_scalar_auto`

Handler `0x37EF4`, extra words: 0.

- 0x1B7 (0x37EF4 read) / 0x1B8 (0x37E2C store): progress SCALAR with the lazily allocated id at actor+0x152 (16E48 allocate_progress_scalar / 17054 signed byte << 12 / 16F34 byte := popped SRA 12).
- r607: 0x37E2C/0x37EF4 keep the scalar id at caller+0x152 (zeroed by the normal constructor);
- r607: ASL 0x1B7 (0x37EF4 read) / 0x1B8 (0x37E2C store) progress scalar with the lazily allocated id at actor+0x152 (16E48 / 17054 /
- r607: 0x37EF4 (read) / 0x37E2C (store): +0x152 == 0 -> 16E48 allocates a scalar id into it;
- r607: ASL 0x1B7/0x1B8: the executing actor's lazily allocated progress SCALAR id halfword +0x152 (pool bytes only, normal

## 0x1B8 `progress_scalar_auto_store`

Handler `0x37E2C`, extra words: 0.

- 0x1B7 (0x37EF4 read) / 0x1B8 (0x37E2C store): progress SCALAR with the lazily allocated id at actor+0x152 (16E48 allocate_progress_scalar / 17054 signed byte << 12 / 16F34 byte := popped SRA 12).
- r607: 0x37E2C/0x37EF4 keep the scalar id at caller+0x152 (zeroed by the normal constructor);
- r607: ASL 0x1B7 (0x37EF4 read) / 0x1B8 (0x37E2C store) progress scalar with the lazily allocated id at actor+0x152 (16E48 / 17054 /
- r607: 0x37EF4 (read) / 0x37E2C (store): +0x152 == 0 -> 16E48 allocates a scalar id into it;

## 0x1B9 `progress_bit_auto`

Handler `0x37F50`, extra words: 0.


## 0x1BA `progress_bit_auto_store`

Handler `0x37E90`, extra words: 0.

- 37E90: pop raw value, lazy16E88 only whenC2==0, then16F48.

## 0x1BB `root_inside_current_waypoint_rectangle`

Handler `0x3A85C`, extra words: 0.

- op 0x1BB from a special script).
- 0x3A85C: same rectangle test as 0x161 (current waypoint +0x10/+0x18 against its link or actor+0x14), but the point is the

## 0x1BC `move_actor_to_c5_point`

Handler `0x40D48`, extra words: 0.

- ASL 0x1BC (0x40D48: position := C5 point): r607-op1bc-check 10,000/0.
- Consumed-number translation of40AE0..40D48.
- r607: ASL 0x1BC (0x40D48: position := C5 point) through the native VM tick against the ORIGINAL handler.
- r607: 0x40D48 copies the C5 point (+124/+128/+12C, the field 81/82/83 words) into the actor position +34/+38/+3C;

## 0x1BD `set_particle_primary_vector`

Handler `0x4ED5C`, extra words: 0.


## 0x1BE `set_particle_primary_vector_range`

Handler `0x4EDD0`, extra words: 0.


## 0x1BF `interpolate_wrapped_angle`

Handler `0x3F994`, extra words: 0.


## 0x1C0 `set_process_projection_scale`

Handler `0x40D64`, extra words: 0.


## 0x1C1 `clear_referenced_actor_flags`

Handler `0x40DA0`, extra words: 0.


## 0x1C2 `set_actor_a0_bit10`

Handler `0x40DCC`, extra words: 1.


## 0x1C3 `add_owned_local_word`

Handler `0x40E0C`, extra words: 0.

- ITEM 144 (build-170): 0x1C3 / 0x1C4 (40E0C / 40E44: lw (ref);
- Original 40E0C/40E44 operate on raw 32-bit words.
- r607 item 144: 0x1C3/0x1C4 (40E0C/40E44: lw (ref);
- r607 item 167: 40E0C / 40E44 on a save-image word reference (0x0B/113 = save +0x3DC): lw;
- r607 item 181: 40E0C / 40E44 (lw;

## 0x1C4 `subtract_owned_local_word`

Handler `0x40E44`, extra words: 0.

- ITEM 144 (build-170): 0x1C3 / 0x1C4 (40E0C / 40E44: lw (ref);
- Original 40E0C/40E44 operate on raw 32-bit words.
- r607 item 144: 0x1C3/0x1C4 (40E0C/40E44: lw (ref);
- r607 item 167: 40E0C / 40E44 on a save-image word reference (0x0B/113 = save +0x3DC): lw;
- r607 item 181: 40E0C / 40E44 (lw;

## 0x1C5 `multiply_owned_local_word_q12`

Handler `0x40E7C`, extra words: 0.

- Item 177 (build-217): op 0x1C5 (0x40E7C) on a GLOBAL word reference: *ref = (lo>>12)|(hi<<20) of the signed 64-bit product (q12 multiply in place).
- r607 item 177: 1C5 (0x40E7C) on a global word: lw;
- r607 item 177: 1C5 (0x40E7C) signed Q12 multiply of the referenced global word (appended ABI).

## 0x1C7 `shift_left_owned_local_word`

Handler `0x40F34`, extra words: 0.

- ASL 0x1C7/0x1C8 (0x40F34 SLLV / 0x40F6C SRAV on a local reference).
- r607: original 40F34 (SLLV) / 40F6C (SRAV) shift the referenced word by (popped>>12) (MIPS uses the low 5 bits).
- r607: ASL 0x1C7 (0x40F34 SLLV) / 0x1C8 (0x40F6C SRAV) on a referenced word against the ORIGINAL handlers.
- r607: 0x1C7 (0x40F34, SLLV) / 0x1C8 (0x40F6C, SRAV): *local = *local <</>> ((popped>>>12)&31)

## 0x1C8 `shift_right_arithmetic_owned_local_word`

Handler `0x40F6C`, extra words: 0.

- ASL 0x1C7/0x1C8 (0x40F34 SLLV / 0x40F6C SRAV on a local reference).
- r607: original 40F34 (SLLV) / 40F6C (SRAV) shift the referenced word by (popped>>12) (MIPS uses the low 5 bits).
- r607: ASL 0x1C7 (0x40F34 SLLV) / 0x1C8 (0x40F6C SRAV) on a referenced word against the ORIGINAL handlers.
- r607: 0x1C7 (0x40F34, SLLV) / 0x1C8 (0x40F6C, SRAV): *local = *local <</>> ((popped>>>12)&31)

## 0x1C9 `find_word_buffer_value`

Handler `0x40398`, extra words: 0.

- Original 40398: unsigned Q12 count, first equal source word, index Q12.

## 0x1CA `signed_inclusive_range_three_words`

Handler `0x41014`, extra words: 0.


## 0x1CE `start_owned_primary_animation`

Handler `0x4117C`, extra words: 0.

- 0x1CE (0x4117C start PRIMARY animation layer: ctx+0 clip, +4 frame 0, +A fraction 0, +8 rate 0x1000, 9C |= 0x4000): start_actor_primary_animation_context + QuantumSecondaryAnimation::start_primary.
- r607-op1ce-check 69,633/0 (original 0x4117C);
- r607: nonnull 0x4117C writer (ASL 0x1CE), the PRIMARY twin of 41540: +0 clip, +4 frame 0, +A fraction 0, +8 rate 0x1000, 9C |= 0x4000.
- r607: ASL 0x1CE (0x4117C), the primary-layer twin of start().
- r607: ASL 0x1CE primary writer 0x4117C against the ORIGINAL routine (same fixture as the 0x1D5 secondary writer check).
- it does not ensure or read a context (41540 / r607: 4117C both test the popped word first).

## 0x1D0 `stop_primary_animation_clock`

Handler `0x41334`, extra words: 0.

- Ported: 0x1D2 (0x41388 primary rate, PrimaryRate1D2 call kind), 0x1D0 (0x41334: 9C &= ~0x4000), 0x166 (0x3FDD8 base frame seek: frame = v >> 12, 0 when >= total, +13C / +140, flags |= 8), 0x69 (0x3A180 pitch toward root), 0xC3 (0x39740 timer max via set_process_timer_c3), 0x97 (0x385C8 drop two), 0xD8 (0x55EFC sign q12), 0x107 (0x52DB4 literal prompt, as 0xF2 with the 0x167 prompt misc words).
- r607 item 101: self-field oracle + the 0x1D0 (41334), 0x97 (385C8), 0xD8 (55EFC) handlers.
- r607 item 101: ASL 0x1D0 (41334, 9C &= ~0x4000), 0x97 (385C8, drop two words), 0xD8 (55EFC, sign as q12) through the full
- r607 item 101: 0x41334, primary twin of 0x1D7 (9C &= ~0x4000, the bit 0x1CE sets)

## 0x1D1 `clear_owned_animation_primary`

Handler `0x41348`, extra words: 0.

- Actual 1D1/0x41348: ensure context (0x344AC), primary layer pointer := NULL (context+0), actor 9C &= ~0x4000.
- ASL 0x1D1: ensure the owned context, clear the primary layer and the actor 9C bit 0x4000 (typed flags of the executing quantum).
- ASL 0x1D1 (source 0x41348): ensure the owned animation context, primary layer := NULL, actor 9C &= ~0x4000 (typed flags).
- ASL 0x1D8 (appended ABI) // ASL 0x1D1 (appended ABI)

## 0x1D2 `set_primary_animation_rate`

Handler `0x41388`, extra words: 0.

- Ported: 0x1D2 (0x41388 primary rate, PrimaryRate1D2 call kind), 0x1D0 (0x41334: 9C &= ~0x4000), 0x166 (0x3FDD8 base frame seek: frame = v >> 12, 0 when >= total, +13C / +140, flags |= 8), 0x69 (0x3A180 pitch toward root), 0xC3 (0x39740 timer max via set_process_timer_c3), 0x97 (0x385C8 drop two), 0xD8 (0x55EFC sign q12), 0x107 (0x52DB4 literal prompt, as 0xF2 with the 0x167 prompt misc words).
- r607: ASL 0x1D2 (0x41388), the primary twin of 0x1D9: after 344AC, ctx+8 (primary rate) := the popped value's low 16 bits.
- r607: ASL 0x1D2 (0x41388), the primary-layer twin of rate().
- r607 item 101: ASL 0x1D2 primary rate 0x41388 against the ORIGINAL routine (344AC ensure, ctx+8 := u16 pop), plus the VM path.
- r607: ASL 0x1D2 (0x41388: 344AC, ctx+8 := u16 pop), primary twin of 0x1D9 (appended ABI)
- r607: admit 0x41388 (ASL 0x1D2 primary rate) for its own check only

## 0x1D4 `write_owned_animation_context_mask`

Handler `0x41460`, extra words: 0.


## 0x1D5 `start_owned_secondary_animation`

Handler `0x41540`, extra words: 0.

- r607: nonnull 0x4117C writer (ASL 0x1CE), the PRIMARY twin of 41540: +0 clip, +4 frame 0, +A fraction 0, +8 rate 0x1000, 9C |= 0x4000.
- it does not ensure or read a context (41540 / r607: 4117C both test the popped word first).

## 0x1D6 `seek_owned_secondary_animation`

Handler `0x415F0`, extra words: 0.


## 0x1D7 `stop_secondary_animation_clock`

Handler `0x416FC`, extra words: 0.


## 0x1D8 `clear_owned_animation_secondary`

Handler `0x41714`, extra words: 0.

- ASL 0x1D8 (0x41714) clears the secondary layer and 9C bit 0x10000
- ASL 0x1D8 (appended ABI) // ASL 0x1D1 (appended ABI)

## 0x1D9 `set_secondary_animation_rate`

Handler `0x41754`, extra words: 0.


## 0x1DB `global_word_or`

Handler `0x40FA4`, extra words: 0.

- Original40FDC/40FA4 mutate a word through the existing local lease.

## 0x1DC `and_owned_word`

Handler `0x40FDC`, extra words: 0.


## 0x1DF `narration_q12`

Handler `0x52CF4`, extra words: 0.

- 0 if a narration start (0x52C58/0x52CF4) is emitted in the same tick.
- r607 item 180: a narration start emitted in THIS tick (0xE8 0x52C58 / 0x1DF 0x52CF4 -> 0x52804 clears +5A8)

## 0x1E0 `dialogue_q12`

Handler `0x52D54`, extra words: 0.

- ITEM 141 (build-164): 0x0B selector 136 = 1 when a VOICED dialogue start (0x52D54 / 0x52E0C with a string voice >= 0) is the last window event this frame;
- The old header claim "+5C4 is never written" was wrong: every ASL dialogue starter writes +5C0 / +5C4 / +5C8 before 0x52804 - 0xF2 (0x52CA4) / 0x1E0 (0x52D54): +5C0 = 4096, +5C4 = 0;
- Also: selector 103 read (close flag +5A8) in the same tick as a dialogue start now sees 0 for 0x52CA4 (0xF2) and 0x52DB4 (0x107) too (only 0x52D54 / 0x52E0C before) - the original starts the window synchronously.
- r607 item 157: +5C0 / +5C4 / +5C8 ARE written by the ASL starters before 0x52804 (0xF2 0x52CA4 / 0x1E0 0x52D54: +5C0 = 4096,
- 0x52D54 / 0x52CA4 (ASL 0xF2): [0x7C6A8]=4096, [0x7C6AC]=0
- 136: a dialogue / narration start emitted in THIS tick (0x52D54 / 0x52E0C) is applied by the caller only after the tick;

## 0x1E1 `draw_centered_stack_scene_text`

Handler `0x407D0`, extra words: 0.

- r607 item 183: 0x408BC / 0x4099C = 0x1EE / 0x1EF with the string number POPPED: (word SRA 12) - 1 (as 0x1E1 / 0x407D0),
- 407D0: SRA12 then ADDIU -1;

## 0x1E2 `copy_word_buffer_references`

Handler `0x40418`, extra words: 0.

- No40368/40418 ASL calls and no extra allocation.
- 40368 store,40418 copy

## 0x1E3 `search_waypoint_rectangle_at_root`

Handler `0x3A8F8`, extra words: 0.

- 0x3A8F8: the 0x1F5 search with (x,z) = the ROOT actor's +0x34/+0x3C (root_field1c selectors 1 and 3);

## 0x1E4 `bind_animation_reference`

Handler `0x3EE68`, extra words: 0.

- Item 192: actor +CC (ASL 0x1E4, "animation_reference" in the native struct) is the far/LOD MODEL: 0x1F8E4 picks it by camera distance, 0x205C0 skips the clip for it;
- r607 item 203: 0x1F8E4: a nonzero +CC (far / LOD model, ASL 0x1E4) replaces the drawn model when [0x7B60C] <u the sum of the

## 0x1E5 `notify_actor_type8_event`

Handler `0x41A24`, extra words: 0.

- ITEM 147 (build-173): 0x1E5 (41A24) on a RAW actor pointer: the source dereferences the popped word (+9C, +AE, +A8 triggers);
- ITEM 151 (build-177): 0x1E5 (41A24) on an ActorReference whose actor was DESTROYED: the source dereferences the kept pointer, so the event reads the current +9C / +AE of the old slot (the live occupant, or the released bytes;
- 41A24 still dereferences the kept pointer (the old slot), so the
- r607 item 147: 41A24 dereferences the popped word as an actor pointer;

## 0x1E6 `broadcast_type8_event`

Handler `0x41AC8`, extra words: 0.

- Source41A24/41AC8/41C90 enqueue only: matching type8+message increments

## 0x1E7 `list_move_to_tail`

Handler `0x3FF14`, extra words: 0.

- Source 0x3FF14 (ASL 0x1E7): walk actor+0xC to the tail of the normal list;
- ASL 0x1E7: no anchor, append the executing actor to the normal list tail
- ASL 0x1E7 (0x3FF14): move the executing actor to the normal list tail (appended ABI).

## 0x1E8 `spawn_actor_at_list_tail`

Handler `0x3E380`, extra words: 5.

- 0x93 / 0x1E8 (3E2AC / 3E380): the D9 spawn with record flag +0x14 = 0 / 2.
- 0x3E380/0x1E8: 2 = append at the tail).
- r607: ASL 0x93 / 0x1E8 (3E2AC / 3E380 = the D9 spawn with constructor record flag +0x14 = 0 / 2): the list insertion of 346B0
- Wrappers: 3E2AC stores half 0, 3E314 half 1, 3E380 half 2 at sp+44 (= record+0x14);
- r607: 0x93 / 0x1E8 (3E2AC / 3E380) are the same spawn with record flag 0 / 2 (list head / tail);

## 0x1E9 `begin_filtered_actor_iterator`

Handler `0x401E4`, extra words: 0.

- 0x1E9/0x1EA (0x401E4/0x40210) are 0x189/0x18A with 0x4009C(1): the A0 0x18000 and 0x880 candidate filter.

## 0x1EA `advance_filtered_actor_iterator`

Handler `0x40210`, extra words: 0.

- 0x1E9/0x1EA (0x401E4/0x40210) are 0x189/0x18A with 0x4009C(1): the A0 0x18000 and 0x880 candidate filter.

## 0x1EC `open_save_screen`

Handler `0x41F88`, extra words: 0.

- 0x1EC (0x41F88) is NOT a level exit: it is the shared "health ran out" script (word 199 of the same script in 15 levels) that opens the in-game menu in game-over mode: 0x82420 episode/level == 1/9 -> progression slot marks + 0x339F8;
- 0x1EC research (2026-11-01): after 41F88 sets 77610 := 2, the main frame driver 27028 (mode 75F8 == 3, control == 2) runs 0x318B8 every frame instead of the process step: a 35-state machine (state word 0x7C7F0, jump table 0x763EC, code 0x318B8..0x33694 ~7.5 KB) that draws strings (1A044, table *0x7D350, e.g.
- Save/load step 4: ASL 0x1EC (41F88) is PORTED (native-save-screen.h: 339F8 duplicate native_progress_summary_339f8, hub marks when primary[1..2] == 1/9, E84 := 0, 77610 := 2, 2FF90 hybrid = option bytes primary[0x52..0x54] copied into the backup, 267BC E8C, 30C54 resets).
- r607: ASL 0x1EC (0x41F88), the save point opening the save screen in game:
- r607: the in-game save screen opened by ASL 0x1EC (native-save-menu.h);
- r607: ASL 0x1EC, same canonical-progress transaction shape as 172 (raw synced first, observed after).

## 0x1ED `transition_base_animation`

Handler `0x4183C`, extra words: 0.

- Full-body previous-clip context from opcode1ED/4183C.

## 0x1EE `draw_left_aligned_inline_scene_text`

Handler `0x40858`, extra words: 1.

- 0x1EE (0x40858 label at anchor x: NativeWorldLabel::left_aligned) and 0x208 (0x40A60 string empty: n <= 0 -> 4096, else string (n>>12)-1 after the 406D8 '#'/'$' prefixes, first glyph 0/10 -> 4096 else 0;
- r607: ASL 0x1EE (0x40858) draws at x
- r607: set only during left() (ASL 0x1EE)
- plus 0x1EE (0x40858) operand handling.
- r607: ASL 0x1EE (0x40858): the 0x1B3 draw at anchor x (appended ABI)

## 0x1EF `draw_right_aligned_inline_scene_text`

Handler `0x40928`, extra words: 1.

- 0x1EF (0x40928 = 0x1B3 drawn at anchor x - full width): NativeWorldLabel::right_aligned + LabelStage::right;
- r607: ASL 0x1EF (0x40928) draws at x - width;
- r607: set only during right() (ASL 0x1EF)
- r607: ASL 0x1EF (0x40928) through the native VM: the inline word is the string index handed to the right-aligned label service,
- (0x40928 = 0x40750 with x - width instead of x - width/2.)
- r607: 0x40928: inline string index, 406D8 string, drawn at anchor x - width (not width/2), then anchor reset (406C0).

## 0x1F0 `draw_left_aligned_stack_scene_text`

Handler `0x408BC`, extra words: 0.

- Item 183: ops 0x1F0 (0x408BC) / 0x1F1 (0x4099C) = left/right aligned text from a stack word (id = (word>>12)-1), same services as 0x1EE/0x1EF.
- r607 item 183: 0x408BC / 0x4099C = 0x1EE / 0x1EF with the string number POPPED: (word SRA 12) - 1 (as 0x1E1 / 0x407D0),

## 0x1F1 `draw_right_aligned_stack_scene_text`

Handler `0x4099C`, extra words: 0.

- Item 183: ops 0x1F0 (0x408BC) / 0x1F1 (0x4099C) = left/right aligned text from a stack word (id = (word>>12)-1), same services as 0x1EE/0x1EF.
- r607 item 183: 0x408BC / 0x4099C = 0x1EE / 0x1EF with the string number POPPED: (word SRA 12) - 1 (as 0x1E1 / 0x407D0),

## 0x1F3 `allocate_particle_template`

Handler `0x4EC90`, extra words: 0.

- ASL 0x1F3 (0x4EC90), appended (ABI)

## 0x1F4 `filtered_broadcast_type8_event`

Handler `0x41C90`, extra words: 0.

- Source41A24/41AC8/41C90 enqueue only: matching type8+message increments

## 0x1F5 `search_waypoint_rectangle_xz`

Handler `0x3A81C`, extra words: 0.

- 1F5/3A81C -> 3A6A4: starting at the CURRENT waypoint (actor+0x1C), test the rectangle spanned by the waypoint and its link (NULL link wraps
- 0x3A81C pops z (top) then x, searches the waypoint rectangles (3A6A4) and pushes 4096 / 0.

## 0x1F6 `signed_integer_remainder`

Handler `0x41F20`, extra words: 0.


## 0x1F7 `notify_actor_e0`

Handler `0x42148`, extra words: 0.

- Its type-4 trigger handler (word 10: field 169 = 1 -> progress_bit_write(L0, 1), global 61 learned bits) can only fire via the 0x04000000 event (ASL 0x1F7 notify_actor_e0 / pair contact).
- 0x42148: the popped actor gets +0xE0 = the CALLER and +0x9C |= 0x04000000.
- ASL 0x1F7 (0x42148): target+0xE0 = caller, target+0x9C |= 0x04000000 (appended ABI)

## 0x1F8 `load_story_book`

Handler `0x42178`, extra words: 0.


## 0x1F9 `actor_has_type8_trigger`

Handler `0x41E6C`, extra words: 0.


## 0x1FA `store_scene_texture_relative_word`

Handler `0x309BC`, extra words: 0.

- Whole valid1FA/309BC path.

## 0x1FB `random_other_index_q12`

Handler `0x3B458`, extra words: 0.

- Original1FB/3B458 unsigned Q12 index step.

## 0x1FC `remap_model_texture_faces`

Handler `0x42270`, extra words: 0.

- Item 212: 0x1FC (0x42270) with +C8 NULL (no 0x54 ran;
- Build initial34E64/42270 resource owner from THIS loaded immutable source.
- ASL 0x1FC: the quantum stages a copy-on-write ModelTextureOverlay plus the 0x7B5B4 journal counter;
- 0x42270 then reads the model header words +0x58/+0x54 at
- callback80, three 42270, BC B2, body yield and normal tail.
- Original 36EC4 clears yield2, then the SAME three 42270 operations run,

## 0x201 `request_scene_transition`

Handler `0x376BC`, extra words: 0.


## 0x202 `project_world_text_anchor`

Handler `0x40AE0`, extra words: 0.


## 0x203 `story_book_close`

Handler `0x421B4`, extra words: 0.

- 0x203 (0x421B4 -> 0x1437C): close the story book (only while busy 78EAC == 0): native_story_close;
- r607: source 0x1437C (ASL 0x203, close the book on chapter n): only while busy 78EAC (signed half) == 0: n % 100 == 0 -> 78EB7 := 1;
- 0x203 (0x421B4 -> 0x1437C book close, 14450 MoveImage leaf) by the ORIGINAL interpreter vs the native VM + native helpers.
- r607: ASL 0x203 (0x421B4 -> 0x1437C) close the book on chapter n (appended ABI)

## 0x205 `clamp_to_waypoint_rectangles`

Handler `0x3A9E4`, extra words: 0.

- 205/3A9E4 scans PAIRS: after each outside rectangle, actor1C := next.next
- 205/3A9E4 paired rectangles

## 0x206 `read_string_voice_id`

Handler `0x39090`, extra words: 1.

- when its string has the '#' voice prefix (0x52580, the same parse as ASL 0x206) the start
- 0x39090: string index = operand word;
- Opcode 0x206 (source 0x39090): operand word = scene string index;

## 0x207 `set_target_actor_bytes_158_15b`

Handler `0x3BC90`, extra words: 0.

- 0x207 (0x3BC90 = 0x11D bytes on a POPPED actor;
- r607: 0x3BC90 writes the target's pool bytes only (no typed alias), exactly like 0x11D on the executing actor.
- r607: ASL 0x207 (0x3BC90: target actor +158/+159/+15A := popped >> 12 bytes, +15B := 1) by the ORIGINAL interpreter vs the native VM.
- r607: ASL 0x207 (0x3BC90): the 0x11D byte store (+158/+159/+15A, +15B := 1) on the POPPED actor (appended ABI)

## 0x208 `scene_string_is_empty`

Handler `0x40A60`, extra words: 0.

- 0x1EE (0x40858 label at anchor x: NativeWorldLabel::left_aligned) and 0x208 (0x40A60 string empty: n <= 0 -> 4096, else string (n>>12)-1 after the 406D8 '#'/'$' prefixes, first glyph 0/10 -> 4096 else 0;
- r607: ASL 0x208 (0x40A60): after the 406D8 prefixes, a string whose first glyph is 0 or 10 counts as empty (4096), else 0.
- r607: ASL 0x208 (0x40A60 scene string emptiness, via 0x406D8 prefixes and 0x52580) — native_world_label_empty + the VM operand path
- r607: 0x40A60: n <= 0 -> 4096 without a string read;
- r607: ASL 0x208 (0x40A60) string emptiness (appended ABI)

