
import os
from openai import OpenAI

#set open api key
os.environ["OPENAI_API_KEY"]="api-key"

#read tasks from file
# make call to open ai to categorize our tasks
def read_tasks(filepath):
    with open(filepath, "r") as f:
        return f.read()


client = OpenAI()


def summarize_Tasks(tasks):
    prompt = f"""
        You are a smart task planning agent. 
        Given a list of tasks, categorize them into 3 priorities:
        High, Medium, and Low.

        Tasks:
        {tasks}

        Return the response in this format:

        High Priority:
        - Task 1
        - Task 4

        Medium Priority:
        - Task 2
        - Task 5

        Low Priority:
        - Task 3
        """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    tasks = read_tasks("task.txt")
    summary = summarize_Tasks(tasks)
    print("-" * 30)
    print(summary)


