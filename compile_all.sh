#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "$0")" && pwd)
cd "$ROOT_DIR"

OUT_DIR="$ROOT_DIR/media/math"
BUILD_DIR="$ROOT_DIR/media/_manim_build"
MANIM_QUALITY="${MANIM_QUALITY:--pqh}"

mkdir -p "$OUT_DIR"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

if command -v manim >/dev/null 2>&1; then
  MANIM=(manim)
elif command -v python3 >/dev/null 2>&1; then
  MANIM=(python3 -m manim)
else
  MANIM=(python -m manim)
fi

render_one() {
  local dir=$1
  local scene=$2
  local file="math/${dir}/main.py"
  local tmp_dir="${BUILD_DIR}/${dir}"

  echo "Rendering ${dir} (${scene}) ..."
  mkdir -p "$tmp_dir"

  "${MANIM[@]}" "$MANIM_QUALITY" --media_dir "$tmp_dir" "$file" "$scene"

  local video
  video=$(find "$tmp_dir" -type f -name '*.mp4' -print -quit)
  if [[ -z "$video" ]]; then
    echo "No mp4 produced for ${dir}" >&2
    exit 1
  fi

  cp "$video" "${OUT_DIR}/${dir}.mp4"
  echo "Saved: media/math/${dir}.mp4"
}

render_one perfect_square PerfectSquareFormula
render_one difference_of_squares DifferenceOfSquares
render_one distributive_law DistributiveLaw
render_one associative_law AssociativeLaw

echo "All videos compiled to ${OUT_DIR}"
