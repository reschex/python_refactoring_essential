!/usr/bin/env bash
  git add .
  pytest && git commit -m "It works!" || git reset --hard