# Hinglish & Regional Language Understanding Benchmark

**Goal:** Measure how well modern LLMs understand **Hinglish** (Hindi + English mix) and other Indian regional languages in real-world usage.

This benchmark tests:
- Code-switching comprehension
- Roman Hindi / Hinglish understanding
- Contextual meaning & intent
- Sentiment & emotion in mixed language
- Reasoning and instruction following in Hinglish
- Regional slang & idioms (basic support)

---

## Structure

```
hinglish-regional-benchmark/
├── README.md
├── tasks/
│   └── hinglish_understanding.py   # Main Kaggle Benchmark task
├── data/
│   └── sample_prompts.json         # Example test cases
└── examples/
    └── run_local.md                # How to test locally
```

---

## How to Use

### 1. Local Development

```bash
# Install Kaggle CLI + auth
pip install kaggle
kaggle b init -y

# Test the task
python tasks/hinglish_understanding.py
```

### 2. Push to Kaggle Benchmarks

```bash
kaggle b t push hinglish-understanding -f tasks/hinglish_understanding.py --wait
```

### 3. Create a Benchmark on Kaggle

1. Go to [https://www.kaggle.com/benchmarks](https://www.kaggle.com/benchmarks)
2. Create a new Benchmark
3. Add the task `hinglish-understanding`
4. Run on multiple models (Gemini, Claude, GPT, Qwen, DeepSeek etc.)

---

## Current Task Focus

**Task Name:** `hinglish_understanding`

It evaluates the model on 5 categories:
1. **Simple Understanding** – Basic meaning of Hinglish sentence
2. **Intent Detection** – What does the user want?
3. **Sentiment** – Positive / Negative / Neutral / Mixed
4. **Code-switch Reasoning** – Multi-step reasoning in Hinglish
5. **Instruction Following** – Follow mixed language instructions accurately

---

## Future Expansion Ideas

- Add pure Hindi (Devanagari)
- Add Bengali, Tamil, Telugu, Marathi, Gujarati samples
- Add transliteration robustness (different spellings of same word)
- Add long-context Hinglish conversations
- Add cultural context & idioms

---

## License

Apache 2.0 (same as Kaggle Benchmarks SDK)

## Author

Created for community contribution to Kaggle Benchmarks.
