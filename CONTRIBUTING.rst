The PyPI package publishing is done automatically via GitHub actions when a new tag is pushed.

To push a tag and trigger the release for new version::

    pipx run --pip-args="cython" --spec="zest.releaser[recommended]>=6.22.1" fullrelease

You can also apply this process manually:

* Create a new branch with the name `release-VER` (ex release-1.1.0) No need to create a separate issue.
* On that branch update the version from `setup.cfg ` to the final version to be released.
* Update the  CHANGELOG.rst file with the final version and release date.
* Push the commit and record the commit SHA as this will be the one used to tag and do the release.
* Include the tagged commit to the PR description.
* On the same branch, update the `setup.cfg ` to a `.dev0` version and update CHANGELOG.rst to a new empty unreleased section.
* Push the latest commit and request a review for the PR.
* Once the PR is approved, you can merge the PR
* After the merge, push the release tag. GitHub action will take care of the release.

You can check the GitHub actions release process here https://github.com/twisted/twisted-iocpsupport/actions

Below is the template text for the unreleased NEWS section::

    1.0.1 (unreleased)
    ------------------

    - Nothing changed yet.
