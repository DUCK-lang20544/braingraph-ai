import streamlit as st
import google.generativeai as genai
from PIL import Image
import networkx as nx
from pyvis.network import Network
from gtts import gTTS
import tempfile
import json

# Gemini API setup
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🧠 BrainGraph AI")
st.write("Upload your study notes and convert them into graphs, quizzes, flashcards and explanations.")

uploaded_file = st.file_uploader("Upload Notes Image")

def generate_ai_content(image):

    prompt = """
    Analyze the study notes image and return structured JSON with:
    main_topic
    subtopics (list)
    quiz (5 MCQ with question, options, answer, explanation)
    flashcards (front, back)
    explanation (short explanation)
    """

    response = model.generate_content([prompt, image])
    return response.text


def create_graph(main_topic, subtopics):

    G = nx.Graph()
    G.add_node(main_topic)

    for s in subtopics:
        G.add_node(s)
        G.add_edge(main_topic, s)

    net = Network(height="400px", width="100%")

    for node in G.nodes:
        net.add_node(node)

    for edge in G.edges:
        net.add_edge(edge[0], edge[1])

    path = tempfile.NamedTemporaryFile(delete=False, suffix=".html").name
    net.save_graph(path)

    return path


if uploaded_file:

    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("Generate BrainGraph"):

        with st.spinner("AI is analyzing notes..."):

            result = generate_ai_content(image)

        st.subheader("AI Output")
        st.write(result)

        # Try JSON parsing
        try:
            data = json.loads(result)

            main_topic = data["main_topic"]
            subtopics = data["subtopics"]

            st.subheader("📊 BrainGraph")

            graph_file = create_graph(main_topic, subtopics)

            with open(graph_file, "r", encoding="utf-8") as f:
                html = f.read()

            st.components.v1.html(html, height=450)

            st.subheader("❓ Quiz")

            for q in data["quiz"]:
                st.write("**Q:**", q["question"])
                for opt in q["options"]:
                    st.write("-", opt)
                st.write("Answer:", q["answer"])
                st.write("Explanation:", q["explanation"])
                st.write("---")

            st.subheader("🃏 Flashcards")

            for f in data["flashcards"]:
                st.write("Front:", f["front"])
                st.write("Back:", f["back"])
                st.write("---")

            st.subheader("🔊 Voice Explanation")

            text = data["explanation"]
            tts = gTTS(text)

            audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(audio_file.name)

            st.audio(audio_file.name)

            st.subheader("📅 Study Plan")

            st.write("Day 1: Overview of topic")
            st.write("Day 2: Study subtopics")
            st.write("Day 3: Practice quiz")
            st.write("Day 4: Revision")

        except:
            st.warning("AI output not in JSON format. Showing raw output.")
