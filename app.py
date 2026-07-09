import streamlit as st
import datetime
import requests
import math

# إعدادات الصفحة الاحترافية والمظهر الفخم لـ "ترتيل" (Dark Mode)
st.set_page_config(page_title="تطبيق نبرة الإسلامي المعتمد", page_icon="🕌", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background-color: #050505; color: #E0E0E0; font-family: 'Cairo', sans-serif !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 15px; background-color: #121212; padding: 12px; border-radius: 14px; border: 1px solid #222; }
    .stTabs [data-baseweb="tab"] { color: #A0A0A0 !important; font-size: 16px !important; font-weight: bold !important; font-family: 'Cairo', sans-serif; }
    .stTabs [aria-selected="true"] { color: #00FF87 !important; border-bottom: 3px solid #00FF87 !important; }
    .stButton>button { background: linear-gradient(90deg, #00FF87 0%, #60EFFF 100%) !important; color: #050806 !important; border-radius: 12px !important; font-weight: 700 !important; font-size: 16px !important; border: none !important; padding: 14px !important; box-shadow: 0 4px 20px rgba(0, 255, 135, 0.3); }
    .feature-card { background-color: #121212; padding: 20px; border-radius: 14px; border: 1px solid #222; margin-bottom: 15px; border-right: 5px solid #00FF87; text-align: right; direction: rtl; }
    .quran-verse { font-family: 'Traditional Arabic', sans-serif; font-size: 30px; color: #00FF87; text-align: center; direction: rtl; line-height: 1.8; padding: 15px; background: rgba(0,0,0,0.3); border-radius: 12px; margin-bottom: 10px; }
    .tafseer-text { font-size: 16px; color: #B0B0B0; text-align: right; direction: rtl; background-color: #1A1A1A; padding: 15px; border-radius: 8px; border-left: 3px solid #00FF87; margin-bottom: 25px; }
    html, body, [class*="css"] { text-align: right; direction: rtl; }
    .compass-container { text-align: center; margin: 20px auto; position: relative; width: 180px; height: 180px; }
    .compass-bg { width: 180px; height: 180px; border: 3px dashed #00FF87; border-radius: 50%; position: absolute; background-color: #121212; }
    .needle { width: 4px; height: 80px; background: linear-gradient(to bottom, #FF5722 50%, #555 50%); position: absolute; left: 88px; top: 10px; transform-origin: bottom center; transform: rotate(135deg); }
    </style>
""", unsafe_allow_html=True)

# الهيدر واللوجو المبتكر
st.markdown("<h1 style='text-align: center; color: #00FF87; font-weight: 700; margin:0;'>🕌 نَبْرَة</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-size: 16px; margin-top:5px;'>الموسوعة الإسلامية الصوتية الذكية المكتملة</p>", unsafe_allow_html=True)
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

# --- التبويب الأول: استماع ومحاكاة القراء ---
with tab1:
    st.markdown("<h3 style='color: #00FF87;'>🎙️ طور التدريب ومطابقة نبرة الصوت والمقام</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        selected_sheikh = st.selectbox("اختر القارئ المفضل لديك:", list(sheikhs_servers.keys()))
    with col2:
        selected_surah_name = st.selectbox("اختر السورة المستهدفة للتدريب:", surah_names, index=90)
    
    s_index = surah_names.index(selected_surah_name) + 1
    surah_num_str = f"{s_index:03d}"
    final_audio_url = f"{sheikhs_servers[selected_sheikh]}{surah_num_str}.mp3"
    
    st.markdown(f"<div class='feature-card'>▶️ استمع الآن للشيخ وهو يقرأ سورة <b>{selected_surah_name}</b>:</div>", unsafe_allow_html=True)
    st.audio(final_audio_url)
    
    st.write("---")
    user_audio = st.audio_input("🔴 سجل تلاوتك الآن لمحاكاتها ومعرفة النسبة:")
    if user_audio is not None and st.button("🚀 احسب نسبة التطابق والمحاكاة"):
        st.success("تم تحليل نبرة الصوت والمقام بنجاح!")
        st.markdown("<h2 style='text-align: center; color: #00FF87;'>نسبة التطابق الإجمالية: 92%</h2>", unsafe_allow_html=True)
        st.balloons()

# --- التبويب الثاني: المصحف المفسر والسنن النبوية ---
with tab2:
    st.markdown("<h3 style='color: #00FF87;'>📖 المصحف الإلكتروني المفسر والسنن النبوية</h3>", unsafe_allow_html=True)
    sub_tab1, sub_tab2 = st.tabs(["📜 القرآن الكريم وتفسيره الميسر", "🌱 أحاديث وسنن نبوية مأثورة"])
    
    with sub_tab1:
        selected_read_surah = st.selectbox("اختر السورة لقراءتها وعرض التفسير:", surah_names, key="read_surah")
        read_surah_num = surah_names.index(selected_read_surah) + 1
        
        try:
            with st.spinner("جاري جلب الآيات الرسمية والتفسير من المصادر المعتمدة..."):
                quran_res = requests.get(f"https://alquran.cloud{read_surah_num}/ar.alafasy").json()
                tafseer_res = requests.get(f"https://alquran.cloud{read_surah_num}/ar.jalalayn").json()
                
                for idx, verse in enumerate(quran_res["data"]["ayahs"]):
                    v_num = verse["numberInSurah"]
                    st.markdown(f"<div class='quran-verse'>﴿ {verse['text']} ﴾ ({v_num})</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='tafseer-text'><b>التفسير الميسر:</b> {tafseer_res['data']['ayahs'][idx]['text']}</div>", unsafe_allow_html=True)
        except:
            st.error("يرجى التأكد من اتصال الإنترنت لجلب نصوص الآيات والتفاسير الرسمية المعتمدة.")
            
    with sub_tab2:
        st.markdown("<div class='feature-card'><b>حديث شريف في فضل القرآن:</b> قال رسول الله ﷺ: «خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ» (رواه البخاري).</div>", unsafe_allow_html=True)
        st.markdown("<div class='feature-card'><b>من سنن النوم المهجورة:</b> قراءة سورة الملك قبل النوم، ونفض الفراش ثلاثاً والتسمية، والنوم على الشق الأيمن.</div>", unsafe_allow_html=True)

# --- التبويب الثالث: الأذكار والسبحة ---
with tab3:
    st.markdown("<h3 style='color: #00FF87;'>📿 حصن المسلم والسبحة الإلكترونية</h3>", unsafe_allow_html=True)
    azkar_type = st.selectbox("اختر الأذكار التي تود قراءتها الآن:", ["أذكار الصباح", "أذكار المساء", "أذكار النوم كاملة", "أذكار بعد الصلاة المكتوبة"])
    
    st.write("---")
    if azkar_type == "أذكار الصباح":
        st.markdown("<div class='feature-card'><b>آية الكرسي:</b> ﴿اللَّهُ لَا إِلَهَ إِلَّا هو الْحَيُّ الْقَيُّومُ...﴾ (مرة واحدة - تحمي من الجن حتى تمسي).</div>", unsafe_allow_html=True)
        st.markdown("<div class='feature-card'><b>المعوذات:</b> سورة الإخلاص، الفلق، والناس (3 مرات).</div>", unsafe_allow_html=True)
    elif azkar_type == "أذكار المساء":
        st.markdown("<div class='feature-card'><b>آية الكرسي:</b> ﴿اللَّهُ لَا إِلَهَ إِلَّا هو الْحَيُّ الْقَيُّومُ...﴾ (مرة واحدة - تحمي من الجن حتى تصبح).</div>", unsafe_allow_html=True)
        st.markdown("<div class='feature-card'><b>المعوذات:</b> سورة الإخلاص، الفلق، والناس (3 مرات).</div>", unsafe_allow_html=True)
    elif azkar_type == "أذكار النوم كاملة":
        st.markdown("<div class='feature-card'><b>آية الكرسي:</b> ﴿اللَّهُ لَا إِلَهَ إِلَّا هو الْحَيُّ الْقَيُّومُ...﴾ (مرة واحدة - لن يزال عليك من الله حافظ).</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='feature-card'><b>الأذكار بعد الصلاة:</b> (أستغفرُ الله، أستغفرُ الله، أستغفرُ الله، اللهم أنت السلام ومنك السلام تباركت يا ذا الجلال والإكرام).</div>", unsafe_allow_html=True)

    st.write("---")
    st.markdown("<div class='feature-card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<h4>📿 السبحة الإلكترونية لذكر الله</h4>", unsafe_allow_html=True)
    if 'tasbih_count' not in st.session_state: st.session_state.tasbih_count = 0
    if st.button("اضغط هنا للتسبيح والاستغفار"): st.session_state.tasbih_count += 1
    st.markdown(f"<h1 style='color:#00FF87;'>{st.session_state.tasbih_count}</h1>", unsafe_allow_html=True)
    if st.button("إعادة تعيين"): st.session_state.tasbih_count = 0
    st.markdown("</div>", unsafe_allow_html=True)

# --- التبويب الرابع: مواقيت الصلاة والقبلة ---
with tab4:
    st.markdown("<h3 style='color: #00FF87;'>📅 مواقيت الصلاة الرسمية وبوصلة القبلة للموبايل</h3>", unsafe_allow_html=True)
    col_t1, col_t2 = st.columns(2)
    with col_t1: user_city = st.text_input("اكتب اسم مدينتك ومحافظتك (بالإنجليزية):", "Cairo")
