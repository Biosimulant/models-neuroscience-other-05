# COMBO_0031 - Neuroscience General

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
- `neuroscience-other-human-attentional-networks-a-connectionist-model-115813-model`: Neuroscience: HumanAttentionalNetworksAConnectionistModel115813Model
- `neuroscience-other-hyperconnectivity-slow-synapses-in-pfc-mental-re-140033-model`: Neuroscience: HyperconnectivitySlowSynapsesInPfcMentalRe140033Model
- `neuroscience-other-hypocretin-and-locus-coeruleus-model-neurons-car-145162-model`: Neuroscience: HypocretinAndLocusCoeruleusModelNeuronsCar145162Model

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
- neuroscience-other-human-attentional-networks-a-connectionist-model-115813-model :: modeldb:115813 :: https://modeldb.science/115813
- neuroscience-other-hyperconnectivity-slow-synapses-in-pfc-mental-re-140033-model :: modeldb:140033 :: https://modeldb.science/140033
- neuroscience-other-hypocretin-and-locus-coeruleus-model-neurons-car-145162-model :: modeldb:145162 :: https://modeldb.science/145162

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
