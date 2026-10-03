---
name: Higgs Camera Review
author: KamHiggs
license: MIT
open_source: true
stable: false
maintained: true
pypi: false
github: https://github.com/KamHiggs/higgs-camera-change-review
issue_tracker: https://github.com/KamHiggs/higgs-camera-change-review/issues
website: https://github.com/KamHiggs/higgs-camera-change-review/releases/tag/inventree-v0.1.3-correction.1
categories:
    - Integration
tags:
    - Camera
    - Engineering review
    - Offline verification
---

Experimental camera change review demonstrated with InvenTree 1.5.6.

The plugin preserves a camera assessment and its declared inputs, flags the saved assessment when relevant inventory declarations change, and exports a record that can be rechecked outside InvenTree with its matching verifier.

Start with the [recorded walkthrough](https://github.com/KamHiggs/higgs-camera-change-review/blob/inventree-v0.1.3-correction.1/docs/DEMONSTRATION.md), [release and installation notes](https://github.com/KamHiggs/higgs-camera-change-review/releases/tag/inventree-v0.1.3-correction.1), or [tagged integration source](https://github.com/KamHiggs/higgs-camera-change-review/tree/inventree-v0.1.3-correction.1). The repository's default branch retains an earlier standalone application; use the integration release for this plugin.

The current demonstration uses a fixed synthetic installation model and manually configured bindings. It is not a general camera compatibility tool or hardware approval. Verification acceptance concerns the recorded decision, not permission to install the camera. Installation, exact build matching, and other [known limitations](https://github.com/KamHiggs/higgs-camera-change-review/blob/inventree-v0.1.3-correction.1/docs/KNOWN_LIMITATIONS.md) are documented. The offline verifier requires neither InvenTree nor an AI model or external API.

Created and led by Kamden Higgs through Higgs AI, with AI assisted development and separate nonblind review. The Higgs code is MIT licensed; retained third party material has the qualifications described in the release.
