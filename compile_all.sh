#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

QUALITY="${MANIM_QUALITY:--qh}"
OUT_DIR="$ROOT_DIR/media/math"
BUILD_DIR="$ROOT_DIR/.manim_build_tmp"

SCENES=(
  "math/perfect_square:PerfectSquareFormula:perfect_square"
  "math/difference_of_squares:DifferenceOfSquares:difference_of_squares"
  "math/distributive_law:DistributiveLaw:distributive_law"
  "math/associative_law:AssociativeLaw:associative_law"
)

mkdir -p "$OUT_DIR"
rm -rf "$BUILD_DIR"
cleanup() {
  rm -rf "$BUILD_DIR"
}
trap cleanup EXIT

for item in "${SCENES[@]}"; do
  IFS=':' read -r dir scene name <<< "$item"

  rm -rf "$BUILD_DIR"
  mkdir -p "$BUILD_DIR"

  echo "Compiling $scene from $dir/main.py ..."
  manim "$QUALITY" --media_dir "$BUILD_DIR" "$dir/main.py" "$scene"

  src="$(find "$BUILD_DIR" -type f -name "${scene}.mp4" -print -quit)"
  if [[ -z "$src" ]]; then
    echo "Error: output video for $scene not found" >&2
    exit 1
  fi

  cp "$src" "$OUT_DIR/${name}.mp4"
  echo "Saved $OUT_DIR/${name}.mp4"
  rm -rf "$BUILD_DIR"
done

echo "Cleaning intermediate files..."
find "$OUT_DIR" -mindepth 1 -maxdepth 1 ! -name '*.mp4' -exec rm -rf {} +
find "$ROOT_DIR/media" -mindepth 1 -maxdepth 1 ! -name 'math' -exec rm -rf {} +
find "$ROOT_DIR" -type d -name '__pycache__' -prune -exec rm -rf {} +
find "$ROOT_DIR" -type f -name '*.pyc' -delete
rm -rf "$BUILD_DIR"

echo "Done. Final videos are in $OUT_DIR"
