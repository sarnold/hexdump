Changelog
=========


1.7.2 (2025-03-20)
------------------

Changes
~~~~~~~
- Try flexible priority for py313, cleanup branch names. [Stephen L
  Arnold]
- Add reuse config and migrate to LICENSES folder, cleanup lint.
  [Stephen L Arnold]

  * add sec and reuse envs to tox file, update tool cfg

Fixes
~~~~~
- Cleanup artifact names for included wheel workflow. [Stephen L Arnold]
- Update conda recipe with new version, license, depends. [Stephen L
  Arnold]

Other
~~~~~
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


