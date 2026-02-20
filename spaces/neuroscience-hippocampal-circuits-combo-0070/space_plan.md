# Space Plan - neuroscience-hippocampal-circuits-combo-0070

## Scientific Scope
- Domain: neuroscience
- Theme: hippocampal_circuits
- Base models: neuroscience-other-ionic-mechanisms-of-bursting-in-ca3-pyramidal-ne-114337-model, neuroscience-other-ketamine-disrupts-theta-modulation-of-gamma-in-a-139421-model, neuroscience-other-linear-vs-non-linear-integration-in-ca1-oblique-144450-model, neuroscience-other-long-time-windows-from-theta-modulated-inhib-in-181967-model

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
