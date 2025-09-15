# streamlit_app.py
import streamlit as st
import datetime
import io

# --- Numerology Logic (Copied directly from your astro.py) ---
# This part remains unchanged as it's pure Python.

mulank_info = {
    '1': {
        'planet': 'Sun',
        'traits': (
            "People with Mulank 1 are natural leaders who exude confidence and authority. "
            "They are independent, ambitious, and often take initiative in their careers and relationships. "
            "These individuals possess a royal aura and often become trendsetters in their social circles. "
            "They are determined and strong-willed, which helps them achieve their goals, but they may also exhibit stubbornness, "
            "dominance, or aggression when things do not go their way. Their authoritative nature makes them influential, "
            "though they must be cautious not to become bossy or overpowering."
        ),
        'lucky_colours': 'Red, White',
        'unlucky_colours': 'Black',
        'lucky_numbers': '1, 9, 6',
        'unlucky_numbers': '8'
    },
    '2': {
        'planet': 'Moon',
        'traits': (
            "Mulank 2 individuals are sensitive, emotionally rich, and deeply intuitive. They are naturally charming, often blessed "
            "with a pleasing appearance, and known for their hospitality and caring nature. These individuals are supportive in relationships, "
            "but may tend to be dependent on others for emotional stability. They are prone to mood swings, low self-confidence, and periods of emotional turmoil. "
            "However, their strong intuitive sense makes them empathetic and compassionate listeners. They may sometimes face indecisiveness and struggle with "
            "self-doubt or emotional vulnerability, but they remain deeply loving and caring at heart."
        ),
        'lucky_colours': 'White, Red, Green',
        'unlucky_colours': 'Black',
        'lucky_numbers': '1, 5',
        'unlucky_numbers': '4, 8, 9'
    },
    '3': {
        'planet': 'Jupiter',
        'traits': (
            "Mulank 3 individuals are highly creative, imaginative, and intellectually curious. They have a passion for learning and are often drawn to education, "
            "teaching, or mentorship roles. Their ideas are innovative and inspiring, and they excel at starting new projects with energy and enthusiasm. "
            "However, they may struggle to maintain focus and follow through, often leaving things unfinished. Their tendency to explore multiple areas "
            "can lead to scattered efforts, but their wisdom and creativity remain their biggest strengths."
        ),
        'lucky_colours': 'Yellow, Red, Green',
        'unlucky_colours': 'White',
        'lucky_numbers': '1, 3, 5',
        'unlucky_numbers': '6'
    },
    '4': {
        'planet': 'Rahu',
        'traits': (
            "People with Mulank 4 are disciplined, determined, and grounded. They are practical thinkers who approach life with logic and order. "
            "They have a reputation for being stubborn and impulsive, and while they can be emotionally distant, they are highly focused on their goals. "
            "These individuals are not afraid of hard work and often face delays in life, but they eventually reach success through persistence. "
            "Mulank 4 people may come across as blunt or harsh, and their intense focus can sometimes strain relationships. However, they are deeply committed "
            "to improving their lives and achieving tangible outcomes."
        ),
        'lucky_colours': 'White',
        'unlucky_colours': 'Black',
        'lucky_numbers': '7, 1, 5, 6 (4,8 are very good in temporary relationships)',
        'unlucky_numbers': '2, 9 (4,8 are worst in permanent relationships)'
    },
    '5': {
        'planet': 'Mercury',
        'traits': (
            "Mulank 5 people are dynamic, flexible, and resourceful. They are great at adapting to change and balancing energies around them. "
            "They can easily replenish or compensate for the absence of other numbers in the Lo Shu Grid. These individuals are self-responsible "
            "and have the ability to bounce back from setbacks. On the flip side, they may be lazy, overconfident, or avoid physical effort. "
            "They dislike being micromanaged and prefer to work on their own terms. Their mental agility and communicative abilities make them well-suited "
            "for roles involving negotiation or creativity."
        ),
        'lucky_colours': 'Green, Red, White',
        'unlucky_colours': 'None',
        'lucky_numbers': '5, 1, 6',
        'unlucky_numbers': 'None'
    },
    '6': {
        'planet': 'Venus',
        'traits': (
            "Individuals born under Mulank 6 are lovers of beauty, luxury, and refinement. They are romantic by nature and find joy in art, nature, travel, "
            "and aesthetic pleasures. Their charming personality often draws people to them. However, they may have a cunning or manipulative side when it comes to achieving their goals. "
            "They can be great at presenting themselves and may occasionally stretch the truth to maintain appearances. Despite this, they are generally warm-hearted and sociable."
        ),
        'lucky_colours': 'White',
        'unlucky_colours': 'Yellow',
        'lucky_numbers': '6, 1, 5, 7',
        'unlucky_numbers': '3'
    },
    '7': {
        'planet': 'Ketu',
        'traits': (
            "Mulank 7 individuals are spiritual, introspective, and deeply intuitive. They are seekers of truth and often drawn to research, philosophy, and the occult. "
            "Their trusting nature can lead them to be betrayed or taken advantage of, yet they remain kind-hearted and humane. They have a magnetic personality that attracts others, "
            "but may experience loneliness or complex relationships. Despite emotional ups and downs, they possess strong intuitive abilities and are capable of profound insight."
        ),
        'lucky_colours': 'Red, White, Green',
        'unlucky_colours': 'Black',
        'lucky_numbers': '4, 6, 1',
        'unlucky_numbers': 'None'
    },
    '8': {
        'planet': 'Saturn',
        'traits': (
            "Mulank 8 people are highly disciplined and realistic. They often experience significant struggles and delays in life but ultimately succeed through effort and endurance. "
            "They are great at managing finances, working with systems, and maintaining routines. However, they can also be egoistic or emotionally reserved. "
            "Their practical approach sometimes makes them appear cold, but they are deeply committed to their responsibilities. Emotional growth may be a lifelong journey for them."
        ),
        'lucky_colours': 'Green, White',
        'unlucky_colours': 'Black',
        'lucky_numbers': '5, 6 (4,8 are good temporarily)',
        'unlucky_numbers': '4, 8 (bad in permanent relationships)'
    },
    '9': {
        'planet': 'Mars',
        'traits': (
            "People with Mulank 9 are intelligent, assertive, and action-driven. They are passionate and courageous, often taking bold steps toward their goals. "
            "Their memory is sharp, and they can be incredibly helpful to those in need. However, their aggressive tendencies and mood swings may sometimes create conflicts. "
            "They are natural fighters and problem-solvers, known for their ability to handle tough situations and protect others with determination."
        ),
        'lucky_colours': 'Orange, Red, Green',
        'unlucky_colours': 'None',
        'lucky_numbers': '1, 5',
        'unlucky_numbers': '4, 2'
    }
}
dict1 = {
    1: ['A','I','J','Q','Y'], 2: ['B','K','R'], 3: ['C','G','L','S'],
    4: ['D','M','T'], 5: ['E','H','N','X'], 6: ['U','V','W'],
    7: ['O','Z'], 8: ['P','F']
}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def calculate_totals(user_input):
    count = 0
    for i in user_input:
        if i.upper() in alphabet:
            for key, value in dict1.items():
                if i.upper() in value:
                    count += key
        elif i.isdigit():
            count += int(i)
        elif i != ' ':
            raise ValueError(f"Invalid character: {i}")
    full_total = count
    while count > 9:
        count = sum(int(d) for d in str(count))
    return full_total, count

