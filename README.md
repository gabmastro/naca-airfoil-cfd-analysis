# NACA 2412 CFD Aerodynamic Analysis

**2D CFD analysis of a NACA 2412 airfoil using ANSYS Fluent**

This project presents a two-dimensional Computational Fluid Dynamics (CFD)
analysis of a NACA 2412 airfoil performed using ANSYS Fluent.

The project was developed as an independent study to gain practical experience
with the complete CFD workflow and to connect theoretical concepts from fluid
dynamics and aerodynamics with numerical simulation.

The analysis includes geometry preparation, mesh generation, near-wall
refinement, solver setup, convergence monitoring, aerodynamic force evaluation
and flow-field post-processing.

---

## Project Objectives

The main objectives of the project were to:

- Set up a complete external-aerodynamics CFD simulation in ANSYS Fluent
- Generate an appropriate computational mesh around an airfoil
- Apply local mesh refinement and inflation layers near the airfoil surface
- Define suitable boundary conditions and numerical models
- Monitor numerical convergence
- Calculate lift and drag coefficients
- Analyse pressure and velocity fields
- Visualise the flow using contours and pathlines
- Develop a better understanding of the relationship between flow structures
  and aerodynamic performance

---

## Software

The project was developed using:

- **ANSYS Workbench**
- **ANSYS Meshing**
- **ANSYS Fluent**

The results were subsequently analysed through Fluent post-processing and
aerodynamic coefficient monitoring.

---

## CFD Workflow

The general workflow followed throughout the project was:

**Airfoil Geometry → Computational Domain → Mesh → Boundary Conditions →  
Physical Models → Solver Setup → Convergence → Aerodynamic Coefficients →  
Flow-Field Analysis**

Each stage was progressively refined while checking the physical consistency
of the simulation.

---

# 1. Airfoil Geometry

The main configuration analysed in this project is the **NACA 2412** airfoil.

The NACA 2412 is a cambered four-digit NACA profile. Unlike a symmetric
airfoil, its camber allows it to generate lift even at zero geometric angle
of attack.

A two-dimensional representation of the airfoil was placed inside an external
fluid domain sufficiently large to model the surrounding airflow while
reducing the influence of the far-field boundaries on the solution.

---

# 2. Computational Mesh

Mesh generation was one of the main parts of the CFD setup.

The objective was to obtain sufficient resolution in the regions characterised
by the largest aerodynamic gradients without unnecessarily increasing the
overall computational cost.

Local refinement was applied around the airfoil, with particular attention to:

- Leading edge
- Trailing edge
- Airfoil surface
- Near-wall region
- Wake region

### Edge Sizing

Local edge sizing was used to increase the spatial resolution around the
airfoil geometry.

A finer discretisation is particularly important near the leading edge,
where the flow undergoes rapid acceleration and large pressure gradients.

### Inflation Layers

Inflation layers were generated along the airfoil surface to improve the
resolution of the near-wall flow.

This allows the mesh to better represent the strong velocity gradients
associated with the boundary layer.

The inflation setup was adjusted during the project to obtain a mesh suitable
for the final simulations.

> Detailed mesh settings and parameters are documented in the technical report.

---

# 3. Boundary Conditions and Solver Setup

The simulations were performed using **ANSYS Fluent**.

A pressure-based numerical solution procedure was used for the aerodynamic
analysis.

The external flow conditions were imposed through the boundaries of the
computational domain, while the airfoil surface was treated as a wall.

During the simulations, both residuals and aerodynamic force coefficients
were monitored.

Convergence was not assessed solely from the residual history: the stability
of the lift and drag coefficients was also considered when evaluating whether
the solution had reached a sufficiently stable state.

---

# 4. Baseline Check — NACA 0012

Before the final NACA 2412 analysis, a **NACA 0012** symmetric airfoil was
used as a baseline case.

At zero angle of attack, a symmetric NACA 0012 airfoil is expected to produce
approximately zero lift.

This provided a useful physical sanity check for the CFD setup before moving
to the cambered NACA 2412 geometry.

The NACA 0012 case is therefore treated as a preliminary validation of the
workflow rather than as the main result of the project.

---

# 5. NACA 2412 Analysis

The final analysis was performed using the **NACA 2412** airfoil.

Because of its asymmetric geometry and positive camber, the NACA 2412 produces
a non-zero lift coefficient even at zero geometric angle of attack.

After convergence, the final simulation produced:

| Parameter | Result |
|---|---:|
| Airfoil | NACA 2412 |
| Angle of attack | 0° |
| Lift coefficient, CL | **0.2174** |
| Drag coefficient, CD | **0.0100** |

These values represent the final converged NACA 2412 case obtained during
the project.

The positive lift coefficient at zero geometric angle of attack is consistent
with the expected aerodynamic behaviour of a cambered airfoil.

---

# 6. Convergence

Numerical convergence was monitored throughout the simulations.

Two complementary indicators were considered:

### Residuals

The evolution of the governing-equation residuals was monitored during the
iterative solution process.

### Aerodynamic Coefficients

Lift and drag coefficients were monitored simultaneously.

A solution was considered meaningful only when the aerodynamic coefficients
reached sufficiently stable values in addition to the reduction of the
residuals.

This was particularly useful for avoiding the assumption that a simulation
was converged based only on the iteration count.

---

# 7. Flow-Field Post-Processing

The converged solution was analysed using several flow visualisations.

The post-processing included:

- Pathlines

These visualisations were used together with the numerical values of CL and CD
to interpret the aerodynamic behaviour of the profile.



## Pathlines

Pathlines were used to visualise the direction and evolution of the flow around
the airfoil.

They provide a useful qualitative representation of how the external flow
interacts with the geometry and how the wake develops downstream.

---

# 8. Results Summary

The project progressed from a symmetric baseline configuration to a final
cambered-airfoil simulation.

| Configuration | Purpose | Main Observation |
|---|---|---|
| NACA 0012 at 0° | Baseline / sanity check | Lift approximately zero, as expected for a symmetric airfoil |
| NACA 2412 at 0° | Final CFD case | Positive lift generated by airfoil camber |
| NACA 2412 at 0° | Quantitative result | CL = 0.2174, CD = 0.0100 |

The comparison helped connect the numerical results with the fundamental
aerodynamic differences between symmetric and cambered airfoils.

---

# 9. What I Learned

The project provided practical experience with the main stages of a CFD
aerodynamic analysis.

In particular, I developed experience with:

- External aerodynamic CFD setup
- ANSYS Workbench workflow
- ANSYS Meshing
- ANSYS Fluent
- Computational domain definition
- Local mesh refinement
- Edge sizing
- Inflation layers
- Boundary-condition definition
- Numerical solver setup
- Residual monitoring
- Lift and drag coefficient monitoring
- CFD convergence assessment
- Pressure and velocity field interpretation
- Pathline visualisation
- Aerodynamic interpretation of numerical results

Most importantly, the project helped me understand that obtaining a CFD result
is only one part of the analysis: mesh quality, convergence and physical
interpretation must also be considered before accepting the numerical output.

---

# 10. Limitations and Future Development

This project represents an introductory CFD aerodynamic study rather than a
fully validated research-level analysis.

Further development could include:

- Formal mesh-independence study
- Detailed near-wall resolution and y+ assessment
- Comparison with experimental wind-tunnel data
- Investigation of additional operating conditions
- Systematic angle-of-attack sweep
- Comparison between turbulence models
- Automated extraction and analysis of CFD results using Python
- Generation of complete CL-α and CD-α aerodynamic curves

These steps would provide a more rigorous assessment of the numerical accuracy
and extend the project into a more complete aerodynamic study.

---
