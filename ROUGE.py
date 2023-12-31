# -*- coding: utf-8 -*-
"""source_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zB2kWP8leqZFbBVb6dOz0XkmDnXbgcLh
"""

"""To generate the evaluation scores for each text summarization system, we will use the ROUGE toolkit. The ROUGE-1, ROUGE-2, and ROUGE-L scores will be reported for each of the following text summarization systems: Centroid, DPP, ICSISumm, LexRank, and Submodular.

Experimental Setup:

ROUGE Options:
We will use the following ROUGE options to evaluate the performance of each system:

-n 4: Compute Rouge-n up to max-ngram
-e RELEASE-1.5.5/data: Specify the data folder that comes with ROUGE
-m: Use stemming
-2 -4 -u: Use unigram and skip-bigram with distance up to 4 (aka ROUGE-SU4)
-l 100: Use the first 100 words of the summary for evaluation
-c 95: Confidence level

Python Code for Implementation: """

from pyrouge import Rouge155
import os

def evaluate_summarization_system(system_name, summaries):
    # Initialize the ROUGE evaluator
    rouge = Rouge155()

    # Set ROUGE options
    rouge.system_dir = os.path.join(os.getcwd(), system_name)
    rouge.model_dir = os.path.join(os.getcwd(), "human_summaries")
    rouge.system_filename_pattern = 'text.(\d+).txt'
    rouge.model_filename_pattern = 'human.(\d+).txt'
    rouge.options = ['-n', '4', '-m', '-2', '4', '-u', '-c', '95', '-r', '1000', '-f', 'A', '-p', '0.5', '-t', '0', '-a', '-l', '100']

    # Create system summary directory
    if not os.path.exists(rouge.system_dir):
        os.makedirs(rouge.system_dir)

    # Write summaries to file
    for i, summary in enumerate(summaries):
        with open(os.path.join(rouge.system_dir, f"text.{i}.txt"), "w") as f:
            f.write(summary)

    # Evaluate summaries and get ROUGE scores
    scores = rouge.convert_and_evaluate()
    print(scores)


"""To use this code, i call the evaluate_summarization_system function with the name of the summarization system
and a list of summaries to evaluate. The human summaries is store in  "human_summaries" folder in the current working directory.
The output are  the ROUGE-1, ROUGE-2, and ROUGE-L scores for the system.”””