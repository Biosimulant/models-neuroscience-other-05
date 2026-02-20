# COMBO_0066 - Neuroscience Hippocampal Circuits

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
- `neuroscience-other-fergusonetal2013-pvfastfiringcell-fergusonetal2013pvfastfiringcell-model`: Neuroscience: Fergusonetal2013PvfastfiringcellFergusonetal2013pvfastfiringcellModel
- `neuroscience-other-fergusonetal2014-ca1pyrcell-fergusonetal2014ca1pyrcell-model`: Neuroscience: Fergusonetal2014Ca1pyrcellFergusonetal2014ca1pyrcellModel
- `neuroscience-other-ferrante2009-dentategyrusgranulecell-ferrante2009dentategyrusgranulecell-model`: Neuroscience: Ferrante2009DentategyrusgranulecellFerrante2009dentategyrusgranulecellModel
- `neuroscience-other-functional-impact-of-dendritic-branch-point-morp-146509-model`: Neuroscience: FunctionalImpactOfDendriticBranchPointMorp146509Model

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
- neuroscience-other-fergusonetal2013-pvfastfiringcell-fergusonetal2013pvfastfiringcell-model :: opensourcebrain:FergusonEtAl2013-PVFastFiringCell :: https://github.com/OpenSourceBrain/FergusonEtAl2013-PVFastFiringCell
- neuroscience-other-fergusonetal2014-ca1pyrcell-fergusonetal2014ca1pyrcell-model :: opensourcebrain:FergusonEtAl2014-CA1PyrCell :: https://github.com/OpenSourceBrain/FergusonEtAl2014-CA1PyrCell
- neuroscience-other-ferrante2009-dentategyrusgranulecell-ferrante2009dentategyrusgranulecell-model :: opensourcebrain:Ferrante2009-DentateGyrusGranuleCell :: https://github.com/OpenSourceBrain/Ferrante2009-DentateGyrusGranuleCell
- neuroscience-other-functional-impact-of-dendritic-branch-point-morp-146509-model :: modeldb:146509 :: https://modeldb.science/146509

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
