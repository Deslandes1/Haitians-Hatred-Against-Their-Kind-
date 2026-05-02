import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Haitians Hatred Against Their Kind – written by Gesner Deslandes",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- LANGUAGE STATE ----------
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# ---------- UI TRANSLATIONS ----------
ui_text = {
    "en": {
        "app_title": "📘 Haitians Hatred Against Their Kind – written by Gesner Deslandes",
        "app_sub": "A raw exploration of envy, betrayal, and the struggle to rise",
        "sidebar_company": "🌐 GlobalInternet.py",
        "sidebar_founder": "👨‍💻 Gesner Deslandes – Author & Python Builder",
        "sidebar_phone": "📞 (509) 4738-5663",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_website": "🌍 Visit our website",
        "sidebar_book_title": "📖 Haitians Hatred Against Their Kind",
        "sidebar_book_author": "written by Gesner Deslandes",
        "sidebar_book_desc": "A powerful book about the hidden beast within",
        "sidebar_price": "💰 Price: $19.99 USD (e-book) | $29.99 USD (paperback + source code)",
        "sidebar_caption": "Built by Gesner Deslandes – GlobalInternet.py",
        "chapter_selector": "📖 Select Chapter",
        "read_aloud_button": "🔊 Read Aloud",
        "reading_indicator": "🔊 Now reading... (audio playing)",
        "reading_success": "🔊 Now reading aloud... (make sure your device volume is on)",
        "footer_copyright": "GlobalInternet.py – Storytelling by Gesner Deslandes",
        "footer_book": "📖 \"Haitians Hatred Against Their Kind\" – written by Gesner Deslandes",
        "footer_built": "🌐 Built with Streamlit | Hosted on GitHub + Streamlit Cloud",
        "language_selector": "🌐 Language",
    },
    "fr": {
        "app_title": "📘 La Haine des Haïtiens Envers Leur Prochain – écrit par Gesner Deslandes",
        "app_sub": "Une exploration brute de l'envie, de la trahison et de la lutte pour s'élever",
        "sidebar_company": "🌐 GlobalInternet.py",
        "sidebar_founder": "👨‍💻 Gesner Deslandes – Auteur & Constructeur Python",
        "sidebar_phone": "📞 (509) 4738-5663",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_website": "🌍 Visitez notre site web",
        "sidebar_book_title": "📖 La Haine des Haïtiens Envers Leur Prochain",
        "sidebar_book_author": "écrit par Gesner Deslandes",
        "sidebar_book_desc": "Un livre puissant sur la bête cachée à l'intérieur",
        "sidebar_price": "💰 Prix : 19,99 $US (livre numérique) | 29,99 $US (papier + code source)",
        "sidebar_caption": "Construit par Gesner Deslandes – GlobalInternet.py",
        "chapter_selector": "📖 Choisir le chapitre",
        "read_aloud_button": "🔊 Lire à voix haute",
        "reading_indicator": "🔊 Lecture en cours... (audio en cours)",
        "reading_success": "🔊 Lecture en cours... (vérifiez le volume de votre appareil)",
        "footer_copyright": "GlobalInternet.py – Contes par Gesner Deslandes",
        "footer_book": "📖 \"La Haine des Haïtiens Envers Leur Prochain\" – écrit par Gesner Deslandes",
        "footer_built": "🌐 Construit avec Streamlit | Hébergé sur GitHub + Streamlit Cloud",
        "language_selector": "🌐 Langue",
    },
    "es": {
        "app_title": "📘 El Odio de los Haitianos Hacia su Propia Gente – escrito por Gesner Deslandes",
        "app_sub": "Una exploración cruda de la envidia, la traición y la lucha por surgir",
        "sidebar_company": "🌐 GlobalInternet.py",
        "sidebar_founder": "👨‍💻 Gesner Deslandes – Autor & Constructor Python",
        "sidebar_phone": "📞 (509) 4738-5663",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_website": "🌍 Visite nuestro sitio web",
        "sidebar_book_title": "📖 El Odio de los Haitianos Hacia su Propia Gente",
        "sidebar_book_author": "escrito por Gesner Deslandes",
        "sidebar_book_desc": "Un libro poderoso sobre la bestia oculta dentro",
        "sidebar_price": "💰 Precio: $19.99 USD (libro electrónico) | $29.99 USD (papel + código fuente)",
        "sidebar_caption": "Construido por Gesner Deslandes – GlobalInternet.py",
        "chapter_selector": "📖 Seleccionar capítulo",
        "read_aloud_button": "🔊 Leer en voz alta",
        "reading_indicator": "🔊 Leyendo ahora... (audio en curso)",
        "reading_success": "🔊 Leyendo en voz alta... (asegúrese de que el volumen de su dispositivo esté activado)",
        "footer_copyright": "GlobalInternet.py – Narración por Gesner Deslandes",
        "footer_book": "📖 \"El Odio de los Haitianos Hacia su Propia Gente\" – escrito por Gesner Deslandes",
        "footer_built": "🌐 Construido con Streamlit | Alojado en GitHub + Streamlit Cloud",
        "language_selector": "🌐 Idioma",
    }
}

