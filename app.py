import streamlit as st
from PIL import Image
import base64

# Configurações da página
st.set_page_config(
    page_title="SF Locação de Veículos",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização personalizada avançada
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #001f3f;
        color: #ffffff;
    }
    
    [data-testid="stSidebar"] {
        display: none;
    }

    h1, h2, h3 {
        color: #FFD700 !important;
        font-weight: 700;
    }

    /* Hero Section */
    .hero-container {
        background: linear-gradient(rgba(0, 31, 63, 0.7), rgba(0, 31, 63, 0.7)), 
                    url('https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-position: center;
        padding: 80px 50px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 50px;
        border: 1px solid rgba(255, 215, 0, 0.3);
    }

    /* Cards com Efeito Hover */
    .modern-card {
        background-color: #002d5a;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid rgba(255, 215, 0, 0.1);
        transition: all 0.3s ease;
        height: 100%;
        text-align: center;
    }
    .modern-card:hover {
        transform: translateY(-10px);
        border-color: #FFD700;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }

    /* Botões Modernos */
    .stButton>button {
        background: linear-gradient(45deg, #FFD700, #FFC800);
        color: #001f3f;
        border-radius: 30px;
        font-weight: bold;
        border: none;
        padding: 8px 20px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        width: auto !important;
        min-width: 120px;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(255, 215, 0, 0.4);
    }
    
    /* Estilo específico para o menu superior para evitar quebras */
    .nav-button-container {
        display: flex;
        justify-content: flex-start;
        gap: 10px;
    }

    .testimonial-card {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        font-style: italic;
        border-left: 4px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MENU SUPERIOR ---
# Layout de colunas ajustado para aproximar o menu do logo e entre si
m_col1, m_col2, m_col3, m_col4, m_col5 = st.columns([1.5, 0.6, 0.8, 0.6, 3])

with m_col1:
    try:
        logo = Image.open("logo_transparent.png")
        st.image(logo, width=140)
    except:
        st.markdown("<h2 style='color:#FFD700; margin:0;'>SF Locação</h2>", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = "Início"

with m_col2:
    if st.button("Início", key="nav_home"): st.session_state.page = "Início"
with m_col3:
    if st.button("Quem Somos", key="nav_about"): st.session_state.page = "Quem Somos"
with m_col4:
    if st.button("Contato", key="nav_contact"): st.session_state.page = "Contato"

st.markdown("---")

# --- CONTEÚDO ---
page = st.session_state.page

if page == "Início":
    st.markdown("""
        <div class="hero-container">
            <h1 style='font-size: 3rem; margin-bottom: 10px;'>SF LOCAÇÃO DE VEÍCULOS</h1>
            <p style='font-size: 1.3rem; color: #FFD700;'>Mobilidade que te leva mais longe.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Por que escolher a SF Locação?")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
            <div class="modern-card">
                <h2 style='font-size: 2.5rem;'>🛡️</h2>
                <h3>Segurança Total</h3>
                <p>Manutenção preventiva rigorosa para sua tranquilidade em cada quilômetro.</p>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
            <div class="modern-card">
                <h2 style='font-size: 2.5rem;'>⚡</h2>
                <h3>Agilidade Digital</h3>
                <p>Processo 100% online e sem burocracia. Saia dirigindo no mesmo dia.</p>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
            <div class="modern-card">
                <h2 style='font-size: 2.5rem;'>📅</h2>
                <h3>Flexibilidade</h3>
                <p>Planos que se moldam ao seu bolso, com opções semanais e mensais.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### Nossos Planos Exclusivos")

  # Construindo a tabela via HTML string
   tabela_html = """
    <table style="width:100%; border-collapse: collapse;">
     <tr style="background-color: #333; color: white;">
    <th>Categoria</th><th>Semanal</th><th>Calção</th>
    </tr>
    <tr>
    <td>Compacto Econômico</td><td>R$ 700,00</td><td>R$ 1.700,00</td>
    </tr>
     <!-- LINHA EM BRANCO (Fundo Branco e Texto Branco) -->
    <tr style="background-color: white; color: white; height: 30px;">
    <td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>
     </tr>
    <tr>
    <td>Sedan Intermediário</td><td>R$ 599,00</td><td>R$ 2.000,00</td>
    </tr>
   </table> """

# Renderiza o HTML no Streamlit
st.markdown(tabela_html, unsafe_allow_html=True)
    
    planos_data = {
        #"Categoria": ["Compacto Econômico", "Sedan Intermediário", "Premium Executivo"],
        #"Semanal": ["R$ 700,00", "R$ 599,00", "R$ 799,00"],
        #"Mensal": ["R$ 1.890,00", "R$ 2.290,00", "R$ 2.990,00"],
        #"KMs Inclusos": ["2.000 km/mês", "2.500 km/mês", "3.000 km/mês"]
        "Categoria": ["Compacto Econômico"],
        "Semanal": ["R$ 700,00"],
        "Calção": ["R$ 1.700,00"]
    }
    st.table(planos_data)
    
    col_cta_left, col_cta_center, col_cta_right = st.columns([1, 2, 1])
    with col_cta_center:
        if st.button("Quero Reservar Agora!", key="cta_main"):
            st.balloons()
            st.info("📲 Chamando consultor no WhatsApp (16) 98115-5809...")

    st.markdown("O que dizem nossos parceiros")
    dep1, dep2 = st.columns(2)
    with dep1:
        st.markdown("""
            <div class="testimonial-card">
                "Alugar na SF foi a melhor decisão que tomei. O carro nunca me deixou na mão e o suporte é sensacional. Recomendo para todos!"<br>
                <strong>— Anderson, Motorista Uber 5 Estrelas</strong>
            </div>
        """, unsafe_allow_html=True)
    with dep2:
        st.markdown("""
            <div class="testimonial-card">
                "Processo muito rápido e transparente. O carro estava impecável na entrega. Ótimo custo-benefício para quem trabalha com app."<br>
                <strong>— Bil, Motorista Uber</strong>
            </div>
        """, unsafe_allow_html=True)

elif page == "Quem Somos":
    st.title("Nossa História")
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        #st.image("https://images.unsplash.com/photo-1560179707-f14e90ef3623?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60", use_container_width=True)
        st.image("https://img.magnific.com/premium-photo/aerial-view-ribeirao-preto-city-sao-paulo-state-with-skyline-sunset_88235-2505.jpg", use_container_width=True)
    with col_txt:
        st.markdown("""
        ### Transformando a Mobilidade em Ribeirão Preto
        Nascemos com o propósito de transformar a forma como as pessoas se movem. Com raízes fortes no interior paulista, a **SF Locação** é mais que uma locadora; somos parceiros de quem faz a cidade girar.
        """)

    st.markdown("---")
    st.markdown("### Perguntas Frequentes")
    with st.expander("Quais documentos são necessários?"):
        st.write("Você precisa apenas da sua CNH válida e um comprovante de residência atualizado.")
    with st.expander("Como funciona a manutenção do veículo?"):
        st.write("A manutenção preventiva e corretiva é totalmente por nossa conta.")

elif page == "Contato":
    st.title("Vamos Conversar?")
    c_info, c_form = st.columns(2)
    with c_info:
        st.markdown("""
            <div class="modern-card" style="text-align: left;">
                <h3>📍 Onde estamos</h3>
                <p>Ribeirão Preto - SP</p>
                <h3>📞 Contato Direto</h3>
                <p>WhatsApp: (16) 98115-5809</p>
            </div>
        """, unsafe_allow_html=True)
    with c_form:
        st.markdown("### Envie sua dúvida")
        st.text_input("Nome Completo")
        st.text_input("E-mail")
        st.text_area("Sua Mensagem")
        st.button("Enviar Agora")

st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<center>© 2026 SF Locação de Veículos | Ribeirão Preto - SP | <span style='color:#FFD700;'>Mobilidade que te leva mais longe.</span></center>", unsafe_allow_html=True)
