# Space Plan - neuroscience-hippocampal-circuits-combo-0068

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-hippocampal-basket-cell-gap-junction-network-dyn-114047-model, neuroscience-other-hippocampal-ca3-network-and-circadian-regulation-142104-model, neuroscience-other-hippocampal-context-dependent-retrieval-hasselmo-83516-model, neuroscience-other-hippocampus-ca1-simulations-of-ltp-signaling-pat-139655-model

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
