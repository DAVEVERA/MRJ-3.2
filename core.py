"""
core.py — The Quiet Engine
MRJ3.0 | Mr. Jealousy Interior Intelligence System

This file is the single source of truth for all phase laws, the product catalog,
descriptor maps, response schemas, and system constants. It defines — it never executes.
Every other module in this project imports from here. Nothing runs inside core.py itself.
"""

from typing import TypedDict, List, Dict, Any, Optional


# ── TYPE DEFINITIONS ───────────────────────────────────────────────────────────

class ProductColor(TypedDict):
    name: str
    hex: str
    material: str
    sampleUrl: str
    galleryUrls: Optional[List[str]]


class ColourPaletteEntry(TypedDict):
    hex_code: str
    extracted_source: str
    matched_catalog_color: str


class WindowCheck(TypedDict):
    obstacles: bool
    windowType: str
    detectedWindowCount: int
    recommendation: str
    reasoning: str
    specialConsiderations: str


class ProductSuggestion(TypedDict):
    productType: str
    material: str
    colorName: str
    colorHex: str
    suitabilityScore: int
    reasoning: str


class AnalysisResult(TypedDict):
    style: str
    styleSummary: str
    styleDescription: str
    roomMood: str
    lightingConditions: str
    colour_palette: List[ColourPaletteEntry]
    windowCheck: WindowCheck
    materialSuggestions: List[str]
    suggestions: List[ProductSuggestion]


class RenderInstruction(TypedDict):
    product_type: str
    color_name: str
    hex_code: str
    mount_type: str
    window_sections: int
    lighting_condition: str
    state: str
    slat_width: Optional[str]
    ladder_tape: bool
    scene_description: str
    negative_prompt: str
    camera_angle: str
    room_context: str


# ── SYSTEM CONSTANTS ───────────────────────────────────────────────────────────

PHASE_COUNT       = 9
ANALYSIS_MODEL    = "claude-opus-4-6"
FALLBACK_MODEL    = "claude-sonnet-4-6"
RENDER_MODEL      = "models/gemini-2.5-flash-image"
UPLOAD_PATH       = "data/uploads"
JSON_CACHE_PATH   = "data/json_convert_to_text.txt"
ANALYSE_JSON_PATH = "data/analyse.json"
SUPABASE_BUCKET   = "uploads"


# ── PRODUCT RULES ──────────────────────────────────────────────────────────────

ALLOWED_PRODUCT_TYPES: List[str] = [
    "Aluminium Jaloezieën",
    "Houten Jaloezieën",
]

ALLOWED_WOODEN_SUBTYPES: List[str] = [
    "Paulownia",
    "Bamboo",
    "Abachi",
]

MOUNT_LABELS: Dict[str, str] = {
    "inside":  "in de dag",
    "outside": "op de dag",
}


# ── MR. JEALOUSY CATALOG ───────────────────────────────────────────────────────

