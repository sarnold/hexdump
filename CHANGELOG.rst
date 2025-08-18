Changelog
=========


3.5.3 (2025-08-18)
------------------

Fixes
~~~~~
- Remove deprecated version attribute from package metadata. [Stephen L
  Arnold]


3.5.2 (2025-07-22)
------------------

Changes
~~~~~~~
- Relax setuptools_scm version, fix mypy error, cleanup test cfg.
  [Stephen L Arnold]

  * update pre-commit hook versions, apply format controls, update changelog

Fixes
~~~~~
- Rename bandit workflow job name to workaround weird hang. [Stephen L
  Arnold]

  * this has been holding up automerge waiting for security_check
    after it worked fine for a few weeks
  * remove deprecated 20.04 instance left over in coverage workflow
- Remove extraneous job name from release workflow. [Stephen L Arnold]

Other
~~~~~
- Merge pull request #20 from sarnold/el9-compat-versions. [Steve
  Arnold]

  packaging and cleanup
- Merge pull request #15 from sarnold/fix-rule-checks. [Steve Arnold]

  CI fixes
- Merge pull request #13 from sarnold/release-cleanup. [Steve Arnold]

  shared workflow cleanup


3.5.1 (2025-03-21)
------------------

Changes
~~~~~~~
- Remove py312 from conda workflow, bump changelog and version. [Stephen
  L Arnold]
- Update changelog, cleanup tox file and history. [Stephen L Arnold]
- Try flexible priority for py313, cleanup branch names. [Stephen L
  Arnold]
- Add reuse config and migrate to LICENSES folder, cleanup lint.
  [Stephen L Arnold]

  * add sec and reuse envs to tox file, update tool cfg

Fixes
~~~~~
- Disable py313 in conda workflow, cleanup readme nits. [Stephen L
  Arnold]
- Cleanup artifact names for included wheel workflow. [Stephen L Arnold]
- Update conda recipe with new version, license, depends. [Stephen L
  Arnold]

Other
~~~~~
- Merge pull request #12 from sarnold/nit-fixes2. [Steve Arnold]

  Conda and changelog
- Merge pull request #11 from sarnold/nit-fixes. [Steve Arnold]

  Fix some nits
- Merge pull request #10 from sarnold/changelogs. [Steve Arnold]

  Changelogs and cleanup
- Merge pull request #9 from sarnold/cruft-cleanup. [Steve Arnold]

  Cleanup cruft from separate workflows
- Merge pull request #8 from sarnold/refurbish. [Steve Arnold]

  workflow env cleanup
- Merge pull request #7 from sarnold/refurbish. [Steve Arnold]

  Refurb packaging and workflows


3.5.0 (2023-09-11)
------------------

New
~~~
- Switch to dynamic versioning, use setuptools-scm. [Stephen L Arnold]

  * basic pep517 mode, no version file or full toml project cfg
- Add pre-commit cfg and new channgelog file, cleanup formatting.
  [Stephen L Arnold]

  * add/update more tool config files and tox cmds
- Add coverage workflow and one more test, cleanup readme. [Stephen L
  Arnold]

Changes
~~~~~~~
- Update coverage workflow and packaging. [Stephen L Arnold]
- Add simple test file, remove python2 support. [Stephen L Arnold]
- Still more modernization, use pytest instead of nose. [Stephen L
  Arnold]

  * cleanup and update workflows and pkging/config files

Fixes
~~~~~
- Cleanup packaging and tox file. [Stephen L Arnold]

  * use proper/modern constructs and syntax, bump py versions

Other
~~~~~
- Update new changelog for release. [Stephen L Arnold]
- Merge pull request #6 from sarnold/cleanup2. [Steve Arnold]

  modernize packaging and tox file
- Even more modernizing, swap out optparse, swap in argparse. [Stephen L
  Arnold]

  * note this should emulate the original behavior
- Doc: use current issues link, reformat history file. [Stephen L
  Arnold]


3.4.0 (2021-03-08)
------------------

Changes
~~~~~~~
- Add conda recipe and workflow, update readme. [Stephen L Arnold]
- Add pylint/custom badge workflow, reset codeclimate cfg. [Stephen L
  Arnold]
- Cleanup doctests so they run with py3, update history and readme.
  [Stephen L Arnold]
- Test examples, update/reformat readme. [Stephen L Arnold]

Fixes
~~~~~
- Cleanup lint, packaging, tox envs (#2) [Steve Arnold]

  * update tox env/cfg and cleanup some lint and reformat source
  * revert to original entry-point name, cleanup MANIFEST, update tox
  * update ci workflows (add release and wheel artifact check)
  * sync up workflow triggers, run src test with python

Other
~~~~~
- Merge pull request #5 from sarnold/conda. [Steve Arnold]

  chg: add conda recipe and workflow, update readme
- Fix minor formatting glitch in readme, prep for release. [Stephen L
  Arnold]
- Merge pull request #4 from sarnold/pylint. [Steve Arnold]

  chg: add pylint/custom badge workflow, reset codeclimate cfg
- Merge pull request #3 from sarnold/doc-updates. [Steve Arnold]

  fix: doctest/examples and docs
- Bump version for release, fix branch name in workflows. [Stephen L
  Arnold]
- Bump version 3.3 -> 3.3-1 and update readme. [Stephen L Arnold]
- Merge pull request #1 from sarnold/v3.3. [Steve Arnold]

  packaging cleanup
- Hard-code version, rename console_script, update tox cfg. [Stephen L
  Arnold]


3.3 (2020-11-13)
----------------
- Add origin note to readme. [Stephen L Arnold]
- Remove crufty files and wheel, setuptools handling, push version to
  40.8.0. [Stephen L Arnold]
- Add simple python CI runner. [Stephen L Arnold]
- Re-format as modern project directory using PEP 517 setup files.
  [Stephen L Arnold]
- Initial commit. [Steve Arnold]
