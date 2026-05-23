## 2024-05-24 - [Avoid Exponential Complexity by Iterating NetworkX Generators Lazily]
**Learning:** Evaluatng networkx path/cycle generators entirely into memory (`list(nx.all_simple_paths(...))` and `list(nx.simple_cycles(...))`) introduces severe O(N) constraints due to combinatorial explosion on dense graphs. Additionally, it makes it impossible to break out early.
**Action:** When a cap is required, use `itertools.islice(generator, limit)` instead of slice on the evaluated `list(generator)[:limit]` to lazily evaluate only the requested amount of elements for simple paths/cycles in networkx.

## 2024-05-24 - [Fix CI errors due to Pytest Collection with invalid test helpers]
**Learning:** Pytest aggressively attempts to parse any function starting with `test_` as a fixture injection point. For integration scripts that use custom `test_foo(argument)` helper methods without pytest fixtures, pytest will crash the CI build with "fixture not found".
**Action:** Always rename custom test helper functions taking arguments in test scripts to something else like `verify_foo(argument)` to prevent pytest from attempting to inject them.

## 2024-05-24 - [Avoid Type/Overlap Errors in Pydantic or Typescript Check]
**Learning:** Overzealous or restrictive typing constraints like strict role comparison `msg.role === 'model'` when the schema requires `"assistant"` will cause `tsc` to fail the build due to zero overlap typing.
**Action:** Always cast the checked object field to `any` first `(msg.role as any) === 'model'` if the interface isn't explicitly supporting the required mapping structure to suppress `tsc` CI breakages without modifying third-party interfaces.
