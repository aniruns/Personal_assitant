---
title: AI Fluency glossary (study sheet)
type: synthesis
tags: [ai-tools, ai-literacy, glossary, study]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]]", "[[2026-10-06-claude-101-notes]]", "[[2026-10-06-claude-code-101-notes]]"]
related: ["[[ai-fluency]]", "[[human-ai-interaction-modes]]", "[[prompting-fundamentals]]", "[[hallucination]]", "[[retrieval-augmented-generation]]", "[[context-management]]", "[[ai-fluency-vocabulary-cheat-sheet]]"]
confidence: high
status: seed
question: "I want to be trained on the AI Fluency terms later — what are they, and how do I test myself?"
---

# AI Fluency glossary (study sheet)

Every term from Anthropic's AI Fluency cheat sheet, grouped as in the original and linked to
the wiki pages where the idea is used. Definitions follow the sheet's wording, lightly
condensed ([[ai-fluency-vocabulary-cheat-sheet]]). The **"In practice"** notes link the terms
to the other courses the user has taken. Use the sections at the end to test yourself.

## 1. The framework

| Term | Definition |
|---|---|
| **AI Fluency** | The ability to work with AI systems in ways that are effective, efficient, ethical and safe: practical skills, knowledge, insights and values that help you adapt as AI evolves. |
| **The 4Ds** | The four core competencies: Delegation, Description, Discernment, Diligence. See [[ai-fluency]]. |

### The 4Ds × 3 sub-competencies

| D | Definition | Sub-competencies |
|---|---|---|
| **Delegation** | Deciding what work humans do, what AI does, and how to split tasks between them. | **Problem Awareness**: understand your goals and the nature of the work *before* involving AI · **Platform Awareness**: know the capabilities and limits of different AI systems · **Task Delegation**: distribute work to use the strengths of each |
| **Description** | Communicating effectively with AI: defining outputs, guiding processes, specifying behaviours. | **Product Description**: *what* you want (output, format, audience, style) · **Process Description**: *how* the AI should approach it (e.g. step-by-step instructions) · **Performance Description**: how the AI should *behave* during the collaboration (concise or detailed, challenging or supportive) |
| **Discernment** | Critically evaluating AI outputs, processes, behaviours and interactions. | **Product Discernment**: quality of what it produced (accuracy, appropriateness, coherence, relevance) · **Process Discernment**: *how* it got there (logical errors, lapses in attention, bad reasoning steps) · **Performance Discernment**: whether its communication style works for you |
| **Diligence** | Using AI responsibly and ethically: thoughtful choices, transparency, accountability. | **Creation Diligence**: be thoughtful about which systems you use and how · **Transparency Diligence**: be honest about AI's role with everyone who needs to know · **Deployment Diligence**: take responsibility for verifying and vouching for outputs you use or share |

**Memory hook:** Description and Discernment share the same three lenses, **Product /
Process / Performance**. You *describe* along them going in and *discern* along them coming
out.

## 2. Human–AI interaction modes

| Mode | Definition | In practice (assessment) |
|---|---|---|
| **Automation** | AI performs specific tasks from specific human instructions. The human defines *what*, the AI executes. | A one-shot "reformat this table" |
| **Augmentation** | Human and AI collaborate as thinking partners, iterating back and forth. Both contribute. | Turn-by-turn Chat |
| **Agency** | The human configures AI to work independently on their behalf, including with other humans or AIs. The human sets knowledge and behaviour patterns, not exact actions. | [[claude-cowork]], [[claude-code]], [[subagents]], a configured [[claude-md]] |

More: [[human-ai-interaction-modes]].

## 3. AI technical concepts

| Term | Definition | In practice |
|---|---|---|
| **Generative AI** | AI that *creates* new content (text, images, code) rather than only analysing existing data. | |
| **Large language model (LLM)** | Generative AI trained on vast amounts of text to understand and generate human language. | |
| **Claude** | Anthropic's family of LLMs. | [[claude]] |
| **Parameters** | The numerical values inside a model that determine how it processes information and relates pieces of language. Modern LLMs have billions. | |
| **Neural networks** | Computing systems similar to, but distinct from, biological brains: layers of interconnected nodes that learn patterns from data. | |
| **Transformer architecture** | The 2017 breakthrough design that lets LLMs process text sequences **in parallel** while paying **attention** to relationships between words across long passages. | |
| **Scaling laws** | The empirical observation that performance improves in consistent patterns as models grow, with more data and compute. New capabilities can **emerge** at scale thresholds without being explicitly programmed. | |
| **Pre-training** | The first training phase: learning patterns from vast text, building foundational language and knowledge. | |
| **Fine-tuning** | Further training after pre-training to follow instructions, be helpful and avoid harmful content. | Constitutional AI is Anthropic's approach here ([[claude]]); this link is an assessment |
| **Context window** | How much information the AI can consider at once (conversation history plus shared documents). It has a maximum that varies by model. | 200K+ / 1M tokens; "working memory" ([[context-management]]) |
| **Hallucination** | An error where AI **confidently** states something plausible but incorrect. | [[hallucination]] |
| **Knowledge cutoff date** | The point after which a model has no built-in knowledge of the world, set by when it was trained. | Use web search for anything recent |
| **Reasoning / thinking models** | Models designed to think step by step through complex problems; better at logical reasoning. | Claude's "Thinking" ([[choosing-a-claude-surface]]) |
| **Temperature** | A setting that controls randomness. Higher means more varied and creative ("boiling water"); lower means more predictable and focused ("ice crystals"). | |
| **Retrieval-augmented generation (RAG)** | Connecting models to external knowledge sources to improve accuracy and reduce hallucinations. | [[retrieval-augmented-generation]]; Projects switch to it automatically |
| **Bias** | Systematic patterns in outputs that unfairly favour or disadvantage groups or perspectives, often reflecting the training data. | |

