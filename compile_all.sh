#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$ROOT_DIR"

QUALITY=${MANIM_QUALITY:-qh}
if [[ $QUALITY == -* ]]; then
  QUALITY_FLAG=$QUALITY
else
  QUALITY_FLAG=-$QUALITY
fi

OUT_DIR=$ROOT_DIR/media/math
BUILD_DIR=$ROOT_DIR/.manim_build/math
MATH_SCENES=(PerfectSquareFormula DifferenceOfSquares DistributiveLaw AssociativeLaw)

mkdir -p "$OUT_DIR"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

cleanup() {
  rm -rf "$BUILD_DIR"

  find "$OUT_DIR" -type d -name partial_movie_files -prune -exec rm -rf {} + 2>/dev/null || true
  for scene in "${MATH_SCENES[@]}"; do
    find "$ROOT_DIR/media" -type d -path "*/partial_movie_files/${scene}" -prune -exec rm -rf {} + 2>/dev/null || true
  done
  find "$ROOT_DIR/media" -type d -name partial_movie_files -empty -delete 2>/dev/null || true

  find "$ROOT_DIR/math" -type d -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null || true
  find "$ROOT_DIR/math" -type f -name '*.pyc' -delete 2>/dev/null || true
}
trap cleanup EXIT

scenes=(
  'math/perfect_square/main.py|PerfectSquareFormula|perfect_square'
  'math/difference_of_squares/main.py|DifferenceOfSquares|difference_of_squares'
  'math/distributive_law/main.py|DistributiveLaw|distributive_law'
  'math/associative_law/main.py|AssociativeLaw|associative_law'
)

for item in "${scenes[@]}"; do
  IFS='|' read -r src scene output <<< "$item"
  echo "==> Compiling ${src} (${scene})"
  manim "$QUALITY_FLAG" --media_dir "$BUILD_DIR" "$src" "$scene"
  mp4=$(find "$BUILD_DIR" -type f -name "${scene}.mp4" -print -quit)
  if [[ -z $mp4 ]]; then
    echo "Error: cannot find output for ${scene}" >&2
    exit 1
  fi
  cp "$mp4" "$OUT_DIR/${output}.mp4"
done

echo "Done. Videos written to ${OUT_DIR}"
