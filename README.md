# Wingmate POC scan repository

This private repository contains intentional vulnerabilities for a controlled Wingmate POC.
Do not deploy this application. All records are synthetic.

The Flask endpoint passes an untrusted name into a SQLite lookup.
The SQL injection regression test fails before the fix.

Run the regression tests:

```sh
python -m unittest discover -s tests
```

The POC can create branches and pull requests under `wingmate/*`.
No real customer data or credentials belong in this repository.
