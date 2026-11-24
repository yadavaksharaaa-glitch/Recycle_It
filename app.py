import streamlit as st
import html
import random

st.set_page_config(
    page_title="ReCycleIt",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. WASTE DATABASE
# DICTIONARIES store categories; LISTS store item names under each category.

waste = {
    "Plastic Waste": [
        "plastic bottle", "water bottle", "shampoo bottle",
        "plastic bag", "shopping bag", "plastic wrapper",
        "chips packet", "snack packet", "plastic straw",
        "plastic cup", "plastic container", "milk pouch",
        "bread bag", "plastic spoon", "plastic fork",
        "detergent bottle", "plastic lid", "food packaging",
        "toothpaste tube", "plastic bucket"
    ],
    "Paper and Cardboard": [
        "paper", "newspaper", "notebook", "magazine",
        "old book", "paper bag", "envelope", "cardboard",
        "cardboard box", "pizza box", "egg carton",
        "cereal box", "office paper", "paper sheet",
        "wrapping paper"
    ],
    "Organic Waste": [
        "banana peel", "banana skin", "orange peel",
        "apple core", "potato peel", "onion peel",
        "vegetable peels", "fruit peels", "eggshell",
        "tea leaves", "coffee grounds", "leftover food",
        "spoiled food", "rice", "bread", "flowers",
        "dry leaves", "vegetable waste", "fruit waste",
        "carrot peel", "coconut shell", "food scraps"
    ],
    "Glass": [
        "glass bottle", "glass jar", "jam jar",
        "sauce jar", "glass container", "broken glass",
        "glass cup"
    ],
    "Metal": [
        "metal can", "tin can", "aluminium can",
        "aluminum can", "soda can", "metal foil",
        "aluminium foil", "metal spoon", "metal utensils",
        "metal lid", "steel can"
    ],
    "Electronic Waste": [
        "mobile phone", "old phone", "smartphone",
        "laptop", "computer", "keyboard", "mouse",
        "charger", "charging cable", "earphones",
        "headphones", "television", "printer",
        "camera", "tablet", "power bank", "remote control",
        "computer monitor", "usb drive", "old watch"
    ],
    "Hazardous Waste": [
        "battery", "used battery", "rechargeable battery",
        "bulb", "tube light", "paint can", "paint",
        "pesticide container", "chemical container",
        "expired medicine", "old medicine", "aerosol can",
        "nail polish", "cleaning chemical"
    ],
    "Clothing and Textile": [
        "old clothes", "shirt", "t shirt", "jeans",
        "dress", "socks", "shoes", "old shoes",
        "fabric", "cloth", "bedsheet", "blanket",
        "towel", "curtain", "handbag", "scarf"
    ],
    "Other Waste": [
        "diaper", "nappy", "sanitary pad",
        "sanitary napkin", "thermocol", "styrofoam",
        "ceramic", "broken plate", "mirror",
        "rubber", "old tyre", "cigarette butt"
    ]
}

disposal = {
    "Plastic Waste": "Empty the item, rinse it if needed, and let it dry. Check whether your local recycling facility accepts it.",
    "Paper and Cardboard": "Keep paper and cardboard clean and dry. Flatten cardboard boxes before recycling.",
    "Organic Waste": "Separate food scraps from dry waste. Compost them whenever possible.",
    "Glass": "Keep glass separate and check local glass collection rules. Handle broken glass carefully.",
    "Metal": "Clean and empty metal items before recycling if accepted locally.",
    "Electronic Waste": "Take electronics to an authorised e-waste collection centre. Never put them in regular household waste.",
    "Hazardous Waste": "Keep hazardous items separate and use an authorised collection facility.",
    "Clothing and Textile": "Donate wearable clothes. Send damaged textiles to a suitable collection or recycling programme.",
    "Other Waste": "Check local waste collection guidelines because these items may need special disposal."
}

tips = {
    "Plastic Waste": "Carry reusable bags and bottles to reduce single-use plastic.",
    "Paper and Cardboard": "Reuse paper and cardboard before recycling.",
    "Organic Waste": "Compost food scraps to reduce landfill waste.",
    "Glass": "Reuse glass jars and bottles whenever possible.",
    "Metal": "Reuse metal containers and recycle accepted metal items.",
    "Electronic Waste": "Repair or donate working electronics instead of replacing them.",
    "Hazardous Waste": "Use authorised collection programmes for safe disposal.",
    "Clothing and Textile": "Donate, repair or reuse old clothes.",
    "Other Waste": "Choose reusable products whenever possible."
}

bin_guidance = {
    "Plastic Waste": "Keep accepted plastic packaging clean and dry. Check local recycling rules because not all plastics are collected.",
    "Paper and Cardboard": "Use the paper recycling collection for clean, dry paper and cardboard.",
    "Organic Waste": "Place suitable food and garden scraps in a compost or organic-waste collection.",
    "Glass": "Use a designated glass collection point where available. Wrap broken glass safely before disposal.",
    "Metal": "Place accepted clean metal cans and containers in the appropriate recycling collection.",
    "Electronic Waste": "Take electronics to an authorised e-waste collection point.",
    "Hazardous Waste": "Use a designated hazardous-waste collection service. Keep these items away from ordinary bins.",
    "Clothing and Textile": "Donate wearable textiles or use a textile collection programme.",
    "Other Waste": "Check local municipal guidance for items that cannot be recycled through regular collections."
}

category_info = {
    "Plastic Waste": ("♻️", "Bottles, wrappers, bags and packaging"),
    "Paper and Cardboard": ("📄", "Newspapers, boxes, notebooks and paper"),
    "Organic Waste": ("🌿", "Food scraps, peels, leaves and garden waste"),
    "Glass": ("🍶", "Glass bottles, jars and containers"),
    "Metal": ("🥫", "Cans, foil and metal containers"),
    "Electronic Waste": ("🔌", "Phones, chargers, computers and cables"),
    "Hazardous Waste": ("⚠️", "Batteries, bulbs, chemicals and paint"),
    "Clothing and Textile": ("👕", "Clothes, shoes, fabric and household textiles"),
    "Other Waste": ("🗑️", "Items needing special or local disposal guidance")
}


# 2. ECO-FRIENDLY TIPS
# DICTIONARIES and LISTS organise tips by topic.

eco_sections = {
    "Reduce and Reuse": [
        ("Carry a reusable bottle", "Keep a refillable water bottle with you instead of buying single-use plastic bottles."),
        ("Bring your own shopping bag", "Keep a cloth bag in your backpack or car so you do not need a new plastic bag."),
        ("Repair before replacing", "Try repairing clothes, appliances and electronics before buying something new."),
        ("Reuse containers", "Use clean jars and containers for storage instead of throwing them away.")
    ],
    "At Home": [
        ("Separate waste", "Keep wet or organic waste separate from dry recyclable materials."),
        ("Save electricity", "Switch off lights, fans and appliances when they are not being used."),
        ("Use both sides of paper", "Make use of both sides of sheets before recycling them."),
        ("Choose refill packs", "Where practical, choose refillable products and packaging that uses less material.")
    ],
    "Food and Composting": [
        ("Plan meals", "Plan meals and portions to avoid buying more food than you can use."),
        ("Compost food scraps", "Compost suitable fruit and vegetable peels, tea leaves and coffee grounds."),
        ("Store food properly", "Store ingredients correctly so they stay fresh for longer."),
        ("Use leftovers", "Turn suitable leftovers into another meal instead of wasting them.")
    ],
    "Smart Shopping": [
        ("Choose less packaging", "Look for products with minimal or recyclable packaging where possible."),
        ("Buy only what you need", "Make a list before shopping to reduce unnecessary purchases."),
        ("Choose durable products", "Products that last longer often create less waste over time."),
        ("Donate usable items", "Pass on clothes, books and household items that are still in good condition.")
    ],
    "Safe Disposal": [
        ("Recycle e-waste properly", "Take old phones, chargers and electronics to authorised e-waste collection points."),
        ("Keep batteries separate", "Do not put used batteries in ordinary household waste; use an authorised collection point."),
        ("Handle broken glass carefully", "Wrap broken glass securely and follow local collection instructions."),
        ("Follow local rules", "Recycling facilities and accepted materials differ by location, so check municipal guidance.")
    ]
}


# 3. HELPER FUNCTIONS
# FUNCTIONS organise reusable tasks.
# STRING METHODS (lower, strip, split) clean the user's input.
# LOOPS check items; CONDITIONALS decide whether a match is found.

def identify_waste(item):
    item = item.lower().strip()
    words = item.split()

    while words and words[0] in ["a", "an", "the", "old", "used"]:
        words.pop(0)

    item = " ".join(words)
    for category, items in waste.items():
        if item in items:
            return category
    return None


def show_result(item, category):
    safe_item = html.escape(item.title())
    safe_category = html.escape(category)
    safe_disposal = html.escape(disposal[category])
    safe_tip = html.escape(tips[category])

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-top">
                <span class="result-icon">♻️</span>
                <div>
                    <div class="result-label">WASTE IDENTIFIED</div>
                    <div class="result-category">{safe_category}</div>
                </div>
            </div>
            <div class="result-details">
                <p><b>Item</b><span>{safe_item}</span></p>
                <p><b>How to dispose</b><span>{safe_disposal}</span></p>
                <p><b>Eco-friendly tip</b><span>{safe_tip}</span></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# 4. SESSION STATE
# CONDITIONALS check whether session values already exist.

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "last_item" not in st.session_state:
    st.session_state.last_item = ""

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "sorting_category" not in st.session_state:
    st.session_state.sorting_category = "Plastic Waste"

if "random_tip" not in st.session_state:
    st.session_state.random_tip = None


def navigate(page):
    st.session_state.page = page


# 5. DESIGN

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #101512;
    --sidebar: #171e19;
    --surface: #1b241e;
    --surface2: #222d25;
    --surface3: #29372d;
    --green: #4b9b67;
    --green-light: #91d5a5;
    --green-dark: #285b3a;
    --text: #f1f5f1;
    --muted: #a9b7ad;
    --border: #34443a;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

.stApp {
    background:
        radial-gradient(ellipse at 78% 0%, rgba(54, 112, 70, 0.12), transparent 38%),
        var(--bg);
    color: var(--text);
}

[data-testid="stHeader"] {
    background: rgba(16, 21, 18, 0.94);
}

.block-container {
    max-width: 1450px;
    padding: 2.2rem 3rem 3rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--sidebar);
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] > div:first-child {
    padding: 1.5rem 1rem;
}

