import streamlit as st
import hashlib
import time

st.set_page_config(page_title="Proof of Work Dashboard", layout="centered")
st.title("🔗 Proof of Work Dashboard")

data = st.text_input("Enter Block Data")
difficulty = st.number_input("Enter Difficulty", min_value=1, max_value=6, value=3)


# Styling
st.markdown("""
<style>
.result-box {
    border: 2px solid #4CAF50;
    padding: 20px;
    border-radius: 12px;
    background-color: #0e1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)


if st.button("Start Mining 🚀"):
    if data:

        target = "0" * difficulty
        nonce = 0

        st.write("⛏️ Mining in progress...")

        # Placeholders for live updates
        nonce_placeholder = st.empty()
        hash_placeholder = st.empty()

        start_time = time.time()

        while True:
            text = data + str(nonce)
            hash_result = hashlib.sha256(text.encode()).hexdigest()

            # 🔥 Update UI every 100 iterations (for performance)
            if nonce % 100 == 0:
                nonce_placeholder.write(f"🔢 Trying Nonce: {nonce}")
                hash_placeholder.write(f"🔐 Hash: {hash_result[:25]}...")

                time.sleep(0.01)  # smooth animation

            if hash_result.startswith(target):
                break

            nonce += 1

        end_time = time.time()

        st.success("✅ Block Mined Successfully!")
        st.divider()

        # Final Result Box
        st.markdown(f"""
        <div class="result-box">
        <h3>📊 Results</h3>
        <p><b>Block Data:</b> {data}</p>
        <p><b>Difficulty:</b> {'0'*difficulty}</p>
        <p><b>Nonce Found:</b> {nonce}</p>
        <p><b>Final Hash:</b> {hash_result}</p>
        <p><b>Time Taken:</b> {end_time - start_time:.2f} seconds</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter block data")
