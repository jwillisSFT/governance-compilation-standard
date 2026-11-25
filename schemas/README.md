# Schemas

The v0.1.0 interchange profile uses JSON Schema 2020-12.

These schemas define interoperable representations; they do not require a compiler or runtime to use JSON internally.

`gir.schema.json` is intentionally self-contained for simple validation. Component schemas provide separately addressable artifact contracts.

Schema validation establishes structural conformance only. It does **not** establish semantic properties such as authority-space closure, satisfiability, no-silent-weakening, projection soundness, closure reachability, or deployment non-bypassability. Those require the additional analyses described in `formal/` and `conformance/`.
