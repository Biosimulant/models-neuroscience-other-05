# Space Plan - neuroscience-general-combo-0040

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-kinness-a-modular-framework-for-computational-ne-113939-model, neuroscience-other-laminar-analysis-of-excitatory-circuits-in-vibri-137743-model, neuroscience-other-laminar-connectivity-matrix-simulation-weiler-et-114655-model

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