def digit_sum(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

# --- PDF Generation Function using FPDF2 ---
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, '🔮 Lo Shu Grid Numerology Report', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 5, body)
        self.ln()
        
    def draw_grid(self, counts):
        pos_map = {
            '4': (0, 0), '9': (0, 1), '2': (0, 2),
            '3': (1, 0), '5': (1, 1), '7': (1, 2),
            '8': (2, 0), '1': (2, 1), '6': (2, 2),
        }
        
        # Invert pos_map for easy lookup
        grid_numbers = {v: k for k, v in pos_map.items()}

        cell_width = 30
        cell_height = 30
        self.set_font('Arial', '', 20)
        
        # Center the grid
        start_x = (self.w - 3 * cell_width) / 2
        self.set_x(start_x)

        for r in range(3):
            for c in range(3):
                num = grid_numbers[(r, c)]
                count = counts.get(num, 0)
                text = num * count if count else ""
                self.cell(cell_width, cell_height, text, 1, 0, 'C')
            self.ln(cell_height)
            if r < 2:
                self.set_x(start_x)
        self.ln(10)


def create_pdf_report(data):
    pdf = PDF()
    pdf.add_page()

    # Basic Info
    pdf.chapter_title('Numerology Profile:')
    info_body = (
        f"Date of Birth: {data['dob'].strftime('%d-%B-%Y')}\n"
        f"Mulank (Driver Number): {data['mulank']}\n"
        f"Bhagyank (Conductor Number): {data['bhagyank']}\n"
        f"Kua Number ({data['gender']}): {data['kua']}"
    )
    pdf.chapter_body(info_body)
    
    # Lo Shu Grid
    pdf.chapter_title('Your Lo Shu Grid:')
    pdf.draw_grid(data['counts'])

    # Traits Info
    if data['mulank'] in mulank_info:
        info = mulank_info[data['mulank']]
        pdf.chapter_title(f"Analysis for Mulank {data['mulank']} (Planet: {info['planet']})")
        
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(0, 5, "Personality Traits:", 0, 1)
        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(0, 5, info['traits'])
        pdf.ln(5)

        details_body = (
            f"Lucky Colours: {info['lucky_colours']}\n"
            f"Unlucky Colours: {info['unlucky_colours']}\n"
            f"Lucky Numbers: {info['lucky_numbers']}\n"
            f"Unlucky Numbers: {info['unlucky_numbers']}"
        )
        pdf.chapter_body(details_body)

    # Use a memory buffer to return the PDF data
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    return pdf_buffer.getvalue()


