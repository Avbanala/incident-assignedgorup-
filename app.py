{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff73ce93",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "\n",
    "import streamlit as st\n",
    "\n",
    "st.beta_set_page_config(page_title='AM', page_icon=None, layout='centered', initial_sidebar_state='auto')\n",
    "\n",
    "# To hide hamburger (top right corner) and “Made with Streamlit” footer\n",
    "hide_streamlit_style = \"\"\"\n",
    "            <style>\n",
    "            #MainMenu {visibility: hidden;}\n",
    "            footer {visibility: hidden;}\n",
    "            </style>\n",
    "            \"\"\"\n",
    "st.markdown(hide_streamlit_style, unsafe_allow_html=True)\n",
    "\n",
    "# load the model from disk\n",
    "clf = pickle.load(open('clf.pkl', 'rb'))\n",
    "cv = pickle.load(open('cv.pkl', 'rb'))\n",
    "le = pickle.load(open('le.pkl', 'rb'))\n",
    "\n",
    "\n",
    "def predict(description):\n",
    "    prediction = clf.predict(cv.transform(description))\n",
    "    return le.inverse_transform(prediction)[0]\n",
    "\n",
    "\n",
    "def main():\n",
    "    st.title(\"Assignment group prediction for tickets\")\n",
    "    st.markdown(\"#### Enter ticket description below\")\n",
    "    description = st.text_area(\"Description\")\n",
    "    if st.button(\"Predict\"):\n",
    "        text = [description]\n",
    "        assignment_group = predict(text)\n",
    "        st.write(\"### Assignment group: \")\n",
    "        st.success(assignment_group)\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
