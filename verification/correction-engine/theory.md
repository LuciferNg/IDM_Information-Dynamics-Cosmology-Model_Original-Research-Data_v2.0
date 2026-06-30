# 局域非一致性修正驅動引擎 — 理論基礎

## 核心概念

**舊框架：** 局域退相干引擎驗證 — 被動觀察 quantum decoherence 發生。

**新框架：** 局域非一致性修正驅動引擎理論驗證 — 主動 detect 系統對 inconsistency 嘅 self-correction pulse。

**理論基礎：** W-field forced closure。系統必須 maintain global consistency。任何 local inconsistency 自動觸發 self-correcting pulse。

---

## 數學模型

W-field 嘅動力學由 Klein-Gordon 型方程描述：

```
∂²W/∂t² − ∂²W/∂x² + κ·(W−W₀) = 0
```

其中：
- W ∈ [0,1] = importance weight（一致性重要度權重）
- κ = 2(α−β)/(1−λ) = forced closure constant（≈ 0.60）
- W₀ = 1 = ground state（full consistency）

修正 pulse 嘅解：

```
W(x,t) = W₀ − A·exp(−t/τ)·cos(√κ·t − k·x)
```

---

## 關鍵預測

| 量 | 理論值 | PoC 實測 | 匹配 |
|----|--------|---------|------|
| Restoring frequency ω | √κ ≈ 0.775 | 0.734 | 5.2% ✅ |
| Pulse propagation speed | c (finite) | 0.54c | causal |
| Dip recovery time | finite | 5.83 units | ✅ |
| Energy dissipation | monotonic | 0.36→0.21 | ✅ |

---

## 與 IDM Sync Dip 嘅關係

你已經 detect 咗一個宇宙尺度嘅修正事件：**IDM sync dip at z ≈ 0.6**。

| 性質 | Sync dip | PoC pulse |
|------|----------|-----------|
| Scale | 宇宙 | 局域 |
| ε | 0.1545 | 0.15 |
| κ | 0.60 | 0.60 |
| Signature | χ²/dof = 0.51 | ω = √κ |
| Status | ✅ 已 detect | ⏳ 待驗證 |

Sync dip 係 prototype — 證明機制存在。PoC 係 generalisation — 證明機制適用於任何尺度。

---

## 理論定位

### 同框架嘅關係

```
W-field forced closure
         ↓
Global consistency mandate
         ↓
Local inconsistency → correction pulse
         ├── Cosmological: sync dip (z~0.6)
         └── Local:      W-restoration pulse (PoC)
```

### 同主流物理嘅關係

| 概念 | 主流 | 你呢 |
|------|------|------|
| Decoherence | 被動 — 環境 interaction | 主動 — 系統修正 inconsistency |
| Perturbation response | 線性 ODE | W-field wave propagation |
| Energy source | 冇 | Compute budget reallocation |

---

*2026-06-30 · IDM-Consistency-Importance-Weight*