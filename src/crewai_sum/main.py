#!/usr/bin/env python
from crewai_sum.crew import CrewaiSumCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'n1': '250',
        'n2': '780'
    }
    CrewaiSumCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
