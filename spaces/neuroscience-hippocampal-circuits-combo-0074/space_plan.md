# Space Plan - neuroscience-hippocampal-circuits-combo-0074

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-long-time-windows-from-theta-modulated-inhib-in-181967-model, neuroscience-other-ltp-in-cerebellar-mossy-fiber-granule-cell-synap-51196-model, neuroscience-other-mec-layer-ii-stellate-cell-synaptic-mechanisms-o-150239-model, neuroscience-other-model-of-long-range-transmission-of-gamma-oscill-137505-model

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
