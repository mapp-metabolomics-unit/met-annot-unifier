# Contributing to `met-annot-unifier`

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

You can contribute in many ways:

# Types of Contributions

## Report Bugs

Report bugs at https://github.com/mapp-metabolomics-unit/met-annot-unifier/issues

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

## Fix Bugs

Look through the GitHub issues for bugs.
Anything tagged with "bug" and "help wanted" is open to whoever wants to implement a fix for it.

## Implement Features

Look through the GitHub issues for features.
Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

## Write Documentation

met-annot-unifier could always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts, articles, and such.

## Submit Feedback

The best way to send feedback is to file an issue at https://github.com/mapp-metabolomics-unit/met-annot-unifier/issues.

If you are proposing a new feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

# Get Started!

Ready to contribute? Here's how to set up `met-annot-unifier` for local development.
Please note this documentation assumes you already have `uv` and `Git` installed and ready to go.

1. Fork the `met-annot-unifier` repo on GitHub.

2. Clone your fork locally:

```bash
cd <directory_in_which_repo_should_be_created>
git clone git@github.com:YOUR_NAME/met-annot-unifier.git
```

3. Now we need to install the environment. Navigate into the directory

```bash
cd met-annot-unifier
```

Then, install and activate the environment with:

```bash
uv sync
```

4. Install pre-commit to run linters/formatters at commit time:

```bash
uv run pre-commit install
```

5. Create a branch for local development:

```bash
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

6. Don't forget to add test cases for your added functionality to the `tests` directory.

7. When you're done making changes, check that your changes pass the formatting tests.

```bash
make check
```

Now, validate that all unit tests are passing:

```bash
make test
```

9. Before raising a pull request you should also run tox.
   This will run the tests across different versions of Python:

```bash
tox
```

This requires you to have multiple versions of python installed.
This step is also triggered in the CI/CD pipeline, so you could also choose to skip this step locally.

10. Commit your changes and push your branch to GitHub:

```bash
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

11. Submit a pull request through the GitHub website.

# Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated.
   Put your new functionality into a function with a docstring, and add the feature to the list in `README.md`.

# Release a New Version

Releases are published from `main`. As of writing, the latest tag is `0.1.0`;
choose a new, unused version (for example, `0.1.1`). A GitHub release triggers
`.github/workflows/on-release-main.yml`, which builds and uploads the package
to PyPI using the `PYPI_TOKEN` GitHub Actions secret. You need push access and
the GitHub CLI (`gh`) authenticated, or you can publish the release in the
GitHub web interface instead.

1. After merging the changes to `main`, update your checkout and set the
   `[project]` version in `pyproject.toml` to the new version (without a `v`
   prefix). Update the lock file and check the changes:

   ```bash
   git switch main
   git pull --ff-only origin main
   # Edit pyproject.toml: version = "0.1.1"
   uv lock
   make check
   make test
   ```

2. Commit the version and lock file, then push the commit and its matching
   tag to GitHub:

   ```bash
   git add pyproject.toml uv.lock
   git commit -m "Release 0.1.1"
   git push origin main
   git tag 0.1.1
   git push origin 0.1.1
   ```

3. Publish the GitHub release for that tag (pushing a tag alone does **not**
   trigger the PyPI upload):

   ```bash
   gh release create 0.1.1 --verify-tag --title 0.1.1 --generate-notes
   ```

   Alternatively, select the existing tag at
   [New release](https://github.com/mapp-metabolomics-unit/met-annot-unifier/releases/new)
   and click **Publish release**. Check the
   [release workflow](https://github.com/mapp-metabolomics-unit/met-annot-unifier/actions/workflows/on-release-main.yml)
   succeeds, then check that `0.1.1` appears on
   [PyPI](https://pypi.org/project/met-annot-unifier/). Do not run `make publish`
   as well: the workflow handles the PyPI upload.
