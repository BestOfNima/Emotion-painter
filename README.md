# 🎙️ Emotion Painter

#Emotion #Paint #Art #AI #Gemma3-4b #Wisper-medium-int8 #Streamlit 

#Ollama #pollinations #Python

Turn spoken or written words into an emotion-driven AI image prompt — record or type text, detect the emotional "DNA" of it, and get a cinematic image prompt (plus visual breakdowns) ready to feed into an image generator.

## How it works

1. **Input** — record audio with the browser mic, or type text directly.
2. **Speech-to-Text** — if audio was recorded, it's transcribed locally with Whisper.
3. **Emotion Detection + Prompt Building** — the transcript/text is sent to a local LLM (via Ollama) which analyzes the emotional content and returns a structured JSON: dominant emotion, an "Emotion DNA" breakdown (Happyness / Sadness / Anger / Fear / Calm as percentages), a matching color palette + art style, and a ready-to-use image generation prompt.
4. **Visualization** — the results are rendered as progress bars, a radar chart, and a donut chart, plus a color swatch palette.
5. **Image Generation** — the generated prompt can be turned into an image (currently via the Pollinations.ai API; the architecture also anticipates a local Stable Diffusion pipeline), and the result can be uploaded/displayed in the app.

## Tech stack & libraries

| Purpose | Technology |
|---|---|
| Web UI | [Streamlit](https://streamlit.io/) |
| Speech-to-Text | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) (Whisper `medium` model, CPU, int8 quantization) |
| Emotion detection & prompt generation | [Ollama](https://ollama.com/) running a local LLM (default: `gemma3:4b`) |
| Image generation | [Pollinations.ai](https://pollinations.ai/) API via `requests` (architecture diagram also references a local Stable Diffusion option) |
| Charts | [Plotly](https://plotly.com/python/) (`plotly.graph_objects`) — radar chart, donut chart, progress bars |
| HTTP requests | `requests` |
| Misc | Python standard library (`json`, `os`, `re`, `uuid`, `datetime`) |

### Python dependencies to install

```bash
pip install -r requirements.txt
```

> Ollama itself must also be installed and running separately (see [ollama.com](https://ollama.com/)), with the desired model pulled, e.g.:
> ```bash
> ollama pull gemma3:4b
> ```

## Project structure

```
.
├── app.py                  # Main Streamlit app / page flow
├── python/
│   ├── app_STT.py           # Speech-to-text (faster-whisper)
│   ├── app_ollama.py        # Emotion analysis + prompt generation (Ollama LLM call + system prompt)
│   ├── app_image.py         # Image generation via Pollinations.ai
│   ├── parser.py            # Robust parsing/normalization of the LLM's JSON output
│   ├── ui.py                 # Streamlit render functions (prompt, summary, emotions, debug, download)
│   ├── palette.py            # Emotion badge + color palette rendering
│   ├── charts.py             # Plotly charts (progress bars, radar, donut)
│   ├── constants.py          # Shared constants (emotions, emojis, colors, defaults)
│   └── styles.py             # Custom CSS injection (light/dark theme support)
├── obsidian/
│   └── Emotion painter.canvas   # Architecture/whiteboard diagram (Obsidian Canvas)
└── audio/                    # Recorded audio files are saved here at runtime
```

## Emotion → Color → Style mapping

The LLM is grounded with this mapping so results stay consistent:

| Emotion | Colors | Style |
|---|---|---|
| Happyness | Yellow, Orange | Impressionism |
| Sadness | Dark Blue | Watercolor |
| Anger | Red, Black | Expressionism |
| Fear | Dark Purple | Surreal |
| Calm | Green, Turquoise | Minimalist |

## Running the app

```bash
streamlit run app.py
```

Make sure Ollama is running locally (`ollama serve`) with the target model pulled before clicking "Analyze Emotion & Generate Prompt".

## Notes

- The LLM's raw output isn't always clean JSON — `python/parser.py` strips markdown code fences, extracts the outer `{...}` block, and coerces/normalizes fields (emotion keys lowercased, colors normalized to a list, missing fields filled from safe defaults) so the UI never crashes on a malformed response.
- Recorded audio is saved under `audio/` with a timestamp + short UUID filename, and past recordings are listed/playable in the app.
- The `obsidian/Emotion painter.canvas` file is a visual architecture sketch (in Farsi/Persian) mapping out the original MVP plan — useful as a reference but not required to run the app.
