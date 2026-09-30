# Numerical Matrix Analysis Labs

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive collection of laboratory assignments, algorithmic implementations, and performance benchmarks for **Numerical Matrix Analysis / Numerical Linear Algebra**. This repository covers direct and iterative system solvers, matrix factorizations, spectral analysis, and stability/conditioning experiments.

---

## 📑 Lab Overview

| Lab | Module Name | Mathematical Focus & Algorithms |
| :--- | :--- | :--- |
| **Lab 01** | Direct Methods for $A\mathbf{x}=\mathbf{b}$ | Gaussian Elimination (Partial/Full Pivoting), $LU$ Decomposition, Cholesky Factorization ($\mathbf{A} = \mathbf{L}\mathbf{L}^T$) |
| **Lab 02** | Orthogonalization & $QR$ | Modified Gram-Schmidt, Householder Transformations, Givens Rotations, $QR$ Decomposition |
| **Lab 03** | Iterative Solvers | Jacobi Method, Gauss-Seidel Method, Successive Over-Relaxation (SOR), Conjugate Gradient (CG) |
| **Lab 04** | Eigenvalue Problems | Power Method, Inverse Power Iteration, Rayleigh Quotient Iteration, $QR$ Algorithm for Spectrum Computation |
| **Lab 05** | Singular Value Decomposition | Full/Truncated SVD ($\mathbf{A} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^T$), Low-Rank Approximations, Image Compression |
| **Lab 06** | Error & Conditioning | Condition Number $\kappa(\mathbf{A})$, Perturbation Analysis, Linear Least Squares ($\mathbf{A}^T\mathbf{A}\mathbf{x} = \mathbf{A}^T\mathbf{b}$ vs. $QR$) |

---

## 📂 Repository Structure

```text
numerical-matrix-analysis/
├── labs/
│   ├── lab01_direct_solvers/
│   │   ├── lu_decomposition.py
│   │   └── cholesky.py
│   ├── lab02_qr_factorization/
│   ├── lab03_iterative_methods/
│   ├── lab04_eigenvalues/
│   ├── lab05_svd_applications/
│   └── lab06_conditioning_least_squares/
├── notebooks/            # Jupyter notebooks with convergence plots & benchmarks
├── src/                  # Core library functions and utility modules
├── tests/                # Unit tests comparing implementations against NumPy/SciPy
├── requirements.txt      # Python dependencies
└── README.md
