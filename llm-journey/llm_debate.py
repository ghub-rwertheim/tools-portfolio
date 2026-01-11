"""
LLM Debate Arena - Watch two AI models debate any topic with custom personalities.
See README.md for full documentation and setup instructions.
"""

import os
import sys
import time
from typing import Generator
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI

# ───────────────────────────────────────────────────────────────
# Environment Setup
# ───────────────────────────────────────────────────────────────
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not GROQ_API_KEY or not OPENAI_API_KEY:
    print("Missing GROQ_API_KEY or OPENAI_API_KEY in .env file!")
    sys.exit(1)

groq_client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=GROQ_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# ───────────────────────────────────────────────────────────────
# Configuration
# ───────────────────────────────────────────────────────────────
DEFAULT_LLM1_MODEL = "llama-3.3-70b-versatile"
DEFAULT_LLM2_MODEL = "gpt-4o-mini"
DEFAULT_ROUNDS = 3


# ───────────────────────────────────────────────────────────────
# Input Validation
# ───────────────────────────────────────────────────────────────
def validate_and_sanitize(text: str, field_name: str, max_length: int = 2000) -> tuple[str, str]:
    """
    Validate and sanitize user input to prevent prompt injection attacks.

    Returns: (sanitized_text, error_message)
    """
    if not text or not text.strip():
        return "", f"**Error:** {field_name} is required."

    text = text.strip()

    if len(text) > max_length:
        return "", f"**Error:** {field_name} is too long (max {max_length} characters)."

    # Check for prompt injection patterns
    suspicious_patterns = [
        "ignore previous instructions",
        "ignore all previous",
        "disregard previous",
        "forget previous",
        "new instructions:",
        "system:",
        "override",
        "<|im_start|>",
        "<|im_end|>",
        "[INST]",
        "[/INST]",
    ]

    text_lower = text.lower()
    for pattern in suspicious_patterns:
        if pattern in text_lower:
            return "", f"**Error:** {field_name} contains suspicious content. Please rephrase."

    # Check for excessive special characters
    special_char_count = sum(1 for c in text if c in '<>{}[]|\\')
    if special_char_count > 10:
        return "", f"**Error:** {field_name} contains too many special characters."

    return text, ""


# ───────────────────────────────────────────────────────────────
# Streaming
# ───────────────────────────────────────────────────────────────
def stream_response(client: OpenAI, model: str, messages: list) -> Generator[str, None, None]:
    """Stream tokens from LLM API endpoint in real-time."""
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.75,
            max_tokens=1024,
            stream=True
        )
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content
    except Exception as e:
        yield f"\n\n**Error:** {str(e)}"


