# Local Testing Guide

## Prerequisites

```bash
# 1. Install Kaggle package
pip install kaggle

# 2. Setup credentials (one time)
kaggle b init -y
```

## Run the task locally

```bash
cd tasks
python hinglish_understanding.py
```

You will see category-wise scores and overall score.

## Push to Kaggle

```bash
# From project root
kaggle b t push hinglish-understanding -f tasks/hinglish_understanding.py --wait
```

After push is successful:
1. Go to https://www.kaggle.com/benchmarks
2. Create a new **Benchmark**
3. Add task → `hinglish-understanding`
4. Select models and Run

## Tips for Improvement

- Add more diverse Hinglish samples (different cities/slang)
- Include pure Devanagari Hindi
- Add regional languages (Bengali, Tamil etc.) later
- Use LLM-as-Judge for more subjective questions instead of keyword matching
