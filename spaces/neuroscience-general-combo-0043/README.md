# COMBO_0043 - Neuroscience General

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
- `neuroscience-other-lobster-stg-pyloric-network-model-with-calcium-s-144387-model`: Neuroscience: LobsterStgPyloricNetworkModelWithCalciumS144387Model
- `neuroscience-other-long-term-adaptation-with-power-law-dynamics-zil-125855-model`: Neuroscience: LongTermAdaptationWithPowerLawDynamicsZil125855Model
- `neuroscience-other-loss-of-phase-locking-in-non-weakly-coupled-inhi-118799-model`: Neuroscience: LossOfPhaseLockingInNonWeaklyCoupledInhi118799Model

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
- neuroscience-other-lobster-stg-pyloric-network-model-with-calcium-s-144387-model :: modeldb:144387 :: https://modeldb.science/144387
- neuroscience-other-long-term-adaptation-with-power-law-dynamics-zil-125855-model :: modeldb:125855 :: https://modeldb.science/125855
- neuroscience-other-loss-of-phase-locking-in-non-weakly-coupled-inhi-118799-model :: modeldb:118799 :: https://modeldb.science/118799

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
