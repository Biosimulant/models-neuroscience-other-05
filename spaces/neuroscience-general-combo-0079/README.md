# COMBO_0079 - Neuroscience General

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
- `neuroscience-other-ell-pyramidal-neuron-simmonds-and-chacron-2014-168590-model`: Neuroscience: EllPyramidalNeuronSimmondsAndChacron2014168590Model
- `neuroscience-other-encoding-and-discrimination-of-vowel-like-sounds-126371-model`: Neuroscience: EncodingAndDiscriminationOfVowelLikeSounds126371Model
- `neuroscience-other-endothelin-action-on-pituitary-latotrophs-bertra-91899-model`: Neuroscience: EndothelinActionOnPituitaryLatotrophsBertra91899Model
- `neuroscience-other-evaluation-of-stochastic-diff-eq-approximation-o-118195-model`: Neuroscience: EvaluationOfStochasticDiffEqApproximationO118195Model

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
- neuroscience-other-ell-pyramidal-neuron-simmonds-and-chacron-2014-168590-model :: modeldb:168590 :: https://modeldb.science/168590
- neuroscience-other-encoding-and-discrimination-of-vowel-like-sounds-126371-model :: modeldb:126371 :: https://modeldb.science/126371
- neuroscience-other-endothelin-action-on-pituitary-latotrophs-bertra-91899-model :: modeldb:91899 :: https://modeldb.science/91899
- neuroscience-other-evaluation-of-stochastic-diff-eq-approximation-o-118195-model :: modeldb:118195 :: https://modeldb.science/118195

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
