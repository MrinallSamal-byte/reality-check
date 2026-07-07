#!/usr/bin/env python3
"""Version-consistency guard.

Reality Check declares its version in four manifests plus the CHANGELOG, and
every release bumps all of them by hand. Manifests that merely agree with each
other can still all be stale together, so this also checks the release tag on
tag builds (GITHUB_REF_TYPE/GITHUB_REF_NAME, set by GitHub Actions).
"""
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
PINNED = re.compile(r"^\d+\.\d+\.\d+$")


def read_json(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8-sig") as f:
        return json.load(f)


versions = [
    ("package.json", read_json("package.json")["version"]),
    (".claude-plugin/plugin.json", read_json(".claude-plugin/plugin.json")["version"]),
    ("gemini-extension.json", read_json("gemini-extension.json")["version"]),
]
marketplace = read_json(".claude-plugin/marketplace.json")
versions.append((".claude-plugin/marketplace.json (metadata)", marketplace["metadata"]["version"]))
versions.append((".claude-plugin/marketplace.json (plugin)", marketplace["plugins"][0]["version"]))

with open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8") as f:
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\]", f.read(), re.M)
if not m:
    sys.exit("CHANGELOG.md has no '## [X.Y.Z]' release heading")
versions.append(("CHANGELOG.md (latest entry)", m.group(1)))

failed = False
for name, v in versions:
    if not PINNED.match(v):
        print(f"{name}: version must be pinned X.Y.Z, got {v!r}", file=sys.stderr)
        failed = True

if len({v for _, v in versions}) > 1:
    print("Version mismatch — every file must share one version:", file=sys.stderr)
    for name, v in versions:
        print(f"  {v}\t{name}", file=sys.stderr)
    failed = True
else:
    shared = versions[0][1]
    # On a release-tag CI run the shared version must equal the tag — catches
    # tagging a release whose version files were never bumped.
    if os.environ.get("GITHUB_REF_TYPE") == "tag":
        tag = os.environ.get("GITHUB_REF_NAME", "").lstrip("v")
        if PINNED.match(tag) and tag != shared:
            print(f"release tag v{tag} does not match version {shared}; bump before tagging", file=sys.stderr)
            failed = True

if failed:
    sys.exit(1)
print(f"All {len(versions)} version fields pinned at {versions[0][1]}.")
