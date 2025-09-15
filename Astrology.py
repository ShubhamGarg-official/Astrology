import streamlit as st
import datetime

# --- Numerology Logic ---
mulank_info = {
    '1': {'planet': 'Sun', 'traits': "People with Mulank 1 are natural leaders...", 'lucky_colours': 'Red, White', 'unlucky_colours': 'Black', 'lucky_numbers': '1, 9, 6', 'unlucky_numbers': '8'},
    '2': {'planet': 'Moon', 'traits': "Mulank 2 individuals are sensitive...", 'lucky_colours': 'White, Red, Green', 'unlucky_colours': 'Black', 'lucky_numbers': '1, 5', 'unlucky_numbers': '4, 8, 9'},
    '3': {'planet': 'Jupiter', 'traits': "Mulank 3 individuals are highly creative...", 'lucky_colours': 'Yellow, Red, Green', 'unlucky_colours': 'White', 'lucky_numbers': '1, 3, 5', 'unlucky_numbers': '6'},
    '4': {'planet': 'Rahu', 'traits': "People with Mulank 4 are disciplined...", 'lucky_colours': 'White', 'unlucky_colours': 'Black', 'lucky_numbers': '7, 1, 5, 6', 'unlucky_numbers': '2, 9'},
    '5': {'planet': 'Mercury', 'traits': "Mulank 5 people are dynamic...", 'lucky_colours': 'Green, Red, White', 'unlucky_colours': 'None', 'lucky_numbers': '5, 1, 6', 'unlucky_numbers': 'None'},
    '6': {'planet': 'Venus', 'traits': "Individuals born under Mulank 6 are lovers of beauty...", 'lucky_colours': 'White', 'unlucky_colours': 'Yellow', 'lucky_numbers': '6, 1, 5, 7', 'unlucky_numbers': '3'},
    '7': {'planet': 'Ketu', 'traits': "Mulank 7 individuals are spiritual...", 'lucky_colours': 'Red, White, Green', 'unlucky_colours': 'Black', 'lucky_numbers': '4, 6, 1', 'unlucky_numbers': 'None'},
    '8': {'planet': 'Saturn', 'traits': "Mulank 8 people are highly disciplined...", 'lucky_colours': 'Green, White', 'unlucky_colours': 'Black', 'lucky_numbers': '5, 6', 'unlucky_numbers': '4, 8'},
    '9': {'planet': 'Mars', 'traits': "People with Mulank 9 are intelligent...", 'lucky_colours': 'Orange, Red, Green', 'unlucky_colours': 'None', 'lucky_numbers': '1, 5', 'unlucky_numbers': '4, 2'}
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

    dob = st.date_input(
        "Enter your Date of Birth:",
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today()
    )
    gender = st.selectbox("Select your Gender:", ["Male", "Female"])

    if st.button("Generate Grid", key="grid_gen"):
        day = str(dob.day).zfill(2)
        month = str(dob.month).zfill(2)
        year = str(dob.year)

        # Calculations
        day_int = int(day)
        year_sum = sum(int(d) for d in year)
        dob_digits = list(day + month + year)
        digits = [d for d in dob_digits if d in '123456789']

        mulank = str(digit_sum(day_int))
        if day_int >= 10:
            digits.append(mulank)

        all_digits_sum = sum(int(d) for d in (day + month + year))
        bhagyank = str(digit_sum(all_digits_sum))
        digits.append(bhagyank)

        if gender == "Male":
            kua = str(digit_sum(abs(11 - digit_sum(year_sum))))
        else:
            kua = str(digit_sum(4 + digit_sum(year_sum)))
        digits.append(kua)

        counts = {str(i): 0 for i in range(1, 10)}
        for d in digits:
            if d in counts:
                counts[d] += 1

        st.session_state.report_data = {
            'dob': dob,
            'gender': gender,
            'mulank': mulank,
            'bhagyank': bhagyank,
            'kua': kua,
            'counts': counts
        }

    if 'report_data' in st.session_state:
        data = st.session_state.report_data
        
        st.subheader("Your Numerology Numbers")
        col1, col2, col3 = st.columns(3)   # ✅ ye line ab hamesha define karegi
        col1.metric("Mulank (Driver)", data['mulank'])
        col2.metric("Bhagyank (Conductor)", data['bhagyank'])
        col3.metric(f"Kua ({data['gender']})", data['kua'])

        st.subheader("Your Lo Shu Grid")
        
        pos_map = {
            '4': (0, 0), '9': (0, 1), '2': (0, 2),
            '3': (1, 0), '5': (1, 1), '7': (1, 2),
            '8': (2, 0), '1': (2, 1), '6': (2, 2),
        }
        grid_numbers = {v: k for k, v in pos_map.items()}
        
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
        st.write("")

        mulank_val = data['mulank']
        if mulank_val in mulank_info:
            info = mulank_info[mulank_val]
            st.subheader(f"Analysis for Mulank {mulank_val} — Planet {info['planet']}")
            
            st.markdown(f"**Personality Traits:** {info['traits']}")
            st.markdown(f"**Lucky Colours:** {info['lucky_colours']}")
            st.markdown(f"**Unlucky Colours:** {info['unlucky_colours']}")
            st.markdown(f"**Lucky Numbers:** {info['lucky_numbers']}")
            st.markdown(f"**Unlucky Numbers:** {info['unlucky_numbers']}")
