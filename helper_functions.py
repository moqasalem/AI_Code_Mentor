import openai
import time
import logging


def create_assistant(client, name, instructions, model):
    assistant = client.beta.assistants.create(
        name=name,
        instructions=instructions,
        model=model
    )
    return assistant

def create_thread(client, initial_message):
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": initial_message,
            }
        ]
    )
    return thread

def create_message(client, thread_id, content):
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content
    )

def run_assistant(client, thread_id, assistant_id, instructions):
    return client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions=instructions
    )

def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"Run completed in {formatted_elapsed_time}")

                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"AI answer: {response}")
                break
        except Exception as e:
            logging.error(f"An error occurred while retrieving the run: {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)

def log_run_steps(client, thread_id, run_id):
    run_steps = client.beta.threads.runs.steps.list(thread_id=thread_id, run_id=run_id)
    print(f"Steps---> {run_steps.data[0]}")
