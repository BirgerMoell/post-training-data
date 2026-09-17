#!/bin/bash
#SBATCH --job-name=dolci-dpo-data
#SBATCH --account=project_465002530
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=128G
#SBATCH --time=02:00:00
#SBATCH --output=/scratch/project_465002530/training/collection/post-training/2026q3/openeurollm-dolci-instruct-dpo-translated/counts/slurm-%j.out
#SBATCH --error=/scratch/project_465002530/training/collection/post-training/2026q3/openeurollm-dolci-instruct-dpo-translated/counts/slurm-%j.err

set -euo pipefail
umask 0007

REVISION=a57841a6bbabfed8ca2597438995c2991e5b73b7
DATASET_ROOT=/scratch/project_465002530/training/collection/post-training/2026q3/openeurollm-dolci-instruct-dpo-translated
SOURCE_DIR="$DATASET_ROOT/source/$REVISION"
RELEASE_ID="candidate-${REVISION:0:8}"
SCRIPT_DIR=${SCRIPT_DIR:?Set SCRIPT_DIR to the staged post-training-data/scripts directory}
SIF=/appl/local/laifs/containers/lumi-multitorch-u24r70f21m50t210-20260807_115122/lumi-multitorch-full-u24r70f21m50t210-20260807_115122.sif

mkdir -p "$DATASET_ROOT/counts"

srun singularity exec \
  -B /scratch/project_465002530:/scratch/project_465002530 \
  -B "$SCRIPT_DIR:$SCRIPT_DIR" \
  "$SIF" \
  python3 "$SCRIPT_DIR/materialize_preference_release.py" \
    --repo-id openeurollm/Dolci-Instruct-DPO-translated \
    --revision "$REVISION" \
    --source-dir "$SOURCE_DIR" \
    --release-dir "$DATASET_ROOT/release/$RELEASE_ID" \
    --quality-dir "$DATASET_ROOT/quality/$RELEASE_ID" \
    --counts-dir "$DATASET_ROOT/counts/$RELEASE_ID" \
    --languages cs de el en es fi fr it pl ro sv uk \
    --rows-per-shard 50000

chmod -R g+rwX "$DATASET_ROOT/release/$RELEASE_ID" \
  "$DATASET_ROOT/quality/$RELEASE_ID" \
  "$DATASET_ROOT/counts/$RELEASE_ID"
