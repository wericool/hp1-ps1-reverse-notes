#!/bin/bash
# r607: regenerates the numeric part of PROGRESS.md (function / opcode / level coverage). Static only, no probe run.
cd "$(dirname "$0")/.." || exit 1  # needs the port sources (full-src/) and an asm dump (ASM=...)
ASM=${ASM:-/tmp/all.asm}
grep -o "jal func_[0-9A-F]*" "$ASM" | sed 's/jal func_000//' | tr 'A-F' 'a-f' | sort -u > progress-funcs.txt
cat full-src/*.h full-src/*.cpp native-pc-session.cpp | grep -oiE "(0x)?[0-9a-f]{5}\b" | sed 's/^0x//I' | tr 'A-F' 'a-f' | sort -u > progress-named.txt
comm -12 progress-funcs.txt progress-named.txt > progress-done.txt
SDK=5b2b0 # r607: first Sony PSY-Q library function (LIBSN __main); everything below is the game's own code (linker order)
echo "| Address range | Contents | Named in the port | Total called | % |"
echo "|---|---|---|---|---|"
for b in 1 2 3 4 5; do lo=${b}0000; hi=$( [ $b = 5 ] && echo $SDK || echo $((b+1))0000 )
  t=$(awk -v lo=$lo -v hi=$hi '$1>=lo && $1<hi' progress-funcs.txt | wc -l); d=$(awk -v lo=$lo -v hi=$hi '$1>=lo && $1<hi' progress-done.txt | wc -l)
  case $b in 1) c="main loop, modes, pad";; 2) c="front end, menus, camera, fades";; 3) c="actors, ASL VM core";; 4) c="ASL ops, sound managers, text";; 5) c="text windows, render, misc";; esac
  echo "| 0x$lo-0x$hi | $c | $d | $t | $((100*d/t))% |"; done
t=$(awk -v s=$SDK '$1<s' progress-funcs.txt | wc -l); d=$(awk -v s=$SDK '$1<s' progress-done.txt | wc -l)
echo "| **game code total** | | **$d** | **$t** | **$((100*d/t))%** |"
st=$(awk -v s=$SDK '$1>=s' progress-funcs.txt | wc -l); si=$(cut -d' ' -f1 psyq-sdk-functions.txt | sort -u | comm -12 progress-funcs.txt - | wc -l)
echo "| 0x$SDK+ | Sony PSY-Q SDK (identified by signature: $si) | replaced natively | $st | n/a |"
awk -v s=$SDK '$1<s' progress-funcs.txt | comm -23 - progress-done.txt > progress-todo.txt
echo; echo "Game functions not yet named in the port: $(wc -l < progress-todo.txt) (list: progress-todo.txt)"
echo
head -1 opcode-coverage-218.txt | sed 's/^/ASL opcodes: /'
tail -1 gate-oracle.txt | sed 's/^/Gate oracle: /'
f=$(ls -t level-smoke[0-9]*.txt | head -1); echo "Level smoke ($f): $(grep -c 'exit=0' $f) / $(grep -c 'exit=' $f) story WADs run 300 frames from a save"