def _(key):
    return ui_text[st.session_state.lang].get(key, key)

# ---------- BEAST IMAGE FOR CHAPTER 1 (from GitHub) ----------
beast_image_url = "https://raw.githubusercontent.com/Deslandes1/Haitians-Hatred-Against-Their-Kind-/main/33382.jpg"

# ---------- CHAPTERS DATA (ENGLISH) ----------
chapters_en = [
    {
        "title": "Chapter 1: The Translator Who Never Flew",
        "image": beast_image_url,
        "text": "This is the story about a Haitian translator who missed several opportunities to legally travel to the United States of America. Haitian families have this tendency to hate you and pray that you never find an opportunity like that, to travel to the United States of America. In every Haitian you will find this demon of hatred to another Haitian fellow – naturally hating you if they suspect you want to travel to the United States. When I check AI and my own logic as a human being, they all resonated the same thing: if I cannot make it, I don't want you to make it. If you finally make it, and I couldn't kill you in the process, you will be considered as victorious and respectable. That's the beast.",
        "caption": "A dark beast – symbol of the hidden hatred within"
    }
]

# ---------- FRENCH CHAPTER ----------
chapters_fr = [
    {
        "title": "Chapitre 1 : Le traducteur qui n'a jamais volé",
        "image": beast_image_url,
        "text": "Voici l'histoire d'un traducteur haïtien qui a manqué plusieurs occasions de se rendre légalement aux États‑Unis d'Amérique. Les familles haïtiennes ont cette tendance à vous haïr et à prier pour que vous ne trouviez jamais une telle opportunité. Chez chaque Haïtien, vous trouverez ce démon de la haine envers un autre Haïtien – vous haïr naturellement s'ils soupçonnent que vous voulez voyager vers les États‑Unis. Quand je consulte l'IA et ma propre logique d'être humain, elles résonnent toutes de la même manière : si je n'y arrive pas, je ne veux pas que tu y arrives. Si finalement tu y arrives, et que je n'ai pas pu te tuer en cours de route, tu seras considéré comme victorieux et respectable. Voilà la bête.",
        "caption": "Une bête sombre – symbole de la haine cachée à l'intérieur"
    }
]

# ---------- SPANISH CHAPTER ----------
chapters_es = [
    {
        "title": "Capítulo 1: El traductor que nunca voló",
        "image": beast_image_url,
        "text": "Esta es la historia de un traductor haitiano que perdió varias oportunidades de viajar legalmente a los Estados Unidos de América. Las familias haitianas tienen esta tendencia a odiarte y rezar para que nunca encuentres una oportunidad así. En cada haitiano encontrarás este demonio de odio hacia otro haitiano – odiarte naturalmente si sospechan que quieres viajar a los Estados Unidos. Cuando consulto a la IA y mi propia lógica como ser humano, todas resuenan lo mismo: si yo no puedo lograrlo, no quiero que tú lo logres. Si finalmente lo logras, y no pude matarte en el proceso, serás considerado victorioso y respetable. Esa es la bestia.",
        "caption": "Una bestia oscura – símbolo del odio escondido dentro"
    }
]

# ---------- MAP LANGUAGE TO CHAPTERS ----------
language_map = {
    "en": chapters_en,
    "fr": chapters_fr,
    "es": chapters_es
}

