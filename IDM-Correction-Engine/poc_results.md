# 局域非一致性修正驅動引擎 — 概念驗證結果

**PoC 模擬:** 1+1D Klein-Gordon W-field
**日期:** 2026-06-30

---

## 設定

| 參數 | 值 | 意義 |
|------|-----|------|
| κ | 0.60 | Forced closure constant |
| W₀ | 1.0 | Ground state（full consistency） |
| A | 0.15 | Initial dip amplitude |
| σ | 0.30 | Initial dip width |
| Grid | 300 × 1200 | Nx × Nt |
| Lx, Lt | 10.0, 30.0 | Domain size |
| CFL | 0.75 | dt/dx < 1 ✅ |

## 結果

```
Max dip depth: 0.8502
Dip recovery time: 5.83 units
Pulse propagation speed: 0.54 (c = 1)
Correction energy: 0.3577 → 0.2096
```

## 驗證嘅 Predictions

### Prediction 1: Restoring oscillation ✅

系統修正 local inconsistency 時，中心點以 ω = √κ 振盪。

| 量 | 理論 | 實測 | 匹配 |
|----|------|------|------|
| ω | 0.775 | 0.734 | **5.2%** |

### Prediction 2: Causal propagation ✅

修正 pulse 以 finite speed 向外傳播，形成 causal horizon。速度 ~0.54c，受 grid 細分影響，但係 finite 而唔係 instantaneous。

### Prediction 3: Energy dissipation ✅

Correction energy 由 0.3577 降到 0.2096，monotonic decay。能量透過 spatial spreading dissipate。

### Prediction 4: Dip recovery ✅

初始 dip（depth 0.85）喺 ~5.83 時間單位內回復到 99% baseline。

## 圖表

`results/correction_pulse_poc.png` 包含四格：

| Panel | 內容 |
|-------|------|
| 左上 | W(x,t) spacetime — 修正 pulse 向外傳播 |
| 右上 | 中心點回復 — 振盪回升到 W₀=1 |
| 左下 | 不同時間 slice — t=0,5,10,20,30 |
| 右下 | 修正能量 — monotonic dissipation |

## 結論

**概念驗證成功。** W-field forced closure 嘅 signature 被模擬證實。系統自動修正 local inconsistency，修正 pulse 有 specific、predictable 嘅 signature。

---

*2026-06-30 · IDM-Consistency-Importance-Weight*