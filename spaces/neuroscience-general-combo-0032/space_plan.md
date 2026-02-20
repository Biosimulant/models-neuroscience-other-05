# Space Plan - neuroscience-general-combo-0032

## Scientific Scope
- Domain: neuroscience
- Theme: general
- Base models: neuroscience-other-hysteresis-in-voltage-gating-of-hcn-channels-eli-82758-model, neuroscience-other-ia-and-it-interact-to-set-first-spike-latency-mo-59479-model, neuroscience-other-iandf-recurrent-networks-with-current-or-conduct-152539-model

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
