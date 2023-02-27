# Adapted from Prompt-aided Language Models [PAL](https://arxiv.org/pdf/2211.10435.pdf).

from minichain import Prompt, TemplatePrompt, show_log, start_chain


class PalPrompt(TemplatePrompt):
    template_file = "pal.pmpt.tpl"


class PyPrompt(Prompt):
    def prompt(self, inp):
        return inp + "\nprint(solution())"

    def parse(self, response, inp):
        return int(response)


with start_chain("pal") as backend:
    question = "Melanie is a door-to-door saleswoman. She sold a third of her ' \
    'vacuum cleaners at the green house, 2 more to the red house, and half of ' \
    'what was left at the orange house. If Melanie has 5 vacuum cleaners left, ' \
    'how many did she start with?'"
    prompt = PalPrompt(backend.OpenAI()).chain(PyPrompt(backend.Python()))
    result = prompt({"question": question})
    print(result)


# + tags=["hide_inp"]
PalPrompt().show(
    {"question": "Joe has 10 cars and Bobby has 12. How many do they have together?"},
    "def solution():\n\treturn 10 + 12",
)
# -

# + tags=["hide_inp"]
PyPrompt().show("def solution():\n\treturn 10 + 12", "22")
# -

show_log("pal.log")
