#!/usr/bin/env python
from crewai_read_email.crew import ReadEmailCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'request': 'Could you list my last emails?'
    }
    ReadEmailCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
