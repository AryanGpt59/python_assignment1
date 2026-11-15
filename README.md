# Python Assignment 1 — Solutions

Solutions are grouped by the headings in the supplied assignment screenshots. Each topic file contains reusable functions/classes and a runnable example under `if __name__ == "__main__"`.

## Run the programs

Use Python 3.10 or newer. Extract the ZIP, open a terminal in the `python_assignment` folder, then run for example:

```bash
python conditional/conditional.py
python loops/loops.py
python strings/strings.py
python data_structures/data_structures.py
python functions_recursion/functions_recursion.py
python exceptions/exceptions.py
python modules/module_examples.py
python oop/oop.py
python -m modules.geometry_demo
```

## Notes on assumptions

- **Electricity bill:** slabs are progressive: first 100 units at Rs. 5, next 200 at Rs. 7, and units above 300 at Rs. 10. The 5% surcharge is applied to the calculated bill only when it exceeds Rs. 2,000.
- **Loan approval:** all three listed conditions passing means Approved; exactly two passing means Conditionally Approved; fewer than two means Rejected. The assignment does not define the conditional-approval rule, so this is an explicit practical interpretation.
- **Exam division:** the average is used for division, after checking whether any subject mark is below 33. The listed ranges do not specify a division below 40, so that case is labelled `Pass (no division specified)`.
- **String compression:** every run is represented as character followed by its count, including count 1 (e.g. `aaabbc` becomes `a3b2c1`), matching the example.
- **Missing number:** assumes distinct integers from 1 through n with exactly one missing.
- **Password retry:** the sample correct password is `python123`; change it in the source if your instructor expects a different value.
- **Password validation:** custom exception is raised if any of the three stated rules fail.
- **Random password:** uses Python's `secrets`-backed `SystemRandom` selection; OTP uses random digits for this basic assignment exercise.

## Geometry package

The `geometry` folder is a Python package with `circle.py` and `rectangle.py`. Run its example from the assignment root using `python -m modules.geometry_demo`.
