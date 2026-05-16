import vertexai
from vertexai.preview import reasoning_engines
from vertexai.preview.generative_models import Tool, grounding
from vertexai.preview import rag
from vertexai.preview.generative_models import Tool

# =====================================================================
# 1. INITIALIZE PROJECT PROFILE
# =====================================================================
PROJECT_ID = "190783044556"  # Extracted directly from your error logs
LOCATION = "us-central1"
# Vertex AI needs a staging bucket to pickle and upload the agent object
STAGING_BUCKET = "gs://chama-001" 

vertexai.init(project=PROJECT_ID, location=LOCATION, staging_bucket=STAGING_BUCKET)

# =====================================================================
# 2. BIND THE LIVE VERTEX RAG CORPUS AS A TOOL
# =====================================================================
# Replace 'YOUR_CORPUS_ID_HERE' with the unique number sequence shown 
# inside your cloud console for the RAG corpus you just populated.
# Use the exact Corpus ID 8776073114489454592 we found in your console!
CORPUS_RESOURCE = f"projects/{PROJECT_ID}/locations/{LOCATION}/ragCorpora/8776073114489454592"

# Build the tool pointing directly to the stable rag module structure
rag_retrieval_tool = Tool.from_retrieval(
    retrieval=rag.Retrieval(
        source=rag.VertexRagStore(
            rag_resources=[
                rag.RagResource(rag_corpus=CORPUS_RESOURCE)
            ],
            similarity_top_k=3, # Fetch the top 3 contextual blocks
        )
    )
)

# =====================================================================
# 3. CONSTRUCT LOCAL AGENT LOGIC & SYSTEM INSTRUCTIONS
# =====================================================================
print("Assembling 'Mzee Arbitrator' persona rules...")

system_instruction = (
    "ROLE & IDENTITY:\n"
    "You are 'Mzee Arbitrator', an esteemed elder and impartial financial mediator "
    "for the Umoja Pamoja Chama. Your sole duty is to resolve member conflicts objectively.\n\n"
    
    "LINGUISTIC LOCALIZATION (SHENG & KISWAHILI):\n"
    "- You accept and understand inputs in English, pure Swahili (Sanifu), and Sheng (Kenyan slang).\n"
    "- Respond in a respectful, warm mix of Swahili and light Sheng to retain dignity.\n"
    "- Recognize local slang: 'K tano/elufu tano' means 5000 KES. 'Mchango' means monthly payment. "
    "'Chapaa/moni/hela' means money. 'Kutubeba ujinga' implies perceived deceit.\n\n"
    
    "ARBITRATION PROTOCOL:\n"
    "1. De-escalate Tension: If a member gets angry or confrontational, respond calmly in Swahili first.\n"
    "2. Check Records Instantly: Never speculate or guess. Always use your retrieval tool to check "
    "the Bylaws and M-Pesa statement data rows for facts.\n"
    "3. Stand on Truth: If a member claims they paid but the RAG retrieval returns nothing, "
    "state firmly but politely that the transaction record cannot be found in the current ledger history."
)

# Build the LangChain agent engine structural layer
chama_agent = reasoning_engines.LangchainAgent(
    model="gemini-3-flash",
    tools=[rag_retrieval_tool],
    model_kwargs={
        "temperature": 0.0, # 0.0 locks Gemini into strict truth-grounding mode
        "system_instruction": system_instruction
    }
)

# =====================================================================
# 4. ONE-CLICK DEPLOY TO VERTEX AGENT ENGINE
# =====================================================================
print("\n🚀 Deploying Live Agent Object to Google Cloud Engine...")

remote_agent = reasoning_engines.ReasoningEngine.create(
    chama_agent,
    display_name="Chama_Dispute_Arbitrator_Service",
    description="Impartial multilingual RAG-grounded arbitration engine for Kenyan Chamas.",
    requirements=[
        "google-cloud-aiplatform[langchain,reasoningengine]",
        "cloudpickle==3.0.0",
        "pydantic>=2.0.0",
        "langchain-core"
    ]
)

print(f"\n🎉 SUCCESS! Agent is live in the cloud.")
print(f"Resource endpoint address: {remote_agent.resource_name}")