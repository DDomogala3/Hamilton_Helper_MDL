import streamlit as st

# Title of the app
st.title("Hamilton Error Handling")
st.markdown("Welcome to the Hamilton Error Handling Tool. Follow the steps below to resolve issues.")

# Step 1: Is there an error on your Hamilton?
step_one_input = st.radio("Is there an error on your Hamilton?", ["Yes", "No"], index=1)

if step_one_input == "Yes":
    # Step 2: Is this an emergency?
    emergency = st.radio("Is this an emergency? Is this occurring mid-run?", ["Yes", "No"], index=1)

    if emergency == "Yes":
        st.error("🚨 Emergency Detected!")
        st.write("""
            **Immediate Actions:**
            1. Call The Automation Team.
            2. Record error log.
            3. Save trace files.
            4. Email MDL Automation and Liquidbiopsy Mole.
        """)
    else:
        # Step 3: Is this a hardware issue?
        hardware_issue = st.radio("Is this a hardware issue?", ["Yes", "No"], index=1)

        if hardware_issue == "Yes":
            st.warning("⚠️ Hardware Issue Detected!")
            st.write("""
                **Actions for Hardware Issues:**
                1. Call The Automation Team.
                2. Record error log.
                3. Save trace files.
                4. Email MDL Automation and Liquidbiopsy Mole.
            """)
        else:
            st.info("ℹ️ Non-Hardware Issue Detected!")
            st.write("""
                **General Actions:**
                1. Call The Automation Team.
                2. Record error log.
                3. Save trace files.
                4. Email MDL Automation and Liquidbiopsy Mole.
            """)

elif step_one_input == "No":
    st.success("✅ No errors detected. Your Hamilton is running smoothly!")

# Footer
st.markdown("---")
st.markdown("Created by [Your Name] | For support, contact the Automation Team.")
