import config
import openai

MODEL = "gpt-3.5-turbo"
SEP_BARS = "--------------"

openai.api_key = config.OPEN_API_KEY

def ask_message():
    print("Hi, I'm ChatGPT. How can I help you?")
    print("\n")
    print(SEP_BARS + " You " + SEP_BARS)
    message = input(">> ")
    print("\n")

    return message

def get_response():
    response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )

    return response

def get_answer(response):
    FINISH_REASON_NOTES = {
        'stop': '',
        'length': '! Imconplete output due to too long input !',
        'content_filter': '! Omitted content due to a flag from our content filters !',
        'null': '! API response still in progress or incomplete !'
    }
    finish_reason, content = response['choices'][0]['finish_reason'], response['choices'][0]['message']['content']
    answer = content if finish_reason == 'stop' else FINISH_REASON_NOTES[finish_reason] + '\n' + content

    return answer

if __name__ == "__main__":
    message = ask_message()
    print(SEP_BARS + " ChatGPT " + SEP_BARS)
    response = get_response()
    answer = get_answer(response)

    print(answer)