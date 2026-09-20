import streamlit as st

# =========================================================
# ⭐ PY★STAR — AI ИНФОРМАТИКА ҰСТАЗЫ
# =========================================================

st.set_page_config(
    page_title="PY★STAR — AI Информатика Ұстазы",
    page_icon="⭐",
    layout="wide"
)

# =========================================================
# ОЙЫН ДЕРЕКТЕРІ
# =========================================================

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "grade" not in st.session_state:
    st.session_state.grade = "7-сынып"

if "starcoin" not in st.session_state:
    st.session_state.starcoin = 0

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "mission_274_done" not in st.session_state:
    st.session_state.mission_274_done = False

# =========================================================
# ДИЗАЙН
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #070b16, #10182b, #080b14);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.hero {
    text-align: center;
    padding: 55px 20px;
}

.logo {
    font-size: 64px;
    font-weight: 900;
    letter-spacing: 4px;
}

.subtitle {
    font-size: 21px;
    margin-top: 10px;
    opacity: 0.85;
}

.welcome {
    text-align: center;
    font-size: 30px;
    font-weight: 800;
    margin-top: 25px;
}

.player-card {
    padding: 22px;
    border-radius: 20px;
    background: rgba(20, 28, 48, 0.9);
    border: 1px solid #3c4968;
    text-align: center;
    margin-bottom: 20px;
}

.mission {
    padding: 28px;
    border-radius: 22px;
    background: rgba(15, 23, 42, 0.95);
    border: 1px solid #52617f;
    margin-top: 20px;
}

.stat {
    padding: 18px;
    border-radius: 16px;
    background: rgba(18, 25, 43, 0.95);
    border: 1px solid #394763;
    text-align: center;
}