# --- Streamlit App UI ---
st.set_page_config(page_title="Numerology Toolkit", page_icon="🔮", layout="centered")
st.title("🔮 Numerology Toolkit")

tab1, tab2 = st.tabs(["🔢 Name & Phone Calculator", "🗓️ Lo Shu Grid"])

# --- Tab 1: Name Calculator ---
with tab1:
    st.header("Name / Phone Numerology")
    st.write("Calculate the single-digit numerological total for any name or number.")
    
    name_input = st.text_input("Enter a name or phone number:", placeholder="e.g., John Doe or 12345")

    if st.button("Calculate Total", key="name_calc"):
        if name_input:
            try:
                full_total, single_total = calculate_totals(name_input)
                result_str = f"**Single Digit Total: {single_total}**"
                if full_total > 9:
                    result_str = f"**Total: {full_total}** → {result_str}"
                st.success(result_str)
            except ValueError as e:
                st.error(f"Input Error: {e}")
        else:
            st.warning("Please enter a value to calculate.")

# --- Tab 2: Lo Shu Grid ---
with tab2:
    st.header("Lo Shu Grid Calculator")
    st.write("Generate your Lo Shu Grid based on your date of birth.")

    # Input fields
    dob = st.date_input(
        "Enter your Date of Birth:",
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today()
    )
    gender = st.selectbox("Select your Gender:", ["Male", "Female"])

    if st.button("Generate Grid & Report", key="grid_gen"):
        day = str(dob.day).zfill(2)
        month = str(dob.month).zfill(2)
        year = str(dob.year)

        # Calculations
        day_int = int(day)
        year_sum = sum(int(d) for d in year)
        dob_digits = list(day + month + year)
        digits = [d for d in dob_digits if d in '123456789']

        # Mulank
        mulank = str(digit_sum(day_int))
        if day_int >= 10:
             digits.append(mulank)

        # Bhagyank
        all_digits_sum = sum(int(d) for d in (day + month + year))
        bhagyank = str(digit_sum(all_digits_sum))
        digits.append(bhagyank)

        # Kua Number
        if gender == "Male":
            kua = str(digit_sum(abs(11 - digit_sum(year_sum))))
        else: # Female
            kua = str(digit_sum(4 + digit_sum(year_sum)))
        digits.append(kua)

        counts = {str(i): 0 for i in range(1, 10)}
        for d in digits:
            if d in counts:
                counts[d] += 1
        
        # Store results in session state to use for PDF export
        st.session_state.report_data = {
            'dob': dob,
            'gender': gender,
            'mulank': mulank,
            'bhagyank': bhagyank,
            'kua': kua,
            'counts': counts
        }

    # Display results if they exist in the session state
    if 'report_data' in st.session_state:
        data = st.session_state.report_data
        
        st.subheader("Your Numerology Numbers")
        col1, col2, col3 = st.columns(3)
        col1.metric("Mulank (Driver)", data['mulank'])
        col2.metric("Bhagyank (Conductor)", data['bhagyank'])
        col3.metric(f"Kua ({data['gender']})", data['kua'])

        st.subheader("Your Lo Shu Grid")
        
        # --- Display Grid using HTML Table ---
        pos_map = {
            '4': (0, 0), '9': (0, 1), '2': (0, 2),
            '3': (1, 0), '5': (1, 1), '7': (1, 2),
            '8': (2, 0), '1': (2, 1), '6': (2, 2),
        }
        grid_numbers = {v: k for k, v in pos_map.items()} # Inverted map
        
        grid_html = "<table style='width: 300px; height: 300px; border-collapse: collapse; margin: auto;'>"
        for r in range(3):
            grid_html += "<tr>"
            for c in range(3):
                num = grid_numbers[(r, c)]
                count = data['counts'].get(num, 0)
                text = num * count if count else ""
                grid_html += f"<td style='border: 2px solid #ccc; text-align: center; font-size: 24px; font-weight: bold;'>{text}</td>"
            grid_html += "</tr>"
        grid_html += "</table>"
        
        st.markdown(grid_html, unsafe_allow_html=True)
        st.write("") # Spacer

        # Display Traits
        mulank_val = data['mulank']
        if mulank_val in mulank_info:
            info = mulank_info[mulank_val]
            st.subheader(f"Analysis for Mulank {mulank_val} — Planet {info['planet']}")
            
            st.markdown(f"**Personality Traits:** {info['traits']}")
            st.markdown(f"**Lucky Colours:** {info['lucky_colours']}")
            st.markdown(f"**Unlucky Colours:** {info['unlucky_colours']}")
            st.markdown(f"**Lucky Numbers:** {info['lucky_numbers']}")
            st.markdown(f"**Unlucky Numbers:** {info['unlucky_numbers']}")
        
        st.write("---") # Divider
