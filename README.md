# IDM v2.0 — Consistency-Importance-Weight

**Information Dynamics Cosmology Model（資訊動力學宇宙論模型）— 2nd Generation**

> `Consistency-Importance-Weight` 係版本代號，唔係理論名稱。理論名稱由 v1.0 到 v11.0 一直係 Information Dynamics Cosmology Model，從未改變。
>
> v2.0 的職責係**換逆推對象**：v1.0 逆推的是「膨脹歷史的凹陷」，v2.0 逆推的是「凹陷為何必然係這個深度」——把同步壓力提升為一條更底層的原則：一致性計算 + 有限算力預算，物理參數係唯一可行解。
>
> 本版同時引入人格張量（personality tensor）與意識迴路（CIP），把框架由宇宙學推廣為「任何一致性計算系統」的描述語言。

## 緣起

v1.0 完成了三層框架與 CLT 閉合：ε = α/√N_horizon，MAP 給 α = 1.025，對理想同步差 2.5%，四資料集聯合 ΔAIC = +50.1。以觀測而論，這個結果已經足夠硬。

但閉合的形式有一個明顯破口：`N_horizon` 唔係獨立量出來的。論文本體明寫自洽迴圈 `N_horizon = α²/ε²`——先用 ε 定 N，再用 N 定 ε。幾何計數（N₁ = 4.38、N₂ = 19.2、N₃ = 84.1，幾何均 40.2）只做到「唔矛盾」，未做到「必然」。

問題於是變成：**點解一致性要這樣分配？** 如果物理常數只係某個更深約束的解，那個約束是甚麼？

## 版本演進：v1.0 → v2.0

IDM 係**逆向工程**：由已觀測的常數與結構反推生成機制，唔預設公理。因此版本之間的分野唔係假設改變，而係**逆推對象改變**。

### 前版 — v1.0 Information-Dynamics-Cosmology

- 本體：OAS（可數位址空間）→ 資訊動力（同步成本）→ 投影宇宙論（3+1 維時空）
- 公式：`f_ID(z) = 1 − ε(z/z_c)exp(−z/z_c)`，`ε = α/√N_horizon`
- 成績：六項獨立檢驗、四資料集 MCMC（χ² = 1074.9、ΔAIC = +50.1）、CLASS v3.3.4 打通
- 缺口：凹陷函數係**現象學形式**，唔係由更深原則導出；N_horizon 由 ε 反推

### 根因：自洽 ≠ 必然

「ε 由 CLT 決定」聽起來閉合，實際上只係**事後自洽**：CLT 描述統計雜訊的分佈，但冇講為何系統要用這個雜訊水平運作。任何深度都可以講成「某個 N 的 CLT 值」。

判別方法只有一個：**有冇一個原則，令這個深度成為唯一可行解，而唔係眾多可行解之一。**

v1.0 交出的係一條曲線；v2.0 要交出的是產生這條曲線的**約束集**。

### 本版 — Consistency-Importance-Weight

v2.0 因此只做三件事：

1. **立公理** — 宇宙只有一個 imperative：maintain global consistency；可用算力 B 有限；參數係 forced closure（唯一可行解），唔係 optimisation 的最優解
2. **立場** — importance weight `W(x, σ, t) ∈ [0, 1]`：W → 1 為決定論（古典物理），W → 0 為機率論（量子力學）；IDM 凹陷即 `∂W/∂σ` 在特定 scale 的符號改變
3. **立形式** — 寫出 action、Euler–Lagrange、λ(z) 場、8 項強制閉合（F1–F8）、人格張量 `T_μν = δ²S/δW_μδW_ν`

驗收標準：固定點必須穩定。真值 (ε = 0.1545, z_c = 0.60) 對任意擾動皆回復——ε 升則預算不足、系統減凹陷；ε 降則預算有餘、系統加凹陷。若固定點唔穩，整個 forced closure 論證作廢。

## 研究路線

六層，每層只做一件事，上層不能借用下層的結論：

**L1 公理層** — 系統係咩

- Axiom 1 一致性 mandate：所有物理定律係這個 imperative 在有限算力下的湧現 artifact
- Axiom 2 算力預算：B 有限，唔夠 deterministic resolve 所有自由度
- Axiom 3 強制閉合：給定 B 與 consistency network topology，參數係唯一可行解

