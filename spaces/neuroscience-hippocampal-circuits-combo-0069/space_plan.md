# Space Plan - neuroscience-hippocampal-circuits-combo-0069

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-hippocampus-ca1-temporal-sensitivity-of-signalin-125733-model, neuroscience-other-hippocampus3ddemo-hippocampus3ddemo-model, neuroscience-other-ih-tunes-oscillations-in-an-in-silico-ca3-model-151282-model, neuroscience-other-impact-of-dendritic-atrophy-on-intrinsic-and-syn-147867-model

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
