# Space Plan - neuroscience-hippocampal-circuits-combo-0066

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-fergusonetal2013-pvfastfiringcell-fergusonetal2013pvfastfiringcell-model, neuroscience-other-fergusonetal2014-ca1pyrcell-fergusonetal2014ca1pyrcell-model, neuroscience-other-ferrante2009-dentategyrusgranulecell-ferrante2009dentategyrusgranulecell-model, neuroscience-other-functional-impact-of-dendritic-branch-point-morp-146509-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
