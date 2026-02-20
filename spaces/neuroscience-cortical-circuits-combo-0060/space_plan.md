# Space Plan - neuroscience-cortical-circuits-combo-0060

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-kv4-3-kv1-4-encoded-k-channel-in-heart-cells-and-62654-model, neuroscience-other-kv4-3-kv1-4-encoded-k-channel-in-heart-cells-gre-62287-model, neuroscience-other-l23pyramidalcelltutorial-l23pyramidalcelltutorial-model, neuroscience-other-l5-pfc-microcircuit-used-to-study-persistent-act-155057-model

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
