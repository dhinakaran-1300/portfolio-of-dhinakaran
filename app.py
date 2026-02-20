import streamlit as st
import requests
from pathlib import Path
import urllib.parse

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Dhinakaran S | Data Analyst", page_icon="📊", layout="wide"
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    profile_img = Path(__file__).parent / "images" / "dhina.JPG"
    st.image(profile_img, width=150)

    st.title("Dhinakaran S")
    st.write("Chennai, Tamil Nadu")
    st.write("dhinakaran1300@gmail.com")

    st.markdown("---")
    st.subheader("Connect")
    st.link_button("LinkedIn Profile", "https://linkedin.com/in/dhinakaran1300")
    st.link_button("GitHub Profile", "https://github.com/dhinakaran-1300")
    st.markdown("---")
    st.caption("© 2026 Dhinakaran S")

# ---------------- HEADER ----------------
with st.container(border=True):
    st.title("Dhinakaran S")
    st.caption("Data Analyst | Open to Opportunities")

    st.write(
        "Data Analytics fresher with hands-on experience in Python, SQL, and Power BI. "
        "Skilled in data cleaning, analysis, and visualization with strong analytical thinking "
        "and knowledge of machine learning fundamentals. Focused on using data to support "
        "business decision-making and solve real-world problems."
    )


# ---------- VBA INFO MODAL ----------
@st.dialog("VBA Automation Details")
def show_vba_info():
    st.markdown("""
### Developed a Macro to Enhance Process Efficiency, Quality, and Accuracy

- Reduced processing time by **30–45 minutes**
- Improved data deduplication, mapping, and organization
- Achieved **40% time saving** in key workflows
- Automated repetitive tasks and ensured consistent outputs
- Improved accuracy and reduced manual effort
""")


# ---------------- EXPERIENCE ----------------
with st.container(border=True):
    st.header("Professional Experience")

    role_col, date_col = st.columns([3, 1])

    with role_col:
        st.subheader("Process Associate — Tata Consultancy Services")

    with date_col:
        st.caption("Apr 2023 – Aug 2025 | Chennai")

    st.markdown(
        """
<div style="font-size:18px">

- Analyzed large transactional datasets to identify trends, anomalies, and risk indicators using data-driven analytical techniques.

- Extracted, cleaned, and validated structured and unstructured data to ensure accuracy, consistency, and data quality for reliable reporting.

- Generated structured reports and analytical insights to support business operations and compliance decision-making.

- Performed data profiling and pattern analysis to improve investigation efficiency and enhance process outcomes.

- Automated reporting workflows using <b>Excel VBA</b>, improving data processing efficiency and reducing manual effort by approximately <b>70%</b>.

- Maintained data accuracy and quality standards by documenting data processes, validation procedures, and investigation findings.

- Prepared data reports and dashboards using <b>Microsoft Excel</b> to support monitoring, performance tracking, and data-driven decision-making.

</div>
""",
        unsafe_allow_html=True,
    )

    st.divider()
    st.subheader("Achievements")

    ach1, ach2 = st.columns(2)

    with ach1:
        with st.container(border=True):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.success("VBA automation reduced 70% manual effort")
            with col2:
                if st.button("Details", key="vba_info"):
                    show_vba_info()

    with ach2:
        with st.container(border=True):
            st.success("Best Performer Award — MUFG Client")

# ---------------- SKILLS ----------------
with st.container(border=True):
    st.header("Technical Skills")
    st.caption("Technologies and analytical capabilities")

    col1, col2 = st.columns(2)

    # Data & Programming Card
    with col1:
        with st.container(border=True):
            st.subheader("Data & Programming")

            s1, s2 = st.columns(2)

            with s1:
                st.write("Python")
                st.progress(90)

                st.write("SQL (MySQL)")
                st.progress(85)

                st.write("Excel & VBA")
                st.progress(80)

            with s2:
                st.write("Power BI")
                st.progress(75)

                st.write("R")
                st.progress(60)

    # Libraries Card
    with col2:
        with st.container(border=True):
            st.subheader("Libraries & Tools")

            t1, t2 = st.columns(2)

            with t1:
                st.write("Pandas")
                st.write("NumPy")
                st.write("Matplotlib")

            with t2:
                st.write("Seaborn")
                st.write("Scikit-learn")
                st.write("Streamlit")

    st.divider()
    st.subheader("Core Competencies")
    st.info("EDA • Feature Engineering • Model Building • Evaluation")