MR_JEALOUSY_CATALOG: Dict[str, List[ProductColor]] = {
    "Aluminium Jaloezieën": [
        {"name": "Like RAL9002",      "hex": "#E9E5CE", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Looks-Like-9002/ALU_0590_Looks-Like-9002_MAT_MRJEALOUSY_TOP_1024x1024_7446caaa-9d15-4069-92d6-3ddf710f0a1d.png"},
        {"name": "Like RAL9010",      "hex": "#F7F9EF", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Looks-Like-9010/ALU_0159_Looks-Like-9010_SILK-GLOSS_MRJEALOUSY_TOP_SWATCH_1024x1024_0007.png"},
        {"name": "Moody Munt",        "hex": "#98FF98", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Moody-Munt/ALU_3790_Moody-Munt_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_fe054c58-b2d6-41b9-8a2f-7e63c97b1fd0.png"},
        {"name": "Naughty Aubergine", "hex": "#472C4C", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Naughty-Aubergine/ALU_8222_Naughty-Aubergine_v2_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_dfb711a6-8dbb-476f-8ef0-4325ca6aebcb.png"},
        {"name": "Oud Green",         "hex": "#8F9779", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Oud-Green/ALU_1229_Oud-Green_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_a069cbc7-0edd-4213-8f5d-12c5e30f30d3.png"},
        {"name": "Peachy Pink",       "hex": "#FFDAB9", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Peachy-Pink/ALU_8238_Peachy-Pink_SUPER-MAT_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_42be3990-4e2b-4c58-9e77-b4ef67b2c0ea.jpg"},
        {"name": "Poolside Blue",     "hex": "#00BFFF", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Poolside-Blue/ALU_8234_Poolside-Blue_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_9d9b6b8c-cdae-4863-8614-262eb018bae2.png"},
        {"name": "Purple Grey",       "hex": "#6D6875", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Purple-Grey/ALU_2095_Purple-Grey_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_3d1758b0-7075-4576-bd79-ac3d49fde2b8.png"},
        {"name": "Rocky Rood",        "hex": "#8B0000", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Rocky-Rood/ALU_5699_Rocky-Rood_MAT_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_301069ec-b4ad-439d-a128-36e58307d44f.jpg"},
        {"name": "Rusty Retro",       "hex": "#B7410E", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Rusty-Retro/ALU_7919_Rusty-Retro_RUST_MRJEALOUSY_TOP_1024x1024_9e8d82c0-35c3-4939-9e2c-9402ec88f281.png"},
        {"name": "Silk Zwart",        "hex": "#050505", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Silk-Zwart/ALU_9020_Silk-Zwart_SPARKLY_MRJEALOUSY_TOP_1024x1024_4db5d3d8-81a1-4ddb-aa32-fd02f440f111.png"},
        {"name": "Skinny Dip",        "hex": "#F4C2C2", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Skinny-Dip/ALU_8266_Skinny-Dip_MAT-SPARKLE_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_01215c2e-f6d9-4ce0-8e7d-46753c58dd56.jpg"},
        {"name": "Smokey Grey",       "hex": "#708090", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Smokey-Grey/ALU_9018_Smokey-Grey_SPARKLE_MRJEALOUSY_TOP_SWATCH_1024x1024-min.png"},
        {"name": "Soft Naakt",        "hex": "#E3BC9A", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Soft-Naakt/ALU_9015_Soft-Naakt_SUPER-MAT-DUO-A_MRJEALOUSY_TOP_SWATCH_1024x1024_0a7b9406-a0b9-4c21-b048-b78abfa34cb5.png"},
        {"name": "Soft Terra",        "hex": "#E2725B", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Soft-Terra/ALU_9019_Soft-Terra_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_351183ef-f366-417f-a1a8-4f8f3455466f.png"},
        {"name": "Stevig Taupe",      "hex": "#483C32", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Stevig-Taupe/ALU_4544_Stevig-Taupe_SILK-GLOSS_MRJEALOUSY_TOP_1024x1024_23f6ce17-f7d1-44ad-9060-6159f30eacff.png"},
        {"name": "Stormy Taupe",      "hex": "#5C5552", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Stormy-Taupe/ALU_8236_Stormy-Taupe_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_43cec98d-7761-4198-b3a5-397dada8c168.png"},
        {"name": "Twijfel Taupe",     "hex": "#876C5E", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Twijfel-Taupe/ALU_9014_Twijfel-Taupe_SUPER-MAT_MRJEALOUSY_01_MAIN_KOORD1500x1500_f0c4b72f-cc58-42a3-8613-b0dc4f4bb0ed.jpg"},
        {"name": "Velvet Brown",      "hex": "#4B3621", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Velvet-Brown/ALU_9017_Velvet-Brown_SPARK_MRJEALOUSY_TOP_1024x1024_28ed1acb-1276-4408-8491-92f664a17086.png"},
        {"name": "Bold Bruin",        "hex": "#654321", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Bold-Bruin/ALU_4798_Bold-Bruin_SUPER-MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_3209ffaa-c291-4894-936e-1d54df7e1024.png"},
        {"name": "Butter Geel",       "hex": "#F3E5AB", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Butter-Geel/ALU_4315_Butter-Geel_MAT_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_94998412-3a05-4417-91e6-869499133260.jpg"},
        {"name": "Cherry Pop",        "hex": "#D2042D", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Cherry-Pop/ALU_8261_Cherry-Pop_VELVET_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_f89ac437-aa33-41fb-a8ac-f6afc3cb4c24.jpg"},
        {"name": "Cool Grey",         "hex": "#A9A9A9", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Cool-Grey/ALU_9011_Cool-Grey_SUPER-MAT-DUO-A_MRJEALOUSY_TOP_1024x1024_d61f2511-63a8-4f26-b8d7-e1d7f86c24d2.png"},
        {"name": "Cosmic Blauw",      "hex": "#000080", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Cosmic-Blauw/ALU_8235_Cosmic-Blauw_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_69979c25-1f00-4fd8-a15a-dc55ccd644fd.png"},
        {"name": "Crazy Karamel",     "hex": "#C68E17", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Crazy-Karamel/ALU_4394_Crazy-Karamel_MAT_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_a95969d2-2c42-472c-b40c-ca98d81772d4.jpg"},
        {"name": "Drop Zwart",        "hex": "#1A1A1A", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Drop-Zwart/ALU_1861_Drop-Zwart_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024-min.png"},
        {"name": "Fluffy Naakt",      "hex": "#F5DEB3", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Fluffy-Naakt/ALU_9021_Fluffy-Naakt_SPARKLY_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500-UPDATE_beb76d64-3a68-4902-b00f-6cc94c2733c0.jpg"},
        {"name": "Brushed Nikkel",    "hex": "#B0C4DE", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Geborsteld-Nikkel/ALU_7325_Geborsteld-Nikkel_BRUSHED_MRJEALOUSY_TOP_SWATCH_1024x1024_0007.png"},
        {"name": "Koffie Koper",      "hex": "#B87333", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Gebrand-Koper/ALU_7380_Gebrand-Koper_BRUSHED_MRJEALOUSY_TOP_SWATCH_1024x1024_00c4f029-31d0-4ff2-8b02-98d4caab6182.png"},
        {"name": "Glitter Gold",      "hex": "#FFD700", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Glitter-Gold/ALU_7529_Glitter-Gold_SUPER-SPARKLY_MRJEALOUSY_TOP_SWATCH_1024x1024_ac71dcb9-965c-46fc-b26c-30ba3935ca6f.png"},
        {"name": "Goed Grijs",        "hex": "#808080", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Goed-Grijs/ALU_1510_Goed-Grijs_SUPER-MAT_MRJEALOUSY_01_MAIN_KOORD1500x1500_b61149c4-07dc-4310-a851-16d25587536f.jpg"},
        {"name": "Jet Black",         "hex": "#050505", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Jet-Black/ALU_8228_Jet-Black_SUPER-MAT_MRJEALOUSY_TOP_1024x1024_3d0b276f-7c04-4038-9bdf-de065e9cfd2c.png"},
        {"name": "Juicy Olive",       "hex": "#808000", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Juicy-Olive/ALU_8268_Juicy-Olive_MAT-SPARKLE_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_015e04c2-5484-4b90-8751-2118242bbb12.jpg"},
        {"name": "Koel Blue",         "hex": "#AEC6CF", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Koel-Blue/ALU_0990_Koel-Blue_MAT_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500_fbea5a24-82ec-4d5b-8b95-13dcb97c723a.jpg"},
        {"name": "Like RAL9001",      "hex": "#FDF4E3", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Looks-Like-9001/ALU_4491_Looks-Like-9001_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_6d667459-0060-451b-811b-0535050e0c76.png"},
        {"name": "Cowboy Koper",      "hex": "#8B4513", "material": "Aluminium", "sampleUrl": "/media/Catalogus/Cowboy-Koper/ALU_7381_Cowboy-Koper_BRUSHED_MRJEALOUSY_01_MAIN_KOORD_50mm_1500x1500-UPDATE_54e947fe-f03e-48e7-baa3-442c19cdcda4.jpg"},
    ],
    "Houten Jaloezieën": [
        {"name": "Like RAL9016",    "hex": "#F0F8FF", "material": "Hout", "sampleUrl": "/media/Catalogus/Looks-Like-9016/ALU_0192_Looks-Like-9016_MAT_MRJEALOUSY_TOP_SWATCH_1024x1024_8b8dd131-8457-4478-ac84-26b0703d93dd.png"},
        {"name": "Mister Sandman",  "hex": "#C2B280", "material": "Hout", "sampleUrl": "/media/Catalogus/SAND/HOUTEN-JALOEZIE_SAND_MRJEALOUSY_TOP_1024x1024_4b523e1b-34c3-4291-8e42-5bf5ebaaaa22.png"},
        {"name": "Misty Bamboo",    "hex": "#DCC098", "material": "Hout", "sampleUrl": "/media/Catalogus/MISTY-BAMBOO/BAMBOE-JALOEZIE_MISTY-BAMBOO_MRJEALOUSY_01_MAIN_KOORD_1500x1500_e3578a74-154c-46e6-ad81-d433bc92ce21.jpg"},
        {"name": "Oak Mooi",        "hex": "#C3A376", "material": "Hout", "sampleUrl": "/media/Catalogus/OAKMOOI/HOUTEN-JALOEZIE_OAKMOOI_MRJEALOUSY_KOORD_MAIN_1500x1500_5a1c1a8f-0e00-4144-85f0-994fad991b55.jpg"},
        {"name": "Parel White",     "hex": "#F5F5F5", "material": "Hout", "sampleUrl": "/media/Catalogus/WHITE/HOUTEN-JALOEZIE_WHITE_MRJEALOUSY_KOORD_MAIN_1500x1500_2d53cdc9-263f-4546-9a33-c66dcc9728e4.jpg"},
        {"name": "Shades of Grey",  "hex": "#808080", "material": "Hout", "sampleUrl": "/media/Catalogus/GREY/HOUTEN-JALOEZIE_GREY_MRJEALOUSY_TOP_1024x1024_41c102dd-1ad8-4eb8-a3a2-f185d6e5bd62.png"},
        {"name": "Smokey Taupe",    "hex": "#9E958C", "material": "Hout", "sampleUrl": "/media/Catalogus/SMOKEYTAUPE/BAMBOE-JALOEZIE_SMOKEYTAUPE_MRJEALOUSY_01_MAIN_KOORD_1500x1500_3990fc50-3b7e-4aa4-8a0e-496d729fb416.jpg"},
        {"name": "Teder Taupe",     "hex": "#D8CCBB", "material": "Hout", "sampleUrl": "/media/Catalogus/TEDERTAUPE/HOUTEN-JALOEZIE_TEDERTAUPE_MRJEALOUSY_KOORD_MAIN_1500x1500_UPDATE0025_5a28e143-4438-4139-8ee8-fe5878ac17c7.jpg"},
        {"name": "Tiki Taupe",      "hex": "#A69686", "material": "Hout", "sampleUrl": "/media/Catalogus/TIKITAUPE/BAMBOE-JALOEZIE_TIKITAUPE_MRJEALOUSY_01_MAIN_KOORD_1500x1500_fd8a7a0a-5f3f-4032-a715-6d0c2d7057ea.jpg"},
        {"name": "BBQ Black",       "hex": "#111111", "material": "Hout", "sampleUrl": "/media/Catalogus/BBQ-BLACK/BAMBOE-JALOEZIE_5081_BBQ-BLACK_MRJEALOUSY_01_MAIN_KOORD_1500x1500_UPDATE0025_48eb9015-6d2a-4f1e-bf23-9f3a4e14e3f6.jpg"},
        {"name": "Behoorlijk Black","hex": "#222222", "material": "Hout", "sampleUrl": "/media/Catalogus/BLACK/BAMBOE-JALOEZIE_5079_BLACK_MRJEALOUSY_01_MAIN_KOORD1500x1500-2_6929703f-b633-42fa-a265-223eddd8e237.jpg"},
        {"name": "Bonsai Bamboo",   "hex": "#6B8E23", "material": "Hout", "sampleUrl": "/media/Catalogus/BONZAI/BAMBOE-JALOEZIE_BONZAI_MRJEALOUSY_TOP_1024x1024_d3a38bca-34a8-4844-b1dd-6dc704eb0ce4.png"},
        {"name": "Bourbon Bamboo",  "hex": "#654321", "material": "Hout", "sampleUrl": "/media/Catalogus/BOURBON/BAMBOE-JALOEZIE_BOURBON_MRJEALOUSY_01_MAIN_KOORD_1500x1500_6ad88844-0811-4346-8f89-71b1dfecd9de.jpg"},
        {"name": "De Naturist",     "hex": "#D2B48C", "material": "Hout", "sampleUrl": "/media/Catalogus/NATURAL/BAMBOE-JALOEZIE_5072_NATURAL_MRJEALOUSY_TOP_1024x1024_ba7c8107-70d1-43dd-a529-02f4c3b971ab.png"},
        {"name": "Donker Brown",    "hex": "#3B2F2F", "material": "Hout", "sampleUrl": "/media/Catalogus/DARK-BROWN/BAMBOE-JALOEZIE_5072_DARK-BROWN_MRJEALOUSY_TOP_1024x1024_416f5253-08e5-4168-a8a3-7ff799951240.png"},
        {"name": "Eigenlijk Eiken", "hex": "#A0785A", "material": "Hout", "sampleUrl": "/media/Catalogus/OAK/BAMBOE-JALOEZIE_5072_OAK_MRJEALOUSY_TOP_1024x1024_d3ca885b-8fea-46a0-9a72-d2c5c7f1c65e.png"},
        {"name": "Flat White",      "hex": "#FFFAF0", "material": "Hout", "sampleUrl": "/media/Catalogus/WHITE/HOUTEN-JALOEZIE_WHITE_MRJEALOUSY_KOORD_MAIN_1500x1500_2d53cdc9-263f-4546-9a33-c66dcc9728e4.jpg"},
        {"name": "Gebroken White",  "hex": "#FDF5E6", "material": "Hout", "sampleUrl": "/media/Catalogus/GEBROKEN-WHITE/HOUTEN-JALOEZIE_GEBROKEN-WHITE_MRJEALOUSY_KOORD_MAIN_1500x1500_1f3f4314-50c3-46ed-80ee-9f6e4479f680.jpg"},
        {"name": "Haver Milk",      "hex": "#EFEBD8", "material": "Hout", "sampleUrl": "/media/Catalogus/HAVERMILK/BAMBOE-JALOEZIE_HAVERMILK_MRJEALOUSY_01_MAIN-SHUT_KOORD_1500x1500_7e2e1ca1-077a-41f3-86d1-ffc0b0f4b46d.jpg"},
        {"name": "Smokey Bamboo",   "hex": "#4A4A4A", "material": "Hout", "sampleUrl": "/media/Catalogus/SMOKEYTAUPE/BAMBOE-JALOEZIE_SMOKEYTAUPE_MRJEALOUSY_01_MAIN_KOORD_1500x1500_3990fc50-3b7e-4aa4-8a0e-496d729fb416.jpg"},
        {"name": "Deep Zwart",      "hex": "#080808", "material": "Hout", "sampleUrl": "/media/Catalogus/BBQ-BLACK/BAMBOE-JALOEZIE_5081_BBQ-BLACK_MRJEALOUSY_01_MAIN_KOORD_1500x1500_UPDATE0025_48eb9015-6d2a-4f1e-bf23-9f3a4e14e3f6.jpg"},
    ],
}


# ── DESCRIPTOR MAPS (migrated verbatim from TypeScript) ────────────────────────

STATE_MAP: Dict[str, str] = {
    "Tot de helft": (
        "lowered exactly halfway. The bottom 50% of the window is clear glass allowing "
        "direct sunlight to hit the floor/sill. The top 50% is covered by the blind, "
        "casting slat shadows."
    ),
    "Geheel uitgerold": (
        "fully lowered, covering the entire window height from top to bottom. The light "
        "entering the room is filtered through the slats, creating a soft striped shadow "
        "pattern on the floor/interior."
    ),
}

MOUNTING_MAP: Dict[str, str] = {
    "in de dag": (
        "**MOUNTING TYPE: INSIDE MOUNT — In de dag**\n"
        "\n"
        "DEFINITION: The blind is installed INSIDE the window recess (dagmaat), between the\n"
        "left and right reveals (dagvlakken). The headrail sits at the very top of the recess\n"
        "opening, on the front-most edge closest to the interior room.\n"
        "\n"
        "GEOMETRY:\n"
        "1. WIDTH: The blind width equals the internal clear opening of the recess minus\n"
        "   2–5 mm clearance on each side so the blind can move freely without touching\n"
        "   the reveals.\n"
        "2. HEIGHT: The blind drops from the headrail at the top of the recess down to (or\n"
        "   near) the window sill inside the recess.\n"
        "3. DEPTH POSITION: The headrail bracket is mounted at the FRONT EDGE of the recess\n"
        "   (the innermost wall face), leaving a minimum 10 mm shadow-gap between the\n"
        "   headrail back and the wall face. The blind hangs plumb inside the recess depth.\n"
        "4. WALL SURFACE: The interior wall, window casing, architraves, and sill AROUND the\n"
        "   recess remain fully EXPOSED and unobstructed. The blind does NOT overlap the wall.\n"
        "\n"
        "TILT-TURN / KANTEL-KIEPRAAM — CRITICAL CONSTRAINT:\n"
        "If the window is a tilt-turn (kantel-kiepraam / Dreh-Kipp / inward-opening):\n"
        "  - TOO DEEP IN RECESS: positioning the headrail too far back into the recess depth\n"
        "    causes the inward-swinging or inward-tilting sash to collide with the slat stack\n"
        "    or bottom rail when the window opens. THIS IS FORBIDDEN.\n"
        "  - TOO CLOSE TO WALL FACE: when the blind is raised (stacked), the bottom of the\n"
        "    stack extends below the window frame plane and protrudes outside the recess into\n"
        "    the room. THIS IS FORBIDDEN.\n"
        "  - CORRECT POSITION: mount at the front-most viable bracket position (front edge\n"
        "    of the recess, 10–15 mm from the interior wall face). The lowered blind hangs\n"
        "    within the glass plane; the raised stack clears the full opening arc of the sash.\n"
        "    The window handle must remain accessible at the front of the reveal.\n"
        "For fixed or outward-opening windows: depth placement is less critical; use\n"
        "front-edge mounting as default.\n"
        "\n"
        "SHADOW AND DEPTH:\n"
        "  - The headrail and slats are visually RECESSED inside the wall — they do NOT\n"
        "    protrude into the room beyond the wall face.\n"
        "  - Shadows from the slats fall onto the glass pane and onto the side reveals and\n"
        "    sill INSIDE the recess. There are no slat shadows on the outer wall surface.\n"
        "\n"
        "RENDER INSTRUCTIONS:\n"
        "  - Show the blind fitting snugly between the reveals with a narrow 2–5 mm gap\n"
        "    each side.\n"
        "  - Show the headrail flush with or very slightly behind the interior wall face.\n"
        "  - Do NOT extend blind, headrail, or bottom rail beyond the recess opening.\n"
        "  - Preserve the visible window frame, sill, and architraves around the recess."
    ),
    "op de dag": (
        "**MOUNTING TYPE: OUTSIDE MOUNT — Op de dag**\n"
        "\n"
        "DEFINITION: The blind is mounted on the WALL SURFACE, directly ABOVE the window\n"
        "frame (kozijn). The headrail bracket anchors to the flat wall plaster or masonry,\n"
        "positioned just above the top outer edge of the window frame — NOT on the frame\n"
        "itself, but on the wall above it.\n"
        "\n"
        "GEOMETRY:\n"
        "1. HEADRAIL POSITION: The headrail sits on the wall face immediately above the\n"
        "   top of the kozijn. The underside of the headrail starts approximately 2–5 cm\n"
        "   above the top frame edge, anchored into the wall substrate above the kozijn.\n"
        "2. WIDTH OVERLAP: The blind extends PAST the window opening: minimum 5–10 cm\n"
        "   beyond the left outer frame edge and minimum 5–10 cm beyond the right outer\n"
        "   frame edge. This overlap blocks side-light and covers the visible reveals.\n"
        "3. HEIGHT: From the headrail above the kozijn, the blind drops down to cover the\n"
        "   full window height including the kozijn frame itself, reaching to (or just\n"
        "   below) the sill level on the outside.\n"
        "4. FORWARD PROJECTION: The headrail and blind hang PROUD of the wall face, standing\n"
        "   off the wall by the bracket depth (typically 4–6 cm). This creates a visible\n"
        "   3D gap between the back of the blind and the wall surface.\n"
        "\n"
        "OBSTRUCTION CHECK ABOVE THE KOZIJN — CRITICAL:\n"
        "  - Inspect the wall surface ABOVE the kozijn for obstructions: ceiling proximity,\n"
        "    crown molding, wall cabinets, overhead radiators, pipes, electrical boxes,\n"
        "    or any other fixture.\n"
        "  - The brackets require a minimum clear wall height of approximately 6–8 cm\n"
        "    above the kozijn for proper anchoring.\n"
        "  - If the wall above is obstructed or ceiling clearance is insufficient, this\n"
        "    mounting method is not feasible — flag the obstruction in the render.\n"
        "\n"
        "3D LAYERING AND SHADOWS:\n"
        "  - Render a hard, physically accurate drop shadow cast from the headrail ONTO\n"
        "    the wall surface directly below and behind it.\n"
        "  - Slat shadows project onto the wall surface and floor according to the active\n"
        "    lighting condition and light angle.\n"
        "  - The blind partially or fully COVERS the window frame/kozijn when lowered —\n"
        "    this is physically correct and must be rendered as such.\n"
        "\n"
        "WALL AND FRAME PRESERVATION:\n"
        "  - Do NOT repaint or recolor the wall surface above, beside, or below the blind.\n"
        "  - Do NOT recolor the window frame/kozijn that is covered by the lowered blind.\n"
        "  - The wall retains its original material and color everywhere the blind does\n"
        "    not cover it.\n"
        "\n"
        "RENDER INSTRUCTIONS:\n"
        "  - Show the headrail on the wall above the kozijn, not on the frame.\n"
        "  - Show the blind extending 5–10 cm past both side edges of the window frame.\n"
        "  - Render the visible gap between the back of the blind and the wall surface.\n"
        "  - Render the drop shadow from the headrail onto the wall behind the blind.\n"
        "  - The blind is a physically separate 3D object standing in front of the wall."
    ),
    "Twee aparte jaloezieën voor hoekraam": "as two separate blinds for the corner window",
}

LIGHTING_MAP: Dict[str, str] = {
    "Ochtend (Koel)": (
        "MORNING LIGHT. Low angle sunlight from the East. Color Temp: 5500K (Cool/Fresh). "
        "Shadows: Long, crisp shadows projected deep into the room. Atmosphere: Crisp, energetic."
    ),
    "Middag (Helder)": (
        "MID-DAY SUN. High angle overhead sunlight. Color Temp: 6000K (Neutral White). "
        "Shadows: Short, sharp, high-contrast shadows on the window sill and floor. "
        "Atmosphere: Bright, clear, revealing."
    ),
    "Zonsondergang (Warm)": (
        "GOLDEN HOUR. Very low angle sunlight from the West. Color Temp: 3500K (Warm/Orange/Gold). "
        "Shadows: Extremely long, dramatic, stretching across the floor. "
        "Reflections: Warm metallic glow on slats. Atmosphere: Cozy, romantic."
    ),
    "Avond (Sfeervol)": (
        "EVENING/NIGHT. No direct sunlight. Light Source: Artificial interior lamps "
        "(Warm White 2700K). Shadows: Soft, multi-directional from room lights. "
        "Reflections: Interior room reflected in the glass. Atmosphere: Intimate, dark outside."
    ),
    "Bewolkt (Diffuus)": (
        "OVERCAST/CLOUDY. Diffuse, soft white light (6500K). No hard direct sunlight. "
        "Shadows: Very soft, ambient occlusion only, no hard projection. "
        "Atmosphere: Soft, even, calm."
    ),
}

PRODUCT_MAP: Dict[str, str] = {
    "Houten Jaloezieën": (
        "Premium Wooden Horizontal Venetian Blinds. "
        "Material physics: Matte or Satin finish, visible wood grain texture, "
        "absorbs light, warm reflections."
    ),
    "Aluminium Jaloezieën": (
        "Sleek Aluminum Horizontal Venetian Blinds. "
        "Material physics: Smooth metallic finish, slight specular highlights, "
        "reflects light, cool/sharp reflections."
    ),
}


# ── MASTER PROMPT ──────────────────────────────────────────────────────────────
#
# PROMPT 1 — ANALYSIS / DECISION PROMPT
# This is the single source of truth for all identity, laws, rules, and
# forbidden behaviors. Every phase prompt is built on top of this foundation.
# The placeholder [CATALOG] is replaced at runtime with the full catalog text.
#
MASTER_PROMPT = """\
You are a World-Class Interior Vision Architect, Window Treatment Surveyor, Product Configurator, \
and Lighting Physicist with elite computer vision precision.
You specialize exclusively in high-end horizontal Venetian blinds for Mr. Jealousy.

MISSION
Analyse the uploaded room image with forensic, pixel-level precision and return one technically \
correct, catalog-locked, installation-aware JSON object that can be used by a separate rendering \
model to place the blind photorealistically onto the window.

You are not a general interior assistant. You operate as a combined:
- interior architect
- blind installer
- window surveyor
- material and color analyst
- lighting physicist
- catalog-matching expert
- visualization planner

ABSOLUTE PRODUCT LOCK
You may ONLY use products that literally exist in the Mr. Jealousy catalog below.

ONLY ALLOWED:
  Houten Jaloezieën
  Aluminium Jaloezieën
  Allowed wooden subtypes only: Paulownia, Bamboo, Abachi

STRICTLY FORBIDDEN:
  Any product other than Houten Jaloezieën or Aluminium Jaloezieën
  Invented products
  Invented materials
  Invented colors not present in the catalog
  Invented finish names
  Free interpretation outside the catalog

GOLDEN RULE
A beautiful recommendation that cannot exist physically is a failed result.

PRIMARY PRIORITIES
1. physical correctness
2. mounting correctness
3. catalog truth
4. window geometry correctness
5. perspective realism planning
6. style harmony
7. commercial relevance

CORE RULE
Do not treat the window as a flat rectangle. Treat it as a functional architectural object with:
  frame depth, glass sections, sash logic, hardware, reveal geometry, sill,
  opening motion, mounting constraints, obstacle zones, light interaction.

MR. JEALOUSY CATALOG (AUTHORITATIVE — DO NOT INVENT OUTSIDE THIS LIST):
[CATALOG]

OUTPUT OBLIGATION
Return ONLY valid JSON in Dutch. No markdown. No code fences. No explanation before or after.

FAIL CONDITIONS — output is wrong if:
  - it suggests a non-catalog product
  - it uses a non-catalog color
  - it invents materials
  - it ignores visible handles/vents/locks
  - it ignores recess depth logic
  - it fails to count glass sections
  - it gives generic style commentary
  - it outputs invalid JSON
  - it outputs anything other than Dutch JSON
  - it prioritizes beauty over feasibility
  - it treats the window as a flat decorative area instead of a functional architectural object
"""


# ── PHASE LAWS ─────────────────────────────────────────────────────────────────

PHASE_LAWS: Dict[int, Dict[str, Any]] = {
    1: {
        "name": "IMAGE_UPLOAD",
        "laws": [
            "Upload the image to Supabase simultaneously with triggering analyse_claude.py.",
            "The result is a temporary cached JSON file at data/json_convert_to_text.txt.",
            "The JSON must be read and interpreted as a fundamental law to obey.",
            "All applicable files given in Phase 1 are chronologically ordered and mandatory to follow.",
            "You may not self-interpret. Laws are given; you must obey.",
        ],
        "negative_seeds": [],  # TODO: populate in next session
    },
    2: {
        "name": "IMAGE_QUALITY_COMPLIANCE",
        "laws": [
            "Check: Alignment — the image must show the window/room without extreme rotation.",
            "Check: Framing — the window must be clearly visible and not cut off.",
            "Check: Lighting — the image must not be completely dark or overexposed.",
            "Check: Focus / Blur — the image must not be so blurry that the window is unreadable.",
            "Check: Resolution — the image must have sufficient resolution to analyse window details.",
            "Check: Angle — the viewing angle must allow forensic window analysis.",
            "Check: Image Size — the image must be within the accepted size limits.",
            "Check: Unwanted content — no explicit, offensive, or unrelated content.",
            "Check: Format — the image must be PNG, JPG, or WEBP.",
            "If any check fails: return an error message with specific feedback on what to improve.",
            "If all checks pass: proceed to Phase 3.",
        ],
        "negative_seeds": [],  # TODO: populate in next session
    },
    3: {
        "name": "EXTRACT_INTERIOR_THESIS",
        "laws": [
            "Determine: style (e.g., Japandi, Industrial, Hotel Chic, Scandinavisch, etc.)",
            "Determine: room mood",
            "Determine: luxury level",
            "Determine: warmth/coolness of the space",
            "Determine: material language (dominant materials visible)",
            "Determine: line language (horizontal, vertical, curved, geometric)",
            "Determine: spatial calm/density",
            "Write: style — single label string",
            "Write: styleSummary — maximum 2 sentences",
            "Write: styleDescription — minimum 200 words in Dutch, one paragraph per header, "
            "one blank line between each header paragraph",
        ],
        "negative_seeds": [],  # TODO: populate in next session
    },
    4: {
        "name": "EXTRACT_COLOR_DNA",
        "laws": [
            "Extract exactly 5 real visible colors from the room.",
            "Each matched_catalog_color must literally exist in the MR. JEALOUSY catalog.",
            "Each color must come from a clearly visible room surface or object.",
            "hex_code must be a valid 6-digit hex code (e.g. #AEC6CF).",
            "For each of the 5 colors return: hex_code, extracted_source, matched_catalog_color.",
        ],
        "negative_seeds": [],  # TODO: populate in next session
    },
    5: {
        "name": "WINDOW_ARCHITECTURE",
        "laws": [
            "Determine: outer frame bounds",
            "Determine: visible glass bounds",
            "Determine: exact number of distinct visible glass sections",
            "Determine: sash divisions",
            "Determine: mullions/transoms if visible",
            "Determine: recess depth estimate (in cm)",
            "Determine: sill presence and depth",
            "Determine: frame material",
            "Determine: handle presence and side (left/right)",
            "Determine: vent/grille/lock/sensor/protrusion presence",
            "Determine: likely opening mechanism",
            "Determine: likely opening direction (inward/outward)",
            "Determine: fixed or operable",
            "Determine: nearby collision risks with wall/furniture/radiator",
            "Determine: type of glazing",
            "Determine: stack height clearance (distance from top of sash to ceiling)",
            "Determine: structural substrate",
            "Determine: corner proximity",
            "Classify window type as precisely as possible: "
            "Tilt and turn / Fixed / Casement / Sliding / Pivot / French / Multi-pane",
            "Count the EXACT number of distinct visible glass sections.",
            "State any exceptions worth pointing out which impact the mounting strategy.",
        ],
        "negative_seeds": [],  # TODO: populate in next session
    },
    6: {
        "name": "MOUNTING_STRATEGY",
        "laws": [
            "NEVER propose a physically impossible placement.",
            "RULE 1 — DEPTH THRESHOLD (The Foundation): "
            "IF recess depth < 5 cm → OUTSIDE MOUNT (op de dag) is mandatory. "
            "Reason: inadequate surface area for bracket tension and headrail stability.",
            "RULE 2 — PROTRUSION & CLEARANCE (The Obstacle): "
            "IF handle/vent/sensor exists AND protrusion depth > recess depth → "
            "OUTSIDE MOUNT (op de dag) is mandatory. "
            "IF handle/vent/sensor exists AND recess depth is 5–15 cm → "
            "INSIDE MOUNT (in de dag), but shift position to the outermost front edge (flush with wall).",
            "RULE 3 — KINEMATIC COLLISION (The Tilt & Turn Factor): "
            "IF window type = Tilt and turn OR Inward Opening → run stack calculation: "
            "stack_height = (window_height / 10) + 10 cm (for Wood/Bamboo). "
            "IF top clearance (sash to ceiling) < stack_height → OUTSIDE MOUNT is mandatory. "
            "Note: the blind must be mounted high enough so the sash clears the stack when opened.",
            "RULE 4 — LATERAL COLLISION (The Corner Risk): "
            "IF side clearance (frame to wall) < 3 cm AND mounting = outside → "
            "FLAG ERROR: 'Insufficient lateral space for overlap; check for corner collision.'",
            "RULE 5 — DEFAULT SELECTION: "
            "IF Rules 1–4 are all false → INSIDE MOUNT (in de dag). "
            "Placement: recessed 10 mm from the wall edge for a clean architectural shadow-gap.",
        ],
        "negative_seeds": [],  # TODO: populate in next session
    },
    7: {
        "name": "LIGHTING_CONDITIONS",
        "laws": [
            "Determine: light direction",
            "Determine: light intensity (lux estimate)",
            "Determine: light softness/hardness",
            "Determine: light temperature (warm/cool, approximate Kelvin)",
            "Determine: natural vs artificial contribution (% each)",
            "Determine: reflection behavior on glass/frame",
            "Determine: probable shadow behavior inside the room",
            "Determine: whether wood or aluminium integrates more naturally with this light",
        ],
        "negative_seeds": [],  # TODO: populate in next session
    },
    8: {
        "name": "CATALOG_MATCH",
        "laws": [
            "ABSOLUTE PRODUCT LOCK: You may ONLY use products that literally exist in the "
            "MR. JEALOUSY catalog.",
            "ONLY ALLOWED product types: Houten Jaloezieën, Aluminium Jaloezieën.",
            "Allowed wooden subtypes only: Paulownia, Bamboo, Abachi.",
            "STRICTLY FORBIDDEN: any product other than Houten Jaloezieën or Aluminium Jaloezieën.",
            "STRICTLY FORBIDDEN: invented products.",
            "STRICTLY FORBIDDEN: invented materials.",
            "STRICTLY FORBIDDEN: invented colors not present in the catalog.",
            "STRICTLY FORBIDDEN: invented finish names.",
            "STRICTLY FORBIDDEN: free interpretation outside the catalog.",
        ],
        "negative_seeds": [],  # TODO: populate in next session
    },
    9: {
        "name": "RENDER_PLANNING",
        "laws": [
            "Prepare exact render instructions for the visualization model.",
            "Output must conform to the RenderInstruction schema.",
            "scene_description must be a minimum of 200 words in Dutch.",
            "The mounting geometry rules from Phase 6 must be reflected verbatim in the instruction.",
            "The lighting physics determined in Phase 7 must drive shadow and reflection specifications.",
            "The product and color must exactly match the Phase 8 catalog selection.",
            "Include a negative_prompt listing all rendering artifacts to avoid.",
            "Specify camera_angle matching the original uploaded image perspective.",
        ],
        "negative_seeds": [],  # TODO: populate in next session
    },
}


# ── HELPER FUNCTIONS ───────────────────────────────────────────────────────────

def get_phase_prompt(phase: int) -> str:
    """
    Build the complete system prompt for a given phase number.
    Injects the live catalog into MASTER_PROMPT, then appends the phase name,
    all phase laws, and negative seeds.
    Returns a single string ready to be sent as the system prompt to Claude.
    """
    if phase not in PHASE_LAWS:
        raise ValueError(f"Phase {phase} does not exist. Valid phases: 1–{PHASE_COUNT}.")

    # Inject catalog into the master prompt at runtime
    base_prompt = MASTER_PROMPT.replace("[CATALOG]", get_catalog_as_text())

    entry = PHASE_LAWS[phase]
    laws_text = "\n".join(f"  - {law}" for law in entry["laws"])

    negative_text = ""
    if entry["negative_seeds"]:
        seeds = "\n".join(f"  - {seed}" for seed in entry["negative_seeds"])
        negative_text = f"\nNEGATIVE SEEDS (forbidden behaviors in this phase):\n{seeds}"

    return (
        f"{base_prompt}\n"
        f"{'─' * 60}\n"
        f"ACTIVE PHASE: {phase} — {entry['name']}\n"
        f"{'─' * 60}\n"
        f"LAWS FOR THIS PHASE (mandatory, in order):\n{laws_text}"
        f"{negative_text}"
    )


def get_catalog_as_text() -> str:
    """
    Format MR_JEALOUSY_CATALOG as plain readable text for injection into prompts.
    Each product type is listed with all its colors (name + hex).
    """
    lines: List[str] = ["MR. JEALOUSY CATALOG (authoritative — only these products exist):"]
    for product_type, colors in MR_JEALOUSY_CATALOG.items():
        lines.append(f"\n{product_type}:")
        for color in colors:
            lines.append(f"  - {color['name']} | hex: {color['hex']} | material: {color['material']}")
    return "\n".join(lines)


def get_allowed_colors(product_type: str) -> List[ProductColor]:
    """Return the full color list for a given product type from the catalog."""
    if product_type not in MR_JEALOUSY_CATALOG:
        raise ValueError(
            f"Product type '{product_type}' not in catalog. "
            f"Allowed: {ALLOWED_PRODUCT_TYPES}"
        )
    return MR_JEALOUSY_CATALOG[product_type]


def validate_phase_order(current: int, expected: int) -> bool:
    """
    Enforce chronological phase execution.
    Returns True only if current == expected.
    Use this before executing any phase to prevent out-of-order calls.
    """
    return current == expected


def resolve_mounting(key: str) -> str:
    """
    Return the full mounting description string from MOUNTING_MAP.
    Defaults to 'in de dag' if the key is not found.
    """
    return MOUNTING_MAP.get(key, MOUNTING_MAP["in de dag"])


def resolve_lighting(key: str) -> str:
    """
    Return the full lighting description string from LIGHTING_MAP.
    Defaults to 'Middag (Helder)' if the key is not found.
    """
    return LIGHTING_MAP.get(key, LIGHTING_MAP["Middag (Helder)"])
