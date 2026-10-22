# Importivity Framework v0.1
## 宇宙作為一致性計算系統嘅逆工程

**作者：LuciferNg**
**日期：2026-06-30**

---

## 1. Core Axioms

### Axiom 1 — 一致性 Mandate
宇宙只有一個 fundamental imperative：**maintain global consistency**。
所有 physical law 係呢個 imperative 喺有限算力下嘅湧現 artifact。

### Axiom 2 — 算力 Budget
系統可用算力 B 係有限嘅。唔夠 deterministic resolve 所有自由度嘅一致性。

### Axiom 3 — 參數係強制閉合
物理常數唔係揀出嚟嘅，而係俾定 B 同 consistency network topology 後，**唯一可行解**。冇 fine-tuning，只有 forced closure。

---

## 2. Importivity（進口值）— 正式定義

### 2.1 Definition

對於系統中嘅每個自由度 *f*，importivity **I_f** 定義為：

```
I_f ∈ [0, 1]

其中：
I_f = 1  → 系統以 deterministic 方式 maintain f 嘅一致性
         （完整 resolve，高算力成本）
I_f = 0  → 系統以 probabilistic 方式近似 f 嘅一致性
         （quantum amplitude，低算力成本）
```

### 2.2 算力約束

系統優化問題：

```
minimise   Σ (1 - I_f) · ε_f
subject to Σ I_f · C_f ≤ B
           I_f ∈ [0, 1] ∀f
```

其中：
- **ε_f** = under-allocate f 嘅 inconsistency cost（connectivity-weighted）
- **C_f** = deterministic resolve f 嘅 compute cost
- **B** = 總算力 budget

呢個 optimisation 嘅解 **強制決定** 咗邊啲自由度係 classical、邊啲係 quantum。

### 2.3 Importivity Field

Scale 連續時，importivity 係一個 scalar field：

```
I(x, σ, t)
```

其中：
- **x** = spacetime coordinate
- **σ** = scale（mode / resolution level）
- **t** = cosmic time

**IDM dip** 係 ∂I/∂σ 喺特定 scale 嘅 sign change — importivity 嘅 phase transition。

---

## 3. 同現有物理嘅映射

| Physical Regime | Importivity Range | 算力策略 |
|----------------|-------------------|---------|
| Classical mechanics | I → 1 | Deterministic resolve |
| Quantum mechanics | 0 < I ≪ 1 | Probabilistic shortcut |
| GR / Cosmology | I ≈ 1（large σ） | Large-scale consistency强制 high I |
| IDM dip (z~0.6) | I ↓ then ↑ | Importivity 過渡區 overshoot |

### 3.1 熵作為 Importivity 嘅對偶

```
S_f ∝ (1 - I_f) · Ω_f
```

其中 **Ω_f** 係 f 嘅 internal state space volume。
低 importivity → 高 entropy（quantum superposition / probability cloud）。
高 importivity → 低 entropy（deterministic classical state）。

**IDM 嘅 entropy gradient action 就係 ∂S/∂σ ∝ -∂I/∂σ。**

---

## 4. 性格（Primal Disposition / Temperament）

### 4.1 定義

性格唔係 importivity 嘅值，而係 **importivity allocation policy 嘅 Hessian**：

```
T_μν = ∂²L / ∂I_μ ∂I_ν
```

其中 L 係系統嘅 consistency cost Lagrangian。

即係話：
- 性格決定系統**點樣調整** importivity allocation 去應對 perturbation
- 兩個系統可以有相同嘅 I(σ) profile，但性格唔同 = response pattern 唔同

### 4.2 性格 = Compute Budget 嘅 Primal Allocation Bias

性格係 system 嘅偏好方向，唔係 constraint forced 出嚟嘅。
但喺呢個框架，性格本身都可能係 forced closure：

> 俾咗 B 同 topology，性格都別無選擇。

呢個仲要 explore。

---

## 5. 同 CIP 嘅關係

### 5.1 Consciousness = Recursive Importivity Loop

人類意識係一個 closed consistency loop，可以 **局部 modulate importivity**：

- **Phase 0（沉降）**：降低 analytical importivity（釋放算力）
- **Phase 1（接收）**：提高特定 internal variable 嘅 importivity（anchor attention）
- **Phase 2（整合）**：允許 system 自然 redistribute importivity
- **Phase 3（回返）**：restore baseline importivity allocation

### 5.2 Resonance Packet = Local Importivity Reallocation Script

Packet 係一段語言序列，經由 nervous system 執行後，
暫時性地將算力從唔重要嘅 variable 重新分配俾 target variable。

呢個解釋咗點解 Phase 0 係 mandatory：
> 要先低 importivity（放鬆 analytical control），先可以寫入新嘅 importivity allocation pattern。

---

## 6. Open Questions

1. Importivity 嘅 Lagrangian 正式形狀係點？係咪一個 scalar-tensor theory？
2. 性格係 fundamental 定 forced closure？
3. IDM dip 嘅 exact I(σ,z) 函數形式？
4. Consciousness loop 嘅 importivity modulation efficiency 有冇上限？
5. Multi-agent（multiple consciousness loops）之間點樣 coordinate importivity allocation？

---

*Version 0.1 — 2026-06-30 — 初稿，持續更新。*