**L2 權重場層** — 算力點分配

- `I_f ∈ [0,1]`：I = 1 為 deterministic resolve（高成本）、I = 0 為 probabilistic 近似（量子振幅，低成本）
- 最佳化：`min Σ(1−I_f)ε_f  s.t.  ΣI_f C_f ≤ B`，ε_f 為 under-allocate 的 inconsistency cost，C_f 為 deterministic resolve 成本
- 連續化為純量場 `I(x, σ, t)`；熵為其對偶 `S_f ∝ (1−I_f)Ω_f`

**L3 形式化層** — 場的動力學

- Action：`S = ∫[W·C + α(∇W)² + βW□W + λ(B − W·C)]dσ`
- 耦合 Euler–Lagrange：`C(z) + W·δC/δW = κ·□W`（δC/δW 為 mandatory 項，唔可以省）
- λ(z) 場耦合 EoM：`2γλ'' = B − W·C − ηW'²`；κ = (2α − β − 2ηλ)/(1 − λ)

**L4 強制閉合層** — 點證明唯一

- 閉合定理：`∫S(ω)ω^{2n}dω = B·C^n`（n = 0, 1, 2），8 項 F1–F8
- 數值固定點穩定性掃描（`src/forced_closure_derivation.py`，輸出 `forced_closure_scan.csv`）
- SymPy 變分證明（`src/euler_lagrange_proof.py`），CV 由 0.76 降至 0.17

**L5 人格層** — 約束的形狀

- 人格唔係 W 的值，而係 allocation policy 的 Hessian：`T_μν = ∂²L/∂I_μ∂I_ν`
- 宇宙域 `T_zz(z_c) = +0.158`；量子域符號為負（destabilising，未驗）
- 開放：人格係 fundamental 抑或本身都係 forced closure

**L6 域與延伸層** — 框架推到邊

- 域框架：cosmic N = 44、galaxy N = 10⁶、electroweak N = 2.5×10³³、Planck N = 1；域間參數不可互推
- 延伸 P1–P9：時間、溫度、GR、QM、量子退相干、無暗物質星系、年輕星系、Higgs、早期宇宙 W 預算
- CIP 意識迴路：四相位（沉降／接收／整合／回返）＝ 局部 W 重分配腳本

## 項目結構