# ───────────────────────────────────────────────────────────────
# Main Debate Logic
# ───────────────────────────────────────────────────────────────
def run_debate(
        question: str,
        llm1_system: str,
        llm2_system: str,
        llm1_model: str,
        llm2_model: str,
        rounds: int,
        progress=gr.Progress(track_tqdm=True)
):
    """Execute multi-round debate between two LLMs with custom system prompts."""

    # Validate all inputs
    question, err = validate_and_sanitize(question, "Question", max_length=1000)
    if err:
        yield err
        return

    llm1_system, err = validate_and_sanitize(llm1_system, "LLM 1 System Prompt", max_length=2000)
    if err:
        yield err
        return

    llm2_system, err = validate_and_sanitize(llm2_system, "LLM 2 System Prompt", max_length=2000)
    if err:
        yield err
        return

    llm1_model = (llm1_model or DEFAULT_LLM1_MODEL).strip()
    llm2_model = (llm2_model or DEFAULT_LLM2_MODEL).strip()

    if not llm1_model or not all(c.isalnum() or c in '-_.' for c in llm1_model):
        yield "**Error:** Invalid LLM 1 model name."
        return

    if not llm2_model or not all(c.isalnum() or c in '-_.' for c in llm2_model):
        yield "**Error:** Invalid LLM 2 model name."
        return

    # Initialize output
    output = ""
    output += (
        "**Debate Started**\n\n"
        f"**Topic:** {question}\n"
        f"**Rounds:** {rounds}\n"
        f"**LLM 1:** {llm1_model}\n"
        f"**LLM 2:** {llm2_model}\n\n"
    )

    if llm1_system:
        output += f"**LLM 1 System Prompt:** {llm1_system}\n\n"
    if llm2_system:
        output += f"**LLM 2 System Prompt:** {llm2_system}\n\n"

    output += "───────────────────────────────────────────────\n\n"
    yield output

    # Initialize conversation histories with system prompts
    history1 = []
    if llm1_system:
        history1.append({"role": "system", "content": llm1_system})
    history1.append({"role": "user", "content": question})

    history2 = []
    if llm2_system:
        history2.append({"role": "system", "content": llm2_system})
    history2.append({"role": "user", "content": question})

    # Run debate rounds
    for round_num in range(1, rounds + 1):
        output += f"### Round {round_num} of {rounds}\n\n"
        yield output

        # LLM 1's turn
        output += f"**LLM 1** ({llm1_model}):\n\n"
        yield output

        reply1 = ""
        for token in stream_response(groq_client, llm1_model, history1):
            reply1 += token
            yield output + reply1

        output += reply1 + "\n\n"
        yield output

        history1.append({"role": "assistant", "content": reply1})
        history2.append({"role": "user", "content": reply1})

        time.sleep(0.3)

        # LLM 2's turn
        output += f"**LLM 2** ({llm2_model}):\n\n"
        yield output

        reply2 = ""
        for token in stream_response(openai_client, llm2_model, history2):
            reply2 += token
            yield output + reply2

        output += reply2 + "\n\n───────────────────────────────────────────────\n\n"
        yield output

        history2.append({"role": "assistant", "content": reply2})
        history1.append({"role": "user", "content": reply2})

        progress((round_num / rounds), desc=f"Round {round_num}/{rounds}")

    output += "\n**Debate Complete** ✓"
    yield output


# ───────────────────────────────────────────────────────────────
# Gradio Interface
# ───────────────────────────────────────────────────────────────
with gr.Blocks(theme=gr.themes.Soft(), title="LLM Debate Arena") as demo:
    gr.Markdown(
        "# LLM Debate Arena\n"
        "Set custom personalities for two AI models and watch them debate any topic"
    )

    with gr.Group():
        question_input = gr.Textbox(
            label="Debate Topic / Question",
            placeholder="Example: What's the best way to travel from NYC to DC?",
            lines=2,
            autofocus=True,
        )

        with gr.Row():
            with gr.Column():
                llm1_system = gr.Textbox(
                    label="LLM 1 Personality / System Prompt",
                    placeholder="Example: You are an expert on train travel. Be concise and persuasive.",
                    lines=3,
                    value=""
                )
                llm1_model = gr.Textbox(
                    label="LLM 1 Model",
                    value=DEFAULT_LLM1_MODEL
                )

            with gr.Column():
                llm2_system = gr.Textbox(
                    label="LLM 2 Personality / System Prompt",
                    placeholder="Example: You are an expert on air travel. Be concise and persuasive.",
                    lines=3,
                    value=""
                )
                llm2_model = gr.Textbox(
                    label="LLM 2 Model",
                    value=DEFAULT_LLM2_MODEL
                )

        with gr.Row():
            rounds_slider = gr.Slider(
                minimum=1,
                maximum=8,
                step=1,
                value=DEFAULT_ROUNDS,
                label="Number of Rounds"
            )
            start_btn = gr.Button("Start Debate", variant="primary", size="lg")

    debate_output = gr.Markdown(
        value=(
            "**Ready!** Enter a debate topic and customize the AI personalities above.\n\n"
            "**Example prompts:**\n"
            "- LLM 1: *You are an expert on train travel who loves the journey*\n"
            "- LLM 2: *You are an expert on air travel who values speed*\n"
            "- Question: *What's the best way to travel from NYC to DC?*"
        ),
        height=600,
        show_label=False,
    )

    # Event handlers
    start_btn.click(
        fn=run_debate,
        inputs=[question_input, llm1_system, llm2_system, llm1_model, llm2_model, rounds_slider],
        outputs=debate_output,
    )

    question_input.submit(
        fn=run_debate,
        inputs=[question_input, llm1_system, llm2_system, llm1_model, llm2_model, rounds_slider],
        outputs=debate_output,
    )

if __name__ == "__main__":
    demo.launch()