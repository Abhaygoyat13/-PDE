import json

class Intent:
    def _init_(self, action, domain, depth_level, max_problems, metrics=None):
        self.action = action
        self.domain = domain
        self.depth_level = depth_level
        self.max_problems = max_problems
        self.metrics = metrics or []

    def to_dict(self):
        return {
            "action": self.action,
            "domain": self.domain,
            "depth_level": self.depth_level,
            "max_problems": self.max_problems,
            "metrics": self.metrics
        }
