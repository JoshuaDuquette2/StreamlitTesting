import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.use("agg")

# -- Set page config
apptitle = 'GW Quickview'
st.set_page_config(page_title=apptitle, page_icon=":eyeglasses:")

# -- Default detector list
detectorlist = ['All', 'Parking Lot 1A']

def get_eventlist():
    return ["All", "Handgun", "Shotgun", "AR", "Submachine Gun", "Person"]
    
st.sidebar.markdown("## Select Model and Inference Mode")

# -- Get list of events
eventlist = get_eventlist()

#-- Set time by GPS or event
select_event = st.sidebar.selectbox('Select Model',
                                    ['YoloV8.pt', 'Other.pt'])

chosen_event = st.sidebar.selectbox('Select Infernce Target', eventlist)
    
#-- Choose detector as H1, L1, or V1
detector = st.sidebar.selectbox('Detector', detectorlist)

# -- Select for high sample rate data
high_fs = st.sidebar.checkbox('Disable Detection?')



# -- Create sidebar for plot controls
st.sidebar.markdown('## Set Model Parameters')
dtboth = st.sidebar.slider('Confidence', 0.1, 1.0, 0.1)

st.sidebar.markdown('#### Other Settings')
whiten = st.sidebar.checkbox('Use Default Parameters?', value=True)
freqrange = st.sidebar.slider('Target Update Rate (ms):', min_value=10, max_value=3000, value=(50,250))