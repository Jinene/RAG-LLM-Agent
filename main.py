from agent import build_agent


def main():
    agent = build_agent()

    print("RAG Agent Ready! Type 'exit' to quit.")

    while True:
        query = input("\nQuestion: ")
        if query.lower() == "exit":
            break

        result = agent({"query": query})

        print("\nAnswer:", result["result"])


if __name__ == "__main__":
    main()
