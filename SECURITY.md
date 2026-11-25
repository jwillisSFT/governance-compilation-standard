# Security Policy

## Scope

This repository contains specification material, schemas, examples, and bounded validation code. It is not a production runtime service.

Report security issues involving:

- a specification ambiguity that permits authority expansion;
- a schema weakness that invalidates a mandatory semantic constraint;
- a validation defect that incorrectly accepts a known invalid fixture;
- a supply-chain issue in release tooling;
- accidental disclosure of credentials, private keys, tokens, or non-public implementation information.

## Do not commit secrets

This repository must not contain production credentials, signing keys, private certificates, customer data, tenant configuration, internal deployment topology, or proprietary AGCP source/configuration.

Example cryptographic values must be obviously non-secret placeholders.

## Security claim boundary

A conforming package can require non-bypassable enforcement, but package conformance does not prove that a deployment is non-bypassable. Deployment claims require independent route, identity, configuration, and target-side evidence within a declared boundary.