# ---------------- PROJECTS ----------------
with st.container(border=True):
    if "github_repos" not in st.session_state:
        url = "https://api.github.com/users/dhinakaran-1300/repos"
        response = requests.get(url)

        if response.status_code != 200:
            st.error("Unable to fetch GitHub projects")
            st.stop()

        st.session_state.github_repos = response.json()

    repos = st.session_state.github_repos

    pinned_names = ["Health-Ai-Suite", "Employee-Attrition-Prediction"]

    live_links = {
        "Health-Ai-Suite": "https://health-ai-suite.streamlit.app/",
        "Employee-Attrition-Prediction": "https://employee-attrition-prediction-ibm.streamlit.app/",
    }

    pinned = [r for r in repos if r["name"] in pinned_names]
    others = sorted(
        [r for r in repos if r["name"] not in pinned_names],
        key=lambda x: x["created_at"],
        reverse=True,
    )

    all_projects = pinned + others

    h1, h2 = st.columns([6, 1])
    h1.header("Projects")
    h2.metric("Total", len(all_projects))

    st.session_state.setdefault("project_index", 0)

    per_page = 2
    max_index = max(0, len(all_projects) - per_page)

    nav1, _, nav3 = st.columns([1, 6, 1])

    if nav1.button("⬅️", use_container_width=True):
        st.session_state.project_index = max(
            0, st.session_state.project_index - per_page
        )

    if nav3.button("➡️", use_container_width=True):
        st.session_state.project_index = min(
            max_index, st.session_state.project_index + per_page
        )

    visible = all_projects[
        st.session_state.project_index : st.session_state.project_index + per_page
    ]

    for col, repo in zip(st.columns(per_page), visible):
        with col:
            with st.container(border=True):
                if repo["name"] in pinned_names:
                    st.markdown("Featured")

                st.subheader(repo["name"])
                st.write(repo["description"] or "No description")
                st.caption(f"Language: {repo['language'] or 'Not specified'}")

                c1, c2 = st.columns(2)
                c1.link_button("GitHub", repo["html_url"])

                if repo["name"] in live_links:
                    c2.link_button("Live", live_links[repo["name"]])

# ---------------- VIRTUAL EXPERIENCE ----------------
with st.container(border=True):
    st.header("Virtual Experience")

    st.markdown(
        """
<div style="font-size:18px">

<b>Tata Data Visualisation Program (Forage)</b> | February 2026

- Completed a virtual simulation focused on creating data visualizations for <b>Tata Consultancy Services</b> to support business decision-making.

- Designed analytical questions and prepared insights for discussions with client senior leadership.

- Developed data visualizations and dashboards to communicate findings clearly and help executives make informed strategic decisions.

</div>
""",
        unsafe_allow_html=True,
    )

# ---------------- CERTIFICATIONS ----------------
mysql_img = Path(__file__).parent / "images" / "mysql_cert.jpeg"
python_img = Path(__file__).parent / "images" / "python_cert.jpg"
tata_img = Path(__file__).parent / "images" / "tata_cert.jpg"

with st.container(border=True):
    st.header("Certifications")

    certifications = [
        (
            "MySQL Certification — GUVI",
            mysql_img,
            "https://www.guvi.in/verify-certificate?id=C428q6X179Pgbm361W",
        ),
        (
            "Python Certification — IBM",
            python_img,
            "https://courses.cognitiveclass.ai/certificates/917f2ee0e26041019722a8694df4fc3f",
        ),
        (
            "Tata Data Visualisation — Forage",
            tata_img,
            "https://www.theforage.com/completion-certificates/ifobHAoMjQs9s6bKS/MyXvBcppsW2FkNYCX_ifobHAoMjQs9s6bKS_694f46a339ff7eaad9e80a28_1770188839626_completion_certificate.pdf",
        ),
    ]

    for i in range(0, len(certifications), 3):
        cols = st.columns(3)

        for col, cert in zip(cols, certifications[i : i + 3]):
            title, img, link = cert
            with col:
                with st.container(border=True):
                    st.subheader(title)
                    st.image(img, width=350)
                    st.divider()
                    st.link_button("Verify Certificate", link)

# ---------------- CONTACT ----------------
with st.container(border=True):
    st.header("Connect With Me")
    st.subheader("Send a Message")

    with st.form("contact_form", clear_on_submit=True):
        email = st.text_input("Your Email")
        name = st.text_input("Your Name")
        message = st.text_area("Message", height=150)

        submit = st.form_submit_button("Send Message")

        if submit:
            if email and name and message:
                subject = f"Portfolio Contact from {name}"
                body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

                subject_encoded = urllib.parse.quote(subject)
                body_encoded = urllib.parse.quote(body)

                gmail_link = (
                    f"https://mail.google.com/mail/?view=cm&fs=1"
                    f"&to=dhinakaran1300@gmail.com"
                    f"&su={subject_encoded}"
                    f"&body={body_encoded}"
                )

                st.success("Send message using Gmail")
                st.link_button("Open Gmail Compose", gmail_link)

            else:
                st.error("Please fill all fields.")

