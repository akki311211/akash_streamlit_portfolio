# Rohit Jindal — Personal Website

A modular Streamlit personal website. One-page, three tabs (Industry · Education · Teaching),
hero with stats, skills section, and a reserved slot for a future live-chat / AI-clone feature.

---

## Run locally

```bash
# 1. (recommended) create a fresh venv
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 2. install deps
pip install -r requirements.txt

# 3. run
streamlit run app.py
```

Streamlit will open the site at **http://localhost:8501**. The app auto-reloads on save.

On first launch the app generates placeholder images for every photo slot. **You don't have to do anything to see the site working** — replace placeholders later as you have real photos.

---

## Project layout

```
personal_website/
├── app.py                  # entry point — orchestrates sections, ~70 lines
├── styles.css              # all custom styling (color tokens at top)
├── requirements.txt
├── .streamlit/config.toml  # Streamlit theme
│
├── data/                   # ← EDIT THESE TO UPDATE CONTENT
│   ├── profile.py            #  hero info, summary, stats
│   ├── industry.py           #  Target, Symphony/CPS, Railways, …
│   ├── education.py          #  IISc, DTU, Cambridge, DPS
│   ├── teaching.py           #  Scaler, NexaML, REVA, …
│   └── skills.py             #  tech stack categories
│
├── sections/               # rendering logic per section
│   ├── hero.py
│   ├── industry.py
│   ├── education.py
│   ├── teaching.py
│   ├── skills.py
│   └── contact.py
│
├── components/
│   └── card.py             # reusable card used by all three tabs
│
├── utils/
│   └── images.py           # placeholder generator + image loader
│
└── assets/
    └── images/             # ← drop your real photos here
```

---

## How to update content

**Almost everything you'll change is in `data/`.** Each file is a plain Python list/dict — no
framework knowledge required.

### Add a new role at Target (or any company)
Open `data/industry.py`, find the Target dict, and append to its `subprojects` list:

```python
{
    "name": "My New Project — Headline Result",
    "description": "Short paragraph describing what I built and the impact.",
    "tags": ["LangChain", "PySpark"],
},
```

### Add a new company / school / teaching role
Just add a new dict to the corresponding list (`INDUSTRY`, `EDUCATION`, or `TEACHING`).
Order on the page = order in the list.

### Update the hero
Edit `data/profile.py`. Photo path, summary, contact links, and the four stat cards
all live there.

### Update tech stack
Edit `data/skills.py`. Add a category, remove one, or reorder freely.

---

## Replacing photos

All images live in `assets/images/`. Filenames are referenced from the data files:

| Filename                | Used for                        |
| ----------------------- | ------------------------------- |
| `profile.jpg`           | Your photo in the hero          |
| `target.jpg`            | Target role card                |
| `symphony_cps.jpg`      | Chicago Public Schools contract |
| `indian_railways.jpg`   | Indian Railways                 |
| `state_street.jpg`      | State Street Global Advisors    |
| `mastercard.jpg`        | Mastercard AI Garage            |
| `iisc.jpg`              | IISc                            |
| `dtu.jpg`               | DTU                             |
| `cambridge.jpg`         | Cambridge / King's College      |
| `dps.jpg`               | DPS Paschim Vihar               |
| `scaler.jpg`            | Scaler Academy                  |
| `nexaml.jpg`            | NexaML                          |
| `reva.jpg`              | REVA University                 |
| `teaching_misc.jpg`     | Generic talks / workshops       |

To swap any photo: drop a new image into `assets/images/` with the **same filename**.
No code change needed. JPG / PNG both work.

If you want a different filename, update the `logo:` or `photo:` field in the
corresponding `data/*.py` entry.

---

## Restyling

All colors live as CSS variables at the top of `styles.css`:

```css
:root {
  --navy:   #1F3A5F;   /* primary brand color */
  --accent: #2E5C8A;   /* secondary / links */
  ...
}
```

Change those four-five tokens and the entire site rebrands.

---

## Deploying to Streamlit Cloud

1. Push this folder to a public (or private) GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Point it at your repo, branch, and `app.py`
4. Click Deploy

It'll be live at `https://<your-app>.streamlit.app/`.

---

## What's next (planned)

- **Live chat / AI clone** — placeholder card already in `sections/contact.py`. When ready,
  swap the placeholder div for a chat UI calling Anthropic's API.
- **Optional**: case study sub-pages, blog/writing section, talks page.
