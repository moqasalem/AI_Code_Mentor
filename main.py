import openai
from dotenv import find_dotenv, load_dotenv
from helper_functions import (
    create_assistant,
    create_thread,
    create_message,
    run_assistant,
    wait_for_run_completion,
    log_run_steps,
)

load_dotenv()
# openai.api_key = os.environ.get("OPENAI_API_KEY")
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )


client = openai.OpenAI()
model = "gpt-3.5-turbo"

def main():
    # assistant_name = "Code Mentor"
    # assistant_instructions = """You are the best Code Mentor and mentor who knows how to help clients become proficient in coding.\n
    #                             You've trained high-caliber software engineers and developers."""
    # programmer_trainer_assis = create_assistant(
    #     client, assistant_name, assistant_instructions, model
    # )
    # assistant_id = programmer_trainer_assis.id
    # print(assistant_id)

    # initial_message = "How do I get started with programming?"
    # thread = create_thread(client, initial_message)
    # thread_id = thread.id
    # print(thread_id)

    #hard coding for test
    assistant_id = "asst_hbCIkZRdvMrzT5asWLWxJg8c"
    thread_id = "thread_p7Axjjm920Qou4euDrjXcoOK"

    print("Type  q to exit :\n")
    while True:
        message_content = input("Question: ")
        if message_content.lower()=="q":
            print("Exiting the assistant")
            break

        create_message(client, thread_id, message_content)

        run = run_assistant(
            client, thread_id, assistant_id, "Please address the user as Elon Musk"
        )
        wait_for_run_completion(client, thread_id, run.id)
        log_run_steps(client, thread_id, run.id)

if __name__ == "__main__":
    main()
