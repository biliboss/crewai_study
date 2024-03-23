#!/usr/bin/env python
from crewai_study.crew import CrewaiStudyCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    CrewaiStudyCrew().crew().kickoff(inputs=inputs)