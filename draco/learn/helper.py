'''
Helper functions for learning algorithm.
'''

import json
import os
from typing import Dict

import numpy as np

from draco.run import run
from draco.spec import Task


def current_weights() -> Dict:
    ''' Get the current weights as a dictionary. '''
    with open(os.path.join(os.path.dirname(__file__), '../../data/weights.json')) as f:
        return json.load(f)

def compute_cost(violations: Dict) -> int:
    weights = current_weights()
    c = 0
    for k,v in violations.items():
        c += v * weights[f'{k}_weight']
    return c

def compute_violation_costs(violations: Dict) -> Dict:
    result = {}

    weights = current_weights()
    for k, v in violations.items():
        result[k] = (v, weights[f'{k}_weight'])

    return result

def count_violations(task: Task, debug=False) -> Dict[str, int]:
    ''' Get a dictionary of violations for a full spec.
        Args:
            task: a task spec object
        Returns:
            a dictionary storing violations of soft rules
    '''
    task = run(task, files=['define.lp', 'soft.lp', 'output.lp'], silence_warnings=True, debug=debug)
    return task.violations


def contingency_table(labels_1: np.array, labels_2: np.array) -> np.array:
    '''
    Compute a contingency table for two arrays of booleans.
    '''
    return [[np.sum(labels_1), len(labels_1) - np.sum(labels_1)],
            [np.sum(labels_2), len(labels_2) - np.sum(labels_2)]]
