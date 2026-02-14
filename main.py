from fastapi import FastAPI
from models.schemas import QueryRequest

from agents.response_agent import generate_response
from agents.claim_extractor import extract_claims
from agents.verification_agent import verify_claims
from agents.scoring_agent import calculate_risk
from agents.correction_agent import regenerate_response
from agents.monitoring_agent import log_request
from agents.analytics_agent import calculate_stats

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Hallucination Guard Running"}


@app.post("/ask")
def ask_question(request: QueryRequest):

    user_query = request.query

    # 1️⃣ Generate draft response
    draft_response = generate_response(user_query)

    # 2️⃣ Extract claims
    extracted_claims = extract_claims(draft_response)

    # 3️⃣ Verify claims
    verification_results = verify_claims(extracted_claims)

    # 4️⃣ Calculate risk
    risk_analysis = calculate_risk(verification_results)

    response_data = {
        "user_query": user_query,
        "draft_response": draft_response,
        "extracted_claims": extracted_claims,
        "verification_results": verification_results,
        "risk_analysis": risk_analysis
    }

    # 5️⃣ Trigger correction if Medium or High risk
    if risk_analysis["risk_level"] in ["Medium", "High"]:
        corrected_response = regenerate_response(
            user_query,
            verification_results
        )
        response_data["corrected_response"] = corrected_response

    # 6️⃣ Log request for monitoring
    log_request(response_data)

    return response_data


@app.get("/stats")
def get_stats():
    return calculate_stats()