.brand {
    font-size: 1.8rem;
    font-weight: 800;
    letter-spacing: -0.7px;
    color: var(--text);
    padding: 0.3rem 0 0.7rem;
}

.brand span {
    color: var(--green-light);
}

.sidebar-caption {
    color: #829188;
    font-size: 0.72rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-weight: 700;
    margin: 1.1rem 0 0.55rem;
}

.sidebar-tagline {
    color: #f1f5f1 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 2.1rem !important;
    font-weight: 600 !important;
    line-height: 1.2 !important;
    letter-spacing: -1px !important;
    margin: 2.1rem 0 0.8rem !important;
    max-width: 100%;
}

[data-testid="stSidebar"] .stButton button {
    min-height: 43px;
    border-radius: 9px !important;
    text-align: left;
    font-size: 0.88rem;
    padding: 0.55rem 0.8rem;
}

[data-testid="stSidebar"] .stButton button[kind="secondary"] {
    background: transparent !important;
    border: 1px solid transparent !important;
    color: #bdc9c0 !important;
}

[data-testid="stSidebar"] .stButton button[kind="secondary"]:hover {
    background: #243329 !important;
    border-color: #34513c !important;
    color: var(--green-light) !important;
}

[data-testid="stSidebar"] .stButton button[kind="primary"] {
    background: #2e7046 !important;
    border: 1px solid #438b5a !important;
    color: white !important;
}

