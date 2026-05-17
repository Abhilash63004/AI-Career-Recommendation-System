import streamlit as st

st.set_page_config(
    page_title="AI Career Recommendation System",
    page_icon="🚀",
    layout="wide"
)

CAREERS = [
    {
        "title": "Data Scientist",
        "icon": "🔬",
        "skills": "python machine learning statistics data visualization",
        "education": "bachelor",
        "interests": "data analytics research ai",
        "experience": "mid",
        "description": "Analyzes data to extract insights and build predictive models.",
        "salary": "₹8L–₹18L",
        "growth": "High"
    },
    {
        "title": "Software Engineer",
        "icon": "💻",
        "skills": "java c++ algorithms react javascript python",
        "education": "bachelor",
        "interests": "coding development software",
        "experience": "junior",
        "description": "Designs and develops scalable software applications.",
        "salary": "₹6L–₹25L",
        "growth": "Very High"
    },
    {
        "title": "Cybersecurity Analyst",
        "icon": "🛡️",
        "skills": "network security python cryptography linux",
        "education": "bachelor",
        "interests": "security hacking technology",
        "experience": "mid",
        "description": "Protects systems and networks from cyber threats.",
        "salary": "₹7L–₹20L",
        "growth": "Very High"
    },
    {
        "title": "Graphic Designer",
        "icon": "🎨",
        "skills": "photoshop illustrator creativity design",
        "education": "associate",
        "interests": "art creativity media",
        "experience": "entry",
        "description": "Creates visual concepts and modern designs.",
        "salary": "₹3L–₹8L",
        "growth": "Medium"
    },
    {
        "title": "UX Designer",
        "icon": "🖌️",
        "skills": "wireframing prototyping figma user research",
        "education": "bachelor",
        "interests": "design psychology user experience",
        "experience": "mid",
        "description": "Improves user experience and product usability.",
        "salary": "₹6L–₹18L",
        "growth": "High"
    }
]

SKILL_SUGGESTIONS = [
    "Python", "Machine Learning", "React", "JavaScript", "SQL",
    "Cybersecurity", "Java", "C++", "UI/UX", "Data Analysis",
    "Leadership", "Communication", "Photoshop", "Linux"
]

INTEREST_SUGGESTIONS = [
    "AI", "Software Development", "Cybersecurity", "Design",
    "Data Science", "Gaming", "Research", "Technology",
    "Marketing", "Creativity"
]


def score_career(career, user_skills, user_education, user_interests, user_experience):
    skill_words = user_skills.lower().split()
    interest_words = user_interests.lower().split()

    career_skill_words = career["skills"].lower().split()
    career_interest_words = career["interests"].lower().split()

    skill_score = sum(1 for sw in skill_words if sw in career_skill_words)
    interest_score = sum(1 for iw in interest_words if iw in career_interest_words)

    edu_levels = ["highschool", "associate", "bachelor", "master", "phd"]
    user_edu_idx = edu_levels.index(user_education)
    career_edu_idx = edu_levels.index(career["education"])
    edu_score = 1 if user_edu_idx >= career_edu_idx else 0.5

    exp_levels = ["entry", "junior", "mid", "senior"]
    user_exp_idx = exp_levels.index(user_experience)
    career_exp_idx = exp_levels.index(career["experience"])

    exp_diff = abs(user_exp_idx - career_exp_idx)

    if exp_diff == 0:
        exp_score = 1
    elif exp_diff == 1:
        exp_score = 0.7
    else:
        exp_score = 0.4

    total = (
        (skill_score * 0.4)
        + (interest_score * 0.3)
        + (edu_score * 0.15)
        + (exp_score * 0.15)
    )

    max_possible = (
        (max(len(skill_words), 1) * 0.4)
        + (max(len(interest_words), 1) * 0.3)
        + 0.15
        + 0.15
    )

    return min(total / max_possible, 1)


st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
        color: white;
    }

    .hero {
        padding: 35px;
        border-radius: 25px;
        background: linear-gradient(135deg,#6366f1,#8b5cf6,#ec4899);
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    .hero h1 {
        color: white;
        font-size: 50px;
    }

    .hero p {
        color: #f1f5f9;
        font-size: 18px;
    }

    .card {
        background: rgba(255,255,255,0.06);
        padding: 20px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 20px;
    }

    .career-card {
        background: linear-gradient(135deg,#1e293b,#0f172a);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }

    .stButton>button {
        background: linear-gradient(135deg,#6366f1,#8b5cf6);
        color: white;
        border-radius: 15px;
        height: 55px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        width: 100%;
    }

    .skill-chip {
        display: inline-block;
        background: #312e81;
        color: white;
        padding: 8px 15px;
        border-radius: 20px;
        margin: 5px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>🚀 AI Career Recommendation System</h1>
        <p>Discover your ideal career path using AI-powered matching and smart recommendations.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🛠️ Enter Your Skills")
    skills = st.text_input(
        "Skills",
        placeholder="Python React MachineLearning Java"
    )

    st.markdown("#### Suggested Skills")
    st.write(" | ".join(SKILL_SUGGESTIONS))

    st.markdown("### 💡 Enter Your Interests")
    interests = st.text_input(
        "Interests",
        placeholder="AI Design Security Technology"
    )

    st.markdown("#### Suggested Interests")
    st.write(" | ".join(INTEREST_SUGGESTIONS))

with col2:
    st.markdown("### 🎓 Education Level")

    education = st.selectbox(
        "Education",
        [
            "highschool",
            "associate",
            "bachelor",
            "master",
            "phd"
        ],
        help="Choose your education level"
    )

    st.markdown("### ⚡ Experience Level")

    experience = st.selectbox(
        "Experience",
        [
            "entry",
            "junior",
            "mid",
            "senior"
        ],
        help="Choose your experience level"
    )

    st.info("💡 Higher education and experience improve recommendations.")


if st.button("🚀 Discover My Career Paths"):

    results = []

    for career in CAREERS:
        score = score_career(
            career,
            skills,
            education,
            interests,
            experience,
        )

        results.append({
            "career": career,
            "score": score,
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    st.markdown("## 🎯 Your Top Career Matches")

    for idx, item in enumerate(results[:3]):

        career = item["career"]
        score = int(item["score"] * 100)

        st.markdown('<div class="career-card">', unsafe_allow_html=True)

        st.markdown(f"# {career['icon']} {career['title']}")

        if idx == 0:
            st.success("🏆 Best Match")

        st.write(career["description"])

        st.progress(score / 100)

        st.markdown(f"### 🔥 Match Score: {score}%")

        col1, col2 = st.columns(2)

        with col1:
            st.success(f"💰 Salary: {career['salary']}")

        with col2:
            st.info(f"📈 Growth: {career['growth']}")

        st.markdown("### 🧠 Required Skills")

        for skill in career['skills'].split():
            st.markdown(
                f'<span class="skill-chip">{skill}</span>',
                unsafe_allow_html=True,
            )

        st.markdown("### ✨ AI Career Insight")

        st.write(
            f"Based on your profile, you have strong potential to become a successful {career['title']}. Your selected skills, interests, education, and experience align well with this career path."
        )

        st.markdown('</div>', unsafe_allow_html=True)


st.markdown("---")
st.caption("Built with ❤️ using Python + Streamlit by [RAVURI ABHILASH]")