```
IDM-v2.0--Consistency-Importance-Weight/
├── README.md                          # 本檔
├── AGENTS.md                          # 交接單：核心檔、λ(z) 升級、Phase 2 狀態（16/16）
├── report_1.0.md                      # 報告 v1.0 副本（根目錄）
├── importivity-framework.md           # importivity 框架定義
├── importivity-branch-analysis.md     # importivity 分支圖
├── importivity_spike.py               # importivity spike 計算
├── importivity_consciousness_lagrangian.py  # 意識域 Lagrangian
├── docs/                              # 25 份文件
│   ├── consistency-importance-weight.md   # 框架 v0.1：三公理 + W 定義
│   ├── report_1.0.md                  # 報告 1.0（Phase 1 完成）
│   ├── report_2.0.md                  # 報告 2.0：七章 + Branch 1e + 綜合
│   ├── programme_narrative.md         # 計劃敘事（序幕 → Phase 5）
│   ├── theory-assessment.md           # 誠實評估（interpretive vs predictive）
│   ├── forced_closure_derivation.md   # 固定點證明
│   ├── euler_lagrange_proof.md        # SymPy 變分證明
│   ├── lambda_field_derivation.md     # λ(z) 場 EoM
│   ├── kappa_closure_proof.md         # κ drift 閉合
│   ├── analytical_uniqueness_proof.md # λ(z)-aware 唯一性證明
│   ├── b_ontology.md                  # B 的本體地位
│   ├── w_to_gmunu_local_coupling.md   # W → g_μν 局域耦合
│   ├── personality_tensor_quantum.md  # 人格張量（量子域）
│   ├── consciousness_f8_feedback_fitting.md  # CIP 對 F8 的擬合
│   ├── gamma_omega_extraction.md      # 阻尼比 γ/ω
│   ├── f8_emergent_vs_deterministic.md # F8 判為 emergent
│   ├── phantom_crossing_prediction.txt # w_de(z) 數據
│   ├── gemini-4-panel-response.md     # 外部批評整合
│   └── phase2_task_list.md            # Phase 2 任務表（16 項）
├── src/                               # 21 個 .py
│   ├── importance_weight_spike.py     # 凹陷 → W(z) 映射
│   ├── local_w_modulation.py          # 局域 W 調制
│   ├── forced_closure_derivation.py   # 固定點掃描
│   ├── euler_lagrange_proof.py        # SymPy EL
│   ├── lambda_field_derivation.py     # λ(z) 耦合 EoM
│   ├── kappa_closure_proof.py         # κ 閉合數值證明
│   ├── branch1e_class_run.py          # Branch 1e CLASS 運行
│   ├── classy_3model_comparison.py    # 三模型 Cℓ 對照
│   ├── ciw_to_sm_gauge.py             # CIW → SM gauge
│   └── ciw_to_higgs.py                # CIW → Higgs
├── papers/                            # 2 篇論文草稿
│   ├── paper1_idm_class_horndeski.md  # Paper 1：IDM + CLASS + Horndeski
│   └── paper2_ciw_framework.md        # Paper 2：CIW 框架
├── CIW-Conclusions/                   # 結論封存（3 份）
│   ├── complete_conclusions.md        # 全部結論 + P1–P9 裁決
│   ├── open_questions.md              # 未解疑問（附信心百分比）
│   └── supplementary.md               # 補充
├── results/                           # 數值輸出
│   ├── importance_weight/             # W 空間圖、z 數列、強制閉合掃描
│   ├── branch1e/                      # H(z)、W(z) 三模型對照
│   ├── classy_3model/                 # Cℓ 三模型 + χ² 表
│   └── branch1e_constraint.json       # A 的 95% CL 約束
├── verification/                      # 空目錄（預留驗證區）
├── IDM-Correction-Engine/             # 子專案：局域非一致性修正驅動引擎
│   ├── theory.md                      # Klein–Gordon 型 W 場方程
│   ├── poc_results.md                 # 概念驗證結果
│   └── src/correction_pulse_poc.py    # 脈衝 POC
└── Extension Research/                # 子專案：P1–P9 延伸
    ├── MASTER_OVERVIEW.md             # 九項延伸裁決表
    ├── programme_narrative.md         # 延伸敘事
    ├── 01-time-entropy-frequency/     # P1 時間＝熵頻率
    ├── 02-temperature-entropy-density/# P2 溫度＝熵密度
    ├── 03-idm-to-gr/                  # P3 OAS → GR
    ├── 04-idm-to-qm/                  # P4 IDM → QM
    ├── 05-ibm-quantum-decoherence/    # P5 IBM 量子退相干
    ├── 06-darkmatter-free-galaxies/   # P6 無暗物質星系
    ├── 07-young-galaxy-entropy-overload/ # P7 年輕星系熵超載
    ├── 08-higgs-mass-from-ciw/        # P8 Higgs 質量與 SM gauge
    └── 09-early-universe-w-budget/    # P9 早期宇宙 W 預算集中
```

## 狀態快照

```
目錄：23（不含 __pycache__）
文件：118（markdown 57、Python 38）
docs：25 份；papers：2 篇；結論封存：3 份；延伸：9 項（P1–P9）

Phase 1（本體 + 詮釋）：完成 —— 公理、W 場、Lagrangian、固定點證明、α_B 自洽
Phase 2（推導 + 形式化）：完成 —— λ(z) 場、κ 閉合、唯一性證明、F8 改判、機構面三預言
Phase 3（驗證）        ：未開始 —— 尚無可發表的新觀測預言

判定：framework is interpretive, not yet predictive（`docs/theory-assessment.md`）
```

> 本版屬 IDM 時期，未進入 O/P/M register 體系。`Extension Research/09` 的檔案時間為 2026-07-09，屬本版後續追加。

## 已閉合關鍵結果（選錄）