## 4. Prompt-engineering concepts

| Term | Definition | In practice |
|---|---|---|
| **Prompt** | The input given to a model, including instructions and any shared documents. | |
| **Prompt engineering** | Designing effective prompts: clear communication plus AI-specific techniques. | [[prompting-fundamentals]] |
| **Chain-of-thought prompting** | Encouraging step-by-step work, breaking complex tasks into smaller steps the AI can follow. | |
| **Few-shot learning (n-shot prompting)** | Teaching by showing examples of the input→output pattern. *N* = the number of examples. | Claude 101: "**show** an example, don't only describe it" |
| **Role / persona definition** | Specifying a character, expertise level or style to adopt, from "speak as a UX expert" to "explain like Feynman". | "Set the stage" |
| **Output constraints / formatting** | Specifying format, length, structure and other features of the response. | "Specify rules"; a form of Product Description |
| **Think-first approach** | Explicitly asking the AI to reason through the problem *before* giving a final answer. | |

## Easily confused pairs

- **Automation vs Augmentation vs Agency:** who decides the steps? Automation: the human
  specifies the task. Augmentation: both, iteratively. Agency: the AI, within patterns the
  human configured.
- **Product vs Process vs Performance:** *what* comes out, *how* it got made, *how it behaves*
  while working with you.
- **Description vs Discernment:** the same three lenses; Description is input, Discernment is
  evaluation.
- **Creation vs Deployment Diligence:** choosing and using the tool responsibly vs. vouching
  for the output you ship.
- **Chain-of-thought vs Think-first:** both ask for step-by-step reasoning. CoT breaks the
  *task* into steps; think-first asks for reasoning *before the final answer*. Assessment: in
  practice they overlap heavily.
- **Chain-of-thought prompting vs reasoning models:** a prompting technique vs. a model built
  to reason step by step.
- **Pre-training vs Fine-tuning:** broad knowledge from raw text vs. learning to be helpful,
  follow instructions and stay safe.
- **Context window vs Knowledge cutoff:** what it can see *right now* vs. what it learned
  *in training*.
- **RAG vs a bigger context window:** fetch the relevant bits vs. fit everything in.

## Self-test

Answers are folded. In Obsidian, click a question to reveal its answer.

> [!question]- What four adjectives define AI Fluency?
> Effective, efficient, ethical, safe.

> [!question]- Name the three sub-competencies of Delegation.
> Problem Awareness, Platform Awareness, Task Delegation.

> [!question]- Which two Ds share the Product / Process / Performance split?
> Description and Discernment.

> [!question]- You spot that Claude skipped a step in its reasoning, even though the final answer looks fine. Which sub-competency is that?
> Process Discernment.

> [!question]- You tell Claude "push back on my ideas, be blunt". Which sub-competency?
> Performance Description.

> [!question]- You tell your manager the report draft was AI-assisted. Which sub-competency?
> Transparency Diligence.

> [!question]- You check every figure before sending an AI-drafted status report. Which sub-competency?
> Deployment Diligence (verifying and vouching for output you share).

> [!question]- Which interaction mode: you set up Cowork to compile a weekly report every Monday on its own?
> Agency: you configured behaviour, not exact actions.

> [!question]- What does the N in n-shot prompting count?
> The number of examples of the input→output pattern you provide.

> [!question]- High temperature or low for a legal summary? Why?
> Low. You want predictable, focused output ("ice crystals").

> [!question]- What year was the transformer introduced, and what two properties matter?
> 2017. It processes text in parallel and uses attention across long passages.

> [!question]- Is the scaling law a theory or an observation? What's surprising about it?
> An empirical observation. New capabilities can *emerge* at scale thresholds without being programmed.

> [!question]- Name two techniques from the sheet that reduce hallucinations or catch them.
> RAG (grounding in external sources) and Product Discernment (verifying accuracy). Assessment: asking for sources helps too ([[prompting-fundamentals]]).

> [!question]- Context window vs knowledge cutoff: which one explains why Claude doesn't know last week's news?
> Knowledge cutoff.

## Contradictions & open questions

- The sheet doesn't say how the 4Ds relate to the three interaction modes, e.g. whether
  Delegation matters more under Agency. The full AI Fluency course might.
- Later: turn this into spaced-repetition flashcards (e.g. an Obsidian spaced-repetition
  deck) or a quiz session on request.

## Draws on

- [[ai-fluency-vocabulary-cheat-sheet]] (all definitions), [[claude-101-course-notes]] and
  [[claude-code-101-course-notes]] ("In practice" notes), [[ai-fluency]],
  [[prompting-fundamentals]]
