# COMBO_0076 - Neuroscience Synaptic Plasticity

## Scientific Question
How do synaptic changes influence network-level outcomes?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-lgncircuit-minimal-lgn-network-model-of-temporal-153092-model`: Neuroscience: LgncircuitMinimalLgnNetworkModelOfTemporal153092Model
- `neuroscience-other-local-variable-time-step-method-lytton-hines-200-33975-model`: Neuroscience: LocalVariableTimeStepMethodLyttonHines20033975Model
- `neuroscience-other-model-of-working-memory-based-on-negative-deriva-181010-model`: Neuroscience: ModelOfWorkingMemoryBasedOnNegativeDeriva181010Model
- `neuroscience-other-modeling-hebbian-and-homeostatic-plasticity-toyo-180791-model`: Neuroscience: ModelingHebbianAndHomeostaticPlasticityToyo180791Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- neuroscience-other-lgncircuit-minimal-lgn-network-model-of-temporal-153092-model :: modeldb:153092 :: https://modeldb.science/153092
- neuroscience-other-local-variable-time-step-method-lytton-hines-200-33975-model :: modeldb:33975 :: https://modeldb.science/33975
- neuroscience-other-model-of-working-memory-based-on-negative-deriva-181010-model :: modeldb:181010 :: https://modeldb.science/181010
- neuroscience-other-modeling-hebbian-and-homeostatic-plasticity-toyo-180791-model :: modeldb:180791 :: https://modeldb.science/180791

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
