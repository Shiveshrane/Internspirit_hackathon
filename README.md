---
title: Churn Prediction API
emoji: 🔮
colorFrom: blue
colorTo: red
sdk: docker
pinned: false
---

# Churn Prediction API

This API provides churn predictions using a machine learning model.

## API Usage

Send POST requests to `/predict` endpoint with customer data in JSON format.

Example request:
```json
{
    "feature1": value1,
    "feature2": value2
}