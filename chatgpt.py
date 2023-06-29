#!/usr/bin/python3
import openai
log = True

if __name__ == '__main__':
    print("STARTING REPL...")
    print("================")
    line = input()
    if line == "list models":
        models = openai.Model.list()
        print(models)
        print(models.data)
    else:
        while line != "quit":
            with open("log.txt", "a") as f:
                chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": line}])
                content = chat_completion.choices[0].message.content
                print(content)

                if log:
                    f.write(str({line: dict(chat_completion)}) + "\n")

                next_line = input()
                if next_line != "quit":
                    line = line + ';' + content + ';' + next_line
                else:
                    line = next_line
