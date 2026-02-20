# COMBO_0032 - Neuroscience General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-hysteresis-in-voltage-gating-of-hcn-channels-eli-82758-model`: Neuroscience: HysteresisInVoltageGatingOfHcnChannelsEli82758Model
- `neuroscience-other-ia-and-it-interact-to-set-first-spike-latency-mo-59479-model`: Neuroscience: IaAndItInteractToSetFirstSpikeLatencyMo59479Model
- `neuroscience-other-iandf-recurrent-networks-with-current-or-conduct-152539-model`: Neuroscience: IandfRecurrentNetworksWithCurrentOrConduct152539Model

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
- neuroscience-other-hysteresis-in-voltage-gating-of-hcn-channels-eli-82758-model :: modeldb:82758 :: https://modeldb.science/82758
- neuroscience-other-ia-and-it-interact-to-set-first-spike-latency-mo-59479-model :: modeldb:59479 :: https://modeldb.science/59479
- neuroscience-other-iandf-recurrent-networks-with-current-or-conduct-152539-model :: modeldb:152539 :: https://modeldb.science/152539

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