.big-button {
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

.mentor {
    padding: 20px;
    border-radius: 18px;
    background: rgba(28, 37, 63, 0.95);
    border: 1px solid #5b6988;
}

.locked {
    padding: 20px;
    border-radius: 18px;
    background: rgba(30, 35, 48, 0.8);
    border: 1px solid #343b4d;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 1. КІРІСПЕ ЭКРАН
# =========================================================

if not st.session_state.game_started:

    st.markdown("""
    <div class="hero">

    <div class="logo">⭐ PY★STAR</div>

    <div class="subtitle">
    AI Информатика Ұстазы
    </div>

    <br>

    <div class="welcome">
    🚀 Қош келдің, болашақ CODE MASTER!
    </div>

    <p style="font-size:18px;">
    Білімді жина • Миссияларды орында • StarCoin тап • Деңгейіңді көтер!
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown("### 👤 Ойыншы профилі")

        name = st.text_input(
            "Аты-жөнің",
            placeholder="Мысалы: Аян"
        )

        grade = st.selectbox(
            "Сыныбыңды таңда",
            ["7-сынып", "8-сынып", "9-сынып"]
        )

        st.write("")

        if st.button(
            "🎮 ОЙЫНДЫ БАСТАУ",
            use_container_width=True
        ):

            if name.strip() == "":
                st.warning("⚠️ Алдымен аты-жөніңді енгіз!")
            else:

                st.session_state.student_name = name
                st.session_state.grade = grade
                st.session_state.game_started = True

                st.rerun()

    st.divider()

    st.markdown(
        """
        <div style="text-align:center; opacity:0.7;">
        🎯 7–9 сынып • 💻 Информатика • 🤖 AI Mentor • ⭐ StarCoin
        </div>
        """,
        unsafe_allow_html=True
    )

    st.stop()

# =========================================================
# 2. НЕГІЗГІ ОЙЫН ЭКРАНЫ
# =========================================================

name = st.session_state.student_name
grade = st.session_state.grade

st.markdown(
    f"""
    <div class="player-card">
    <div style="font-size:32px;">⭐ PY★STAR</div>
    <div style="font-size:22px;">
    Қош келдің, <b>{name}</b>!
    </div>
    <div style="opacity:0.8;">
    🎓 {grade} • 🚀 Ойын басталды!
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# СТАТИСТИКА
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="stat">
        🏆<br>
        <b>STARTER</b><br>
        Деңгей
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class="stat">
        ⭐<br>
        <b>{st.session_state.starcoin}</b><br>
        StarCoin
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class="stat">
        ⚡<br>
        <b>{st.session_state.xp}</b><br>
        XP
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="stat">
        🗺️<br>
        <b>274</b><br>
        Миссия
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# =========================================================
# МИССИЯ КАРТАСЫ
# =========================================================

st.header("🗺️ МИССИЯЛАР КАРТАСЫ")

st.write(
    "273 миссия — алдыңғы кезең. "
    "Енді жаңа PY★STAR жүйесі **274-миссиядан** басталады."
)

m1, m2, m3 = st.columns(3)

with m1:
    st.success("""
    👑

    **273**

    АЛДЫҢҒЫ КЕЗЕҢ
    """)

with m2:
    if st.session_state.mission_274_done:
        st.success("""
        ✅

        **274**

        АЯҚТАЛДЫ
        """)
    else:
        st.warning("""
        ⭐

        **274**

        ҚАУІПСІЗДІК КІЛТІ
        """)

with m3:
    st.markdown(
        """
        <div class="locked">
        🔒<br><br>
        <b>275</b><br>
        Құлыптаулы
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# =========================================================
# 274 МИССИЯ
# =========================================================

st.header("⭐ MISSION 274")

st.markdown(
    """
    <div class="mission">

    <h2>🔐 ҚАУІПСІЗДІК КІЛТІ</h2>

    <p>
    🎯 <b>Тақырып:</b>
    Жеке қауіпсіздік және сервистік программалардың рөлі
    </p>

    <p>
    🚀 <b>Миссия мақсаты:</b>
    Цифрлық ортада қауіпсіз шешім қабылдау.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# =========================================================
# ҮЙРЕНУ
# =========================================================

with st.expander("📖 1-КЕЗЕҢ — ҮЙРЕНУ", expanded=True):

    st.markdown("""
    ### 🔐 Қауіпсіздік ережелері

    🔑 Парольді басқа адамға берме.

    🛡️ Антивирус зиянды программаларды анықтауға көмектеседі.

    🔥 Firewall желілік қауіптерден қорғауға көмектеседі.

    📁 Бейтаныс файлды бірден ашпа.

    ☁️ Жеке ақпаратты интернетте абайлап қолдан.
    """)

# =========================================================
# ӨЗІҢ ШЫҒАР
# =========================================================

st.header("✍️ 2-КЕЗЕҢ — ӨЗІҢ ШЫҒАР")

st.info(
    "Бұл жерде дайын жауап таңдамайсың. "
    "Жауапты өзің жазасың."
)

a1 = st.text_area(
    "🔐 1. Досың сенен пароль сұрады. Не істейсің?",
    key="m274_a1"
)

a2 = st.text_input(
    "🛡️ 2. Бейтаныс файл компьютерге жүктелді. "
    "Қай программа көмектеседі?",
    key="m274_a2"
)

a3 = st.text_area(
    "🚨 3. Басқа оқушының аккаунты мектеп компьютерінде ашық тұр. "
    "Қауіпсіздік үшін 2 әрекет жаз.",
    key="m274_a3"
)

# =========================================================
# AI MENTOR
# =========================================================

st.header("🤖 3-КЕЗЕҢ — AI MENTOR")

st.markdown(
    """
    <div class="mentor">

    🤖 <b>AI Mentor:</b>

    <br><br>

    Мен сенің орныңа жауап бермеймін.

    <br>

    Егер қате болса — саған <b>кеңес беремін</b>.

    <br>

    Қайта ойланып, өзің түзетесің. 💡

    </div>
    """,
    unsafe_allow_html=True
)

if st.button(
    "🤖 ЖАУАПТАРЫМДЫ ТЕКСЕР",
    use_container_width=True
):

    score = 0

    # 1
    text1 = a1.lower()

    if any(x in text1 for x in [
        "берм", "айтпай", "жіберм", "құпия"
    ]):
        st.success("✅ 1-тапсырма: дұрыс бағыт!")
        score += 1
    else:
        st.warning(
            "💡 Кеңес: пароль — жеке құпия ақпарат. "
            "Оны басқа адамға беру қауіпсіз бе?"
        )

    # 2
    text2 = a2.lower()

    if "антивирус" in text2:
        st.success("✅ 2-тапсырма: дұрыс!")
        score += 1
    else:
        st.warning(
            "💡 Кеңес: компьютерді зиянды программалардан "
            "қорғайтын құралды есіңе түсір."
        )

    # 3
    text3 = a3.lower()

    keywords = [
        "жаб", "шығ", "logout",
        "аккаунт", "құпия", "пароль"
    ]

    found = sum(x in text3 for x in keywords)

    if found >= 2:
        st.success("✅ 3-тапсырма: жақсы!")
        score += 1
    else:
        st.warning(
            "💡 Кеңес: ашық тұрған аккаунтпен не істеу "
            "керек екенін және жеке ақпаратты қалай қорғауға "
            "болатынын ойлан."
        )

    st.write(f"### 🎯 Өзің шығарған тапсырмалар: {score}/3")

# =========================================================
# MINI TEST
# =========================================================

st.header("📝 4-КЕЗЕҢ — MINI TEST")

q1 = st.radio(
    "1. Күшті парольді таңда:",
    [
        "123456",
        "qwerty",
        "password",
        "A7!kP9#zQ2"
    ],
    key="q274_1"
)

q2 = st.radio(
    "2. Зиянды программаларды анықтауға көмектеседі:",
    [
        "Калькулятор",
        "Антивирус",
        "Paint",
        "Музыка ойнатқыш"
    ],
    key="q274_2"
)

q3 = st.radio(
    "3. Парольді:",
    [
        "Досыма беремін",
        "Бейтаныс адамға беремін",
        "Ешкімге бермеймін",
        "Әлеуметтік желіге жазамын"
    ],
    key="q274_3"
)

q4 = st.radio(
    "4. Бейтаныс файл келгенде:",
    [
        "Бірден ашамын",
        "Басқаларға жіберемін",
        "Қауіпсіздігін тексеремін",
        "Барлығын өшіремін"
    ],
    key="q274_4"
)

q5 = st.radio(
    "5. Firewall не үшін қажет?",
    [
        "Сурет салу үшін",
        "Желілік қауіптерден қорғауға көмектесу үшін",
        "Музыка тыңдау үшін",
        "Мәтін теру үшін"
    ],
    key="q274_5"
)

# =========================================================
# МИССИЯНЫ АЯҚТАУ
# =========================================================

if st.button(
    "🏆 МИССИЯНЫ АЯҚТАУ",
    use_container_width=True
):

    correct = 0

    if q1 == "A7!kP9#zQ2":
        correct += 1

    if q2 == "Антивирус":
        correct += 1

    if q3 == "Ешкімге бермеймін":
        correct += 1

    if q4 == "Қауіпсіздігін тексеремін":
        correct += 1

    if q5 == "Желілік қауіптерден қорғауға көмектесу үшін":
        correct += 1

    percent = correct * 20

    st.write(
        f"## 🎯 Нәтиже: {correct}/5 — {percent}%"
    )

    if correct >= 4:

        if not st.session_state.mission_274_done:

            st.session_state.starcoin += 200
            st.session_state.xp += 300

            st.session_state.mission_274_done = True

        st.success("🎉 MISSION 274 АЯҚТАЛДЫ!")

        st.balloons()

        st.markdown("""
        ### 🎁 СЫЙАҚЫ

        ⭐ **+200 StarCoin**

        ⚡ **+300 XP**

        🔓 **MISSION 275 АШЫЛДЫ!**
        """)

    else:

        st.warning(
            "💡 4 немесе 5 дұрыс жауап қажет. "
            "Қателеріңді қарап, қайта орында."
        )

# =========================================================
# 275
# =========================================================

if st.session_state.mission_274_done:

    st.divider()

    st.success(
        "🔓 MISSION 275 — «АҚПАРАТ ӨЛШЕМІ» ашылды!"
    )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "⭐ PY★STAR | AI Информатика Ұстазы | "
    "Білім • Ойын • AI Mentor"
)
