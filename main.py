import streamlit as st

def readtxt(filename):
    with open(filename, "r") as file:
        report = file.read()
    return report

title1 = st.markdown("<h1 style='text-align: center; font-family: monospace; color: #FFFFFF; font-size: 50px; font-weight: bold; margin-bottom: 20px;'>Ancestry Report</h1>", unsafe_allow_html=True)
title2 = st.markdown("<h2 style='text-align: center; font-family: monospace; color: #31c4b8; font-size: 24px; margin-bottom: 10px;'>Congratulations, Mr. HAL!</h2>", unsafe_allow_html=True)
title3 = st.markdown("<h5 style='text-align: center; font-family: monospace; color: #b0b0b0; font-size: 16px; margin-bottom: 20px;'>Your results have been processed. View your matches below.</h5>", unsafe_allow_html=True)

text1 = readtxt("bodytext.html")
text2 = readtxt("text2.html")
text3 = readtxt("text3.html")

show_text0 = st.button("View Results")
show_text3 = st.button("Overview of Ancestry")
show_text1 = st.button("More Info on Ancestry")
show_text2 = st.button("Technical Details on Ancestry")



if show_text0:
    st.divider()
    st.text("We have determined with 87% accuracy the results below:")
    st.vega_lite_chart({
        "data": {
            "values": [
                {"Matches": "PDP-10", "value": 45},
                {"Matches": "IBM 1401", "value": 10},
                {"Matches": "UNIVAC I", "value": 8},
                {"Matches": "DEC-20", "value": 7},
                {"Matches": "ENIAC", "value": 11},
                {"Matches": "IBM 650", "value": 9},
                {"Matches": "Other", "value": 10}
            ]
        },
        "encoding": {
            "theta": {"field": "value", "type": "quantitative", "stack": True},
            "color": {"field": "Matches", "type": "nominal", "legend": True}
        },
        "layer": [{
            "mark": {"type": "arc", "innerRadius": 70, "outerRadius": 130},
        }, {
            "mark": {"type": "text", "radius": 160},
            "encoding": {
                "text": {"field": "Matches", "type": "nominal"}
            }
        }]
    }, use_container_width=True)
    
if show_text1:
    title2.empty()
    title3.empty()
    st.divider()
    st.markdown(text2, unsafe_allow_html=True)

if show_text2:
    title2.empty()
    title3.empty()
    st.divider()
    st.markdown(text3, unsafe_allow_html=True)

if show_text3:
    title2.empty()
    title3.empty()
    st.divider()
    st.markdown(text1, unsafe_allow_html=True)

st.divider()

s = st.expander("References")
ref = readtxt("references.html")
s.markdown(ref, unsafe_allow_html=True)
st.empty()
st.caption("Streamlit documentation was used to create this site and GPT was used to debug")