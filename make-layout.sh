#!/bin/bash
asciiart -w 55 -i pi-circle.png | grep -v '^W:'  | grep -v '^[+]' | sed 's/[|^%]/ /g' | sed 's/[^ ]/*/g' > layout-tmp.txt
{
  echo `wc -l < layout-tmp.txt`
  cat layout-tmp.txt
} > layout.txt
rm layout-tmp.txt
# python layout_code.py < layout.txt
