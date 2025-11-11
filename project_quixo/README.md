# Grading

Grading is done solely by whether your function's output matches exactly given an output.
Just because your code *works* to have a functioning Quixo game does not mean that you will score.
It **must** fulfil the specifications of each function, i.e. following the function name, inputs (order and data types), and outputs (order and data types).

For those familiar, this is similar to LeetCode and other sites that have automated testing.

[quixo_function_specs.pdf](./quixo_function_specs.pdf) spells out exactly the requirements for each function, and is just a condensed form of the original pdf.
It *must* pass a test to score for that test.

**The tests must run without any user intervention.**

# Extra tests

I do not guarantee the correctness of all the tests (or my code), though it has been generally tested against other code online.

Some extra tests are provided in [quixo_tests.py](./quixo_tests.py) and [quixo_tests_computer_move.py](./quixo_tests_computer_move.py)
You can see the test generation process in [quixo_test_gen.py](./quixo_test_gen.py) if you are curious.

Passing all of them is a good indication that you have done the functions correctly.

**The test file must run without any user intervention.**

# Submitting

You only need to submit the `quixo.py` file, and nothing else, in a zip file.

You can just create the zip file yourself, but a [script](./quixo_project_zipper.py) has been created to help in the creation of the zip file for submission.
Just run the script and follow the prompts.
If it is unclear, you can let me know.