# ---------- CUSTOM CSS (BLUE THEME) ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #e6f0ff 0%, #cce4ff 100%);
    }
    .main-header {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .lesson-card {
        background-color: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.2s;
        border-left: 5px solid #2a5298;
    }
    .lesson-card:hover { transform: translateY(-5px); }
    .story-text {
        font-family: 'Georgia', serif;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #1e2a3e;
        text-align: justify;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background-color: #d4e4ff;
        border-radius: 20px;
        color: #1e3c72;
    }
    .sidebar-logo {
        text-align: center;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .pulse-dot {
        display: inline-block;
        width: 12px;
        height: 12px;
        background-color: #ff4444;
        border-radius: 50%;
        animation: pulse 1.2s infinite;
        margin-right: 8px;
        vertical-align: middle;
    }
    @keyframes pulse {
        0% { transform: scale(0.8); opacity: 0.5; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(0.8); opacity: 0.5; }
    }
    .reading-indicator {
        display: inline-flex;
        align-items: center;
        background: #f0f0f0;
        padding: 5px 12px;
        border-radius: 30px;
        font-size: 0.8rem;
        margin-top: 10px;
    }
    h1, h2, h3 {
        color: #1e3c72;
    }
    .stButton button {
        background-color: #2a5298;
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #1e3c72;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# ---------- LANGUAGE SELECTOR IN SIDEBAR ----------
lang_options = {
    "English": "en",
    "Français": "fr",
    "Español": "es"
}
selected_lang_name = st.sidebar.selectbox(
    _("language_selector"),
    list(lang_options.keys()),
    index=["en","fr","es"].index(st.session_state.lang)
)
st.session_state.lang = lang_options[selected_lang_name]
chapters = language_map[st.session_state.lang]

# ---------- SIDEBAR CONTENT (with author and price) ----------
with st.sidebar:
    st.markdown(f'<div class="sidebar-logo">📘</div>', unsafe_allow_html=True)
    st.markdown(f"## {_('sidebar_company')}")
    st.markdown(f"**{_('sidebar_founder')}**")
    st.markdown(_("sidebar_phone"))
    st.markdown(_("sidebar_email"))
    st.markdown("---")
    st.markdown(f"[{_('sidebar_website')}](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown(f"### {_('sidebar_book_title')}")
    st.markdown(f"*{_('sidebar_book_author')}*")
    st.markdown(_("sidebar_book_desc"))
    st.markdown(f"**{_('sidebar_price')}**")
    st.markdown("---")
    st.caption(_("sidebar_caption"))

# ---------- MAIN PAGE ----------
def main():
    st.markdown(
        f"""
        <div class="main-header">
            <h1>{_("app_title")}</h1>
            <p>{_("app_sub")}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    chapter_titles = [f"{i+1}. {ch['title']}" for i, ch in enumerate(chapters)]
    selected_idx = st.sidebar.selectbox(_("chapter_selector"), range(len(chapters)), format_func=lambda i: chapter_titles[i])
    
    chapter = chapters[selected_idx]
    
    with st.container():
        st.markdown(f'<div class="lesson-card">', unsafe_allow_html=True)
        col_img, col_text = st.columns([1, 2])
        with col_img:
            st.image(chapter['image'], caption=chapter.get('caption', 'Illustration'), use_container_width=True)
        with col_text:
            st.markdown(f"## {chapter['title']}")
            st.markdown(f'<div class="story-text">{chapter["text"]}</div>', unsafe_allow_html=True)
            
            read_btn = st.button(f"{_('read_aloud_button')} ({selected_idx+1})", key=f"read_{selected_idx}")
            if read_btn:
                indicator = st.empty()
                indicator.markdown(
                    f'<div class="reading-indicator"><span class="pulse-dot"></span> {_("reading_indicator")}</div>',
                    unsafe_allow_html=True
                )
                text_to_speak = chapter["text"].replace('"', '\\"').replace("\n", " ").replace("'", "\\'")
                lang_code = {"en": "en-US", "fr": "fr-FR", "es": "es-ES"}[st.session_state.lang]
                js_code = f"""
                <script>
                    var utterance = new SpeechSynthesisUtterance("{text_to_speak}");
                    utterance.lang = "{lang_code}";
                    utterance.onend = function() {{
                        var event = new CustomEvent('streamlit:setComponentValue', {{detail: {{value: "done"}}}});
                        window.dispatchEvent(event);
                    }};
                    window.speechSynthesis.cancel();
                    window.speechSynthesis.speak(utterance);
                </script>
                """
                components.html(js_code, height=0)
                st.success(_("reading_success"))
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown(f"""
    <div class="footer">
        <p>© {datetime.now().year} {_('footer_copyright')}</p>
        <p>{_('footer_book')}</p>
        <p>{_('footer_built')}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
