#!/usr/bin/python3
import openai
import requests
log = True
special_start="<?"
special_end="?>"

def send_message(request, log = False):
    """
    This function takes in a request and sends it and returns the response

    Args:
        request (string): The message to be sent
        log (boolean): If the message should be logged

    Returns:
        string: the response
    """
    # TODO: use the saved logs for responses
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": request}])
    content = chat_completion.choices[0].message.content

    if log:
        with open("log.txt", "a") as f:
            f.write(str({request: dict(chat_completion)}) + "\n")

    return content

def convert_commands_to_text(line):
    """
    This function converts special commands and returns their text

    Args:
        line (string): line to be converted

    Returns:
        string: the response
    """
    try:
        start=line.index(special_start)
        end=line.index(special_end)
    except (ValueError):
        return line
    
    command=line[start+len(special_start):end]
    # print(f'the command before the url is {command}')
    if command[:4] == "url=":
        # print(f'the command in the if is {command}')
        command = requests.get(command[4:]).text
        # print(f'the html code type is {type(command)}')

    return convert_commands_to_text(line[:start] + command + line[end+len(special_end):])

if __name__ == '__main__':
    print("STARTING REPL...")
    print("================")
    line = convert_commands_to_text(input())
    if line == "list models":
        models = openai.Model.list()
        print(models)
        print(models.data)
    else:
        while line != "quit":
            
            content = send_message(line, log)
            print(content)

            next_line = convert_commands_to_text(input())
            if next_line != "quit":
                line = line + ';' + content + ';' + next_line
            else:
                line = next_line
