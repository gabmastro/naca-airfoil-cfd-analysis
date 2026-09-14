# NACA 2412 CFD Aerodynamic Study

## Overview

This project presents a two-dimensional CFD analysis of a **NACA 2412 airfoil** using **ANSYS Fluent**.

The objective was to study the aerodynamic behaviour of a cambered airfoil over a range of angles of attack, from attached-flow conditions to stall.

The project includes:

- NACA 2412 geometry generation using Python
- 2D computational domain and mesh generation
- boundary-layer inflation
- mesh refinement study
- steady RANS simulations using the k-ω SST turbulence model
- angle-of-attack sweep from 0° to 18°
- lift and drag analysis
- drag polar and aerodynamic efficiency
- comparison with thin-airfoil theory
- visualization of flow separation and stall using velocity pathlines

The simulations were performed at:

- Freestream velocity: **30 m/s**
- Chord: **1 m**
- Air density: **1.225 kg/m³**
- Dynamic viscosity: **1.79 × 10⁻⁵ Pa·s**

giving a chord-based Reynolds number of approximately:

**Re = 2.05 × 10⁶**

---

## Geometry

The NACA 2412 profile was generated using a Python script from the standard NACA 4-digit analytical definition.

For a NACA 2412 airfoil:

- Maximum camber: **2% of chord**
- Maximum camber position: **40% of chord**
- Maximum thickness: **12% of chord**

The generated coordinates were exported and imported into ANSYS for the CFD analysis.

The chord was kept equal to:

**c = 1 m**

The angle of attack was imposed by changing the freestream velocity components rather than rotating the airfoil geometry.

For each angle:

`Ux = U∞ cos(α)`

`Uy = U∞ sin(α)`

This allowed the same geometry and mesh to be used throughout the angle-of-attack sweep.

---

## Computational Domain

A two-dimensional external-flow domain was created around the airfoil.

Domain dimensions:

- Upstream boundary: **5c**
- Downstream boundary: **11c**
- Upper boundary: **2.5c**
- Lower boundary: **2.5c**

The airfoil was subtracted from the fluid domain to obtain a single 2D fluid region.

Boundary conditions were adapted to the direction of the freestream during the angle-of-attack sweep.

---

## Mesh

The final refined mesh used:

- Global element size: **0.15 m**
- Airfoil edge sizing: **0.005 m**

Boundary-layer inflation was applied directly to the airfoil surface.

### Inflation settings

| Parameter | Value |
|---|---:|
| First layer height | 2.4 × 10⁻⁵ m |
| Maximum layers | 30 |
| Growth rate | 1.18 |
| Inflation algorithm | Pre |

The small first-layer height was selected to obtain adequate near-wall resolution for the k-ω SST turbulence model.

A coarser mesh was also investigated before adopting the refined configuration in order to assess the sensitivity of the aerodynamic coefficients to mesh refinement.

---

## CFD Setup

The simulations were performed using **ANSYS Fluent**.

### Solver

- 2D
- Steady
- Pressure-based solver
- Double precision
- SIMPLE pressure-velocity coupling

### Turbulence model

**k-ω SST**

The SST model was selected because of its ability to provide good near-wall treatment while also being suitable for aerodynamic flows involving adverse pressure gradients and flow separation.

### Freestream conditions

| Parameter | Value |
|---|---:|
| Velocity | 30 m/s |
| Density | 1.225 kg/m³ |
| Dynamic viscosity | 1.79 × 10⁻⁵ Pa·s |
| Turbulence intensity | 1% |
| Turbulent viscosity ratio | 10 |
| Reynolds number | ≈ 2.05 × 10⁶ |

Second-order spatial discretization was used for the final converged solutions.

Convergence was assessed using both residual behaviour and stabilization of the aerodynamic force coefficients.

---

## Angle-of-Attack Sweep

The NACA 2412 was simulated at:

**α = 0°, 4°, 8°, 12°, 14°, 16°, 17°, 18°**

The converged lift and drag coefficients were:

| α [deg] | Cl | Cd | Cl/Cd |
|---:|---:|---:|---:|
| 0 | 0.2174 | 0.0100 | 21.74 |
| 4 | 0.6176 | 0.0125 | 49.41 |
| 8 | 1.0246 | 0.0196 | 52.28 |
| 12 | 1.3415 | 0.0334 | 40.16 |
| 14 | 1.4651 | 0.0441 | 33.22 |
| 16 | 1.5241 | 0.0605 | 25.19 |
| 17 | 1.4888 | 0.0748 | 19.90 |
| 18 | 1.4175 | 0.0961 | 14.75 |

