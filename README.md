# Mr. Jealousy 3.2 — Interior Blind Visualization Tool

AI-powered interior design tool that uses Claude vision and Gemini image generation to visualize venetian blinds in real room photos.

## Features

- **Claude Vision Analysis**: 8-phase analysis pipeline
  - Quality & compliance check
  - Interior style analysis
  - Color palette extraction
  - Window architecture forensics
  - Mounting strategy calculation
  - Lighting conditions analysis
  - Catalog product matching

- **Gemini Image Generation**: Photorealistic blind visualization
  - Physics-based rendering
  - Material realism (wood/aluminum)
  - Lighting integration
  - Perspective accuracy

- **Modern UI**: Pink/rose design system
  - Landing page (upload)
  - Loading state (analysis progress)
  - Results page (before/after slider + configuration)
  - Color selection flyout
  - Responsive design

## Project Structure

```
MRJ3.2/
├── app.py                 # Flask backend
├── core.py               # Configuration & catalogs
├── requirements.txt      # Python dependencies
├── start.bat             # Windows startup script
│
├── src/AI/               # AI Pipeline
│   ├── analyse_claude.py # Vision analysis phases 2-8
│   ├── utils.py          # Helpers (Supabase, base64, etc)
│   └── __init__.py
│
├── static/               # Frontend
│   ├── index.html        # Page structure
│   ├── script.js         # Application logic
│   ├── style.css         # Design system
│   └── fonts/            # Custom typefaces
│
├── media/                # Assets
│   ├── Catalogus/        # Product images (70+ colors)
│   ├── img/              # Design mockups
│   └── ui/               # Components & icons
│
├── data/
│   ├── catalogus.json    # Product catalog
│   └── uploads/          # User uploads
│
└── .env.example          # Environment template
```

## Setup

### 1. Environment Variables

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` with your API keys:
```
ANTHROPIC_API_KEY=sk-ant-api03-...
GEMINI_API_KEY=AIzaSy...
GEMINI_MODEL=gemini-flash-3.5
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Server

**Windows:**
```bash
start.bat
```

**Manual:**
```bash
python app.py
```

Server runs on `http://localhost:5000`

## API Endpoints

### POST `/analyze`
Analyzes uploaded room image (phases 2-8).

**Request:**
```json
{
  "image": "data:image/jpeg;base64,..."
}
```

**Response:**
```json
{
  "style": "Modern Minimalist",
  "colour_palette": [...],
  "windowCheck": {...},
  "suggestions": [...]
}
```

### POST `/render`
Generates photorealistic blind visualization (phase 9).

**Request:**
```json
{
  "image": "data:image/jpeg;base64,...",
  "config": {
    "productType": "Houten Jaloezieën",
    "material": "Hout",
    "colorName": "BBQ Black",
    "colorHex": "#111111"
  },
  "mounting": "in de dag",
  "state": "Tot de helft",
  "extraOptions": {...}
}
```

**Response:**
```json
{
  "image": "data:image/jpeg;base64,..."
}
```

## Color Catalog

### Aluminum Blinds (Aluminium Jaloezieën)
40+ colors: Cherry Pop, Cosmic Blauw, Glitter Gold, Koel Blue, etc.

### Wooden Blinds (Houten Jaloezieën)
30+ colors: BBQ Black, Bonsai Bamboo, De Naturist, Flat White, etc.

Each color includes:
- Hex code
- Sample thumbnails (TOP, BOTTOM, MAIN, SIDE, LAMEL-CLOSE, TOP-BAK)
- Material specification

## Design System

**Colors:**
- Background: `#F5CEC9` (rose)
- Card: `#FFFFFF` (white)
- Text Dark: `#111111`
- Accent: `#CC0022` (red)

**Fonts:**
- Headings: MrGintoNord (900, 800, 700 weights)
- Body: Poppins (400, 500, 700 weights)

**Spacing:**
- Card radius: 16px
- Button radius: 999px (pill)
- Shadows: 2px/8px offset, 8-16% opacity

## Development

### Adding New Colors

Edit `script.js` MR_JEALOUSY_CATALOG and `core.py`:
```python
{
  name: 'New Color',
  hex: '#XXXXXX',
  material: 'Aluminium',
  sampleUrl: '/media/Catalogus/...'
}
```

### Modifying Analysis Pipeline

Edit `src/AI/analyse_claude.py`:
- Phases 2-5: Vision analysis (Claude)
- Phase 6: Mounting strategy (logic)
- Phase 7-8: Lighting & catalog match (Claude)

### Updating UI

- **Pages**: `static/index.html`
- **Logic**: `static/script.js`
- **Styles**: `static/style.css`

## Troubleshooting

### 500 Error on /analyze
- Check `ANTHROPIC_API_KEY` in `.env`
- Ensure Flask is restarted after .env changes
- Check server logs for detailed error

### No color suggestions returned
- Verify `core.py` PRODUCT_MAP is populated
- Check Claude response parsing in `analyse_claude.py`

### Gemini image not generating
- Verify `GEMINI_API_KEY` is valid
- Check that `response_modalities=["IMAGE"]` is set
- Review Gemini API rate limits

## License

Proprietary — Mr. Jealousy Interior Intelligence System

## Contact

For questions or issues: https://github.com/DAVEVERA/MRJ-3.2
