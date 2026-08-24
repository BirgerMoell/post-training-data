# European language identifiers

Dataset entries use ISO 639-3 plus ISO 15924 identifiers, matching the OpenEuroLLM training-data catalogue. A broad label such as “multilingual” is useful for discovery but does not replace measured per-language coverage.

## Official EU languages

| Language | Catalogue code(s) |
| --- | --- |
| Bulgarian | `bul_Cyrl` |
| Croatian | `hrv_Latn` |
| Czech | `ces_Latn` |
| Danish | `dan_Latn` |
| Dutch | `nld_Latn` |
| English | `eng_Latn` |
| Estonian | `est_Latn`, `ekk_Latn` |
| Finnish | `fin_Latn` |
| French | `fra_Latn` |
| German | `deu_Latn` |
| Greek | `ell_Grek` |
| Hungarian | `hun_Latn` |
| Irish | `gle_Latn` |
| Italian | `ita_Latn` |
| Latvian | `lav_Latn`, `ltg_Latn`, `lvs_Latn` |
| Lithuanian | `lit_Latn` |
| Maltese | `mlt_Latn` |
| Polish | `pol_Latn` |
| Portuguese | `por_Latn` |
| Romanian | `ron_Latn` |
| Slovak | `slk_Latn` |
| Slovenian | `slv_Latn` |
| Spanish | `spa_Latn` |
| Swedish | `swe_Latn` |

## Co-official, candidate, and associated languages

| Group | Language | Catalogue code(s) |
| --- | --- | --- |
| Co-official | Basque | `eus_Latn` |
| Co-official | Catalan | `cat_Latn` |
| Co-official | Galician | `glg_Latn` |
| EU candidate | Albanian | `sqi_Latn`, `als_Latn` |
| EU candidate | Bosnian | `bos_Latn` |
| EU candidate | Georgian | `kat_Geor` |
| EU candidate | Macedonian | `mkd_Cyrl` |
| EU candidate | Serbian | `srp_Cyrl`, `srp_Latn` |
| EU candidate | Turkish | `tur_Latn` |
| EU candidate | Ukrainian | `ukr_Cyrl` |
| Associated | Icelandic | `isl_Latn` |
| Associated | Norwegian | `nor_Latn`, `nno_Latn`, `nob_Latn` |

`zxx_Zyyy` is used for non-linguistic code data and `und_Zyyy` only when language/script is genuinely unspecified. Replace both with measured language/script identifiers whenever possible.

Per-language tables should report documents, segments, tokens, length, and characters when those measures have been reproduced for that dataset version. Comparable token totals use the official catalogue tokenizer, currently Gemma 3, with an immutable revision; training-tokenizer counts must be labelled separately.
