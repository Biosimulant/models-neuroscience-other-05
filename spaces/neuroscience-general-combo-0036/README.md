# COMBO_0036 - Neuroscience General

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
- `neuroscience-other-integrate-and-fire-model-code-for-spike-based-co-126052-model`: Neuroscience: IntegrateAndFireModelCodeForSpikeBasedCo126052Model
- `neuroscience-other-interaural-time-difference-detection-by-slowly-i-150445-model`: Neuroscience: InterauralTimeDifferenceDetectionBySlowlyI150445Model
- `neuroscience-other-intrinsic-sensory-neurons-of-the-gut-chambers-et-155796-model`: Neuroscience: IntrinsicSensoryNeuronsOfTheGutChambersEt155796Model

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
- neuroscience-other-integrate-and-fire-model-code-for-spike-based-co-126052-model :: modeldb:126052 :: https://modeldb.science/126052
- neuroscience-other-interaural-time-difference-detection-by-slowly-i-150445-model :: modeldb:150445 :: https://modeldb.science/150445
- neuroscience-other-intrinsic-sensory-neurons-of-the-gut-chambers-et-155796-model :: modeldb:155796 :: https://modeldb.science/155796

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
