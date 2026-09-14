# NACA Airfoil CFD Analysis

2D aerodynamic analysis using ANSYS Fluent
This project presents a two-dimensional CFD study of a NACA airfoil performed
using ANSYS Fluent.

The objective was to investigate the aerodynamic behaviour of the airfoil
at different angles of attack by evaluating lift and drag coefficients and
analysing the evolution of the surrounding flow field.

The project was developed as an independent study to gain practical experience
with the complete CFD workflow, from geometry and mesh generation to solver
setup, convergence assessment and post-processing.

---

## Objectives

The main objectives of the project were to:

- Build a suitable computational domain around the airfoil
- Generate a refined mesh in the regions of aerodynamic interest
- Apply local edge sizing and inflation layers near the airfoil surface
- Set appropriate boundary conditions and solver parameters
- Run simulations at multiple angles of attack
- Monitor solution convergence
- Evaluate lift and drag coefficients
- Analyse pressure and velocity distributions
- Visualise the flow using contours and pathlines
- Investigate the aerodynamic behaviour at increasing angle of attack

---

## Software

- **ANSYS Workbench**
- **ANSYS Fluent**
- **ANSYS Meshing**
- **Python** — aerodynamic data analysis and visualisation

---

## CFD Workflow

The analysis followed the general workflow:

Geometry → Computational Domain → Mesh → Boundary Conditions → Solver Setup
→ Convergence → Aerodynamic Coefficients → Flow Visualisation → Analysis

### 1. Geometry and Computational Domain

A two-dimensional airfoil geometry was placed inside a sufficiently large
fluid domain to reduce the influence of the external boundaries on the
solution.

The angle of attack was varied across multiple simulations to investigate
the evolution of the aerodynamic forces and flow structures.

### 2. Mesh

The mesh was refined in the regions where large velocity and pressure
gradients were expected.

Particular attention was given to:

- airfoil surface refinement
- leading-edge resolution
- trailing-edge resolution
- near-wall mesh quality
- inflation layers
- wake resolution

The objective was to obtain sufficient resolution around the airfoil while
maintaining a reasonable computational cost.

> Detailed mesh parameters are reported in the technical report.

### 3. Solver Setup

The simulations were performed in ANSYS Fluent using a pressure-based CFD
solution procedure.

Lift and drag coefficients were monitored together with the residuals to
assess convergence.

The same general numerical setup was maintained across the different angles
of attack to allow a consistent comparison between operating conditions.

---

## Simulation Campaign

Several angles of attack were investigated to analyse the evolution of the
airfoil aerodynamic behaviour.

For each case, the following quantities were evaluated:

- Lift coefficient, **CL**
- Drag coefficient, **CD**
- Pressure distribution
- Velocity field
- Flow pathlines
- Convergence behaviour

This allowed the aerodynamic performance to be compared across the complete
set of simulated conditions.

---

## Results

The simulations show the expected increase in lift as the angle of attack
increases over the investigated range, together with an increase in drag.

At the higher angles of attack, the flow-field visualisations become
particularly important for interpreting the aerodynamic coefficients and
identifying changes in the flow behaviour around the airfoil.

The project therefore combines quantitative aerodynamic data with qualitative
CFD post-processing rather than relying only on the final CL and CD values.

### Example result

One of the converged simulations produced:

| Quantity | Value |
|---|---:|
| Lift coefficient, CL | 1.4888 |
| Drag coefficient, CD | 0.0748 |

The complete results for all investigated angles of attack are reported in
the project report.

---

## Flow Visualisation

Post-processing was used to examine the physical behaviour of the flow around
the airfoil.

The analysis includes:
- Pathlines
- Wake development
- Flow behaviour at increasing angle of attack
