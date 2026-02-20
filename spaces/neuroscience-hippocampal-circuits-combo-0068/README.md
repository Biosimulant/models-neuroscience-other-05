# COMBO_0068 - Neuroscience Hippocampal Circuits

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
- `neuroscience-other-hippocampal-basket-cell-gap-junction-network-dyn-114047-model`: Neuroscience: HippocampalBasketCellGapJunctionNetworkDyn114047Model
- `neuroscience-other-hippocampal-ca3-network-and-circadian-regulation-142104-model`: Neuroscience: HippocampalCa3NetworkAndCircadianRegulation142104Model
- `neuroscience-other-hippocampal-context-dependent-retrieval-hasselmo-83516-model`: Neuroscience: HippocampalContextDependentRetrievalHasselmo83516Model
- `neuroscience-other-hippocampus-ca1-simulations-of-ltp-signaling-pat-139655-model`: Neuroscience: HippocampusCa1SimulationsOfLtpSignalingPat139655Model

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
- neuroscience-other-hippocampal-basket-cell-gap-junction-network-dyn-114047-model :: modeldb:114047 :: https://modeldb.science/114047
- neuroscience-other-hippocampal-ca3-network-and-circadian-regulation-142104-model :: modeldb:142104 :: https://modeldb.science/142104
- neuroscience-other-hippocampal-context-dependent-retrieval-hasselmo-83516-model :: modeldb:83516 :: https://modeldb.science/83516
- neuroscience-other-hippocampus-ca1-simulations-of-ltp-signaling-pat-139655-model :: modeldb:139655 :: https://modeldb.science/139655

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
