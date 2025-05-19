import streamlit as st

# Set up session state variables
if 'c' not in st.session_state:
    st.session_state.c = 0  # step
    st.session_state.sum = 0  # total guessed number
    st.session_state.last_clicked = None  # to prevent double increment

# Define all steps with text and value
sets = [
    {
        "text": [
            "Welcome to Num-Sherlock!",
            "Pick any number from 1 to 100",
            "Click NEXT when ready",
            "Don't make it easy for me though ;) !!"
        ],
        "button": "NEXT"
    },
    {
        "text": [
            "Check for your number and click 'YES' if present or else 'NO'",
            "",
            "16  17  18  19  20  21  22  23",
            "24  25  26  27  28  29  30  31",
            "48  49  50  51  52  53  54  55",
            "56  57  58  59  60  61  62  63",
            "80  81  82  83  84  85  86  87",
            "88  89  90  91  92  93  94  95"
        ],
        "value": 16
    },
    {
        "text": [
            "Check for your number and click 'YES' if present or else 'NO'",
            "",
            "02  03  06  07  10  11  14  15",
            "18  19  22  23  26  27  30  31",
            "34  35  38  39  42  43  46  47",
            "50  51  54  55  58  59  62  63",
            "66  67  70  71  74  75  78  79",
            "82  83  86  87  90  91  94  95",
            "98  99"
        ],
        "value": 2
    },
    {
        "text": [
            "Check for your number and click 'YES' if present or else 'NO'",
            "",
            "64  65  66  67  68  69  70  71",
            "72  73  74  75  76  77  78  79",
            "80  81  82  83  84  85  86  87",
            "88  89  90  91  92  93  94  95",
            "96  97  98  99  100"
        ],
        "value": 64
    },
    {
        "text": [
            "Check for your number and click 'YES' if present or else 'NO'",
            "",
            "32  33  34  35  36  37  38  39",
            "40  41  42  43  44  45  46  47",
            "48  49  50  51  52  53  54  55",
            "56  57  58  59  60  61  62  63",
            "96  97  98  99  100"
        ],
        "value": 32
    },
    {
        "text": [
            "Check for your number and click 'YES' if present or else 'NO'",
            "",
            "04  05  06  07  12  13  14  15",
            "20  21  22  23  28  29  30  31",
            "36  37  38  39  44  45  46  47",
            "52  53  54  55  60  61  62  63",
            "68  69  70  71  76  77  78  79",
            "84  85  86  87  92  93  94  95",
            "100"
        ],
        "value": 4
    },
    {
        "text": [
            "Check for your number and click 'YES' if present or else 'NO'",
            "",
            "08  09  10  11  12  13  14  15",
            "24  25  26  27  28  29  30  31",
            "40  41  42  43  44  45  46  47",
            "56  57  58  59  60  61  62  63",
            "72  73  74  75  76  77  78  79",
            "88  89  90  91  92  93  94  95"
        ],
        "value": 8
    },
    {
        "text": [
            "Check for your number and click 'YES' if present or else 'NO'",
            "",
            "01  03  05  07  09  11  13  15",
            "17  19  21  23  25  27  29  31",
            "33  35  37  39  41  43  45  47",
            "49  51  53  55  57  59  61  63",
            "65  67  69  71  73  75  77  79",
            "81  83  85  87  89  91  93  95",
            "97  99"
        ],
        "value": 1
    },
    {
        "text": [
            "Hmmm!",
            "That wasn't hard at all :) ",
            "Click REVEAL to see your chosen number"
        ],
        "button": "REVEAL >>"
    }
]

# App UI
st.title("🔍 Num Sherlock")

# Step 0: Intro
if st.session_state.c == 0:
    for line in sets[0]['text']:
        st.write(line)
    if st.button(sets[0]['button']):
        st.session_state.c += 1

# Steps 1–7: YES/NO selections
elif 1 <= st.session_state.c <= 7:
    stage = sets[st.session_state.c]
    for line in stage['text']:
        st.write(line)
    col1, col2 = st.columns(2)
    if col1.button("YES", key=f"yes_{st.session_state.c}"):
        st.session_state.sum += stage['value']
        st.session_state.c += 1
    if col2.button("NO", key=f"no_{st.session_state.c}"):
        st.session_state.c += 1

# Step 8: Reveal prompt
elif st.session_state.c == 8:
    for line in sets[8]['text']:
        st.write(line)
    if st.button(sets[8]['button']):
        st.session_state.c += 1

# Step 9: Final reveal
else:
    st.header("Your chosen number is:")
    st.success(f"{st.session_state.sum}")
    st.write("Isn't it?")
    st.write("Thank you 😊")

    # Optionally add restart
    if st.button("Play Again"):
        st.session_state.c = 0
        st.session_state.sum = 0
