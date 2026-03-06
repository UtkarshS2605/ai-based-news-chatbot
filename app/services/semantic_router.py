from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

domains = {
    "technology": "technology artificial intelligence machine learning startups software",
    "finance": "finance business economy stock market fintech",
    "sports": "sports football cricket basketball olympics",
    "crypto": "cryptocurrency blockchain bitcoin ethereum web3",
    "health": "health medicine healthcare research vaccine",
    "science": "science research discovery physics biology space",
}

domain_embeddings = {
    key: model.encode(value) for key, value in domains.items()
}


def detect_domain_semantic(query: str):

    query_embedding = model.encode(query)

    scores = {}

    for domain, embedding in domain_embeddings.items():
        similarity = cosine_similarity(
            [query_embedding], [embedding]
        )[0][0]

        scores[domain] = similarity

    best_domain = max(scores, key=scores.get)

    return best_domain