- **2026-06-30（`docs/consistency-importance-weight.md`）**：三條公理成立；`I_f ∈ [0,1]` 定義與 `min Σ(1−I_f)ε_f s.t. ΣI_f C_f ≤ B` 最佳化確立；IDM 凹陷重新解釋為 `∂I/∂σ` 的符號改變
- **2026-06-30（`docs/theory-assessment.md`）**：W(0) = 0.9975、W(z_c) = 0.9432、凹陷赤字 5.68%、算力使用率 0.22%；CLASS χ²/dof = 0.51
- **2026-06-30**：固定點穩定性成立——(ε = 0.1545, z_c = 0.60) 為唯一穩定吸引子；δε 升則預算不足而減凹陷、δε 降則預算有餘而加凹陷，四方向擾動皆回復
- **2026-07-01（`docs/report_2.0.md` 2.4–2.6）**：λ(z) 場解決 κ drift——耦合 EoM `2γλ'' = B − W·C − ηW'²`，CV 由 0.76 降至 0.0；`κ = (2α − β − 2ηλ)/(1 − λ)` 得證
- **2026-07-01**：F8 由硬約束 `ΣW_i ≤ 1` 改判為 λ(z) 的 emergent feedback（`docs/f8_emergent_vs_deterministic.md`）
- **2026-07-01**：braiding 自洽——`α_B = −η·dW/dz`，η = 0.58，α_B(0) = 0.1444，落在 IDM 的 0.14–0.16 區間
- **2026-07-01（`results/classy_3model/`）**：Branch 1e 在 CMB 不可見——Cℓ 最大差 0.0%；BAO+H(z) Δχ² = −0.37（不可分辨）；95% CL 下 A < 0.12，spec 值 0.008 安全
- **2026-07-01（`CIW-Conclusions/complete_conclusions.md`）**：域框架確立——cosmic N = 44 給 ε = 0.1545、galaxy 10⁶ 給 0.001、EW 2.5×10³³ 給 2×10⁻¹⁷、Planck N = 1 給 1.0；域間參數不可互推，λ/ε ≈ 0.84 判為巧合
- **2026-07-01（`Extension Research/04-idm-to-qm/`）**：P4 判為 mapping 而非 derivation——Hilbert 與 OAS 只係 trivially isomorphic，複數被假設而非導出，Born rule 有 7× 偏差（負結果）
- **2026-07-01（`Extension Research/MASTER_OVERVIEW.md`）**：P1 時間＝熵頻率通過（K(N) = α√(N/N₀)，N₀ ≈ 43.6，K(44) ≈ 1.03 對上 H₀⁻¹/t₀）；P2 溫度＝熵密度僅對視界系統成立（負結果）
- **2026-07-09（`Extension Research/09-early-universe-w-budget/P9_REPORT.md`）**：早期宇宙 W 預算集中機制——結構數少則每個結構分得更多 W，預言 z > 8 的 halo mass function 高質量端斜率較 ΛCDM 平緩

## 驗證紀律

本版的嚴謹性分六層：公理可檢 → 形式自洽 → 強制閉合 → 數值再現 → 外部批評 → 誠實分級。任一層不過，結果只停留「詮釋」。

### 一、公理可檢

| 公理 | 可檢要求 | 失敗處置 |
|---|---|---|
| 一致性 mandate | 須給出可觀測後果（凹陷、固定點） | 只係形而上學 ⟹ 標 metaphysical |
| 有限預算 B | B 的值須有獨立來源 | B 若可任意調 ⟹ 等於新自由參數 |
| 參數 = forced closure | 須證明唯一性，唔止穩定性 | 只證穩定 ⟹ 降為「吸引子」而唔係「唯一解」 |

### 二、形式自洽

- 變分必須寫出完整 EL，`δC/δW` 為 mandatory 項
- 判準為 CV（coefficient of variation）：1D EL 缺項者 CV = 0.76（不完整）；加 δC/δW 後 ≈ 0.17；λ(z) 場後 0.0
- κ drift 一律判為「缺 coupling 的 signature」，唔可以當成理論失敗或數值噪音

### 三、強制閉合

