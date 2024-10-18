#!/usr/bin/env python
import sys
from andy_swarm.crew import AndySwarmCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'book': 'Animal Farm',
        'prompt': 'How does the author handle the tension between idealism and the harsh realities of corruption and inequality'
    }
    AndySwarmCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "book": "Animal Farm",
        "prompt": "How does the author handle the tension between idealism and the harsh realities of corruption and inequality"
    }
    try:
        AndySwarmCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AndySwarmCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "book": "Animal Farm",
        "prompt": "How does the author handle the tension between idealism and the harsh realities of corruption and inequality"
    }
    try:
        AndySwarmCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
