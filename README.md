# yasbd-eu-packs

External language profiles for Latvian (`lv`), Hungarian (`hu`), Croatian (`hr`), Finnish (`fi`) and Slovenian (`sl`). Uses the public `PROFILES` API; does not modify yasbd core modules.

## Install

```sh
pip install git+https://github.com/brunnojob/yasbd-eu-packs.git
```

## Use

```python
from yasbd import BoundaryDetector

detector = BoundaryDetector(lang="fi", external_lang_packs=["yasbd_eu_packs"])
assert list(detector.segment("Tämä on esim. hyvä ratkaisu. Se toimii.")) == [
    "Tämä on esim. hyvä ratkaisu.",
    "Se toimii.",
]
```

Pass `external_lang_packs` explicitly for every detector. Installing this package alone does not register new built-in languages. Supports yasbd 1.x and Python 3.10+.

## Verify

```sh
pip install ".[test]"
pytest -q
ruff check .
python -m build
```

The test suite exercises all 60 original language examples through the external-pack API, registration and punctuation boundaries. Abbreviation coverage is conservative and has not been independently validated by native speakers.

## Attribution

Language rules and original test fixtures by [raffaelemancuso](https://github.com/raffaelemancuso), from [yasbd-lib PR #335](https://github.com/speedyk-005/yasbd-lib/pull/335), commit `8660c1e70c78ee9eb66856ba53cb417a25953469`. External packaging and integration tests prepared for [brunnojob](https://github.com/brunnojob). yasbd core by [speedyk-005](https://github.com/speedyk-005). Licensed under MPL-2.0; see LICENSE.

The maintainer requested external distribution because built-in language additions are frozen. This package is a migration of the proposed rules, not an official yasbd pack or an accepted upstream change.
