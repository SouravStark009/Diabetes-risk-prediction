from app.about import app as about_app
from app.perm_importance import app as perm_importance_app
from app.performance import app as performance_app
from app.explainer import app as explainer_app
from app.predict import app as predict_app
from app.input import app as input_app
from app.header import app as header_app
from function.function import *
import streamlit as st
from loader import page_icon


st.set_page_config(
    page_title="Diabetes Prediction with AI",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
header_app()

# Inputs
input_data = input_app()

# Prediction
predict_app(input_data)

# Explain
explainer_app(input_data)

# Model performance
performance_app()

# perm_importance
perm_importance_app()

# About
about_app()