---

## Lift Curve

At low and moderate angles of attack, the lift coefficient increases approximately linearly with α.

Using the CFD results between 0° and 8°:

`dCl/dα ≈ 0.101 /deg`

At higher incidence, the slope progressively decreases.

The maximum lift coefficient observed in the simulated points was:

**Cl,max ≈ 1.52 at α = 16°**

Beyond this point, the lift coefficient decreases while drag continues to increase.

This behaviour indicates the onset of stall between approximately **16° and 18°** for the present CFD setup.

---

## Aerodynamic Efficiency

Aerodynamic efficiency was evaluated using:

`Cl/Cd`

The highest value among the simulated points was obtained at:

**α = 8°**

with:

**Cl/Cd ≈ 52.3**

At larger angles of attack, drag increases significantly and the aerodynamic efficiency decreases.

---

## Thin-Airfoil Theory Comparison

The zero-angle CFD result was compared with thin-airfoil theory.

For the NACA 2412 camber line, thin-airfoil theory gives an estimated zero-lift angle of approximately:

**αL=0 ≈ -2.08°**

Using:

`Cl = 2π(α - αL=0)`

the theoretical lift coefficient at α = 0° is approximately:

**Cl,theory ≈ 0.228**

The CFD result was:

**Cl,CFD = 0.2174**

corresponding to a difference of approximately **4.6%**.

The agreement provides a useful sanity check for the CFD setup while accounting for the different assumptions of viscous RANS CFD and inviscid thin-airfoil theory.

---

## Flow Separation and Stall

Velocity pathlines were compared at several representative angles of attack:

- **0°** – attached flow
- **8°** – strong acceleration over the upper surface with mostly attached flow
- **16°** – significant separation close to the maximum lift condition
- **18°** – larger separated region and post-stall behaviour

For comparison, the same velocity scale was used for the selected pathline visualizations.

The transition from 16° to 18° is particularly relevant.

Between these two conditions:

`Cl: 1.5241 → 1.4175`

while:

`Cd: 0.0605 → 0.0961`

The reduction in lift combined with the rapid increase in drag is consistent with the increasing flow separation observed over the upper surface.

---

## Main Results

The main results obtained from the study are:

- **Cl(0°) = 0.2174**
- **Cd(0°) = 0.0100**
- **Low-angle lift-curve slope ≈ 0.101 /deg**
- **Maximum sampled Cl ≈ 1.52 at 16°**
- **Maximum sampled Cl/Cd ≈ 52.3 at 8°**
- Clear nonlinear behaviour at high angles of attack
- Flow separation becomes significant close to the maximum-lift condition
- At 18°, lift decreases while drag increases strongly, indicating post-stall behaviour

The reported stall angle should be interpreted as the result of the present **2D steady RANS model, mesh, turbulence assumptions and sampled angles**, rather than as a universal value for the NACA 2412.

---

## Repository Structure

```text
NACA2412-CFD-Study/
│
├── README.md
│
├── report/
│   └── NACA2412_CFD_Report.pdf
│
├── geometry/
│   ├── generate_naca2412.py
│   └── naca2412.txt
│
├── data/
│   └── aerodynamic_coefficients.csv
│
├── postprocessing/
│   └── plot_aerodynamic_results.py
│
└── figures/
    ├── mesh.png
    ├── cp_alpha0.png
    ├── pathlines_alpha0.png
    ├── pathlines_alpha8.png
    ├── pathlines_alpha16.png
    ├── pathlines_alpha18.png
    ├── lift_curve.png
    ├── drag_curve.png
    ├── drag_polar.png
    └── aerodynamic_efficiency.png
```

---

## Limitations

The analysis uses a two-dimensional steady RANS approach.

The main limitations are therefore:

- three-dimensional aerodynamic effects are not included
- transition from laminar to turbulent flow is not explicitly modelled
- the standard SST model assumes a fully turbulent treatment
- steady RANS becomes less representative as the separated flow becomes increasingly unsteady near and beyond stall
- the exact maximum-lift angle was not resolved with a very fine angle-of-attack increment

Further work could include transient simulations near stall, transition modelling, additional mesh refinement and comparison with experimental data.

---

## Tools

- **ANSYS Fluent** – CFD solver
- **ANSYS Meshing / Discovery** – geometry and mesh preparation
- **Python** – NACA geometry generation and aerodynamic post-processing
- **NumPy**
- **Pandas**
- **Matplotlib**

---

## Author

**Gabriele Mastropierro**  
M.Sc. student in Aeronautical Engineering  
University of Padua
