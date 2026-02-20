# COMBO_0071 - Neuroscience Basal Ganglia Dopamine

## Scientific Question
How do basal ganglia dopamine mechanisms compare across these models?

## Biological Context
Neuronal dynamics, network signaling, and emergent circuit behavior.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `neuroscience-other-erg-current-in-repolarizing-plateau-potentials-i-100603-model`: Neuroscience: ErgCurrentInRepolarizingPlateauPotentialsI100603Model
- `neuroscience-other-fs-striatal-interneuron-k-currents-solve-signal-79465-model`: Neuroscience: FsStriatalInterneuronKCurrentsSolveSignal79465Model
- `neuroscience-other-gap-junction-coupled-network-of-striatal-fast-sp-118389-model`: Neuroscience: GapJunctionCoupledNetworkOfStriatalFastSp118389Model
- `neuroscience-other-globus-pallidus-multi-compartmental-model-neuron-114639-model`: Neuroscience: GlobusPallidusMultiCompartmentalModelNeuron114639Model

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
- neuroscience-other-erg-current-in-repolarizing-plateau-potentials-i-100603-model :: modeldb:100603 :: https://modeldb.science/100603
- neuroscience-other-fs-striatal-interneuron-k-currents-solve-signal-79465-model :: modeldb:79465 :: https://modeldb.science/79465
- neuroscience-other-gap-junction-coupled-network-of-striatal-fast-sp-118389-model :: modeldb:118389 :: https://modeldb.science/118389
- neuroscience-other-globus-pallidus-multi-compartmental-model-neuron-114639-model :: modeldb:114639 :: https://modeldb.science/114639

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
