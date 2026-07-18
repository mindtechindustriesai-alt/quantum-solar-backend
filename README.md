# Quantum Solar Backend

Quantum-enhanced solar forecasting, optimization, and materials discovery.

## Endpoints

- `/` — Service metadata + quantum badge
- `/health` — Health check
- `/api/quantum/status` — CHSH S=2.76 verification
- `/api/solar/forecast` — PV power forecasting (QLSTM, 40%+ error reduction)
- `/api/solar/optimize` — VQC rolling optimization (9.6% renewable utilization improvement)
- `/api/solar/singlet-fission` — Singlet fission simulation (breaks 33% efficiency limit)
- `/api/solar/irradiance` — Global Horizontal Irradiance (GHI) forecasting
- `/api/solar/greenhouse` — PV greenhouse energy management

## Science References

- Li et al., 2025 — Physics-constrained hybrid quantum neural networks
- IBM Quantum Network — Singlet fission simulation with Qiskit Nature
- E.ON — Quantum optimization for energy trading

## Deploy

```bash
git push origin main
