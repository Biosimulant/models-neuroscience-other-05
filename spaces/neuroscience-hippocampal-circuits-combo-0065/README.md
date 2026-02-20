# COMBO_0065 - Neuroscience Hippocampal Circuits

## Scientific Question
How do recurrent hippocampal motifs shape network dynamics over time?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-encoding-and-retrieval-in-a-model-of-the-hippoca-123815-model`: Neuroscience: EncodingAndRetrievalInAModelOfTheHippoca123815Model
- `neuroscience-other-epilepsy-may-be-caused-by-very-small-functional-124392-model`: Neuroscience: EpilepsyMayBeCausedByVerySmallFunctional124392Model
- `neuroscience-other-excitability-of-the-soma-in-central-nervous-syst-62266-model`: Neuroscience: ExcitabilityOfTheSomaInCentralNervousSyst62266Model
- `neuroscience-other-fast-sodium-channel-gating-in-mossy-fiber-axons-128079-model`: Neuroscience: FastSodiumChannelGatingInMossyFiberAxons128079Model

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
- neuroscience-other-encoding-and-retrieval-in-a-model-of-the-hippoca-123815-model :: modeldb:123815 :: https://modeldb.science/123815
- neuroscience-other-epilepsy-may-be-caused-by-very-small-functional-124392-model :: modeldb:124392 :: https://modeldb.science/124392
- neuroscience-other-excitability-of-the-soma-in-central-nervous-syst-62266-model :: modeldb:62266 :: https://modeldb.science/62266
- neuroscience-other-fast-sodium-channel-gating-in-mossy-fiber-axons-128079-model :: modeldb:128079 :: https://modeldb.science/128079

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
