# Practical AI Security: Course Labs

Hands-on notebooks for the Practical AI Security course by LogicStack.
Every lesson is a notebook you run in Google Colab. No installs, no API
key, all data fake.

## Lessons

| # | Lesson | Open in Colab |
|---|--------|---------------|
| 1 | Why agents fail differently | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MuhammadSaud60/ai-security-course-labs/blob/main/notebooks/01-why-agents-fail-differently.ipynb) |
| 2 | Build your sandbox | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MuhammadSaud60/ai-security-course-labs/blob/main/notebooks/02-build-your-sandbox.ipynb) |

More lessons land here as the course is built. The full course opens on
logicstack.org all at once when complete.

## How to run

1. Click the Open in Colab badge for the lesson.
2. In Colab: Runtime > Run all. Work top to bottom.
3. Do the steps. Change the code where the lesson asks. Compare your
   output with the expected output in the lesson.

## Run locally (optional)

```bash
python3 labs/01-trust-map/demo_agent.py
```

Python 3.10+, standard library only. No installs.

## Repo layout

- `notebooks/`: one `.ipynb` file per lesson, built for Colab.
- `labs/`: the plain Python version of each lesson lab, with the exact
  outputs captured from verified runs.

## About

Built by LogicStack: https://logicstack.org
