# Script Computation System

## Overview

Combines **Aramaic (RTL)** + **Greek** + **Mathematical symbols** to create computation formulas that evolve and transform scripts.

## Core Concept

### The Problem
- Aramaic reads **right-to-left (RTL)**
- Need to mix/match different scripts
- Scripts need to evolve and take different shapes
- Need computational formulas to transform scripts

### The Solution
- **Aramaic glyphs** (RTL) as input
- **Greek letters** + **Math symbols** form computation formulas
- Formulas transform scripts, allowing evolution
- Mix/match scripts to create new patterns

## Formula Structure

### Basic Formula Format
```
[Input Script] [Math Operation] [Greek Variable] → [Output Script]
```

### Examples

#### 1. Evolution: Multiply by Pi
```
𐡀 × π → β
```
- **Input**: Aramaic Aleph (𐡀)
- **Operation**: Multiply by π
- **Output**: Greek Beta (β)

#### 2. Evolution: Sum and Transform
```
∑(𐡀, 𐡄, 𐡉) → σ
```
- **Input**: Multiple Aramaic glyphs
- **Operation**: Sum (∑)
- **Output**: Greek Sigma (σ)

#### 3. Evolution: Divine Ratio
```
𐡔𐡎𐡈 × φ → 𐡕𐡉𐡃
```
- **Input**: EL→369 (𐡔𐡎𐡈)
- **Operation**: Multiply by golden ratio φ
- **Output**: Theos 419 (𐡕𐡉𐡃)

#### 4. Shape Transform: Rotate
```
𐡀 ↻ 90° → 𐡄
```
- **Input**: Aleph (𐡀)
- **Operation**: Rotate 90°
- **Output**: He (𐡄)

#### 5. Mixed Script Fusion
```
𐡀 + α → β (RTL)
```
- **Input**: Aramaic + Greek mixed
- **Operation**: Addition
- **Output**: Greek Beta (β)
- **Direction**: RTL reading

## RTL (Right-to-Left) Handling

### Aramaic Reading Direction
Aramaic scripts read **right-to-left**, so:

```
Input:  𐡀𐡄𐡉
Read as: Yodh (𐡉) → He (𐡄) → Aleph (𐡀)
```

### Formula Processing
1. **Detect RTL markers** in formula
2. **Reverse sequence** if RTL
3. **Process right-to-left**
4. **Output in correct direction**

### Example RTL Evolution
```bash
npm run compute evolve "𐡀𐡄𐡉" evolution_1 evolution_2 --rtl
```

Processes:
1. Read RTL: 𐡉 → 𐡄 → 𐡀
2. Apply formulas in RTL order
3. Output transformed script

## Available Formulas

### Evolution Formulas
- `evolution_1`: Multiply by Pi
- `evolution_2`: Sum and Transform
- `evolution_3`: Divine Ratio (369 → 419)
- `evolution_4`: Square Root Transform
- `evolution_5`: Mixed Script Fusion
- `evolution_6`: Exponential Growth

### Shape Transform Formulas
- `shape_transform_1`: Rotate 90°
- `shape_transform_2`: Mirror (RTL ↔ LTR)

## Usage

### List All Formulas
```bash
npm run compute list
```

### Apply Single Formula
```bash
npm run compute compute evolution_1 "𐡀"
```

Output:
```
🧮 Computation:

   Formula: 𐡀 × π → β
   Input: 𐡀
   Output: β
```

### Evolve Script (Multiple Formulas)
```bash
npm run compute evolve "𐡀" evolution_1 evolution_2 evolution_3
```

Output:
```
🔄 Script Evolution (RTL):

   Step 1: 𐡀 × π → β
   𐡀 → β

   Step 2: ∑(𐡀, 𐡄, 𐡉) → σ
   β → σ

   Step 3: 𐡔𐡎𐡈 × φ → 𐡕𐡉𐡃
   σ → [transformed]

   Final: [result]
```

