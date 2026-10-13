from yasbd.rules.base import Rules


# fmt: off
class FiRules(Rules):


    TITLE_ABBRVS = Rules.TITLE_ABBRVS | {
        # Academic & Professional
        "dos", "toht", "tri", "fil", "maist", "ins", "dipl.ins",
        "kand", "yliopp",

        # Social
        "hra", "rva", "nti",

        # Roles
        "joht", "nimim", "pj", "puh.joht", "siht", "toim", "yo",
    }

    REFERENCE_ABBRVS = Rules.REFERENCE_ABBRVS | {
        # Layout & Citations
        "s", "ss", "kpl", "kuv", "taul", "liite", "ks", "vrt", "huom",
        "nro", "n:o", "mom", "kohta", "aik", "alk", "alv", "ed", "k",
        "ko", "lk", "lkm", "lyh", "läh", "nyk", "oik", "par", "per",
        "puh", "rak", "srk", "synt", "t", "tark", "til", "vas", "vast",
        "vm", "po", "so", "yl",

        # Legal Reference Identifiers
        "pykälä", "ao", "em", "ml",
    }

    INLINE_ONLY_ABBRVS = Rules.INLINE_ONLY_ABBRVS | {
        "esim", "mm", "jne", "ym", "yms", "tms", "ts", "ns",
        "n", "mrd", "milj", "klo", "eaa", "jaa", "os", "pl",
        "as", "miel", "myöh",
    }

    SECTION_MARKERS = Rules.SECTION_MARKERS | {
        "Luku", "Osa", "Kohta", "Liite", "Pykälä", "Momentti",
    }

    DATE_ABBRVS = Rules.DATE_ABBRVS | {
        # Months
        "tammik", "helmik", "maalisk", "huhtik", "toukok", "kesäk",
        "heinäk", "elok", "syysk", "lokak", "marrask", "jouluk",

        # Days
        "ma", "ti", "ke", "to", "pe", "la", "su", "ark", "pvm",
    }

    CORP_ENTITY_ABBRVS = Rules.CORP_ENTITY_ABBRVS | {
        "RY", "YHT",
    }

# fmt: on
