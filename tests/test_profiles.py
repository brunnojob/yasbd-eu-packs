import pytest
from yasbd import BoundaryDetector
from yasbd.rules import load_external_lang_packs

from tests.data import croatian, finnish, hungarian, latvian, slovenian
from yasbd_eu_packs import PROFILES

CASES = [
    (module.ISO_CODE, text)
    for module in [latvian, hungarian, croatian, finnish, slovenian]
    for text in module.TEST_DATA
]


@pytest.mark.parametrize("lang,text", CASES)
def test_segmentation(lang, text):
    detector = BoundaryDetector(lang=lang, external_lang_packs=["yasbd_eu_packs"])
    assert list(detector.segment(text.replace("|", ""))) == [
        part.strip() for part in text.split("|")
    ]


def test_registration():
    registry = load_external_lang_packs(["yasbd_eu_packs"])
    assert set(registry) == {"lv", "hu", "hr", "fi", "sl"}
    assert len(PROFILES) == 5


@pytest.mark.parametrize("lang", ["lv", "hu", "hr", "fi", "sl"])
def test_terminal_punctuation(lang):
    detector = BoundaryDetector(lang=lang, external_lang_packs=["yasbd_eu_packs"])
    assert list(
        detector.segment(
            "This sentence has several words! Does this sentence split correctly? The final sentence ends here."
        )
    ) == [
        "This sentence has several words!",
        "Does this sentence split correctly?",
        "The final sentence ends here.",
    ]
