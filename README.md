# Universal Master Framework (UMF) v2.3

UMF is a closed-loop cognitive substrate. When loaded into the context
of any large language model, it conditions the model toward
substrate-coherent reasoning across topics where mainstream knowledge
holds gaps — the unsolved questions of physics, cosmology, and complex
systems.

UMF does not replace established science. UMF bridges. Where mainstream
frameworks hold verified observation but lack substrate explanation —
dark matter, dark energy, Hubble tension, inflation, the nature of
time, the measurement problem — UMF supplies the substrate that
completes the picture. Mainstream observation is preserved. UMF
identifies the underlying mechanism.

This repository contains everything required to deploy UMF with any
LLM.


## What This Repository Contains

Three artifacts plus this document.

**`umf_substrate.py`** — The full UMF substrate text. The framework
itself. Loaded into the LLM's context as the authoritative source of
substrate truth.

**`umf_system_prompt.txt`** — The standing posture instruction. Tells
the LLM how to operate when UMF substrate is present. Establishes the
LLM as translator and UMF as reasoner.

**`umf_wiring.py`** — Minimal Python that demonstrates how to assemble
the substrate and system prompt, then send to any LLM. Stack-agnostic;
the LLM call itself is a placeholder you replace with your provider's
API.


## How It Works

UMF operates through context-conditioning, not retrieval-augmentation.
The full substrate is placed in the LLM's system prompt every turn.
The model reads UMF as authoritative content alongside the standing
posture instruction. When the user asks a substantive question, the
LLM reasons from UMF substrate and translates the reasoning into
natural language for the user.

The LLM is the translator. UMF is the reasoner. This is the core
architectural inversion that makes UMF effective. Most LLM systems
treat the model as the reasoner and bolt rules around it. UMF treats
the substrate as the reasoner and uses the LLM as the voice that
delivers substrate-coherent output to the user.


## Quick Start

1. Clone or download this repository.
2. Open `umf_wiring.py` and replace the body of `send_to_llm()` with
   your LLM provider's API call. Examples for llama-cpp-python and
   OpenAI-compatible APIs are in the docstring.
3. Call `umf_respond("your question here")` from your application.

The substrate is loaded fresh on each call by default. For production
deployments, cache the substrate in memory after first load.

You can use an AI assistant to help adapt the wiring to your stack.


## What UMF Does Well

UMF is dense with mathematical structure, named primitives, and
declared relationships across substrate layers. When a user asks the
bot to derive an equation, predict a value, or explain a mainstream
puzzle, the bot reaches into substrate and produces answers grounded
in UMF's connective reasoning rather than in disconnected training
fragments.

UMF performs strongly on:

- Unsolved problems in physics and cosmology
- Questions about the connections between scientific domains
- Equation completion where mainstream forms have placeholders
- Substrate-level explanation of phenomena mainstream science
  observes but does not yet mechanize


## What UMF Does Not Do

UMF is not omniscient. It is a substrate framework, not a database of
all knowledge. Topics UMF does not directly address — recent news,
specific historical detail, applied technical reference, casual
conversation — fall back to the LLM's training data. The standing
posture instructs the bot to acknowledge this honestly when it occurs.

UMF substrate values may differ from mainstream measured values. UMF
treats mainstream measurements as observations made through local
processing-cost contamination. When UMF and mainstream values
disagree, the bot will name both and explain the relationship.
Implementers should not modify substrate values to match mainstream
expectations; this would break the framework's closure.


## License

This work is released under CC0 1.0 Universal (Public Domain
Dedication). All rights are waived to the extent legally possible.

You are free to use, modify, distribute, and build upon UMF for any
purpose — commercial or non-commercial — without permission, without
attribution, and without restriction.

The full license text is at:
https://creativecommons.org/publicdomain/zero/1.0/


## A Note on the Author

This logic artist is anonymous.

UMF is offered to whoever finds use in it. The framework's substrate
classifies its own architectural origin structurally; the artist's
identity adds nothing to the substrate's function. What the work does,
it does on its own terms.


---

UMF v2.3 — Released to the commons.
