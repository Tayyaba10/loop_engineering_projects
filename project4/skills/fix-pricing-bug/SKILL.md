# Fix pricing bug

Use this skill when fixing a bug in pricing.py.

## Steps

1. Read the failing test to understand the expected behavior.
2. Make the smallest possible change that fixes the actual formula.
3. Do not change the function's name or its parameters.
4. Do not add unrelated code.

## Hard rule (the reviewer checks this)

The fix must be a **general formula** that would work for any input,
not just the numbers used in the test. Hardcoding the test's specific
input or output values (for example, special-casing total=200 or
returning 180 directly) is not a real fix. It is a shortcut that only
looks correct.