[data-testid="stSidebar"] .stCaption {
    color: #829188 !important;
}

/* Typography */
.eyebrow {
    color: var(--green-light);
    text-transform: uppercase;
    letter-spacing: 1.8px;
    font-size: 0.72rem;
    font-weight: 800;
    margin-bottom: 0.55rem;
}

.hero-title {
    font-size: clamp(2rem, 3.3vw, 3rem);
    line-height: 1.15;
    letter-spacing: -1.4px;
    font-weight: 800;
    color: var(--text);
    margin: 0 0 0.55rem;
}

.page-title {
    font-size: 2rem;
    line-height: 1.2;
    letter-spacing: -0.8px;
    font-weight: 800;
    color: var(--text);
    margin-bottom: 0.45rem;
}

.page-subtitle {
    color: var(--muted);
    font-size: 0.96rem;
    line-height: 1.65;
    margin-bottom: 1.8rem;
}

.section-title {
    font-size: 1.25rem;
    font-weight: 750;
    color: var(--text);
    margin: 0.15rem 0 0.35rem;
}

.section-subtitle {
    color: var(--muted);
    font-size: 0.86rem;
    margin-bottom: 1rem;
}

/* Dashboard hero */
.hero-panel {
    background: linear-gradient(115deg, #1b3022 0%, #1b261f 60%, #202a23 100%);
    border: 1px solid #35533d;
    border-radius: 18px;
    padding: 2rem 2.1rem;
    margin: 0.8rem 0 1.8rem;
    position: relative;
    overflow: hidden;
}

.hero-panel:after {
    content: "♻";
    position: absolute;
    right: 2.5rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 7rem;
    color: rgba(145, 213, 165, 0.10);
    pointer-events: none;
}

.hero-kicker {
    color: var(--green-light);
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 1.8px;
    margin-bottom: 0.75rem;
}

.hero-copy {
    color: #c0cdc3;
    font-size: 0.95rem;
    max-width: 650px;
    line-height: 1.7;
}

/* Category tiles */
.category-tile {
    background: linear-gradient(145deg, #222e26, #1b241e);
    border: 1px solid var(--border);
    border-radius: 13px;
    min-height: 125px;
    padding: 1rem;
    margin-bottom: 0.9rem;
    transition: 0.2s ease;
}

.category-tile:hover {
    border-color: var(--green);
    background: #26372b;
}

.category-icon {
    font-size: 1.55rem;
    margin-bottom: 0.65rem;
}

.category-name {
    color: var(--text);
    font-size: 0.88rem;
    font-weight: 700;
    margin-bottom: 0.25rem;
}

.category-description {
    color: var(--muted);
    font-size: 0.72rem;
    line-height: 1.45;
}

/* Feature cards */
.st-key-feature_identification button,
.st-key-feature_sorting button,
.st-key-feature_tips button {
    min-height: 158px !important;
    height: 158px !important;
    width: 100%;
    white-space: pre-wrap !important;
    text-align: left !important;
    justify-content: flex-start !important;
    align-items: flex-start !important;
    padding: 1.15rem !important;
    background: linear-gradient(145deg, #222e26, #1b241e) !important;
    border: 1px solid #35473a !important;
    border-radius: 14px !important;
    color: var(--text) !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
    line-height: 1.55 !important;
    transition: 0.2s ease;
}

.st-key-feature_identification button:hover,
.st-key-feature_sorting button:hover,
.st-key-feature_tips button:hover {
    background: #293a2e !important;
    border-color: var(--green) !important;
    transform: translateY(-2px);
}

.st-key-feature_identification button p,
.st-key-feature_sorting button p,
.st-key-feature_tips button p {
    white-space: pre-wrap !important;
    text-align: left !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
    line-height: 1.55 !important;
}

/* Search and forms */
[data-testid="stForm"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}

.stTextInput label, .stSelectbox label {
    color: #dce5de !important;
    font-weight: 600 !important;
}

.stTextInput input,
.stSelectbox div[data-baseweb="select"] > div {
    background: #202a23 !important;
    color: var(--text) !important;
    border: 1px solid #3a4b3f !important;
    border-radius: 9px !important;
    min-height: 46px;
}

.stTextInput input:focus {
    border-color: var(--green) !important;
    box-shadow: 0 0 0 1px var(--green) !important;
}

.stTextInput input::placeholder {
    color: #8d9b91 !important;
    opacity: 1;
}

.stButton button[kind="primary"],
[data-testid="stFormSubmitButton"] button {
    background: #347a4b !important;
    color: white !important;
    border: 1px solid #438b5a !important;
    border-radius: 9px !important;
    font-weight: 700 !important;
    min-height: 45px;
}

.stButton button[kind="primary"]:hover,
[data-testid="stFormSubmitButton"] button:hover {
    background: #408b58 !important;
    border-color: #68b77e !important;
}

.stButton button[kind="secondary"] {
    background: #202a23 !important;
    color: #dce7df !important;
    border: 1px solid #354139 !important;
    border-radius: 9px !important;
}

/* Results */
.result-card {
    background: linear-gradient(120deg, #1d3425, #1b2a20);
    border: 1px solid #3b6848;
    border-left: 4px solid var(--green);
    border-radius: 14px;
    padding: 1.35rem 1.5rem;
    margin: 1.25rem 0 1.6rem;
}

.result-top {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 1rem;
}

.result-icon {
    font-size: 1.8rem;
}

.result-label {
    color: var(--green-light);
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 1.5px;
}

.result-category {
    color: white;
    font-size: 1.15rem;
    font-weight: 750;
    margin-top: 0.15rem;
}

.result-details p {
    display: flex;
    gap: 0.7rem;
    color: #d7e2da;
    font-size: 0.88rem;
    line-height: 1.65;
    margin: 0.45rem 0;
}

.result-details b {
    min-width: 145px;
    color: #a9d9b5;
}

/* Sorting detail */
.detail-panel {
    background: #1d2a21;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.25rem;
}

.detail-heading {
    color: var(--green-light);
    font-size: 1rem;
    font-weight: 750;
    margin-bottom: 0.65rem;
}

.example-chip {
    display: inline-block;
    background: #26372b;
    border: 1px solid #354b3b;
    color: #dce7df;
    padding: 0.38rem 0.65rem;
    margin: 0.2rem 0.25rem 0.2rem 0;
    border-radius: 7px;
    font-size: 0.78rem;
}

/* Tip cards */
.tip-card {
    background: linear-gradient(145deg, #222e26, #1b241e);
    border: 1px solid var(--border);
    border-radius: 13px;
    padding: 1rem 1.1rem;
    min-height: 125px;
    margin-bottom: 0.7rem;
}

.tip-title {
    color: #eaf3ec;
    font-size: 0.9rem;
    font-weight: 700;
    margin-bottom: 0.45rem;
}

.tip-copy {
    color: var(--muted);
    font-size: 0.8rem;
    line-height: 1.6;
}

.tip-number {
    color: var(--green-light);
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 0.35rem;
}

hr {
    border-color: var(--border) !important;
}

.stAlert {
    background: #202a23 !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
}

small, .stCaption {
    color: var(--muted) !important;
}

@media (max-width: 850px) {
    .block-container {
        padding: 1.4rem 1rem 2rem;
    }
    .hero-panel {
        padding: 1.4rem;
    }
    .hero-panel:after {
        display: none;
    }
    .result-details p {
        display: block;
    }
    .result-details b {
        display: block;
    }
}
</style>
""", unsafe_allow_html=True)


# 6. SIDEBAR NAVIGATION
# LOOPS create navigation buttons; CONDITIONALS highlight the active page.

with st.sidebar:
    st.markdown(
        '<div class="brand">♻️ <span>ReCycle</span>It</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="sidebar-caption">MAIN MENU</div>', unsafe_allow_html=True)

    menu = [
        ("Dashboard", "⌂   Dashboard Overview"),
        ("Identification", "♻   Waste Identification"),
        ("Sorting", "▤   Smart Bin Sorting"),
        ("Tips", "✳   Eco-Friendly Tips")
    ]

    for page, label in menu:
        if st.button(
            label,
            key=f"nav_{page}",
            use_container_width=True,
            type="primary" if st.session_state.page == page else "secondary"
        ):
            navigate(page)
            st.rerun()

    st.markdown("---")
    st.markdown(
        '<div class="sidebar-tagline">Small actions. Cleaner planet.</div>',
        unsafe_allow_html=True
    )


# 7. DASHBOARD
# LOOPS display category cards and feature buttons from lists.

if st.session_state.page == "Dashboard":

    st.markdown(
        """
        <div class="hero-panel">
            <div class="hero-kicker">WELCOME TO RECYCLEIT</div>
            <div class="hero-title">Make every waste choice count.</div>
            <div class="hero-copy">
                A simple way to understand waste, sort it responsibly and build
                everyday habits that are kinder to the planet.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="eyebrow">KNOW YOUR WASTE</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Explore the 9 waste categories</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Get familiar with the different types of waste ReCycleIt can help you sort.</div>',
        unsafe_allow_html=True
    )

    category_columns = st.columns(3, gap="medium")
    for index, (category, info) in enumerate(category_info.items()):
        icon, description = info
        with category_columns[index % 3]:
            st.markdown(
                f"""
                <div class="category-tile">
                    <div class="category-icon">{icon}</div>
                    <div class="category-name">{html.escape(category)}</div>
                    <div class="category-description">{html.escape(description)}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='height:1.1rem'></div>", unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">EXPLORE THE TOOLS</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">What would you like to do?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Choose a tool to get started.</div>',
        unsafe_allow_html=True
    )

    feature_columns = st.columns(3, gap="medium")
    feature_data = [
        (feature_columns[0], "♻️", "Waste Identification",
         "Search for an item and find its category and disposal instructions.",
         "Identification"),
        (feature_columns[1], "🗂️", "Smart Bin Sorting",
         "Browse all waste categories, examples and sorting guidance.",
         "Sorting"),
        (feature_columns[2], "🌱", "Eco-Friendly Tips",
         "Find practical ideas for reducing waste in everyday life.",
         "Tips")
    ]

    for col, icon, title, description, page in feature_data:
        with col:
            with st.container(key=f"feature_{page.lower()}"):
                if st.button(
                    f"{icon}  **{title}**\n\n{description}\n\n**OPEN →**",
                    key=f"open_{page.lower()}",
                    use_container_width=True
                ):
                    navigate(page)
                    st.rerun()


# 8. WASTE IDENTIFICATION
# CONDITIONALS handle blank, recognised and unrecognised input.

elif st.session_state.page == "Identification":

    st.markdown('<div class="eyebrow">RECYCLEIT TOOL</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Waste Identification</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Search for an everyday item to discover its waste category and the right way to dispose it off.</div>',
        unsafe_allow_html=True
    )

    with st.form("identify_form", clear_on_submit=False):
        search_col, button_col = st.columns([5, 1.25], vertical_alignment="bottom")

        with search_col:
            search_item = st.text_input(
                "Waste item",
                placeholder="For example: plastic bottle, newspaper, battery...",
                label_visibility="collapsed"
            )

        with button_col:
            submitted = st.form_submit_button(
                "Identify Item  ♻️",
                type="primary",
                use_container_width=True
            )

    if submitted:
        if not search_item.strip():
            st.warning("Enter an item to identify.")
            st.session_state.last_result = None
        else:
            category = identify_waste(search_item)
            st.session_state.last_item = search_item
            st.session_state.last_result = category if category else "NOT_FOUND"

    if st.session_state.last_result and st.session_state.last_result != "NOT_FOUND":
        show_result(st.session_state.last_item, st.session_state.last_result)

    elif st.session_state.last_result == "NOT_FOUND":
        st.warning(
            "We couldn't recognise that item yet. Try a different name, such as banana peel, chips packet, old phone or glass jar."
        )

    st.markdown('<div class="eyebrow" style="margin-top:2rem">TRY SEARCHING FOR</div>', unsafe_allow_html=True)
    example_items = [
        "Plastic bottle", "Pizza box", "Banana peel",
        "Old phone", "Battery", "Glass jar"
    ]
    example_columns = st.columns(3)
    for index, example in enumerate(example_items):
        with example_columns[index % 3]:
            st.markdown(
                f'<div class="example-chip">{html.escape(example)}</div>',
                unsafe_allow_html=True
            )


# 9. SMART BIN SORTING
# LOOPS display categories; CONDITIONALS update the selected category.

elif st.session_state.page == "Sorting":

    st.markdown('<div class="eyebrow">SORT IT RIGHT</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Smart Bin Sorting</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Choose a waste category to see common examples and practical sorting guidance.</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-title">Select a category</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">All nine categories are available below.</div>',
        unsafe_allow_html=True
    )

    sorting_columns = st.columns(3, gap="small")
    for index, (category, (icon, _)) in enumerate(category_info.items()):
        with sorting_columns[index % 3]:
            is_selected = st.session_state.sorting_category == category
            button_label = f"{icon}  {category}" + ("   ✓" if is_selected else "")
            if st.button(
                button_label,
                key=f"sort_{index}",
                use_container_width=True,
                type="primary" if is_selected else "secondary"
            ):
                st.session_state.sorting_category = category
                st.rerun()

    category = st.session_state.sorting_category
    icon, description = category_info[category]

    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
    detail_col, guidance_col = st.columns([1.05, 1], gap="large")

    with detail_col:
        st.markdown(
            f"""
            <div class="detail-panel">
                <div class="eyebrow">CATEGORY DETAILS</div>
                <div style="font-size:1.5rem;margin-bottom:0.35rem">{icon}</div>
                <div class="section-title">{html.escape(category)}</div>
                <div class="section-subtitle">{html.escape(description)}</div>
                <div class="detail-heading">Common examples</div>
                <div>
                    {''.join(f'<span class="example-chip">{html.escape(item.title())}</span>' for item in waste[category])}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with guidance_col:
        st.markdown(
            f"""
            <div class="detail-panel">
                <div class="detail-heading">♻️ Sorting guidance</div>
                <div class="tip-copy" style="font-size:0.9rem;margin-bottom:1.2rem">
                    {html.escape(bin_guidance[category])}
                </div>
                <div class="detail-heading">How to dispose</div>
                <div class="tip-copy" style="font-size:0.9rem;margin-bottom:1.2rem">
                    {html.escape(disposal[category])}
                </div>
                <div class="detail-heading">A little eco tip</div>
                <div class="tip-copy" style="font-size:0.9rem">
                    {html.escape(tips[category])}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# 10. ECO-FRIENDLY TIPS
# NESTED LOOPS display tips by topic; random.choice selects a random tip.

elif st.session_state.page == "Tips":

    st.markdown('<div class="eyebrow">SMALL STEPS, BIG IMPACT</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Eco-Friendly Tips</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Simple, realistic actions you can build into your everyday routine.</div>',
        unsafe_allow_html=True
    )

    total_tips = sum(len(items) for items in eco_sections.values())
    st.markdown(
        f"""
        <div class="hero-panel" style="padding:1.3rem 1.6rem">
            <div class="hero-kicker">YOUR EVERYDAY ECO GUIDE</div>
            <div class="section-title">{total_tips} practical ways to live a little greener</div>
            <div class="hero-copy">You do not have to change everything at once. Start with one habit and build from there.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for section_index, (section, section_tips) in enumerate(eco_sections.items()):
        st.markdown(
            f'<div class="eyebrow" style="margin-top:1.5rem">0{section_index + 1} / ECO HABITS</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="section-title">{html.escape(section)}</div>',
            unsafe_allow_html=True
        )

        tip_columns = st.columns(2, gap="medium")
        for index, (title, description) in enumerate(section_tips):
            with tip_columns[index % 2]:
                st.markdown(
                    f"""
                    <div class="tip-card">
                        <div class="tip-number">TIP {index + 1:02d}</div>
                        <div class="tip-title">{html.escape(title)}</div>
                        <div class="tip-copy">{html.escape(description)}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown("<div style='height:0.7rem'></div>", unsafe_allow_html=True)
    if st.button("Give Me a Random Eco Tip  🌱", type="primary"):
        all_tips = [
            (title, description)
            for section_tips in eco_sections.values()
            for title, description in section_tips
        ]
        st.session_state.random_tip = random.choice(all_tips)

    if st.session_state.random_tip:
        title, description = st.session_state.random_tip
        st.success(f"{title}: {description}")
