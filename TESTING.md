# Testing Strategy (Quick-Calc)

## 1. Overall strategy
The goal is to test calculator operations and ensure correct results for normal inputs and edge cases.
The focus is on logic correctness (no UI).

## 2. Lecture concept reference
- Unit testing: test each operation function separately
- Integration testing: test a small flow using multiple functions together
- Edge cases: division by zero, negative numbers, decimals, large numbers
- Regression: run the same test suite after every change

## 3. Testing pyramid
Most tests are unit tests because they are fast and check logic in isolation.
A small number of integration tests check that key flows work end-to-end.

## 4. Black-box vs White-box
- Black-box: verify input/output behavior without relying on internal details.
- White-box: test each operation function directly knowing the internal structure.

## 5. Functional vs Non-functional
- Functional tested: correctness of operations, clear behavior, division by zero error.
- Not tested (non-functional): performance, security, UI/UX, accessibility.

## 6. Regression testing
If new features are added, the same tests should be run again.
New tests should be added for new functions.

## 7. Test results summary
| Test name | Type | Result |
|---|---|---|
| test_add_positive_numbers | Unit | Pass |
| test_subtract_positive_numbers | Unit | Pass |
| test_multiply_positive_numbers | Unit | Pass |
| test_divide_positive_numbers | Unit | Pass |
| test_divide_by_zero_raises | Unit | Pass |
| test_add_negative_numbers | Unit | Pass |
| test_divide_decimal_result | Unit | Pass |
| test_multiply_large_numbers | Unit | Pass |
| test_full_flow_like_user_action | Integration | Pass |
| test_clear_resets_to_zero | Integration | Pass |