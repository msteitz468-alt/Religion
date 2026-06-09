# E2E Test Infra: Religion Wiki Extraction

## Test Philosophy
- Opaque-box, requirement-driven. No dependency on implementation design.
- Methodology: Category-Partition + BVA + Pairwise + Workload Testing.

## Feature Inventory
| # | Feature | Source (requirement) | Tier 1 | Tier 2 | Tier 3 |
|---|---------|---------------------|:------:|:------:|:------:|
| 1 | Process all 47 commentaries in mapping.json | ORIGINAL_REQUEST R1 | 5 | 5 | ✓ |
| 2 | Non-destructively inject narrative info | ORIGINAL_REQUEST R2 | 5 | 5 | ✓ |
| 3 | Create/update figure pages per schema | ORIGINAL_REQUEST R3 | 5 | 5 | ✓ |
| 4 | Append new figure pages to index.md | ORIGINAL_REQUEST R4 | 5 | 5 | ✓ |

## Test Architecture
- Test runner: `tests/run_tests.sh` - iterates over test directories and executes scripts, expecting exit code 0.
- Test case format: Executable scripts (bash or python) inside `tests/tierX/` directories.
- Directory layout:
  - `tests/run_tests.sh`
  - `tests/tier1_feature_coverage/`
  - `tests/tier2_boundary_cases/`
  - `tests/tier3_cross_feature/`
  - `tests/tier4_real_world/`

## Real-World Application Scenarios (Tier 4)
| # | Scenario | Features Exercised | Complexity |
|---|----------|--------------------|------------|
| 1 | Validate End-to-End Extraction for specific raw file | F1, F2, F3, F4 | High |
| 2 | Figure page completeness and index presence | F3, F4 | Medium |
| 3 | Non-destructive narrative updates | F2 | High |
| 4 | Mapping.json exhaustive processing verification | F1 | High |
| 5 | CLAUDE.md Schema Compliance for all figures | F3 | High |

## Coverage Thresholds
- Tier 1: ≥5 per feature (Total 20)
- Tier 2: ≥5 per feature (where boundaries exist) (Total 20)
- Tier 3: pairwise coverage of major feature interactions (Total 6)
- Tier 4: ≥5 realistic application scenarios (Total 5)
