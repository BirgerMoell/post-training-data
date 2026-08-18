# Contributing

Keep entries useful to someone preparing a training run. Prefer concrete locations, revisions, commands, and limitations over general descriptions.

## Add a dataset

1. Copy `datasets/_template/README.md` to `datasets/<short-name>/README.md`.
2. Fill in the metadata block and the five short sections.
3. Run `python3 scripts/build_indexes.py`.
4. Run `python3 scripts/build_indexes.py --check`.
5. Open a pull request.

## Update a dataset

Update its page when any of these change:

- a public or LUMI location is added, moved, or removed;
- a dataset is used in a completed run;
- licensing or access information becomes clearer;
- a canonical revision, split, or artifact is selected;
- a quality, contamination, or privacy check is completed;
- a candidate is deprecated or becomes production-ready.

## State vocabulary

Use one of these `status_key` values:

- `used-in-completed-run`
- `used-in-research`
- `published`
- `configured-runnable`
- `staged`
- `candidate`
- `planned`
- `supporting`
- `needs-verification`
- `historical`
- `eval-only`

“Used” should point to evidence of the run. “Staged” means that a concrete artifact location is known. “Published” means that other people can obtain it. These states are independent of quality or legal approval, which must be described on the page.

## Locations

- Link public data directly.
- Put LUMI and other filesystem paths in backticks.
- Never commit credentials or signed download URLs.
- Record the date on which a location was last verified.
- If an artifact exists in a personal directory, identify the responsible owner and the intended shared destination.

