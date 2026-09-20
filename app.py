import streamlit as st

# =========================================================
# PY★STAR — AI ИНФОРМАТИКА ҰСТАЗЫ
# Бірінші нұсқа
# =========================================================

st.set_page_config(
    page_title="PY★STAR — AI Информатика Ұстазы",
    page_icon="⭐",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================

if "starcoin" not in st.session_state:
    st.session_state.starcoin = 0

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "mission_274_done" not in st.session_state:
    st.session_state.mission_274_done = False

# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>
.main {
    background-color: #080b14;
}

.block-container {
    padding-top: 2rem;
}

.game-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 5px;
}

.game-subtitle {
    text-align: center;
    font-size: 18px;
    opacity: 0.8;
    margin-bottom: 30px;
}

.stat-box {
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #30384d;
    background: #111625;
}

.mission-card {
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #30384d;
    background: #101522;
    margin-top: 15px;
}

.mentor {
    padding: 20px;
    border-radius: 18px;
    background: #151b2d;
    border: 1px solid #46506b;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="game-title">⭐ PY★STAR</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="game-subtitle">AI Информатика Ұстазы • Білімді ойын арқылы меңгер</div>',
    unsafe_allow_html=True
)

# =========================================================
# PLAYER
# =========================================================

st.sidebar.header("👤 Ойыншы")

student_name = st.sidebar.text_input(
    "Аты-жөніңіз",
    placeholder="Мысалы: Алияр"
)

grade = st.sidebar.selectbox(
    "Сынып",
    ["7-сынып", "8-сынып", "9-сынып"]
)

st.sidebar.divider()

st.sidebar.markdown("### 🎮 Ойын статистикасы")

level = "STARTER"

if st.session_state.xp >= 3000:
    level = "CODER"
elif st.session_state.xp >= 1500:
    level = "CODE EXPLORER"

st.sidebar.write(f"🏆 Деңгей: **{level}**")
st.sidebar.write(f"⭐ StarCoin: **{st.session_state.starcoin}**")
st.sidebar.write(f"⚡ XP: **{st.session_state.xp}**")

# =========================================================
# TOP STATS
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"""
        <div class="stat-box">
        👤<br>
        <b>{student_name if student_name else "Ойыншы"}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class="stat-box">
        🏆<br>
        <b>{level}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class="stat-box">
        ⭐<br>
        <b>{st.session_state.starcoin} StarCoin</b>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f"""
        <div class="stat-box">
        ⚡<br>
        <b>{st.session_state.xp} XP</b>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# =========================================================
# MISSION MAP
# =========================================================

st.header("🗺️ МИССИЯЛАР КАРТАСЫ")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.success("✅ 273\n\nАяқталды")

with m2:
    st.warning("⭐ 274\n\nҚАУІПСІЗДІК КІЛТІ")

with m3:
    st.info("🔒 275\n\nҚұлыптаулы")

with m4:
    st.info("🔒 276\n\nҚұлыптаулы")

st.divider()

# =========================================================
# MISSION 274
# =========================================================

