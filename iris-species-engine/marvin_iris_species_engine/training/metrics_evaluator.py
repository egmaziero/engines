#!/usr/bin/env python
# coding=utf-8

"""MetricsEvaluator engine action.

Use this module to add the project main code.
"""
from sklearn import metrics as sk_metrics

from .._compatibility import six
from .._logging import get_logger

from marvin_python_toolbox.engine_base import EngineBaseTraining

__all__ = ['MetricsEvaluator']


logger = get_logger('metrics_evaluator')


class MetricsEvaluator(EngineBaseTraining):

    def __init__(self, **kwargs):
        super(MetricsEvaluator, self).__init__(**kwargs)

    def execute(self, **kwargs):
        _metrics = {}

        for m in self.model.keys():
            dataset_key = m.split("_")[-1]

            _test_X = self.dataset[dataset_key]['test_X']
            _test_y = self.dataset[dataset_key]['test_y']

            self.model[m].predict(_test_X)
            prediction = self.model[m].predict(_test_X)
            _metrics[m] = sk_metrics.accuracy_score(prediction, _test_y)

        _metrics = sorted(_metrics.iteritems(), key=lambda (k, v): (v, k), reverse=True)

        self.metrics = {
            "best_model": _metrics[0],
            "all_metrics": _metrics
        }
