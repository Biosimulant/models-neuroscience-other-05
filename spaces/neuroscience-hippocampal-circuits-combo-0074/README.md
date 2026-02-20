# COMBO_0074 - Neuroscience Hippocampal Circuits

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
- `neuroscience-other-long-time-windows-from-theta-modulated-inhib-in-181967-model`: Neuroscience: LongTimeWindowsFromThetaModulatedInhibIn181967Model
- `neuroscience-other-ltp-in-cerebellar-mossy-fiber-granule-cell-synap-51196-model`: Neuroscience: LtpInCerebellarMossyFiberGranuleCellSynap51196Model
- `neuroscience-other-mec-layer-ii-stellate-cell-synaptic-mechanisms-o-150239-model`: Neuroscience: MecLayerIiStellateCellSynapticMechanismsO150239Model
- `neuroscience-other-model-of-long-range-transmission-of-gamma-oscill-137505-model`: Neuroscience: ModelOfLongRangeTransmissionOfGammaOscill137505Model

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
- neuroscience-other-long-time-windows-from-theta-modulated-inhib-in-181967-model :: modeldb:181967 :: https://modeldb.science/181967
- neuroscience-other-ltp-in-cerebellar-mossy-fiber-granule-cell-synap-51196-model :: modeldb:51196 :: https://modeldb.science/51196
- neuroscience-other-mec-layer-ii-stellate-cell-synaptic-mechanisms-o-150239-model :: modeldb:150239 :: https://modeldb.science/150239
- neuroscience-other-model-of-long-range-transmission-of-gamma-oscill-137505-model :: modeldb:137505 :: https://modeldb.science/137505

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
