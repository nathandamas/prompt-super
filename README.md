[![DOI](https://zenodo.org/badge/968695322.svg)](https://doi.org/10.5281/zenodo.15242949)

# Prompt Super (Generic Multidisciplinary Version)

**Prompt Super** is a fully–featured template prompt that guides large‑language‑model
assistants through every stage of academic writing: diagnosis, restructuring,
editing, formatting, reproducibility and dissemination.  
It is discipline‑agnostic: just fill in the `⚙️[[…]]` placeholders and paste
the prompt into ChatGPT (or any LLM).

<p align="center">
  <img src="docs/img/logo_prompt_super.svg" width="220" alt="Prompt Super logo"/>
</p>

---

## Quick Start

```bash
git clone https://github.com/YOUR-USERNAME/prompt-super.git
cd prompt-super
open prompt_super_generic.md
```

* Choose a language variant from `examples/`.
* Replace the placeholder fields `⚙️[[…]]`.
* Copy the prompt into your LLM session.
* Follow the interactive workflow (Questions → Outline → Rewrites …).

## Multilingual Versions

| Language | File |
|----------|------|
| Português | [examples/prompt_super_generic_pt.md](examples/prompt_super_generic_pt.md) |
| 简体中文 (Mandarin) | [examples/prompt_super_generic_zh.md](examples/prompt_super_generic_zh.md) |
| Español | [examples/prompt_super_generic_es.md](examples/prompt_super_generic_es.md) |
| English | [examples/prompt_super_generic_en.md](examples/prompt_super_generic_en.md) |
| हिन्दी (Hindi) | [examples/prompt_super_generic_hi.md](examples/prompt_super_generic_hi.md) |
| العربية الفصحى | [examples/prompt_super_generic_ar.md](examples/prompt_super_generic_ar.md) |
| Русский | [examples/prompt_super_generic_ru.md](examples/prompt_super_generic_ru.md) |
| বাংলা (Bengali) | [examples/prompt_super_generic_bn.md](examples/prompt_super_generic_bn.md) |
| 日本語 (Japanese) | [examples/prompt_super_generic_ja.md](examples/prompt_super_generic_ja.md) |

## Directory Layout

```
prompt-super/
│  prompt_super_generic.md
│  LICENSE
│  README.md
│  CONTRIBUTING.md
│  CODE_OF_CONDUCT.md
│  CHANGELOG.md
│  CITATION.cff
│  .gitignore
│
├─ examples/
│   ├─ example_science.md
│   └─ example_engineering.md
│
├─ templates/
│   ├─ outline_table_template.md
│   ├─ graphic_abstract_template.svg
│   └─ cover_letter_template.md
│
├─ scripts/
│   ├─ generate_prompt.py
│   └─ check_guidelines.py
│
└─ docs/
    ├─ index.md
    └─ faq.md
```

## Contributing

We welcome pull requests — please read `CONTRIBUTING.md` first.

## License

* **Code**: MIT License  
* **Prompt & documentation**: Creative Commons Attribution 4.0

---

© 2025 Nathan Damas
