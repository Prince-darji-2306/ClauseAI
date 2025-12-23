import os
import json
from llama_index.core.llms import MockLLM

def get_query_engine(results):
    tools = []
    contracts = []

    for i, (index, filename) in enumerate(results):
        contracts.append(os.path.splitext(os.path.basename(filename))[0])

        query_engine = index.as_query_engine(
            similarity_top_k=5,
            llm= MockLLM()
        )

        tools.append(query_engine)

    return tools, contracts

def query_routing(llm, query, tdocs):

    ans = llm.complete(f'''
        User query: {query} \n Total documents : {tdocs} \n
        Rules:
        - If the query is casual, greeting, or answerable without documents → return [].
        - Select documents number ONLY if required to answer (e.g [1,2]).
        - If unsure → return [[], ''].

        Return ONLY valid JSON:
        [[doc_numbers], "General vector query for single documents"].

        Do not give anything extra not a word'''
    ).text
    ans = json.loads(ans)

    return ans 