# Contributing

## Issues

Bug reports, questions, or feature requests can be submitted as [GitHub issues](https://github.com/jamesturk/projname/issues).

## Developing Locally

0. Before starting, you'll need [poetry](https://python-poetry.org/docs/#installation) installed.
  [pre-commit](https://pre-commit.com/#install) is also recommended.

0. Fork `projname` and check out your fork:
  ``` console
  $ git clone git@github.com:<your username>/projname.git
  ```

0. Install pre-commit hooks
  ```
  $ pre-commit install
  ```
  This will make sure that the linters run before each commit, saving you time.

0. Install `projname` and its development dependencies locally:
  ```
  $ cd projname
  $ poetry install
  ```

0. Optional: Install `just`

  https://github.com/casey/just#installation

  Doing this will give you helpful shortcuts for running common commands.

### Common Commands

* `just test` - run tests
* `just lint` - run linters
* `just docs` - build docs
