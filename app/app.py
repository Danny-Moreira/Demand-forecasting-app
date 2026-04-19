import gradio as gr
import pandas as pd
import joblib

model = joblib.load("model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

def predict(price, discount, inventory_level, promotion, competitor_pricing, category):
    input_data = pd.DataFrame({
        "Price": [price],
        "Discount": [discount],
        "Inventory Level": [inventory_level],
        "Promotion": [promotion],
        "Competitor Pricing": [competitor_pricing],
        "Category": [category]
    })

    for col, encoder in label_encoders.items():
        if col in input_data.columns:
            input_data[col] = encoder.transform(input_data[col])

    return int(model.predict(input_data)[0])

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(value=50, label="Price"),
        gr.Number(value=10, label="Discount (%)"),
        gr.Number(value=100, label="Inventory Level"),
        gr.Dropdown([0,1], label="Promotion"),
        gr.Number(value=50, label="Competitor Pricing"),
        gr.Dropdown(
            label_encoders["Category"].classes_.tolist(),
            label="Category"
        ),
    ],
    outputs=gr.Number(label="Predicted Demand"),
    title="Demand Forecasting App"
)

demo.launch()