st.markdown(
    """
    <div class="mission-card">
    <h2>⭐ MISSION 274 — «ҚАУІПСІЗДІК КІЛТІ»</h2>
    <p>🎯 Тақырып: Жеке қауіпсіздік және сервистік программалардың рөлі</p>
    <p>🎮 Мақсат: цифрлық ортада қауіпсіз шешім қабылдау.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# =========================================================
# LEARN
# =========================================================

with st.expander("📖 1-КЕЗЕҢ — ҮЙРЕНУ", expanded=True):

    st.markdown("""
    ### 🔐 Цифрлық қауіпсіздік

    Интернетте жеке мәліметтерді қорғау өте маңызды.

    **Есте сақта:**

    - 🔑 Парольді басқа адамға берме.
    - 🛡️ Антивирус зиянды программаларды анықтауға көмектеседі.
    - 🔥 Firewall желілік қауіптерден қорғауға көмектеседі.
    - ☁️ Бұлттық сервистерде де жеке ақпаратты қорғау қажет.
    - 📁 Бейтаныс файлдарды бірден ашпа.
    """)

# =========================================================
# SELF SOLVE
# =========================================================

st.header("✍️ 2-КЕЗЕҢ — ӨЗІҢ ШЫҒАР")

st.write("Бұл жерде дайын жауапты таңдамайсың. **Өзің жазасың.**")

answer1 = st.text_area(
    "🔐 1-тапсырма. Досың саған: «Пароліңді маған жіберші, ешкімге айтпаймын» деді. Не істейсің?",
    key="mission274_answer1"
)

answer2 = st.text_input(
    "🛡️ 2-тапсырма. Компьютерге бейтаныс файл жүктелді. Қай сервистік программа көмектеседі?",
    key="mission274_answer2"
)

answer3 = st.text_area(
    "🚨 3-тапсырма. Мектеп компьютерінде басқа оқушының аккаунты ашық тұр. Қауіпсіздік үшін қандай 2 әрекет жасайсың?",
    key="mission274_answer3"
)

# =========================================================
# AI MENTOR
# =========================================================

st.header("🤖 3-КЕЗЕҢ — AI MENTOR")

st.markdown(
    """
    <div class="mentor">
    🤖 <b>AI Mentor:</b><br><br>
    Мен сенің орныңа жауап бермеймін.<br>
    Қате болса — <b>қай жерден қате кеткенін түсіндіремін</b>.<br>
    Қайта ойланып, өзің түзетесің.
    </div>
    """,
    unsafe_allow_html=True
)

if st.button("🤖 AI-ға жауаптарымды тексерту", use_container_width=True):

    score = 0

    # Task 1
    a1 = answer1.lower()

    if any(word in a1 for word in [
        "берм", "айтпай", "жіберм", "құпия", "беруге болмайды"
    ]):
        st.success("✅ 1-тапсырма дұрыс бағытта!")
        score += 1
    else:
        st.warning(
            "💡 AI Mentor: Пароль жеке мәліметке жатады. "
            "Оны басқа адамға беруге болмайтынын ойлан."
        )

    # Task 2
    a2 = answer2.lower()

    if "антивирус" in a2:
        st.success("✅ 2-тапсырма дұрыс!")
        score += 1
    else:
        st.warning(
            "💡 AI Mentor: Бейтаныс файл зиянды программа болуы мүмкін. "
            "Компьютерді зиянды программадан қорғайтын құралды есіңе түсір."
        )

    # Task 3
    a3 = answer3.lower()

    security_words = [
        "жаб", "шығ", "logout", "пароль",
        "аккаунт", "құпия", "сақтама"
    ]

    found = sum(word in a3 for word in security_words)

    if found >= 2:
        st.success("✅ 3-тапсырма жақсы орындалды!")
        score += 1
    else:
        st.warning(
            "💡 AI Mentor: кемінде екі қауіпсіздік әрекетін жаз. "
            "Мысалы, ашық аккаунтпен не істеу керек екенін ойлан."
        )

    st.write(f"### Нәтиже: **{score}/3**")

# =========================================================
# MINI TEST
# =========================================================

st.header("📝 4-КЕЗЕҢ — MINI TEST")

q1 = st.radio(
    "1. Күшті парольге қайсысы жатады?",
    [
        "123456",
        "qwerty",
        "Janar2026",
        "A7!kP9#zQ2"
    ],
    key="m274_q1"
)

q2 = st.radio(
    "2. Зиянды программаларды анықтауға көмектесетін құрал:",
    [
        "Антивирус",
        "Калькулятор",
        "Paint",
        "Музыка ойнатқыш"
    ],
    key="m274_q2"
)

q3 = st.radio(
    "3. Парольді кімге беру керек?",
    [
        "Досыма",
        "Бейтаныс адамға",
        "Ешкімге бермеу керек",
        "Интернеттегі кез келген адамға"
    ],
    key="m274_q3"
)

q4 = st.radio(
    "4. Бейтаныс файл келгенде бірінші не істеген дұрыс?",
    [
        "Бірден ашу",
        "Барлығына жіберу",
        "Қауіпсіздігін тексеру",
        "Атын өзгерту"
    ],
    key="m274_q4"
)

q5 = st.radio(
    "5. Firewall не үшін қолданылады?",
    [
        "Сурет салу үшін",
        "Желілік қауіптерден қорғауға көмектесу үшін",
        "Музыка тыңдау үшін",
        "Мәтін теру үшін"
    ],
    key="m274_q5"
)

# =========================================================
# COMPLETE MISSION
# =========================================================

if st.button("🏆 МИССИЯНЫ АЯҚТАУ", use_container_width=True):

    correct = 0

    if q1 == "A7!kP9#zQ2":
        correct += 1

    if q2 == "Антивирус":
        correct += 1

    if q3 == "Ешкімге бермеу керек":
        correct += 1

    if q4 == "Қауіпсіздігін тексеру":
        correct += 1

    if q5 == "Желілік қауіптерден қорғауға көмектесу үшін":
        correct += 1

    percent = correct * 20

    st.write(f"## 🎯 Нәтиже: {correct}/5 — {percent}%")

    if correct >= 4:

        if not st.session_state.mission_274_done:

            st.session_state.starcoin += 200
            st.session_state.xp += 300
            st.session_state.mission_274_done = True

        st.success("🎉 MISSION 274 АЯҚТАЛДЫ!")

        st.balloons()

        st.markdown("""
        ### 🎁 Сыйақы

        ⭐ **+200 StarCoin**

        ⚡ **+300 XP**

        🔓 **MISSION 275 ашылды!**
        """)

    else:

        st.warning(
            "💡 Миссия әлі толық аяқталған жоқ. "
            "Қателеріңді қарап, тестті қайта орында."
        )

# =========================================================
# NEXT MISSION
# =========================================================

if st.session_state.mission_274_done:

    st.divider()

    st.success(
        "🔓 MISSION 275 ашылды! Келесі миссияда "
        "«Ақпараттың өлшем бірліктері» тақырыбына өтесің."
    )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "⭐ PY★STAR | AI Информатика Ұстазы | "
    "Білім + Ойын + AI Mentor"
)