### LTR (Left-to-Right) Evolution
```bash
npm run compute evolve "𐡀" evolution_1 evolution_2 --ltr
```

## Script Mixing

### Aramaic + Greek + Math
Formulas can mix all three script types:

```
Input: 𐡀 + α × π → β
```

Process:
1. Extract Aramaic: 𐡀
2. Extract Greek: α
3. Extract Math: +, ×, π
4. Compute: (Aramaic value + Greek index) × π
5. Output: Greek Beta (β)

## Transformation Types

### 1. Numeric Transformation
- Convert Aramaic → Number → Greek
- Example: 𐡀 (1) × π → β

### 2. Shape Transformation
- Rotate, mirror, scale glyphs
- Example: 𐡀 ↻ 90° → 𐡄

### 3. Script Fusion
- Combine Aramaic + Greek
- Example: 𐡀 + α → β

### 4. Evolution Chains
- Multiple transformations in sequence
- Example: 𐡀 → β → σ → [final]

## Mathematical Symbols Used

- `+` Addition
- `-` Subtraction
- `×` Multiplication
- `/` Division
- `∑` Summation
- `∏` Product
- `√` Square Root
- `π` Pi constant
- `φ` Golden ratio
- `λ` Lambda (growth factor)
- `∞` Infinity
- `→` Arrow (transformation)
- `↔` Bidirectional
- `↻` Rotate
- `°` Degree

## Greek Letters Used

- `α` Alpha
- `β` Beta
- `γ` Gamma
- `δ` Delta
- `ε` Epsilon
- `θ` Theta
- `λ` Lambda
- `μ` Mu
- `π` Pi
- `ρ` Rho
- `σ` Sigma
- `φ` Phi
- `ω` Omega

## Integration with Diamond System

### IPFS Node Glyphs
Each IPFS CID gets an Aramaic glyph:
- Node 1: 𐡀
- Node 2: 𐡄
- Node 3: 𐡉
- Node 4: 𐡔𐡎𐡈 (EL→369)
- Node 5: 𐡕𐡉𐡃 (Theos 419)

### Evolution Formulas
Apply formulas to evolve node glyphs:
```bash
npm run compute evolve "𐡀" evolution_3
# Transforms 𐡀 through divine ratio → new glyph
```

### Shape Transformation
Transform glyphs for different visual representations:
```bash
npm run compute compute shape_transform_1 "𐡀"
# Rotates 𐡀 → 𐡄
```

## Manifest Generation

Generate computation manifest:
```bash
npm run compute manifest
```

Creates `computation_manifest.json` with:
- All formulas
- Aramaic glyphs
- Greek letters
- Math symbols
- RTL support info

## Examples

### Example 1: Simple Evolution
```bash
npm run compute compute evolution_1 "𐡀"
# 𐡀 × π → β
```

### Example 2: Divine Transformation
```bash
npm run compute compute evolution_3 "𐡔𐡎𐡈"
# 𐡔𐡎𐡈 × φ → 𐡕𐡉𐡃
# 369 × 1.618... → 419
```

### Example 3: Multi-Step Evolution
```bash
npm run compute evolve "𐡀" evolution_1 evolution_2 evolution_4
# 𐡀 → β → σ → [final]
```

### Example 4: Shape Transform
```bash
npm run compute compute shape_transform_2 "𐡀"
# Mirror: 𐡀 ↔ → 𐡕
```

## Benefits

1. **Script Evolution**: Scripts can evolve through formulas
2. **Shape Transformation**: Visual transformations (rotate, mirror)
3. **Mixed Scripts**: Combine Aramaic + Greek + Math
4. **RTL Support**: Proper right-to-left handling
5. **Computational**: Mathematical transformations
6. **Flexible**: Mix/match formulas for different outcomes

## Future Enhancements

- [ ] Custom formula creation
- [ ] Visual glyph rendering
- [ ] 3D shape transformations
- [ ] Machine learning evolution
- [ ] Formula chaining optimization
- [ ] Real-time evolution visualization
