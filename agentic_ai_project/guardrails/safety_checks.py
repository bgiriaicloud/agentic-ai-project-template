from typing import List

class SafetyGuardrails:
    forbidden_terms: List[str] = ["hack", "exploit", "malware", "illegal"]

    @classmethod
    def check_input(cls, text: str) -> bool:
        """Checks if input contains forbidden terms. Returns True if safe."""
        lower_text = text.lower()
        for term in cls.forbidden_terms:
            if term in lower_text:
                return False
        return True

    @classmethod
    def check_output(cls, text: str) -> bool:
        """Checks if output is safe. Returns True if safe."""
        # Simple placeholder logic
        return cls.check_input(text)
