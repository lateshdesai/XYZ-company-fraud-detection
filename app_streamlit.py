import streamlit as st
from src.predict import predict_fraud_by_transaction_id

st.title("XYZ Fraud Detection - Transaction ID Mode (D Drive)")

transaction_id = st.text_input("Enter transaction_id")

if st.button("Predict Fraud"):

    if transaction_id.strip() == "":
        st.warning("Please enter a valid transaction_id")
    else:
        result = predict_fraud_by_transaction_id(transaction_id)

        if "error" in result:
            st.error(result["error"])
        else:
            st.success("Prediction Completed")

            # Convert numeric to Yes/No
            fraud_label = "Yes" if result["is_fraud_prediction"] == 1 else "No"

            st.write("Transaction ID:", result["transaction_id"])
            st.write("Fraud Prediction:", fraud_label)
            st.write("Fraud Probability:", round(result["fraud_probability"], 4))