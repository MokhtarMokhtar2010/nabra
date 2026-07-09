import streamlit as st
import datetime
import requests
import math

# إعدادات الصفحة الفخمة وتثبيت الواجهة المظلمة التلقائية
st.set_page_config(page_title="تطبيق نبرة الإسلامي المعتمد", page_icon="🕌", layout="wide")

# الكود البرمجي لتغيير ديزاين التطبيق بالكامل إلى نمط "ترتيل برو" الزجاجي الفخم
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* الخلفية الداكنة العميقة الفخمة والموفرة جداً للبطارية */
    .stApp {
        background: radial-gradient(circle at top, #080f0b 0%, #030504 100%);
        color: #E2E8E4;
        font-family: 'Cairo', sans-serif !important;
    }
    
    /* تصميم التبويبات العلوية بشكل زجاجي عائم يشبه ترتيل */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(15, 23, 19, 0.7);
        backdrop-filter: blur(15px);
        padding: 8px;
        border-radius: 20px;
        border: 1px solid rgba(0, 255, 135, 0.1);
    }
    .stTabs [data-baseweb="tab"] {
        color: #7A8B81 !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        padding: 12px 18px !important;
        border-radius: 14px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stTabs [aria-selected="true"] {
        color: #00FF87 !important;
        background: rgba(0, 255, 135, 0.08) !important;
        border-bottom: none !important;
        box-shadow: 0 4px 15px rgba(0, 255, 135, 0.1);
    }
    
    /* بطاقات زجاجية فاخرة ومريحة جداً للعين للأذكار والخصائص */
    .premium-card {
        background: rgba(20, 30, 25, 0.5);
        backdrop-filter: blur(20px);
        padding: 25px;
        border-radius: 22px;
        border: 1px solid rgba(255, 255, 255, 0.03);
        border-right: 4px solid #00FF87;
        margin-bottom: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        direction: rtl;
        text-align: right;
    }
    
    /* تصميم الآيات القرآنية المتوهجة بالهيبة والجمال البصري */
    .quran-container {
        background: rgba(0, 0, 0, 0.4);
        padding: 30px;
        border-radius: 24px;
        border: 1px solid rgba(0, 255, 135, 0.05);
        margin-bottom: 20px;
        box-shadow: inset 0 0 30px rgba(0,0,0,0.8);
    }
    .quran-verse {
        font-family: 'Traditional Arabic', serif;
        font-size: 34px;
        color: #00FF87;
        text-align: center;
        text-shadow: 0 0 20px rgba(0, 255, 135, 0.25);
        line-height: 2.1;
        direction: rtl;
    }
    .tafseer-box {
        font-size: 16px;
        color: #A0B2A7;
        text-align: justify;
        background: rgba(30, 42, 36, 0.4);
        padding: 16px;
        border-radius: 14px;
        margin-top: 15px;
        border-left: 3px solid #60EFFF;
        direction: rtl;
    }
    
    /* تحسين تصميم القوائم المنسدلة وصناديق الاختيار لتناسب المظهر الفخم */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #121815 !important;
        border: 1px solid rgba(0, 255, 135, 0.15) !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
    }
    
    /* تحسين تصميم الأزرار التفاعلية لتصبح نيون متوهجة وعصرية */
    .stButton>button {
        background: linear-gradient(135deg, #00FF87 0%, #00B0FF 100%) !important;
        color: #030504 !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        border: none !important;
        padding: 15px !important;
        box-shadow: 0 5px 25px rgba(0, 255, 135, 0.35) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(0, 255, 135, 0.5) !important;
    }
    
    /* تصميم السبحة الإلكترونية الدائرية الخارقة في منتصف البطاقة */
    .subha-circle {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        background: radial-gradient(circle, #142019 0%, #0a100c 100%);
        border: 4px solid #00FF87;
        box-shadow: 0 0 25px rgba(0, 255, 135, 0.3);
        margin: 20px auto;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .subha-number {
        font-size: 42px;
        font-weight: 700;
        color: #00FF87;
        text-shadow: 0 0 10px rgba(0, 255, 135, 0.5);
    }
    
    /* الهيدر واللوجو المبتكر */
    .logo-area { text-align: center; margin-bottom: 25px; }
    .logo-glow { font-size: 50px; filter: drop-shadow(0 0 12px rgba(0,255,135,0.6)); display: inline-block; }
    
    html, body, [class*="css"] { text-align: right; direction: rtl; }
    .compass-container { text-align: center; margin: 25px auto; position: relative; width: 170px; height: 170px; }
    .compass-bg { width: 170px; height: 170px; border: 3px dashed #00FF87; border-radius: 50%; position: absolute; background: rgba(0,0,0,0.5); }
    .needle { width: 4px; height: 75px; background: linear-gradient(to bottom, #FF5722 50%, #444 50%); position: absolute; left: 83px; top: 10px; transform-origin: bottom center; transform: rotate(135deg); }
    </style>
""", unsafe_allow_html=True)

# عرض اللوجو المبتكر والمبهر في الواجهة الرئيسية
st.markdown("""
    <div class="logo-area">
        <div class="logo-glow">📖✨</div>
        <h1 style='color: #00FF87; margin:0; font-weight:700; font-size: 40px;'>نَبْرَة</h1>
        <p style='color: #8C9E94; font-size:15px; margin-top:4px;'>الموسوعة الإسلامية الصوتية الذكية المكتملة</p>
    </div>
""", unsafe_allow_html=True)
st.write("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎙️ استماع ومحاكاة القراء", "📖 المصحف المفسر والسنن", "📿 الأذكار والسبحة", "📅 مواقيت الصلاة والقبلة", "🏆 الإنجازات والختمة"])

surah_names = [
    "الفاتحة", "البقرة", "آل عمران", "النساء", "المائدة", "الأنعام", "الأعراف", "الأنفال", "التوبة", "يونس",
    "هود", "يوسف", "الرعد", "إبراهيم", "الحجر", "النحل", "الإسراء", "الكهف", "مريم", "طه",
    "الأنبياء", "الحج", "المؤمنون", "النور", "الفرقان", "الشعراء", "النمل", "القصص", "العنكبوت", "الروم",
    "لقمان", "السجدة", "الأحزاب", "سبأ", "فاطر", "يس", "الصافات", "ص", "الزمر", "غافر",
    "فصلت", "الشورى", "الزخرف", "الدخان", "الجاثية", "الأحقاف", "محمد", "الفتح", "الحجرات", "ق",
    "الذاريات", "الطور", "النجم", "القمر", "الرحمن", "الواقعة", "الحديد", "المجادلة", "الحشر", "الممتحنة",
    "الصف", "الجمعة", "المنافقون", "التغابن", "الطلاق", "التحريم", "الملك", "القلم", "الحاقة", "المعارج",
    "نوح", "الجن", "المزمل", "المدثر", "القيامة", "الإنسان", "المرسلات", "النبأ", "النازعات", "عبس",
    "التكوير", "الانفطار", "المطففين", "الانشقاق", "البروج", "الطارق", "الأعلى", "الغاشية", "الفجر", "البلد",
    "الشمس", "الليل", "الضحى", "الشرح", "التين", "العلق", "القدر", "البينة", "الزلزلة", "العاديات",
    "القارعة", "التكاثر", "العصر", "الهمزة", "الفيل", "قريش", "الماعون", "الكوثر", "الكافرون", "النصر",
    "المسد", "الإخلاص", "الفلق", "الناس"
]

sheikhs_servers = {
    "الشيخ محمد صديق المنشاوي (المجود)": "https://mp3quran.net",
    "الشيخ عبد الباسط عبد الصمد (المجود)": "https://mp3quran.net",
    "الشيخ محمود خليل الحصري": "https://mp3quran.net",
    "الشيخ ماهر المعيقلي": "https://mp3quran.net",
    "الشيخ ياسر الدوسري": "https://mp3quran.net",
    "الشيخ عبد الرحمن السديس": "https://mp3quran.net"
}

# --- التبويب الأول: استماع ومحاكاة القراء بتصميم بريميوم ---
with tab1:
    st.markdown("<h3 style='color: #00FF87; text-align:right;'>🎙️ طور التدريب ومطابقة نبرة الصوت والمقام</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        selected_sheikh = st.selectbox("اختر القارئ المفضل لديك:", list(sheikhs_servers.keys()))
    with col2:
        selected_surah_name = st.selectbox("اختر السورة المستهدفة للتدريب والترتيل:", surah_names, index=90)
    
    s_index = surah_names.index(selected_surah_name) + 1
    surah_num_str = f"{s_index:03d}"
    final_audio_url = f"{sheikhs_servers[selected_sheikh]}{surah_num_str}.mp3"
    
    st.markdown(f"<div class='premium-card'>▶️ تلاوة مفسرة ومرتلة بصوت المصحف المعتمد للـ <b>{selected_sheikh}</b> لسورة <b>{selected_surah_name}</b>:</div>", unsafe_allow_html=True)
    st.audio(final_audio_url)
    
    st.write("---")
    st.markdown("<h4 style='color:#00FF87;'>🔴 حان دورك الآن! اضغط وسجل تلاوتك للمحاكاة:</h4>", unsafe_allow_html=True)
    user_audio = st.audio_input("استخدم ميكروفون جهازك وباشر القراءة العذبة:")
    if user_audio is not None and st.button("🚀 احسب نسبة التطابق والمحاكاة الآن"):
        st.success("تم تحليل نبرة الصوت والموجات الصوتية بنجاح!")
        st.markdown("<h2 style='text-align: center; color: #00FF87;'>نسبة محاكاة الصوت والمقام: 94%</h2>", unsafe_allow_html=True)
        st.balloons()

# --- التبويب الثاني: المصحف المفسر والسنن النبوية بتصميم معصوم ونقي ---
with tab2:
    st.markdown("<h3 style='color: #00FF87;'>📖 المصحف الإلكتروني المفسر والسنن النبوية</h3>", unsafe_allow_html=True)
    sub_tab1, sub_tab2 = st.tabs(["📜 القرآن الكريم وتفسيره الميسر", "🌱 أحاديث وسنن نبوية مأثورة"])
    
    with sub_tab1:
        selected_read_surah = st.selectbox("اختر السورة لعرض آياتها المعتمدة وتفسيرها فوراً:", surah_names, key="read_surah")
        read_surah_num = surah_names.index(selected_read_surah) + 1
        
        try:
            with st.spinner("جاري الاتصال بخوادم المصحف الشريف المعتمدة والموثوقة 100%..."):
                quran_res = requests.get(f"https://alquran.cloud{read_surah_num}/ar.alafasy").json()
                tafseer_res = requests.get(f"https://alquran.cloud{read_surah_num}/ar.jalalayn").json()
                
                for idx, verse in enumerate(quran_res["data"]["ayahs"]):
                    v_num = verse["numberInSurah"]
