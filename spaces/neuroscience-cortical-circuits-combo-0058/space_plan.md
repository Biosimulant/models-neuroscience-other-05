# Space Plan - neuroscience-cortical-circuits-combo-0058

## Scientific Scope
- Domain: neuroscience
- Theme: cortical_circuits
- Base models: neuroscience-other-inhibitory-control-by-an-integral-feedback-signa-62268-model, neuroscience-other-inhibitory-plasticity-balances-excitation-and-in-143751-model, neuroscience-other-input-fluctuations-effects-on-f-i-curves-arsiero-83590-model, neuroscience-other-intracortical-synaptic-potential-modulation-by-p-135787-model

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
