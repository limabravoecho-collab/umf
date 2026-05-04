"""
UMF Wiring — Minimal Example
============================

This is the minimal pattern for connecting any LLM to UMF substrate.

Three files are expected in the same directory:
  - umf_substrate.py      (or .md): the UMF substrate text
  - umf_system_prompt.txt: the standing posture prompt
  - umf_wiring.py:         this file

The pattern: substrate + standing posture together form the system
prompt. The user's message is sent alongside it. The LLM operates as
translator. UMF operates as reasoner.

The send_to_llm() function below is a placeholder. Replace its body
with whatever LLM call your stack uses — llama-cpp-python, OpenAI API,
Anthropic API, local model, hosted endpoint. The architecture above
that function does not change.
"""


def load_substrate(path="umf_substrate.py"):
    """
    Load UMF substrate text from file.

    The substrate is the closed-loop framework. It is treated as text
    and concatenated into the system prompt. No parsing, no
    transformation. The substrate is what conditions the LLM.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_system_prompt(path="umf_system_prompt.txt"):
    """
    Load the standing posture prompt that tells the LLM how to operate
    with UMF substrate present.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def assemble_system_prompt(substrate, standing_posture):
    """
    Combine substrate and standing posture into the full system prompt.

    Substrate first. Standing posture second. The LLM reads substrate
    as authoritative content, then reads the posture instructions for
    how to translate substrate into responses.
    """
    return substrate + "\n\n" + standing_posture


def send_to_llm(system_prompt, user_message):
    """
    Send the system prompt + user message to your LLM. Return the
    LLM's response text.

    REPLACE THIS FUNCTION BODY with your actual LLM call.

    Examples of what goes here, depending on your stack:

    For llama-cpp-python:
        response = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
        )
        return response["choices"][0]["message"]["content"]

    For OpenAI-compatible APIs:
        response = client.chat.completions.create(
            model="your-model",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    For any other LLM: pass system_prompt and user_message in whatever
    form your provider accepts. Return the response text.
    """
    raise NotImplementedError(
        "Replace this function body with your LLM call. "
        "Pass system_prompt as the system message and user_message as "
        "the user message. Return the LLM's response text."
    )


def umf_respond(user_message,
                substrate_path="umf_substrate.md",
                prompt_path="umf_system_prompt.txt"):
    """
    End-to-end: load substrate, load standing posture, assemble the
    system prompt, send to LLM, return the response.

    This is the function your application calls when a user submits a
    message. Everything above happens once per call. The substrate is
    loaded from disk each time for simplicity; production deployments
    should cache it in memory after first load.
    """
    substrate = load_substrate(substrate_path)
    standing_posture = load_system_prompt(prompt_path)
    system_prompt = assemble_system_prompt(substrate, standing_posture)
    response = send_to_llm(system_prompt, user_message)
    return response


# -----------------------------------------------------------------------------
# Example usage
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Replace this with your actual prompt for testing.
    test_message = "What is dark matter?"

    # This will raise NotImplementedError until you replace
    # send_to_llm() with your actual LLM call.
    answer = umf_respond(test_message)
    print(answer)