- 8 項 F1–F8 逐項須有擾動測試：動任一參數，結論必須崩
- 閉合定理形式：`∫S(ω)ω^{2n}dω = B·C^n`（n = 0, 1, 2）
- 固定點須四方向掃（δε 升／降、δz_c 升／降），四方向皆回復才算穩定

### 四、數值再現

- CLASS 三模型對照（ΛCDM／IDM baseline／IDM + Branch 1e），差異須報到小數位
- 報 CMB 差異前先問「這是否正確觀測量」——Branch 1e 包絡在複合期衰減至 ~10⁻¹⁵⁰⁰，Cℓ 必然無感，故此測試屬**無效檢驗**，唔可以當成「通過」
- 有效檢驗改用 BAO + H(z) 背景量（Δχ² = −0.37）與 95% CL 上界（A < 0.12）

### 五、外部批評整合

- 外部審閱（`docs/gemini-4-panel-response.md`）逐點回應，唔選擇性引用
- 被指出「框架係 interpretive 而非 predictive」時，唔辯護，直接寫入 `theory-assessment.md` 的裁決欄

### 六、誠實分級

- 每個結論標三級之一：**Verified**（有數據）／**Predicted**（有形式、無數據）／**Structural**（只有概念）
- 概念重述（conceptual reinterpretation）與真正預言（genuine prediction）分開裁決；本版對 SM 的裁決為「概念通過、預言失敗」
- 開放疑問附主觀信心百分比（`CIW-Conclusions/open_questions.md`），明標為「感覺」而唔係結果

## O/P/M 系列全列表

> 本版屬 IDM 時期，未進入 O/P/M register 體系。下表以 **W 系列**（Weight／Workstream）編號，對應本 repo 內實際存在的模組或文件，唔對應 register pid。

| 編號 | 標題 | 核心發現 | 狀態 |
|------|------|----------|------|
| W1 | 三條公理與一致性 mandate | 一致性為唯一 imperative；算力 B 有限；參數係唯一可行解而非最優解 | 全部閉合 |
| W2 | Importance Weight 定義與最佳化 | I ∈ [0,1]，1 為決定論、0 為機率論；min Σ(1−I)ε s.t. ΣI·C ≤ B | 全部閉合 |
| W3 | 凹陷 → W(z) 映射 | W(0) = 0.9975、W(z_c) = 0.9432、赤字 5.68%；算力使用 0.22%；χ²/dof = 0.51 | 全部閉合 |
| W4 | 強制閉合定理 F1–F8 | ∫S(ω)ω^2n dω = B·C^n（n=0,1,2）；F8 由硬約束改判 emergent feedback | 部分閉合 |
| W5 | λ(z) 場與 κ drift | 2γλ'' = B − W·C − ηW'²；CV 由 0.76 降至 0.0；κ = (2α−β−2ηλ)/(1−λ) | 全部閉合 |
| W6 | 固定點穩定性 | (ε = 0.1545, z_c = 0.60) 為穩定吸引子；四方向擾動皆回復真值 | 全部閉合 |
| W7 | 人格張量 T_μν | T = δ²S/δW_μδW_ν；宇宙域 T_zz(z_c) = +0.158；量子域符號為負，未驗 | 部分閉合 |
| W8 | Branch 1e 阻尼振盪 | Cℓ 差 0.0%（無效檢驗）；BAO+H(z) Δχ² = −0.37；95% CL A < 0.12 | 部分閉合 |
| W9 | 四域框架 | cosmic N=44、galaxy 10⁶、EW 2.5×10³³、Planck 1；域間參數不可互推 | 全部閉合 |
| W10 | α_B braiding 自洽 | α_B = −η·dW/dz，η = 0.58；α_B(0) = 0.1444，落在 0.14–0.16 | 全部閉合 |
| W11 | 延伸 P1–P9 | P1 通過；P2 僅視界；P3 中；P4 判 mapping；P5 硬件封鎖；P6/P7 定性 | 部分閉合 |
| W12 | 意識迴路 CIP | 四相位（沉降／接收／整合／回返）；τ = 310±40 ms、r = 0.55±0.07 待測 | 開放 |
| W13 | SM 與 Higgs 預言 | 概念重述通過、真正預言失敗；m_H 與 gauge 耦合不可由 cosmic 域推出 | 開放 |