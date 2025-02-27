How to do a release
###################

We use calendar versioning, similar to the `twisted/twisted` project.

To do a release, follow these steps:

* Create a new branch. You can name the branch `release-YEAR.MONTH`.
* Update the `[metadata] version` inside `setup.cfg`
* Update the `Changelog.rst` file with the summary of the changes.
* Commit the changes to GitHub and create a PR
* Request the review from `twisted-contributors` team.
* Once the PR is approved create a `git tag` based on the latest commit from
  the PR.
  The tag name should be the current version.
* Push the tag to Github.
  This will automatically trigger the build process for the wheels and will
  publish them to PyPI


Implementation details
======================

To publish to PyPi, the GitHub Action workflow needs to be named `github-deploy.yml`.
You can `reconfigure this via PyPi <https://pypi.org/manage/project/twisted-iocpsupport/settings/publishing/>`_.

The binary wheels are generated using `cibuildwheel`.
To build wheels for newer Python version you might need to update the version
of `cibuildwheel`.

To disable building binaries for older Python version you might need to
edit the `[tool.cibuildwheel]` section from the `pyproject.toml` file.

GitHub Action is used to run `cibuildwheel` to generate the wheels on any
commit pushed to the main branch, to a PR or a tag.

Any tag pushed that has a name starting with `v` will trigger the publishing
to the production PyPI site.
