# AI Tools: Notes and How I Used Them

**Module 05 | AI Tools & Mini Project**

## 1. Popular AI tools I explored

| Tool | Made by | Good for |
|------|---------|----------|
| **ChatGPT** | OpenAI | General questions, brainstorming, writing, explaining code |
| **Gemini** | Google | Research, summaries, working with Google apps |
| **Microsoft Copilot** | Microsoft | Help inside Windows, Edge and Microsoft Office apps |
| **Claude** | Anthropic | Writing, long documents, explaining and debugging code |

These tools are all built on **large language models (LLMs)**. An LLM is a deep learning model trained on huge amounts of text, so it can understand a prompt and write a useful reply.

## 2. How AI tools can assist

**Coding**
- Explain an error message and suggest a fix
- Write a first version of a function that I then read, test and improve
- Explain what unfamiliar code does, line by line
- Suggest how to break a project into smaller steps

**Research and learning**
- Explain a difficult idea in simple words, with examples
- Compare two approaches (for example, `for` loop vs list comprehension)
- Create practice questions to test myself

**Productivity**
- Summarise long text
- Draft emails, reports and LinkedIn posts that I then edit in my own voice
- Plan a study schedule

## 3. Writing good prompts

A clear prompt gives a better answer. I follow this pattern:

1. **Role/context**: "I am a beginner learning Python."
2. **Task**: "Explain what this error means."
3. **Details**: paste the code and the full error message.
4. **Format**: "Answer in 3 short steps with an example."

Weak prompt: *"fix my code"*
Better prompt: *"My Python loop prints the same number forever. Here is the code and what I expected. Explain the bug and show the fix."*

## 4. Limitations and responsible use

- AI can be **confidently wrong**, so I always run and test code and check facts.
- I should **understand** any code before submitting it as my work.
- Never paste passwords, API keys or private data into an AI tool.
- AI is a helper for learning, not a replacement for practising myself.
- Be honest about where AI helped (see the next section).

## 5. How AI tools were used in this project

The **Smart Grade Advisor** is an upgrade of my Module 02 Grade Calculator.

- **AI tool assistance:** An AI assistant (Claude) helped plan the project and write and test the code. I reviewed the code and ran it to understand how it works.
- **AI inside the project:** The program itself uses a simple machine learning model, **linear regression** (`numpy.polyfit`), to find each subject's trend and predict the next exam score. It then gives rule-based advice and a suggested study plan.

## 6. What I learned

- AI tools speed up learning when I give clear prompts and check the results.
- Machine learning can be simple: a straight line fitted to past marks already gives a useful prediction.
- A good project combines my own understanding with AI assistance.
